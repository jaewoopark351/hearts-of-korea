# 한국 재벌·시민사회 산업정책 구현 명세

작성일: 2026-10-11; 갱신일: 2026-10-12. 이 문서는 현재 소스의 확정값과 연결 관계를 기록한다. 연구 후보·소스 구현·정적 확인과 실제 엔진 관측을 구분한다. 이번 개정의 증거·대기 항목은 [유지보수 기록](incidents/2026-10-12-korean-civic-revision.md), 개정 전 실제 실행은 외부 `C:/hoi/test/civic-influence-20261012-authorized-runtime/TEST_REPORT.md`를 따른다.

**2026-10-12 승인 개정:** [변경 기록](HOK_KOREAN_CHAEBOL_CIVIL_SOCIETY_REVISION_PLAN.md)의 주문이관·구협력노드 제거/호환ID·민주진입/배치·패널y1400·19상태명key를 반영했다. 한국playable중점472개·신규내정13개이며 지도자매핑은 그대로다.82/0·구조498/0의 정적확인과 실제관측을 구분한다. 4410에서 구 완료 A의 즉시 주문 표시와 A 재로드 후 월간 비중복을 확인했다. 합성 fixture 없는 자연 독립당 경로로 협약·산업협력을 완료하고 원래 주문 3개를 각 100PP로 사용했다. 90일 타이머의 만료 후 삼성 재사용, 자연 저장의 전체 프로세스 재시작에서 93PP·70/45/23/45·공통 대기90일·주문90일·김구 유지도 관측했다. SHOW 민주 중점 전후의 같은 카메라15점 유지, 한글 상태명19종의 최소1회 tooltip 표시, 등록 민주6명의 제한된 표시 범위를 확인했다. 합성조건/role fixture의 한계와 일반save·DLC/AI/MP 미검증, 최종 원본보호 확인과 settings byte복원 제한은 유지보수 기록을 따른다.

**진단 없는 자유당 후속 확인:** 진단mod·fixture·정치력forcing 없는 d2e6(HoK1mod·36DLC·debug, 역사적AI/HIDE)에서 자유당 정상선행→협약→산업협력을 완료했다. 협약 OR는 자유당초록/독립당빨강·산업화조건없음·150PP/category안내였고 패널60/35/20/40→70/35/25/45를 관측했다. 다음월06.07.09에도 같은상태에서 원래삼성/현대/선경을308→208→108→8PP·각90일로 실제사용했다. 이d2e6의주문만료·저장/reload는 실행하지 않았으며 앞선4410독립당게임의 증거와구분한다. 정확완료순간·순수150PPdelta를 역산하지 않는다. 최종 원본71metadata보호·프로필2파일 byte일치·설정 기능복귀는 확인했고 settings의 로딩화면 순서 byte복원 제한은 아래 최종절에 기록한다.

## 2026-10-12 최종 런타임·원본 보호 확인

진단 없는 d2e6 자유당 게임을 1936.06.07.09에 정상 종료했다. 초기와 종료 직전 오류 내용은 같았고, 해당 내정·주문·구 ID를 직접 가리키는 오류는 없었다. 종료 후에는 기존 random.log 이름 변경 실패 2행이 추가됐다. 정상 진행·합성 표시 검사·정적 확인을 구분한 결과를 외부 `TEST_REPORT.md`와 [최종 기록](incidents/2026-10-12-korean-civic-revision.md)에 정리했다.

등록된 구 완료 저장 B도 d2e6 소스만으로 재저장하고 전체 재시작해 불러왔다. 1936.03.08.23·정치력45·70/35/25/45·세 기업 주문 표시와 잠긴 관리 기능이 유지됐고, 다음 월04.11.05에도 수치가 중복 증가하지 않았다. 초기 구 저장의 누락된 진단 디시전 경고는 재저장 파일에서 재발하지 않았다. 이 한 사례를 일반 저장 호환으로 확대하지 않는다.

기존 저장 71개의 이름·크기·정밀 UTC 수정 시각 차이는 0이다. 신규 테스트 임시 저장 총5개는 보존했고 진단 로더는 제거했다. 모드 목록과 기존 런처 파일의 원본 해시는 일치한다. 자동저장 반년·해상도·창 모드 등 설정은 원본과 같지만, 게임이 같은 로딩 화면 28개의 순서를 바꿔 settings.txt 해시가 다르다. 백업으로 덮어쓰기는 Windows 접근 거부로 실패했다. 설정 기능 복귀와 파일 전체의 byte 일치를 구분하며, 보안 설정을 변경하지 않았다.

실제 한국 AI 선택·DLC 비활성 게임·멀티플레이, 모든 기존 저장의 일반 호환과 모든 표시 조합 등은 미검증이다. 기존 저장 보호 확인을 전체 저장 호환 통과로 해석하지 않는다.

## 1. 범위와 구현 의도

신규 내정 13개 중점과 재벌·시민사회 두 세력 패널을 제공한다. 2026-10-12 개정에서 진입을 민주 정치 가지의 독립당 또는 자유당 단독집권 이후로 옮겼으므로 새 게임의 정상 접근은 해당 민주 경로로 좁아진다. 재벌의 빠른 생산망, 시민 개혁의 연구·인력·효율 보상, 공공 소유의 설비와 기술 승계를 서로 다른 정책으로 제공한다. 기존 기업·주문·재벌 길들이기 대안과 지도자·인물 ID는 유지하되 구 협력의 플레이 가능한 노드만 제거했다. 일본의 육군·해군·천황 세력 체계를 한국에 복제하지 않는다.

재벌 의존의 문제는 이미 얻은 생산망과 별도로 누적되는 조달 비리와 기관 장악이다. 시민 경로의 대가는 작은 소비재 부담과 기득권의 기관 반격이며, 비리와 같은 크기의 벌칙을 시민 경로에 대칭으로 부과하지 않는다. 비용과 기한을 감수하면 기관 개혁을 완수하고 산업 협약을 유지할 수 있다.

한국화약의 가상 항공용 화약·탄약 급행 공급과 컨소시엄 검수 누락에 따른 격납고 폭발, 1936년 한국화약 추진제 계약·폭발, 기업과 결탁한 검찰 권력망의 정변은 이 모드의 가상 대체역사 설정이다. 실존 기업의 실제 비리나 사건을 확인한 역사 서술이 아니다. 다른 모드 연구의 근거와 미채택 후보는 [연구 계획](HOK_KOREAN_CHAEBOL_CIVIL_SOCIETY_RESEARCH_PLAN.md)에 남긴다.

