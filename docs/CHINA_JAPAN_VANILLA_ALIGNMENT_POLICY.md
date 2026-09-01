# 중국·일본 1.19.2 바닐라 정렬 정책

## 문서 상태

- 작업 모드: **Documentation only**
- 목표 게임: HOI4 `Operation Postern v1.19.2.0.a729 (d245)`
- 기준 데이터: 설치된 목표 버전 Vanilla (`V_TARGET`)
- 정책 우선순위: **HoK 한국 보존 > 중국·만주·일본의 HoK 변경 보존**
- 구현 상태: **NOT STARTED — 이 문서 작성으로 게임 데이터는 변경하지 않음**
- 런타임 검증: **NOT RUN — 현재 로그의 읽기 전용 분석만 수행**
- Git 기준선: branch `main`, HEAD `07bba722b6541c9b2316bee29a450ee4e08b888a`
- working tree: 기존 target-native 맵 구현과 문서 변경이 남아 있는 dirty 상태이며, 이번 문서화에서 이를 되돌리거나 production 파일을 수정하지 않음
- production mod root: `C:\hoi\hearts_of_korea`
- target root: `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`
- live log root: `C:\Users\jaewo\OneDrive\문서\Paradox Interactive\Hearts of Iron IV\logs`

이 문서는 Hearts of Korea의 한국 콘텐츠와 한국 지도는 최대한 보존하면서 중국·만주·일본 데이터는 HOI4 1.19.2 바닐라와 다시 정렬하기 위한 후속 구현 계약이다. 사용자는 이 정렬 과정에서 HoK의 중국·일본 전용 기능이 일부 사라지는 것을 허용했다. 이번 작업 범위는 문서화뿐이며, 아래 파일 제거·교체·추출·ID 변경은 아직 적용하지 않았다.

관련 문서:

- [1.19.2 맵 재구성 설계](HOK_MAP_RECONSTRUCTION_PLAN.md)
- [맵 호환성 점검표](MAP_COMPATIBILITY_CHECKLIST.md)
- [수정 후 검증 점검표](VALIDATION_CHECKLIST.md)
- [target-native 맵 구현 기록](incidents/2026-09-01-target-native-map-implementation.md)
- [fresh 맵 격리 사건](incidents/2026-09-01-fresh-map-isolation.md)

## 1. 결정

후속 구현의 기본식은 다음과 같다.

```text
V_TARGET 1.19.2 중국·만주·일본 데이터
+ 보존이 승인된 HoK 한국 콘텐츠
+ 독립 한국과 HoK 한국 지도에 꼭 필요한 최소 접점 delta
= 중국·일본 바닐라 정렬 후보
```

구현 원칙은 다음과 같다.

1. 중국·만주·일본의 국가 색상, state, focus, decision, event, AI, character, MIO, country history와 OOB는 목표 버전 바닐라를 기본값으로 한다.
2. 같은 상대경로의 구형 전체 파일은 가능하면 모드에서 제거해 목표 버전 파일을 상속한다. 바닐라 파일을 저장소에 통째로 복사해 새 고정 snapshot으로 만들지 않는다.
3. 한국 전용 정의만 필요한 전역 데이터베이스는 목표 바닐라를 상속하고, HoK 고유 항목만 고유 파일명과 고유 ID로 분리한다.
4. `KOR` focus·event·decision·idea·character·history·OOB·asset·localisation과 한국 province/state topology는 보존 대상이다.
5. 구형 중국·일본 시스템을 유지하기 위해 현행 바닐라 정의를 다시 덮어쓰지 않는다. 한국 caller가 꼭 필요로 하는 일본·중국 접점만 현재 바닐라 의미를 확인한 뒤 별도 `HOK_` 호환 계층으로 이식한다.
6. 숫자 전역 치환, 중국 province 재채색, 바닐라 설치본 수정, `replace_path` 추가는 금지한다.
7. 시작 크래시 복구 사건과 중국·일본 gameplay 정렬은 별도 사건이다. 현재 증거는 구형 중국·일본 코드가 1.19.2와 불일치함을 입증하지만, 그것이 이미 해결된 시작 크래시의 직접 원인이었다고 입증하지는 않는다.

