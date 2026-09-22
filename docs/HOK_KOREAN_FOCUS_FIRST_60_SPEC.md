# 한국 중점 1차 확장 60개 명세

> 2026-09-22 후속 적용: 현재 총354개(기존326+공산 경제정책10+후속 내정9+기술보급·계획행정9). 현재 구성·좌표·검증 상태는 [2차 확장 기록](HOK_KOREAN_SECOND_WAVE_PLAN.md)을 따른다. 아래326개 좌표·화면 관측은 이전 기준선 이력이며 후속 추가분의 게임 검증 결과가 아니다.

작성: 2026-09-21. 대상: 설치본 HOI4 1.19.3. 후속 개발 콘텐츠이며 호환성 복구 패치와 구분한다.

좌표 상태: **압축 재배치 적용 / HIDE 초기 상태 전체 분야 화면 검수 완료**. HOI4 1.19.3·27bf, 1936 한국 일시정지, 1600×900·GUI 배율 1에서 확인한 28개 화면에 아이콘·이름판 겹침이나 관계없는 선의 중점 가림은 관측되지 않았다. HIDE/SHOW 12개 조건의 위치 불변은 정적 검사이며, 이념 전환·SHOW 런타임은 이번에 재실행하지 않았다. [압축 작업 기록](incidents/2026-09-21-korean-focus-compact.md)의 범위와 한계를 따른다.

기존 266개를 유지한 총 326개 트리다. 아래 60개는 전부 `cost = 5`(35일)이며 기존 중점의 선행조건에 새 중점을 끼워 넣지 않는다. 산업 양산/유연생산과 공군 국산/우방 설계 각 한 쌍은 상호배타여서 한 플레이에서 신규 60개를 전부 완료하지 않는다. 표의 괄호 안은 OR, 괄호 사이는 AND다.

[구현·검증 기록](incidents/2026-09-21-korean-focus-expansion.md)과 [원본 후보 조사](HOK_KOREAN_FOCUS_DONOR_CATALOG.md)를 함께 읽는다. 선행·이름은 실제 코드에서 확인했고, 좌표는 재배치 적용 명세의 상대 기준 연쇄를 계산했으며 보상은 읽기 쉽게 풀어 썼다. 표에서 새 ID의 공통 `HOK_KOR_` 접두사만 생략하고 기존 `KOR_` ID는 그대로 표시했다. 수치는 원작 HoK의 기존 보상과 병행되며 장기 밸런스 검증은 별도다.

아래 60개는 `relative_position_id` 기준 상대 x/y를 사용한다. 표의 **기본 절대 x,y**는 현재 압축 배치의 참조 연쇄를 계산한 위치다. 직접 offset 4개는 조건문을 유지하고 이동량을 (0,0)으로 했으며, HIDE의 가지 숨김 조건은 그대로다. 기준 ID·상대값·AA58 전후 326개 표는 [압축 좌표 명세](HOK_KOREAN_FOCUS_LAYOUT_COORDINATES.md)를 따른다. 압축 좌표 검수 당시 소스 SHA-256은 `23049d0d607ecbdfe5454da644c292a55e7d903a4dca1b4f3d930105cde66242`다. 첫 재배치 이력과 기존 확장 기능 검증을 새 배치의 화면 검증으로 재사용하지 않는다.

강화 전 설명 동기화 이력(2026-09-21): 사용자가 저장한 산업 국민정신 10개에 맞춰 보상표와 양쪽 언어 채널을 동기화했다. 당시 전력 단계는 -10%/-20%/-30%, 숙련 단계는 +10%/+20%였다. 이 선행 작업은 수치·로직·좌표를 변경하지 않았다. 이후 아래 보상 강화가 숙련·생산 등 해당 수치를 대체하며, 전력 3단계는 유지한다.

보상 강화 상태(2026-09-21): 사용자 승인으로 [보상 재조정 설계](HOK_KOREAN_FOCUS_REBALANCE_PLAN.md)의 수치·기간·반복 사업을 적용하고, 아래 표를 실제 중점·국민정신·결정 코드와 대조했다. **보병장비 한정 생산량 보정은 적용 방식 확정 대기이며 표에 적용된 효과로 쓰지 않았다. 강화 후 런타임과 장기 밸런스는 검증 전이다.** 이전 확장·좌표 화면 검수 결과를 강화 수치 검증으로 재사용하지 않는다.

