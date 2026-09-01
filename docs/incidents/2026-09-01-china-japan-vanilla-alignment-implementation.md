# 2026-09-01 중국·만주·일본 1.19.2 바닐라 정렬 구현 기록

## 판정

- 작업 모드: **Implementation / 후속 static validation / runtime 재검증 중**
- 목표 게임: HOI4 `Operation Postern v1.19.2.0.a729 (d245)`
- 기준 데이터: 설치된 목표 버전 Vanilla (`V_TARGET`)
- 보존 우선순위: **HoK 한국 > 중국·만주·일본의 구형 HoK 변경**
- production 구현: **적용**
- production 정적 검사: **TARGETED PASS — 쓰시마 마이그레이션 표적 오류 0, 전체 scanner raw result는 vanilla-shared ERROR 118 때문에 FAIL 유지**
- 최초 `D-CJ-POST`: **FAIL — state ID gap으로 map load crash**
- post-fix 런타임 검증: **PASS — HoK-only map 진입, 1/7/30일 진행과 정상 종료**
- 중국·산둥 색상 화면 확인: **UNPROVEN**
- 일본 historical AI의 중일전쟁 진행: **UNPROVEN**
- 최초 runtime 실패 root cause: **CONFIRMED — effective state ID `1085–1087` 구멍**
- 후속 수정의 exact `D-CJ-POST` 크래시 제거: **CONFIRMED — bounded fix 뒤 동일 HoK-only gate 통과**
- Git commit·push: **수행하지 않음**

이번 변경은 사용자가 승인한 정책에 따라 중국·만주·일본을 HOI4 1.19.2 바닐라에 맞추고, 그 과정에서 HoK 한국과 독립 한국에 필요한 최소 접점만 남긴 구현이다. 구형 HoK 일본 파일을 현재 바닐라 파일로 무조건 복사하지 않았다. 모드에 파일이 없으면 같은 상대경로의 설치된 바닐라 정의가 로드되는 곳은 stale override를 삭제해 `V_TARGET`을 상속한다. 한국 state 분할 때문에 바닐라의 완전 상속만으로 의미가 부족한 파일에 한해서만 target-derived KOR bridge를 둔다.

이 기록은 [중국·일본 바닐라 정렬 정책](../CHINA_JAPAN_VANILLA_ALIGNMENT_POLICY.md)의 실제 적용 기록이다. 시작 크래시를 제거한 이전 맵 재구성은 [target-native 맵 구현 기록](2026-09-01-target-native-map-implementation.md)에 별도로 남긴다.

## 범위와 기준선

- Git branch: `main`
- 구현 시작 HEAD: `8a6d075fb64e9bcdc88bfdf8122ab261be7e43ec`
- 구현 시작 시 `origin/main`: 같은 commit
- 구현 시작 working tree: clean
- production mod root: `C:\hoi\hearts_of_korea`
- target root: `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`
- live log root: `C:\Users\jaewo\OneDrive\문서\Paradox Interactive\Hearts of Iron IV\logs`
- base-game 설치본, Workshop 관리 복사본, save, playset과 launcher 설정: 수정하지 않음
- descriptor와 `Korean Language` 계약: 이번 구현에서 수정하지 않음
- 무관한 HoK 한국 밸런스·focus·event·asset: 보존

구현 전 live 로그는 다음 불변 bundle로 보존했다.

- 실행 ID: `CJ-PRE-LOGS-193412`
- 구성 메타데이터: HoK only
- evidence: `<PROJECT>/.local-artifacts/incidents/2026-09-01-china-japan-alignment/CJ-PRE-LOGS-193412/`
- `SHA256SUMS.tsv` SHA-256: `1E48A31BC0604CA901CED00E527CE07394072317EBD56B167B1C61E6AAF8CEF5`

이 bundle은 구현 전 로그를 식별하지만 historical AI checkbox, 모든 game rule, DLC와 종료 방식까지 완전한 재현 사건으로 고정한 것은 아니다. 따라서 로그에서 관찰된 일본 행동은 구현 방향의 증거이며 post-runtime 판정을 대신하지 않는다.

최초 post-implementation 실패는 별도 불변 bundle로 보존했다.

