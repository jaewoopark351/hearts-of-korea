# 2026-08-31 시작 크래시 조사

## 문서 판정과 현재 상태

- 조사 모드: **Diagnostic**
- 결론 적용 범위: **Hearts of Korea 단독 구성 `D-PRE`에서 재현된 시작 크래시**
- 현재 결론: 구버전 맵 데이터와 HOI4 `1.19.2` 맵 데이터의 불일치가 해당 크래시의 주원인으로 **STRONGLY_SUPPORTED**
- 지원 구성 상태: `Korean Language`를 포함한 구성 `C`는 아직 미검증
- 수정 상태: 미수정
- 게임 재실행 상태: 이번 문서 작성 및 보정 과정에서는 실행하지 않음
- Diagnostic documentation: **CONDITIONAL PASS**
- Map implementation: **NOT APPROVED / BLOCKED**

이 결론은 `D-PRE`와 동일 조건의 `D-POST`, 그리고 실제 지원 구성인 `C-POST`가 검증되기 전까지 `CONFIRMED`로 승격하지 않는다. 엔진 내부에서 정확히 어떤 검사·assert 또는 함수가 실패했는지도 미확인이다.

## 기준 환경

- 경로 별칭:
  - `<PROJECT>`: `C:\hoi\hearts_of_korea`
  - `<D_PRE_MOD_PATH>`: `C:\hoi\hearts of korea` — `D-PRE` 당시 launcher descriptor가 가리킨 경로이며 현재는 존재하지 않음
  - `<HOI4_INSTALL>`: `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`
  - `<HOI4_USER_DATA>`: `C:\Users\<USER>\OneDrive\문서\Paradox Interactive\Hearts of Iron IV`
  - `<HOK_ORIGINAL_WORKSHOP>`: `C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\2898629778`
  - `<KOREAN_LANGUAGE_WORKSHOP>`: `C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\2743487021`
  - `<WER_REPORT>`: `C:\ProgramData\Microsoft\Windows\WER\ReportArchive\AppCrash_hoi4.exe_41f0a696844af03db9895fd87a56c21f7591a29_4a5fc6d1_041a5c83-6e37-41ba-ba22-fee534ecd921\Report.wer`
- Git 기준선(최종 문서 보정 시작 직전): branch `main`, commit `fd168974d29ac0af774ac0b8aa752b01e32f22a0`, working tree clean
- 로컬 추적 참조 상태: `origin/main`과 같은 commit, ahead/behind `0/0`. 이번 문서 보정에서는 원격 fetch를 수행하지 않음
- 원본 프로젝트: Hearts of Korea, Workshop ID `2898629778`
- 마지막 알려진 원본 릴리스 표기: `1.0.9(1)`
- 현재 설치된 원본 Workshop descriptor: version `1.0.0`, `supported_version = 1.16.*`, `remote_file_id = 2898629778`
- 원본 릴리스 표기 `1.0.9(1)`과 설치 descriptor `1.0.0`의 의미 차이: 미해결, 기준본 확정 전 `UNPROVEN`
- 현재 목표 게임: Operation Postern `v1.19.2.0.a729 (d245)`
- 현재 계승판 개발 descriptor 이름: `하츠 오브 코리아 Hearts of Korea[1.19 호환](씹덕 모드 제작자 개정)`
- 현재 계승판 개발 descriptor 버전: `1.0.0`
- 현재 descriptor의 `supported_version`: `1.19.*`
- 선언된 필수 의존 모드: `Korean Language`
- 설치된 `Korean Language` 후보 descriptor: Workshop ID `2743487021`, version `25.11.23`, `supported_version = 1.17.*`
- 현재 launcher 설정에서 확인된 활성 모드: `mod/hearts of korea.mod`만 활성
- 현재 launcher `.mod`의 `path`: `<D_PRE_MOD_PATH>`를 가리키며 `<PROJECT>`와 불일치
- 현재 launcher playset 이름: 기록되지 않음
- 제한 사항: 정확한 보유/활성 DLC 전체 목록은 별도로 기록되지 않음

현재 descriptor의 `[1.19 호환]`과 `supported_version = 1.19.*`는 **검증되지 않은 임시 개발 메타데이터**다. `C-POST`와 최소 스모크 테스트를 통과하기 전에는 공개 배포의 호환성 주장으로 사용하지 않는다.