기준 저장소는 feat/korean-focus-expansion-ai, 기준 HEAD는 4d8241e3cd33ebbceaca9650ab36b9891a22b56d이다. 아래 추가물은 아직 커밋하지 않은 개발 작업이며 Git 변경이나 배포·업로드를 수행한 기록이 아니다. 대상 구문은 설치된 HOI4 1.19.3 소스에 대조했다.

## 2. 상태, 수명과 멱등 초기화

모든 상태는 country KOR의 저장 변수·country flag이다. 재벌과 시민사회의 영향력 합계는 100으로 고정되지 않는다. 비리와 기관 장악도 영향력에서 다시 계산하지 않으므로 세력을 견제한 뒤에도 과거의 손실과 결탁이 남는다.

| 변수 | 최초 값 | 범위 | 의미 |
|---|---:|---|---|
| HOK_KOR_chaebol_influence | 60 | 0~100 | 재벌의 투자·납품·정책 영향력 |
| HOK_KOR_civic_influence | 35 | 0~100 | 노동·교육·시민 감독의 영향력 |
| HOK_KOR_procurement_corruption | 20 | 0~100 | 누적된 조달 비리 |
| HOK_KOR_institutional_capture | 40 | 0~100 | 행정·수사·예산 기관의 장악 |

HOK_KOR_initialize_civic_system은 HOK_KOR_civic_system_initialized가 없는 KOR에만 최초 값을 넣는다. 선택 정책은 초기화하지 않는다. HOK_KOR_sync_civic_state는 네 변수의 범위를 제한하고 오래된 tier·정책·비리 spirit을 제거한 뒤 현재 상태와 일치하는 spirit만 유지한다.

HOK_KOR_register_legacy_civic_state는 초기화 이후 구협력ID 또는 새산업협력완료와 기존길들이기·국유화완료의 once helper를 확인한다. on_startup/on_monthly_KOR는 수정하지 않았으며 명시적KOR scope에서 호출한다. 초기화 안에서legacy helper를 역호출하지 않아 재귀를 피한다.7874 양성A의 구완료TRUE·첫월+10/+5/+5·두 번째월 비중복, B 등록완료fixture월간 비중복을 관측했다.4410 A 월간저장 게임내Load 후04.11.07에도70/35/25/45를 유지했다. 자연 새협력 완료도60/35/20/40→70/35/25/45와 일치했다. startup즉시등록·모든기존저장 일반호환은 미검증이다.

패널은 상태 초기화 이후 표시된다. 버튼과 첫 결정 category는 HOK_KOR_civic_panel_unlocked 이후 사용한다. 이 flag는 산업·사회협약 중점에서 켠다. 최초 seed는 정책 미선택이며 이 상태에서는 정책에 따른 월간 비리 변화나 정변이 발생하지 않는다. 초기화 시 해당 영향력 tier spirit은 적용된다.

## 3. 네 영향력 단계와 비리 부담

UI 단계 경계와 spirit 경계를 25/50/75로 통일했다. 기반과 간섭은 별도 spirit과 보너스를 사용한다. 각 세력은 자기 tier 하나만 가지며, 두 세력의 spirit은 함께 존재할 수 있다.

| 단계 | 값 | 재벌 spirit 및 보너스 | 시민사회 spirit 및 보너스 |
|---|---|---|---|
| 약함 | 25 미만 | 없음 | 없음 |
| 기반 | 25~49 | HOK_KOR_chaebol_established: 군수공장 건설 +3%, 군수공장 생산 +3% | HOK_KOR_civic_established: 안정도 +2%, 효율 성장 +3% |
| 간섭 | 50~74 | HOK_KOR_chaebol_interfering: 군수공장 건설 +5%, 군수공장 생산 +5% | HOK_KOR_civic_interfering: 안정도 +3%, 효율 성장 +5% |
| 지배 | 75 이상 | HOK_KOR_chaebol_dominant: 군수공장 건설 +10%, 군수공장 생산 +8% | HOK_KOR_civic_dominant: 안정도 +5%, 효율 성장 +10%, 생산라인 변경 시 효율 유지 +5% |

| 누적 비리 | spirit | 확정 부담 |
|---|---|---|
| 40 미만 | 없음 | tier 부담 없음 |
| 40~69 | HOK_KOR_procurement_corruption_moderate | 군수공장 생산 -8%, 연구 속도 -3%, 정치력 획득 계수 -5% |
| 70 이상 | HOK_KOR_procurement_corruption_severe | 군수공장 생산 -20%, 연구 속도 -10%, 소비재 공장 계수 +10% |

소비재 공장 계수는 consumer_goods_factor다. 위 +5%/+10%는 소비재의 절대 비율에 5/10%p를 더한다고 적지 않는다. 지속 안정도 modifier와 event의 add_stability 즉시 변화도 구분한다. 효율 유지의 실제 키는 line_change_production_efficiency_factor이며, 존재가 확인되지 않은 production_factory_efficiency_loss_factor를 사용하지 않는다.

## 4. 지원·견제 버튼과 결정

공통 가용 조건은 KOR, 초기화 완료, 패널 사용 해금, 항복하지 않음, 내전 없음, 정치력 50 이상, 공통 대기 flag 없음이다. 지원은 해당 영향력 100 미만, 견제는 0 초과일 때 사용할 수 있다. 범위 끝에서는 sync가 0~100으로 제한한다.

정치력 경계는 NOT = { has_political_power < 50 }로 처리한다. GUI의 HOK_KOR_support/suppress_* 공개 효과는 50PP를 차감한 뒤 내부 HOK_KOR_apply_support/suppress_* helper를 호출한다. 동일 이름의 결정은 표시 cost=50으로 엔진이 먼저 차감하고 내부 helper만 호출한다. helper는 PP를 다시 요구하거나 차감하지 않으며 상태·범위·cooldown을 재확인한다. 따라서 두 진입점의 실제 비용은 각각 50PP 한 번이다.

| 공개 효과 및 결정 ID | 해당 영향력 | 비리 | 기관 장악 | 비용·대기 |
|---|---:|---:|---:|---|
| HOK_KOR_support_chaebol | 재벌 +10 | +5 | +3 | 50PP, 전체 지원·견제 공통 90일 |
| HOK_KOR_suppress_chaebol | 재벌 -10 | -3 | +4 | 동일 |
| HOK_KOR_support_civic | 시민 +10 | -2 | 시민 개혁 정책에서 +3, 그 외 변화 없음 | 동일 |
| HOK_KOR_suppress_civic | 시민 -10 | +8 | +5 | 동일 |