- 실행 ID: `D-CJ-POST-205045`
- 구성: HoK project mod only, `hoi4.exe --debug`, runtime checksum `2bfa`
- 시작: 2026-09-01 20:51:55 +09:00
- 싱글플레이 시작: 20:58:20
- crash: 20:58:22
- evidence: `<PROJECT>/.local-artifacts/incidents/2026-09-01-china-japan-alignment/D-CJ-POST-205045-FAIL-205822/`
- 핵심 파일: `capture.json`, `runtime-logs/error.log`, `runtime-logs/game.log`, `crash/exception.txt`, `crash/meta.yml`
- `SHA256SUMS.tsv` SHA-256: `8E309FB61910BC782D229C514ACF68A16253D06729C15FFBF3AA79E0F11D96E6`

이 bundle은 `C0000005 EXCEPTION_ACCESS_VIOLATION` at `0x00007FF62E2D3BD6`, `IsMapInGoodState: no`, 그리고 같은 실행의 state ID 누락 로그를 함께 고정한다.

## 구현 전 증거와 원인 분류

### 중국·산둥

- 모드의 구형 `common/countries/colors.txt`가 target의 현행 `CHI`, `SND`와 여러 중국계 tag 정의를 가렸다. `CONFIRMED`
- 중국·만주 state `1085–1087`과 연결 state·전략 지역·보급망은 1.19.2 target 분할과 달랐다. `CONFIRMED`
- `provinces.bmp`의 target 대비 1,889 pixel 차이는 모두 한국 crop 안에 있고 중국·만주 geometry 차이는 0이었다. 중국 province를 다시 칠할 근거는 없었다. `CONFIRMED`
- stale 전역 색상 snapshot이 사용자가 본 산둥·중국 정치색 이상 현상의 주원인이다. `STRONGLY_SUPPORTED` — 같은 화면의 post 비교가 필요하다.

### 일본과 중일전쟁

- 구형 exact-path `common/national_focus/japan.txt`는 일본 focus 128개만 등록했지만 target은 449개이며, 현행 historical plan이 요구하는 focus가 다수 누락됐다. `CONFIRMED`
- 구형 일본 AI, decision, character, MIO, country history와 OOB에서 1.19.2 ID 불일치가 확인됐다. `CONFIRMED`
- 구현 전 장기 `game.log`에서는 일본이 한국과 남방전쟁은 시작했지만 1942년까지 CHI·중국 군벌과의 전쟁은 기록되지 않았다. `CONFIRMED` — 해당 실행에 한정한다.
- 구형 일본 focus/AI와 현행 historical plan·event·decision의 version skew가 중일전쟁 미발생의 주원인이다. `STRONGLY_SUPPORTED` — 정렬 뒤 같은 조건의 AI 진행 확인이 필요하다.

이 중국·일본 version skew가 과거 startup crash의 직접 원인이었다는 주장은 하지 않는다. 과거 시작 크래시는 별도 사건에서 target과 불일치한 맵·`buildings.txt` 데이터로 분리됐다.

## 적용 내용

아래 1–5절은 최초 중국·만주·일본 정렬 적용을 기록한다. 당시 쓰시마는 `1088`에 남아 있었으며, 이 역사적 적용 결과는 뒤의 **D-CJ-POST 실패와 승인된 후속 마이그레이션** 절이 쓰시마 ID에 한해 supersede한다.

### 1. 중국·만주 지도와 색상

- state `1085`(간도), `1086`(안둥), `1087`(헤이허)를 제거하고 target source states `328`, `714`, `715`, `716`, `717`, `761`의 구형 override도 제거해 1.19.2 state를 상속한다.
- strategic regions `155`, `243`의 구형 override를 제거해 target membership을 복원한다.
- `history/units/MAN_1936.txt`와 `common/units/names_ships/CHI_ship_names.txt`의 stale snapshot을 제거해 target을 상속한다.
- `map/buildings.txt`는 target의 비한국 행과 승인된 HoK 한국 state 행만 합성했다. 최초 정렬 시 제거된 `1085–1087` 행은 남기지 않았고 쓰시마 `1088` 행은 보존했다. 이 마지막 ID 선택은 후속 마이그레이션에서 수정했다.
- `map/railways.txt`에서 HoK 만주 branch 8개를 제거하고, `map/supply_nodes.txt`에서 만주 node `11781`만 제거했다. HoK 한국 rail·node는 유지했다.
- `provinces.bmp`, `definition.csv`, `unitstacks.txt`와 한국 strategic region `186`은 이번 정렬에서 바꾸지 않았다. 중국·만주 province RGB를 새로 지정하지 않았다.
- KOR focus·event·decision·on_action의 `1085–1087` state-context 참조를 제거했다. 같은 숫자의 province 참조는 state로 오인해 일괄 변경하지 않았다.
- `gookppong_on_actions`에서 제거 state의 시작 건물·부대 효과는 지리적 target parent `717`, `328`, `716`, `714`로 명시적으로 매핑했다. 간도 claim·core·transfer처럼 target parent 전체로 확대하면 의미가 달라지는 효과는 제거했다.
- 중국 군벌을 통합하고 공장·OOB·AI를 추가하던 `jungppong` on-action과 game rule, 관련 localisation을 제거했다. 삭제된 구형 `CHI_DE_HISTORICAL`을 요구하는 경로도 남기지 않았다.

