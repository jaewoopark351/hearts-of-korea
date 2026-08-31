# 2026-08-31 시작 크래시 조사

## 상태

- 조사 모드: **Diagnostic**
- 현재 결론: 맵 데이터의 버전 불일치가 현재 시작 크래시의 주원인으로 **강하게 뒷받침됨**
- 수정 상태: 미수정
- 게임 재실행 상태: 이번 문서 작성 과정에서는 실행하지 않음

이 결론은 수정 후 A/B 재현 시험 전까지 “확인됨”으로 승격하지 않는다. 엔진 내부에서 정확히 어떤 검사가 실패했는지는 미확인이다.

## 기준 환경

- 경로 별칭:
  - `<PROJECT>`: `C:\hoi\hearts of korea`
  - `<HOI4_INSTALL>`: `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`
  - `<HOI4_USER_DATA>`: `C:\Users\<USER>\OneDrive\문서\Paradox Interactive\Hearts of Iron IV`
  - `<WER_REPORT>`: `C:\ProgramData\Microsoft\Windows\WER\ReportArchive\AppCrash_hoi4.exe_41f0a696844af03db9895fd87a56c21f7591a29_4a5fc6d1_041a5c83-6e37-41ba-ba22-fee534ecd921\Report.wer`
- Git 기준선: `<PROJECT>`는 조사 시점에 Git 저장소로 인식되지 않음
- 알려진 upstream: Hearts of Korea, Workshop ID `2898629778`, 마지막 알려진 버전 `1.0.9(1)`, 마지막 선언 호환 버전 `1.16`
- 게임 버전: Operation Postern `v1.19.2.0.a729 (d245)`
- 현재 fork descriptor 이름: `하츠 오브 코리아 Hearts of Korea[1.19 호환](씹덕 모드 제작자 개정)`
- 현재 fork descriptor 버전: `1.0.0`
- 현재 fork descriptor 지원 버전: `1.19.*`
- 선언된 의존 모드: `Korean Language`
- 현재 launcher 설정에서 확인된 활성 모드: `mod/hearts of korea.mod`만 활성
- launcher `.mod`의 `path`: `<PROJECT>`를 가리킴
- 현재 launcher playset 이름: 기록되지 않음
- 제한 사항: 정확한 보유/활성 DLC 전체 목록은 별도로 기록되지 않음

현재 재현은 선언된 필수 의존 모드가 빠진 HoK 단독 구성이다. 따라서 최종 지원 구성 검증에는 `Korean Language`를 포함한 별도 실행 기록이 필요하다. `dlc_load.json`의 `disabled_dlcs`가 비어 있다는 사실은 보유·활성 DLC 전체 목록의 증거가 아니다.

저장소 descriptor 전체와 launcher descriptor를 조사했을 때 `replace_path`와 `remote_file_id` 항목은 없었다. launcher 설정의 활성 `.mod`와 그 `path`, 그리고 모드 `definition.csv`의 province 수와 일치하는 runtime 로그를 함께 볼 때 `<PROJECT>` 복사본이 로드됐다는 판단은 강하게 뒷받침된다. 다음 clean reproduction에서는 launcher 로그까지 보존해 실제 물리 경로를 다시 확정한다.

## 감사 가능한 증거 위치

개인 식별 경로는 별칭으로 적었다. 현재 로그는 다음 실행에서 덮어써질 수 있으며, 이번에는 별도 원본 사본을 만들지 않았다.

| 증거 | 위치 | 확인 내용 |
|---|---|---|
| 저장소 descriptor | `<PROJECT>/descriptor.mod:1,8-12` | 버전, 이름, `Korean Language`, `supported_version`; 전체 12줄에 `replace_path`와 `remote_file_id` 없음 |
| launcher descriptor | `<HOI4_USER_DATA>/mod/hearts of korea.mod:1,8-13` | 저장소와 같은 핵심 필드, `<PROJECT>`를 가리키는 `path` |
| 현재 launcher 설정 | `<HOI4_USER_DATA>/dlc_load.json:1` | `mod/hearts of korea.mod`만 enabled, 명시적 disabled DLC 없음 |
| province 로드 수 | `<HOI4_USER_DATA>/logs/game.log:2` | `[13:13:25] Loaded 13410 provinces.` |
| malformed province | `<HOI4_USER_DATA>/logs/error.log:29-32` | `[13:13:21]`에 `13410`, `13413`, `13412`, `13411` 순으로 malformed |
| 모드 definition 끝 | `<PROJECT>/map/definition.csv:13411` | 마지막 정의 ID가 `13409` |
| 바닐라 definition 끝 | `<HOI4_INSTALL>/map/definition.csv:13410-13414` | ID `13409-13413`; 마지막 정의 ID가 `13413` |
| 모드 custom state | `<PROJECT>/history/states/1017-*.txt`부터 `1027-*.txt`의 내부 `id` 줄 | 모드가 `1017-1027`을 서로 다른 한국·만주·쓰시마 state로 정의 |
| 바닐라 state 충돌 | `<HOI4_INSTALL>/history/states/1017 - Trung Bo.txt`부터 `1027 - Bataan.txt`의 내부 `id` 줄 | 같은 ID가 현재 바닐라의 서로 다른 지역에 사용됨 |
| WER | `<WER_REPORT>:2,8,37-40,259-260` | BEX64, 보고서 ID, 예외 코드/오프셋, HOI4 실행 파일 |

