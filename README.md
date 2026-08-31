# Hearts of Korea 디버깅 문서

이 폴더는 Hearts of Korea 모드의 크래시를 재현하고 원인을 좁히며, 특히 맵 데이터를 현재 Hearts of Iron IV 기준에 맞게 이식할 때 사용할 작업 문서다.

문서 자체는 작업 허가가 아니다. 매 작업을 시작하기 전에 요청이 아래 어느 범위인지 확인한다.

- **Review**: 파일을 읽고 상태와 위험만 보고한다.
- **Diagnostic**: 로그와 데이터를 비교해 원인을 진단한다. 프로덕션 동작은 바꾸지 않으며, 사용자가 별도로 허가한 경우에만 가설을 구분하기 위한 최소·한정 instrumentation을 사용한다.
- **Implementation**: 사용자가 승인한 범위만 수정하고 검증한다.

## 문서 목록

- [크래시 디버깅 런북](docs/CRASH_DEBUGGING_RUNBOOK.md): 재현부터 원인 격리까지의 표준 절차
- [증거 기록 양식](docs/EVIDENCE_RECORD_TEMPLATE.md): 실행별 로그와 가설을 섞지 않고 기록하는 양식
- [맵 호환성 점검표](docs/MAP_COMPATIBILITY_CHECKLIST.md): 맵 데이터 이식 전후의 필수 검사
- [검증 점검표](docs/VALIDATION_CHECKLIST.md): 수정 승인 후 완료 판정 기준
- [2026-08-31 시작 크래시 조사](docs/incidents/2026-08-31-startup-crash.md): 현재 확인된 사실과 남은 가설

## 고정 안전 원칙

1. `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`의 게임 원본과 Workshop 모드는 읽기 전용 기준 자료로 취급한다.
2. 로그, 크래시 덤프, 세이브, 런처 사용자 데이터는 증거다. 사용자의 별도 승인 없이 수정·이동·삭제하지 않는다.
3. 목표 버전의 바닐라 파일을 기준으로 삼고, 구버전 파일 전체를 복사해 덮지 않는다.
4. 모드의 의도, 이벤트·포커스 ID, 밸런스, 명칭은 호환성 수정에 필요한 경우가 아니면 변경하지 않는다.
5. 맵 ID 변경은 세이브·스크립트·서브모드와의 호환성을 깨뜨릴 수 있다. 명시적인 마이그레이션 승인 전에는 실행하지 않는다.
6. 숫자는 문맥 없이 일괄 치환하지 않는다. 같은 숫자가 state, province, 이벤트 값 등 서로 다른 의미로 사용될 수 있다.
7. 수정이 승인되더라도 먼저 대상과 영향 범위를 기록하고, 작은 단위로 적용한 뒤 같은 조건에서 검증한다.
8. 게임 실행, Nudger 사용, 테스트, 커밋·푸시·배포는 각각 사용자의 명시적인 요청 범위 안에서만 한다.
9. 저장소 `descriptor.mod`와 launcher `.mod`의 `dependencies`, `replace_path`, `remote_file_id`, `path`를 감사하고, 런처가 실제로 읽은 물리적 모드 복사본을 확인한다.
10. `supported_version` 변경이나 메인 메뉴 진입만으로 호환성이 증명됐다고 판단하지 않는다.
11. localisation은 일반 YAML이 아니다. UTF-8 BOM, locale header, 키·토큰과 `Korean Language` 의존 계약을 보존하고 일반 YAML formatter를 사용하지 않는다.

## 증거 등급

- **확인됨(Confirmed)**: 파일·로그·반복 재현으로 직접 확인한 사실
- **강하게 뒷받침됨(Strongly supported)**: 여러 증거가 같은 원인을 가리키지만 수정 후 재현 검증이 남은 판단
- **미확인(Unproven)**: 가능성은 있으나 직접 증거 또는 분리 시험이 부족한 가설
- **반증됨(Disproven)**: 현재 재현 조건에서 성립하지 않는 가설

결론에는 반드시 이 등급을 붙인다. 엔진 크래시 주소만으로 내부 원인을 단정하지 않는다.

## 민감하거나 임시인 자료

다음 자료는 필요할 때 원래 위치에서 읽고, 기본적으로 프로젝트에 복사하거나 커밋하지 않는다.

- `error.log`, `game.log`, `system.log`, `setup.log`, `exceptions.log`
- Windows Error Reporting 보고서와 덤프
- 플레이어 세이브 및 런처 설정
- 사용자 이름이나 로컬 절대 경로가 포함된 진단 자료

사건 문서에는 원본 파일 자체가 아니라 감사에 필요한 경로 별칭, 파일명, 줄 번호, 수정 시각과 짧은 발췌만 기록한다. 개인 식별 경로는 `<HOI4_USER_DATA>` 같은 별칭으로 비식별화한다. 원본 로그 보존이 필요하면 사용자가 승인한 별도 진단 위치에 실행 ID별로 복사하고, 커밋하지 않는다.
