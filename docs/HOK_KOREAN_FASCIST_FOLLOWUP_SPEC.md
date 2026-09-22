# 파시즘 후속 점령행정·삼군 조정·재건예산 명세

작성: 2026-09-23. 시작 기준은 `feat/korean-focus-expansion-ai`의 `e511f31`, 한국 중점 366개다. 공산 확장 28개와 파시즘 F1·F2·F3 12개를 보존하면서 F4·F5·F6 후보 12개를 구체화한다. 적용 후 총 378개이며 기존 366개의 보상·조건·좌표·ID·AI 가중치는 변경하지 않는다. 후보 초안의 직렬 연결과 임시 보상은 아래 명세로 대체한다.

## 범위와 진입 조건

세 신규 정책 묶음은 서로의 완료를 요구하지 않는다. F4·F5는 진입 1개 → 함께 완료할 수 있는 병렬 2개 → 두 정책을 모두 요구하는 합류 1개다. F6는 진입 → **실제 예산 우선순위의 상호배타 선택** → 선택한 정책을 강화하는 OR 합류다. F6의 배타는 모양을 위한 분기가 아니라 일일 정치력과 민간공장 건설 사이의 정책 선택이다. F4는 기존 F2 참모업무 규정을 군정 행정의 기반으로 사용하므로 F2 완료를 요구하는 의도적인 예외다. F5·F6에는 F1·F2·F3·F4 완료를 요구하지 않는다.

모든 신규 중점은 `cost = 5`(35일), 파시즘 정부, 내전 없음, `KOR_establishment_of_the_national_salvation_army` 완료를 요구한다. `cancel_if_invalid = yes`, `continue_if_invalid = no`, `available_if_capitulated = no`를 적용한다. 일반 `ai_will_do`는 기존 F1·F2·F3와 같은 `factor = 2`이며 민주 역사 AI 목록에는 추가하지 않는다. 실제 AI의 선택 순서나 완료 시점은 가중치 정의만으로 검증되지 않는다.

| 묶음 | 실제 선행 중점 | 추가 조건 | 조건 상실과 이미 받은 보상 |
|---|---|---|---|
| F4 점령행정 | `HOK_KOR_nrsc_staff_regulations` | `KOR_korea_reigns_above_the_world` 완료, 우리 핵심이 아니며 전역을 완전히 통제하는 주가 최소 1개 존재 | 마지막 적격 주를 잃으면 진행 중 중점 취소. 기존 제도는 보존하며 적용할 점령지가 없으면 지역 점령 효과의 대상도 없음 |
| F5 삼군 조정 | `KOR_empowering_the_nrsc` | `KOR_prussia_in_the_far_east` 완료 | 다른 신규 정책 묶음의 순서와 무관. 기존 참모업무·병역정책을 요구하거나 교체하지 않음 |
| F6 재건예산 | `KOR_empowering_the_nrsc` | `KOR_korea_reigns_above_the_world` 완료, 전쟁 없음, 경기(525) 소유 및 완전 통제 | 전쟁 재개 또는 경기 소유·완전 통제 상실 시 진행 중 중점 취소. 이미 수립한 예산 제도는 보존 |

F4의 영토 조건은 `any_controlled_state = { NOT = { is_core_of = ROOT } is_fully_controlled_by = ROOT }`다. 주 소유권·핵심·순응도 수치를 직접 바꾸지 않으며 현재 정치 경로만으로 점령행정을 조기 개방하지 않는다. 핵심 지역만 통제하면 진입할 수 없고, 특정 정복·동맹 선택의 후속 중점을 요구하지 않으므로 기존 두 외교 노선 모두에서 참모업무 규정을 완성하고 실제 비핵심 영토를 확보한 뒤 접근할 수 있다. F2의 보고·작전 업무 규정을 군과 민간 행정의 책임 구분으로 확장한다는 연결을 명세에 고정한다. F2+F4는 총 8개·280일, 최장 필수 연결 6개이며 기존 정치 선행의 기간은 별도다. 모든 후속 묶음을 여기에 연달아 붙이지 않는다.

