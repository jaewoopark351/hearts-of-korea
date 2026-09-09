# 2026-09-09 HoK 일본 민주주의 전체 분기 1.19.2 통합 구현 기록

> 상태: **D-JAP-15 절대좌표 fallback 및 D-JAP-16/17 정치·SEA HIDE 동작 확인 / D-JAP-18 최소 수정·fresh startup 통과 및 UI 확인 대기 / SHOW·역방향 잠금·save/load 미검증**
>
> 목표 게임: HOI4 `Operation Postern v1.19.2.0.a729 (d245)`
>
> 구현 기준: branch `main`, HEAD `887930f6e88c80568d62dab9cfbe1ba8a498a252`
>
> 원작 Workshop item `2898629778`은 읽기 전용 출처이며 successor 업로드 대상이 아니다.

이 문서는 [HoK 일본 민주주의 전체 분기 1.19.2 통합 설계](../HOK_JAPAN_DEMOCRATIC_BRANCH_INTEGRATION_PLAN.md)를 실제 production 소스에 적용한 결과를 기록한다. 사용자 제공 화면은 shared 분기의 로드와 이전 좌표 시안 문제뿐 아니라, 최초 D-JAP-16 적용 뒤 정상 SEA 산업·군부 계통만 사라지고 경쟁 NCNS 정치 하위 계통은 남는 역전 현상을 보여 준다. 19:32 로그와 source graph 재감사로 숨김 대상을 교정했고, 20:08 실행은 shared→ordinary 상대좌표안을 반증했다. 20:18 fresh 실행과 사용자 제공 완료 화면은 절대좌표 fallback의 로드 및 D-JAP-16/17 정치 숨김·SEA 공통 계통 재배치를 확인했다. 후속 22:03 화면에서는 `제국의 영향력` inlay가 HoK 완료 후 보이지 않는 D-JAP-18 회귀를 확인했다. D-JAP-18은 HoK 상태 전용 10번째 위치 override로 최소 수정했으며, 23:24 fresh startup과 1936 진입은 통과했다. 실제 패널 배치와 `SHOW`, 역방향 잠금, save/load는 아직 재검증하지 않았다.

## 1. 승인 범위

구현한 범위:

- 설치된 1.19.2 `japan_wtt_focus`의 바닐라 focus 448개를 보존한 target-derived host
- 원작 HoK 일본 민주주의 직결 focus 32개
- 민주·공산 공유 본토경제 focus 8개를 HoK 민주 root에 귀속한 총 40개 shared focus
- 실행에 필요한 event, idea, character, decision, localisation과 기존 GFX 연결
- 바닐라 정치 진입점과의 양방향 잠금
- 기존 KOR AI 조건의 최소 HoK root 인식
- Taiwan 독립 기능에 직접 필요한 `TWN` history의 제거된 doctrine-tech 참조 정리
- NCNS 정치 하위 자체 `allow_branch` 경계 9개의 HoK HIDE guard
- 완료 reward와 relayout 사이의 판정 시점을 제거하는 HoK 선택 flag
- D-JAP-18의 `HIDE` + HoK 완료/선택 flag 전용 imperial-influence inlay 위치 override 1개

구현하지 않은 범위:

- 원작 일본 AI strategy와 AI focus 선택
- `Minshu_ikki` 음악 조건 복구
- 원작 일본 전체 focus/history/OOB/character/MIO/decision snapshot 복원
- map/state/province/railway 데이터 변경
- 교정본의 실제 2·26 사건 완료·진행 중 `HIDE` UI, `SHOW`, save/load, 멀티플레이와 성능 검증
- SEA 산업·군부의 gameplay 또는 visibility 변경. D-JAP-17의 HoK-HIDE용 산업 root 위치 offset 1개만 예외
- 경제·군부 shortcut 위치 변경과 D-JAP-18 범위 밖의 imperial-influence GUI·가시성·gameplay 변경
- Git commit/push/tag, Workshop 업로드 또는 metadata 변경

## 2. 기준선과 증거

### 2.1 Git와 사용자 변경 보존

구현 시작 시 저장소는 clean이 아니었다. 다음 상태를 보존하고 관계없는 내용을 되돌리지 않았다.

- `M docs/CHINA_JAPAN_VANILLA_ALIGNMENT_POLICY.md`
- `M docs/VALIDATION_CHECKLIST.md`
- `?? docs/HOK_JAPAN_DEMOCRATIC_BRANCH_INTEGRATION_PLAN.md`

구현 전 runtime 로그는 다음 경로에 복사해 보존했다.

`.local-artifacts/incidents/2026-09-09-japan-democratic-integration/PRE-IMPLEMENTATION/`

보존 파일은 `error.log`, `game.log`, `setup.log`, `system.log`이다.

D-JAP-16 적용 직전 17:12 실행 로그도 다음 경로에 별도로 보존했다.

`.local-artifacts/incidents/2026-09-09-japan-democratic-integration/PRE-D-JAP-16-1712/`