공통 flag는 HOK_KOR_civic_action_cooldown, 지속 90일이다. 재벌 견제는 영향력을 낮추면서도 기관 장악을 올릴 수 있다. 시민 감시를 늘려 비리를 줄이는 효과와 개혁에 대한 기관 반발 역시 서로 다른 변수에 기록한다.

## 5. 세 산업정책과 월간 변화

세 선택 중점은 상호 배타적이다. 선택 효과는 다른 새 정책 flag를 지우고 자신의 flag를 설정한다. 원래 한국의 기업 spirit이나 기존 보상은 제거하지 않는다. 정책 선택만으로 네 변수의 누적값을 리셋하지 않는다.

| 정책·effect | flag / spirit | 기본 보상 |
|---|---|---|
| 재벌 협력 / HOK_KOR_select_chaebol_cooperation | HOK_KOR_policy_cooperation / HOK_KOR_chaebol_cooperation | 군수공장 건설 +20%, 군수공장 생산 +15% |
| 독점 해체·시민 개혁 / HOK_KOR_select_civic_reform | HOK_KOR_policy_civic_reform / HOK_KOR_civic_reform | 소비재 공장 계수 +5%, 안정도 +10%, 연구 +5%, 징병 가능 인구 +2%p, 라인 변경 효율 유지 +15%, 군수공장 생산 +10% |
| 공공 소유 / HOK_KOR_select_public_ownership | HOK_KOR_policy_public_ownership / HOK_KOR_public_ownership | 군수공장 생산 +15%, 민간공장 건설 +15%; 선택 중점에서 민간공장 2개 추가 |

시민 정책의 인력 키는 conscription=0.02이며 conscription_factor의 상대 증가와 다르다. 국민개병제 후속은 2%p를 재차 쌓는 대신 인력 100,000과 육군 경험 30을 즉시 준다. 산업·전자 연구 일회성 할인은 아래 기업·정착·검수 중점에 따로 배치한다.

| 월간 조건 | 비리 변화 | 기관 장악 변화 |
|---|---:|---:|
| 협력 정책 + 재벌 지배(75 이상) | +2 | +1 |
| 시민 개혁 + 검찰 국정 장악 상태 아님 | -1 | HOK_KOR_civic_reform_pressure가 있으면 +1 |
| 공공 소유 정책 | -1 | 없음 |
| 정책 미선택 | 없음 | 없음 |

시민 개혁 선택이 HOK_KOR_civic_reform_pressure를 켠다. 기관 장악망 해체 또는 시민적 위임 회복을 완료하면 이 flag를 지워 개혁 저항에 따른 월간 기관 장악 증가를 끝낸다. 이후 지원·견제·특혜·은폐의 직접 변화는 여전히 가능하다. 매월 마지막에 sync하고 정변 경고 조건을 한 번 확인한다.

## 6. 기존 중점과 저장의 누적 의미

| 등록 대상 완료 이력 | 공용 helper | 한번만 추가되는 상태 변화 | 등록 flag |
|---|---|---|---|
| KOR_cooperation_with_the_jaebeol OR HOK_KOR_civic_chaebol_cooperation | HOK_KOR_legacy_cooperation_adjustment | 재벌 +10, 비리 +5, 기관 장악 +5 | HOK_KOR_legacy_cooperation_registered — 기업 협력 이력 등록 |
| KOR_taming_the_jaebeol | HOK_KOR_legacy_taming_adjustment | 재벌 -10, 시민 +5, 비리 -5 | HOK_KOR_legacy_taming_registered |
| KOR_confiscation_of_chaebol_assets | HOK_KOR_legacy_nationalization_adjustment | 재벌 -20, 시민 +10, 기관 장악 -5 | HOK_KOR_legacy_nationalization_registered |

각 helper는 init을 호출하고 자신의 등록 flag가 없을 때만 적용한다. 협력 helper는 새 산업협력의 completion_reward와 초기·월간의 구 ID OR 새 ID 확인에서 공유한다. 기존 길들이기·국유화의 직접 완료 연결은 보존했다. 동일 helper의 여러 호출이 소스상 같은 flag로 중복을 막는다. 협력 등록 flag는 구·신 협력 모두의 이력을 뜻하며 구 저장 전용 표식이 아니다.

구 협력은 한국 트리에서 제거하되 [별도 shared 정의](../common/national_focus/HOK_KOR_civic_legacy_focus.txt)에 ID를 한 번 등록했다. 해당 shared 정의는 트리에 가져오지 않고 available always=no·AI 0·빈 보상으로 새 선택을 제공하지 않는다. 설치 1.19.3의 shared-focus 형식에 대조했고 7874 A 저장의 구 완료 ID 판정 TRUE·월간 등록을 관측했다. A 월간후 새저장의4410 게임 내 Load는 관측했으며 B 재저장/재로드는 d2e6에서 확인했고 모든 저장의 일반 호환은 미검증이다. 구 완료 때문에 새 정책을 자동 선택하거나 산업·사회협약을 자동 완료·150PP 지급하는 효과는 없다.

새 협력·국유화·시민 정책을 선택해도 기존 KOR_jaebeol의 군수공장 생산 +20% 등 원래 혜택을 제거하지 않는다. 기존 정책과 새 산업정책은 별도 세대의 콘텐츠이며 함께 누적될 수 있다. 새 세 정책 spirit만 서로 중복되지 않도록 sync한다. 혼합 경로의 최종 수치에는 기존 혜택, 해당 영향력 tier, 비리 부담과 다른 한국 spirit이 더해질 수 있으므로 아래 신규 보상 표를 국가 전체 최종값으로 해석하지 않는다.

## 7. 13개 중점과 직접 보상

모든 새 중점 cost=5, 설치된 vanilla FOCUS_POINT_DAYS=7 기준 정상 소요 35일이다. 진입은 KOR_independent_party_in_power 또는 KOR_liberal_party_sole_power 완료 이후다. 기존 산업화 선행을 대체했으며 추가 AND가 아니다. 한 prerequisite block의 여러 focus는 OR, 서로 다른 prerequisite block은 AND다. 중점 보상은 [korea.txt](../common/national_focus/korea.txt)와 [새 중점 문안](../localisation/korean/HOK_KOR_civic_focus_l_korean.yml)을 함께 읽어 확인했다.