F5·F6의 화면 연결선과 배치 기준은 `KOR_empowering_the_nrsc`를 사용한다. 이 연결선만으로 즉시 착수할 수 있다는 뜻은 아니다. 각 묶음의 모든 중점에 F5는 선군주의, F6는 세계위에 군림하는 대한 완료를 `available` 조건으로 명시하며 공통 을해군란 완료 조건도 유지한다. 기존 선군주의·세계위에 군림하는 대한의 선행 구조를 변경하거나 우회하지 않는다.

F6의 추가 조건은 `has_war = no owns_state = 525 has_full_control_of_state = 525`다. 경기의 주 이름·서울 승점·한국 핵심은 프로젝트의 `history/states/525-South Korea.txt`와 `localisation/*/replace/HoK_state_name_*.yml`에서 확인했다. 을해군란은 `events/Korea.txt`의 `kor_events.3`에서 내전을 일으키고, 기존 세계위에 군림하는 대한은 그 이후 군부 정치 정비를 요구한다. 따라서 이 묶음은 **군부 내전 이후의 평시 재건**이며 별도 대외전쟁 승리나 만주 합병을 증명하는 조건은 아니다. 강제 완료로 선행 정치 중점을 만든 시험 상태도 실제 내전 승리 증거로 취급하지 않는다. 특정 건물이 손상된 상태를 계속 요구하여 자동 수리 때문에 중점이 취소되는 조건은 추가하지 않는다.

## F4 — 점령행정 4개

아래 ID에는 모두 `HOK_KOR_` 접두사가 붙는다. 병렬 두 중점의 완료 순서는 자유이며 마지막 행에는 별도의 `prerequisite` 두 블록을 사용한다.

| ID / 이름 | 선행 | 보상 |
|---|---|---|
| `nrsc_military_administration` / 군정 실무편람 | 참모업무 규정; 세계위에 군림하는 대한 완료·영토 조건 | 정치력 150 |
| `nrsc_civil_supply_offices` / 민생물자 관리소 | 군정 실무편람 | 점령행정 체계 I: 저항 목표 −10%, 필요 주둔군 −15% |
| `nrsc_claims_accounts` / 민원·보상 기록부 | 군정 실무편람 | 정치력 100, 안정도 +5%p |
| `nrsc_civil_administration_rules` / 군정 행정규정 | 민생물자 관리소 **AND** 민원·보상 기록부 | 체계 I→II. 기존 두 효과를 유지하며 순응도 증가 속도 +10%, 주둔군이 받는 저항 피해 −15% 추가 |

전체 140일이며 구조상 최장 선행 연결은 3개지만 최종 중점까지 병렬 두 개를 모두 진행해야 한다. 선행 정치·영토 조건을 만족한 뒤 정치력 150은 35일, 체계 I 또는 기록부 보상은 빠르면 70일에 받는다. 누적 일회 보상은 정치력 250·안정도 5%p이며 최종 국민정신은 II 하나다. 순응도 증가 속도는 비율 보정이며 매일 순응도 0.1을 직접 더하는 효과가 아니다.

## F5 — 삼군 조정 4개

| ID / 이름 | 선행 | 보상 |
|---|---|---|
| `nrsc_interservice_liaison` / 삼군 연락사무국 | `KOR_empowering_the_nrsc`; 선군주의 완료 조건 | 육군·해군·공군 경험치 각 25 |
| `nrsc_joint_logistics_board` / 삼군 군수조정회의 | 삼군 연락사무국 | 삼군 군수조정 I: 육군 보급 소모 −10%, 해군 연료 소비 −10%, 공군 연료 소비 −10% |
| `nrsc_joint_dispatch_records` / 통합 청구·수송 명부 | 삼군 연락사무국 | 전자공학 연구 혜택 100% × 1회, 해군·공군 경험치 각 25 |
| `nrsc_service_supply_rules` / 삼군 군수업무 규정 | 삼군 군수조정회의 **AND** 통합 청구·수송 명부 | 군수조정 I→II. 세 종류의 소모 감소를 모두 −15%로 강화 |