표의 안정도 획득은 완료 즉시 지급하는 %p이고 국민정신의 안정도 보정과 별개다. 상위 국민정신의 최종값은 이전 단계와 중첩되지 않는다. 야간교육과 농촌교육의 연구 속도 보정은 서로 별도이며, 두 보정의 합은 +20%다. 통합 군수체계와 해외 보급업무 개선의 보급 소모 보정 합은 -20%다. 연구 보너스의 횟수는 지정 범위에만 사용되며, 대상 기술을 이미 연구했다면 모두 소진하지 못할 수 있다.

## 산업·교육 20개

| ID (`HOK_KOR_` 접두사) | 한국 이름 | 선행 중점 | 기본 절대 x,y | 보상·연결 기능 | 바닐라 기반 |
|---|---|---|---|---|---|
| `link_power_grids` | 전국 전력망 연계 | (KOR_comprehensive_national_development_plan) | 5,7 | 전력 국민정신: 공장 에너지 소비 -10% | I1 |
| `industrial_power_allocation` | 산업용 전력 배분 | (link_power_grids) | 5,8 | 전력 국민정신을 공장 에너지 소비 -20%로 교체 | I1 |
| `industrial_measurement_standards` | 공업 계량규격 통일 | (industrial_power_allocation) | 5,9 | 산업 연구 150% 보너스 2회 | I1 |
| `factory_safety_inspections` | 공장 안전검사제 | (industrial_measurement_standards) | 5,10 | 즉시 안정도 +10%p | I1 |
| `national_power_coordination` | 국가전력조정위원회 | (factory_safety_inspections) | 5,11 | 전력 국민정신을 공장 에너지 소비 -30%로 교체 | I1 |
| `technical_colleges` | 실업전문학교 확충 | (KOR_seoul_national_university_expansion) | 12,3 | 전자공학 연구 100% 보너스 2회 | I2 |
| `workshop_apprenticeships` | 공장 도제교육 | (technical_colleges) | 12,4 | 숙련인력: 생산효율 성장 +30% | I2 |
| `workers_night_schools` | 노동자 야간학교 | (workshop_apprenticeships) | 12,5 | 즉시 안정도 +5%p; 별도 영구 국민정신 연구 속도 +10% | I2 |
| `university_industry_labs` | 산학 공동연구실 | (workers_night_schools) | 12,6 | 산업 연구 150% 보너스 1회 | I2 |
| `skilled_workforce` | 숙련공 양성체계 | (university_industry_labs) | 12,7 | 숙련인력을 최종 생산효율 성장 +60%로 교체; 이전 단계 대비 +30%p | I2 |
| `production_review` | 생산공정 실태조사 | (KOR_development_of_heavy_industry) | 18,3 | 정치력 +150; 산업 연구 100% 보너스 1회 | I3 |
| `standardized_mass_production` | 표준규격 대량생산 | (production_review) | 17,4 | 대량생산 선택: 생산효율 상한 +15%, 생산라인 전환 시 효율 유지 -5% | I3 |
| `flexible_production_lines` | 유연한 생산라인 | (production_review) | 19,4 | 유연생산 선택: 생산라인 전환 시 효율 유지 +20%, 생산효율 상한 -2.5% | I3 |
| `production_quality_assurance` | 생산품 품질보증 | (standardized_mass_production 또는 flexible_production_lines) | 18,5 | 기본 생산효율 +10% | I3 |
| `integrated_production_planning` | 통합 생산계획 | (production_quality_assurance) | 18,6 | 선택 정책만 교체: 양산 최종 생산효율 상한 +30%·전환 유지 -5% 또는 유연 최종 전환 유지 +40%·상한 -2.5%; 이전 단계와 중첩 안 됨 | I3 |
| `regional_industry_fund` | 지역 공업 투자기금 | (KOR_first_new_city_plan) | 30,5 | 정치력 +150; 지역 공업 투자 카테고리 | I4 |
| `pyeongan_machine_workshops` | 평안 기계공업 육성 | (regional_industry_fund) | 30,6 | 평안 군수공장 1개·슬롯 1개 유료 건설 결정; PP150·민공5·90일, 순차 반복 | I4 |
| `gangwon_electrical_workshops` | 강원 전기기기 공업 | (pyeongan_machine_workshops) | 30,7 | 강원 민간공장 1개·슬롯 1개 유료 건설 결정; PP150·민공5·90일, 순차 반복 | I4 |
| `chungcheong_supplier_network` | 충청 부품공급망 | (gangwon_electrical_workshops) | 30,8 | 충청 민간공장 1개·슬롯 1개 유료 건설 결정; PP150·민공5·90일, 순차 반복 | I4 |
| `gyeongsang_export_workshops` | 경상 수출조선 지원 | (chungcheong_supplier_network) | 30,9 | 경상 조선소 1개·슬롯 1개 유료 건설 결정; PP150·민공5·90일, 순차 반복 | I4 |