## 2. 보존 경계

| 영역 | 후속 기준 | 비고 |
|---|---|---|
| 한국 province `13414–13447` | `PRESERVE_KOREA` | 검증된 한국 crop의 geometry를 보존한다. |
| 한국 state `525`, `527`, `1028–1031`, `1082–1084` | `PRESERVE_KOREA` | HoK 한국 9도 분할과 연결 콘텐츠를 보존한다. |
| 쓰시마 state `1088`와 province `10011` 분리 | `TARGET_DERIVED_KOREA_DELTA` | 일본 본토 state `528`은 target 기반으로 두고 쓰시마 분리만 유지한다. |
| 간도·안둥·헤이허 state `1085–1087` | `DEFERRED_REVIEW → INHERIT_TARGET` | 중국·만주 target 정렬의 목표는 source state `328`, `714`, `716`, `717` 복원이지만 KOR 영유권 기능과 persistent ID 처리 결정을 먼저 받는다. |
| 중국·만주 province bitmap/RGB | `INHERIT_TARGET` | 현재 target과 다른 1,889 pixel은 한국 crop 안에만 있다. 중국을 다시 칠하지 않는다. |
| 중국·만주 국가 색상·cosmetic·name pool | `INHERIT_TARGET` + 한국 delta | stale 전역 snapshot을 제거하고 HoK 한국 정의만 분리한다. |
| 중국·만주 국가 history·focus·AI·OOB | `INHERIT_TARGET` | HoK 한국을 직접 호출하는 접점만 별도 검토한다. |
| 일본 focus·decision·event·AI·character·MIO·history·OOB | `INHERIT_TARGET` | 구형 HoK 일본 시스템과 강제 대한전쟁은 제거 대상이다. |
| 한국이 일본·중국을 상대하는 HoK 콘텐츠 | `PRESERVE_KOREA` 또는 최소 bridge | 현행 바닐라 ID·scope와 호환되는 caller만 유지한다. |
| KJP·KCH·RKY·ANU·TWN 등 HoK 고유 태그·cosmetic | `DEFERRED_REVIEW` | 한국 경로에 실제 필요한 항목만 보존한다. stale 전역 파일 유지 근거로 사용하지 않는다. |

`1085–1087` 제거는 persistent state ID를 없애고 KOR 영유권 콘텐츠도 바꾸는 마이그레이션이다. 기존 세이브와 해당 ID를 참조하는 서브모드는 호환 대상으로 주장하지 않는다. 실제 삭제 전에 영향표, KOR 기능별 `REMOVE`·`REDESIGN`·`KEEP_EXCEPTION` 결정과 구현 승인을 별도로 기록한다.

## 3. 증거와 판정

현재 분석한 live 로그는 HoK 단독 `D-POST` 장기 실행에서 생성됐고 `Korean Language`는 활성화되지 않았다. 정확한 historical AI checkbox와 모든 game rule이 불변 실행 기록으로 묶여 있지 않으므로, 일본의 관찰 동작은 이 실행에서 발생한 사실과 그 원인 가설을 구분한다.

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
- 이 state 차이가 현재 시작 크래시의 원인이라는 주장은 현재 재현에서 입증되지 않았다. `UNPROVEN`

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

이 로그는 읽기 시점에 실행 중인 게임이 사용하던 live 파일이므로 불변 증거 bundle이 아니다. 후속 구현 전에 원본 로그를 실행 ID와 SHA-256 manifest로 별도 보존해야 한다.

### 3.4 핵심 exact-path 관찰 hash

다음 값은 2026-09-01 문서화 시점의 working tree와 설치된 target 1.19.2를 식별한다. 원본 HoK 불변 archive의 manifest를 대신하지 않으며, 구현 직전 다시 계산한다.

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

## 4. 파일 분류 규칙

각 영향 파일은 구현 전에 다음 중 하나로 등록한다.