전체 140일, 최장 선행 연결 3개다. 경험치 각 25는 진입 조건 만족 후 35일, 군수조정 I 또는 연구·추가 경험치는 빠르면 70일에 받는다. 누적 일회 보상은 육군 경험치 25·해군 50·공군 50과 전자공학 100% 연구 혜택 1회다. II는 I와 중복 적용하지 않으며 보급 소모·연료 소비의 각 최종 보정은 −15%다. 기존 공통 병참 정신과는 별도 정책이므로 함께 적용될 수 있고, 기존 F2의 계획 속도·최대 계획 보상은 그대로 유지한다.

## F6 — 재건예산 4개 정의, 한 경로 3개 선택

| ID / 이름 | 선행 | 보상 |
|---|---|---|
| `nrsc_reconstruction_secretariat` / 재건행정 사무국 | `KOR_empowering_the_nrsc`; 세계위에 군림하는 대한 완료·평시·경기 조건 | 정치력 150 |
| `nrsc_public_accounts` / 행정예산 우선배정 | 재건행정 사무국; 건설예산과 상호배타 | 재건 행정예산 I: 매일 정치력 +0.5, 건물 수리에 투입되는 민간공장 수리 속도 +15% |
| `nrsc_construction_practice` / 건설예산 우선배정 | 재건행정 사무국; 행정예산과 상호배타 | 재건 건설예산 I: 민간공장 건설 속도 +15%, 건물 수리에 투입되는 민간공장 수리 속도 +15% |
| `nrsc_reconstruction_budget` / 재건예산 정례화 | 행정예산 **OR** 건설예산 우선배정 | 선택한 정책만 I→II. 행정 II는 일일 정치력 +1.2·수리 +15%, 건설 II는 민공 건설 +20%·수리 +25% |

총 4개 정의 중 정상 플레이에서 3개를 선택하므로 전체 105일이며 최장 선행 연결도 3개다. 정치력 150은 35일, 선택한 I는 70일, II는 105일에 받는다. 마지막 OR 선행은 하나의 `prerequisite` 블록에 두 중점 ID를 넣는다. 마지막 보상은 완료한 배타 정책을 확인하여 해당 국민정신만 교체한다. 다른 예산 계열을 부여하지 않으며 선택하지 않은 정책의 수치를 누적 합산하지 않는다.

`political_power_gain`은 고정 일일 정치력이며 +0.5%·+1.2%가 아니다. `industry_repair_factor`는 건물 수리에 투입되는 민간공장 출력 보정이다. 자동 무료 수리(`industry_free_repair_factor`)나 함선 수리(`repair_speed_factor`)의 보상이 아니다. 이 범위에서 새 결정·반복 사업·예산 자원 체계는 추가하지 않는다.

## 국민정신 8개와 교체

모든 ID에는 `HOK_KOR_nrsc_` 접두사가 붙는다. 공통 `allowed = { original_tag = KOR }`, `allowed_civil_war = { always = yes }`, `removal_cost = -1`, `cancel = { NOT = { has_government = fascism } }`를 사용한다.

| ID | 수정치 |
|---|---|
| `occupation_administration_1` | `resistance_target = -0.10`, `required_garrison_factor = -0.15` |
| `occupation_administration_2` | I의 두 수정치 유지, `compliance_growth = 0.10`, `resistance_damage_to_garrison = -0.15` 추가 |
| `service_coordination_1` | `supply_consumption_factor = -0.10`, `navy_fuel_consumption_factor = -0.10`, `air_fuel_consumption_factor = -0.10` |
| `service_coordination_2` | 위 세 수정치를 각각 `-0.15`로 강화 |
| `administrative_budget_1` | `political_power_gain = 0.50`, `industry_repair_factor = 0.15` |
| `administrative_budget_2` | `political_power_gain = 1.20`, `industry_repair_factor = 0.15` |
| `construction_budget_1` | `production_speed_industrial_complex_factor = 0.15`, `industry_repair_factor = 0.15` |
| `construction_budget_2` | `production_speed_industrial_complex_factor = 0.20`, `industry_repair_factor = 0.25` |