최초 D-JAP-16 실행의 18:11 로그는 timing-safe flag 보강 전에 다음 경로로 보존했다.

`.local-artifacts/incidents/2026-09-09-japan-democratic-integration/PRE-D-JAP-16-FLAG-1811/`

timing-safe flag 보강 뒤 19:26 직접 실행 로그는 다음 경로로 보존했다.

`.local-artifacts/incidents/2026-09-09-japan-democratic-integration/POST-D-JAP-16-FLAG-1926-STARTUP/`

### 2.2 물리적 소스와 launcher 상태

- target 설치본: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV`
- 원작 읽기 전용 소스: `C:/Program Files (x86)/Steam/steamapps/workshop/content/394360/2898629778`
- production 저장소와 launcher `.mod`의 `path`: `C:/hoi/hearts_of_korea`
- repository/launcher dependency: `Korean Language`
- `replace_path`: 없음
- successor `remote_file_id`: `3793992662`; 이번 작업에서 변경하지 않음
- 조사 당시 `dlc_load.json`의 명시적 enabled mod는 `mod/hearts of korea.mod` 하나였다. 선언 dependency의 실제 자동 로드와 순서는 런타임에서 확인하지 않았다.

### 2.3 고정한 입력 hash

| 입력 | SHA-256 |
|---|---|
| target `common/national_focus/japan.txt` | `BF5EF4B6A17E70E4AD83030A0AAC4DE72105CB8803CA6F93A9BF3FCEF8662623` |
| 원작 `common/national_focus/japan.txt` | `61726A271861E243FA100F071EA5657E6D0CA70513F8D4D88EBCE369F1ABCCA5` |
| 원작 `events/japan_HoK.txt` | `A9A3D9EACB87CC865421C70D465E4FD2BC1785C333F4A14C4E2D55A825CDA4EC` |
| 원작 `common/ideas/democratic_japan.txt` | `0E1B313A43E04A2CCAC9DFABB6B9F6824CED15AB61B467C80A19E7D4E1B3B145` |
| 원작 `republican_japan_focus_l_english.yml` | `0136E1C5CDF22654C4B20EA27B26B1BA140EC3FAAA1BA66D73F04E0893C541CE` |

## 3. 구현 구조

```text
japan_wtt_focus (target 1.19.2 focus 448개)
└─ shared_focus = HOK_JAP_strengthen_civilian_government
   └─ HoK 일본 민주주의 모듈 40개
      ├─ 민주 직결 32개
      └─ 민주 root에 귀속한 공유 본토경제 8개