현재 재현은 선언된 필수 의존 모드가 빠진 HoK 단독 구성이다. 따라서 최종 지원 구성 검증에는 `Korean Language`를 포함한 별도 실행 기록이 필요하다. `dlc_load.json`의 `disabled_dlcs`가 비어 있다는 사실은 보유·활성 DLC 전체 목록의 증거가 아니다. 설치된 `Korean Language` 후보도 목표 HOI4 `1.19.2` 지원 여부와 실제 로드 결과가 미검증이다.

역사적 `D-PRE` 시점에는 launcher `.mod`가 당시 존재하던 `<D_PRE_MOD_PATH>`를 가리켰고, 모드 `definition.csv`의 province 수와 runtime 로그가 일치하므로 그 복사본이 로드됐다는 판단은 `STRONGLY_SUPPORTED`다. 그러나 현재 작업 저장소는 `<PROJECT>`에 있고 launcher는 존재하지 않는 `<D_PRE_MOD_PATH>`를 가리킨다. 따라서 현재 저장소가 다음 실행에서 실제로 로드된다는 주장은 `UNPROVEN`이며, 경로 정합성과 launcher 로그를 확정하기 전에는 새 재현을 시작하지 않는다. 이번 문서 작업에서는 launcher 설정을 수정하지 않았다.

## 재현 식별과 누락된 실행 기록

기존 2026-08-31 13:13 실행을 이 문서에서 소급해 `D-PRE`로 부른다. 이 이름은 비교를 명확히 하기 위한 문서상 식별자이며, 원래 실행 당시 사건 ID가 기록된 것은 아니다.

| 항목 | 기록 상태 |
|---|---|
| 실행 ID | `D-PRE`로 소급 지정 |
| 구성 | Hearts of Korea 단독 |
| 필수 의존 모드 | `Korean Language` 미활성 |
| launcher playset 이름 | 미기록 |
| 전체 DLC 목록 | 미기록 |
| 실행 옵션 및 `-debug` 여부 | 미기록 |
| 실제 사용자 조작 순서 | 미기록 |
| 실행 시작 시각 | 미기록 |
| 마지막 화면·로딩 문구·진행률 | 미기록 |
| 로그 snapshot | 2026-08-31 13:13:05~13:13:29 |
| 종료 형태 | 바탕 화면 종료 및 WER `BEX64` 확인 |
| `game.log` 마지막 확인 진행 단계 | `Loaded 13410 provinces.` |

다음 재현에서는 실행 시작·종료 시각, 마지막 화면, 크래시까지의 경과 시간, launcher/playset, 실행 옵션과 실제 조작 절차를 사건별 증거 bundle에 남긴다.

## 불변 기준선과 현재 blocker

`<PROJECT>`는 현재 별도 Git 작업 복사본이며 문서 보정 시작 직전 commit `fd168974d29ac0af774ac0b8aa752b01e32f22a0`으로 불변 기준선을 가진다. 따라서 “Git 저장소가 아님”이라는 기존 blocker는 해소됐다. 다만 설치된 Workshop 관리 복사본은 불변 archive가 아니며, 정확한 구형 바닐라와 전체 manifest도 아직 확보되지 않았다.

기준선 확보 상태는 다음과 같다.

1. **PARTIAL** — 원본 Workshop ID `2898629778` 설치본은 존재하지만 읽기 전용 archive로 동결되지 않음
2. **BLOCKED** — 원본 전체 파일 목록과 SHA-256 manifest 미생성
3. **CONFIRMED** — 현재 계승판은 `<PROJECT>`의 별도 Git 작업 복사본
4. **BLOCKED** — 정확한 마지막 지원 Vanilla `1.16.x` patch/build/checksum 기준본 미확보
5. **PARTIAL** — 목표 Vanilla `1.19.2.0.a729 (d245)` 설치본은 있으나 전체 manifest와 영향 파일 snapshot 미완성
6. **PARTIAL** — `Korean Language` 설치 후보는 찾았지만 `1.19.2` 지원성, 실제 로드 순서와 ID 영향 inventory 미확정
7. **CONFIRMED** — Git baseline commit `fd168974d29ac0af774ac0b8aa752b01e32f22a0` 확보
8. **BLOCKED** — launcher `path`가 현재 `<PROJECT>`와 불일치