states `1085–1087`을 사용하는 기존 세이브와 서브모드는 호환 대상으로 주장하지 않는다. 이는 임시 offset 치환이 아니라 target state topology로 돌아가는 의도된 persistent ID 변경이다.

### 2. 전역 국가 registry

- `common/countries/colors.txt`는 target을 기준으로 복원하고 HoK KOR 파란색과 KJP·KCH·RKY·TWN 색상만 보존했다. target `CHI`·`SND`와 현행 중국계 tag 정의를 그대로 유지한다.
- `common/countries/cosmetic.txt`는 target을 기준으로 `KOR_Goguryeo`, `KOR_PRK_communism`, `KJP_PSJ`만 추가했다.
- `common/names/00_names.txt`는 target schema를 기준으로 KOR 이름을 보강하고 KJP·KCH·RKY·TWN만 추가했다.
- `common/characters/KOR.txt`는 target KOR character와 HoK 한국 character를 합쳐 73개 유효 정의로 만들고 case-insensitive 중복 없이 target exact ID `KOR_syngman_rhee`를 사용했다.
- target 1.19.2가 이미 정의하는 `ANU`의 HoK country, country history와 tag override를 제거했다. target과 충돌하던 ANU flag 12개와 localisation 11개도 제거해 국가 정의·표시를 함께 target에 맞췄다.
- target 전역 파일을 가릴 수밖에 없는 generic MIO, intelligence agency, difficulty, advisor, special-project effect와 medal trigger는 target을 기준으로 다시 만들고 KOR 정의·제외 조건만 유지했다.
- `events/ElectionEvents.txt`는 target을 기준으로 복원하고, HoK 한국의 자체 선거 흐름을 보호하는 기존 KOR guard 14개만 다시 적용했다.
- 24 MB 규모의 구형 exact-path `common/scripted_localisation/FR_SCRIPTING_FULL_AUTOMATED.txt`를 제거해 target을 상속한다.

### 3. 일본의 target 상속

다음 stale exact-path 파일은 현재 바닐라 파일을 저장소에 복사하지 않고 삭제했다. 따라서 HOI4 1.19.2의 같은 상대경로 정의가 직접 로드된다.

- `common/national_focus/japan.txt`
- `common/ai_strategy/JAP.txt`
- `common/ai_strategy_plans/JAP_alternate_strategy_plan.txt`
- `common/characters/JAP.txt`
- `common/units/names_divisions/JAP_names_divisions.txt`
- 일본 본토 state `282`, `530`, `531`, `536`, `537`

다음 HoK 일본 additive 시스템도 제거했다.

- `common/ai_strategy/JAP_HoK.txt`
- `common/decisions/JAP_HoK_decision.txt`와 category
- `events/japan_HoK.txt`
- `common/ideas/democratic_japan.txt`
- `common/military_industrial_organization/organizations/JAP_HoK_organization.txt`
- `common/peace_conference/ai_peace/JAP_HoK.txt`
- `common/on_actions/buff_japan_if_japan_is_ai_on_actions.txt`

이에 따라 초기 정렬에서는 HoK의 일본 AI buff, 구형 민주 일본 경로와 1939년 한국 최후통첩·강제 전쟁이 의도적으로 사라졌다. 일본의 focus와 historical plan은 설치된 1.19.2 바닐라를 따라야 한다.

#### 3.1 후속 승인: 1939년 대한전쟁 최소 복구