## 육해공군 25개

| ID (`HOK_KOR_` 접두사) | 한국 이름 | 선행 중점 | 기본 절대 x,y | 보상·연결 기능 | 바닐라 기반 |
|---|---|---|---|---|---|
| `procurement_contracts` | 국방조달계약 | (KOR_army_augmentation) | 45,3 | 보병장비 연구 100% 2회; AAT·KOR이면 기존 조병창 MIO 자금 +300, 그 외 육군 경험치 +10 | M1 |
| `ammunition_standards` | 탄약 규격 통일 | (procurement_contracts) | 45,4 | 조달 국민정신: 생산효율 상한 +3% | M1 |
| `ordnance_inspection` | 병기 검사제도 | (ammunition_standards) | 44,5 | 포병 연구 100% 1회; AAT·KOR이면 한화 MIO 자금 +300, 그 외 육군 경험치 +10 | M1 |
| `field_maintenance` | 야전 정비창 | (ammunition_standards) | 46,5 | 정비중대 연구 100% 2회 | M1 |
| `distributed_ordnance_depots` | 분산 군수창 체계 | (ordnance_inspection) 및 (field_maintenance) | 45,6 | 조달 최종 상한 +10%·보급 소모 -10%로 교체; 군수중대 연구 100% 1회 | M1 |
| `staff_exercises` | 참모부 도상훈련 | (KOR_research_army_doctrine) | 38,7 | 육군 경험치 +40; 계획 수립 속도 +10% | M2 |
| `winter_training` | 개마고원 동계훈련 | (staff_exercises) | 37,8 | 겨울 소모 -30% | M2 |
| `mountain_reconnaissance` | 산악 정찰학교 | (staff_exercises) | 39,8 | 산악병 연구 100% 2회; 육군 경험치 +10 | M2 |
| `radio_coordination` | 무선 지휘망 표준화 | (winter_training 또는 mountain_reconnaissance) | 38,9 | 무전 연구 100% 2회; 육군 경험치 +10 | M2 |
| `joint_arms_exercises` | 제병협동 연습 | (radio_coordination) | 38,10 | 참모 국민정신을 최종 계획 속도 +20%·조직적 협동 +6%로 교체; 육군 경험치 +15 | M2 |
| `rapid_repairs` | 진해 수리창 정비 | (KOR_daehanminguk_haegun) | 61,2 | 함선 수리 속도 +30% | M3 |
| `archipelago_training` | 다도해 기동훈련 | (rapid_repairs) | 60,3 | 해군 경험치 +30; MTG에서 미연구 연막발생기 해금, 미보유·기연구 시 추가 해군 경험치 +40(합계 70) | M3 |
| `escort_school` | 호위전대 학교 | (rapid_repairs) | 62,3 | 구축함 연구 100% 2회; 수송선 호위 효율 +30% | M3 |
| `anti_submarine_school` | 대잠전 학교 | (archipelago_training 또는 escort_school) | 61,4 | MTG 소나·폭뢰 연구 100% 2회, 그 외 구축함 연구 100% 2회; 해군 경험치 +10 | M3 |
| `coastal_fire_control` | 함포지원 연락체계 | (anti_submarine_school) | 61,5 | 해안 포격 +30%; 상륙 불이익 -15% | M3 |
| `fleet_staff_college` | 함대 참모학교 | (KOR_large_surface_fleet 또는 KOR_commerce_raiding) | 55,4 | 해군 경험치 +50 | M4 |
| `underway_replenishment` | 해상 보급절차 | (fleet_staff_college) | 54,5 | 해군 연료 소비 -15%; 항속거리 +15% | M4 |
| `deck_training` | 갑판 운용학교 | (fleet_staff_college) | 56,5 | 항공모함 연구 100% 2회; 해군·공군 경험치 각 +20 | M4 |
| `naval_air_coordination` | 해공 합동연락망 | (underway_replenishment 또는 deck_training) | 55,6 | 뇌격기 연구 100% 2회; 공군 경험치 +30 | M4 |
| `amphibious_rehearsals` | 상륙지원 합동연습 | (naval_air_coordination) | 55,7 | 해병 연구 100% 2회; 해군·육군 경험치 각 +30 | M4 |
| `domestic_aircraft_designs` | 국산 설계 역량 집중 | (KOR_korea_aerospace_industry) | 71,4 | 국산 선택: BBA 항공 모듈 연구 150% 2회, 그 외 경전투기 연구 150% 2회; AAT·KOR이면 KAI 자금 +500, 그 외 공군 경험치 +15 | M5 |
| `foreign_aircraft_designs` | 우방 항공기술 도입 | (KOR_korea_aerospace_industry) | 73,4 | 우방 선택: 같은 정부의 비적대 강대국 필요; 항공장비 연구 75% 2회와 공군 경험치 +15; 특정국 기술 직접 지급 아님 | M5 |
| `formation_flying` | 편대전술 표준화 | (domestic_aircraft_designs 또는 foreign_aircraft_designs) | 72,5 | 공군 임무 효율 +10% | M5 |
| `air_maintenance_school` | 항공정비학교 | (formation_flying) | 72,6 | 항공 사고 -30%; 공군 경험치 +20 | M5 |
| `combat_lessons_center` | 항공전훈 연구반 | (air_maintenance_school) | 72,7 | 공군 임무 효율을 최종 +30%로 교체(이전 대비 +20%p); 공군 경험치 +25 | M5 |