남은 기준선과 launcher 경로 정합성이 확보되기 전에는 bitmap 및 영구 ID 변경의 **Implementation blocker**가 유지된다. 추가 commit, push 또는 저장소 구조 변경도 해당 작업을 사용자가 명시적으로 요청한 경우에만 수행한다.

## 연결 문서 상태

현재 프로젝트에서 다음 연결 문서의 존재와 상대 경로를 확인했다.

- [증거 기록 양식](../EVIDENCE_RECORD_TEMPLATE.md)
- [맵 호환성 점검표](../MAP_COMPATIBILITY_CHECKLIST.md)

이 조사서는 `docs/incidents/`에 있으므로 상위 `docs/`의 문서에는 `../` 상대 경로를 사용한다. 두 링크는 최종 문서 보정 시점에 유효하다.

## 감사 가능한 증거 위치

개인 식별 경로는 별칭으로 적었다. 현재 로그는 다음 실행에서 덮어써질 수 있으며, 이번에는 별도 원본 사본을 만들지 않았다. `D-PRE` 당시 상태와 최종 문서 보정 시점의 현재 상태를 구분한다.

| 증거 | 위치 | 확인 내용 |
|---|---|---|
| 저장소 descriptor | `<PROJECT>/descriptor.mod:1,8-12` | 버전, 이름, `Korean Language`, `supported_version`; 전체 12줄에 `replace_path`와 `remote_file_id` 없음 |
| Git 기준선 | `<PROJECT>/.git` | 보정 시작 전 `main` / `fd168974...` / clean, 로컬 `origin/main`과 `0/0` |
| 원본 Workshop descriptor | `<HOK_ORIGINAL_WORKSHOP>/descriptor.mod:1,8-13` | version `1.0.0`, `supported_version = 1.16.*`, `remote_file_id = 2898629778` |
| Korean Language descriptor | `<KOREAN_LANGUAGE_WORKSHOP>/descriptor.mod:1,5-7` | version `25.11.23`, `supported_version = 1.17.*`, `remote_file_id = 2743487021` |
| launcher descriptor | `<HOI4_USER_DATA>/mod/hearts of korea.mod:1,8-13` | `path`가 현재 존재하지 않는 `<D_PRE_MOD_PATH>`를 가리키며 `<PROJECT>`와 불일치 |
| 현재 launcher 설정 | `<HOI4_USER_DATA>/dlc_load.json:1` | `mod/hearts of korea.mod`만 enabled, 명시적 disabled DLC 없음 |
| province 로드 수 | `<HOI4_USER_DATA>/logs/game.log:2` | `[13:13:25] Loaded 13410 provinces.` |
| malformed province | `<HOI4_USER_DATA>/logs/error.log:29-32` | `[13:13:21]`에 `13410`, `13413`, `13412`, `13411` 순으로 malformed |
| 모드 definition 끝 | `<PROJECT>/map/definition.csv:13411` | 마지막 정의 ID가 `13409` |
| 바닐라 definition 끝 | `<HOI4_INSTALL>/map/definition.csv:13410-13414` | ID `13409-13413`; 마지막 정의 ID가 `13413` |
| 모드 custom state | `<PROJECT>/history/states/1017-*.txt`부터 `1027-*.txt`의 내부 `id` 줄 | 모드가 `1017-1027`을 서로 다른 한국·만주·쓰시마 state로 정의 |
| 바닐라 state 충돌 | `<HOI4_INSTALL>/history/states/1017 - Trung Bo.txt`부터 `1027 - Bataan.txt`의 내부 `id` 줄 | 같은 ID가 현재 바닐라의 서로 다른 지역에 사용됨 |
| WER | `<WER_REPORT>:2,8,37-40,259-260` | BEX64, 보고서 ID, 예외 코드/오프셋, HOI4 실행 파일 |