| 중점 ID·한국명 | 선행 | 직접 보상 |
|---|---|---|
| HOK_KOR_civic_industrial_compact · 산업·사회협약 | 독립당 단독집권 OR 자유당 단독집권 | 상태 init, 패널 버튼·세력 결정 해금, 150PP |
| HOK_KOR_civic_chaebol_cooperation · 재벌과의 산업협력 | 산업·사회협약 | 협력 정책 spirit, 조달 category·삼성/현대/선경 주문 3개 해금 안내, 등록 이력이 없을 때 재벌 +10·비리 +5·기관 +5 |
| HOK_KOR_civic_nationalization · 재벌의 공공 소유 전환 | 산업·사회협약 | 공공 소유 정책 spirit, 민간공장 2개, 조달 category 해금 |
| HOK_KOR_civic_break_monopolies · 독점 해체와 시민 개혁 | 산업·사회협약 | 시민 정책 spirit, 조달 category 해금 |
| HOK_KOR_civic_sunkyong_investment · 선경 원료·설비 투자 | 협력 정책 | 산업 연구 +150% 1회, 외부 민간공장 1개 |
| HOK_KOR_civic_samsung_electronics · 삼성전자 기술투자 | 협력 정책 | 전자 연구 +100% 1회, 100PP |
| HOK_KOR_civic_goldstar_mass_production · 금성 대량생산 설비 | 협력 정책 | 외부 군수공장 2개 |
| HOK_KOR_civic_labor_compact · 노동·생산 협약 | 시민 정책 | HOK_KOR_civic_production_quality: 효율 성장 +10%, 효율 한계 +10%, 초기 효율 +15% |
| HOK_KOR_civic_mass_conscription · 국민개병제 정비 | 노동·생산 협약 | 인력 100,000, 육군 경험 30 |
| HOK_KOR_civic_public_accountability · 공적 책임과 공정 인사 | 노동·생산 협약 | HOK_KOR_civic_professional_service: 신규 육군 지휘관 공격 +1·군수 +1, 부대 회복 +5% |
| HOK_KOR_civic_social_settlement · 시민 개혁의 정착 | 국민개병제 AND 공적 책임 | 산업 연구 +150% 1회, 150PP |
| HOK_KOR_civic_public_procurement · 공공 계약과 기술 승계 | 공공 소유 정책 | HOK_KOR_civic_contract_succession: 연구 +5%, 라인 변경 효율 유지 +10%; 100PP |
| HOK_KOR_civic_procurement_inspections · 조달 검수체계 | 세 정책 중 하나(OR) | 공군 경험 50, 전자 연구 +100% 1회, 항공·로켓 급행 계약 각각 해금 |

공공 소유의 민간공장 2개는 완전히 통제하는 core state 중 두 칸 이상을 사용할 수 있는 곳에 건설하며 두 공유 건물 칸을 추가한다. 적합한 state가 없으면 외부 민간공장 2개를 준다. 선경·금성은 처음부터 외부 공장을 사용한다. 주문이나 회사 MIO를 제거·대체하는 보상이 아니다.

### 정상 진행 시간과 신규 보상 누적

| 선택 경로 | 진입 포함 중점 수 / 시간 | 해당 경로와 공통 검수까지의 신규 누적 |
|---|---|---|
| 협력 + 기업 3개 + 검수 | 6개 / 210일 | 군수공장 건설 +20%, 생산 +15%; 외부 민간 1·군수 2; 산업 +150% 1회, 전자 +100% 2회; 250PP, 공군 경험 50; 주문 3개·두 급행 계약 해금; 협력 이력 미등록 시 재벌 +10·비리 +5·기관 +5 |
| 시민 + 노동·개병·책임·정착 + 검수 | 7개 / 245일 | 기본 소비재 계수 +5%, 안정도 +10%, 연구 +5%, 징병 인구 +2%p, 생산 +10%, 효율 유지 +15%; 효율 성장/한계 +10%, 초기 효율 +15%; 신규 지휘관 공격/군수 +1, 회복 +5%; 인력 100,000; 산업 +150%·전자 +100% 각 1회; 300PP, 육군 경험 30·공군 경험 50 |
| 공공 소유 + 기술 승계 + 검수 | 4개 / 140일 | 생산 +15%, 민간공장 건설 +15%, 연구 +5%, 효율 유지 +10%; 민간공장 2; 전자 +100% 1회; 250PP, 공군 경험 50; 두 급행 계약 해금 |

진입에서 정책 선택까지는 70일, 진입·정책·공통 검수까지는 105일이다. 시민 정착은 양쪽 후속이 모두 필요하므로 검수 없이 진입부터 210일이다. 전체 가지의 13개를 같은 게임에서 모두 완료할 수는 없다. 위 누적은 세력 tier·기존 spirit·비리·사고·정변을 제외한다. 정치력은 즉시 지급 보상의 합이며 일일 정치력 증가로 바꾸어 해석하지 않는다. 이 기간은 진입 이후 신규 모듈 내부의 소요이며 민주 정치 선행을 완료하는 시간은 별도다.

## 8. 결정 category와 조달 공통 제한

HOK_KOR_civic_balance는 패널 flag 이후 보인다. HOK_KOR_procurement_integrity는 패널 flag와 세 정책 중 하나의 flag가 모두 있을 때 보인다. 따라서 진입 중점은 첫 category만, 정책 중점은 조달 category를 명시적으로 해금한다. 조달 검수체계 중점은 분야별 flag HOK_KOR_air_procurement_unlocked와 HOK_KOR_rocket_procurement_unlocked 및 두 unlock_decision_tooltip을 제공한다.

기존 KOR_jaebeol_category의 삼성·현대·선경주문은100PP·90일·기존수정치·재사용규칙과category original_tag=KOR를 유지한다. visible/available은 새산업협력완료 OR 기업협력이력등록 OR 구재벌협력완료 OR 길들이기완료다. 새협력 주문안내와 조달category안내는 별개다. 구완료A즉시표시를4410전체재시작으로 확인했고 A와자연새협력경로에서 원래3주문을각100PP/90일로 실제사용했다. 세타이머 감소·만료 뒤재활성·자연삼성100PP 재사용도 관측했다. 정확만료순간·국가총modifier제거·현대/선경2회사용·길들이기 실제사용은 별도다. 삼성연구10%/프로젝트5%, 현대조선소10%, 선경합성석유50%/정제소건설20%는 실제개별tooltip이며 국가전체합계 실측이 아니다.

급행 계약은 재벌 영향력 40 이상, 정책 선택, 항복하지 않은 KOR에 한정한다. 두 분야는 HOK_KOR_procurement_contract_cooldown 365일을 착수일부터 공유한다. 진행 중인 계약 또는 조사·복구가 있으면 다른 계약도 시작할 수 없다. 항공·로켓 사고 spirit 중 하나라도 남아 있으면 새로운 급행 계약을 시작할 수 없다. 독립 감사는 별도 작업이며 기존 계약의 경고·사고를 자동으로 지우지 않는다.