## 민주 내정·외교 15개

| ID (`HOK_KOR_` 접두사) | 한국 이름 | 선행 중점 | 기본 절대 x,y | 보상·연결 기능 | 바닐라 기반 |
|---|---|---|---|---|---|
| `parliamentary_committee` | 국정 협의위원회 | (KOR_strengthen_government_support) | 107,9 | 정치력 +100; 즉시 안정도 +10%p | D1 |
| `civil_service_audit` | 공직 감찰 정비 | (parliamentary_committee) | 106,11 | 민주정부 동안 일일 정치력 +0.25 | D1 |
| `technical_civic_schools` | 실업·시민교육 확대 | (parliamentary_committee) | 109,11 | 전자공학 연구 25% 보너스 1회 유지; 소유·완전통제·부지 조건을 갖춘 경기525·전라1082·충청1031에 민간공장과 슬롯 각 2개(공장 총 6개) | D1 |
| `rural_education_missions` | 농촌 순회교육 | (technical_civic_schools) | 109,13 | 연구 속도 +10%, 영구; 야간교육과 별도 | D1 |
| `public_accounts_committee` | 국회 결산위원회 | (civil_service_audit) 및 (rural_education_missions) | 107,14 | 즉시 안정도 +10%p; 행정 국민정신 교체 후 일일 정치력 +0.25 유지·안정도 +2% | D1 |
| `volunteer_liaison_bureau` | 의용군 연락본부 | (KOR_korean_volunteer_corps) | 138,11 | 육군 경험치 +50; 정치력 +100; 해외 지원 결정 카테고리 | D2 |
| `overseas_medical_detachments` | 해외 의료지원반 | (volunteer_liaison_bureau) | 136,13 | 지원기술 연구 100% 2회; 한국 비축 지원장비 50개 기부 결정 | D2 |
| `volunteer_supply_depots` | 의용군 보급계획 | (volunteer_liaison_bureau) | 140,13 | 한국 육군 전체 보급 소모 -10%, 영구; 통합 군수체계와 별도 | D2 |
| `expeditionary_lessons` | 전훈 교류 | (overseas_medical_detachments) 및 (volunteer_supply_depots) | 138,15 | 완료 육군 경험치 +50; 1회성 PP35·30일 전훈 교류 결정의 성공 보상 육군 경험치 +25 | D2 |
| `overseas_relief_network` | 해외 구호망 | (expeditionary_lessons) | 138,16 | 즉시 안정도 +10%p; 정치력 +100; 한국 비축 보병장비 100개 기부 결정 | D2 |
| `asian_trade_secretariat` | 아시아 공동통상사무국 | (KOR_founding_of_the_asian_union) | 116,17 | 정치력 +150; 아시아 공동사업 카테고리 | D3 |
| `asian_customs_convention` | 아시아 관세협약 | (asian_trade_secretariat) | 114,19 | 동맹에 수락·거절 이벤트 발송; 수락국의 대한국 수입 비용 -30%, 730일; PP25·대상별 180일 간격 재제안, 횟수 상한 없음 | D3 |
| `asian_development_fund` | 아시아 공동개발기금 | (asian_customs_convention) | 114,21 | 관세협약 동맹 민간공장 1개·슬롯 1개 사업 해금; PP75·민공2·180일, 같은 대상에도 순차 반복 | D3 |
| `asian_armaments_commission` | 아시아 공동군수위원회 | (asian_trade_secretariat) | 118,19 | 육군 경험치 +50; 포병 연구 100% 2회 | D3 |
| `asian_license_agreement` | 아시아 면허생산협정 | (asian_armaments_commission) | 118,21 | DOD: 수락국↔한국에 730일 면허생산 속도·기술 격차 보정 각 +30%, AI 수락 의향 +20 유지; 재제안 결정; DOD 없으면 육군 경험치 +50 | D3 |

