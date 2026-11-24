# Ase-PS Bridge Pro

아티스트가 Photoshop과 Aseprite 사이에서 레이어와 프레임을 주고받습니다.

- **구현 범위** 로컬 파일을 통한 레이어 전송과 프레임·정렬 지원
- **운영 버전** 0.3.6
- **후속 UI 소스** `c4f628a`: Photoshop 연결 선택과 선택 버전의 실행 경고 검토를 분리하고, Aseprite 안내 순서와 기본 접힘 진단 패널을 정리했습니다. 자동 115개 통과, [Windows Qt 화면 검토](https://github.com/rodetoast/PS2ASE/blob/c4f628aba74acce7ac428dea3f35215afea3dd59/docs/ui-reviews/setup-ux.md). 기존 0.3.7-rc1 EXE/ZIP에는 미포함입니다.
- **개발 상태** 0.3.7 Windows Onefile 후보 `0.3.7-rc1-74f57bb` 제작 완료. Photoshop 2027 제품명/내부 28.0(실제 JSX 28.0.0)을 구분해 설정 경로를 보완하고 기존 시작·버전 선택·복사·진단·원본 보호 개선을 포함했습니다. 운영은 계속 0.3.6입니다.
- **검증** 자동 113개 통과(skip 0). 실제 2027/Aseprite 1.3.18.6 합성 문서로 세 Copy Mode x 세 정렬, 프레임/row 순서·빈 cel, 양방향 픽셀/알파/좌표를 확인했습니다. 패키징 EXE의 Normal Copy/Preview와 역방향 Paste, 2026/2027 목록 구분·저장 경로 복원도 확인했습니다. 2026 및 이전 호스트 실기동, 기존 GUI F4/F5/최초 Trust 재시험과 모든 PC/DPI는 미검증입니다.
- **후보 소스** `74f57bbf9c01443d1eda6267559762a1088a9236`, 개발 브랜치 `codex/photoshop-2027-candidate-20261124`. 제품명/아이콘/`ps2ase`/`bridge_ui.exe`/설정 위치 유지. [런처 인계·ZIP/EXE 해시](https://github.com/rodetoast/PS2ASE/blob/codex/photoshop-2027-candidate-20261124/docs/RELEASE_0.3.7_HANDOFF.md)
- **다음 단계** 런처 프로젝트에서 후보 ZIP의 설치/업데이트/보존 경로를 검증한 뒤 별도 승인으로 운영 카탈로그 서명·게시합니다. 이번 작업에서 운영 Release/Latest/카탈로그/태그는 바꾸지 않았습니다.
- **확인일** 2026-11-24

[상세 개발 현황](https://github.com/rodetoast/PS2ASE/blob/codex/photoshop-2027-candidate-20261124/docs/PROJECT_STATUS.md) · [소스 저장소](https://github.com/rodetoast/PS2ASE) · [프로젝트 목록](../docs/PROJECTS.md)
