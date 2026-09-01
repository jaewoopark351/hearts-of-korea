# 중국·일본 1.19.2 바닐라 정렬 정책

## 문서 상태

- 작업 모드: **Implementation 적용 / 후속 static validation 완료 / `D-CJ-POST-FIX` runtime PASS**
- 목표 게임: HOI4 `Operation Postern v1.19.2.0.a729 (d245)`
- 기준 데이터: 설치된 목표 버전 Vanilla (`V_TARGET`)
- 정책 우선순위: **HoK 한국 보존 > 중국·만주·일본의 HoK 변경 보존**
- 구현 상태: **APPLIED — 중국·만주 target 복원, 일본 stale override 제거, KOR bridge와 쓰시마 `1088 → 1085` 후속 마이그레이션 적용**
- 런타임 검증: **PARTIAL — `D-CJ-POST-FIX` map 진입·1/7/30일 진행·정상 종료 PASS, `C-CJ-POST`와 gameplay 장기 검증은 미실행**
- Git 기준선: branch `main`, HEAD `8a6d075fb64e9bcdc88bfdf8122ab261be7e43ec`
- working tree: 구현 시작 시 clean, 현재 승인된 production 구현과 문서 변경으로 dirty
- production mod root: `C:\hoi\hearts_of_korea`
- target root: `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`
- live log root: `C:\Users\jaewo\OneDrive\문서\Paradox Interactive\Hearts of Iron IV\logs`

이 문서는 Hearts of Korea의 한국 콘텐츠와 한국 지도는 최대한 보존하면서 중국·만주·일본 데이터는 HOI4 1.19.2 바닐라와 다시 정렬하기 위한 구현 계약과 현재 적용 상태를 함께 기록한다. 사용자는 이 정렬 과정에서 HoK의 중국·일본 전용 기능이 일부 사라지는 것을 허용했다. 구현 세부사항과 실제 검증 상태는 [중국·만주·일본 1.19.2 바닐라 정렬 구현 기록](incidents/2026-09-01-china-japan-vanilla-alignment-implementation.md)에 고정한다.

관련 문서:

- [1.19.2 맵 재구성 설계](HOK_MAP_RECONSTRUCTION_PLAN.md)
- [맵 호환성 점검표](MAP_COMPATIBILITY_CHECKLIST.md)
- [수정 후 검증 점검표](VALIDATION_CHECKLIST.md)
- [target-native 맵 구현 기록](incidents/2026-09-01-target-native-map-implementation.md)
- [중국·만주·일본 1.19.2 바닐라 정렬 구현 기록](incidents/2026-09-01-china-japan-vanilla-alignment-implementation.md)
- [fresh 맵 격리 사건](incidents/2026-09-01-fresh-map-isolation.md)

## 1. 결정

적용한 구현의 기본식은 다음과 같다.

```text
V_TARGET 1.19.2 중국·만주·일본 데이터
+ 보존이 승인된 HoK 한국 콘텐츠
+ 독립 한국과 HoK 한국 지도에 꼭 필요한 최소 접점 delta
= 중국·일본 바닐라 정렬 후보
```

구현 원칙은 다음과 같다.

1. 중국·만주·일본의 국가 색상, state, focus, decision, event, AI, character, MIO, country history와 OOB는 목표 버전 바닐라를 기본값으로 한다.
2. 같은 상대경로의 구형 전체 파일은 가능하면 모드에서 제거해 목표 버전 파일을 상속한다. 바닐라 파일을 저장소에 통째로 복사해 새 고정 snapshot으로 만들지 않는다.
3. 한국 전용 정의가 필요한 전역 데이터베이스는 목표 바닐라를 base로 하고 HoK 고유 항목만 최소 delta로 유지한다. loader상 안전하게 분리할 수 없는 exact-path 전역 파일은 target-derived snapshot임을 명시하고 버전별로 다시 대조한다.
4. `KOR` focus·event·decision·idea·character·history·OOB·asset·localisation과 한국 province/state topology는 보존 대상이다.
5. 구형 중국·일본 시스템을 유지하기 위해 현행 바닐라 정의를 다시 덮어쓰지 않는다. 한국 caller가 꼭 필요로 하는 일본·중국 접점만 현재 바닐라 의미를 확인한 target-derived 호환 계층으로 이식한다.
6. 숫자 전역 치환, 중국 province 재채색, 바닐라 설치본 수정, `replace_path` 추가는 금지한다.
7. 시작 크래시 복구 사건과 중국·일본 gameplay 정렬은 별도 사건이다. 현재 증거는 구형 중국·일본 코드가 1.19.2와 불일치함을 입증하지만, 그것이 이미 해결된 시작 크래시의 직접 원인이었다고 입증하지는 않는다.

## 2. 보존 경계

