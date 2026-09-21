# 한국 중점 확장용 바닐라 원본 목록

작성일: 2026-09-21 · 상태: **설계 제안 / 문서화만 승인 / 구현 미승인**

이 문서는 [한국 중점 확장 계획](HOK_KOREAN_FOCUS_EXPANSION_PLAN.md)의 원본 선택과 이식 범위 판단을 돕는다.
새 중점의 확정 명세, 승인된 ID 목록, 확정 개수·보상 수치, 호환성 판정은 아니다.
기존 한국 중점을 삭제하지 않고, 기존 기관·노선의 후속 선택을 늘리는 후보를 기록한다.
기존 70일 중점을 35일로 바꾸는 방향도 현재 코드 변경으로 실행하지 않았다.

## 조사 범위와 경로

- 요청 비교 버전은 **HOI4 1.19.2**이나, 이번 조사 환경에서 확인된 설치본은 **1.19.3**이다.
- 아래 바닐라 행 번호는 이번에 읽은 설치본 기준이다. 정확한 1.19.2 대조 결과로 소개하지 않는다.
- 구현 전에 최종 대상 버전·빌드·체크섬을 정하고, 그 버전의 불변 원본 스냅샷에서 다시 대조해야 한다.
- `V` = `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV`.
- `H` = 저장소 루트. 한국 중점은 [common/national_focus/korea.txt](../common/national_focus/korea.txt)에 있다.
- `V`와 Workshop 원본은 읽기 전용 자료다. 이 문서 작업은 외부 원본 변경이나 게임 코드 구현을 허가하지 않는다.
- `CONFIRMED`는 인용한 소스의 정의·연결을 확인했다는 뜻이다. 한국에 이식한 실제 동작은 모두 `UNPROVEN`이다.
- 이번 조사에서는 게임 실행, 테스트·검증 스크립트, Git 변경 작업을 수행하지 않았다.

## 원본을 고르는 기준

HoK에는 세계 학자 초빙, ADD, 포항제철, KAI, 특수부대, 대함대·통상파괴, 전술·전략공군이 이미 있다.
같은 기관을 새 이름으로 다시 설립하기보다 그 기관의 운용·투자·교리·외교 선택을 늘린다.
원본의 조건, 취소, 비용, 효과 회수까지 묶어서 검토하고, 한국 이름만 바꾼 중점 블록을 완성본으로 보지 않는다.
아래 한국어 이름은 콘셉트 예시이며 새 localisation key나 중점 ID로 확정한 것이 아니다.

| 후보 | 재사용할 구조 | 난도 | 우선 연결할 기존 한국 계통 |
|---|---|---|---|
| 스웨덴 지역 개발 | 중점 해금 후 비용을 지불하는 지역 사업 | 중간 | 신도시·자원 개발 |
| 스웨덴 군수 규격화 | 연구·조달·국민정신 교체 | 중간 | 소총·포병·지원병과 |
| 핀란드 지형전 | 동계전 및 지역별 준비 결정 | 높음 | 육군 교리·특수부대 |
| 스웨덴 연안 해군 | 수리·군도전·해안 지원의 전문화 | 낮음~중간 | 해군 장기계획·제주 기지 |
| 스웨덴 항공 설계 | 국내 설계와 해외 기술 협력 선택 | 중간 | 기존 KAI |
| 독일·핀란드 생산 | 생산 규모와 공정·설계 효율 | 중간~높음 | 중공업·산업단지 |
| 일본 산업·전력 | 산업 국민정신의 단계적 발전 | 중간~높음 | 댐·ADD·신도시 |
| 일본 동맹 경제 | 동맹국의 가입·거부·이탈 처리 | 높음 | 기존 아시아 연합·OFN |

## 1. 스웨덴: 지역 개발 결정

**원본:** `V/common/national_focus/sweden.txt`의 `SWE_urbanization`(139행), `SWE_deep_mining_complexes`(1547행).