| 분류 | 의미 |
|---|---|
| `INHERIT_TARGET` | 모드의 stale override를 제거하고 설치된 1.19.2 파일을 그대로 상속한다. |
| `TARGET_DERIVED_KOREA_DELTA` | target 파일을 기준으로 한국에 필요한 최소 차이만 유지한다. |
| `PRESERVE_KOREA` | HoK 한국 전용 정의를 그대로 보존하되 target ID·scope 호환성을 검사한다. |
| `REMOVE_STALE_OVERRIDE` | 구형 전체 snapshot이나 HoK 중국·일본 전용 additive 동작을 제거한다. |
| `DEFERRED_REVIEW` | 한국 경로의 실제 caller나 의미가 불명확해 자동 제거·이식하지 않는다. |

등록표에는 상대경로, loader/override 방식, mod·target SHA-256, 주요 ID, 한국 caller, DLC gate, save·서브모드 영향, 증거 등급과 승인 상태를 적는다. target 버전이 바뀌면 모든 target hash와 의미 비교를 다시 수행한다.

## 5. 중국·만주 후속 구현 명세

### 5.1 색상·cosmetic·name pool

| 현재 경로 | 후속 처리 | 한국 보존 처리 |
|---|---|---|
| `common/countries/colors.txt` | `REMOVE_STALE_OVERRIDE` 후 target 상속 | KOR의 파란색과 실제 필요한 KJP·KCH·RKY·TWN·ANU 색상만 고유 `HOK_` 파일로 추출한다. |
| `common/countries/cosmetic.txt` | `REMOVE_STALE_OVERRIDE` 후 target 상속 | `KOR_Goguryeo`, `KOR_PRK_communism`, `KJP_PSJ` 중 실제 caller가 있는 정의만 고유 파일로 추출한다. |
| `common/names/00_names.txt` | target 기반으로 복귀 | target name pool 전체를 가리지 않도록 KOR 고유 block만 검증된 방식으로 분리한다. |
| `common/units/names_ships/CHI_ship_names.txt` | target 상속 | 한국 caller가 없는지 확인한 뒤 구형 중국 함명 snapshot을 제거한다. |

산둥은 별도의 임의 색을 지정하지 않는다. 목표 결과는 target `SND`의 국가 색과 UI 색을 그대로 사용하는 것이다. 국가 정치색과 province bitmap RGB는 서로 다른 데이터이므로 province를 다시 칠하는 방식으로 해결하지 않는다.

### 5.2 state·전략 지역·보급망

| 항목 | 후속 처리 |
|---|---|
| `history/states/1085 - Jiandao.txt` | 제거하고 target source states를 상속한다. |
| `history/states/1086 - Andung.txt` | 제거하고 target source states를 상속한다. |
| `history/states/1087 - Heihe.txt` | 제거하고 target source states를 상속한다. |
| `328-Manchukuo`, `714-Heilungkiang`, `716-Liaotung`, `717-Chuho` | province membership과 history를 target과 일치시킨다. |
| `715-Liaoning`, `761-Hulunbuir` | 현재 category·VP 등 차이를 감사한 뒤 중국·만주 완전 정렬 범위에서는 target을 상속한다. |
| strategic regions `155`, `243` | `3970`, `6860`, `6910`, `6981`의 HoK 이동을 되돌리고 target membership을 상속한다. |
| `common/on_actions/14_sea_on_actions.txt` | `1086` Great Wall delta를 제거하고 target을 base로 삼되, 별도 감사에서 승인된 `1082–1084` 한국 semantic delta만 유지한다. |
| `map/buildings.txt` | 전체 파일을 제거하지 않고 states `328`, `714`, `716`, `717`의 target rows 복원과 `1085–1087` rows 제거만 수행한다. 한국 항구·site 보정은 보존한다. |
| `map/supply_nodes.txt` | Manchuria mod-only node `11781`을 제거하고 한국 node는 보존한다. |
| `map/railways.txt` | target에 없는 Manchuria branch를 제거하고 한국 route는 보존한다. |
| `map/unitstacks.txt` | 현재 추가분이 한국 custom province에 한정되므로 중국 rollback 대상으로 삼지 않는다. |
| `history/units/MAN_1936.txt` | target OOB를 상속한다. |