| 영역 | 후속 기준 | 비고 |
|---|---|---|
| 한국 province `13414–13447` | `PRESERVE_KOREA` | 검증된 한국 crop의 geometry를 보존한다. |
| 한국 state `525`, `527`, `1028–1031`, `1082–1084` | `PRESERVE_KOREA` | HoK 한국 9도 분할과 연결 콘텐츠를 보존한다. |
| 쓰시마 state `1085`와 province `10011` 분리 | `TARGET_DERIVED_KOREA_DELTA` | 일본 본토 state `528`은 target 기반으로 두고 쓰시마 분리만 유지한다. 최초 정렬의 `1088`은 후속 런타임 실패 뒤 `1085`로 마이그레이션했지만 안정적인 localisation key `STATE_1088`은 유지한다. |
| 간도·안둥·헤이허 state `1085–1087` | `INHERIT_TARGET` / 적용 | 세 의미 state를 제거하고 source states `328`, `714`, `716`, `717`을 복원했다. 이후 비게 된 ID `1085`는 쓰시마가 재사용하며, 간도 의미를 되살리지 않는다. target parent 전체로 의미가 확대되는 KOR claim·core·transfer는 제거하고, 승인된 시작 건물·부대 효과만 parent state에 매핑했다. |
| 중국·만주 province bitmap/RGB | `INHERIT_TARGET` | 현재 target과 다른 1,889 pixel은 한국 crop 안에만 있다. 중국을 다시 칠하지 않는다. |
| 중국·만주 국가 색상·cosmetic·name pool | `INHERIT_TARGET` + 한국 delta | stale 전역 snapshot을 제거하고 HoK 한국 정의만 분리한다. |
| 중국·만주 국가 history·focus·AI·OOB | `INHERIT_TARGET` / 적용 | `jungppong`과 stale MAN OOB·CHI 함명 override를 제거했고, 한국을 직접 호출하는 승인된 접점만 target-derived로 유지했다. |
| 일본 focus·decision·event·AI·character·MIO·history·OOB | `INHERIT_TARGET` + 최소 KOR bridge / 적용 | unchanged focus·AI·character는 삭제 상속하고, 독립 KOR·한국 9도에 필요한 파일만 target-derived로 유지했다. |
| 한국이 일본·중국을 상대하는 HoK 콘텐츠 | `PRESERVE_KOREA` 또는 최소 bridge / 적용 | 현행 바닐라 ID·scope와 호환되는 caller만 유지하고 끊어진 구형 ID는 정리했다. |
| KJP·KCH·RKY·TWN HoK 고유 태그·cosmetic | `PRESERVE_KOREA` / 적용 | target-derived registry에 필요한 HoK 정의만 유지했다. target이 이미 정의하는 `ANU`의 HoK override는 제거했다. |

간도·안둥·헤이허 `1085–1087` 제거는 persistent state ID를 없애고 KOR 영유권 콘텐츠도 바꾸는 승인된 마이그레이션이다. 최초 정렬은 쓰시마를 `1088`에 남겨 effective state ID가 `1–1084, 1088`로 끊겼고, 첫 `D-CJ-POST`에서 이 구멍이 map load 실패의 원인으로 확인됐다. 사용자가 승인한 후속 수정은 쓰시마만 `1088 → 1085`로 옮겨 `1–1085`를 연속화한다. 기존 세이브와 해당 ID를 참조하는 서브모드는 호환 대상으로 주장하지 않는다. 구현에서는 state-context 참조를 문맥별로 처리하고, 같은 숫자의 province ID·좌표는 일괄 치환하지 않았다. 세부 disposition과 실제 파일 변경은 구현 기록에 남긴다.

## 3. 증거와 판정

구현 전 분석한 live 로그는 HoK 단독 장기 실행에서 생성됐고 `Korean Language`는 활성화되지 않았다. 로그는 `<PROJECT>/.local-artifacts/incidents/2026-09-01-china-japan-alignment/CJ-PRE-LOGS-193412/`에 보존했으며 `SHA256SUMS.tsv` SHA-256은 `1E48A31BC0604CA901CED00E527CE07394072317EBD56B167B1C61E6AAF8CEF5`다. 다만 정확한 historical AI checkbox와 모든 game rule이 실행 메타데이터에 완전히 묶여 있지 않으므로, 일본의 관찰 동작은 이 실행에서 발생한 사실과 그 원인 가설을 구분한다.

### 3.1 중국·산둥 색상

| 관찰 | 판정 |
|---|---|
| 모드 `common/countries/colors.txt` SHA-256 `89486BFB25DDA2C8D0CC3C4A6B4ED6B1BEE6BFDC740E39C652EAAA35660384A9`가 target 파일 SHA-256 `346E1AC0D82B929FCA9E4917A60A689685948A83A9066CCC4E2EA257AFA275A9`와 다르다. | `CONFIRMED` |
| 모드 파일은 275개 block, target은 304개 block이며 target-only 중국계 tag `GDC`, `GSM`, `HBC`, `KHM`, `KUM`, `NXM`, `RNG`, `SIC`, `SND`, `XIC` 등이 빠져 있다. | `CONFIRMED` |
| target의 `SND` 색상은 `rgb { 230 92 0 }`, UI 색상은 `rgb { 153 61 0 }`이나 모드 exact-path 파일에는 `SND` block이 없다. | `CONFIRMED` |
| 모드 `CHI` 색상은 target `rgb { 40 40 140 }`와 다르다. | `CONFIRMED` |
| `SND` tag와 state `597`, `743`, `1038`은 모드가 별도로 덮지 않아 target을 상속한다. | `CONFIRMED` |
| stale `colors.txt`가 사용자가 본 산둥 색상 이상 현상의 주원인이다. | `STRONGLY_SUPPORTED` — 정렬 후 동일 화면 재확인이 필요하다. |

`common/countries/cosmetic.txt`도 모드 SHA-256 `9CE9F5DDC930C7FEF84F834AA6D4D8A588AF63B9C40BED36775939C108B64309`, target SHA-256 `D3666EE4F63FAE0E8B5ABFAA93416A7F9F8D10A19F3C379E52F83A1EF89134AA`로 서로 다르다. 모드 331개 block과 target 385개 block 사이에 `PRC_proclaimed`, `MAN_republic_of_china`, `XIC_new_fengtian_clique` 등 현행 중국·만주 cosmetic이 누락돼 있다. `common/names/00_names.txt`도 구형 전역 snapshot이라 `SND`를 비롯한 현행 중국 tag의 name pool이 없다.

### 3.2 중국·만주 지도

- `provinces.bmp`의 target 대비 변경 1,889 pixel은 모두 한국 crop 안에 있다. 중국·만주 province RGB를 새로 지정할 근거는 없다. `CONFIRMED`
- state `1085`는 target `717`·`328`, state `1086`은 `328`·`716`, state `1087`은 `714`에서 province를 분리해 만든 HoK state다. `CONFIRMED`
- 이 분할 때문에 strategic region `155`·`243`, Great Wall on-action, buildings, railway와 supply node에도 연쇄 delta가 있다. `CONFIRMED`
- 이 중국·만주 topology 차이가 과거 시작 크래시의 원인이었다는 주장은 당시 재현에서 입증되지 않았다. `UNPROVEN` — 후속 정렬에서 `1085–1087`을 제거하고 `1088`만 남겨 만든 별도의 ID 구멍과 그 `D-CJ-POST` 실패는 아래 3.5절의 새 사건이다.