사용자의 후속 승인으로 강제 대한전쟁 제거만 일부 supersede했다. target-derived `common/decisions/JAP.txt`에 AI 전용 `jap_warning_to_korea`와 `jap_ultimatum_to_korea`를 현행 형식으로 추가하고, `common/decisions/categories/JAP_HoK_decision_category.txt`에는 `JAP_war_on_korea_category` 하나만 복구했다. 호출은 실제 이벤트 ID와 같은 lowercase `kor_events.20`·`kor_events.16`으로 정렬했고 각 decision은 `cost = 0`, `fire_only_once = yes`를 명시한다.

구형 `common/decisions/JAP_HoK_decision.txt`, 일본 focus, AI buff, 추가 사단, `jap_attack_Rhee_korea`, 사할린 decision과 나머지 HoK 일본 시스템은 복구하지 않았다. `kor_events.16`의 현행 `take_state_focus`·`generator = { 525 }` 계약과 기존 대한국 AI strategy를 재사용한다. 전용 회귀 검사 6개와 전체 도구 테스트 33개는 통과했지만, 수정 전부터 실행 중인 HOI4 프로세스에는 이 변경이 로드되지 않으므로 1936 새 게임의 1939년 경고·최후통첩·실제 선전포고와 중일전쟁 병행은 아직 `UNPROVEN`이다.

### 4. 독립 한국과 한국 9도 bridge

완전 상속만으로는 target이 모르는 추가 한국 states `1082–1084`와 독립 KOR 시작 상태를 처리할 수 없다. 다음 파일은 target 1.19.2를 base로 두고 승인된 KOR 차이만 적용했다.

- `common/decisions/JAP.txt`, `common/decisions/KOR.txt`
- `common/scripted_triggers/JAP_scripted_triggers.txt`
- `common/national_focus/china_shared_TSR.txt`
- `events/WTT_Japan.txt`, `events/SEA_Japan.txt`
- `common/peace_conference/ai_peace/USA.txt`, `SOV.txt`
- `common/on_actions/14_sea_on_actions.txt`
- `common/bookmarks/the_gathering_storm.txt`
- `history/countries/JAP - Japan.txt`
- `history/units/JAP_1936.txt`, `JAP_1936_nsb.txt`, `JAP_1936_naval.txt`, `JAP_1936_naval_legacy.txt`

한국 전체·남부·북부를 완전 열거하는 target block에만 `1082–1084`를 지리적 의미에 맞게 추가했다. 일본 1936 OOB에서 바닐라 일본령 한국에 놓이는 land 위치 `4052 → 7169`, `7125 → 12031`, `4056 → 10011`과 부산 함대 위치 `4056 → 10011`만 옮겼다. 1939 bookmark는 HoK state history가 `1939.3.14`에 한국 states를 JAP에 넘기므로 별도 1939 OOB 위치 patch를 만들지 않았다.

`common/on_actions/04_mtg_on_actions.txt`는 중요한 예외다. 이 파일은 삭제 상속하지 않고 target-derived로 유지한다. `ASIA_DECOLONIZED` 처리에서 target의 `JAP release = KOR`, JAP에서 KOR로의 전 부대 이전, 이어지는 KOR에서 JAP로의 전 부대 이전에 해당하는 12줄만 제거했다. 독립 HoK 한국의 시작 OOB가 이 왕복 처리로 일본에 넘어가는 것을 막기 위한 최소 KOR lifecycle 예외이며, 나머지 MAN·MEN·중국·탈식민화 동작은 target을 따른다.

`history/countries/JAP - Japan.txt`의 한국 저항·순응도는 독립 KOR가 존재하는 1936 시작에 즉시 적용하지 않았다. HoK state history가 한국 states를 JAP에 넘기는 날짜와 같은 `1939.3.14` block에서 한국 9개 state에 target-equivalent 값을 적용했다.

### 5. 끊어진 구형 참조 정리

- `history/countries/KOR - Korea.txt`의 지도자 모집 ID를 실제 보존 정의와 같은 lowercase `KOR_syngman_rhee`로 맞췄다.
- `music/hok_songs.txt`에서 삭제된 구형 일본 focus `JAP_proclaim_the_republic`만 요구하던 `Minshu_ikki` music block을 제거했다.
- `events/korea.txt`의 구형 `JAP_sign_tripartite_pact` caller는 현행 target ID `JAP_sea_tripartite_pact`로 맞췄다.
- 삭제한 공화정 일본 경로의 localisation snapshot을 제거했다. target sprite ID를 덮던 `idea_jap_hitachi` texture·sprite와 `JAP_tamon_yamaguchi` portrait sprite 중복도 제거해 현행 일본 asset을 상속한다.