state 복구 전에는 source state별 province 집합, manpower, resource, factory, victory point, category, owner, controller와 core의 전후 합계표를 작성한다. 특히 현재 state `716`은 target의 chromium `4`, tungsten `4`, oil `3`을 포함하지 않으므로, 이를 의도된 HoK 밸런스로 단정하지 않고 target 복원 대상으로 취급한다.

`1085`와 `1086`은 여러 target state 조각으로 구성돼 1:1 대체 ID가 없다. `common/decisions/KOR_decision.txt`, `common/national_focus/korea.txt`, `common/on_actions/gookppong_on_actions.txt`, `events/korea.txt`와 관련 localisation의 세부 간도·안둥·헤이허 claim/transfer는 `DEFERRED_REVIEW`다. strict China target을 택하면 제거가 가장 보수적인 후보지만 이 문서만으로 삭제를 승인하지 않는다. 이를 target state `328`, `716`, `717` 전체에 치환하면 한국의 영토·자원·밸런스를 확대하므로 자동 이식하지 않으며, 다른 방식으로 보존하려면 별도 gameplay 설계와 승인이 필요하다.

## 6. 일본 후속 구현 명세

### 6.1 target 상속 대상

다음 exact-path 파일은 1.19.2 target과 서로 다른 구형 snapshot이다. 기본 조치는 모드 override 제거와 target 상속이다.

- `common/national_focus/japan.txt`
- `common/ai_strategy/JAP.txt`
- `common/ai_strategy_plans/JAP_alternate_strategy_plan.txt`
- `common/decisions/JAP.txt`
- `common/characters/JAP.txt`
- `history/countries/JAP - Japan.txt`
- `common/units/names_divisions/JAP_names_divisions.txt`
- `history/units/JAP_1936.txt`
- `history/units/JAP_1936_nsb.txt`
- `history/units/JAP_1936_naval.txt`
- `history/units/JAP_1936_naval_legacy.txt`

`common/bookmarks/the_gathering_storm.txt`는 stale 일본 focus ID를 포함하지만 KOR bookmark도 담고 있다. 따라서 단순 삭제가 아니라 target bookmark를 상속하면서 KOR entry만 최소 delta로 재구성한다.

다음 전역 공유 파일은 stale 일본·공용 데이터를 고쳐야 하지만 실제 KOR block이나 KOR 제외 조건도 포함하므로 `TARGET_DERIVED_KOREA_DELTA`로 처리한다.

- `common/military_industrial_organization/organizations/00_generic_organization.txt`
- `common/on_actions/04_mtg_on_actions.txt`
- `common/scripted_effects/SP_scripted_effects.txt`
- `common/intelligence_agencies/00_intelligence_agencies.txt`
- `common/difficulty_settings/00_difficulty.txt`
- `history/general/generic_advisors.txt`

각 파일은 target 기준으로 다시 만들고, generic MIO·advisor에서 custom KOR 중복을 막는 조건, KOR difficulty·intelligence agency, KOR special-project asset과 독립 한국 lifecycle에 필요한 block만 개별 검토해 남긴다. 전역 파일을 단순 삭제하거나 현재 구형 snapshot을 유지하지 않는다.

일본 state `282`, `530`, `531`, `536`, `537`의 구형 HoK 밸런스 override는 target을 상속한다. state `528`은 target을 기준으로 하되 province `10011`을 state `1088` 쓰시마로 분리한 map delta만 유지한다.

### 6.2 HoK 일본 전용 additive 제거 대상

다음 파일은 target 파일을 같은 경로에서 덮지는 않지만 일본의 비바닐라 동작을 추가한다. 중국·일본 바닐라 정렬에서는 제거 또는 비활성 대상이다.