- 한국 콘셉트: 도시 기반시설 정비 → 지역개발기금 → 함경·강원 심부광산 개발.
- 기존 연결점: [한국 중점](../common/national_focus/korea.txt)의 `KOR_first_new_city_plan`(627행), `KOR_hamgyeong_underground_resources`(462행), `KOR_gangwon_underground_resources`(491행).
- 도시·자원 개발 중점을 삭제하거나 새 포항제철 중점으로 대체하지 않고 후속 사업을 붙인다.
- `CONFIRMED`: `V/common/decisions/SWE.txt:349`의 `SWE_urbanization_decision`은 특정 주의 도시화를 실행한다.
- 원본은 정치력 120, 80일, 주거 동적수정치 보유 및 시행 완료 플래그를 사용한다. 이 수치는 한국안 확정값이 아니다.
- `CONFIRMED`: `V/common/decisions/resource_prospecting.txt:8657`의 `deeper_swedish_mines`는 기술·소유·통제·민공 조건을 확인한다.
- 원본 광산 사업은 정치력 50, 민공 5개, 60일을 소비한다. 무제한 즉시 자원 지급과 다른 투자 구조다.
- 함께 추적할 것: 결정 카테고리, 주거 동적수정치, 기술 조건, 주 플래그, 완료·취소 동작, AI 선택, localisation.
- 원본 주 `138/140/141/666`은 한국 주가 아니다. 한국의 현재 지도·자원 결정과 겹침을 먼저 대조한다.
- 난도는 **중간**. 목표는 중점에서 권한을 얻고 실제 사업은 비용을 치르는 선택을 늘리는 것이다.

## 2. 스웨덴: 군수 계약과 장비 규격화

**원본:** `V/common/national_focus/sweden.txt`의 `SWE_government_weapons_contract`(390행), `SWE_standardize_equipment`(434행).

- 한국 콘셉트: 국방조달계약 → 탄약 규격 통일 → 육군 병기 표준화.
- 기존 연결점: [한국 중점](../common/national_focus/korea.txt)의 `KOR_new_model_rifle`(1877행), `KOR_improved_artillery`(1899행), `KOR_expansion_of_non_combat_support_units`(1921행).
- `CONFIRMED`: 무기계약은 소화기 연구 보너스와 MIO 자금을 지급한다.
- `CONFIRMED`: 규격화 중점은 군수공장 조건을 확인하고 `SWE_severe_lack_of_ammunition`을 `SWE_standardized_equipment`로 교체한다.
- 실제 교체 아이디어는 `V/common/ideas/sweden.txt:666`에 있으며 스웨덴 태그 조건과 생산효율 상한 보너스가 있다.
- 한국에는 기존 국민정신·MIO가 있으므로 스웨덴의 시작 불이익과 업체를 그대로 끼워 넣지 않는다.
- [한국 중점](../common/national_focus/korea.txt) 1944행 부근은 이미 `KOR_mmaa_organization`과 AAT 분기를 사용한다.
- 함께 추적할 것: 교체 전후 아이디어, 한국의 기존 생산 보너스, MIO 허용 조건, 연구 범주, 툴팁, DLC 없는 경우.
- 규격화의 효과를 새 영구 공장·전투 보너스와 동시에 크게 중첩할지는 별도 밸런스 결정이다.
- 난도는 **중간**. 기존 소총·포병 중점의 성과를 조달·생산 체계로 이어 주는 용도다.

## 3. 핀란드: 동계전과 지역별 방어 준비

**원본:** `V/common/national_focus/finland.txt`의 `FIN_winter_warfare`(11413행), `FIN_motti_tactics`(11446행).