모드 전용 province 범위는 `<PROJECT>/map/definition.csv`에서 `13376-13409`의 행을 추출하고 바닐라 동일 ID의 RGB/속성과 대조해 산출했다. 구현 전에는 사용한 검색 명령, 입력 파일 해시와 전체 결과 목록까지 사건별 증거 묶음에 보존해야 한다.

증거 snapshot 시각은 2026-08-31 로컬 시각 기준으로 `dlc_load.json` 13:13:05, `error.log`와 `game.log` 13:13:25, `<WER_REPORT>` 13:13:29였다. 로그 본문 시각과 파일 수정 시각을 함께 사용하며, 서로 다른 실행의 자료를 한 묶음으로 단정하지 않는다.

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

### 확인됨

1. Hearts of Korea만 활성화한 구성에서도 게임이 크래시했다.
2. 해당 실행의 `game.log`는 `Loaded 13410 provinces`를 기록했다.
3. 해당 실행의 `error.log`는 province `13410`, `13411`, `13412`, `13413`을 malformed로 보고했다.
4. 모드의 `map/definition.csv`는 ID `13409`에서 끝난다.
5. 현재 바닐라 `map/definition.csv`는 ID `13413`까지 존재한다.
6. 모드 전용 province ID는 `13376–13409`, 총 34개다. `13375`는 바닐라와 같은 province이므로 모드 전용 범위에 포함하면 안 된다.
7. 모드 전용 state ID `1017–1027`, 총 11개는 현재 바닐라 state ID와 충돌한다.
8. 현재 바닐라는 한국 지역에 state `1028–1031`을 추가로 가지고 있어, 구버전 모드의 한국 지역 분할과 의미상 겹친다.

### 강하게 뒷받침됨

1. 구버전 전역 맵 데이터가 현재 1.19.2 바닐라 맵의 새 province/state를 가리면서 내부 참조가 불일치한 것이 현재 시작 크래시의 주원인이다.
2. 누락된 province 네 줄만 추가해서는 안전한 해결이 되지 않는다. state 소속, strategic region, 철도, 보급, 위치 데이터까지 함께 재조정해야 한다.
3. 바닐라와 모드 state를 그대로 단순 합성하면 동일 land province가 둘 이상의 state에 소속되는 다수의 충돌이 생긴다. 따라서 의도한 override와 실제 충돌을 구분한 최종 유효 로드 결과를 재구성해야 한다.

### 미확인

1. WER 예외를 일으킨 정확한 엔진 내부 assert 또는 함수
2. 아래 임시 ID 후보가 필수 의존 모드와 모든 스크립트까지 포함했을 때 최종적으로 안전한지 여부
3. 맵 문제를 고친 뒤 다른 하드 크래시가 이어질지 여부
4. ID 변경 뒤 기존 세이브와 서브모드가 호환될지 여부
5. 이전 inventory가 보고한 `103`이 “중복된 서로 다른 province ID 수”인지 “첫 소속을 제외한 초과 membership 수”인지 여부. 입력 목록과 산출물이 보존되지 않아 정확한 수치는 미확인이다.

### 반증됨 또는 현재 구성에서 비활성

1. 다른 Workshop 모드가 반드시 있어야만 이 크래시가 난다는 가설은 반증됐다. HoK 단독 구성에서도 재현됐다.
2. HoK 단독 실행에서는 과거 다른 모드 조합에서 보였던 `events/Korea.txt`와 `events/korea.txt` 중복 이벤트 ID 오류가 나타나지 않았다. 다만 `국뽕모드 이식판`을 다시 활성화하면 별도 크래시 위험으로 돌아올 수 있다.

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

이 파일들은 현재 바닐라와 차이가 있으므로 파일 단위 덮어쓰기가 아니라 다음 방식으로 다뤄야 한다.