## 바닐라 대응과 한국용 조정

아래 경로는 모두 읽기 전용 설치본 1.19.3 기준이다. 원본 전체를 태그만 바꾸어 복사한 것이 아니라 해당 효과·선택·정책 구조를 재사용하고 한국의 기존 선행과 국민정신에 맞게 조정했다. 외국 변수·인물·주·기업 의존성을 그대로 남기지 않았다.

| 기호 | 확인한 원본 | 한국용 적용 |
|---|---|---|
| I1 | national_focus/japan.txt:26133, JAP_establish_nippon_hassoden; ideas/czechoslovakia_skoda.txt:48 이후 | 직접 전력 국민정신 3단계; 석탄 지급과 일본 동적 변수 제외 |
| I2 | national_focus/china_nationalist_sea.txt:14458, CHI_extend_compulsory_education; ideas/bulgaria.txt:675, canada.txt:264 | 교육 연구 및 숙련 성장; 중국 초기 불이익·농촌 변수 제외 |
| I3 | national_focus/finland.txt:13671/13767, FIN_expand_production_lines/FIN_modernize_production_lines; ideas/sweden.txt:661 | 생산 정책 상호배타 및 장단점; 한국용 수치 조합 |
| I4 | decisions/SWE.txt:349의 SWE_urbanization_decision 및 decisions/resource_prospecting.txt:8657의 deeper_swedish_mines; 기존 HoK 팔도개발 | PP150·민공5·90일, 현재 한국 주에 순차 반복 건설; 소유·완전통제·부지 조건 유지 |
| M1 | national_focus/sweden.txt:390/434, 정부 조달·장비 규격화 | 기존 한국 MIO와 연구 보너스; 초기 스웨덴 불이익 제외 |
| M2 | national_focus/finland.txt:11413; japan.txt:30815/30863; usa.txt:5640/5673 | 동계훈련·무전·제병협동, 직접 국민정신·경험치·기술 보너스 |
| M3 | national_focus/sweden.txt:1962/2387; ideas/sweden.txt:556/587; australia.txt:1155 | 수리·다도해·호위·대잠 및 MTG 대체 보상 |
| M4 | national_focus/usa.txt:5640/5673; ideas/usa.txt:1328, japan.txt:5680 | 함대·항속·상륙·해공 연구/훈련을 한국 후속 가지로 구성 |
| M5 | national_focus/sweden.txt:3046/3104/3160; ideas/air_spirits.txt:144/206 | 국산/우방 설계 선택, KAI 자금, BBA/AAT 대체 보상과 항공 정비 |
| D1 | national_focus/china_nationalist_sea.txt의 시민권·의무교육/농촌교육 경로 | 민주 행정과 영구 교육 보너스; 정부 정상화 대기는 별도 유지 |
| D2 | decisions/FRA.txt 원조; national_focus/usa.txt 훈련; decisions/CZE.txt:1295 | 실제 한국 장비 기부, 실전/의용군 참여를 요구하는 유료 전훈 교류 |
| D3 | events/SEA_Japan.txt의 SEA_japan_foreign_policy.97~.102; national_focus/france.txt:4003/4064; modifiers/00_static_modifiers.txt:267 | 수락·거절, 유한 협정, 유료 동맹 공장 사업, 면허 관계 보정 |

효과 보조 근거: ideas/chile.txt:2222 및 scripted_effects/SOV_scripted_effects.txt:2806의 관계 보정 제거; documentation/dynamic_variables_documentation.md:974 및 decisions/_documentation.md:24의 국가 배열·대상 사전 검사. 원본 파일 해시는 [구현 기록](incidents/2026-09-21-korean-focus-expansion.md)의 증거 보관 위치에 남겼다.