- 한국 콘셉트: 개마고원 동계훈련 → 산악 분산전술 → 요충지 매복 준비.
- 기존 연결점: [한국 중점](../common/national_focus/korea.txt)의 `KOR_research_army_doctrine`(1957행), `KOR_organization_rokasf`(1641행).
- 특수부대 창설을 반복하지 않고 지형에 맞는 후속 운용 선택을 추가하는 안이다.
- `CONFIRMED`: 동계전 중점은 핀란드 육군 변수와 겨울 군수지원 기술을 사용한다.
- `CONFIRMED`: 모티 전술은 `V/common/decisions/FIN.txt:213`의 지역 준비 결정을 해금한다.
- 결정은 정치력·지휘력, 준비 기간, 사용에 따른 비용 증가, 취소, 적국 알림 이벤트를 처리한다.
- 카테고리는 `V/common/decisions/categories/FIN_decision_categories.txt:16`, 유효 지역 판정은 `V/common/scripted_triggers/FIN_scripted_triggers.txt:41`에 있다.
- 지역 효과는 `V/common/dynamic_modifiers/aat_dynamic_modifiers.txt:1164`의 `FIN_motti_tactics_modifier`다.
- `V/common/on_actions/09_aat_on_actions.txt:1707`은 지역을 잃을 때 수정치를 제거하고 비용을 되돌리는 흐름을 포함한다.
- 군대 변수는 같은 동적수정치 파일 1041행의 `FIN_finnish_army`와 연결된다.
- 함께 추적할 것: 초기 변수·핵심주 배열, 결정 비용, 이벤트, 점령 변화, 저장·불러오기, AI, DLC 기술 지원.
- 난도는 **높음**. 중점 블록만 복사하면 준비 효과·비용·회수 중 일부가 빠질 수 있다.

## 4. 스웨덴: 연안 해군과 수리 체계

**원본:** `V/common/national_focus/sweden.txt`의 `SWE_refit_gotaverken_for_rapid_repairs`(1962행), `SWE_coastal_support`(2191행), `SWE_archapeligo_harrasment`(2387행).

- 한국 콘셉트: 진해 수리창 정비 → 다도해 기동훈련 → 함포지원 연락체계.
- 기존 연결점: [한국 중점](../common/national_focus/korea.txt)의 `KOR_vision_1950`(2578행), `KOR_jeju_naval_base`(2598행).
- 기존 대함대·잠수함·해병대 중점을 유지하면서 반도와 연안에 맞는 전문화를 추가한다.
- `CONFIRMED`: 수리 아이디어는 `V/common/ideas/sweden.txt:587`에서 함선 수리 속도를 변경한다.
- `CONFIRMED`: 해안지원 아이디어는 같은 파일 556행에서 해안포격과 상륙 페널티를 변경한다.
- 군도전 중점은 해군 지휘관 특성, 교리 비용, 연막발생기 기술 또는 경험치를 다룬다.
- 연막 기술의 `Man the Guns` 조건과 대체 보상은 보존해서 검토한다.
- 함께 추적할 것: 아이디어의 SWE 조건, 주 통제 조건, 해군 지휘관, 특성, 기술, 툴팁.
- 원본의 주 번호와 지휘관 선발 조건이 한국에서도 의미가 있는지 대조해야 한다.
- 난도는 **낮음~중간**. 단순 수리 아이디어보다 지휘관·DLC 기술까지 포함한 군도전이 더 복잡하다.

## 5. 스웨덴: 국내 항공 설계와 해외 기술 협력

**원본:** `V/common/national_focus/sweden.txt`의 `SWE_domestic_designs`(3046행), `SWE_foreign_designs`(3104행), `SWE_formation_flying`(3160행).

- 한국 콘셉트: 국산 항공설계국 ↔ 우방 항공기술 도입 → 편대전술 표준화.
- 기존 연결점: [한국 중점](../common/national_focus/korea.txt)의 `KOR_korea_aerospace_industry`(2942행).
- 기존 전술공군·전략공군 선택(3001·3040행)은 보존한다. 설계 확보 방식은 그 옆에서 별도로 선택하는 안이다.
- `CONFIRMED`: 국내·해외 설계는 원본에서 상호배타다.
- 국내 설계는 BBA 보유 시 항공 모듈 연구, 없으면 전투기 연구로 보상을 나누고 Saab MIO 자금을 지급한다.
- 해외 설계는 같은 정부의 비교전 강대국을 조건으로 연구 보너스를 준다. 실제 라이선스 계약 생성 효과는 아니다.
- Saab 정의는 `V/common/military_industrial_organization/organizations/SWE_organization.txt:161`에 있고 SWE/BRA 조건을 갖는다.
- 한국은 기존 `KOR_kai_company_organization`에 연결할 후보가 있다. Saab을 한국 업체로 이름만 바꾸어 등록하지 않는다.
- 함께 추적할 것: MIO와 DLC 조건, BBA 대체 보상, 외교 관계·이념 조건, 기술 범주, 중복 연구 보너스.
- 난도는 **중간**. KAI를 다시 설립하기보다 설계 전략과 조종사 운용을 확장한다.