### 3.3 일본 중점과 중일전쟁

| 관찰 | 판정 |
|---|---|
| 모드 `common/national_focus/japan.txt`는 target과 같은 tree ID `japan_wtt_focus`를 가진 구형 exact-path 파일이다. 모드는 JAP focus 128개, target은 449개다. | `CONFIRMED` |
| 현행 `JAP_historical_strategy_plan.txt`가 요구하는 `JAP_reinforce_the_beijing_garrison` 등 다수 focus가 유효한 일본 트리에 등록되지 않는다. | `CONFIRMED` |
| 모드 `common/ai_strategy/JAP.txt`는 구형 `JAP_intervene_in_china`를 사용하지만 target은 `JAP_reinforce_the_beijing_garrison` 중심의 현행 중국 구조를 사용한다. | `CONFIRMED` |
| live `game.log`에서 일본은 1939.06.26 한국에 선전포고하고 1941년 남방전쟁을 시작했지만, 1942년까지 일본의 CHI·중국 군벌 상대 선전포고는 기록되지 않았다. | `CONFIRMED` — 이 실행의 동작에 한정한다. |
| 구형 focus/AI와 현행 strategy plan·event·decision·MIO의 불일치가 중일전쟁 미발생의 주원인이다. | `STRONGLY_SUPPORTED` — 정렬 후 동일 조건 비교가 필요하다. |
| `JAP_HoK.txt`의 malformed token 하나나 개별 MIO·character 오류 하나가 단독 원인이다. | `UNPROVEN` |

현재 `error.log`에는 다음과 같은 서로 연결된 version-skew 증거가 있다.

- `common/ai_strategy/JAP_HoK.txt`: malformed `naval_invasion_supremacy_weight`
- `JAP_historical_strategy_plan`: 현행 focus ID 대량 invalid, `JAP_reinforce_the_beijing_garrison` 포함
- `JAP_MIL_02`: division name group 누락
- `JAP_okadas_military_purge_speech`, `JAP_subdue_the_kwantung_army`: 현행 event·decision·중국 focus caller에서 invalid
- `JAP_duplicate_research_efforts`: 구형 country history와 focus에서 invalid
- `JAP_tokyo_arsenal_organization`: 구형 OOB의 존재하지 않는 MIO 참조

원본 live 로그는 실행 ID와 SHA-256 manifest로 별도 보존했다. 보존 bundle은 원본 바이트를 고정하지만 누락된 실행 조건까지 소급해 입증하지는 않는다.

### 3.4 핵심 exact-path 관찰 hash

다음 값은 2026-09-01 구현 전 working tree와 설치된 target 1.19.2를 식별하는 역사적 pre-implementation hash다. 현재 working tree의 파일 상태를 뜻하지 않으며 원본 HoK 불변 archive의 manifest를 대신하지 않는다.

| 상대경로 | 현재 mod SHA-256 | target SHA-256 |
|---|---|---|
| `common/national_focus/japan.txt` | `3B42BE18182684942A072B279FA4589738E1D4D4503D9A05AB4AFD5CBE41B338` | `BF5EF4B6A17E70E4AD83030A0AAC4DE72105CB8803CA6F93A9BF3FCEF8662623` |
| `common/ai_strategy/JAP.txt` | `C90EBD92BE8EE4A5B169EC741688127E95BEB759D7219FAD1D80B2A109C055D0` | `3E372BF6EBE307EA7630F34FDA15A566A708D1EA287834FD996026486E6C65B3` |
| `common/ai_strategy_plans/JAP_alternate_strategy_plan.txt` | `52568EA124584C85D6324D0FF0A44A02560840E8BFBCC307EC839070159C9BD0` | `80D7C091CC09390094334226E1C43B8A56D32F2B3CE3AF3DFB3283010C40F1D8` |
| `common/decisions/JAP.txt` | `0ED2FF92806B2CFA1787B69EADBC4AA29784AF904DFA882DAD5340F006A7B95B` | `2F936D32A11A4A6D196DB972E566EB3D0E921D34FB52DA0C14C56B8E5783DC80` |
| `common/characters/JAP.txt` | `2ECCC9B7C3AE4AF2510A741F2F6C51F047B380D5A991D62C91DFBFD61248D6DF` | `957DF38BD0F7D985B5770346A8F1D0C56C9F026AB54BE7A7187D4D44CD9E6BA4` |
| `history/countries/JAP - Japan.txt` | `C31AB66580B1F910E564F0240A81ACAB6804D7C2C2CB7C33C9D30009D6953F70` | `5724E83B4C83B807FE43B966683155332B23E2967E225D85DD3A3D4BBA527633` |
| `history/units/JAP_1936_nsb.txt` | `DBA096AE13B183685837EA2F7FE557BFBE38A0B41E5A818F89205DF627129749` | `73178BF3E2A4DFFE8622BE3F07AC153155688BFBC3F34603EA352DD5130C8127` |
| `history/units/MAN_1936.txt` | `C7E527F6E26482722BDDD3E8C889370DEAB3BC36BE33D046BE00565861632BE3` | `FDBA63FF7A48DA65E74C508F0B319EA7DACAB8DF32BE10CEC016BDA84053B2C6` |

### 3.5 최초 `D-CJ-POST` 실패와 state ID 구멍

최초 post-implementation HoK 단독 실행 `D-CJ-POST-205045`는 2026-09-01 20:51:55에 시작했고, 20:58:20에 1936 싱글플레이를 시작한 뒤 20:58:22 map load에서 종료됐다. 예외는 `C0000005 EXCEPTION_ACCESS_VIOLATION` at `0x00007FF62E2D3BD6`이며 crash metadata는 `IsMapInGoodState: no`를 기록했다.