## `D-CJ-POST` 실패와 승인된 후속 마이그레이션

### 실패와 root cause

최초 정렬은 간도·안둥·헤이허 state `1085–1087`을 제거하면서 쓰시마 state `1088`을 보존했다. 그 결과 effective state ID는 `1–1084, 1088`이 되어 중간의 세 ID가 비었다. 당시 scanner v11은 정의된 state의 membership과 reference만 검사하고 `1..max_id` 연속성을 검사하지 않아 이 구멍을 놓쳤다.

`D-CJ-POST-205045`에서 엔진은 20:52:07에 `Missing State ID 1085`, `1086`, `1087`을 연속으로 기록했다. 20:58:20 싱글플레이 시작 직후 map load popup이 나타났고 20:58:22 새 crash directory와 함께 프로세스가 종료됐다. `crash/exception.txt`는 `C0000005 EXCEPTION_ACCESS_VIOLATION` at `0x00007FF62E2D3BD6`, `crash/meta.yml`은 `IsMapInGoodState: no`를 기록한다.

- state ID `1085–1087` 구멍: `CONFIRMED`
- 이 구멍이 해당 `D-CJ-POST` map load 실패의 root cause: `CONFIRMED`
- 후속 마이그레이션이 해당 exact `D-CJ-POST` engine crash를 제거했는지: `CONFIRMED` — bounded fix 뒤 동일 HoK-only 구성에서 map 진입·1/7/30일 진행·정상 종료를 통과했다.

### 승인과 production 변경

사용자는 쓰시마 state `1088 → 1085` 마이그레이션을 명시적으로 승인했다. 이는 비게 된 첫 ID를 쓰시마에 재사용해 effective state ID를 `1–1085`로 연속화하는 최소 수정이며, 제거한 간도 state나 그 gameplay를 되살리지 않는다.

production 변경은 다음 state-context 위치로 제한했다.

- `history/states/1088 - Tsushima.txt`를 `history/states/1085 - Tsushima.txt`로 옮기고 내부 `id=1085`로 변경
- `common/decisions/KOR_decision.txt`의 쓰시마 controls/highlight/effect state 참조 3곳을 `1085`로 변경
- `map/buildings.txt`에서 쓰시마 site를 식별하는 첫 필드 `1088` 11행만 `1085`로 변경
- state 정의의 `name="STATE_1088"`과 `localisation/english/replace/HoK_state_name_l_english.yml`의 `STATE_1088:0 "쓰시마"`는 안정적인 localisation key로 유지

`definition.csv`, `unitstacks.txt`, `buildings.txt`의 좌표·province 필드처럼 state ID가 아닌 같은 숫자는 일괄 치환하지 않았다. 이 변경은 persistent state ID migration이므로 새 게임 전용이며, 기존 `1088` 쓰시마 세이브나 state ID를 직접 참조하는 서브모드 호환성은 주장하지 않는다.

## 동작 영향

보존되는 핵심은 HoK 한국의 국가 콘텐츠, province `13414–13447`, 한국 states `525`, `527`, `1028–1031`, `1082–1084`, 후속 ID `1085`의 쓰시마, 한국 보급망과 한국 전용 registry다. 쓰시마 localisation key `STATE_1088`은 유지한다. 중국·만주와 일본은 target 1.19.2 동작을 우선한다.

의도적으로 사라지는 기능은 HoK 중국 군벌 자동 통합(`jungppong`), 간도·안둥·헤이허 별도 state와 관련 claim/transfer, 구형 일본 민주 경로, 일본 AI buff, 그리고 후속 승인으로 복구한 경고·최후통첩 decision 두 개를 제외한 HoK 일본 decision·event·MIO·평화회의 AI다. 이를 한국 콘텐츠의 회귀로 숨기지 않고 승인된 중국·일본 기능 손실과 후속 최소 복구로 기록한다.

## 정적 검증 현황