## 6. 독일·핀란드: 생산 규모와 생산 공정

**원본:** `V/common/national_focus/germany.txt`의 `GER_concentrated_armament_program`(2432행), `GER_establish_production_targets`(2467행).
**선택 구조의 대안:** `V/common/national_focus/finland.txt`의 `FIN_expand_production_lines`(13671행), `FIN_modernize_production_lines`(13767행).

- 한국 콘셉트: 군수시설 증설 / 생산공정 합리화 / 전시 생산조정위원회.
- 기존 연결점: [한국 중점](../common/national_focus/korea.txt)의 `KOR_development_of_heavy_industry`(688행), `KOR_guro_industrial_complex`(708행), `KOR_industrialized_society`(825행).
- `CONFIRMED`: 독일의 두 중점은 원본에서 상호배타가 아니다. 핀란드의 두 중점은 상호배타다.
- 핀란드 현대화는 기존 CAS·전투기·뇌격기 생산 아이디어의 개선형과 연결된다.
- 관련 예시는 `V/common/ideas/finland.txt:1422`와 1448행의 CAS 생산 아이디어다.
- 독일 `GER_modify_industrial_modifier`는 `V/common/scripted_effects/GER_scripted_effects.txt:927`에서 기존 경제 상태별 툴팁을 선택한다.
- 실제 생산효율 변화는 `GER_industrial_*` 변수와 `V/common/dynamic_modifiers/wuw_dynamic_modifiers.txt:462`, 531행 등의 연결에서 나온다.
- 따라서 중점 보상 블록만 복사하면 한국에 연결되지 않은 변수만 바꾸는 결과가 될 수 있다. 효과 호출 자체는 생산효율을 부여하지 않는다.
- 함께 추적할 것: 경제 동적수정치의 부여·교체·초기화, 공장 부지 조건, 숨은 생산 아이디어, 기술 조건.
- 난도는 **중간~높음**. 독일 경제 전체를 들여올지, 한국 국민정신으로 좁혀 대응시킬지는 설계 결정이다.

## 7. 일본: 전력·연구·공업도시의 연계

**원본:** `V/common/national_focus/japan.txt`의 `JAP_fund_the_riken_institute`(25774행), `JAP_build_the_nishotaki_and_miyanaka_dams`(25878행), `JAP_establish_synthetic_fuel_joint_venture`(25937행), `JAP_establish_nippon_hassoden`(26133행), `JAP_new_industrial_city_development_policy`(26175행).

- 한국 콘셉트: 전국 송전망 연계 → 산업 전력 조정 → 연구성과의 공업화 → 공업도시 정비.
- 기존 연결점: [한국 중점](../common/national_focus/korea.txt)의 `KOR_build_soyanggang_dam`(380행), `KOR_create_add`(879행), `KOR_first_new_city_plan`(627행).
- 기존 댐·ADD·신도시 중점의 후속으로 설계한다. 이미 있는 합성연료·고무 계통과도 겹침을 확인한다.
- `CONFIRMED`: 일본발송전 중점은 원본에서 전쟁 중이라는 조건을 요구한다.
- 보상은 `JAP_add_or_modify_early_industrialization`과 산업 에너지 소비·석탄 자원 변수에 연결된다.
- 효과 정의는 `V/common/scripted_effects/JAP_scripted_effects.txt:243`에 있으며 산업 동적수정치의 부여·툴팁을 처리한다.
- 변수의 실제 연결은 `V/common/dynamic_modifiers/SEA_dynamic_modifiers.txt:401`, 428행 등에서 확인된다.
- 새 공업도시 정책에는 핵심주·소유·도시 등급 조건과 bypass가 있다. 한국 도시 등급을 먼저 대조해야 한다.
- 함께 추적할 것: 경제 국민정신 생명주기, 변수 초기화, 전시 조건, 도시 등급, 합성연료·석탄의 기존 보상.
- 난도는 **중간~높음**. 원본의 단계적 산업 발전 구조를 활용하되 독립 기관을 중복 신설하지 않는다.

## 8. 일본: 동맹의 관세·통화 협력