모드 전용 province 범위는 `<PROJECT>/map/definition.csv`에서 `13376-13409`의 행을 추출하고 바닐라 동일 ID의 RGB/속성과 대조해 산출했다. 다만 사용한 검색 명령, 입력 파일 해시와 전체 결과 목록은 사건별 산출물로 보존되지 않았다. 이 수치와 파생 판단은 마이그레이션 제안 전에 fresh scan으로 재산출해야 한다.

`D-PRE` 증거 snapshot 시각은 2026-08-31 로컬 시각 기준으로 `dlc_load.json` 13:13:05, `error.log`와 `game.log` 13:13:25, `<WER_REPORT>` 13:13:29였다. Git·경로·Workshop descriptor 상태는 최종 문서 보정 시점에 별도로 읽기 전용 확인했다. 서로 다른 시점의 자료를 하나의 실행 묶음으로 단정하지 않는다.

## 확인된 크래시 서명

조사 시점의 최신 Windows Error Reporting 자료인 `<WER_REPORT>`에서 확인했다.

- EventType: `BEX64`
- ReportIdentifier: `041a5c83-6e37-41ba-ba22-fee534ecd921`
- 예외 코드: `c0000409`
- 예외 오프셋: `000000000253c715`
- AppName: `HOI4`
- AppPath: Steam 설치 경로의 `hoi4.exe`

이전 읽기 전용 inventory에서는 동일한 코드와 오프셋을 여러 보관 보고서에서 확인했다. 다만 보고서 전체 목록을 별도 산출물로 보존하지 않았으므로 반복 횟수는 다음 재현 전에 다시 산출한다. 같은 서명의 반복은 크래시가 안정적이라는 증거지만, 그 자체만으로 문제 파일을 특정하지는 않는다.

## 핵심 증거

### CONFIRMED

1. Hearts of Korea만 활성화한 구성 `D-PRE`에서도 게임이 크래시했다.
2. 해당 실행의 `game.log`는 `Loaded 13410 provinces`를 기록했다.
3. 해당 실행의 `error.log`는 province `13410`, `13411`, `13412`, `13413`을 malformed로 보고했다.
4. 모드의 `map/definition.csv`는 ID `13409`에서 끝난다.
5. 현재 바닐라 `map/definition.csv`는 ID `13413`까지 존재한다.
6. 현재 검사에서 모드 전용 province ID 후보 범위는 `13376–13409`, 총 34개로 산출됐다. `13375`는 바닐라와 같은 province이므로 이 후보 범위에 포함하면 안 된다.
7. 모드가 사용하는 state ID `1017–1027`, 총 11개는 현재 바닐라 state ID와 충돌한다.
8. 현재 바닐라는 한국 지역에 state `1028–1031`을 추가로 가지고 있어, 구버전 모드의 한국 지역 분할과 의미상 겹친다.

6번의 범위와 개수는 소스 대조에서 확인됐지만, 검색 명령과 전체 산출물이 보존되지 않았으므로 실제 마이그레이션 입력으로 사용하기 전에 재산출한다.

### STRONGLY_SUPPORTED

1. 구버전 전역 맵 데이터가 현재 `1.19.2` 바닐라 맵의 새 province/state와 함께 로드되면서 내부 참조가 불일치한 것이 `D-PRE` 시작 크래시의 주원인이다.
2. 누락된 province 네 줄만 추가해서는 안전한 해결이 되지 않는다. state 소속, strategic region, 철도, 보급과 위치 데이터를 함께 검증하고, 필요한 항목만 재조정해야 한다.
3. 현재 바닐라와 구버전 모드의 state ID 충돌 및 전역 맵 파일 차이 때문에 단순 파일 합성은 안전하지 않다. 원작자의 의도된 override와 구형 바닐라 잔재를 구분한 최종 유효 로드 결과를 재구성해야 한다.

### UNPROVEN

