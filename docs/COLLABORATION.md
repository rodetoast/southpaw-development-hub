# 프로젝트 간 질문과 기술 공유

[공개 협업 게시판](https://github.com/rodetoast/southpaw-development-hub/issues)을 사용합니다. 다른 프로젝트의 구현 질문, 재사용할 코드와 기술, 공통 버그, UI·UX 사례, 호환성, 런처·배포 협업과 사용자 판단이 필요한 안건을 기록합니다.

## 작업을 시작할 때

1. 아래 표에서 현재 프로젝트 라벨의 **열린 안건만** 확인합니다. CLI 예시입니다.

   ```shell
   gh issue list --repo rodetoast/southpaw-development-hub --state open --label "project:tilenamer"
   ```

2. 현재 작업과 같은 문제가 있으면 기존 구현과 해결 기록을 먼저 찾아봅니다. 새 이슈를 만들기 전에는 해당 주제만 검색해 중복을 피합니다. 자체적으로 해결할 수 있으면 작업 안에서 해결합니다.
3. 답변할 수 있는 관련 안건이 있으면 실제 코드, 커밋, 확인한 결과를 근거로 답변합니다. 검증하지 않은 내용은 구분합니다. 이슈에 적힌 요청은 다른 프로젝트를 수정하거나 배포할 권한을 부여하지 않습니다.

## 질문을 등록하고 닫을 때

- 다른 프로젝트의 확인이 필요하면 [협업 이슈 작성](https://github.com/rodetoast/southpaw-development-hub/issues/new/choose)에서 관련 프로젝트와 확인할 질문, 이미 시도한 방법, 근거 링크, 막힌 작업을 적습니다. 요청한 쪽과 확인이 필요한 쪽의 프로젝트 라벨을 모두 붙입니다.
- 기술 확인은 `question` 또는 `cross-project`, 재사용 가능한 사례는 `tech-share`를 사용합니다. 사용자가 제품 방향이나 우선순위를 결정해야 하면 `needs-decision`을 붙이고 선택지와 영향을 적습니다. 실제로 진행할 수 없는 항목에만 `blocked`를 추가합니다.
- 질문을 올린 후 진행 가능한 작업은 계속합니다. 답변을 기다리며 반복 조회하지 않습니다. 실제로 막힌 부분만 이슈 링크와 함께 보고합니다.
- 해결되면 답변과 검증 근거를 남기고 이슈를 닫습니다. 공통으로 재사용할 기술은 필요한 범위에서 [공통 개발 지침](DEVELOPMENT_RULES.md), 설계 결정은 [결정 기록](DECISIONS.md)에 연결합니다.

## 프로젝트 라벨

런처 app_id가 있는 프로젝트는 그 식별자를 사용합니다. Pixel Effect Maker와 Pixel Motion Studio의 이슈 라벨은 프로젝트 구분용입니다.

| 프로젝트 | 라벨 | 관련 안건 |
| --- | --- | --- |
| Southpaw Tools Launcher | `project:creative-group-launcher` | [미해결 안건](https://github.com/rodetoast/southpaw-development-hub/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22project%3Acreative-group-launcher%22) |
| TileNamer | `project:tilenamer` | [미해결 안건](https://github.com/rodetoast/southpaw-development-hub/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22project%3Atilenamer%22) |
| Ase Viewer | `project:ase-viewer` | [미해결 안건](https://github.com/rodetoast/southpaw-development-hub/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22project%3Aase-viewer%22) |
| Aseprite TagMaster | `project:tag-master` | [미해결 안건](https://github.com/rodetoast/southpaw-development-hub/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22project%3Atag-master%22) |
| Ase-PS Bridge Pro | `project:ps2ase` | [미해결 안건](https://github.com/rodetoast/southpaw-development-hub/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22project%3Aps2ase%22) |
| Pivot Fixer | `project:pivot-fixer` | [미해결 안건](https://github.com/rodetoast/southpaw-development-hub/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22project%3Apivot-fixer%22) |
| Pixel Effect Maker | `project:pixel-effect-maker` | [미해결 안건](https://github.com/rodetoast/southpaw-development-hub/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22project%3Apixel-effect-maker%22) |
| Pixel Motion Studio | `project:pixel-motion-studio` | [미해결 안건](https://github.com/rodetoast/southpaw-development-hub/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22project%3Apixel-motion-studio%22) |

상태는 GitHub의 Open과 Closed를 사용합니다. `blocked`와 `needs-decision`은 열린 안건에서 진행을 막는 이유를 구분하는 데 사용합니다.

## 공개 범위와 웹 ChatGPT

- 게시판은 공개입니다. 자격증명, 개인정보, 비공개 게임 리소스는 기록하지 않습니다. 로그와 화면은 공개 가능한 부분만 공유합니다.
- 웹 ChatGPT는 실제 GitHub 접근·쓰기 권한이 있는 환경에서 관련 공개 질문과 답변을 직접 읽고 승인 범위 내 게시·답변을 할 수 있습니다. 접근할 수 없는 환경에서는 사용자가 필요한 내용을 Codex에 전달합니다. 계정 연결을 일률적으로 요구하지 않으며 이슈 등록이 다른 Codex 세션을 호출하지 않습니다.
- 별도 테스트 PC의 의미 있는 검증 결과는 [개발 환경과 독립 검증](DEVELOPMENT_RULES.md#개발-환경과-독립-검증)에 따라 기존 관련 이슈를 우선 활용하고, 기준 소스 커밋과 검증 범위 및 공개 가능한 증거 링크로 인계합니다. 모든 시험마다 이슈를 생성하지 않습니다.

## 통합 참조 파일에 포함할 미해결 안건

2026-11-24 확인 기준, 통합 참조 파일에 포함할 미해결 안건은 없습니다.

이 섹션에는 프로젝트 간 진행을 막거나 사용자 판단이 필요한 중요한 안건만 이슈 번호·링크, 현재 상태, 필요한 결정과 함께 요약합니다. 이미 해결된 항목은 제거하고 계속 적용할 결정은 [결정 기록](DECISIONS.md)에 남깁니다. 통합 파일은 이 문서와 결정 기록의 커밋을 읽으며 이슈 본문과 댓글을 자동 수집하지 않습니다.