| 결정 ID | 비용 | 기간·대기 | 주요 기능 |
|---|---:|---|---|
| HOK_KOR_independent_procurement_audit | 100PP | 60일 작업, 완료 후 180일 대기 | 완료 시 비리 -12, 기관 장악 -5 |
| HOK_KOR_fast_track_air_contracts | 75PP | 두 분야 공통 365일 대기 | 항공 급행 혜택, 비리 +10, 기관 장악 +5, 30~45일 뒤 경고 |
| HOK_KOR_fast_track_rocket_contracts | 75PP | 동일 | 로켓 급행 혜택, 비리 +10, 기관 장악 +5, 30~45일 뒤 경고 |
| HOK_KOR_recover_air_procurement | 150PP | 60일 작업 | 항공 사고 해제, 비리 -10, 기관 장악 -5 |
| HOK_KOR_recover_rocket_procurement | 150PP | 60일 작업 | 로켓 사고 해제, 비리 -10, 기관 장악 -5 |
| HOK_KOR_secure_prosecutorial_records | 150PP | 45일 작업, 위기 중 사용 | 기관 장악 -15, 365일 증거 보전 flag |
| HOK_KOR_break_capture_networks | 200PP | 60일, 1회 | 착수 안정도 -5%p; 완료 기관 -25, 비리 -10, 시민 +5; 월간 개혁 저항 종료 |
| HOK_KOR_restore_civilian_mandate | 200PP | 90일, 국정 장악 상태와 시민 영향력 50 이상 | 기관 -30, 비리 -10, 안정도 +5%p, 시민 정책 기본 혜택 회복, 개혁 저항 종료 |
| HOK_KOR_prosecutor_coup_countdown | 클릭 불가 mission | 경고 이후 90일 | 기한 안에 기관 장악 <60 또는 증거 보전 필요 |

지원·견제 네 결정까지 합하여 이 파일은 결정·mission 13개를 정의한다. independent audit의 cooldown은 완료일부터, 급행 계약의 공통 cooldown은 착수일부터 적용한다. 조사나 사고 복구가 끝나도 365일 계약 대기기간을 지우지 않는다.

## 9. 항공·로켓 특혜 → 징후 → 사고·조사·은폐·회복

| 분야 | 급행 spirit / 최대 지속 | 혜택 | 사고 spirit / 지속 피해 |
|---|---|---|---|
| 항공 | HOK_KOR_fast_air_procurement / 180일 상한 | air_equipment 연구 +15%; small_plane_airframe와 cv_small_plane_airframe 생산 비용 -20% | HOK_KOR_air_procurement_accident: 항공 사고 위험 +25%, 임무 효율 -15%, 공군 경험 획득 -10% |
| 로켓 | HOK_KOR_fast_rocket_procurement / 180일 상한 | rocketry 연구 +20%; 로켓 특별 프로젝트 속도 +25% | HOK_KOR_rocket_procurement_accident: rocketry 연구 -30%; 로켓 특별 프로젝트 속도 -25% |

180일은 timed idea의 상한이다. 정상 사건 흐름에서는 조사 또는 사고 시 급행 spirit을 즉시 제거하므로 180일 내내 받는 보상을 보장하지 않는다. 로켓 피해는 일반 연구 전체가 아니라 rocketry 및 sp_tag_rocket_speed_factor에 한정한다. 항공 사건은 한국화약의 가상 항공용 화약·탄약 급행 공급과 컨소시엄의 검수 누락이 격납고 폭발·비행대 피해로 이어지는 서사다. 한국화약을 항공기 제조기업으로 바꾸지 않는다. 비행대 피해는 위 분야별 운용 부담으로 추상화하며, 임의의 stockpile 장비 ID로 일정 수량의 비행기를 삭제하지 않는다.

1. 75PP 계약을 시작하면 active flag와 365일 공통 cooldown을 설정하고 비리 +10·기관 장악 +5를 기록한다.
2. 30일 + random_days 15 후 분야별 경고 사건을 예약한다. 예약 시점과 실제 날짜 분포의 엔진 관측은 검증 기록에 남긴다.
3. 경고에서 100PP 독립 조사를 선택하면 active flag를 지우고 급행 혜택을 즉시 종료한다. 해당 recovery flag를 켜 60일 검증을 진행한다. 사고는 예약하지 않는다.
4. 경고를 묵살하면 비리 +5, 15일 + random_days 30 후 사고를 예약한다. 앞선 계약 지연과 합하면 명세상 착수 후 45~90일이다. 사고의 무작위 확률을 굴리는 구조가 아니다. 묵살한 active 계약은 지연 후 사고로 이어진다.
5. 사고는 급행 혜택을 제거하고 해당 사고 spirit, 비리 +10, 즉시 안정도 -5%p를 적용한다. 공개에는 75PP와 비리 -5·시민 +5, 은폐에는 보상금 50PP와 비리 +10·기관 장악 +5를 추가한다. 어느 선택도 사고 피해 자체를 즉시 없애지 않는다.
6. 사고 이후 해당 복구 결정 150PP·60일을 마친다. 경고 단계에서 조사했을 때와 같은 분야별 검증 완료 사건이 해당 사고 spirit 및 recovery flag를 해제하고 비리 -10·기관 장악 -5를 적용한다. 다른 분야의 사고와 계약 공통 cooldown은 유지된다.

계약 active/recovery flag와 사고 spirit 검사가 예약 사건을 조건에 맞춰 실행하고 반복 사용을 제한한다. 정치력 보상 은폐 → 무료 재계약 → 무료 비리 회복으로 무제한 순환할 수 없도록 비용, 공유 slot과 365일 대기를 함께 둔다.

| 사건 ID | 기능 |
|---|---|
| HOK_KOR_CIVIC.1 | 항공용 화약·탄약 안전 경고: 독립 조사 / 묵살 |
| HOK_KOR_CIVIC.2 | 격납고 폭발·비행대 피해: 공개 / 은폐 |
| HOK_KOR_CIVIC.3 | 항공 조사·복구 완료 |
| HOK_KOR_CIVIC.11 | 추진제 안전 경고: 독립 조사 / 묵살 |
| HOK_KOR_CIVIC.12 | 한국화약 추진제 폭발: 공개 / 은폐 |
| HOK_KOR_CIVIC.13 | 추진제 조사·복구 완료 |

## 10. 개혁 기관 반격과 검찰 정변