1. WER 예외를 일으킨 정확한 엔진 내부 assert 또는 함수
2. 아래 임시 ID 예약 구간 후보가 필수 의존 모드와 모든 스크립트까지 포함했을 때 최종적으로 안전한지 여부
3. 맵 문제를 고친 뒤 다른 하드 크래시가 이어질지 여부
4. ID 변경 뒤 기존 세이브와 서브모드가 호환될지 여부
5. 이전 inventory가 보고한 `103`이 “중복된 서로 다른 province ID 수”인지 “첫 소속을 제외한 초과 membership 수”인지 여부
6. 바닐라와 모드 state를 단순 합성했을 때 발생하는 전체 중복 province membership의 정확한 목록과 개수
7. 정확한 Vanilla `1.16.x` 기준본과 원본 HoK의 차이 중 어느 항목이 원작자의 의도된 맵 변경인지 여부
8. `Korean Language`를 포함한 실제 지원 구성 `C`에서 동일 크래시가 같은 서명으로 재현되는지 여부

5번과 6번은 입력 목록, 검색 명령과 전체 산출물이 보존되지 않았으므로 예비 inventory 이상의 등급을 부여하지 않는다.

### DISPROVEN 또는 현재 구성에서 비활성

1. “다른 Workshop 모드가 반드시 있어야만 이 크래시가 난다”는 가설은 **현재 `dlc_load.json`과 확인된 `D-PRE` 구성의 범위에서** 반증됐다. HoK 단독 구성에서도 재현됐다.
2. HoK 단독 실행에서는 과거 다른 모드 조합에서 보였던 `events/Korea.txt`와 `events/korea.txt` 중복 이벤트 ID 오류가 나타나지 않았다. 다만 `국뽕모드 이식판`을 다시 활성화하면 별도 크래시 위험으로 돌아올 수 있다.

이 반증은 모든 playset과 모든 물리적 모드 복사본에 대한 일반 명제가 아니다. 실제 로드 경로는 launcher 로그까지 포함한 clean reproduction에서 다시 확정한다.

## 경쟁 가설 상태

| 가설 | 현재 등급 | 근거와 한계 |
|---|---|---|
| H1. 구버전 맵 데이터와 `1.19.2` 맵 데이터의 불일치가 `D-PRE` 크래시의 주원인 | STRONGLY_SUPPORTED | malformed province, definition 끝 차이, state ID 충돌이 일치함. 수정 후 재현은 아직 없음 |
| H2. `Korean Language` 미활성이 직접 크래시 원인 | UNPROVEN | 현재 재현은 의존 모드가 빠졌지만, 맵 증거와의 인과 분리 시험이 없음 |
| H3. 다른 Workshop 모드가 있어야만 크래시 | DISPROVEN within current D-PRE configuration | HoK 단독 구성에서 재현됨. 다른 playset 일반화는 금지 |
| H4. 정확한 엔진 내부 assert 또는 함수가 특정됨 | UNPROVEN | WER 코드와 오프셋은 결과 서명이며 문제 파일을 직접 특정하지 않음 |

## 필수 3-way 맵 비교 기준

현재 문서의 가장 중요한 구현 전 조건은 다음 세 기준본을 분리하는 것이다.

- `V_OLD`: 원본 모드가 마지막으로 지원한 정확한 Vanilla `1.16.x` 빌드
- `HOK_ORIGINAL`: 불변 원본 Hearts of Korea 배포본. 현재 설치본의 descriptor `1.0.0`과 마지막 알려진 릴리스 표기 `1.0.9(1)`의 관계를 먼저 확정해야 함
- `V_TARGET`: 목표 Vanilla `1.19.2.0.a729 (d245)`

개념상 원작자가 의도한 변경분은 다음과 같다.

```text
INTENDED_DELTA = HOK_ORIGINAL - V_OLD
SUCCESSOR_CANDIDATE = V_TARGET + reviewed(INTENDED_DELTA)
```

`HOK_ORIGINAL`과 `V_TARGET`의 단순 차이를 전부 원작자의 의도로 간주하지 않는다. 그 차이에는 원작의 변경, 구형 바닐라 잔재, 1.16 이후 바닐라 변경이 섞여 있다.

### 현재 기준본 확보 상태