같은 실행의 `error.log`는 load 단계에서 `Missing State ID 1085`, `1086`, `1087`을 연속으로 보고했다. production effective state 집합이 `1–1084, 1088`인 사실과 함께 대조해, 최초 정렬에서 만든 state ID 구멍을 이번 map load 실패의 root cause로 `CONFIRMED`한다. 이는 과거 target-native 맵 복구 성공을 소급해 부정하는 결과가 아니라, 그 뒤 중국·만주 state를 제거하면서 새로 생긴 후속 회귀다.

실패 증거는 다음 불변 bundle에 보존했다.

- bundle: `<PROJECT>/.local-artifacts/incidents/2026-09-01-china-japan-alignment/D-CJ-POST-205045-FAIL-205822/`
- 실행 메타데이터와 원본 경로: `capture.json`
- 최초 state 누락과 후속 로그: `runtime-logs/error.log`, `runtime-logs/game.log`
- 예외와 map 상태: `crash/exception.txt`, `crash/meta.yml`
- bundle manifest: `SHA256SUMS.tsv`, SHA-256 `8E309FB61910BC782D229C514ACF68A16253D06729C15FFBF3AA79E0F11D96E6`

사용자는 이 증거를 확인한 뒤 쓰시마 state `1088 → 1085` 마이그레이션을 승인했다. 후속 정적 검증 뒤 같은 HoK 단독 구성의 `D-CJ-POST-FIX`는 map 진입, 1일·7일·30일 gate와 정상 종료를 통과했다. 최초 실패와 이 bounded fix 외 조건이 같은 재실행을 함께 대조해 state ID 구멍과 해당 exact `D-CJ-POST` crash의 인과를 `CONFIRMED`로 유지한다.

성공 실행은 2026-09-01 21:13:20에 시작했고 runtime checksum은 `f39a`였다. 21:20:15 싱글플레이 시작, 21:20:23 `End RestoreDeviceObjects`로 map 진입을 완료한 뒤 unpause해 `game.log` 기준 최소 1936.08.17.13, `error.log`·`system_debug.log` 기준 1936.08.27.07까지 진행했다. `Missing State ID`와 `MAP_ERROR`는 각각 0이고, `CloseMainWindow(true)` 뒤 30초 안에 종료했다. 새 Paradox crash directory와 WER은 없으며 최신 crash는 실패 실행의 `hoi4_20260901_205822`다.

- success bundle: `<PROJECT>/.local-artifacts/incidents/2026-09-01-china-japan-alignment/D-CJ-POST-FIX-211320-EXIT-PASS-1936-08-17/`
- 핵심 메타데이터와 원본 경로: `capture.json`
- bundle manifest: `SHA256SUMS.tsv`, SHA-256 `A49E317F1705986C5D779508FA2666FDE58FA7FA824D53E837B61456B9F19496`
- manifest 검증: 15 files, 4,211,832 bytes, mismatch 0

map 진입 뒤 새 error 6줄은 OneDrive rename 4줄과 Indonesia market access 2줄이며, state gap이나 crash 재발은 아니다. 이들은 별도 non-crash 사건으로 분리한다.

## 4. 파일 분류 규칙

각 영향 파일은 구현 전에 다음 중 하나로 등록했다.

| 분류 | 의미 |
|---|---|
| `INHERIT_TARGET` | 모드의 stale override를 제거하고 설치된 1.19.2 파일을 그대로 상속한다. |
| `TARGET_DERIVED_KOREA_DELTA` | target 파일을 기준으로 한국에 필요한 최소 차이만 유지한다. |
| `PRESERVE_KOREA` | HoK 한국 전용 정의를 그대로 보존하되 target ID·scope 호환성을 검사한다. |
| `REMOVE_STALE_OVERRIDE` | 구형 전체 snapshot이나 HoK 중국·일본 전용 additive 동작을 제거한다. |
| `DEFERRED_REVIEW` | 한국 경로의 실제 caller나 의미가 불명확해 자동 제거·이식하지 않는다. |

등록표에는 상대경로, loader/override 방식, mod·target SHA-256, 주요 ID, 한국 caller, DLC gate, save·서브모드 영향, 증거 등급과 승인 상태를 적는다. target 버전이 바뀌면 모든 target hash와 의미 비교를 다시 수행한다.

## 5. 중국·만주 적용 결과

### 5.1 색상·cosmetic·name pool

| 현재 경로 | 적용 처리 | 한국 보존 처리 |
|---|---|---|
| `common/countries/colors.txt` | target-derived registry 적용 | target `CHI`·`SND`와 현행 tag를 유지하고 KOR 파란색, KJP·KCH·RKY·TWN만 추가했다. |
| `common/countries/cosmetic.txt` | target-derived registry 적용 | `KOR_Goguryeo`, `KOR_PRK_communism`, `KJP_PSJ`만 추가했다. |
| `common/names/00_names.txt` | target schema 기반으로 복귀 | KOR 이름을 보강하고 KJP·KCH·RKY·TWN block만 추가했다. |
| `common/units/names_ships/CHI_ship_names.txt` | target 상속 | 구형 중국 함명 snapshot을 제거했다. |

산둥은 별도의 임의 색을 지정하지 않는다. 목표 결과는 target `SND`의 국가 색과 UI 색을 그대로 사용하는 것이다. 국가 정치색과 province bitmap RGB는 서로 다른 데이터이므로 province를 다시 칠하는 방식으로 해결하지 않는다.

### 5.2 state·전략 지역·보급망

