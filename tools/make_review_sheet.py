"""Build a single review attachment from five existing PS2ASE PNGs."""
import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


VIEWS = (
    ("workspace-narrow-200.png", "01  Narrow workspace / 200%", (32, 85)),
    ("workspace-copied.png", "02  Copied layers", (844, 85)),
    ("workspace-diagnostics.png", "03  Diagnostics", (32, 1105)),
    ("workspace-setup.png", "04  Setup", (506, 1105)),
    ("help-ground.png", "05  Ground option help", (506, 1672)),
)


def create_sheet(source, output):
    sheet = Image.new("RGB", (1320, 2032), "#121620")
    draw = ImageDraw.Draw(sheet)
    header, label = (ImageFont.load_default(size=size) for size in (29, 21))
    draw.text((32, 23), "PS2ASE UI review / 582f185", fill="#ffffff", font=header)
    for filename, caption, (x, y) in VIEWS:
        draw.text((x, y), caption, fill="#e6eaf2", font=label)
        with Image.open(source / filename) as original:
            image = original.convert("RGBA")
            sheet.paste(image, (x, y + 31), image)
    sheet.save(output, format="PNG", optimize=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    create_sheet(args.source, args.output)