| 입력 | 현재 상태 | 구현 전 요구사항 |
|---|---|---|
| `V_OLD` 정확한 Vanilla `1.16.x` | 정확한 patch/build/checksum 및 파일 기준본 미확보 | 정확한 기준본, 경로, 파일 목록, SHA-256 manifest |
| `HOK_ORIGINAL` | Workshop ID `2898629778` 설치본은 존재. descriptor version `1.0.0`과 마지막 알려진 릴리스 표기 `1.0.9(1)`의 관계가 미해결이며 불변 archive·manifest 없음 | 버전 의미 확인, 읽기 전용 archive, 전체 파일 목록, SHA-256 manifest |
| `V_TARGET` `1.19.2.0.a729 (d245)` | 설치 경로와 일부 파일 대조는 확인 | 전체 기준 manifest와 영향 파일 snapshot |
| `Korean Language` | Workshop ID `2743487021` 설치본 발견. version `25.11.23`, declared `1.17.*`, 현재 미활성 | `1.19.2` 지원성, 실제 로드 경로·순서, 파일·ID 영향 inventory |

정확한 `V_OLD`와 확정된 `HOK_ORIGINAL`을 확보하지 못하면 원작 변경의 의미를 `UNPROVEN`으로 남기며, 자동 병합이나 파일 단위 덮어쓰기를 승인하지 않는다.

## 맵 이식 범위

현재 모드에는 다음 전역 또는 맵 연관 파일이 있다.

- `map/definition.csv`
- `map/provinces.bmp`
- `map/heightmap.bmp`
- `map/terrain.bmp`
- `map/adjacencies.csv`
- `map/ambient_object.txt`
- `map/buildings.txt`
- `map/railways.txt`
- `map/supply_nodes.txt`
- `map/unitstacks.txt`
- strategic region `76`, `143`, `154`, `155`, `186`, `243`, `244`
- 관련 `history/states` 파일

이 파일들은 현재 바닐라와 차이가 있다는 사실만으로 원작 의도물로 분류하지 않는다. 3-way 비교에서 검증된 `INTENDED_DELTA`를 기준으로 다음 방식으로 다룬다.

- `definition.csv`: 현재 바닐라 전체를 기준으로 검증된 모드 전용 province를 개별 승인된 ID로 병합
- `provinces.bmp`: 현재 바닐라를 기준으로 원작 의도로 확인된 한국 인근 RGB·기하 변경만 국소 병합
- state: 각 land province가 정확히 한 state에 속하도록 의미 단위로 재구성
- strategic region: 현재 바닐라 파일을 기준으로 검증된 membership 변경만 병합
- railway/supply: 현재 바닐라 보급망을 보존하면서 원작 의도로 확인된 한국·만주 변경만 반영
- buildings/unitstacks: 승인된 province/state 관계와 위치를 기준으로 재검증 또는 필요한 경우 재생성
- heightmap/terrain: 현재 형식과 팔레트를 보존하고 검증된 로컬 픽셀만 반영
- ambient objects: 현재 바닐라에 원작 의도로 확인된 객체만 추가
- `adjacencies.csv`: 합법적인 `-1` sentinel/종료 행을 보존하고, 구버전 행을 자동 승계하지 않으며 현재 바닐라에 필요한 실제 연결만 판단

현재 descriptor에 `replace_path`가 없으므로 모드에 없는 맵 파일은 통상 바닐라 상속을 유지한다. 다만 `heightmap.bmp`와 `terrain.bmp` 변경은 상속되는 `rivers.bmp`, `trees.bmp`, `cities.bmp`, `world_normal.bmp` 등과의 정렬도 감사해야 한다. descriptor가 바뀌면 이 전제를 다시 확인한다.

## 임시 충돌 회피용 ID 예약 구간 후보 — 적용 금지

다음은 빈 번호 공간 후보를 계산한 결과일 뿐이며, 개별 엔티티의 의미 매핑이나 구현 승인이 아니다.

| Entity | 원본 모드 범위 | 임시 예약 구간 후보 | 계산 오프셋 | 상태 |
|---|---:|---:|---:|---|
| Province | `13376–13409` | `13414–13447` | `+38` | 후보, 미승인 |
| State | `1017–1027` | `1082–1092` | `+65` | 후보, 미승인 |

현재 바닐라 최대값은 province `13413`, state `1081`로 확인됐다. 그러나 이 연속 범위가 비어 있다는 사실만으로 개별 지역의 의미 매핑이 성립하지 않는다.

실제 마이그레이션 제안에는 각 엔티티별로 다음을 기록한다.