| 항목 | 적용 처리 |
|---|---|
| `history/states/1085 - Jiandao.txt` | 제거하고 target source states를 상속했다. |
| `history/states/1086 - Andung.txt` | 제거하고 target source states를 상속했다. |
| `history/states/1087 - Heihe.txt` | 제거하고 target source states를 상속했다. |
| `328-Manchukuo`, `714-Heilungkiang`, `715-Liaoning`, `716-Liaotung`, `717-Chuho`, `761-Hulunbuir` | 구형 override를 제거해 target membership과 history를 상속했다. |
| strategic regions `155`, `243` | 구형 override를 제거해 target membership을 상속했다. |
| `common/on_actions/14_sea_on_actions.txt` | target을 base로 복귀하고 승인된 `1082–1084` 한국 semantic fan-out만 유지했다. |
| `map/buildings.txt` | target 비한국 행 + 승인된 HoK 한국 state 행을 합성하고 `1085–1087` 행을 제거했다. |
| `map/supply_nodes.txt` | Manchuria mod-only node `11781`을 제거하고 한국 node를 보존했다. |
| `map/railways.txt` | target에 없는 Manchuria branch 8개를 제거하고 한국 route를 보존했다. |
| `map/unitstacks.txt` | 중국 rollback 범위에서 변경하지 않았다. |
| `history/units/MAN_1936.txt` | override를 제거해 target OOB를 상속했다. |

state 복구에서는 source state별 province 집합을 대조해 `1085–1087`과 residual parent membership의 합집합이 target states `328`, `714`, `716`, `717`과 일치함을 확인했다. 구형 HoK 밸런스를 유지하지 않고 target state history를 상속하므로 target의 resource, factory, victory point, category, owner, controller와 core가 기준이다.

`1085`와 `1086`은 여러 target state 조각으로 구성돼 1:1 대체 ID가 없다. 따라서 `common/decisions/KOR_decision.txt`, `common/national_focus/korea.txt`, `events/korea.txt`와 localisation의 간도·안둥·헤이허 claim/core/transfer를 제거했다. 이를 target states `328`, `716`, `717` 전체에 치환해 한국 영토·자원·밸런스를 확대하지 않았다. `gookppong_on_actions`의 시작 건물·부대처럼 보존 승인을 받은 효과만 지리적 parent states `717`, `328`, `716`, `714`에 개별 매핑했다.

위 두 문단은 최초 정렬에서 간도·안둥·헤이허를 제거한 결과를 보존한 기록이다. 후속 쓰시마 `1088 → 1085` 마이그레이션은 그 가운데 비게 된 숫자 `1085`만 재사용하며, 제거한 간도 state나 KOR 영유권 효과를 복원하지 않는다.

## 6. 일본 적용 결과

### 6.1 바닐라를 직접 상속하는 파일

다음 stale exact-path snapshot은 제거했다. 저장소에 target 원본 복사본을 남기지 않았으므로 설치된 1.19.2 파일을 직접 상속한다.

- `common/national_focus/japan.txt`
- `common/ai_strategy/JAP.txt`
- `common/ai_strategy_plans/JAP_alternate_strategy_plan.txt`
- `common/characters/JAP.txt`
- `common/units/names_divisions/JAP_names_divisions.txt`
- 일본 state `282`, `530`, `531`, `536`, `537`

특히 일본 focus는 내용이 동일한 바닐라 파일을 모드에 복사할 필요가 없다는 사용자의 결정을 따른다. 현행 `japan_wtt_focus`와 historical plan은 모드의 구형 128-focus snapshot이 아니라 target의 449-focus tree를 사용해야 한다. state `528`은 target을 기준으로 province `10011`을 state `1085` 쓰시마로 분리한 map delta만 유지한다. 이 숫자는 최초 정렬의 `1088`에서 후속 마이그레이션된 것이며, state 정의의 `name="STATE_1088"`과 localisation key `STATE_1088`은 번역·표시 호환성을 위해 그대로 유지한다.

### 6.2 target-derived KOR bridge

다음 파일은 target을 기준으로 다시 만들고 KOR block, KOR 제외 조건 또는 한국 state semantic fan-out만 적용했다.

- `common/decisions/JAP.txt`, `common/decisions/KOR.txt`
- `common/scripted_triggers/JAP_scripted_triggers.txt`
- `common/national_focus/china_shared_TSR.txt`
- `events/WTT_Japan.txt`, `events/SEA_Japan.txt`
- `common/peace_conference/ai_peace/USA.txt`, `SOV.txt`
- `common/on_actions/14_sea_on_actions.txt`
- `common/bookmarks/the_gathering_storm.txt`
- `history/countries/JAP - Japan.txt`
- `history/units/JAP_1936.txt`, `JAP_1936_nsb.txt`, `JAP_1936_naval.txt`, `JAP_1936_naval_legacy.txt`

다음 전역 공유 파일도 target-derived KOR delta로 처리했다.

- `common/military_industrial_organization/organizations/00_generic_organization.txt`
- `common/on_actions/04_mtg_on_actions.txt`
- `common/scripted_effects/SP_scripted_effects.txt`
- `common/intelligence_agencies/00_intelligence_agencies.txt`
- `common/difficulty_settings/00_difficulty.txt`
- `history/general/generic_advisors.txt`
- `events/ElectionEvents.txt`

각 파일은 target 기준으로 다시 만들고, generic MIO·advisor에서 custom KOR 중복을 막는 조건, KOR difficulty·intelligence agency, KOR special-project asset, 한국 선거 guard와 독립 한국 lifecycle에 필요한 block만 남겼다.

`common/on_actions/04_mtg_on_actions.txt`는 삭제 상속 예외다. target-derived 파일에서 `ASIA_DECOLONIZED`의 `JAP release = KOR`, JAP→KOR 전 부대 이전, KOR→JAP 전 부대 이전에 해당하는 12줄만 제거했다. 이는 독립 HoK KOR의 OOB가 왕복 처리 뒤 JAP에 넘어가는 것을 막는 최소 lifecycle 보호다. 나머지 MAN·MEN·중국·탈식민화 처리는 target을 유지한다.

### 6.3 HoK 일본 전용 additive 제거

다음 비바닐라 일본 시스템은 초기 정렬에서 제거했다.

- `common/ai_strategy/JAP_HoK.txt`
- `common/decisions/JAP_HoK_decision.txt`
- `common/decisions/categories/JAP_HoK_decision_category.txt`
- `events/japan_HoK.txt`
- `common/ideas/democratic_japan.txt`
- `common/military_industrial_organization/organizations/JAP_HoK_organization.txt`
- `common/peace_conference/ai_peace/JAP_HoK.txt`
- `common/on_actions/buff_japan_if_japan_is_ai_on_actions.txt`