하위 정신이 있으면 `swap_ideas`로 교체하고, 이미 제거된 상태라면 해당 상위 정신만 직접 부여한다. 파시즘을 잃으면 이 8개 정책은 제거되며 정권 복귀만으로 자동 복구되지 않는다. 영토 상실·전쟁 재개는 중점 진행 조건과 이미 수립한 제도의 수명을 구분하므로 국민정신 취소 사유로 추가하지 않는다. 이미 지급된 정치력·안정도·경험치·연구 혜택도 조건 상실 시 회수하지 않는다. 기존 점령법·징병법·F1·F2·F3·공통 산업·군사 정신은 변경하거나 제거하지 않는다.

## 배치와 이미지

세 묶음은 각각 3개의 점유 행으로 배치하고, 상대 위치 기준·화면 연결선·실제 착수 조건을 구분한다. F5는 기존 다른 분야와 HIDE 상태의 충돌을 피하려고 첫 행과 중간 행 사이에 한 행을 비운다. 신규 중점은 파시즘 루트의 HIDE 이동 −84x를 기존 상대 배치 체인으로 한 번 상속하며 별도 offset을 추가하지 않는다. SHOW 및 정치 선택 전에는 기본 위치를 유지한다. 정적 좌표와 연결선 검토는 실제 UI 검증을 대신하지 않는다.

| ID (`HOK_KOR_nrsc_` 생략) | 배치 기준 | 상대 x,y | 기본 x,y | 완료된 파시즘 HIDE x,y |
|---|---|---|---|---|
| `military_administration` | 참모업무 규정 `(172,8)` | `(2,1)` | `(174,9)` | `(90,9)` |
| `civil_supply_offices` | 군정 실무편람 | `(-1,1)` | `(173,10)` | `(89,10)` |
| `claims_accounts` | 군정 실무편람 | `(1,1)` | `(175,10)` | `(91,10)` |
| `civil_administration_rules` | 군정 실무편람 | `(0,2)` | `(174,11)` | `(90,11)` |
| `interservice_liaison` | `KOR_empowering_the_nrsc` `(167,2)` | `(-8,1)` | `(159,3)` | `(75,3)` |
| `joint_logistics_board` | 삼군 연락사무국 | `(-1,2)` | `(158,5)` | `(74,5)` |
| `joint_dispatch_records` | 삼군 연락사무국 | `(1,2)` | `(160,5)` | `(76,5)` |
| `service_supply_rules` | 삼군 연락사무국 | `(0,3)` | `(159,6)` | `(75,6)` |
| `reconstruction_secretariat` | `KOR_empowering_the_nrsc` `(167,2)` | `(-4,1)` | `(163,3)` | `(79,3)` |
| `public_accounts` | 재건행정 사무국 | `(-1,1)` | `(162,4)` | `(78,4)` |
| `construction_practice` | 재건행정 사무국 | `(1,1)` | `(164,4)` | `(80,4)` |
| `reconstruction_budget` | 재건행정 사무국 | `(0,2)` | `(163,5)` | `(79,5)` |

F4는 폭 2·높이 2, F5는 폭 2·높이 3, F6는 폭 2·높이 2의 격자 범위다. 전체 트리의 기존 범위 x0~204/y0~24와 기존 366개의 위치를 보존한다. 기존 다른 정치 경로·지속적 중점 패널·만주 바로가기와의 실제 클릭·표시는 별도 검증 대상이다. 새 선언은 기존 366개 뒤에 추가하므로 모든 배치 기준을 먼저 선언한다.

12개 중점과 8개 국민정신은 파시즘의 갈색·차콜 배경과 청동 장식, 정책별 중심 소재를 사용한다. 같은 계열의 정신은 소재를 공유하며 실제 I·II 단계만 표시한다. 완성 이미지와 광택 마스크·오버레이는 프로젝트 내부 파일을 상대경로로 참조한다. 새 결정이 없어 신규 디시전 아이콘은 만들지 않으며 기존 소형 아이콘을 보존한다. 이미지 출처·합성 기록·해시와 최종 좌표는 이 묶음의 별도 자산 기록 및 현재 좌표 JSON에 기록한다.