- 최초 정렬 당시 도구 단위 테스트: `21/21 PASS`
- scanner v12 state gap 회귀 검사 추가 후 현재 도구 단위 테스트: `22/22 PASS`
- 1차 post scan: `<PROJECT>/.local-artifacts/analysis/china-japan-vanilla-alignment-2026-09-01/post-static-v1/`
- 1차 vanilla-only control: `<PROJECT>/.local-artifacts/analysis/china-japan-vanilla-alignment-2026-09-01/vanilla-control-v1/`
- 두 scan의 `STATE_NONLAND_PROVINCE` ERROR: 각각 118
- 정렬한 ERROR key 차이: 0, 즉 이 scan 기준 mod-introduced map ERROR 0
- `post-static-v1/summary.json` SHA-256: `33CAEBA86DCC5C57A60B7CDD0BD54911FB935F70A44D8A4FE3FF3C7474433D23`
- `post-static-v1/findings.tsv` SHA-256: `AA1A4978A75443E4A38ABB64CC2D2040F08BE56F8E1AEE78F4C986199217DEC5`
- 최초 정렬 final post scan: `<PROJECT>/.local-artifacts/analysis/china-japan-vanilla-alignment-2026-09-01/post-static-v3/`
- 당시 final scan tool version: `11`
- 당시 final findings: 199 (`ERROR` 118, `WARNING` 21)
- 당시 final inputs: 8,515, references: 5,325
- 당시 final scan과 `vanilla-control-v1`의 전체 sorted ERROR key 차이: 0, 즉 v11 scan 기준 mod-introduced map ERROR 0
- `post-static-v3/summary.json` SHA-256: `93889ECF966BC76E69A7ECF8991B498B7A098D45FAE7CA77488E8690A2C3D17A`
- `post-static-v3/findings.tsv` SHA-256: `E367A509EDED4A1ADC7F6EE231E27EC5DB3A20CE61FC873A8BC02F67ACE05E4F`
- `post-static-v3/inputs.tsv` SHA-256: `38FE9BBF2C4D70BC7D1CB6E00F6B1B1F3E9BBE5C787644F3ADB952BE2AA52587`
- `post-static-v3/references.tsv` SHA-256: `8D36D92F1ED8CC2B485B25485371683B46E73557878E431695DE6586D8002A3F`
- `post-static-v3/three_way_files.tsv` SHA-256: `0C75E927E80B1E3505B2F392E325F993F9FB5E99687C966BA890FE89C8C13E28`
- residual source 감사: 활성 중국·일본 1.19.2 충돌, 삭제한 구형 ID의 활성 caller, 주요 중국·일본 localisation 충돌, exact-path binary 충돌과 case-insensitive sprite ID 충돌 0
- residual source 감사: 중국·만주 geometry 차이 0, 주요 중국 state의 `buildings.txt` target 일치, 남은 target-derived Japan/China 차이는 승인된 한국 state·OOB bridge로 분류
- 변경 기존 script 40개(`.txt`, `.mod`, `.gfx`, `.gui`, `.asset`) brace·quote 실패: 0
- 변경 localisation 3개 UTF-8 BOM·header·duplicate key·홀수 quote 실패: 0
- effective character, country tag, focus, event, JAP·KOR decision duplicate: 0
- 최초 정렬 당시 간도·안둥·헤이허 의미의 states `1085–1087` state-context 참조: 0. 같은 숫자의 province ID는 `definition.csv`상 유효하므로 보존
- effective state/strategic-region province membership 중복·누락: 0. 이는 v11이 검사하지 않은 state 번호 연속성을 뜻하지 않는다.
- buildings unknown state: 0. target 대비 차이가 있는 state는 승인된 한국 allowlist 11개뿐
- supply/rail bad reference와 duplicate: 0
- unresolved JAP focus, JAP/KOR character, 삭제한 HoK 일본 unique ID의 live reference: 각각 0
- 변경 production text 43개의 line ending: CRLF 11, LF 32, mixed 0

`post-static-v3`는 production text의 mixed line ending 정리를 반영한 최초 정렬의 final static snapshot이며 이전 `post-static-v2`를 supersede한다. 다만 v11에는 state ID 연속성 검사가 없어 `1085–1087` 구멍을 검출하지 못했다.