여기에는 AI 일본의 시작 부대 buff와 1939년 한국 최후통첩·강제 전쟁이 포함됐다. 초기 제거 후 일본이 1939.06.26 한국에 선전포고하던 HoK 동작은 보존하지 않았으며, 이 기능 손실은 당시 사용자가 허용한 중국·일본 바닐라 정렬의 의도된 결과였다.

후속 승인으로 위 결정을 일부 supersede한다. 구형 일본 focus·AI buff·이벤트·MIO·평화회의 시스템은 제거 상태를 유지하되, target-derived `common/decisions/JAP.txt`에 `jap_warning_to_korea`와 `jap_ultimatum_to_korea`만 1.19.2 문법으로 복구하고 `common/decisions/categories/JAP_HoK_decision_category.txt`에는 해당 category 하나만 복구한다. 이 bridge는 1936 캠페인에서 기존 `kor_events.20`과 `kor_events.16`을 호출하며, 다른 삭제 일본 콘텐츠는 되살리지 않는다.

custom 일본 focus만 참조하는 GFX·flag·localisation은 엔진 동작에 관여하지 않는 것이 확인되면 즉시 삭제할 필요가 없다. 배포 정리는 호환성 구현과 분리한다.

### 6.4 한국 보존을 위한 최소 일본 접점

- KOR가 JAP·CHI·PRC 등의 puppet이 될 때 KOR cosmetic을 적용하는 `common/on_actions/HoK_cosmetic_tag_on_actions.txt`는 일본 AI를 바꾸지 않으므로 보존했다.
- 1.19.2 일본 트리에 독립 한국 분기가 있으므로 독립 한국을 이유로 구형 일본 focus를 유지하지 않았다.
- target 일본 1936 OOB의 평양 `4052`, 서울 `7125`, 부산 `4056` 위치를 각각 `7169`, `12031`, `10011`로 옮기고 부산 함대도 `10011`로 옮겼다. 나머지 OOB는 target을 따른다.
- 1939 bookmark에서는 HoK state history가 `1939.3.14`에 한국 states를 JAP에 넘기고 시작일은 `1939.8.14`이므로 1939 OOB에 별도 위치 patch를 추가하지 않았다. 이 판단은 runtime bookmark 검증 전까지 `UNPROVEN`이다.
- `history/countries/JAP - Japan.txt`의 한국 저항·순응도는 독립 KOR가 존재하는 1936 시작에 즉시 적용하지 않고, state history의 소유권 이전과 같은 `1939.3.14` date block에서 한국 9개 state에 target-equivalent 값으로 적용했다.
- `events/korea.txt`의 구형 `JAP_sign_tripartite_pact` caller를 target의 `JAP_sea_tripartite_pact`로 맞췄다.
- `common/ai_strategy/KOR.txt`가 참조하는 `JAP_strengthen_civilian_government`는 1.19.2에도 존재하므로 유지 가능하다.
- KOR focus·event가 더 이상 존재하지 않는 HoK 일본 ID를 요구하면 일본 코드를 되살리지 않고 KOR caller를 제거하거나 현행 의미로 최소 이식한다.
- 삭제한 구형 focus `JAP_proclaim_the_republic`에만 의존하던 `music/hok_songs.txt`의 `Minshu_ikki` block을 제거했다.
- `history/countries/KOR - Korea.txt`의 모집 ID를 실제 character ID와 같은 lowercase `KOR_syngman_rhee`로 맞췄다.

### 6.5 한국 state semantic fan-out

한국 9도 분할로 추가된 `1082–1084`는 단순 표시용 state가 아니다. target 1.19.2가 한국 전체·남부·북부를 완전 열거하는 다음 파일에 target-derived Korea compatibility를 적용했다.

- `common/scripted_triggers/JAP_scripted_triggers.txt`의 한국 전체·남부·북부 판정
- `common/on_actions/14_sea_on_actions.txt`의 한국 저항·소유권 관련 열거
- `common/decisions/KOR.txt`의 state 대상 결정
- `events/WTT_Japan.txt`의 한국 소유권·해방·이전 효과

추가 적용 파일에는 `common/national_focus/china_shared_TSR.txt`, `events/SEA_Japan.txt`, `common/peace_conference/ai_peace/USA.txt`, `SOV.txt`도 포함한다. 각 block에서 `1082`, `1083`, `1084`가 어느 의미 집합에 들어가는지 지리와 효과별로 결정했다. target 목록에서 state `525`가 의도적으로 빠진 곳은 임의로 추가하지 않았고, 같은 숫자의 province 참조와 섞어 일괄 치환하지 않았다.

## 7. 적용 흐름과 다음 단계

1. `CJ-PRE-LOGS-193412`로 구현 전 live 로그를 보존하고 SHA-256 manifest를 만들었다.
2. exact-path shadow와 additive 중국·일본 파일을 분류했다.
3. 국가 색상·cosmetic·name pool을 target-derived registry + HoK 한국 delta로 복원했다.
4. `1085–1087`을 제거하고 중국·만주 state, region, buildings, rail과 supply를 의미 단위로 target에 맞췄다.
5. 일본 focus·AI·character·name snapshot을 삭제 상속으로 바꾸고 HoK 일본 additive 동작을 제거했다.
6. bookmark, 1936 일본 OOB 위치, 최초 쓰시마 state `1088`, KOR caller와 `1082–1084` semantic fan-out만 target-derived Korea delta로 재적용했다.
7. line-ending 정리까지 반영한 당시 final `post-static-v3`와 vanilla control의 전체 ERROR key를 비교해 mod-introduced map ERROR 0을 확인했고, script/reference 감사를 통과했다. 당시 scanner에는 state ID 연속성 검사가 없어 `1085–1087` 구멍은 검출하지 못했다.
8. 최초 `D-CJ-POST`는 20:58:20 싱글플레이 시작 뒤 20:58:22 map load에서 crash했고, `Missing State ID 1085–1087`과 `IsMapInGoodState: no`를 남겼다.
9. 사용자 승인에 따라 쓰시마 state를 `1088 → 1085`로 마이그레이션하고, production state 정의·KOR decision 3곳·`buildings.txt`의 쓰시마 state 첫 필드 11행을 함께 갱신했다. 안정적인 `STATE_1088` localisation key는 유지했다.
10. scanner v12에 effective state ID 연속성 검사를 추가하고 현재 단위 테스트 `22/22`를 통과했다. 최종 `post-static-v6`에서 새 검사의 표적 오류 5종은 0이며 전체 ERROR 118건은 vanilla v12 control과 동일하다.
11. post-fix `D-CJ-POST-FIX`는 새 게임 map 진입, 1일·7일·30일 진행과 정상 종료를 통과했다. 이후 실제 지원 구성 `C-CJ-POST`를 검증한다.
12. 이후 남는 MIO·event·character·technology·localisation 오류와 이번 실행의 non-crash error 6줄은 각각 별도 사건으로 분리한다.