- `common/ai_strategy/JAP_HoK.txt`
- `common/decisions/JAP_HoK_decision.txt`
- `common/decisions/categories/JAP_HoK_decision_category.txt`
- `events/japan_HoK.txt`
- `common/ideas/democratic_japan.txt`의 일본 전용 idea
- `common/military_industrial_organization/organizations/JAP_HoK_organization.txt`
- `common/peace_conference/ai_peace/JAP_HoK.txt`
- `common/on_actions/buff_japan_if_japan_is_ai_on_actions.txt`

여기에는 AI 일본에 시작 전차사단 8개를 주는 on-action과 1936년 보병사단 30개 생성, 1939년 한국 최후통첩·전쟁을 강제하는 HoK 일본 경로가 포함된다. 제거 후 일본이 1939.06.26 한국에 선전포고하던 기존 동작은 보존하지 않는다. 이 기능 손실은 사용자가 허용한 중국·일본 바닐라 정렬의 의도된 결과다.

custom 일본 focus만 참조하는 GFX·flag·localisation은 엔진 동작에 관여하지 않는 것이 확인되면 즉시 삭제할 필요가 없다. 배포 정리는 호환성 구현과 분리한다.

### 6.3 한국 보존을 위한 최소 일본 접점

- KOR가 JAP·CHI·PRC 등의 puppet이 될 때 KOR cosmetic만 적용하는 `common/on_actions/HoK_cosmetic_tag_on_actions.txt`는 일본 AI를 변경하지 않으므로 보존 후보로 둔다.
- 1.19.2 일본 트리에는 독립 한국을 다루는 `JAP_the_korean_question`과 KOR 존재·종속·동맹 분기가 있다. 독립 한국 때문에 구형 일본 tree를 유지하지 않는다.
- target 일본 OOB는 바닐라에서 일본령인 평양 `4052`, 서울 `7125`, 부산 `4056`에 부대를 배치한다. HoK에서는 한국이 독립이므로 land OOB 위치 `4052 → 7169`, `7125 → 12031`, `4056 → 10011`과 부산 함대 `4056 → 10011`만 target OOB 위에 다시 적용한다. 이 bridge는 1936의 `JAP_1936*`뿐 아니라 1939의 `JAP_1939.txt`, `JAP_1939_nsb.txt`, `JAP_1939_naval.txt`, `JAP_1939_naval_legacy.txt`에도 필요하다. 1939 bookmark를 지원하지 않을 경우에는 누락된 호환을 방치하지 말고 비지원 범위로 명시한다. 나머지 OOB 정의는 target을 따른다.
- `events/korea.txt`의 구형 `JAP_sign_tripartite_pact` caller는 현행 후보 `JAP_sea_tripartite_pact`와 의미·DLC gate를 비교한 뒤 단일 Korea bridge로 이관한다. 이름만 보고 자동 치환하지 않는다.
- `common/ai_strategy/KOR.txt`가 참조하는 `JAP_strengthen_civilian_government`는 1.19.2에도 존재하므로 유지 가능하다.
- KOR focus·event가 더 이상 존재하지 않는 HoK 일본 ID를 요구하면 일본 코드를 되살리지 않고 KOR caller를 제거하거나 현행 의미로 최소 이식한다.

### 6.4 한국 state semantic fan-out

한국 9도 분할로 추가된 `1082–1084`는 단순 표시용 state가 아니다. target 1.19.2가 한국 전체·남부·북부를 열거하는 다음 파일은 현재 여섯 target state만 알고 있으므로, target-derived Korea compatibility 후보로 별도 감사한다.

- `common/scripted_triggers/JAP_scripted_triggers.txt`의 한국 전체·남부·북부 판정
- `common/on_actions/14_sea_on_actions.txt`의 한국 저항·소유권 관련 열거
- `common/decisions/KOR.txt`의 state 대상 결정
- `events/WTT_Japan.txt`의 한국 소유권·해방·이전 효과

