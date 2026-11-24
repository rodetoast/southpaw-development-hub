# Southpaw Games Development Hub

Southpaw Games 내부 제작 도구의 공통 개발 원칙, 프로젝트 진행 상태, 배포와 주요 기술 결정을 확인하는 공개 허브입니다. 문서는 GitHub 로그인 없이 읽을 수 있습니다.

[AI 시작 안내](docs/AI_START_HERE.md) · [공통 개발 지침](docs/DEVELOPMENT_RULES.md) · [배포 절차](docs/RELEASE_GUIDE.md) · [주요 결정](docs/DECISIONS.md)

[협업 게시판](https://github.com/rodetoast/southpaw-development-hub/issues) · [프로젝트 간 질문과 기술 공유 규칙](docs/COLLABORATION.md)

- [Southpaw 도구 런처](projects/launcher.md) · QML 0.2.2, Rod 카탈로그15와 Toast 호환 카탈로그9
- [회사 제작 도구 5개와 Preview 프로젝트](docs/PROJECTS.md) · 운영 버전과 개발 상태
- [Pixel Motion Studio](projects/pixel-motion-studio.md) · 로컬 보존 프로젝트

마지막 확인 2026-11-24. 각 프로젝트 소스 저장소의 상세 상태 문서를 기준으로 중앙 요약을 갱신합니다.

## 웹 접근이 제한된 ChatGPT용 파일

[통합 참조 파일](SOUTHPAW_AI_CONTEXT.md)을 다운로드해 웹 ChatGPT 프로젝트의 공통 참조 파일로 올립니다. GitHub를 열 수 있을 때는 위 원본 문서를 우선합니다.

원본 상태 문서와 허브 요약에 의미 있는 변경을 반영한 뒤 필요할 때 재생성합니다. 프로젝트 상태 커밋은 먼저 공개 개발 브랜치에 push하고, 허브 문서 변경은 먼저 로컬에서 커밋합니다. 허브 루트에서 Python 3.10 이상과 Git으로 다음 명령을 실행합니다.

```shell
python tools/generate_ai_context.py
```

스크립트는 허브의 현재 HEAD와 프로젝트별 공개 상세 상태를 읽어 출처 커밋을 기록합니다. 생성된 파일은 직접 편집하지 않습니다. 재생성 후 공개해도 되는 정보만 포함됐는지 확인하고 파일을 커밋합니다.