실제 commit·push는 별도 지시가 있을 때만 수행한다. 현재 구현과 문서는 working tree에만 있고 commit·push하지 않았다.

## 8. 정적 완료 조건

현재 체크는 구현 diff, final map scan과 production script/reference 감사를 통해 직접 확인한 항목만 표시한다. runtime이 필요한 항목은 미체크로 둔다.

- [x] target `colors.txt`, `cosmetic.txt`, `00_names.txt`를 base로 하고 HoK 전용 delta가 target-only tag를 가리지 않는다.
- [x] `SND` country color와 `color_ui`가 target 값과 일치한다.
- [x] 간도·안둥·헤이허 의미의 `1085–1087` state-context 참조를 제거했다. 후속 쓰시마 state만 `1085`를 사용하며, 같은 숫자의 province ID·좌표는 전역 치환하지 않았다.
- [x] states `328`, `714`, `716`, `717`의 override를 제거해 target membership과 history를 상속한다.
- [x] regions `155`, `243` override를 제거해 target membership을 상속한다.
- [x] `buildings.txt`의 비한국 rows를 target에 맞추고 한국 site·port 보정을 유지했다.
- [x] Manchuria rail·supply delta 제거 결과가 allowlist와 일치한다.
- [x] 현행 `JAP_historical_strategy_plan`이 target에서 상속되는 현행 일본 focus tree를 참조한다.
- [x] residual source 감사에서 삭제한 구형 focus, decision category, character, division name group, idea와 MIO의 활성 caller가 0이다.
- [x] 구형 `JAP_HoK` 전체 시스템과 buff caller는 제거 상태를 유지하고, 승인된 1939년 경고·최후통첩 decision 두 개만 target-derived 일본 decision에 복구했다.
- [x] KOR ID·namespace·localisation과 한국 map registry의 정적 참조·중복 검사가 통과했다.
- [x] `1082–1084`가 한국 전체·남부·북부 판정, 저항, decision와 WTT Japan 효과에 문맥별로 반영됐다.
- [x] 쓰시마 production 참조를 state `1085`로 옮기고 state ID `1–1085` 연속성을 확인했다. 표시용 `STATE_1088` localisation key는 유지했다.
- [x] scanner v12의 state ID gap 회귀 검사와 현재 도구 단위 테스트 `22/22`가 통과했다.
- [ ] 1936과 지원하는 경우 1939 일본 OOB의 한국 위치가 승인된 일본·쓰시마 위치로만 이동했다.
- [x] 변경 script 40개의 brace·quote와 localisation 3개의 BOM·header·duplicate key·quote 검사가 통과했다.

최초 정렬의 final `post-static-v3`와 `vanilla-control-v1`은 모두 `STATE_NONLAND_PROVINCE` ERROR 118건을 냈고 전체 sorted ERROR key 차이는 0이었다. 따라서 당시 scan 기준 mod-introduced map ERROR는 0이었다. v3 output은 `<PROJECT>/.local-artifacts/analysis/china-japan-vanilla-alignment-2026-09-01/post-static-v3/`이며 `summary.json` SHA-256은 `93889ECF966BC76E69A7ECF8991B498B7A098D45FAE7CA77488E8690A2C3D17A`다. 이 결과는 당시 도구 v11이 state ID 구멍을 검사하지 않았다는 한계를 함께 보존한다.

후속 마이그레이션의 최종 source bytes는 scanner v12로 `<PROJECT>/.local-artifacts/audits/2026-09-01-map-post-migration-v6-tsushima-1085-final/`에 고정했다. v6는 195 findings (`ERROR` 118, `WARNING` 17, `INFO` 60)을 기록했으며 `MISSING_STATE_ID`, `BUILDINGS_TRAILING_NEWLINE`, `BUILDING_UNKNOWN_STATE`, `MISSING_AIR_BASE_SITE`, `MISSING_ROCKET_SITE`는 모두 0이다. 유일한 ERROR code는 `STATE_NONLAND_PROVINCE` 118건이고 `<PROJECT>/.local-artifacts/audits/2026-09-01-vanilla-control-v12/`와 code/count가 정확히 같다. 따라서 targeted migration finding은 0이고 전체 ERROR code/count 차이도 0이다. 다만 scanner의 raw `static_result`는 vanilla-shared 118건과 도구 한계 때문에 `FAIL`로 유지하며 이를 전체 정적 PASS로 바꾸지 않는다. v6 `summary.json` SHA-256은 `119D97F853C7FF9A588B804A596785CE984D4E3AF29759FE1A4CFB5AFAB716B3`, `findings.tsv` SHA-256은 `726B7B883203686502D155BA2337BA48430E0242087C1CC9E1496AC3C9C3CB5F`, `inputs.tsv` SHA-256은 `CC79AE36873D83149D76943567D44DC483854E90D32F3B84B56D5F2CA3460C2F`다. v6는 KOR decision의 기존 CRLF 형식을 복원한 뒤 v5를 supersede한다.