각 block에서 `1082`, `1083`, `1084`가 어느 의미 집합에 들어가는지 지리와 효과별로 결정한다. target 목록에서 state `525`가 빠진 곳은 단순 누락으로 단정하지 말고 target 의도를 확인한다. 이 작업은 startup crash 수정이 아니라 후속 gameplay 호환성이며, 같은 숫자의 province 참조와 섞어 일괄 치환하지 않는다.

## 7. 후속 구현 순서

1. `CJ-PRE` 사건 ID로 현재 live 로그와 실행 조건을 불변 보존하고 SHA-256 manifest를 만든다.
2. 파일 registry에 모든 exact-path shadow와 additive 중국·일본 파일을 등록한다.
3. 국가 색상·cosmetic·name pool의 stale 전역 snapshot을 target 상속 + HoK 한국 전용 파일로 분리한다.
4. `1085–1087`과 연결된 KOR 기능의 disposition을 승인한 뒤 중국·만주 state, region, Great Wall, buildings, rail과 supply를 의미 단위로 복원한다.
5. 일본 focus·AI·decision·character·history·MIO·name·OOB를 target 상속으로 전환하고 HoK 일본 전용 additive 동작을 제거한다.
6. bookmark, 일본 OOB 위치, 쓰시마 state `1088`, KOR caller만 target-derived Korea delta로 재적용한다.
7. 정적 검사를 통과한 뒤 `D-CJ-POST`, 실제 지원 구성 `C-CJ-POST` 순서로 새 게임 런타임을 검증한다.
8. 이후 남는 MIO·event·character·technology·localisation 오류는 각각 별도 사건으로 분리한다.

각 단계는 작은 diff와 독립 검증 기록을 가져야 한다. 중국 state 복구, 일본 데이터 복구, 한국 bridge는 가능하면 별도 commit 후보로 유지하되 실제 commit·push는 별도 지시가 있을 때만 수행한다.

## 8. 정적 완료 조건

- [ ] target `colors.txt`, `cosmetic.txt`, `00_names.txt`가 유효하게 상속되고 HoK 전용 delta가 target-only tag를 가리지 않는다.
- [ ] `SND` country color와 `color_ui`가 target 값과 일치한다.
- [ ] `REMOVE`가 승인된 경우 states `1085–1087`의 state-context 참조가 0이며, 같은 숫자의 province ID 참조를 오탐으로 바꾸지 않았다.
- [ ] states `328`, `714`, `716`, `717`의 province membership과 history가 target과 일치한다.
- [ ] regions `155`, `243` membership이 target과 일치한다.
- [ ] 영향 state의 `buildings.txt` rows가 target과 일치하고 한국 site·port 보정은 유지된다.
- [ ] Manchuria rail·supply delta 제거 결과가 allowlist와 일치한다.
- [ ] 현행 `JAP_historical_strategy_plan`이 참조하는 focus가 모두 등록된다.
- [ ] 구형 focus, decision category, character, division name group, idea, technology와 MIO의 invalid 참조가 0이다.
- [ ] `JAP_HoK` 강제 전쟁·buff caller가 유효 실행 경로에서 제거됐다.
- [ ] KOR ID·namespace·localisation·asset과 한국 map registry가 보존됐다.
- [ ] `1082–1084`가 한국 전체·남부·북부 판정, 저항, decision와 WTT Japan 효과에 문맥별로 반영됐다.
- [ ] 1936과 지원하는 경우 1939 일본 OOB의 한국 위치가 승인된 일본·쓰시마 위치로만 이동했다.
- [ ] changed file의 brace·quote·encoding·line ending에 의도치 않은 전역 변경이 없다.

## 9. 런타임 검증 계약

### 9.1 실행 조건

각 실행에서 HOI4 version/build/checksum, DLC, historical AI 설정, game rules, language, playset, load order, launcher가 로드한 물리 경로와 시작·종료 시각을 기록한다. 서로 다른 실행의 로그와 WER을 섞지 않는다.