```

- host는 정확한 target `japan.txt`를 기준으로 추가했다.
- host에는 바닐라 WTT root 정의 뒤 shared root hook 하나, 바닐라 정치 진입점 6개의 HoK 상호배타/HIDE guard, NCNS 정치 하위 자체 `allow_branch` 경계 9개의 동일 HIDE guard, HoK-HIDE용 SEA 산업 root 위치 offset 1개와 D-JAP-18 inlay 위치 override 1개만 추가했다. 바닐라 root·inlay 기본 위치와 기존 9개 override·continuous-focus 좌표 및 SEA 산업·군부 계통은 정확한 1.19.2 target 값을 유지한다. D-JAP-18 추가분은 target에 없는 HoK 완료/선택 상태만 처리한다.
- HoK 본문은 `common/national_focus/HOK_JAP_democratic_shared.txt`에 격리했다.
- 배치 이력은 우측 후보 `x=155` → 좌측 절대 `x=-4` → 전체 `+8` 이동과 HoK 절대 `x=4` → `JAP_the_unthinkable_option` 상대 `(-2,0)` 순서다. 사용자 화면에서 앞선 두 절대좌표안은 각각 좌단 잘림과 과도한 공백이 확인됐고, 상대좌표안은 20:08 HOI4 1.19.2 실행에서 shared→ordinary 참조 오류가 확인돼 폐기했다. 현재 HoK root는 절대 `(10,0)`이며, 하위 39개의 상대좌표 사슬은 유지해 전체 범위가 `x=6..18`, `y=0..9`로 남는다.
- 본토경제 root는 HoK root의 prerequisite 자식 `x = 6`, `y = 1`로 연결했다. 따라서 host hook은 하나만 필요하다.
- root는 WTT와 NCNS가 모두 활성화된 환경에 한정하고 `is_ai = no`, `ai_will_do.factor = 0`으로 두었다.

양방향 잠금 대상은 다음 6개다.

- `JAP_the_unthinkable_option`
- `JAP_strengthen_civilian_government`
- `JAP_support_the_kodoha_faction`
- `JAP_okadas_military_purge_speech`
- `JAP_revere_the_emperor_destroy_the_traitors`
- `JAP_sea_purge_the_kodoha_faction`

2·26 사건 `SEA_japan.1`은 HoK root가 완료됐거나 진행 중이면 기존 5개 선택지를 숨기고 HoK 전용 선택지를 표시한다. root 진행 중 사건이 발동하면 원작의 56일 사건/70일 focus 계약처럼 HoK root를 조건부 완료하고 기존 인물 사상자 및 trial flag 처리를 유지한다. NCNS 민주 루트의 정치·정부 효과는 HoK 내전 경로를 건너뛰므로 이식하지 않았다.

### 3.1 후속 화면 관찰과 D-JAP-16 교정

최초 D-JAP-16은 화면의 잔존 묶음을 SEA 산업 34개와 군부 61개로 잘못 분류했다. 적용 뒤 사용자 화면에서는 이 정상 공통 계통만 사라지고, 실제로 숨겨야 할 NCNS 정치 하위 계통은 계속 남았다. 따라서 SEA root의 HoK mutex/HIDE guard, SEA 선택 flag·relayout과 군부 leaf guard를 전부 롤백했다.

정확한 원인은 `allow_branch` 상속 규칙이다. 일반 focus는 prerequisite 부모가 disallowed이면 함께 숨지만, 자체 `allow_branch`를 가진 focus는 부모 상태를 무시하고 자기 조건만 검사한다. NCNS 정치 구간에는 이런 독립 경계가 9개 있으며, 그중 장군 임명·육군 개혁·붉은 태양·총선 경계는 1936 초기 조건에서 참이어서 정치 root를 숨긴 뒤 최대 123개를 즉시 다시 표시할 수 있다. 조건부 경계와 prerequisite 없는 고이소 내각까지 포함하면 최대 잔존 범위는 135개다.

교정본은 301개 정치 focus를 개별 수정하지 않고 다음 9개 경계에 HoK 완료와 `HOK_JAP_democratic_branch_selected` 조건을 병합한다.

- `JAP_yatagarasus_guidance`
- `JAP_embodying_empress_jinguu`
- `JAP_solidify_tohokai_rule`
- `JAP_the_koiso_cabinet`
- `JAP_appoint_new_generals`
- `JAP_implement_army_reforms`
- `JAP_a_red_sun_rises_for_a_new_era`
- `JAP_the_spirit_of_the_ikko_ikki`
- `JAP_organize_a_general_election`

기존 정치 진입점 6개의 reciprocal mutex/HIDE guard와 HoK 완료 reward의 flag-before-relayout 순서는 유지한다. WTT 하위 자체 경계 두 곳은 NCNS 비활성 조건이므로 WTT+NCNS를 모두 요구하는 현재 HoK 지원 환경에서는 이미 false이며 중복 수정하지 않았다. `SHOW`에서는 바닐라 규칙에 따라 경쟁 정치 계통이 표시될 수 있으나 mutex로 진입을 막는다. SEA 산업·군부 95개는 HoK 완료 전후 모두 사용할 수 있게 복원하고, `HIDE`에서 HoK가 선택된 경우 산업 root 하나에 `x=-83` offset을 적용한다. 산업 범위는 `x=20..37`, 그 상대 자식인 군부 범위는 `x=39..65`가 되어 HoK 범위 `x=6..18` 바로 오른쪽에 배치된다.

## 4. Focus ID migration ledger

모든 focus는 충돌 여부와 무관하게 `HOK_JAP_` namespace로 이동했다.

| 원작 ID | 구현 ID |
|---|---|
| `JAP_strengthen_civilian_government` | `HOK_JAP_strengthen_civilian_government` |
| `JAP_ally_with_the_zaibatsus` | `HOK_JAP_ally_with_the_zaibatsus` |
| `JAP_research_spending` | `HOK_JAP_research_spending` |
| `JAP_returning_home_SMCR_elite` | `HOK_JAP_returning_home_SMCR_elite` |
| `JAP_invest_nigo_project` | `HOK_JAP_invest_nigo_project` |
| `JAP_oppose_peace_preservation_law` | `HOK_JAP_oppose_peace_preservation_law` |
| `JAP_memories_of_taisho_democracy` | `HOK_JAP_memories_of_taisho_democracy` |
| `JAP_purge_the_militarists` | `HOK_JAP_purge_the_militarists` |
| `JAP_pre_emptive_coup` | `HOK_JAP_pre_emptive_coup` |
| `JAP_the_showa_constitution` | `HOK_JAP_the_showa_constitution` |
| `JAP_proclaim_the_republic` | `HOK_JAP_proclaim_the_republic` |
| `JAP_strength_civilian_control` | `HOK_JAP_strength_civilian_control` |
| `JAP_new_officers` | `HOK_JAP_new_officers` |
| `JAP_joint_staff_office` | `HOK_JAP_joint_staff_office` |
| `JAP_citizen_in_uniform` | `HOK_JAP_citizen_in_uniform` |
| `JAP_review_foreign_policy` | `HOK_JAP_review_foreign_policy` |
| `JAP_datsuonyua` | `HOK_JAP_datsuonyua` |
| `JAP_go_with_korea` | `HOK_JAP_go_with_korea` |
| `JAP_rok_jpn_free_trade_agreement` | `HOK_JAP_rok_jpn_free_trade_agreement` |
| `JAP_rebuild_anglo_japanese_alliance` | `HOK_JAP_rebuild_anglo_japanese_alliance` |
| `JAP_pacific_guardian` | `HOK_JAP_pacific_guardian` |
| `JAP_anti_communist_bulwark` | `HOK_JAP_anti_communist_bulwark` |
| `JAP_liberation_of_manchuria` | `HOK_JAP_liberation_of_manchuria` |
| `JAP_demand_sagaren` | `HOK_JAP_demand_sagaren` |
| `JAP_rebuild_the_goverment` | `HOK_JAP_rebuild_the_goverment` |
| `JAP_abolition_peace_preservation_law` | `HOK_JAP_abolition_peace_preservation_law` |
| `JAP_expansion_of_local_autonomy` | `HOK_JAP_expansion_of_local_autonomy` |
| `JAP_disband_takumusho` | `HOK_JAP_disband_takumusho` |
| `JAP_free_election_in_taiwan` | `HOK_JAP_free_election_in_taiwan` |
| `JAP_develop_taiwan` | `HOK_JAP_develop_taiwan` |
| `JAP_integrate_nanyo_gunto` | `HOK_JAP_integrate_nanyo_gunto` |
| `JAP_develop_nanyo_gunto` | `HOK_JAP_develop_nanyo_gunto` |
| `JAP_develop_home_island` | `HOK_JAP_develop_home_island` |
| `JAP_making_use_of_our_islands` | `HOK_JAP_making_use_of_our_islands` |
| `JAP_karafuto_oil_field` | `HOK_JAP_karafuto_oil_field` |
| `JAP_home_island_agriculture` | `HOK_JAP_home_island_agriculture` |
| `JAP_development_tohoku_region` | `HOK_JAP_development_tohoku_region` |
| `JAP_modernize_tatara_ironworks` | `HOK_JAP_modernize_tatara_ironworks` |
| `JAP_tohoku_dairy_farming` | `HOK_JAP_tohoku_dairy_farming` |
| `JAP_sinkansen` | `HOK_JAP_sinkansen` |

`goverment`, `datsuonyua`, `sinkansen` 같은 원작 철자도 안정 ID의 provenance를 위해 유지했다.

## 5. 종속 콘텐츠와 1.19.2 적응

### 5.1 Event

- namespace를 `hok_jap_democratic`으로 통일했다.
- caller가 전혀 없는 원작 event `.11`은 이식하지 않았다. `.1-.10`, `.12-.23`의 22개 정의와 호출만 이식했다.
- 군국주의자 숙청은 target의 확장된 trait 집합 전체가 아니라 원작과 동일한 8명만 명시적으로 MAN으로 이전한다.
- 히로히토 numeric leader ID `700`은 `JAP_emperor_hirohito` character 검사로 바꿨다.
- `man_restored`는 실제 정의 `MAN_restored`로 고쳤다.
- `event_target:WTT_current_china_leader`는 존재할 때 사용하고 없으면 event 수신 CHI scope로 fallback한다.
- 내전 뒤 야마시타가 어느 일본측 태그에 배정됐든 원작처럼 복귀할 수 있도록, `JAP`의 로컬 `has_character` 검사로 막지 않고 target character scope에 직접 `set_nationality = JAP`를 적용한다.
- Taiwan 독립은 원작의 state 524 core → TWN 이전 → `set_autonomy` 흐름을 유지했다. `autonomous_state`는 target 1.19.2의 실제 `set_autonomy` 예제에서도 사용되는 key다. 미존재 TWN 활성화 결과는 런타임 확인 대상이다.
- 사할린, Taiwan, 만주와 중국 state 효과는 원작 의미를 유지했으며 map 파일은 수정하지 않았다.
- 만주 해방은 `MAN`이 실제 존재할 때만 전쟁 명분을 만들고, `MAN` 소멸 시 효과 없이 bypass한다. 한일 자유무역은 `KOR` 존재를 요구하며, 북사할린 요구는 `SOV`가 state 655를 실제 소유할 때만 시작한다. 소련 수락 후 양도 event도 소유권을 다시 검사해 제3국 영토를 강제 이전하지 않는다.

### 5.2 Ideas와 characters

- HoK 전용 idea 7개를 namespaced additive 파일에 정의했다.
- target에 이미 있는 `JAP_strengthen_civilian_government`, `JAP_militarism`, `MAN_militarism`, `MAN_kwantung_veto`, 저정통성 ideas와 재벌 ideas는 재사용한다.
- 신규 HoK character 7개만 additive 정의하고 root 완료 시 모집한다.
- target의 Katayama는 역할을 중복 추가하지 않고 기존 character를 `promote_character`로 승격한다.
- target의 Shidehara, Yamashita와 Yamaguchi를 재사용한다.
- Yamaguchi는 target에서 이미 사용 가능하므로 중복 정의하지 않았다.
- Yonai의 target navy role은 상충하는 NCNS focus에 gate돼 있어 HoK 보상에서 제외했다. 동일 인물 중복 생성을 피하기 위한 의도적 차이다.
- 원작의 이름 없는 `JAP_random_industry_minister_1` 보상은 raw/빈 이름을 피하기 위해 보류했다.

### 5.3 Decisions

- 북사할린 결정은 HoK focus 완료 뒤에만 보이며 state 655 core와 원작명 `Sagaren`을 적용한다. 전역 flag 대신 namespaced country flag를 사용한다.
- target의 `JAP_pacific_guardian` category를 override하지 않는다. `HOK_JAP_pacific_guardian` category와 INS/MAL/Indochina용 namespaced 결정 3개를 별도 정의하고 target `wtt_japan.1` 응답 event를 재사용한다.

### 5.4 Taiwan history

`TWN - Taiwan.txt`에 남아 있던 제거된 구형 doctrine technology 13종, 총 14개 참조를 `set_technology`에서 삭제했다. `formation_flying`은 시작/1939 블록에 각각 한 번 있었다. 시작 블록의 세 ID는 구현 전 `error.log`에 실제 `Invalid tech`로 기록돼 있었다. 1.19.2 doctrine 시스템에 1:1 technology ID 대응이 없으므로 임의 대체하지 않았다. 다른 country history의 동일한 기존 오류는 이번 기능 범위 밖이므로 건드리지 않았다.

### 5.5 Localisation과 GFX

- 영어/한국어 파일에 같은 Korean body를 두는 기존 dependency 계약을 유지했다.
- 각 파일은 focus, tooltip, event, news, idea, character, trait, decision과 2·26 선택지를 포함한 198개 고유 key를 갖는다.
- 두 파일 모두 UTF-8 BOM, 올바른 locale header와 `KEY:0` 형식을 사용한다.
- 원작/저장소/target에 이미 존재하는 focus icon, event picture, portrait, idea/decision art를 재사용했다. binary asset은 복사·변환·덮어쓰기하지 않았다.

## 6. 의도적으로 보류하거나 달라진 동작

- AI는 root를 선택할 수 없으며 원작 일본 AI strategy를 복구하지 않았다.
- 음악은 복구하지 않았다.
- 공유 본토경제 8개는 원작처럼 분리된 무연결 lane이 아니라 HoK 민주 root의 명시적 자식이다.
- Yonai와 이름 없는 산업 고문 보상은 위 사유로 보류했다.
- `JAP_duplicate_research_efforts`는 양쪽 소스 어디에도 정의가 없어 제거 보상에서 제외했다.
- NCNS faction-tier ideas가 민주 내전 뒤 UI와 decision에 남는지는 임의로 제거하지 않고 runtime 확인 대상으로 남겼다.
- 기존 save 호환을 주장하지 않는다. 최초 지원 기준은 새 게임이다.

## 7. 변경 파일

추가:

- `common/national_focus/japan.txt`
- `common/national_focus/HOK_JAP_democratic_shared.txt`
- `events/HOK_JAP_democratic_events.txt`
- `common/ideas/HOK_JAP_democratic_ideas.txt`
- `common/characters/HOK_JAP_democratic_characters.txt`
- `common/decisions/HOK_JAP_democratic_decisions.txt`
- `localisation/english/HOK_JAP_democratic_l_english.yml`
- `localisation/korean/HOK_JAP_democratic_l_korean.yml`

수정:

- `events/SEA_Japan.txt` — 2·26 사건의 HoK 전용 선택지와 기존 선택지 분리
- `common/decisions/categories/JAP_HoK_decision_category.txt` — isolated Pacific Guardian category
- `common/ai_strategy/KOR.txt` — 기존 대일 적대 strategy 종료 조건에 HoK root OR 추가
- `history/countries/TWN - Taiwan.txt` — 제거된 doctrine-tech 참조만 삭제
- `docs/HOK_JAPAN_DEMOCRATIC_BRANCH_INTEGRATION_PLAN.md` — 구현 상태 반영
- `docs/CHINA_JAPAN_VANILLA_ALIGNMENT_POLICY.md` — target 직접 상속 정책에 승인된 HoK 민주 delta 반영
- `docs/VALIDATION_CHECKLIST.md` — 구현 상태 링크 반영

`common/decisions/JAP.txt`는 최종적으로 변경하지 않는다. target category와 decision을 직접 확장하는 초기 시안은 category visibility override 위험 때문에 폐기하고 완전 격리 방식으로 바꿨다.

## 8. 정적 검증

현재 확인된 결과:

- host의 실제 focus 정의: target/구현본 각각 448개
- HoK shared focus: 40개/40 unique, 내부 focus 참조 누락 0
- HoK event: 22개/22 unique, 호출 대상 누락 0, 호출자 없는 정의 0
- 신규 localisation: 언어별 198개/198 unique, 누락·extra·중복 0
- 신규 localisation 198개와 저장소의 다른 파일·설치된 target·`Korean Language` 사이 key 충돌 0
- localisation: 양쪽 UTF-8 BOM, 헤더 정상, 헤더 제외 body byte-decoded 동일
- 신규 focus/event/idea/portrait/category의 직접 GFX 참조: 고유 70개, 누락 0
- 관련 Paradox Script의 brace, quote와 comment-aware nesting: 이상 0
- target host 동작 차이: WTT root 정의 뒤 shared hook 1개, 기존 정치 entry 6개의 reciprocal mutex/HIDE guard, NCNS 정치 하위 자체 `allow_branch` 경계 9개의 HIDE guard, HoK-HIDE용 SEA 위치 offset 1개와 D-JAP-18 inlay 위치 override 1개다. WTT root `x=12`, NCNS root `x=27`, continuous-focus `x=20`과 target inlay 좌표 10개(기본 1개 + override 9개)는 원값과 일치한다. 추가한 10번째 override만 HoK 완료/선택 flag를 검사한다.
- D-JAP-16 감사: target/project host는 각각 448개 focus ID를 보존한다. NCNS 정치 구간은 top-root closure 297개와 독립 고이소 계통 4개이며, 부모 숨김을 덮는 자체 `allow_branch` 경계 9개를 모두 보강했다.
- SEA 산업·군부의 HoK mutex/HIDE/선택 flag 변경은 모두 제거했다. 95개 focus의 기능상 차이는 없고 산업 root에 HIDE+HoK 위치 offset 1개만 남는다. HoK 선택 flag는 완료 reward의 relayout보다 먼저 설정된다.
- 현재 HoK root는 `relative_position_id` 없이 절대 `x=10`, `y=0`이다. 하위 39개의 상대참조 누락·순환은 0이며 계산된 40개 범위는 `x=6..18`, `y=0..9`다.
- 활성 NCNS focus와 HoK focus의 정확 좌표 충돌은 0이다. `HOK_JAP_develop_nanyo_gunto` `(15,8)`과 `JAP_the_lecture_group_ascendant` `(15,9)`의 한 칸 수직 인접은 실제 UI 가독성 검증 대상으로 남긴다.
- D-JAP-18 좌표는 target focus item `165x128`, spacing `96x130`, center offset `(130,32)`와 inlay `620x670`을 사용해 산정했다. `y=700` 구간의 HoK 우측 경계 약 1735px와 SEA/군부 좌측 경계 약 2914px 사이에 창 `x=2000..2620`을 두며 정적 좌우 여유는 약 265px와 294px다.
- cross-country negative path: `MAN`·`KOR`·`SOV` 소멸/소유권 guard와 야마시타 전역 character 복귀 scope 검토 완료
- 제거 대상 stale ID/namespace: 활성 잔재 0
- `descriptor.mod`: 신규 `replace_path` 0
- map 파일 변경 0
- `git diff --check`와 신규 파일 후행 공백 검사: whitespace 오류 0
- 독립 정적 감사의 잔여 `High`/`Medium` 확정 오류 0

이 결과는 텍스트 수준의 정적 검사이며 실제 게임 parser/loader/effect 실행을 대신하지 않는다.

## 9. 런타임 검증 상태와 남은 위험

상대좌표 패치 뒤 사용자가 게임을 실행해 화면을 제공했다. 2026-09-09 17:12 시작 로그는 `Operation Postern v1.19.2.0.a729 (d90f)`와 활성 Hearts of Korea 모드를 기록하고, 당시 HoK shared source line을 가리키는 기존 `recruit_character` 경고도 남겼다. 이로써 D-JAP-16 적용 전 integration source가 로드된 상태에서 우측 잔존 현상이 관찰됐다는 점은 `STRONGLY_SUPPORTED`다.

최초 D-JAP-16 적용 뒤 18:11 새 게임 실행은 체크섬 `(4163)`과 current local mod를 기록했다. 같은 `recruit_character` 경고가 패치 전 65–71행에서 패치 후 소스와 일치하는 71–77행으로 이동해 수정된 shared 파일 로드는 `CONFIRMED`이며, 새 `allow_branch`, mutex와 relayout 관련 parser 오류는 없다. 사용자는 이 실행에서 HoK root가 완료됐다고 확인했지만 대상 계통은 남았다. 로그에는 `obsolete_focus_branches_visibility` 선택값과 focus 완료 effect가 기록되지 않으므로 HIDE에서 timing 문제가 발생했다는 판정은 `UNPROVEN`이며, 이번 보강은 해당 시점 의존성을 제거하는 방어적 수정이다.

2026-09-09 19:26에는 설치된 `hoi4.exe`를 `-start_tag=JAP`, `-auto_start_game_rules=obsolete_focus_branches_visibility:HIDE`, `-start_speed=0`, `-pause`로 직접 실행했다. `game.log`는 1936.1.1.12의 새 singleplayer 진입을, `system.log`는 1.19.2 `(8d0f)`와 활성 Hearts of Korea 모드 1개를 기록했다. `error.log`의 기존 `recruit_character` 경고가 최종 shared source의 84–90행을 가리켜 timing-safe flag 보강본의 실제 로드는 `CONFIRMED`이며, 신규 `allow_branch`, flag, mutex 또는 relayout parser 오류는 없다. 이 로그는 위 `POST-D-JAP-16-FLAG-1926-STARTUP`에 보존했다.

2026-09-09 20:08의 후속 직접 실행에서는 상대좌표안을 포함한 소스가 로드됐고, `error.log`가 `HOK_JAP_strengthen_civilian_government`에 대해 `relative_focus_id: JAP_the_unthinkable_option does not exist. Relative focus must be scripted before this.`를 기록했다. 이 실행으로 top-level shared focus가 해당 ordinary focus를 직접 위치 기준으로 사용하는 D-JAP-15 상대좌표안은 `DISPROVEN`이다. production에서는 root의 `relative_position_id`를 제거하고 같은 계산 결과인 절대 `x=10`, `y=0` fallback을 적용했으며, 하위 39개 상대좌표 사슬은 유지했다. 20:08 실행은 fallback 적용 전 실패 재현이므로 fallback의 후속 startup이나 UI 성공을 증명하지 않는다.

절대좌표 fallback 적용 뒤 20:18:25 fresh process를 시작했다. `system.log` 289행은 `Operation Postern v1.19.2.0.a729 (bd08)`, DLC 36개, 활성 모드 1개와 Hearts of Korea를 기록했고, `game.log`는 20:18:50에 1936 single-player가 시작됐음을 기록했다. clean `error.log`에는 `relative_focus_id`, `Error in focus`, `allow_branch` 또는 위치 관련 오류가 0개였다. 이어 사용자가 제공한 1936-01-01 화면은 121 정치력과 `문민정부 강화` 완료 상태에서 HoK 40개와 정상 SEA 산업·군부 계통이 남고 NCNS 정치 계통은 보이지 않는 결과를 보여 준다. 따라서 절대좌표 fallback startup과 D-JAP-16/17의 정치 숨김·SEA 공통 계통 재배치는 `CONFIRMED`다. 이 판정은 inlay와 전체 가로 스크롤 계약의 통과를 뜻하지 않는다.

다만 현재 자동화 세션은 브라우저 surface만 제공하고 native Windows app 제어 service가 없어 게임 화면을 직접 조작하거나 캡처할 수 없었다. 시험한 `-auto_run` 명령 파일도 실행 결과를 남기지 않아 사용하지 않았으며, 자동 실행한 일시정지 게임은 저장 없이 종료했다. 사용자 화면으로 완료 상태는 확인했지만 실제 2·26 사건 완료 과정, `list_hidden_focuses JAP`, `SHOW`, 역방향 잠금과 save/load는 `NOT RUN`이다.

D-JAP-18 구현 시점에도 수정 전 데이터를 로드한 `hoi4.exe` PID 27032가 실행 중이었다. 미저장 상태를 해칠 수 있어 종료·reload·새 process 실행을 하지 않았고, 22:03 세션의 `system/setup/game/error/code_revisions` 로그를 `.local-artifacts/incidents/2026-09-09-d-jap-18/pre-implementation-2203-active/`에 먼저 보존했다. 그 시점에는 코드 diff와 구조 검사만 통과했고 fresh runtime은 시작하지 않았다.

이후 사용자가 실행한 23:24 fresh 세션은 HOI4 1.19.2 `(68eb)`, DLC 36개, active mod 1개인 Hearts of Korea를 기록하고 1936 single-player에 세 번 진입했다. 새 inlay/focus/layout/parser 오류는 0건이며, 수정본 startup은 `CONFIRMED`다. 유일한 신규 오류 종류는 gamestate reset 때 OneDrive의 `random.log`를 `random_1.log`로 바꾸지 못한 6건으로 D-JAP-18과 연결되지 않는다. 최종 로그 5개는 `.local-artifacts/incidents/2026-09-09-d-jap-18/post-implementation-2324-final/`에 보존했다. 로그는 실제 패널 위치와 조작을 기록하지 않으므로 UI 성공은 `UNPROVEN`이다. 정상 clean 1936 positive path는 단순 70일 완료가 아니라 56일 뒤 아이자와 mission에서 이어지는 2·26 사건 HoK option이 `complete_national_focus`를 실행하는 경로다. `Focus.AutoComplete`는 빠른 probe로만 분리한다. 아래 검증 항목을 갱신한다.

1. 절대 `(10,0)` root와 하위 상대좌표 사슬의 `SHOW`·save/load 배치 및 확대 화면에서 아이콘·제목·연결선 충돌이 없는지
2. root 진행 중과 실제 2·26 사건 완료 과정, 완료 후 `SHOW`와 save/load에서 위치가 유지되는지
3. 2·26 사건이 진행 중 root를 정상 완료하고 다른 option이 동시에 보이지 않는지
4. 민주 내전의 수도, state, 육·해군 분할, militia 10개와 인물 소속
5. NCNS faction-tier ideas가 내전 뒤 어떤 상태로 남는지
6. Showa/공화정 지도자 전환, cosmetic tag와 후속 focus 진행
7. KOR 동맹·자유무역의 수락/거절/faction leader 분기
8. TWN 생성, state 524 이전, puppet autonomy와 history 적용
9. MAN/MEN/CHI/SOV/TWN가 없거나 소유권이 예상과 다른 late-game edge case
10. Pacific Guardian 결정 category와 `wtt_japan.1` 상호작용
11. state 555 보상과 Shinkansen 철도 효과의 실제 결과
12. HoK 미선택 historical JAP AI, 중일전쟁과 기존 KOR bridge 회귀
13. save/load, 기존 save, multiplayer checksum과 동기화
14. 원작 보존 동작인 event `.7`의 state 745와 `.9`의 state 609 이전이 비정상 대체역사에서 현재 소유자를 재검사하지 않는 경로
15. 소련이 거절한 뒤 event `.20`이 1일 후 실행되기 전에 `SOV`가 완전히 소멸하는 극단적 경로
16. D-JAP-16 교정 뒤 save/load한 `HIDE` 게임에서도 NCNS 정치 301개 구간이 자체 `allow_branch` 경계를 통해 재등장하지 않는지
17. `SHOW`에서는 경쟁 정치 계통이 보이더라도 HoK와 동시에 진입할 수 없는지, 경쟁 정치 root를 먼저 완료하면 HoK가 잠기는지
18. SEA 산업 34개·군부 61개의 실제 진행·효과가 유지되고 save/load 뒤에도 정적 범위 `x=20..37`, `x=39..65` 배치를 유지하는지
19. D-JAP-18: 수정 전 `HIDE`의 HoK 완료 후 imperial-influence inlay 화면 부재와 HoK용 위치 override 누락은 `CONFIRMED`, 기본 `X=10000`의 스크롤 범위 이탈은 `STRONGLY_SUPPORTED`다. HoK 전용 `x=2000`, `y=700` override는 구현·정적 검증했고 23:24 fresh startup도 통과했다. 완료 직후 실제 UI·재진입·save/load·`SHOW`는 `UNPROVEN / NOT RUN`이다. 상세 근거는 [별도 진단·구현 기록](2026-09-09-japan-imperial-influence-inlay-offscreen.md)에 둔다.
20. 경제·군부 shortcut이 빈 공간이나 유령 이동을 만들지 않는지

따라서 D-JAP-15 상대좌표안과 최초 D-JAP-16의 대상 분류는 각각 엔진 로그와 사용자 런타임 화면으로 반증됐다. root 절대 `(10,0)` fallback, SEA rollback, 정치 하위 경계 9개 보강, SEA 위치 offset 1개와 D-JAP-18 inlay 위치 override 1개를 적용했다. fallback startup, D-JAP-16/17 정치·SEA `HIDE` 동작과 D-JAP-18 수정본의 fresh startup은 확인했지만, D-JAP-18 실제 UI와 2·26 사건 완료 과정, `SHOW`, 역방향 잠금과 save/load가 남아 있으므로 전체 runtime 완료 또는 release-ready로 판정하지 않는다.

## 10. 구현 당시 Git와 외부 작업

- commit: 수행하지 않음
- push/tag: 수행하지 않음
- Workshop upload/update: 수행하지 않음
- launcher/playset/save/settings 변경: 수행하지 않음
- 설치된 1.19.2 게임 파일 변경: 수행하지 않음
- 원작 Workshop 파일 변경: 수행하지 않음

### 10.1 2026-09-09 후속 Git 상태

구현 뒤 사용자의 명시적 요청으로 관련 변경을 분리해 다음 commit을 `origin/main`에 push했다.

- `b51df1e` — `feat(japan): restore HoK democratic focus branch for 1.19.2`
- `f674c0b` — `fix(taiwan): remove obsolete doctrine technology references`
- `8c300d8` — `docs(japan): record democratic branch integration and validation`
- `494bc15` — `docs(repo): require contributor notes for production changes`

D-JAP-18 문서화 시작 기준은 `main` / `494bc15` clean이었다. 후속 구현 요청에서는 기존 문서 변경을 보존한 채 `common/national_focus/japan.txt`에 HoK 전용 위치 override 1개를 추가했다. production 변경은 후속 Git 승인에 따라 `9a80c6f` (`fix(japan): keep imperial influence panel on HoK path`)로 별도 commit했으며, 이 문서 묶음은 별도 commit 대상으로 유지한다.