추가 production 감사에서는 effective character·tag·focus·event·JAP/KOR decision duplicate, unresolved JAP focus·JAP/KOR character, 삭제한 HoK 일본 ID의 live reference, state/region membership 누락·중복, building unknown state, supply/rail bad reference와 duplicate가 모두 0이었다.

## 9. 런타임 검증 계약

### 9.1 실행 조건

각 실행에서 HOI4 version/build/checksum, DLC, historical AI 설정, game rules, language, playset, load order, launcher가 로드한 물리 경로와 시작·종료 시각을 기록한다. 서로 다른 실행의 로그와 WER을 섞지 않는다.

| 실행 ID | 구성 | 목적 |
|---|---|---|
| `A-CJ-BASE` | 1.19.2 바닐라 | 같은 game rules에서 일본 역사 경로와 중국 색상 기준 확보 |
| `D-CJ-POST` | HoK 단독 | 중국·일본 정렬과 한국 보존을 의존 모드 없이 분리 검증 |
| `C-CJ-POST` | HoK + 정확한 `Korean Language` | 실제 지원 playset 최종 검증 |

최초 `D-CJ-POST-205045`는 `FAIL`이다. 20:51:55 실행, 20:58:20 싱글플레이 시작, 20:58:22 map load crash까지 실패 evidence bundle에 고정했다. 쓰시마 `1088 → 1085` 적용 뒤 `D-CJ-POST-FIX`는 21:13:20 시작, 21:20:15 싱글플레이 시작, 21:20:23 map 진입, 1/7/30일 진행과 정상 종료를 통과했다. 따라서 exact HoK-only map/crash gate는 `PASS`, `C-CJ-POST`는 `NOT RUN`이다.

### 9.2 화면·지도

- [ ] CHI, PRC, MAN, SND와 주요 중국 군벌의 map color와 UI color가 `A-CJ-BASE`와 일치한다.
- [ ] 산둥 state owner·controller·core와 국가 색상이 target과 일치한다.
- [ ] states `328`, `714`, `715`, `716`, `717`, `761`의 경계·자원·VP·건물·보급·철도가 target과 일치한다.
- [ ] 한국 9도, custom province, state `1085` 쓰시마, 항구·보급·철도·유닛 위치는 HoK 보존 기준과 일치한다.
- [ ] 일본군이 독립 한국의 평양·서울·부산에 잘못 생성되지 않는다.
- [ ] 지원 bookmark가 1936과 1939라면 두 시작일 모두에서 일본 land·naval OOB 위치를 확인한다.

### 9.3 일본 역사 동작

- [ ] historical AI에서 일본이 target historical focus plan을 선택하고 `JAP_reinforce_the_beijing_garrison` 경로를 정상 진행한다.
- [ ] `A-CJ-BASE`가 만든 통제 milestone과 비교해 1937년 전후 일본과 CHI 사이의 전쟁이 실제로 발생한다. 기억한 고정 날짜 하나만 pass 조건으로 쓰지 않는다.
- [ ] 1936 historical AI에서 1939년 1월 경고, 6월 최후통첩, KOR/state `525` 전쟁명분과 실제 대한 선전포고가 발생하고, 동시에 target 중일전쟁 경로가 유지된다.
- [ ] 일본의 MIO, character, starting idea, OOB와 division name group이 정상 등록된다.
- [ ] 중국전쟁 뒤 남방전쟁·이벤트·decision이 target control과 비교 가능한 순서로 진행한다.

### 9.4 한국 회귀

- [ ] 한국으로 새 게임을 시작하고 focus tree, 주요 decision·event·character·idea·OOB·localisation을 확인한다.
- [x] `D-CJ-POST-FIX`에서 1일·7일·30일 진행과 정상 종료를 통과했고 `Missing State ID`·`MAP_ERROR`는 0이다. post-map non-crash error 6줄은 별도 사건으로 분리한다.
- [ ] 승인된 disposition에 따라 간도·안둥·헤이허 기능이 제거·재설계·예외 보존됐고, 그 밖의 한국 핵심 경로가 끊기지 않는다.
- [ ] DLC on/off에서 일본·중국의 대체 분기와 KOR gate를 각각 확인한다.
- [ ] 새 게임 save/reload를 통과한다. 기존 persistent map ID 세이브 호환성을 주장하지 않는다.
- [ ] `C-CJ-POST`에서 Korean Language의 UI·font·localisation을 확인한다.

## 10. 완료 판정과 남은 위험

production 구현과 post-migration v6 map scan은 적용됐지만 전체 런타임 완료 판정은 아직 아니다. 중국·일본 바닐라 정렬은 다음 조건을 모두 만족해야 완료로 판정한다.

- 파일 registry와 target hash가 기록됨
- stale exact-path override와 additive 일본 동작이 승인 범위대로 처리됨
- 중국·만주 state 보존표와 한국 기능 손실 목록이 확정됨
- static reference와 map integrity 검사 통과
- `D-CJ-POST`와 `C-CJ-POST`의 새 게임·map·unpause·행동 검증 통과
- 일본의 중일전쟁 경로와 한국 핵심 콘텐츠를 함께 확인
- 새 관련 crash와 WER 없음
- diff에 무관한 밸런스·한국 콘텐츠 삭제·일괄 formatting 없음

`D-CJ-POST-FIX`의 exact HoK-only map/crash gate는 통과했다. 아직 통과하지 않은 항목은 `C-CJ-POST`, save/reload, 중국·산둥 실제 렌더링, 일본 historical AI의 중일전쟁, 1939 bookmark, DLC 조합별 분기, 비역사 AI, multiplayer checksum, 기존 세이브, 서브모드, Korean Language 1.19.2 호환성과 모든 한국 대체역사 경로다. 이번 구현은 production mod의 코드·맵을 수정했고 외부 live 로그·crash data는 읽어 evidence bundle로 복사했지만 descriptor·launcher·base game·원본 live 로그는 수정하지 않았다. commit·push도 수행하지 않았다.
