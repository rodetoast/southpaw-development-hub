# 유지하는 개발 결정

| 결정 | 이유와 적용 범위 |
| --- | --- |
| AGENTS.md와 공개 Markdown 허브 | 2026-11-24부터 공개 문서를 웹 ChatGPT와 Codex가 GitHub 연결 없이 읽을 수 있습니다. 문서 변경은 기존 GitHub 쓰기 권한으로 관리합니다. |
| 제품명과 app_id 분리 | 표시 이름이나 브랜드가 달라져도 설치 상태, 영수증과 업데이트 연결을 유지합니다. |
| 운영 기준은 실제 서명 카탈로그 | 개발 소스와 서명 후보를 실제 직원 배포와 구분합니다. Rod와 Toast는 각자의 신뢰 바인딩과 순번을 유지합니다. |
| 기존 직원 업데이트 버튼 유지 | 기존 Toast 설치는 호환 Bridge, Rod 설치는 관리형 Rod 업데이트를 사용합니다. Toast 채널을 유지해 과거 설치도 업데이트에 접근할 수 있게 합니다. |
| QML 화면과 기존 엔진 재사용 | QML은 표현 계층이며 기존 Python 설치·검증과 Bootstrap 실행·복구 계약을 유지합니다. |
| 도구별 UI 프레임워크를 유지하며 런처 시각 토큰 적용 | [PS2ASE 적용 예](https://github.com/rodetoast/PS2ASE/blob/582f185e79ec2a10dee2253bf2cd380960f3bce9/docs/ui-reviews/launcher-system/README.md): 런처 글꼴과 다크 색상을 공유하되, 작업 도구에는 더 조밀한 간격을 적용하고 기존 Widgets와 입력·전송 계약을 유지합니다. 동작 설명 그림은 시안이 아니라 구현을 기준으로 합니다. |

[런처 현황](../projects/launcher.md)