- `definition.csv`: 현재 바닐라 전체를 기준으로 모드 전용 province만 충돌 없는 ID로 병합
- `provinces.bmp`: 현재 바닐라를 기준으로 의도된 한국 인근 RGB/기하 변경만 국소 병합
- state: 각 land province가 정확히 한 state에 속하도록 의미 단위 재구성
- strategic region: 현재 바닐라 파일을 기준으로 관련 membership만 병합
- railway/supply: 현재 바닐라 보급망을 보존하면서 의도된 한국·만주 변경만 반영
- buildings/unitstacks: 새 province/state 관계와 위치를 기준으로 재검증 또는 재생성
- heightmap/terrain: 현재 형식과 팔레트를 보존하고 검증된 로컬 픽셀만 반영
- ambient objects: 현재 바닐라에 모드 의도물만 추가
- `adjacencies.csv`: 합법적인 `-1` sentinel/종료 행을 보존하고, 구버전 행을 자동 승계하지 않으며 현재 바닐라에 필요한 실제 연결만 판단

현재 descriptor에 `replace_path`가 없으므로 모드에 없는 맵 파일은 통상 바닐라 상속을 유지한다. 다만 `heightmap.bmp`와 `terrain.bmp` 변경은 상속되는 `rivers.bmp`, `trees.bmp`, `cities.bmp`, `world_normal.bmp` 등과의 정렬도 감사해야 한다. descriptor가 바뀌면 이 전제를 다시 확인한다.

## 임시 마이그레이션 후보 — 적용 금지

다음은 충돌을 피할 수 있는지 검토하기 위한 **계산 후보**일 뿐이며, 구현 승인이 아니다.

- province `13376–13409` → `13414–13447` (`+38`)
- state `1017–1027` → `1082–1092` (`+65`)

현재 바닐라 최대값은 province `13413`, state `1081`로 확인됐다. 그러나 적용 전에는 다음을 다시 해야 한다.

1. `Korean Language`와 실제 지원 playset 전체의 ID 공간 스캔
2. state 문맥과 province 문맥을 분리한 전체 참조 목록 생성
3. 파일명, scripted trigger/effect, focus, event, decision, AI, OOB, 철도·보급 참조 검사
4. 세이브·서브모드 비호환 영향에 대한 사용자 결정

이전 inventory는 state ID 관련 참조를 21개 파일의 약 307개 문맥과 11개 state 파일명, 모드 전용 province ID 참조를 18개 파일의 약 712개로 보고했다. 검색 명령과 전체 결과 목록을 보존하지 않았으므로 이 수는 작업 규모를 가늠하는 임시 추정치일 뿐이다. 구현 직전에 문맥별 입력과 산출물을 보존하며 다시 계산한다. `1017–1027` 같은 숫자는 다른 문맥의 province 번호로도 쓰이므로 전역 숫자 치환은 금지한다.

## 맵 이외의 남은 오류

아래는 콘텐츠 손상 또는 후속 오류 위험이지만, 현재 WER 크래시의 직접 원인으로 확인되지는 않았다.

- MIO include/trait graph 오류와 `generic_train_organization` 누락
- 일본 decision/category 오류 및 누락된 mission 참조
- focus/event/on_action의 잘못된 character/effect 참조
- division name group `JAP_MIL_02` 누락
- doctrine/technology 데이터베이스 객체의 다수 잘못된 참조
- `cl_tech` unknown 항목과 일부 AI strategy 형식 오류
- focus icon, bookmark, descriptor, 44.1 kHz 음원 관련 경고

맵 크래시가 제거되면 이 항목들이 다음 초기화 차단 또는 게임 내 기능 오류로 드러날 수 있으므로 별도 사건으로 추적한다.

## 다음 승인 작업 제안

사용자가 Implementation을 승인하면 다음 순서가 안전하다.

1. 필수 의존 모드를 포함한 실제 지원 playset, DLC, 언어 설정, 실제 로드 경로와 기준 로그를 확정한다.
2. 현재 바닐라 1.19.2 맵을 기준으로 모드가 의도한 지리 변경만 목록화한다.
3. 전체 참조와 의존 모드까지 스캔해 ID 마이그레이션 표를 확정하고 사용자에게 호환성 영향을 확인받는다.
4. 맵 파일을 의미 단위로 병합한다. 숫자 전역 치환은 사용하지 않는다.
5. 정적 무결성 검사를 통과한 뒤, 승인된 경우에만 동일 조건 A/B 실행으로 로그와 새 WER 유무를 비교한다. 성공 실행에는 WER이 없어야 하며, 계속 크래시할 때만 예외 코드·오프셋을 대조한다.
6. 남는 콘텐츠 오류를 맵 크래시와 분리해 우선순위별로 처리한다.

## 이번 문서화 작업의 변경 영향

- 사용자가 프로젝트 내부 문서 생성을 명시적으로 요청해 생성한 것은 `docs/` 아래의 문서뿐이다.
- 모드 스크립트, 맵 데이터, descriptor, Steam 원본, Workshop 파일, 로그와 런처 설정은 수정하지 않았다.
- 이 프로젝트는 조사 시점에 Git 저장소로 인식되지 않았으므로 커밋이나 푸시는 수행하지 않았다.
