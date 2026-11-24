"""Combine existing screenshots into captioned PNGs without scaling them."""
import argparse
from dataclasses import dataclass
import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


MARGIN = 24
GAP = 24
HEADING_STEP = 34
CAPTION_STEP = 24


@dataclass
class Panel:
    path: Path
    image_size: tuple[int, int]
    captions: list[str]

    @property
    def width(self):
        return max(self.image_size[0], 300)

    @property
    def height(self):
        return len(self.captions) * CAPTION_STEP + 8 + self.image_size[1]


def wrap(text, font, width):
    result = []
    for paragraph in text.splitlines():
        result.append("")
        for word in paragraph.split():
            line = result[-1]
            candidate = f"{line} {word}" if line else word
            if font.getlength(candidate) <= width:
                result[-1] = candidate
                continue
            if line:
                result.append("")
            for char in word:
                if result[-1] and font.getlength(result[-1] + char) > width:
                    result.append("")
                result[-1] += char
    return [line for line in result if line]


def prepare_panels(views, font):
    panels = []
    for number, (filename, title, state) in enumerate(views, 1):
        path = Path(filename)
        with Image.open(path) as image:
            size = image.size
        width = max(size[0], 300)
        captions = wrap(f"{number:02d}. {title}", font, width)
        captions.extend(wrap(state, font, width))
        panels.append(Panel(path, size, captions))
    return panels


def pack_rows(panels, max_width):
    rows = []
    row, width = [], 0
    for panel in panels:
        if row and width + GAP + panel.width > max_width:
            rows.append(row)
            row, width = [], 0
        width += panel.width + (GAP if row else 0)
        row.append(panel)
    if row:
        rows.append(row)
    return rows


def pack_pages(rows, max_height):
    pages = []
    page, height = [], 0
    for row in rows:
        row_height = max(panel.height for panel in row)
        if page and height + GAP + row_height > max_height:
            pages.append(page)
            page, height = [], 0
        height += row_height + (GAP if page else 0)
        page.append(row)
    if page:
        pages.append(page)
    return pages


def render(rows, heading, header_font, label_font):
    width = max(
        480,
        MARGIN * 2 + max(sum(p.width for p in row) + GAP * (len(row) - 1) for row in rows),
    )
    top = MARGIN + len(heading) * HEADING_STEP + GAP
    height = top + sum(max(p.height for p in row) + GAP for row in rows) - GAP + MARGIN
    sheet = Image.new("RGB", (width, height), "#121620")
    draw = ImageDraw.Draw(sheet)
    for index, line in enumerate(heading):
        draw.text((MARGIN, MARGIN + index * HEADING_STEP), line, fill="#ffffff", font=header_font)
    y = top
    for row in rows:
        x = MARGIN
        for panel in row:
            for index, line in enumerate(panel.captions):
                draw.text((x, y + index * CAPTION_STEP), line, fill="#e6eaf2", font=label_font)
            with Image.open(panel.path) as original:
                image = original.convert("RGBA")
                sheet.paste(image, (x, y + len(panel.captions) * CAPTION_STEP + 8), image)
            x += panel.width + GAP
        y += max(p.height for p in row) + GAP
    return sheet


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--title", required=True, help="Project and build or commit")
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--view", required=True, action="append", nargs=3, metavar=("IMAGE", "TITLE", "STATE"))
    parser.add_argument("--max-width", type=int, default=1400)
    parser.add_argument("--max-height", type=int, default=2200)
    parser.add_argument("--font", type=Path, help="Optional font file for captions")
    args = parser.parse_args()
    if args.output.suffix.lower() != ".png" or args.max_width < 480 or args.max_height < 480:
        parser.error("Use a .png output and page limits of at least 480 pixels.")

    font_path = args.font or Path(os.environ.get("WINDIR", "C:/Windows")) / "Fonts" / "malgun.ttf"
    if args.font or font_path.is_file():
        header_font, label_font = (ImageFont.truetype(str(font_path), size) for size in (29, 18))
    else:
        header_font, label_font = (ImageFont.load_default(size=size) for size in (29, 18))

    heading = wrap(args.title, header_font, 480 - MARGIN * 2)
    panels = prepare_panels(args.view, label_font)
    rows = pack_rows(panels, args.max_width - MARGIN * 2)
    pages = pack_pages(rows, args.max_height - MARGIN * 2 - len(heading) * HEADING_STEP - GAP)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    for number, page in enumerate(pages, 1):
        path = args.output
        if len(pages) > 1:
            path = path.with_stem(f"{path.stem}-{number:02d}")
        render(page, heading, header_font, label_font).save(path, format="PNG", optimize=True)
        print(path.resolve())


if __name__ == "__main__":
    main()