## 설치된 원본의 구문·단위 근거

아래 경로는 읽기 전용으로 확인한 `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/` 아래 경로다. 설치 버전과 실제 플레이세트는 구현 기록의 실행별 기준을 따른다. 예제 존재는 해당 블록의 문법 근거이며 이번 보상이 실제로 적용됐다는 게임 검증은 아니다.

| 근거 | 확인한 내용 |
|---|---|
| `common/national_focus/germany.txt:1857` | `any_controlled_state` 안의 `NOT = { is_core_of = ROOT }`, `is_fully_controlled_by = ROOT` |
| `common/national_focus/japan.txt:1200` | 중점 국가 범위에서 `has_full_control_of_state` 사용 |
| `common/ideas/australia.txt:1375` | 국가 정신의 `resistance_target`, `compliance_growth`, `required_garrison_factor`, `resistance_damage_to_garrison` |
| `common/ideas/army_spirits.txt:1077` | 군 보급 소모와 해·공군 연료 소비의 세 수정치 |
| `common/ideas/british_raj_goe.txt:1534` | 국가 정신의 `industry_repair_factor`와 별도 `industry_free_repair_factor` |
| `common/ideas/japan.txt:172` | 국가 정신의 고정 `political_power_gain` |
| `common/ideas/japan.txt:266` | 국가 정신의 민간공장 건설 속도 수정치 |
| `localisation/english/modifiers_l_english.yml:670` | 민간공장을 투입한 건물 수리 출력 보정의 설명 |
| `localisation/english/modifiers_l_english.yml:1351` | 순응도 증가 속도와 비율 표시 |

## 검증 계약

1. 기존 366개 블록 보존, 최종 378개와 신규 ID 유일성, 상대 기준 선언 순서·순환·좌표·7개 기존 offset 유지, GFX→프로젝트 파일 참조, BOM·언어 헤더·키 중복을 확인한다.
2. F4의 비핵심 완전 통제 없음/있음/상실, F6의 전쟁/평시·경기 소유 및 통제 유무, 파시즘·내전·항복 조건을 나누어 검사한다. 사람과 AI가 적격 상태에서 중점을 선택할 수 있는지와 진행 중 조건 상실을 구분한다.
3. F4·F5 중간 정책은 양 순서로 검사하고 마지막 AND 조건은 한쪽만 완료했을 때 차단되는지 확인한다. F6의 두 예산 선택은 별도 게임 상태에서 OR 합류·배타·선택 계열 승계를 검사한다.
4. 정치력·안정도·경험치·연구 혜택, I→II 교체 및 하위 정신 부재 대체, 기존 다른 정신 보존과 파시즘 상실 시 제거를 확인한다. 연구 범주 존재·정의값 확인과 실제 연구 혜택 소모는 구분한다.
5. 정적 검사, 강제 완료를 통한 즉시 보상 진단, 진단 없는 완전 재시작·새 게임 로드, 실제 HIDE/SHOW 화면, 정상 35일 중점 진행, 전체 모듈 진행을 별도로 기록한다. 배타 경로마다 105일/F4·F5 각각 140일의 정상 진행 및 실제 UI 취소는 별도 검증이다.
6. 신규 저장·재로드와 변경 전 저장 호환성, 장기 AI·DLC 대체 구성·멀티플레이는 각각 실제로 확인한 범위만 보고한다. 이번에 추가하지 않은 결정의 90일 비용·만료 검사는 기존 미검증 목록으로 남으며 이번 신규 보상 진단으로 충족하지 않는다.

이 문서는 구현 계약이다. 실제 통과 건수·스크린샷·소스 해시·실행 환경·미검증 항목은 [구현·검증 기록](incidents/2026-09-23-korean-fascist-followup.md)과 검증 산출물에 기록하며, 명세에 적혀 있다는 이유만으로 완료 처리하지 않는다.