정변 경고는 시민 개혁 정책, HOK_KOR_civic_reform_pressure, 기관 장악 60 이상이 함께 있을 때만 월간 검사에서 예약한다. pending/active/cooldown/국정 장악 flag가 있으면 새 위기를 예약하지 않는다. 다른 두 정책이나 정책 미선택 상태에서 시민 개혁 정변을 자동 발생시키지 않는다.

숨김 사건 20은 pending flag를 먼저 지운 뒤 조건을 다시 확인한다. 예약 후 조건이 사라져도 pending flag가 영구히 남지 않는다. 조건이 맞으면 active flag, 압박 spirit, 90일 mission을 설정하고 가시 경고 사건 24를 보낸다. 압박 spirit은 정치력 획득 계수 -15%, 안정도 -5%다.

mission의 취소 조건은 기관 장악 60 미만 OR 증거 보전 완료 flag OR 시민 정책이 더 이상 선택되지 않은 경우다. 성공하면 압박 spirit과 active flag를 해제하고 365일 정변 cooldown, 저지 사건 21을 준다. 증거 보전은 현재 위기를 막는 대응이며, 기관 해체는 월간 개혁 저항을 끝내는 별도 장기 개혁이다. 선택한 대응은 남은 기한 안에 완료해야 한다. 착수만으로 기한이 연장되지 않는다.

90일 timeout은 압박 spirit을 국정 장악 spirit으로 바꾸고 즉시 안정도 -10%p를 적용한다. HOK_KOR_prosecutorial_takeover와 HOK_KOR_prosecutorial_takeover_idea는 정치력 일일 -1, 안정도 -15%, 연구 -10%를 적용한다. sync는 시민 산업 협약의 기본 HOK_KOR_civic_reform만 중단한다. 세력 tier 및 이미 얻은 품질·전문 군 인력 후속, 기존 한국 spirit은 유지한다.

이 정변은 행정 집행·예산이 가상의 검찰 권력망에 장악된 상태다. 기존 군사 쿠데타 사건, 군 지도자 승격, 기존 정당·지도자 변경을 호출하지 않는다. 국정 장악 후 시민사회 영향력 50 이상을 유지하고 시민적 위임 회복 200PP·90일을 완료하면 해당 spirit·flag를 지우고 시민 정책의 기본 혜택을 복구한다. 동시에 기관 -30, 비리 -10, 즉시 안정도 +5%p, 개혁 저항 종료와 365일 위기 cooldown을 준다.

| 사건 ID | 기능 |
|---|---|
| HOK_KOR_CIVIC.20 | 숨김 dispatcher, pending 정리와 재검사 |
| HOK_KOR_CIVIC.24 | 가시 정변 경고, 대비 결정과 90일 설명 |
| HOK_KOR_CIVIC.21 | 정변 저지 |
| HOK_KOR_CIVIC.22 | 검찰 권력망의 국정 장악 |
| HOK_KOR_CIVIC.23 | 시민적 위임 회복 |

## 11. AI와 평가 범위

새중점 기본ai_will_do factor2,협력 전쟁×3/파시즘×1.5·공공소유 공산×3·시민개혁 민주×3을 보존했다. 가중치는 특정경로완료를 보장하지 않는다. AI 구조상 고립 가설은 소스상DISPROVEN이다. 기존 역사적AI의 민주→김구→독립당이 새협약 OR선행에 닿고 신규중점 가중치는양수다. 역사적106개 우선순위목록에는 신규13개 직접참조0이므로 실제시기·정책선택·AI완주는UNPROVEN이다. 별도AI패치 없이 기존가중치를 보존했다.

지원·견제 결정 기본 factor는 0.3이며 has_political_power >99가 아니면 factor 0이다. 정치력 50 이상은 실제 가용 조건이고 AI는 더 많은 정치력을 남겨두도록 구성한 별도 조건이다. 독립 감사 factor 3은 비리 40 이상에서 ×3, 급행 계약 factor 0.3은 전쟁 시 ×3·비리 70 이상에서 0, 사고 복구 factor 10, 증거 보전 factor 20, 기관 해체 factor 5는 위기 중 ×4, 시민 위임 회복 factor 15다.

경고 선택은 조사 weight 90, 묵살 10이며 전쟁 시 묵살 weight ×5다. 조사의 PP 조건을 충족하지 못하면 묵살만 남는다. 사고 공개 80·은폐 20이며 공개 PP 조건을 충족하지 못하면 은폐만 남는다. 사건 지연에 random_days를 쓰며 추가적인 사고 확률 random_list를 두지 않는다. 장기 AI 자금 관리·정책 경로 완주·월간 부패 유지·위기 방어의 실제 성공률은 별도 플레이 검증 대상이다.

## 12. DLC·그림·초상 재사용

항공 장비 키는 target-version plane_airframes.txt의 현재 small_plane_airframe/cv_small_plane_airframe을 사용한다. Britain national spirit의 equipment_bonus에도 같은 family가 쓰인다. 이 정의의 생산 조건에는 BBA 보유 여부 분기가 없다. 과거 fighter_equipment 루트는 현재 설치본에서 주석으로 남아 있어 신규 계약에 넣지 않았다. air_equipment 연구와 항공 사고·임무·경험 modifier는 country idea에서 적용한다. 이는 현재 소스에 근거한 선택이며 BBA 비활성 실제 생산라인에 비용 -20%가 반영되는지와 모든 구성을 엔진에서 확인했다고 주장하지 않는다.

로켓 country modifier sp_tag_rocket_speed_factor와 research_bonus rocketry는 installed CZE_vladimirs_rocket_program 예제를 대조했다. 로켓 연구 보너스/부담은 일반 기술 분야에 남으며, 해당 특별 프로젝트를 사용할 수 없는 DLC 환경에서 특별 프로젝트 보너스를 별도 PP·일반 연구로 치환하는 자동 보상은 추가하지 않았다. DLC 미보유 시 프로젝트 항목의 비활성·표시 및 음수 rocketry 체감은 검증 기록에서 별도로 확인한다. MIO를 새로 강제 생성하거나 AAT를 새 필수 의존성으로 추가하지 않는다.

