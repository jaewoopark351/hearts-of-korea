# 내부 표식·변수 표시 개선 구현 기록

작성: **2026-11-08 (Asia/Seoul)**. 최종 상태: **승인된 표시 개선·표적 검증·세션 복원과 정리 완료**. 아래의 실제 관측 범위와 미검증 한계를 따른다. 원래 저장 비교의 **55통과·1실패 및 25통과·1실패는 보존**하며, 후속 통제의 귀속 결과와 합쳐 전체 게임 무오류로 해석하지 않는다.

**같은 날 후속:** 사용자의 요청으로 13개 국토개발 사업의 공통 안내만 축약했다. [후속 기록](#7-13개-사업의-공통-안내-축약)을 따른다. 아래의 화면·해시·저장 검증은 축약 전 표시 수리의 기록이며, 짧아진 문구의 새 화면 검증이 아니다.

이번 기록은 [표시 감사의 8개 고유 키](../audits/2026-11-08-continuation-localisation-display-review.md)에 대한 후속 구현을 다룬다. 사용자가 추가 확인을 요청한 **6개는 같은 대장의 L-03~08**이며, 별도 항목을 더해 14개로 계산하지 않는다. 국토개발 L-01·02는 기존 사용자 화면에서 원문 노출이 확인됐고, 새 한국어 기준 실행에서는 L-07의 원문 노출을 재현했다. **L-03~06은 원문 ID 노출이 아니라 해당 변수 명령의 자동 조건·효과 항목이 통째로 표시되지 않은 현상**으로 구분한다. L-08은 실제 동맹 산업지원 화면에서 내부 누적이 원래 표시되지 않음을 확인해 **생산 수정 불필요**로 판정했다. 8개 전체를 같은 유형의 원문 노출 오류로 기록하지 않는다.

고유 키 기준으로 **L-01~07의 7개는 표시 수리를 적용했고, L-08의 1개는 검토 후 무수정**이다. 구현 지점 수와 실제 UI 검증 범위는 아래에서 별도로 기록한다.

관련 규칙은 [프로젝트 지침](../../AGENTS.md), [두 언어 채널 계약](2026-09-01-localisation-contract.md), [CNDP 명세](../HOK_KOREAN_CNDP_STATE_DEVELOPMENT_PLAN.md), [재벌·시민사회 명세](../HOK_KOREAN_CHAEBOL_CIVIL_SOCIETY_SPEC.md)를 따른다. 이 문서는 표시 수리의 이력이며 새 게임플레이 설계나 언어 계약 변경을 승인하는 문서가 아니다.

## 1. 승인 범위와 보존 원칙

- 작업 모드는 **Implementation**이다. 내부 조건·효과의 표시를 개선하고 실제 화면에서 확인한다.
- 표식·변수·중점·결정·사건의 기존 ID, 저장 위치와 수명, 조건의 AND/OR/NOT 구조, 초기값·증감값·범위, 비용·기간·보상·AI·완료 이력과 구형 저장 분기를 보존한다.
- CNDP의 새/구형 체계를 합치거나 개발 완료 제한을 제거하지 않는다. 시민사회 영향력·기관 장악·비리의 값과 증거 보전 표식의 365일 수명을 바꾸지 않는다.
- 동맹 산업지원의 누적 변수는 내부 기록으로 유지한다. 횟수 상한이나 할당량을 추가하지 않으며 기존 150PP·180일·반복 투자 안내를 보존한다.
- 현지화는 기존 key, 각 locale header와 UTF-8 BOM을 보존한다. 저장소의 English/Korean 두 채널에는 기존 계약에 따른 한국어 본문을 유지하고, 실제 활성 영문 번역의 동명 파일 덮어쓰기는 별도로 확인한다.
- 지도·주 분할·시작 데이터·밸런스·Git 이력·커밋·push·게시·업로드는 변경 범위가 아니다.

## 2. 작업 기준선과 원본 보호

기준선 인덱스는 외부 `T/root/baseline.json`이다. 아래 수치는 해당 인덱스의 기록이며 실행 통과 수가 아니다.

| 항목 | 이번 기준선 |
|---|---|
| 저장소 | `C:\hoi\hearts_of_korea` |
| 브랜치·HEAD | `feat/korean-focus-expansion-ai` / `0d73d49726abbfa435c73f1bf8cc24d4a5af014b` |
| 작업 트리 | 기존 주 분할·CNDP·현재 지도 참조 정렬 및 문서 변경이 있는 상태. 기존 변경 보존. |
| 활성 번역 | `C:\hoi\Hearts of Korea English Translation Anime Modder's Edition` |
| 번역 HEAD | `81878a6cccd21214e85223551acceee107c9e585` |
| 기존 모드 순서 | HOK → Hearts of Korea English Translation (Anime Modder's Edition) |
| 기준선 생성 | `2026-11-08T05:41:39.100634+00:00` |
| 보호 인벤토리 | 기존 저장 61개, 지도·주 파일 24개, 원본 소스 사본 14개 |
| 사용자 설정 | 기존 `settings.txt`, `pdx_settings.txt`, `dlc_load.json`, `gameplaysettings.txt`를 `T/user-config-before/`에 보존 |
| 실제 진단 세션의 복원 원본 | 사용자 게임 종료 후 같은 4개 파일을 `T/user-config-session-before/`에 다시 보존. 초기 사본도 별도 유지. |
| 기준 로그 | `T/baseline-logs/`에 기존 로그 사본 보존 |
| 기준 엔진 | 기준 `system.log:139`에서 `Operation Postern v1.19.4.2.2da5 (add6)` 확인. 이 체크섬은 이후 진단·수정 실행에 그대로 적용하지 않는다. |
| DLC·모드 | 기준 로그에서 DLC 36개와 활성 모드 HOK/TR 2개 확인. 기존 선택의 `disabled_dlcs`는 빈 목록. |
| 기준 오류 | 기존 비활성 Workshop descriptor 경고 6행. 이번 수정으로 생긴 오류로 귀속하지 않는다. |

최초 소스·로그 보존 시에는 **기존 사용자 게임 PID 12920이 실행 중**이어서 종료 요청의 답변을 기다렸다. 이후 **사용자가 직접 기존 게임을 종료해 대기가 해소**됐으며 root가 새 진단을 시작했다. 기존 사용자 게임을 에이전트가 종료하거나 조작한 것으로 기록하지 않는다. 새 진단 실행과 테스트 소유 프로세스의 정리는 root가 수행한다. 프로세스 관련 기록은 PID·시작 시각 등 필요한 식별 정보로 제한하며 세션 토큰이나 민감한 CommandLine을 문서·보고서에 싣지 않는다.

실제 진단 전에는 `T/root/runtime.py`의 세션 보존 단계로 사용자 게임 종료 후의 설정 4개와 저장 61개를 다시 인덱스화했다. `T/session-original-config-vs-initial.json`에서 `settings.txt`는 초기 사본과 다르고 나머지 3개는 같다. 두 시점의 원본을 혼동하지 않으며, 종료 후 임시 설정 복원 기준은 **`T/user-config-session-before/`**, 기존 저장 보호의 세션 기준은 **`T/existing-saves-session-before.json`**이다. 초기 사본·인덱스는 앞선 관측의 증거로 보존한다.

첫 신규 실행은 **`baseline01` / 한국어 / PID 2328**, 시작 시각은 `2026-11-08T05:51:39.914007+00:00`이다. HOK → 활성 영문 번역 → 외부 표시 진단의 3개 모드 구성이며 원래 사용자 모드 선택과 구분한다. 이 실행은 미관측 6개 후보의 기본 표시를 확인하기 위한 것이고, 이미 적용된 CNDP 일부 소스 수리가 들어 있는 상태다. 프로세스 시작 자체를 UI·게임 효과·저장 검증 통과로 세지 않는다.

`baseline01`에는 탐색 중 결정·사건 reload 기록도 있다. 완전히 미수정·무재로드인 실행으로 취급하지 않으며, 최종 한국어·영어의 전체 프로세스 재시작과 구분한다. 중복 현지화 로그의 반복 횟수도 고유 결함 수로 해석하지 않는다.

이 실행에서 만든 기준 저장의 헤더는 `date="1936.1.1.20"`, `Operation Postern v1.19.4.2.2da5 (269e)`이다. 저장 사본은 `T/runs/baseline01/saves/KOR_1936_01_01_20_temp.hoi4`이고 SHA-256은 `f7112645da16b27b285750f04fff4c85103bebc148312f6aeb0ade04d155f16f`다. 12시의 기준 UI 화면과 20시의 기준 저장을 같은 시점으로 합치지 않는다. 이 기준 저장의 수정 후 왕복 비교는 아래 `finalKR01-absent` 결과와 연결한다.

`T/cndp/baseline01-snapshot.json`은 해당 기준 저장에서 재벌 60·시민 35·기관 장악 65·비리 40·동맹 산업지원 누적 41과 정치력 1650을 추출했다. 증거 보전 표식은 없고 CNDP 완료 표식 13곳도 없으며 양성 활성 결정 기록은 0이다. 이는 기준 데이터의 관측이지 전후 비교 PASS, 활성 타이머 보존, 완료 이력 양성 또는 365일 만료의 증거가 아니다. 저장 비교 helper의 `READY` 상태나 종료 코드 0만을 검증 완료로 세지 않으며, 실제 두 입력의 경로·해시와 새 결과의 `status=PASS`·실패 0을 함께 확인한다.

수정 소스를 읽는 새 한국어 프로세스 **`finalKR01` / PID 14352**는 `2026-11-08T06:21:35.181110+00:00`에 시작했고, root가 전체 로드와 체크섬 **`058e`**를 확인했다. `T/runs/finalKR01/process.json`으로 실행을 식별한다. 같은 3모드 진단 구성이며, 아래 실제 화면과 저장 비교를 프로세스 시작 기록과 구분한다.

`T/cndp/finalKR01-absent-save-review.json`의 실제 결과는 **`status=PASS`, 55항목 통과·실패 0**이다. 수정 후 사본 `T/runs/finalKR01/saves/KOR_1936_01_01_20_temp.hoi4`의 SHA-256은 `141a232faf44b551e5c7f45f45a26644747c51c3083f471d7fdf11f695987ba1`, 날짜는 같은 `1936.1.1.20`, 버전은 `Operation Postern v1.19.4.2.2da5 (058e)`다. 두 입력의 정확한 엔진 접두부와 정지 날짜는 같고, 소스 변경에 따른 체크섬 차이는 그대로 기록했다. 변수 5종 60·35·65·40·41과 정치력 1650, 국가 표식의 값·날짜, 13개 주의 비교 대상 필드, 11개 보상 프로빈스의 직렬화 필드, 결정 기록 18개 및 비교 대상 공장 비용 필드가 보존됐다. 주의 직렬화된 `variables.random` 배열은 비교에서 제외했다.

이 55항목은 지정한 두 새 진단 저장의 데이터 비교 수이며 게임 기능 55종의 통과 수가 아니다. 두 저장에는 증거 보전 표식과 완료 표식이 없고 양성 활성 결정 기록도 0이므로, **활성 타이머·365일 만료·완료 이력 양성 보존을 입증하지 않는다**. 기존 사용자 저장 61개의 일반 호환성이나 장기 진행 검증과도 구분한다.

표식이 존재하는 별도 24시 저장의 실제 비교 `T/cndp/finalKR01-positive-save-review.json`은 **`status=FAIL`, 55항목 통과·1항목 실패**다. 기준은 `T/runs/baseline01/saves/KOR_1936_01_01_24_temp.hoi4`(SHA-256 `cd2f919245fc0b1ed4b4703ad7399dc2541b429029352350c07afde7333419bc`), 수정 후는 `T/runs/finalKR01/saves/KOR_1936_01_01_24_temp.hoi4`(SHA-256 `95214271863d7b8d170697750902f2f34bcb7fc095e343574d93cdeb6a93f005`)이며 날짜는 모두 `1936.1.1.24`다. 변수 5종·정치력, 증거 표식의 값·날짜·365일 직렬화 정보와 전라남도 1088의 완료 표식은 보존됐다. 다만 `production_factory_cost_fields_preserved`가 실패했고 생산선의 캐시 `speed`에 `4.09463`→`4.01199` 등 차이가 있다. **당시 원인 판정은 UNPROVEN**이었다. 이 원래 실패를 전체 저장 보존 통과로 바꾸지 않으며, 이후 통제 귀속은 아래에 별도로 기록한다. 이 경우도 양성 활성 결정 기록은 0이며 실제 365일 경과·만료를 관측한 것은 아니다.

후속 `T/cndp/finalKR01-positive-production-investigation.json`은 전체 생산 필드에서 바뀐 하위 값이 군수 생산선 114의 `speed` `4.09463`→`4.01199`, 115의 `2.04731`→`2.00599` 두 곳뿐임을 기록했다. 나머지 생산 필드와 저장된 국민정신·정치·안정도·전쟁 지지도는 같다. 캐시 또는 파생값 재계산은 조사 가설이며 확정 원인이 아니다.

이어 root는 **새 한국어 `controlKR01` / PID 10600**, 시작 `2026-11-08T07:11:04.264206+00:00`에서 같은 불변 기준 24시 저장을 불러와 정지 상태 그대로 다시 저장했다. 생산 소스는 수정하지 않고 외부 `T/control-fixture/`에 이 작업 전 정확한 코드 바이트를 덮어쓰는 통제를 사용했다. **변경된 표시 코드 5개 모두를 원형으로 대체**했고, L-08 파일 1개는 원래 바뀌지 않은 출처 보존용 여섯째 사본이다. `T/control-fixture-manifest.json`은 준비 소스·수정 전 사본 해시를, `T/runs/controlKR01/saves/manifest.json`은 실제 저장의 생성·복사 출처를 기록한다. 현지화는 현재 파일을 그대로 상속했으므로 옛 원문 노출 화면의 재현 실험과는 다르다.

통제 저장 `T/runs/controlKR01/saves/KOR_1936_01_01_24_temp.hoi4`의 SHA-256은 `50c1d13ed9c6eae0b33aedbe31c5b2e701902be62014ec405afa27b0cee94bf5`, 정지 날짜는 같은 `1936.1.1.24`, 엔진 체크섬은 `99e4`다. 실제 비교 결과는 다음과 같다.

| 외부 보고서 — `T/cndp/` 기준 | 판정과 범위 |
|---|---|
| `controlKR01-positive-save-review.json` | 기준→원형 통제도 **55통과·1실패**. 같은 생산 필드 동일성 검사 실패를 보존. |
| `controlKR01-vs-finalKR01-positive-save-review.json` | 원형 통제→표시 패치 저장은 **56통과·0실패**. 5변수·PP·국가/완료 표식·13주·11프로빈스·결정 기록과 비교 대상 생산 필드가 같다. |
| `controlKR01-production-causal-review.json` | 인과 비교 **9통과·0실패**. 기준→원형과 기준→패치의 전체 생산 차이가 정확히 같은 두 `speed` 값이며 원형→패치의 전체 생산 차이는 0. 국민정신·정치 필드도 같다. |

**CONFIRMED:** 동일한 두 생산선 속도 차이는 이번 표시 코드 5개가 없는 상태에서도 발생했다. 따라서 이 재로드 차이가 생기는 데 표시 패치는 필요하지 않았다. **UNPROVEN:** 정확한 엔진 캐시·재계산 원인. 원래 패치 저장의 **55통과·1실패를 그대로 남기고** 원형 통제 결과를 추가하는 방식으로 귀속을 구분한다. 이 결과는 모든 게임 필드·모든 저장·활성 타이머 진행·365일 경과 검증을 뜻하지 않는다.

영어 `finalEN01`은 동일한 동결 소스를 읽는 새 프로세스 **PID 3276**, 시작 시각 `2026-11-08T06:45:47.092193+00:00`이다. 실행 인덱스와 영어 스크린샷은 T가 아닌 **`E/runs/finalEN01/`**에 있다. 아래 실제 관측 범위만 기록하며 영어 전체 화면이나 게임 진행 완료로 세지 않는다.

## 3. 외부 증거 위치

이번 작업의 외부 디렉터리는 다음 두 곳이다.

- **T:** `C:\hoi\test\hok-localisation-display-20261108-01`
- **E:** `C:\hoi\test\hok-english-translation-anime\hok-localisation-display-20261108-01`

| 위치 | 역할 |
|---|---|
| `T/root/baseline.json` | 브랜치·HEAD·원본 소스·지도/주 보호 해시·기존 저장 수·원래 모드 선택 인덱스 |
| `T/source-before/root-capture/repository/` | HOK 저장소의 수정 전 소스 사본 |
| `E/source-before/root-capture/` | 활성 영문 번역의 기존 시민 UI·민주 확장 파일 사본. `T/root/baseline.json`의 각 `copy` 경로가 이 위치를 가리킴. |
| `T/existing-saves-before.json` | 기존 저장 61개의 원본 보호 대조 기준 |
| `T/existing-saves-session-before.json` | 사용자 게임 종료 후 실제 진단 직전에 보존한 저장 61개의 세션 보호 기준 |
| `T/git-status-before-main.txt`, `T/working-tree-before-main.patch` | 기존 저장소 변경 상태 |
| `T/git-status-before-translation.txt`, `T/working-tree-before-translation.patch` | 기존 번역 작업 트리 변경 상태 |
| `T/baseline-logs/`, `T/user-config-before/` | 새 실행 전에 보존한 기존 로그와 설정 원본 |
| `T/user-config-session-before/`, `T/session-original-config-vs-initial.json` | 사용자 게임 종료 후 설정 복원 원본과 초기 사본 대비 결과 |
| `T/settings-restored.json`, `T/root/processes-after-cleanup.json` | 세션 설정 4개 정확 복원과 소유 보조창 종료 후 HOI4/Notepad 프로세스 수 기록. Steam 화면 판정과는 구분. |
| `T/root/runtime.py` | **과거 위치·정리 완료.** 세션 보존·실행·복원에 사용한 helper이며 최종 정리 때 제거. |
| `T/fixture/`, `T/root/fixture-created-manifest.json` | 임시 표시 진단 코드의 과거 위치와 생성 경로·해시 인덱스. **진단 코드 파일은 정리 완료, manifest는 보존.** |
| `T/runs/baseline01/process.json` | 첫 한국어 기준 실행의 PID·시작 시각. 같은 실행 아래에 실제 UI·로그·저장 증거 보존. |
| `T/runs/baseline01/screenshots/` | 변수 조건·개혁 효과·정변 임무의 수정 전 화면과 CNDP 첫 수리 화면 |
| `T/runs/baseline01/saves/manifest.json` | 새 기준 저장의 원본/사본 경로·해시·크기·테스트 소유 역할 |
| `T/runs/finalKR01/process.json`, `T/runs/finalKR01/screenshots/` | 수정 소스의 새 한국어 프로세스와 실제 CNDP 해금·변수 조건·개혁 효과 화면 |
| `T/runs/finalKR01/saves/`, `T/cndp/finalKR01-absent-save-review.json` | 같은 정지 날짜의 수정 후 저장과 표식 부재 전후 비교 55항목 결과 |
| `T/cndp/finalKR01-positive-save-review.json` | 24시 표식 양성 저장의 55통과·1실패와 정확한 차이. 원인 조사 중인 실패를 보존. |
| `T/cndp/finalKR01-positive-production-investigation.json` | 양성 재로드에서 생산선 속도 2곳만 달라진 전체 생산·국민정신·정치 필드 조사. 원인 미확정. |
| `T/control-fixture-manifest.json`, `T/runs/controlKR01/process.json`, `T/runs/controlKR01/saves/manifest.json` | 원형 코드 5개와 무변경 출처 사본 1개의 통제 준비·실제 프로세스·실제 저장 출처 보존. **통제 fixture 코드 파일은 사용 후 정리 완료.** |
| `T/runs/controlKR01/logs/` | root가 원형 통제 실행을 정상 종료한 뒤 수집한 로그 20개. |
| `T/runs/controlKR01/read-only-log-review.json` | 원형 통제 99e4 로그의 해시·기준/KR 비교·남은 오류·새 표적 진단 서명 없음 기록. |
| `T/cndp/controlKR01-positive-save-review.json`, `T/cndp/controlKR01-vs-finalKR01-positive-save-review.json`, `T/cndp/controlKR01-production-causal-review.json` | 각각 기준→원형 55·1, 원형→패치 56·0, 재로드 생산 인과 비교 9·0. 원래 실패와 후속 귀속 결과를 구분. |
| `T/runs/finalKR01/after-air-choice-a/`, `T/cndp/finalKR01-air-choice-a-effect-review.json` | 실제 항공 사고 사건 선택 A 후 저장과 의도한 효과·보존 비교 25통과·1실패. |
| `T/runs/finalKR01/logs/` | root가 해당 프로세스 종료 후 수집한 실제 로그. 수집 완료와 오류 판정은 구분. |
| `T/root/focus-cndp-display-patch.json` | root 소유 CNDP 중점 조건 wrapper의 단일 치환·원문 역변환 기록 |
| `T/cndp/` | CNDP 원본·표시 수리 소스 보존 검사와 관련 증거 |
| `T/civic/` | 시민사회 L-03~07의 원본 백업·표시 수리·검증 보고서 보존. 기준 UI seed 등 일회성 코드는 정리 완료. |
| `T/parameter/L08-preparation.json` | L-08의 소스 추적·표시 후보·2단계 UI 관측 계획 |
| `T/parameter/source-before/`, `T/parameter/candidates/` | L-08 원본 백업은 보존. 초기 미적용 후보 코드의 과거 위치인 `candidates/`의 일회성 파일은 정리 완료. 후보는 운영에 적용하지 않음. |
| `T/civic/civic-display-patch-review.json` | 첫 숫자 metadata 수리와 원본 바이트 보존 기록 |
| `T/civic/event-sync-display-review.json`, `T/civic/phase1-before-sync-hidden/` | 사건 UI 차단의 후속 원인·8개 wrapper·단계별 원문 보존 기록과 metadata 단계 소스 사본 |
| `T/cndp/baseline01-snapshot.json` | 새 기준 저장의 변수 5종·정치력·표식·주·결정 상태 읽기 추출. after 비교 통과와 구분. |
| `T/cndp/save-display-preservation.py` | **과거 위치·정리 완료.** 지정된 새 기준/수정 후 저장을 읽기 비교했던 helper. 실제 결과 JSON은 보존하며 helper 준비 상태를 통과로 세지 않음. |
| `E/cndp/` | CNDP 영문 29개 키의 생성·소스 대조·검사 증거를 보존하는 번역 담당 작업 위치 |
| `E/civic/` | 영문 시민사회 번역의 원본·보고서 보존 위치. 임시 진단 라벨·fixture 파일은 정리 완료. |
| `E/runs/finalEN01/process.json`, `E/runs/finalEN01/screenshots/` | 새 영어 프로세스와 L-08 중점·정변 임무 취소 조건·실제 `.12` 사건 선택지 화면. |
| `E/runs/finalEN01/logs/` | root가 영어 실행을 정상 종료한 뒤 보존한 로그 20개. 오류 대조 판정은 별도 기록. |
| `E/runs/finalEN01/read-only-log-review.json` | 영어 20개 로그의 해시·KR/기준 비교·발견/남은 오류·귀속 한계. 새 표시 관련 진단 서명 없음과 엔진 전체 무오류를 구분. |
| `T/final-protection-review.json`, `T/root/steam-play-after-cleanup.jpg` | 기존 저장 61개·지도/주 24개·동결 소스 11개 해시와 설정 복원 최종 대조, 실제 Steam Play 복귀 화면. |
| `T/root/final-completion-review.json` | 최종 증거 경로·브랜치/HEAD·작업 후 Git 상태·커밋/게시 없음의 종합 인덱스. |
| `T/root/cleanup-preflight.json`, `T/root/cleanup-completed.json`, `E/cleanup-completed.json` | 경계·경로·해시 사전 확인과 T 40개·E 15개 일회성 파일의 정확 삭제 완료 기록. |
| `T/root/owned-generated-saves-cleanup.json` | 동일한 외부 증거 사본을 보존한 뒤 작업 소유 사용자 데이터 임시 저장 20시·24시 2개만 제거한 기록. 기존 저장 이름 61개 일치. |

helper·fixture·로그 사본·스크린샷·테스트 저장·백업은 T 또는 E 아래에만 두고 작업했다. 게임이 생성한 원본은 실제 HOI4 사용자 데이터 디렉터리에 있었으며 증거 사본을 외부에 보존했다. 최종 정리에서는 이 작업 소유 임시 저장 2개만 동일 증거 사본을 확인한 뒤 제거했고 기존 사용자 저장 61개는 유지했다. 위 인덱스 중 제거됐다고 표시한 helper·fixture 경로는 **과거 출처이며 현재 재실행 가능한 파일이 아니다**. 보고서·로그·스크린샷·원본 백업·불변 증거 저장은 남겨 두었다.

## 4. 키별 구현·관측 상태

| ID | 고유 키 | 현재 상태 |
|---|---|---|
| L-01 | `HOK_KOR_cndp_state_projects_v1` | 기존 사용자 화면 원문 노출 확인. 공유 주 트리거 13개와 root의 중점 조건 1곳에 표시 wrapper 적용. 한국어·영어 전라남도 1곳의 내부 조건 비표시와 `finalKR01` 중점의 개별 결정 해금 13개·내부 표식 줄 부재를 확인. 13종 전체의 모든 상태를 관측한 것은 아님. |
| L-02 | `HOK_KOR_cndp_developed_v1` | 기존 원문 노출에 대응하는 긍정 완료 이름을 paired/TR에 추가. 전라남도 한국어·영어 화면에서 선행 조건의 부정과 취소 조건의 긍정 표시를 확인. 완료 효과의 `set_state_flag`는 native 기본 표시에서 보이지 않으므로 결정 코드는 유지. |
| L-03 | `HOK_KOR_chaebol_influence` | 기준 화면에서 변수 비교 항목이 자동 조건 목록에 없음을 확인. 원문 ID 노출 재현은 아님. 수정 후 한국어 `>0`·현재 60의 녹색 표시와 영어 외부 시드 C0의 빨간색·C100의 녹색 경계를 확인. |
| L-04 | `HOK_KOR_civic_influence` | 기준 화면에서 자동 변수 조건·효과 항목 누락 확인. 기존 설명·custom tooltip의 숫자까지 없었다는 뜻은 아님. 한국어 `<100`·현재 35 조건과 개혁 `+5`의 녹색 표시, 영어 외부 시드 V0의 녹색·V100의 빨간색 경계를 확인. |
| L-05 | `HOK_KOR_institutional_capture` | 개혁 효과와 임무 취소의 자동 숫자 항목 누락 확인. 원문 ID 노출 재현은 아님. 수정 후 한국어 개혁 효과 `-25`의 녹색 표시와 영어 임무 취소 조건 `<60`·현재 65 표시를 확인. 나머지 상태는 별도 검증 대상. |
| L-06 | `HOK_KOR_procurement_corruption` | 개혁 효과의 자동 숫자 항목 누락 확인. 원문 ID 노출 재현은 아님. 수정 후 개혁 효과 `-10`의 녹색 표시를 확인. |
| L-07 | `HOK_KOR_prosecutor_defence_prepared` | `baseline01` 정변 임무 취소 툴팁에서 원문 노출 재현. 긍정 상태 이름을 추가했고 기존 취소 OR·365일 수명은 유지. 수정 후 영어의 실제 90일 임무 취소 목록에서 `Evidence preservation completed`가 나오고 원문 ID는 없음을 확인. |
| L-08 | `HOK_KOR_asian_projects_started` | 실제 CHI 대상 산업지원 결정에서 내부 누적 비표시를 확인했고, 수정 후 영어 중점 초기화도 원래 비표시임을 확인. 기본 비표시가 정상인 내부 기록이므로 결정 `+1`과 중점 초기화 `0`을 원문 그대로 유지. |

소스의 정확한 이름 정의 부재와 사용자에게 실제 원문이 보이는 현상은 별도 판정한다. 영향받는 결정·중점·선택지 수를 고유 키 수와 합산하지 않는다.

### 한국어 기준 화면의 실제 관측

다음 파일은 root가 캡처한 화면이며 독립적으로 읽기 확인했다. 이 화면 범위를 모든 결정·사건·조건 조합의 재현으로 확대하지 않는다.

| 증거 파일 — `T/runs/baseline01/screenshots/` 기준 | 관측한 현상 |
|---|---|
| `chaebol-condition-before.jpg` | 재벌 견제의 공통 조건과 기존 사용자 설명은 보이지만, 소스의 재벌 영향력 `>0` 자동 조건 항목은 없다. |
| `civic-condition-before.jpg` | 시민사회 지원의 기존 설명·효과 안내는 보이지만 시민 영향력 `<100` 자동 조건 항목은 없다. |
| `reform-before.jpg` | 기관 장악망 해체의 설명문에는 수치가 있으나, 실제 변수 명령의 자동 제거 효과인 기관 -25·비리 -10·시민 +5가 표시되지 않는다. 국민정신의 동기화 효과와 변수 명령을 구분한다. |
| `mission-before.jpg` | 취소 OR 목록에서 기관 장악 `<60` 숫자 조건은 빠지고 `HOK_KOR_prosecutor_defence_prepared`는 원문으로 보인다. |
| `cndp-jeollanam-first-patch.jpg` | 첫 CNDP 표시 수리가 적용된 전라남도 1곳에서 버전 표식은 숨겨지고 완료 상태는 한국어로 보인다. 제거 효과 목록에 완료 표식 설정 자체는 표시되지 않는다. |
| `industry-counter-before.jpg` | 실제 중국 대상 산업지원 결정의 효과에는 기존 산업지원 안내만 보이며 내부 누적 변수 ID·값이나 횟수 제한 표시는 없다. 소스 수정 없이 유지한다. |

마지막 관측에 따라 `KOR_decision.txt`의 13개 `set_state_flag`를 숨기는 추가 wrapper는 넣지 않는다. 이 표시 작업 기준 원본과 현재 파일의 SHA-256은 모두 `9a22d108dc50533bff5e9ded621b4db826a1d29709f9996cfc629a3e6e7ec9e4`다. 이전 지도 참조 수리로 Git 작업 트리가 이미 변경됐던 사실과 이번 표시 작업에서 파일을 유지한 사실을 구분한다.

### 전체 재시작 후 한국어 화면의 관측

root는 `finalKR01`에서 다음 실제 화면을 캡처하고 표시를 확인했다. 숫자 치환·색상과 해당 해금 목록의 확인이며, 실제 결정 실행이나 모든 조건 경계의 검증으로 확대하지 않는다.

| 증거 파일 — `T/runs/finalKR01/screenshots/` 기준 | 수정 후 관측 |
|---|---|
| `cndp-focus-unlocks-top.jpg`, `cndp-focus-unlocks-bottom.jpg` | 중점 효과에 개별 결정 해금 13개가 모두 나오며 내부 버전 표식 줄은 없다. |
| `chaebol-condition-after.jpg` | 재벌 영향력이 0을 초과해야 한다는 조건과 현재 값 60이 녹색으로 표시된다. |
| `civic-condition-after.jpg` | 시민 영향력이 100 미만이어야 한다는 조건과 현재 값 35가 녹색으로 표시된다. |
| `reform-effects-after.jpg` | 개혁의 기관 장악 -25·조달 비리 -10·시민 영향력 +5가 각각 녹색 수치로 표시된다. |
| `air-event-choice-a-after.jpg` | 실제 `.2` 사건의 선택지 A가 화면에서 접근 가능하다. 정치력 -75, 비리 -5·시민 +5의 녹색 수치가 표시된다. |
| `air-event-choice-b-after.jpg` | 같은 사건의 선택지 B도 접근 가능하며 정치력 +50, 비리 +10·기관 장악 +5의 빨간 수치가 표시된다. |

### 새 영어 프로세스 화면의 관측

root가 `finalEN01`에서 캡처한 다음 다섯 화면은 독립 읽기 검토에서도 확인했다. 실제 활성 영어 번역의 렌더링이며, 앞선 영문 소스 대조와 구분한다.

| 증거 파일 — `E/runs/finalEN01/screenshots/` 기준 | 관측 |
|---|---|
| `fund-focus-counter-hidden.jpg` | 동맹 공동개발기금 중점 효과에는 기존 산업지원 결정 해금 안내만 보이며, 내부 누적 변수의 초기화 ID·값은 나타나지 않는다. L-08 무수정 결정을 뒷받침한다. |
| `mission-cancel-after.jpg` | 실제 90일 정변 임무의 취소 OR 목록에 기관 장악 60 미만·현재 65, `Evidence preservation completed`, 개혁 정책 미선택이 나오고 L-07 원문 ID는 없다. 이는 화면 관측이며 저장의 양성 활성 타이머 비교를 대신하지 않는다. |
| `rocket-choice-a-after.jpg` | 실제 `.12` 추진제 사고 사건이 화면 안에 들어오고 선택지 A에 접근 가능하다. PP -75, 비리 -5·시민 +5가 녹색으로 표시된다. |
| `rocket-choice-b-after.jpg` | 같은 사건의 선택지 B에 접근 가능하며 PP +50, 비리 +10·기관 장악 +5가 빨간색으로 표시된다. 실제 A/B 선택 실행은 아직 이 화면 증거의 범위가 아니다. |
| `cndp-jeollanam-after.jpg` | 실제 전라남도 결정에서 내부 버전 조건은 숨겨지고, 선행 조건에는 완료의 부정·즉시 취소 목록에는 완료의 긍정 이름이 나온다. 90일·민간공장 사용 5·75PP·건설 슬롯 +1·목포 승점 +1의 기존 안내도 보인다. |

추가로 root는 같은 영어 실행에서 외부 제어로 값을 0과 100에 맞춘 뒤 다음 조건 표시를 관측했다. **합성 경계 상태의 표시 확인이며 정상 정치 경로 진행이나 실제 변수 증감 검증이 아니다.**

| 증거 파일 — 같은 영어 스크린샷 디렉터리 | 경계 관측 |
|---|---|
| `chaebol-zero-boundary.jpg` | `C>0` 조건이 현재 0에서 빨간색이다. |
| `chaebol-hundred-boundary.jpg` | `C>0` 조건이 현재 100에서 녹색이다. |
| `civic-zero-boundary.jpg` | `V<100` 조건이 현재 0에서 녹색이다. |
| `civic-hundred-boundary.jpg` | `V<100` 조건이 현재 100에서 빨간색이다. |

영어에서 실제 선택 A/B를 실행하거나 영어 저장을 비교하지 않았다. root는 해당 실행을 정상 종료하고 `E/runs/finalEN01/logs/`에 로그 20개를 수집했다. 생산선 차이를 분리한 원형 코드 통제 결과는 위 별도 저장 비교로 기록하며, 영어의 화면 관측을 그 인과 검증의 대체물로 쓰지 않는다.

### CNDP의 현재 정적 기록

`T/cndp/source-preservation-report.json`은 현재 **8개 소스 보존 확인·실패 0**을 기록한다. 내부 체계 조건을 숨기는 13개 추가를 역변환하면 공유 트리거의 원문 전체 바이트가 복원되고, 표시 wrapper를 제외한 조건 순서·내용과 BOM·CRLF가 보존된다. 해당 시점의 결정 파일은 원본과 바이트가 같다. paired 현지화의 기존 본문 보존 확인도 포함한다. 이는 범위가 제한된 소스 확인이며 native 실행이나 UI 통과 수가 아니다.

root의 `KOR_comprehensive_national_development_plan` 중점 보상 조건 변경은 `T/root/focus-cndp-display-patch.json`에 **치환 1회·원문 역변환 동일**로 기록됐다. 기존 두 해금 분기와 조건의 참/거짓은 유지한다. 검토했지만 적용하지 않은 L-08 초기화 후보와는 별개다.

영문 번역 저장소의 `AGENTS.md` 전문을 읽은 뒤 CNDP 한국어 원문과 활성 번역 29개 키를 독립적으로 읽기 대조했다. 기존 공통 규칙·13개 지역 이름/설명·새 긍정 완료 라벨에서 취소, 정치력 환불 없음, 재착수, 완료 보상 1회, 상위 주 등급 유지, 슬롯 상한과 부지 전용 3종의 조건을 바꾸는 실질적인 오역은 찾지 못했다. 이 대조에서는 파일을 수정하거나 별도 검사를 실행하지 않았으며 실제 영어 UI 관측을 대신하지 않는다.

### 시민사회 수리의 소스·정적 기록

기준 관측 후 L-03~07 수리를 적용하고 소스를 동결했다. 일반 변수 명령의 이름만 추가하면 자동 조건·효과가 나타난다고 가정하지 않고, 현행 엔진의 `tooltip` metadata로 기존 숫자 항목을 명시한다. 추가 지점은 **29곳**이며 결정 조건 6·결정 효과 12·공개 사건 선택지 6개의 효과 10·공용 조달 조건 1이다. 이 사용 지점 수는 고유 결함 수가 아니다.

첫 metadata 단계의 `T/civic/civic-display-patch-review.json`은 정확히 추가한 metadata와 contributor note를 소거하면 결정·사건·공유 트리거 3개 원본 파일의 전체 바이트가 복원됨을 기록한다. paired와 활성 TR의 `HOK_KOR_civic_state_l_*.yml`에는 기존 본문을 보존하면서 변수 이름 4·증거 표식 이름 1·숫자 조건 7·증감 효과 3의 **15개 키**를 추가했다. 이 첫 단계에서는 AI·내부 sync·월간 처리·사건 immediate를 수정하지 않았다. 이후 발견된 사건 표시 차단에 대한 별도 최소 수리는 다음 절과 구분한다.

독립 읽기 대조에서도 조건의 `<`·`>`·`>=`, `$RIGHT|0$` 임계값과 현재 변수의 `Y0` 연결, 효과의 부호·색상 형식, locale header·기여 주석·3개 현지화 파일의 실제 BOM을 확인했고 중대한 문제는 찾지 못했다. 짧은 `check_variable` 구문과 metadata를 함께 쓰는 표적 바닐라 `common/decisions/RAJ_GOE.txt:824`, 변수 효과 metadata의 `events/AAT_Denmark.txt:1246` 예시도 대조했다. 이 소스 검토는 실제 `$RIGHT$` 치환·색상·UI·게임 효과 검증의 통과를 뜻하지 않는다.

### 시민 사건의 화면 차단과 후속 최소 수리

`baseline01`에서 실제 `HOK_KOR_CIVIC.2`를 열었을 때, 사건 본문 뒤에 `HOK_KOR_sync_civic_state`의 국민정신 제거·추가 목록이 길게 붙어 **1504px 화면 아래로 선택지가 밀려 접근할 수 없는 현상**을 관측했다. 증거는 `T/runs/baseline01/screenshots/air-event-before.jpg`다. 이는 변수 원문 노출이나 이번 숫자 metadata 추가의 결과가 아니라, 기존 공개 사건의 동기화 helper 표시가 드러난 별도 UI 차단이다. `show_major`는 해당 시민 사건에 없으며 이 현상의 원인이나 효과 숨김 수단으로 사용하지 않는다.

root 승인으로 공개 `.1`·`.2`·`.11`·`.12` 안의 기존 sync 호출만 각각 **1·3·1·3회, 총 8곳**에서 같은 위치의 `hidden_effect`로 감쌌다. 범위는 본문 immediate 2곳과 공개 선택지 6곳이며 `.3`·`.13`은 그대로 유지한다. 실제 동기화, 변수 증감, 국민정신 변경, 호출·예약 순서, 정치력과 AI는 보존하고 공개 변수 숫자 tooltip도 유지한다.

`T/civic/event-sync-display-review.json`에는 wrapper를 역제거하면 첫 metadata 단계의 파일이, metadata까지 역제거하면 최초 사건 파일 전체 바이트가 복원됨이 기록됐다. 이 단계의 사건 SHA-256은 `cb0916510505c5f77f977712a6671aba50dd6ae5cc76bef92fa61b2ce75186f7`이다. 현행 바닐라 `AAT_Finland.txt:35–38`, `AAT_Denmark.txt:1737–1745`의 immediate와 `1354–1356`의 선택지 wrapper, `hidden_effect` 문서를 대조했다.

이후 새 `finalKR01` 프로세스의 실제 `.2` 사건에서는 선택지 A·B 모두 접근 가능해졌고, 위 두 스크린샷에서 각각의 공개 숫자·색상 표시를 확인했다. 원래 immediate의 실제 항공 사고 국민정신·안정도 안내는 계속 표시된다. root는 실제 선택 A를 실행해 화면의 정치력이 1650→1575로 변함을 관측하고 `T/runs/finalKR01/after-air-choice-a/KOR_1936_01_01_24_temp.hoi4`를 저장했다. 이 사본의 SHA-256은 `1a47be068873964d865e5345267e05451c72097c815b3039465d380740fb916d`다.

실제 선택 후 `T/cndp/finalKR01-air-choice-a-effect-review.json`은 **25통과·1실패, `status=FAIL`**이다. 24시 선택 전 C60·V35·I65·P50·누적41·PP1650에서 선택 후 C60·V40·I65·P45·누적41·PP1575가 직렬화되어, 의도한 PP -75·시민 +5·비리 -5와 같은 국민정신 단계 유지를 확인했다. 20시 기준의 P40과 사건 발생 후 24시의 P50을 혼동하지 않는다. 실패는 넓은 생산 필드 동일성 검사 `production_factory_fields_after_choice_unchanged`이며, 생산선의 `speed` `4.01199`→`3.89575`, `2.00599`→`1.94787` 두 값이 달라졌다. 이 차이의 원인도 미확정이다. 위 원형 통제는 재로드 비교이며 원형에서 선택 A까지 실행한 직접 통제가 아니므로, 선택 후 추가 차이에 그 귀속을 확대하지 않는다. 성공한 의도 효과와 실패한 별도 보존 검사를 합쳐 모두 통과로 기록하지 않는다. 선택지 B의 실제 실행과 다른 사건 효과까지 통과했다고 확대하지 않는다.

추가 읽기 검토에서 `.3`·`.13` 회복 사건도 제목·본문·선택지가 있는 공개 사건이며 같은 sync 호출이 immediate에 남아 있음을 확인했다. 이 두 화면에서도 같은 목록 표시가 생길 위험은 **STRONGLY_SUPPORTED**, 실제 선택지 차단 재현은 **UNPROVEN**이다. 현재 승인·구현된 8곳과 구분하며 모든 회복 사건의 UI가 복구됐다고 확대하지 않는다.

### L-08 관측 결과와 미수정 결정

[동맹 산업지원 결정](../../common/decisions/HOK_KOR_democratic_expansion.txt)의 `HOK_KOR_finance_allied_industry.complete_effect`에는 다음 순서가 있다.

1. 한국 범위에서 `HOK_KOR_asian_projects_started`를 1 증가.
2. 대상국 `FROM`에 기존 `HOK_KOR_industrial_project_committed` 표식 설정.
3. 기존 `HOK_KOR_industrial_project_commitment_tt` 표시.

초기 외부 후보는 첫 명령만 `hidden_effect`로 감싸는 방식이었다. 그러나 실제 `industry-counter-before.jpg`에서 이 내부 명령은 이미 비표시였으며 기존 산업지원 안내가 정상 표시됐다. 따라서 **후보를 적용하지 않고 생산 코드를 유지**한다. 결정 원본과 현재 SHA-256은 모두 `6c9c3a56b4a29d126661e40aaab3782fbd3e3cc8b5abc2af529cf2c2284b1b60`이다. 기존 비용 150PP, 기간 180일, 반복 가능, AI 가중치와 모든 가용·취소·완료 조건도 그대로다.

기준 저장에서 엔진이 소문자로 직렬화한 `hok_kor_asian_projects_started=41`도 읽기 확인했다. 내부 값이 존재하는 사실과 그 값이 화면에 보여야 한다는 판단은 다르다. 이 변수 참조는 결정 증가와 중점 초기화 두 곳이며 횟수 제한 조건으로 쓰이지 않는다. 이번 관측은 180일 사업의 실제 완료나 장기 반복 사용까지 입증하지 않는다.

표적 엔진의 `documentation/effects_documentation.md:4659–4665`와 `common/decisions/GER.txt`의 내부 변수 wrapper 예시 대조는 후보 준비 근거로 남긴다. 적법한 wrapper라는 사실만으로 실제 필요 없는 변경을 적용하지 않는다.

root 소유 [한국 중점](../../common/national_focus/korea.txt)의 `HOK_KOR_asian_development_fund` 초기화에 전달했던 wrapper 후보도 적용하지 않는다. 기존 `set_variable = { HOK_KOR_asian_projects_started = 0 }`과 뒤의 결정 해금 안내를 원문 그대로 유지한다. L-08은 **검토·실제 관측 후 변경 불필요 판정**이며 구현한 수리로 집계하지 않는다.

## 5. 실제 UI 확인의 현재 범위와 남은 항목

한국어 기준 화면, 전체 재시작 후 CNDP 해금 13개와 시민사회 일부 숫자 조건·개혁 효과, 실제 `.2` 선택지 접근과 선택 A의 PP·변수 변화, 영어의 증거 표식 취소 조건·실제 `.12` 선택지·L-08 중점 비표시·전라남도 CNDP·C/V 0·100 경계는 위에 기록했다. 재로드 생산선 차이의 원형 코드 통제도 위에 구분했다. 이 표는 이번에 확인한 범위와 확인하지 않은 상태를 구분하며, 최종 세션 정리는 다음 대장의 결과를 따른다.

| 범위 | 기준·수정 후 각각 볼 화면 |
|---|---|
| CNDP | 한국어·영어 전라남도 1곳의 표시와 중점의 개별 결정 해금 13개를 확인. 완료 표식 양성의 직렬화 보존과 실제 취소/완료 실행은 구분하며, 다른 주·구형 분기를 별도 기록. 완료 표식 설정의 기본 미표시는 확인했으므로 결정 코드를 유지. |
| 시민 변수 4종 | C60의 `>0`, V35의 `<100`과 개혁 I-25·P-10·V+5, 한국어 `.2`·영어 `.12` 선택지 A·B 숫자·색상, 외부 시드 C/V 0·100 경계 표시 확인. 조달·나머지 결정 효과, 기존 숫자 패널·설명 보존 여부는 별도 확인. |
| 증거 보전 표식 | 실제 `.20` 경로로 활성화한 정변 임무의 영어 취소 툴팁에서 번역된 이름과 OR 구조 확인. 기본 위기와 모든 결정 표시용 진단 상태, 실제 타이머 직렬화 검증을 구분. |
| L-08 | 실제 CHI 대상 지원의 내부 누적 비표시를 확인해 결정·중점 누적 명령을 유지. 표식 부재 저장 왕복에서 내부 값 41 보존도 확인. 새 UI 수리나 실제 180일 사업 완료를 주장하지 않음. |

시민사회 기본 seed는 재벌 60·시민 35·기관 장악 65·조달 비리 40이며 기준 실행의 로그에서도 이 네 값을 확인했다. 초기화·패널·개혁 정책·조달 해금 이후 실제 정변 경고 경로를 사용하며, 증거 표식은 false·기관 장악은 60 이상으로 두어 관측 전에 임무가 즉시 취소되지 않게 한다. 이는 표시를 위한 합성 상태이고 정상 정치 경로 진행의 증거가 아니다.

한국어 채널과 실제 활성 English/TR 구성의 표시를 분리해 기록한다. 영문 번역을 수정하게 되면 해당 저장소의 `AGENTS.md`를 먼저 읽고 원본·후보·검증 결과를 E에 보존한다. 런처의 선언이나 key 존재만으로 실제 표시를 통과 처리하지 않는다.

## 6. 검증·저장·정리 대장

| 구분 | 현재 기록 |
|---|---|
| 소스 추적·문맥 대조 | CNDP 정적 기록, 시민 metadata 29곳·현지화 15키의 소스 보존 및 독립 읽기 대조, 사건 sync wrapper 8곳의 단계별 원문 보존 기록 확보. L-08 후보는 미적용으로 종료. |
| 이번 작업의 신규 게임 실행 | 한국어 기준 `baseline01` PID 2328, 수정 후 한국어 `finalKR01` PID 14352와 영어 `finalEN01` PID 3276, 원형 코드 한국어 `controlKR01` PID 10600. 수정 후 058e와 원형 통제 저장 99e4를 구분. 기존 사용자 게임 로그와 구분하며 시작 횟수를 검증 통과 수로 세지 않음. |
| 기본 UI 관측 | L-03~06의 자동 숫자 항목 누락·L-07 원문 노출·L-08 정상 비표시·공개 사건의 sync 목록 화면 차단을 한국어 `baseline01`에서 확인. L-01·02의 기존 사용자 화면은 별도 증거. |
| 수정 후 한국어 UI | CNDP 첫 수리 전라남도 1곳과 전체 재시작 후 중점 해금 13개·내부 조건 비표시, C>0/현재60·V<100/현재35, 개혁 I-25·P-10·V+5의 녹색 수치 표시, 실제 `.2` 선택지 A·B 접근과 숫자·색상 확인. 다른 화면·조건은 위의 제한을 따름. |
| 수정 후 활성 영어 번역 UI | `finalEN01`의 실제 90일 임무에서 번역된 L-07·I<60 현재65·NOT 개혁 OR, 실제 `.12` A/B 접근·숫자·색상, L-08 중점 비표시, 전라남도 CNDP 조건·비용·보상과 C/V 0·100 경계 확인. 영어 선택 실행·영어 저장 비교·전체 화면 확인을 뜻하지 않음. |
| 조건·비용·보상·저장 값 보존 | 범위별 소스 보존 기록과 실제 `.2` 선택 A의 PP-75·V+5·P-5·같은 국민정신 단계 유지 확인. 선택 후 별도 생산 필드 동일성은 실패했으며 CNDP 실제 완료/취소·반복 사용은 미검증. |
| 저장·재로드 | 부재 쌍 **55·0**, 양성 패치 쌍 **55·1**, 실제 선택 A 후 **25·1**의 원본 판정 유지. 양성 원형 쌍도 **55·1**, 원형→패치 **56·0**, 재로드 인과 비교 **9·0**. 동일 재로드 차이가 표시 코드 없이 재현됨은 확인했고 정확한 엔진 원인·선택 A 후 추가 차이는 미확정. 5변수·PP·증거/완료 표식 보존 범위는 위 보고서별로 구분. 활성 타이머 진행이나 기존 사용자 저장의 일반 호환을 뜻하지 않음. |
| 로그 비교 | 한국어·영어 최종 및 원형 통제 로그 각 20개 보존. 영어 검토에서 058e, 원형 통제 검토에서 99e4·DLC36을 확인하고 각각 기준/KR과 비교해 새 표시 관련 진단 서명 0. 각 검토의 범위를 구분하며 기존 오류는 아래와 같이 남아 있음. |
| 사용자 저장·지도/주·동결 소스 보호 | `T/final-protection-review.json`의 **PASS·실패 0**: 기존 저장 61개·지도/주 24개·동결 생산 소스 11개의 해시 모두 일치. 이 작업 소유 사용자 데이터 임시 저장 2개를 제거한 뒤 기존 저장 이름 집합도 정확히 61개로 일치. |
| 테스트 프로세스·Steam 상태 | 테스트 소유 실행 정상 종료. 소유 Notepad 보조창 11개도 UI 오류 안내 확인 후 제한된 대상만 종료했고 CIM상 HOI4 0·Notepad 0. Notepad++는 변경하지 않음. root가 실제 Steam의 녹색 Play 버튼 복귀를 확인하고 `T/root/steam-play-after-cleanup.jpg`에 보존. |
| 설정·모드 선택 복원 | 사용 후 제거한 `T/root/runtime.py`로 세션 설정 4개를 복원. `T/settings-restored.json`과 최종 보호 대조에서 모두 정확 일치 `true`, 임시 사용자 데이터 descriptor 없음. 사용자 게임 종료 후의 세션 원본을 복원한 것이며 그보다 앞선 초기 `settings.txt` 사본으로 되돌리지 않음. |
| 일회성 코드·fixture 정리 | T **40개**, E **15개**의 정확 파일 삭제 완료, 각 정리 후보 잔여 0. helper·fixture·미적용 후보 코드는 제거하고 출처 manifest·보고서·로그·스크린샷·소스/설정 백업·불변 증거 저장은 보존. |
| Git·게시 | root가 main 범위 파일과 TR 두 파일의 `git diff --check` 통과 확인. 브랜치·HEAD 유지, 커밋·push·게시·업로드 없음. 기존 작업 트리 보존. |

영어 `error.log` 10행은 비활성 descriptor 경고 6·현지화 충돌 요약 1·`map/buildings.txt:66858` 1·`random.log` 이름 변경 errno 2의 2행이다. 모두 기준/KR에 같은 종류의 메시지가 있다. 현지화 중복은 해군 함장 계열 13개 키·26개 기록으로 CNDP/시민 키가 아니며, 기존 지도 오류와 I/O 오류의 정확한 원인은 이 표시 수리에서 입증하지 않았다. 같은 로그 검토는 기존 river·단축키 충돌·Conflict Risk 메시지도 구분했다. 조용한 표적 로그는 숫자 치환·색상·모든 UI나 저장 보존의 대체 증거가 아니다.

원형 통제의 `read-only-log-review.json`도 20개 수집 로그에서 새 표적 parser/tooltip/현지화 서명 0을 기록했다. 통제 `error.log` 13행은 같은 descriptor 6·현지화 요약 1·지도 1·이름 변경 errno 2의 5행이며, 정규화한 메시지는 모두 기준/KR에 이미 있다. 기존 서명의 재현은 무해함이나 정확한 원인의 입증이 아니다.

최종 정리 전 `T/root/cleanup-preflight.json`으로 경계 안의 정확 경로·해시를 확인했다. 최초 복합 셸 정리는 자동 검토가 **실행 전에 거절**했으므로 그 명령으로 삭제된 파일은 없다. 이후 같은 승인 범위의 개별 파일만 `apply_patch`의 비재귀 정확 삭제로 정리해 T 40개·E 15개가 완료됐다. `T/final-protection-review.json`의 기존 저장 61개 해시는 `2026-11-08T07:27:13.2514996Z`의 대조 결과이고, `T/root/owned-generated-saves-cleanup.json`은 그 뒤 `07:31:24.3909620Z`에 동일 외부 증거 사본을 가진 작업 소유 임시 저장 2개만 제거하고 원래 61개 이름의 일치를 확인한 기록이다.

기존 `docs/assets/korean-fascist-mobilization-validation-20260923/`의 PNG 4개·815,391바이트는 이전부터 남은 정리 미결 자료다. 이번 표시 수리의 신규 산출물이 아니며 이 작업에서 이동·삭제하지 않는다.

승인된 표시 구현과 표적 검증·세션 정리는 완료했다. **한계:** 모든 CNDP 주·구형 분기의 실제 완료/취소, 180일 산업지원 반복, 실제 활성 타이머의 저장·진행과 365일 경과 만료, 장기 AI·다른 DLC 조합·멀티플레이·기존 캠페인 일반 호환은 검증하지 않았다. `.3`·`.13` 공개 회복 사건의 남은 sync 표시 위험도 위와 같이 미관측으로 남긴다. 원래 양성 55·1과 선택 후 25·1 실패를 유지하며, 재로드 차이는 표시 코드 없이도 동일 발생했지만 정확한 엔진 원인과 선택 후 추가 속도 차이의 직접 인과는 미확정이다.

## 7. 13개 사업의 공통 안내 축약

2026-11-08, 사용자가 공통 안내를 줄이도록 요청해 `HOK_KOR_cndp_project_rules` 한 키를 두 문장으로 바꿨다. 한국어 두 채널은 **“취소 시 정치력은 반환되지 않으며 재착수할 수 있습니다. 완료 보상은 주마다 한 번만 지급됩니다.”**, 활성 영문 번역은 **“Cancelled projects can be restarted, but Political Power is not refunded. Completion rewards are granted once per state.”**다. 공통 안내의 소유·통제·항복 조건 반복과 등급·상한 부연을 덜어냈으며, 13개 지역 소개와 자동 조건·보상 표시, 실제 게임 규칙은 유지했다.

변경 파일은 본체 `localisation/{korean,english}/HOK_KOR_cndp_state_development_l_{korean,english}.yml` 두 개와 활성 번역의 `localisation/english/HOK_KOR_cndp_state_development_l_english.yml` 한 개다. 한국어 안내는 144→54자, 영어는 410→120자로 줄었다. 각 파일은 이 값과 필수 기여 주석만 바뀌었고, 역변환 시 수정 전 전체 바이트와 같음을 확인했다. BOM·CRLF·기존 29개 키·공통 안내 참조 13곳과 본체 두 채널의 본문 일치를 보존했다. 결정·공유 트리거·한국 중점 세 파일의 해시도 그대로다.

이번 사본과 대조 기록은 **`C:\hoi\test\hok-cndp-common-copy-20261108-01\`**, 번역 전용 사본·대조 기록은 **`C:\hoi\test\hok-english-translation-anime\hok-cndp-common-copy-20261108-01\`**의 `source-before/`와 `copy-review.json`에 보존했다. 이전 표시 수리의 증거 경로는 옮기거나 덮어쓰지 않았다. 일회성 helper·진단 모드·설정 변경은 없으며 게임을 새로 실행하지 않았다. 위의 축약 전 한국어·영어 스크린샷과 동결 소스 11개 해시는 앞선 검증 시점의 이력으로 유지한다.