검사 대상은 `git diff --name-only --diff-filter=ACMRTUXB`와 `git ls-files --others --exclude-standard`로 수집했다. PowerShell read-only one-off lexer는 `#` comment와 escaped quote를 제외하고 brace depth·unterminated quote를 검사했고, localisation은 `[IO.File]::ReadAllBytes`와 regex로 BOM·header·key·quote를 검사했다. Python `-B -` in-memory scanner는 target + mod same-filename overlay를 구성해 ID·reference를 검사하고 state·region·buildings·rail·supply를 파싱했다. `rg`로 states `1085–1087`의 state-context 패턴과 raw numeric scope도 별도 확인했다. 이 one-off 감사는 output artifact를 만들지 않았으며 HOI4를 실행하지 않았다.

scanner의 raw `static_result`는 바닐라 control에도 같은 118건을 보고하므로 그대로 PASS로 바꾸지 않는다. 최초 판정은 control과의 동일 key 비교를 함께 기록하며, v3 기준 mod-introduced map ERROR는 0이었다.

### 후속 쓰시마 마이그레이션 정적 감사

- final post-migration scan: `<PROJECT>/.local-artifacts/audits/2026-09-01-map-post-migration-v6-tsushima-1085-final/`
- vanilla control: `<PROJECT>/.local-artifacts/audits/2026-09-01-vanilla-control-v12/`
- scan tool version: `12`
- v6 findings: 195 (`ERROR` 118, `WARNING` 17, `INFO` 60)
- v6 inputs: 8,506, references: 5,327
- targeted findings `MISSING_STATE_ID`, `BUILDINGS_TRAILING_NEWLINE`, `BUILDING_UNKNOWN_STATE`, `MISSING_AIR_BASE_SITE`, `MISSING_ROCKET_SITE`: 각각 0
- v6의 유일한 ERROR code: `STATE_NONLAND_PROVINCE` 118
- vanilla v12 control의 유일한 ERROR code: `STATE_NONLAND_PROVINCE` 118
- 전체 ERROR code/count 차이: 0
- effective state ID: `1–1085` 연속
- `history/states/1085 - Tsushima.txt`: SHA-256 `CE45376BB74D5AE944BCEBD7F964DE87AF9D025618FD863D385B2ED73836752F`, 296 bytes
- `map/buildings.txt`: SHA-256 `DA7A22BC7F3996FC89496BEE248B530FA7039917564AD50B09F6B05A7F574A53`, 3,272,931 bytes
- v6 `summary.json`: SHA-256 `119D97F853C7FF9A588B804A596785CE984D4E3AF29759FE1A4CFB5AFAB716B3`
- v6 `findings.tsv`: SHA-256 `726B7B883203686502D155BA2337BA48430E0242087C1CC9E1496AC3C9C3CB5F`
- v6 `inputs.tsv`: SHA-256 `CC79AE36873D83149D76943567D44DC483854E90D32F3B84B56D5F2CA3460C2F`

v12은 effective state definition의 최대 ID까지 빈 번호를 `MISSING_STATE_ID` ERROR로 보고하며 `1,2,3,7` fixture에서 `4,5,6`만 검출하는 회귀 검사를 포함한다. 현재 단위 테스트 `22/22`는 통과했다. 최종 v6의 표적 오류는 모두 0이고 vanilla control과 ERROR code/count도 같지만, `STATE_NONLAND_PROVINCE` 118건과 명시된 parser·geometry 한계 때문에 raw `static_result`는 양쪽 모두 `FAIL`이다. 이 결과를 전체 static PASS나 runtime 호환성 증명으로 과장하지 않는다. v6는 post-runtime에 KOR decision의 기존 CRLF 형식을 복원한 최종 source bytes를 다시 해시해 v5를 supersede한다.

## 런타임 검증과 완료 조건

최초 `D-CJ-POST`는 실행했으며 state ID gap으로 `FAIL`했다. 승인된 쓰시마 마이그레이션 뒤 `D-CJ-POST-FIX`는 다음 exact HoK-only map/crash gate를 통과했다.

- 실행 시작: 2026-09-01 21:13:20 +09:00, runtime checksum `f39a`
- 싱글플레이 시작: 21:20:15
- map 진입: 21:20:23 `End RestoreDeviceObjects`
- 진행: `game.log` 기준 최소 1936.08.17.13, `error.log`·`system_debug.log` 기준 1936.08.27.07
- gate: 1일·7일·30일 `PASS`
- targeted log: `Missing State ID` 0, `MAP_ERROR` 0
- 종료: `CloseMainWindow(true)`, 30초 안에 종료
- crash/WER: 새 Paradox crash directory와 WER 0, 최신 crash는 실패 실행 `hoi4_20260901_205822`
- evidence: `<PROJECT>/.local-artifacts/incidents/2026-09-01-china-japan-alignment/D-CJ-POST-FIX-211320-EXIT-PASS-1936-08-17/`
- `SHA256SUMS.tsv` SHA-256: `A49E317F1705986C5D779508FA2666FDE58FA7FA824D53E837B61456B9F19496`
- manifest 검증: 15 files, 4,211,832 bytes, mismatch 0

