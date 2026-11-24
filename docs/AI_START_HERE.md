# 새 개발 작업 시작

1. [공통 개발 지침](DEVELOPMENT_RULES.md)을 읽습니다. 패키징·배포 작업에서는 [배포 절차](RELEASE_GUIDE.md)도 읽습니다.
2. [프로젝트 목록](PROJECTS.md)에서 해당 프로그램의 상태 문서와 개발 브랜치를 엽니다. 저장소의 AGENTS.md, Git 상태, HEAD, 원격 주소와 관련 설계·검증 기록을 확인합니다.
3. Codex 지시에는 목표, 보존할 기능과 데이터, 변경 관련 검증, 배포 승인 경계, 완료 시 갱신할 문서를 포함합니다.
4. 결과를 실제 커밋, 시험 증거, 운영 아티팩트와 비교합니다. 상태 문서가 다르면 확인한 코드·Git·서명 배포 근거에 맞게 문서를 바로잡습니다. 확인된 사실, 기존 보고서와 미검증 상태를 구분합니다.

작업을 시작할 때 [프로젝트 간 협업 규칙](COLLABORATION.md)의 프로젝트 라벨에서 현재 프로젝트의 열린 안건만 확인합니다.

## 공개 허브 열기

Codex와 웹 ChatGPT는 로그인 없이 GitHub에서 문서를 읽을 수 있습니다. GitHub 화면을 불러올 수 없다면 [Markdown 원문](https://raw.githubusercontent.com/rodetoast/southpaw-development-hub/main/docs/AI_START_HERE.md)이나 공개 Git clone을 사용합니다.

```shell
curl https://raw.githubusercontent.com/rodetoast/southpaw-development-hub/main/docs/AI_START_HERE.md
```

AGENTS.md는 읽기 절차의 진입점입니다. 링크를 적는 것만으로 원격 문서가 자동 로드되지는 않습니다. 접근이 실패하면 읽지 못한 범위를 남기고 접근 가능한 지침으로 진행합니다.

웹 ChatGPT에서 기획·UX·개발 결과를 검토할 때 이 페이지를 공통 시작 링크로 전달합니다. 공개 문서 열람에는 GitHub 계정 연결이 필요 없습니다. 웹 열람이 제한되면 [통합 참조 파일](../SOUTHPAW_AI_CONTEXT.md)을 웹 ChatGPT 프로젝트에 업로드합니다. 파일의 기준 커밋과 확인일을 보고 검토 범위를 판단합니다. GitHub에 변경을 올리려면 기존 쓰기 권한이 필요합니다.

UI나 시각적 기능을 검토할 때는 [시각 자료 공유 규칙](DEVELOPMENT_RULES.md#디자인-시안과-구현-검토-자료)을 따릅니다. 공개 GitHub 갤러리와 커밋 고정 자료를 열 수 있으면 이를 직접 참조합니다. 웹 ChatGPT에서 이미지 접근이 실패하면 사용자가 필요한 이미지만 프로젝트 공통 소스나 해당 대화에 첨부합니다. GPT에서 만든 시안을 사용자가 파일로 전달하면 Codex는 해당 저장소에 참고 자료로 기록할 수 있습니다. 이 과정은 첨부 파일 전달을 통해 이뤄집니다.

## 완료 시 기록

의미 있는 변경은 소스 저장소 `docs/PROJECT_STATUS.md`를 먼저 갱신하고, 같은 작업에서 허브의 프로젝트 요약과 목록도 영향받는 범위만 갱신합니다. 상세 근거는 프로젝트 저장소에 남깁니다. 중앙 쓰기 권한이 없으면 패치를 준비하고 동기화 대기라고 보고합니다. 작업을 수행하는 Codex가 실행하는 절차이며 백그라운드 동기화는 없습니다.