| 실행 ID | 구성 | 목적 |
|---|---|---|
| `A-CJ-BASE` | 1.19.2 바닐라 | 같은 game rules에서 일본 역사 경로와 중국 색상 기준 확보 |
| `D-CJ-POST` | HoK 단독 | 중국·일본 정렬과 한국 보존을 의존 모드 없이 분리 검증 |
| `C-CJ-POST` | HoK + 정확한 `Korean Language` | 실제 지원 playset 최종 검증 |

### 9.2 화면·지도

- [ ] CHI, PRC, MAN, SND와 주요 중국 군벌의 map color와 UI color가 `A-CJ-BASE`와 일치한다.
- [ ] 산둥 state owner·controller·core와 국가 색상이 target과 일치한다.
- [ ] states `328`, `714`, `715`, `716`, `717`, `761`의 경계·자원·VP·건물·보급·철도가 target과 일치한다.
- [ ] 한국 9도, custom province, 쓰시마, 항구·보급·철도·유닛 위치는 HoK 보존 기준과 일치한다.
- [ ] 일본군이 독립 한국의 평양·서울·부산에 잘못 생성되지 않는다.
- [ ] 지원 bookmark가 1936과 1939라면 두 시작일 모두에서 일본 land·naval OOB 위치를 확인한다.

### 9.3 일본 역사 동작

- [ ] historical AI에서 일본이 target historical focus plan을 선택하고 `JAP_reinforce_the_beijing_garrison` 경로를 정상 진행한다.
- [ ] `A-CJ-BASE`가 만든 통제 milestone과 비교해 1937년 전후 일본과 CHI 사이의 전쟁이 실제로 발생한다. 기억한 고정 날짜 하나만 pass 조건으로 쓰지 않는다.
- [ ] 구형 HoK 최후통첩 때문에 일본이 1939.06.26 한국에 강제 선전포고하지 않는다.
- [ ] 일본의 MIO, character, starting idea, OOB와 division name group이 정상 등록된다.
- [ ] 중국전쟁 뒤 남방전쟁·이벤트·decision이 target control과 비교 가능한 순서로 진행한다.

### 9.4 한국 회귀

- [ ] 한국으로 새 게임을 시작하고 focus tree, 주요 decision·event·character·idea·OOB·localisation을 확인한다.
- [ ] 1일·7일·30일 진행 중 crash, event spam이나 관련 error 증가가 없다.
- [ ] 승인된 disposition에 따라 간도·안둥·헤이허 기능이 제거·재설계·예외 보존됐고, 그 밖의 한국 핵심 경로가 끊기지 않는다.
- [ ] DLC on/off에서 일본·중국의 대체 분기와 KOR gate를 각각 확인한다.
- [ ] 새 게임 save/reload를 통과한다. 기존 persistent map ID 세이브 호환성을 주장하지 않는다.
- [ ] `C-CJ-POST`에서 Korean Language의 UI·font·localisation을 확인한다.

## 10. 완료 판정과 남은 위험

문서 작성 완료는 구현 완료가 아니다. 중국·일본 바닐라 정렬은 다음 조건을 모두 만족해야 완료로 판정한다.

- 파일 registry와 target hash가 기록됨
- stale exact-path override와 additive 일본 동작이 승인 범위대로 처리됨
- 중국·만주 state 보존표와 한국 기능 손실 목록이 확정됨
- static reference와 map integrity 검사 통과
- `D-CJ-POST`와 `C-CJ-POST`의 새 게임·map·unpause·행동 검증 통과
- 일본의 중일전쟁 경로와 한국 핵심 콘텐츠를 함께 확인
- 새 관련 crash와 WER 없음
- diff에 무관한 밸런스·한국 콘텐츠 삭제·일괄 formatting 없음

아직 확인하지 않은 항목은 DLC 조합별 분기, 비역사 AI, multiplayer checksum, 기존 세이브, 서브모드, Korean Language 1.19.2 호환성과 모든 한국 대체역사 경로다. 이 문서 작성 시에는 코드·맵·descriptor·launcher·base game·로그를 수정하지 않았고 게임도 새로 실행하지 않았다.