따라서 post-fix `D-CJ-POST-FIX`는 `PASS`이며 state ID gap과 최초 exact crash의 인과는 `CONFIRMED`다. map 진입 뒤 추가된 error 6줄은 OneDrive rename 4줄과 Indonesia market access 2줄로, state gap·map crash 재발이 아닌 별도 non-crash 사건이다.

- post-fix `D-CJ-POST-FIX`: `PASS` — 새 게임 map 진입, unpause, 1/7/30일 진행, 정상 종료
- `C-CJ-POST`: `NOT RUN` — HoK + 정확한 `Korean Language`
- 중국·산둥 map/UI color의 vanilla control 일치: `UNPROVEN`
- 일본의 현행 historical focus 경로와 실제 중일전쟁 발생: `UNPROVEN`
- 1936·1939 bookmark의 일본 OOB와 독립 한국 상태: `UNPROVEN`
- 새 게임 1일·7일·30일 진행: `PASS`; 한국 콘텐츠 점검과 save/reload: `NOT RUN`
- post-fix 새 `error.log`, crash와 WER 비교: exact map/crash gate `PASS`; non-crash error 6줄은 별도 사건

메인 메뉴 진입만으로 정렬 또는 크래시 해결을 완료 판정하지 않는다. `D-CJ-POST-FIX`는 새 게임·맵 진입·unpause·1/7/30일 진행과 로그 확인을 통과했지만, 실제 지원 구성 `C-CJ-POST`는 별도로 실행해야 한다.

## 남은 위험

1. 일본 historical AI가 실제로 `JAP_reinforce_the_beijing_garrison` 경로를 진행하고 CHI와 전쟁하는지는 런타임으로 확인하지 않았다.
2. 중국·산둥 색상은 source가 target과 정렬됐지만 실제 map/UI 렌더링은 확인하지 않았다.
3. `ASIA_DECOLONIZED`의 `04_mtg_on_actions` KOR 예외와 DLC별 분기는 런타임에서 확인하지 않았다.
4. 바닐라 일본 focus는 저장소에 복사하지 않았다. `JAP_prepare_for_peninsular_warfare`의 target province `1003` state-scope가 HoK의 한국 state 분할에서 어떤 동작을 하는지는 별도 gameplay 확인 대상이다.
5. 쓰시마 persistent state ID가 `1088 → 1085`로 바뀌었으므로 기존 세이브와 해당 ID를 직접 참조하는 서브모드 호환성은 주장하지 않는다. save/reload, 1939 bookmark, 비역사 AI, DLC on/off, multiplayer checksum과 모든 한국 대체역사 경로는 미검증이다.
6. `Korean Language`는 descriptor상 `1.17.*` 지원이며 1.19.2 UI·font·localisation 호환성은 `C-CJ-POST` 전까지 미확인이다.
7. 이번 정렬 뒤 드러나는 MIO, technology, event, character와 localisation 오류는 새 로그를 근거로 별도 사건에서 처리해야 한다.
8. 호출자가 없는 일본 trait·뉴스 event·업적, 휴면 TWN tag, 고아 localisation과 고유 구형 일본 GFX가 낮은 우선순위 잔재로 남아 있다. 정적 감사에서는 바닐라 ID 충돌이나 활성 실행 경로가 없어 이번 정상화의 필수 삭제 대상으로 분류하지 않았다.
9. `KOR_Syngman_Rhee`를 target exact ID `KOR_syngman_rhee`로 통일했다. 새 게임 정적 참조는 유효하지만 이전 character ID를 저장한 기존 세이브의 호환성은 runtime에서 확인하지 않았고 주장하지 않는다.

## Git 상태

이 구현과 문서는 working tree에 있으며 commit·push하지 않았다. 구현 시작 기준선은 `main`의 `8a6d075fb64e9bcdc88bfdf8122ab261be7e43ec`이고, base-game 설치본과 외부 사용자 데이터는 수정하지 않았다.