**원본:** `V/common/national_focus/japan.txt`의 `JAP_create_greater_east_asian_treaty_organization`(23784행), `JAP_form_greater_east_asian_customs_union`(23828행), `JAP_form_greater_east_asian_currency_union`(23897행).

- 한국 콘셉트: 아시아 공동통상위원회 → 관세 협정 → 결제 협력 → 공동 조달.
- 기존 연결점: [한국 중점](../common/national_focus/korea.txt)의 `KOR_founding_of_the_asian_union`(6490행), `KOR_invitation_to_independent_asian_countries`(6531행), 별도 노선인 `KOR_establish_ofn`(5696행).
- 기존 세력 창설을 삭제·대체하지 않고 각 노선에서 회원국 협력을 발전시키는 후보로 취급한다.
- `CONFIRMED`: 관세동맹은 동맹국에 `SEA_japan_foreign_policy.97` 이벤트를 보내며 단순 일괄 보상만은 아니다.
- 이벤트는 `V/events/SEA_Japan.txt:7226`, 무역 아이디어는 `V/common/ideas/japan.txt:3567`에 있다.
- 아이디어에는 일본과 전쟁 시 취소, 역외 민공 부여·회수, 플래그, 일본 대상 무역·관계 효과가 연결된다.
- 통화동맹 중점에도 `is_ally_with = JAP`라는 일본 고정 참조가 있다. 표면의 중점 태그만 바꾸면 일본 동맹에 효과를 줄 수 있다.
- 세력 틀은 `V/common/factions/templates/japanese_factions.txt:199`이며 선언·목표·가입·평화·지도국 변경 규칙을 포함한다.
- 함께 추적할 것: 이벤트 수락·거부, 가입 후·이탈 후 국가, 전쟁·괴뢰·세력지도국 조건, 민공 회수, 세력 목표와 DLC.
- 난도는 **높음**. 실제 신규 회원 처리까지 이어지는 이벤트·결정 전체 연결은 구현 전에 추가 추적해야 한다.

## 구현 전에 사용할 대조 목록

1. 최종 대상 버전의 파일 스냅샷, 빌드·체크섬, DLC, 언어 의존 모드, 로드 순서를 고정한다.
2. 이 문서의 설치본 행 번호를 그 스냅샷의 실제 정의로 다시 찾고 차이를 기록한다.
3. 기존 한국 중점·아이디어·결정·MIO·지도를 대조하여 중복 기관과 중첩 보상을 표시한다.
4. 원본 중점에서 이벤트·결정·효과·트리거·변수·동적수정치·on_action까지 참조를 따라간다.
5. 국가·주·프로빈스·장군·장비·MIO·세력·이벤트 대상의 한국 대응표를 만든다.
6. 트리 밖에서 보장하던 DLC 조건까지 확인한다. 스웨덴 트리 선택은 `sweden.txt:10`에서 AAT를 요구한다.
7. 기존 DLC 분기와 대체 보상을 보존하고, 사용할 수 없는 시스템을 무조건 허용하는 방식으로 조건을 제거하지 않는다.
8. 기존 ID는 유지한다. 신규 ID는 HoK 접두사와 전역 중복 확인 후 별도 구현 명세에서 정한다.
9. 한국어 이름·설명·툴팁은 원래 HoK 세계관과 연결하고, 원작·바닐라 기반 및 후속 기여를 구분한다.
10. 35일 단축에 따른 조기 획득 효과와 신규 보상 누적을 별개로 계산한다. 원본 수치는 자동 채택하지 않는다.
11. 결정의 완료·취소·점령 변화·탈퇴·전쟁·저장 후 복원까지 검증 시나리오에 포함한다.
12. 구현이 별도로 지시되면 작은 계통부터 패치하고 실제 게임에서 등록·평가·효과를 각각 확인한다.

현재 확보한 것은 원본 선정 근거와 주요 의존성이다. 모든 전이 참조의 감사나 한국 이식의 동작 검증을 끝낸 상태는 아니다.
새 중점 수, 최종 연결선, 비용, 보상 수치, AI 경로는 [확장 계획](HOK_KOREAN_FOCUS_EXPANSION_PLAN.md)에 따라 후속 명세에서 정한다.