- entity type과 지역 이름
- 기존 ID와 후보 신규 ID
- province의 경우 RGB와 기하적 정체성
- 기존 state·strategic region membership
- 현재 바닐라 또는 의존 모드와의 충돌 근거
- 모든 파일·문맥별 참조 위치
- 세이브·서브모드 영향
- 증거 등급과 승인 상태

적용 전 필수 작업:

1. `Korean Language`와 실제 지원 playset 전체의 ID 공간 스캔
2. state 문맥과 province 문맥을 분리한 전체 참조 목록 생성
3. 파일명, scripted trigger/effect, focus, event, decision, AI, OOB, 철도·보급 참조 검사
4. 개별 old ID → new ID 의미 매핑표 작성
5. 세이브·서브모드 비호환 영향에 대한 사용자 결정

이전 inventory는 state ID 관련 참조를 21개 파일의 약 307개 문맥과 11개 state 파일명, 모드 전용 province ID 참조를 18개 파일의 약 712개로 보고했다. 검색 명령과 전체 결과 목록을 보존하지 않았으므로 이 수는 작업 규모를 가늠하는 임시 추정치일 뿐이다. **Implementation 직전이 아니라 Migration Decision 제안 전에** 문맥별 입력과 산출물을 보존하며 다시 계산한다.

`1017–1027` 같은 숫자는 다른 문맥의 province 번호, 수치, 날짜 또는 다른 ID로도 쓰일 수 있으므로 전역 숫자 치환은 금지한다. `+38`과 `+65` 역시 변환 공식으로 사용하지 않는다.

## 맵 이외의 미검증 오류 inventory

아래 항목은 이전 조사에서 콘텐츠 손상 또는 후속 오류 위험으로 기록됐지만, 이 문서에 로그 위치와 소스 위치가 남아 있지 않다. 따라서 현재 시작 크래시의 구현 작업 목록이 아니라 `UNVALIDATED INVENTORY`로 취급한다.

| 항목 | 로그 위치 | 소스 위치 | 등급 | 현재 시작 크래시와의 관계 |
|---|---|---|---|---|
| MIO include/trait graph 오류와 `generic_train_organization` 누락 | 미기록 | 미기록 | UNPROVEN | 직접 원인 미확인 |
| 일본 decision/category 오류 및 누락된 mission 참조 | 미기록 | 미기록 | UNPROVEN | 후속 콘텐츠 오류 가능성 |
| focus/event/on_action의 잘못된 character/effect 참조 | 미기록 | 미기록 | UNPROVEN | 후속 초기화·기능 오류 가능성 |
| division name group `JAP_MIL_02` 누락 | 미기록 | 미기록 | UNPROVEN | 현재 WER과 직접 연결되지 않음 |
| doctrine/technology 데이터베이스 객체의 잘못된 참조 | 미기록 | 미기록 | UNPROVEN | 후속 초기화·기능 오류 가능성 |
| `cl_tech` unknown 항목과 일부 AI strategy 형식 오류 | 미기록 | 미기록 | UNPROVEN | 현재 WER과 직접 연결되지 않음 |
| focus icon, bookmark, descriptor, 44.1 kHz 음원 관련 경고 | 미기록 | 미기록 | UNPROVEN | 비치명 경고 가능성, 재분류 필요 |

맵 크래시가 제거되면 이 항목들이 다음 초기화 차단 또는 게임 내 기능 오류로 드러날 수 있다. 다음 조사에서는 각 항목에 정확한 로그 위치, 소스 위치, 증거 등급과 현재 사건과의 관계를 붙여 별도 사건으로 추적한다.

## 다음 작업 단계

### 1. Diagnostic continuation

Implementation 승인으로 해석하지 않는다.

1. 현재 로그, WER, launcher 설정과 검사 결과를 사건별 증거 bundle로 보존한다.
2. `D-PRE`의 누락된 재현 정보를 가능한 범위에서 보완하고, 이후 실행부터 정확한 절차를 기록한다.
3. 실제 지원 playset, DLC, 언어 설정, `Korean Language` 버전과 실제 로드 경로를 확정한다.
4. 원본 archive와 각 기준본의 파일 목록·SHA-256 manifest를 생성한다.
5. 정확한 `V_OLD`, `HOK_ORIGINAL`, `V_TARGET`의 3-way 비교를 수행한다.
6. province/state/RGB/membership/reference inventory를 fresh scan으로 재산출하고 명령과 전체 결과를 보존한다.
7. 확인된 연결 문서 링크와 해당 시점의 문서 버전을 사건별 증거 bundle에 기록한다.