최초 시스템 구현에서는 새 비트맵을 생성하지 않았다. 선경·삼성전자·금성 기존한국그림, project-owned idea/decision 소형sprite와 한국초상을 재사용한다. category51×40·decision32×32자산을 직접참조한다. 초상은11character·2name(Deoksugung Pyeonguihoe·Gim Teuleo)의 고정GFX매핑, 이름은`[ROOT.GetLeader]`, 직위는정부조건이다. 민주6명 실제표시는 이승만초기·김구정상교체/자연저장전체재시작·추가4명role fixture 뒤정치창/재열기패널의 초상·이름·대통령 일치로 확인했다.4명 정상선출/각저장재시작·열린패널 교체순간은 미검증이다. 미등록fallback은empty.dds이며 임의지도자/동일인물다른초상 자동추적을 보장하지 않는다. 지도자매핑/초상자산수정은없고 상세는 [지도자 표시 절](HOK_KOREAN_CHAEBOL_CIVIL_SOCIETY_REVISION_PLAN.md#6-지도자-초상이름직위의-현재-대응-범위)을 따른다.

2026-10-12 후속 아이콘 변경에서는 전용 category51×40와 지원·견제4개 공통 blue decision32×32 DDS를 재구성해 `interface/HOK_KOR_civic_decisions.gfx`로 연결했다. 배지는 기존 산업·사회협약 소재, 저울은 분리된 민주 팔레트RGB(53,91,126) 배경을 쓴다. 기존 공용 빨간 그림·지도자·패널·중점·로직은 유지한다. 소스19/0 및 선택된 실제 UI 상태의 전체 재시작 확인, 외부 fixture 정리와 출처는 [아이콘 구현 기록](incidents/2026-10-12-korean-civic-decision-icons.md)과 [전용 매니페스트](data/HOK_KOREAN_CIVIC_DECISION_ICON_MANIFEST.json)를 따른다.

UI 4개 및 사건 2개 원본 DDS는 변경하지 않고 프로젝트 경로로 복사해 고유 sprite로 연결했다. 다음 6개는 작성 시 설치본과 byte-for-byte 동일함을 확인했다.

| 설치본 원본 | 프로젝트 복사 대상 |
|---|---|
| gfx/interface/tiles/tiled_window_thin_border2.dds | gfx/interface/HOK_KOR/civic/tiled_window_thin_border2.dds |
| gfx/interface/tiles/tiled_window_small.dds | gfx/interface/HOK_KOR/civic/tiled_window_small.dds |
| gfx/interface/pol_leader_frame.dds | gfx/interface/HOK_KOR/civic/pol_leader_frame.dds |
| gfx/interface/button_94x31.dds | gfx/interface/HOK_KOR/civic/button_94x31.dds |
| gfx/event_pictures/report_event_fighters.dds | gfx/event_pictures/HOK_KOR/civic/report_event_fighters.dds |
| gfx/event_pictures/report_event_generic_parliament.dds | gfx/event_pictures/HOK_KOR/civic/report_event_generic_parliament.dds |

새 사건 sprite는 GFX_HOK_KOR_civic_event_fighters와 GFX_HOK_KOR_civic_event_parliament다. 로켓 사건의 GFX_report_event_K002는 기존 프로젝트 정의를 그대로 사용한다. 원본 그림의 신규 제작자라고 기재하지 않는다.

## 13. 실제 구현과 연구 초안의 차이

- 재벌·시민 영향력은 합계 100의 시소가 아니라 독립 0~100 변수다. 비리·기관 장악도 독립적이며 초기화·정책 변경으로 지워지지 않는다.
- 영향력은 UI와 함께 25/50/75 네 단계로 확정했다. 초기에 검토한 30/70 세 단계는 최종 코드가 아니다.
- 항공 스캔들은 한국화약의 가상 항공용 화약·탄약 급행 공급과 납품 컨소시엄의 검수 누락에 따른 격납고 폭발이다. 한국화약을 항공기 제조기업으로 대체하지 않으며 실제 한화 회사의 역사적 비리나 사건을 주장하지 않는다. 한국화약 추진제 폭발도 별도의 가상 사건으로 구현하여 로켓만의 비리·폭발 구조에 한정하지 않는다.
- 사고는 비리 수치에 비례하는 무작위 발생 확률이 아니다. 유료 급행 계약 선택 → 무작위 지연의 경고 → 묵살하면 지연 후 확정 사고다. 독립 감사는 분야 경고를 지우지 않으며 조사·복구는 각 분야 상태를 해소한다.
- 실존 검찰·실존 회사와 연결된 실제 정변을 확인한 donor source는 없다. 검찰 권력망의 반격은 이 모드의 신규 서사와 상태 시스템으로 구현했다.
- 국유화는 설비와 기술 승계를 함께 보상한다. 기존 기업 주문·보상·MIO를 제거하지 않으며 새 회사 아이콘을 만들지 않는다.
- 지상군 납품 품질, 해군 조달 스캔들, 세부 무기별 손실, 추가 지도자 초상 매핑은 확장 후보다. 현재 군수공장 생산 비리 부담을 별도의 지상·해군 사고 체인이나 조선소 출력 부담이 구현된 것으로 세지 않는다.

## 14. 소스 파일, 정적 증거와 검증 기록

이번 상태 본체는 scripted effects 18개, triggers 5개, ideas 20개, 결정·mission 13개, category 2개, events 11개를 정의한다. 아래 두 state localisation은 각각 108키, UTF-8 BOM, locale header 직후 동일 contributor note를 사용한다. English 파일의 본문은 기존 프로젝트 paired 관례에 맞춰 한국어 문안을 유지한다.

| 상태 본체 파일 | 역할 |
|---|---|
| [common/scripted_effects/HOK_KOR_civic_effects.txt](../common/scripted_effects/HOK_KOR_civic_effects.txt) | seed·clamp·tier·정책·공통 행동·legacy·월간 변화 |
| [common/scripted_triggers/HOK_KOR_civic_triggers.txt](../common/scripted_triggers/HOK_KOR_civic_triggers.txt) | 정책·버튼·공통 조달 slot·정변 자격 |
| [common/ideas/HOK_KOR_civic_ideas.txt](../common/ideas/HOK_KOR_civic_ideas.txt) | 영향력·정책·후속·비리·분야별 특혜와 사고·정변 |
| [common/decisions/HOK_KOR_civic_decisions.txt](../common/decisions/HOK_KOR_civic_decisions.txt) | 13개 지원·감사·계약·복구·기관 대비·정변 mission |
| [common/decisions/categories/HOK_KOR_civic_categories.txt](../common/decisions/categories/HOK_KOR_civic_categories.txt) | 진입 및 정책별 category 공개 |
| [events/HOK_KOR_civic_events.txt](../events/HOK_KOR_civic_events.txt) | HOK_KOR_CIVIC namespace의 경고·선택·피해·복원 |
| [common/on_actions/HOK_KOR_civic_on_actions.txt](../common/on_actions/HOK_KOR_civic_on_actions.txt) | startup/monthly country callback |
| [localisation/korean/HOK_KOR_civic_state_l_korean.yml](../localisation/korean/HOK_KOR_civic_state_l_korean.yml) | 상태·idea·결정·사건 문안 |
| [localisation/english/HOK_KOR_civic_state_l_english.yml](../localisation/english/HOK_KOR_civic_state_l_english.yml) | paired locale |

중점·UI 통합 소스는 korea.txt, 기존 주문 KOR_decision.txt, 호환 ID HOK_KOR_civic_legacy_focus.txt, HOK_KOR_civic_focus.gfx, HOK_KOR_civic_influence.gfx/.gui, common/focus_inlay_windows/HOK_KOR_civic_influence_inlay_window.txt, common/scripted_localisation/HOK_KOR_civic_influence_scripted_loc.txt, HOK_KOR_civic_events.gfx 및 별도 focus/UI paired localisation이다.

UI paired localisation에는 기존18+구·신공용기업협력이력1=19긍정상태명key를 추가했다. 각각60키·UTF-8 BOM·CRLF·동일note·English UI영문대응이며 기존NOT/정책OR/정치력≥50·비용/기간/보상/AI를 보존했다. 실제한글tooltip은 공통3+정책3+감사2+계약/복구5+기관/증거/회복5+이력1=19종 모두최소1회표시했다. 자연GUI/주문과합성disabled-tooltip의 표시종류집계이며19gameplay통과·모든참/거짓조합·영문UI·정상job/event완료가 아니다. 합성PP50에서 원본시민지원50→0·60/70/18/43·90일로 이버튼의≥50경계를 확인했다. [변경 기록8절](HOK_KOREAN_CHAEBOL_CIVIL_SOCIETY_REVISION_PLAN.md#8-사용-조건-한글-표시-반영과-관측-범위)의 상세표를 따른다.

진입은 민주 기준점 KOR_democracy_advance_forward 기준 상대(6,4), 기본(133,6)이며 완료 민주 HIDE에서는 -35x를 한 번 상속하여(98,6)이다. 신규 13개 후속 좌표와 인접 상선 확대·영국함 이동은 [변경 기록 4절](HOK_KOREAN_CHAEBOL_CIVIL_SOCIETY_REVISION_PLAN.md#4-후속-가지와-민주주의-구역-배치)을 따른다. 패널은 별도 고정 UI 좌표(1050,1400), 크기500×670이며 지속적 중점 패널(200,1700)은 유지한다. 소스 좌표와 실제 표시·스크롤·클릭 검증을 분리한다.

2026-10-11 초기 상태 본체의 순서 보존 AST·호출·참조·필수 loc 연결 정적 검사 46건, country modifier 20개·재사용 sprite 17개·state paired108키·raw-copy6개 대조는 이전 소스의 기록이다. 외부 C:/hoi/test/civic-influence-20261011/static-report.json의 1599 PASS/0 FAIL 및 clean-initial 초기 한국 로드는 개정 전 473개 소스의 증거이며 이번 개정에 전용하지 않는다.

이번개정 정적증거는revision-static-review.json82/0·layout-current-review.json구조498/0/40정적모델비관련후보0이며 모델은렌더링을 대신하지 않는다. 외부루트 C:/hoi/test/civic-revision-20261012의RUNTIME_OBSERVATIONS.md와[incident](incidents/2026-10-12-korean-civic-revision.md)에7874/4410단계별관측을 누적했다. 초기blocked-phase보호75/0은 과거게임미실행단계다. 4410에서 구 완료 A의 즉시 주문 표시와 A 재로드 후 월간 비중복을 확인했다. 합성 fixture 없는 자연 독립당 경로로 협약·산업협력을 완료하고 원래 주문 3개를 각 100PP로 사용했다. 90일 타이머의 만료 후 삼성 재사용, 자연 저장의 전체 프로세스 재시작에서 93PP·70/45/23/45·공통 대기90일·주문90일·김구 유지도 관측했다. SHOW 민주 중점 전후의 같은 카메라15점 유지, 한글 상태명19종의 최소1회 tooltip 표시, 등록 민주6명의 제한된 표시 범위를 확인했다. startup 즉시 등록·모든 기존 저장의 일반 호환, 정확150PP delta·정확 만료 순간·국가 총modifier 제거·현대/선경2회 사용, 모든 표시 전환/배율/클릭·조건 참/거짓 조합·영문UI, 추가4명의 정상 선출/저장재시작·열린 패널의 연속 갱신, 장기AI·DLC 차이·멀티플레이는 미검증이다. 최종 원본71저장metadata 보호와 설정 기능복귀는 확인했으며 settings byte복원 제한은 최종절을 따른다. 자연게임05.31부터UIautosaveNEVER로 임시전환했고 이후반년UI복귀/원본settingsSHA를 한차례확인했으며 새save외부복사/해시거절을 재시도하지 않고 원래위치Load로 진행했다. 저장내용 비교를 주장하지 않는다.

autosave는 UI에서 반년으로 Apply하고02.08.04 정상Quit/process0 뒤 원본settings SHA332B… 복귀를 확인했다. 이후 HoK only·disabled_dlcs빈배열·진단loader제거·HALFYEAR를 적용했으나 frontend 종료에서 엔진의loading-screen2배열 재기록으로 settings SHA26B…가 됐다. 당시 UI 복귀·최종복구 대기와 아래 최종감사의 원본71보호·설정 기능복귀·settings byte복원 제한을 구분한다.

DLC 비활성 프로필 시도는 debug/비debug 전체 재시작 모두 frontend-only(SP world0)였고 system은36DLC·2mods·4410을 계속 열거했다. 따라서 DLC 비활성 gameplay 통과가 아니다. 일부 DLC asset/BLT validation 차이 때문에 JSON 완전 무시를 단정하지 않으며 원인은UNPROVEN이다. debug 제거만으로 해결된다는 가설도 지지되지 않았다. debug151행/63그룹·비debug147행/59그룹은 gameplay 통과수/새civic 오류수가 아니다. 로그는 runtime-no-dlc-attempt-debug/logs와normal/logs에 보존했고상세는[incident](incidents/2026-10-12-korean-civic-revision.md)를 따른다.

정적 검사는 엔진 로드·효과 실행·UI·정상 날짜 진행을 대신하지 않는다. 실제 발견/등록/실행/표시, 지원·견제의 정확한 PP 경계, 기존 저장 멱등성, 경고·사고·복구의 날짜, 90일 정변 성공·실패·회복, 일반 진행·장기 AI·DLC 비활성·멀티플레이와 save 검증의 완료 여부는 검증 기록에서 각각 구분한다. 본 명세는 아직 관측하지 않은 경우를 통과로 기록하지 않는다.