### 2. Migration Decision

1. 검증된 원작 맵 delta를 목록화한다.
2. 각 province/state의 개별 old ID → new ID 의미 매핑표를 작성한다.
3. 현재 바닐라의 한국 state `1028–1031`과 원작 분할을 어떻게 통합할지 결정한다.
4. 기존 세이브와 서브모드 호환성 정책을 결정한다.
5. 임시 ID 예약 구간의 실제 충돌 여부를 필수 의존 모드까지 포함해 재검증한다.
6. 사용자에게 매핑표와 호환성 영향을 제시하고 별도 승인을 받는다.

### 3. Implementation

영구 ID 마이그레이션과 맵 변경이 명시적으로 승인된 뒤에만 수행한다.

1. 승인된 매핑과 `INTENDED_DELTA`만 의미 단위로 병합한다.
2. 숫자 전역 치환과 파일 단위 구버전 덮어쓰기를 사용하지 않는다.
3. 무관한 콘텐츠, 밸런스, 포맷과 인코딩을 변경하지 않는다.
4. 각 변경을 되돌릴 수 있는 작은 diff로 유지한다.

### 4. Validation

1. 정적 맵 무결성 검사를 통과한다.
2. `D-PRE`와 동일 조건의 `D-POST`를 실행해 로그와 WER을 비교한다.
3. 실제 지원 구성 `C-POST`를 실행한다.
4. 새 게임, 지도 표시, 국가 선택, unpause를 확인한다.
5. 한국·만주·쓰시마의 state, ownership, cores, victory points, supply, railway, adjacency, buildings와 positions를 검사한다.
6. 승인된 경우 save/load 및 영향 bookmark를 검증한다.
7. 남은 비맵 오류를 별도 사건으로 분리한다.

성공 실행에는 새 WER이 없어야 한다. 계속 크래시할 때만 예외 코드와 오프셋을 이전 사건과 대조한다. `D-POST` 통과만으로 `C-POST`까지 성공했다고 판정하지 않는다.

## 계승판 배포 경계

이 프로젝트는 원본 Hearts of Korea를 계승·복구해 새 Workshop 항목으로 배포하는 프로젝트다.

- 원본 Workshop ID `2898629778`은 출처와 크레딧용으로 보존한다.
- 원본 항목의 `remote_file_id`를 신규 계승판에 사용하거나 원본 항목을 덮어쓰지 않는다.
- 원 제작자와 기존 기여자의 저작·기여 이력을 명확히 보존한다.
- 실제 업로드, 공개 제목, 설명, 대표 이미지, visibility와 changelog 변경은 사용자의 명시적 게시 지시가 있을 때만 수행한다.
- 구체적인 제3자 권리 충돌이나 사용자가 설명한 계승 권한과 모순되는 자료가 발견된 경우에만 권리 문제로 안전 정지한다.

## 이번 문서 보정의 변경 영향

- 다운로드 수정본의 무결성을 제공된 SHA-256 목록과 대조한 뒤, 프로젝트의 `CRASH_DEBUGGING_RUNBOOK.md`와 이 조사 문서에 반영했다.
- 현재 저장소 경로, Git 기준선, launcher 경로, 설치된 원본 Workshop 및 `Korean Language` descriptor와 연결 문서는 읽기 전용으로 재확인했다.
- 실제 `<PROJECT>` 모드 스크립트, 맵 데이터, descriptor, Steam 원본, Workshop 파일, 로그, WER와 launcher 설정은 수정하지 않았다.
- 게임과 검사 스크립트는 실행하지 않았다.
- 이번 문서 변경에 대한 commit, push 또는 Workshop 업로드는 수행하지 않았다.
- 따라서 크래시 원인 판정은 기존 `D-PRE` 증거 범위에 한정되며, 현재 launcher 경로로 새 실행이 가능하다고 주장하지 않는다.
