# 한국 재벌·시민사회 내정 — 진입·주문·배치·지도자 표시 변경 기록

작성일·갱신일: 2026-10-12 (Asia/Seoul). 상태: **소스·정적 확인 / 4410 독립당·d2e6 자유당 정상 접근·산업협력·주문 / 4410 저장 재시작·90일·SHOW·한글19종·민주6명 표시 / 원본71보호 확인·설정 기능 복귀 / settings byte복원 제한·AI/DLC/MP 미검증 / 추가 아이콘 소스 적용·575f/2430 표시 확인**.

처음에는 설명·문서화만 허용된 변경 계획이었다. 이후 사용자가 앞선 진입·주문·배치·한글 개정의 구현을 명시 승인하여 해당 내용을 소스에 반영했다. 추가 디시전 아이콘은 최초 문서화 뒤 사용자가 구현을 승인했다. 최초 요청과 적용·검증 결과를10절에서 구분한다. [현행 구현 명세](HOK_KOREAN_CHAEBOL_CIVIL_SOCIETY_SPEC.md)와 [이번 개정의 유지보수 기록](incidents/2026-10-12-korean-civic-revision.md)을 함께 읽는다. 문서 갱신 자체는 게임 실행, 사용자 설정 변경, Git 변경이나 배포를 수행하지 않는다. 과거 실행 결과와 이번 소스의 검증 결과를 합산하지 않는다.

## 2026-10-12 최종 런타임·원본 보호 확인

진단 없는 d2e6 자유당 게임을 1936.06.07.09에 정상 종료했다. 초기와 종료 직전 오류 내용은 같았고, 해당 내정·주문·구 ID를 직접 가리키는 오류는 없었다. 종료 후에는 기존 random.log 이름 변경 실패 2행이 추가됐다. 정상 진행·합성 표시 검사·정적 확인을 구분한 결과를 외부 `TEST_REPORT.md`와 [최종 기록](incidents/2026-10-12-korean-civic-revision.md)에 정리했다.

등록된 구 완료 저장 B도 d2e6 소스만으로 재저장하고 전체 재시작해 불러왔다. 1936.03.08.23·정치력45·70/35/25/45·세 기업 주문 표시와 잠긴 관리 기능이 유지됐고, 다음 월04.11.05에도 수치가 중복 증가하지 않았다. 초기 구 저장의 누락된 진단 디시전 경고는 재저장 파일에서 재발하지 않았다. 이 한 사례를 일반 저장 호환으로 확대하지 않는다.

기존 저장 71개의 이름·크기·정밀 UTC 수정 시각 차이는 0이다. 신규 테스트 임시 저장 총5개는 보존했고 진단 로더는 제거했다. 모드 목록과 기존 런처 파일의 원본 해시는 일치한다. 자동저장 반년·해상도·창 모드 등 설정은 원본과 같지만, 게임이 같은 로딩 화면 28개의 순서를 바꿔 settings.txt 해시가 다르다. 백업으로 덮어쓰기는 Windows 접근 거부로 실패했다. 설정 기능 복귀와 파일 전체의 byte 일치를 구분하며, 보안 설정을 변경하지 않았다.

실제 한국 AI 선택·DLC 비활성 게임·멀티플레이, 모든 기존 저장의 일반 호환과 모든 표시 조합 등은 미검증이다. 기존 저장 보호 확인을 전체 저장 호환 통과로 해석하지 않는다.

## 1. 현재 소스와 기록의 구분

- 브랜치: `feat/korean-focus-expansion-ai`; HEAD: `4d8241e3cd33ebbceaca9650ab36b9891a22b56d`. 기존 수정·미추적 개발 파일을 보존한 작업 트리이며 이번 개정은 미커밋 상태다.
- 개정 전 한국 트리는 473개였다. 현재 플레이 가능한 한국 트리는 **472개**이며 신규 내정 13개를 유지하고 구 협력 노드 한 개를 제거했다. 구 ID는 트리에 가져오지 않는 호환용 `shared_focus` 한 정의로 남겼다. 전역 정의 수와 플레이 가능한 트리 수를 혼동하지 않는다.
- 열람 시 `common/national_focus/korea.txt` SHA-256: `36e90bfdbefc1980dad83131745ed00bc4a7a3e33be11f8504c7234cadbc420a`; 개정 전: `e9f96c856982a5ba32b05e5e77cadc782340e294c542c15bab095c80e91c729e`.
- 열람 시 `common/scripted_effects/HOK_KOR_civic_effects.txt` SHA-256: `a114abeea79ac284cdef5d62e0d88ddb232ef5b43beda94e4e991923742151db`; 개정 전: `a348483591cadcb6ecd5414e68bc2c8455da9eb255e834335084dcd295cf5a67`.
- 아래 조건·격자 좌표·매핑과 보존 사항은 소스·정적 근거다. 별도로 표시한 runtime 관측은 엔진UI와 정상/합성 진행의 실제 증거이며 두 종류를 구분한다.

| 요청·검토 항목 | 소스 반영 상태 | 남은 확인 |
|---|---|---|
| 새 재벌 산업협력 완료로 주문 3개 해금 | 구 완료A 즉시 표시·자연 새 협력 뒤3개 실제100PP 사용·90일 뒤삼성 재사용 | 길들이기 실제 사용·국가 총modifier 제거·현대/선경2회 사용 |
| 구 협력 노드 제거, 산업·사회협약으로 자리·선행조건 교체 | 민주anchor(6,4)·단독집권OR; 독립당/자유당 두 정상 경로의 협약/새협력/주문 | 정확150PP delta·남은정책/후속 진행 |
| 민주 구역의 후속 배치와 인접 공간 정리 | 자연0.65화면13개/상선/영국함; SHOW 민주 전후 같은 카메라15점 유지 | 모든 표시 전환·배율·전체 클릭·남은 후속 진행 |
| 구 협력 보상·저장 연결 | A/B 월간 비중복·A 월간 저장Load 뒤다음월70/35/25/45 유지 | startup 즉시 등록·모든 기존save 일반 호환 |
| 민주 지도자 교체 시 패널 갱신 | 이승만 초기·김구 정상/전체재시작·4명role fixture/패널재열기로6명 일치 | 4명 정상 선출/저장재시작·열린 패널 연속 갱신·임의/다른초상 |
| 영향력 패널 하향 배치 | inlay(1050,1400); A 두카드/버튼/하단문구 접근·합성고무 여유 | 모든 배율/스크롤·지속중점과 전체 접근 |
| 사용 조건 한글 표시 | 19종 distinct 상태명 실제한글tooltip·합성 시민지원 정확50PP 사용 | 모든 참/거짓 조합·영문UI·다른버튼 경계 |

## 2. 삼성·현대·선경 주문의 해금 이관

사용자가 요청한 **재벌과의 산업협력**(`HOK_KOR_civic_chaebol_cooperation`) 완료 경로로 주문을 연결했다. [기존 디시전](../common/decisions/KOR_decision.txt)의 세 결정 각각 `visible`과 `available`, 총 **6곳**의 OR는 다음 네 접근 경로다.

1. `HOK_KOR_civic_chaebol_cooperation` 완료
2. `HOK_KOR_legacy_cooperation_registered` — 기업 협력 이력 등록
3. 구 `KOR_cooperation_with_the_jaebeol` 완료 — 월간 등록 전에도 직접 접근
4. 기존 `KOR_taming_the_jaebeol`(재벌 길들이기) 완료

| 주문 | 유지한 ID | 실제 시작 관측 | 툴팁의 기존 수정치 |
|---|---|---|---|
| 삼성에 지시 하달 | `KOR_order_to_samsung` | A1000→900; 독립당443→343/만료뒤170→70; 자유당308→208·각90일 | 연구+10%·특별프로젝트+5% |
| 현대에 지시 하달 | `KOR_order_to_hyundai` | A900→800; 독립당343→243; 자유당208→108·각90일 | 조선소 생산+10% |
| 선경에 지시 하달 | `KOR_order_to_sk` | A800→700; 독립당243→143; 자유당108→8·각90일 | 합성 석유+50%·정제소 건설+20% |

주문 ID·이름·기존 `KOR_jaebeol_category`, 수정치·재사용 규칙은 보존했다. category의 `original_tag = KOR` 조건도 그대로다. 새 협력 완료 효과에는 위 세 ID의 `unlock_decision_tooltip`을 추가했으며 기존 조달 category 안내도 유지했다. 재벌 길들이기의 기존 해금 안내·보상은 변경하지 않았다. 새 독점 해체나 공공 소유 완료 자체는 주문의 새로운 해금 경로가 아니다. 구 완료·기존 협력 이력·길들이기가 남은 저장에서는 그 경로가 계속 적용될 수 있다.

7874 A는 로드 직후 구 완료TRUE·등록flag없음에서 주문3개가 숨겨지고 첫 월간 뒤 복구되는 회귀가 있었다. 6개OR에 구 완료 직접조건만 추가하고 기존3경로·비용·기간·효과·AI·note를 보존했으며 기대OR4경로의 기존정적82/0을 재통과했다.7874 B는 debug DB자동재로드 때문에 수정 전 주문소스라고 단정하지 않는다.4410 전체재시작의 원래A/02.16.15·PP21·준비0에서는 월간 전 주문3개가 즉시 표시되고 삼성4경로 툴팁을 확인했다. 패널60/35/20/40·협약잠금도 유지됐다.

4410의 원래A(02.16.15/PP21)에서 즉시 표시를 확인한 뒤, 같은 프로세스의 게임 내Load로 월간 후 새A 저장(03.06.16)을 원래 위치에서 불러왔다. 준비0에서70/35/25/45·PP43·협약잠금·이승만이 유지됐다. PP-only `exact_pp1000`1회 아래 원래3주문을1000→900→800→700PP로 사용했고, Load 뒤04.11.07의 다음월에도 상태를 유지했다. 세90일 타이머의 감소와06.05.21 재활성 표시를 확인했으나 정확 만료 순간·국가 총modifier 제거는 관측하지 않았다.

별도의 fixture 없는 자연 campaign에서는 독립당→협약→새 산업협력을 정상 완료한 뒤10.06.20에 원래3주문을443→343→243→143PP·각90일로 사용했다. 자연 저장의 전체 프로세스 재시작에서 세 타이머를 유지했다.12.30.20에는GUI와주문 잔여5일,01.17.02에는GUI 재사용 가능 문구를 처음 관측했다. 주문 시계 소멸과 삼성100PP 재사용은01.22.03에 확인했다. 현대/선경은 active clock이 없고100PP만 부족했으나 두 번째 사용은 하지 않았다. 정확 만료시각·국가 총modifier 수치 제거는 별도다. 단계·원본보호는 [유지보수 기록](incidents/2026-10-12-korean-civic-revision.md)을 따른다.

진단mod·fixture·정치력forcing 없는 d2e6(HoK1mod·36DLC·debug, 역사적AI/HIDE)에서 자유당 정상선행→협약→산업협력을 완료했다. 협약 OR는 자유당초록/독립당빨강·산업화조건없음·150PP/category안내였고 패널60/35/20/40→70/35/25/45를 관측했다. 다음월06.07.09에도 같은상태에서 원래삼성/현대/선경을308→208→108→8PP·각90일로 실제사용했다. 이d2e6의주문만료·저장/reload는 실행하지 않았으며 앞선4410독립당게임의 증거와구분한다. 정확완료순간·순수150PPdelta를 역산하지 않는다. 최종 원본71metadata보호·프로필2파일 byte일치·설정 기능복귀는 확인했고 settings의 로딩화면 순서 byte복원 제한은 아래 최종절에 기록한다.

## 3. 구 재벌 협력 자리에 산업·사회협약 배치

구 **재벌과의 협력**(`KOR_cooperation_with_the_jaebeol`) 노드를 한국 트리에서 제거하고 신규 **산업·사회협약**(`HOK_KOR_civic_industrial_compact`)을 그 자리에 옮겼다. 신규 **재벌과의 산업협력**은 별개의 정책 중점으로 유지한다.

| 항목 | 개정 전 | 현재 소스 |
|---|---|---|
| 선행 | `KOR_industrialized_society` | `KOR_independent_party_in_power` OR `KOR_liberal_party_sole_power` |
| 배치 기준 | 산업화된 사회 | `KOR_democracy_advance_forward` |
| 상대 위치 | `(0,1)` | `(6,4)` |
| 직접 보상 | 초기화, 패널 행동 해금, 150PP, 세력관리 category 안내 | 보존 |
| 기간·기본 AI | 35일·factor 2 | 보존 |

두 선행은 **하나의 prerequisite 블록 안에 있으므로 OR**다. 단독집권 둘을 모두 요구하거나 산업화 선행을 추가로 요구하지 않는다. 민주 기준점 기본 `(127,2)`에서 진입은 `(133,6)`이며 HIDE 완료 민주 이동 `-35x`를 한 번 받으면 `(98,6)`이다. 이 격자 해석과 별도로 자연 독립당 경로의 OR/Start·협약 완료를 관측했다. SHOW 민주 중점 진행 중/완료 뒤 같은카메라15점은 같아서 해당 -35x 이동이 없었다. HIDE 초기→완료 전환을 같은 카메라로 검증한 사례는 아니다.

진행은 **독립당 또는 자유당 단독집권 → 산업·사회협약 → 재벌 산업협력 / 독점 해체와 시민 개혁 / 공공 소유 전환**이다. 공통 산업 진입을 바꾸면서 **신규 내정 13개 전체의 새 게임 정상 접근 경로가 민주주의 정치 경로로 좁아졌다.** 다른 이념의 별도 입구를 추가하지 않았다. 이미 완료된 새 중점이나 이력 flag를 가진 저장을 강제 초기화하는 변경도 하지 않았다.

## 4. 후속 가지와 민주주의 구역 배치

진입과 신규 13개를 함께 민주 구역에 재배치했다. 아래는 상대 anchor chain을 해석한 **기본 격자 좌표**다. 민주 진입이 완료된 HIDE에서는 모두 x에서 35를 한 번 빼며 y는 같다. SHOW와 완료 전 HIDE는 기본 위치를 사용한다.

| 중점 ID | 기본 `(x,y)` |
|---|---|
| `HOK_KOR_civic_industrial_compact` | `(133,6)` |
| `HOK_KOR_civic_chaebol_cooperation` | `(133,7)` |
| `HOK_KOR_civic_nationalization` | `(135,7)` |
| `HOK_KOR_civic_break_monopolies` | `(137,7)` |
| `HOK_KOR_civic_sunkyong_investment` | `(132,8)` |
| `HOK_KOR_civic_samsung_electronics` | `(134,8)` |
| `HOK_KOR_civic_goldstar_mass_production` | `(133,9)` |
| `HOK_KOR_civic_labor_compact` | `(137,9)` |
| `HOK_KOR_civic_mass_conscription` | `(136,10)` |
| `HOK_KOR_civic_public_accountability` | `(138,10)` |
| `HOK_KOR_civic_social_settlement` | `(137,12)` |
| `HOK_KOR_civic_public_procurement` | `(135,9)` |
| `HOK_KOR_civic_procurement_inspections` | `(139,8)` |

인접 `KOR_expand_merchant_marine`은 `KOR_join_the_allie` 기준 상대 x를 `-2→0`으로 옮겼다. 그 자손 `KOR_british_naval_ship`은 자신의 상대값 `(0,2)`를 그대로 두고 상선 확대의 이동을 상속한다. 다른 정치 구역이나 전체 트리의 간격을 일괄 압축하지 않았다. 기본 전체 경계는 x0~211/y0~24다.

세 정책 배타, 시민 정착의 두 선행 AND, 공통 검수의 정책 OR, 기존 기간·보상·가용 조건·AI와 정치 offset 7개를 보존했다. 배치 anchor는 자손보다 먼저 선언하고 민주 이동을 자손별로 중복 적용하지 않는다. [배치 계획](HOK_KOREAN_FOCUS_LAYOUT_PLAN.md), [좌표 명세](HOK_KOREAN_FOCUS_LAYOUT_COORDINATES.md), [압축 사건 기록](incidents/2026-09-21-korean-focus-compact.md), [정치 압축 계획](HOK_KOREAN_POLITICAL_COMPACTION_PLAN.md)을 함께 따른다.

현재 소스의 구조 검사 **498 통과·0 실패**, 정치 상태 20개×표시 모델 2개의 정적 모델에서 비관련 겹침·선 접촉·배타선 접촉·일직선 후보 0을 기록했다. 관련 다중 부모 merge 접촉은 별도로 존재한다. 이 모델은 실제 아이콘·명판·선·숨겨진 anchor·클릭 영역이나 엔진 화면의 무겹침을 증명하지 않는다.

## 5. 협력 보상·상태·세이브 연결

`HOK_KOR_legacy_cooperation_adjustment`의 **재벌 영향력 +10·누적 비리 +5·기관 장악 +5**는 등록 flag가 없을 때 한 번 적용한다. 이 기존 helper를 새 산업협력의 완료 효과로 이관했다. 중립 진입인 산업·사회협약에는 붙이지 않았다. `HOK_KOR_legacy_cooperation_registered`는 구·신 협력 모두에서 사용하는 **기업 협력 이력 등록**이며, 구 중점에서만 온 저장이라고 해석하지 않는다.

[초기·월간 등록 효과](../common/scripted_effects/HOK_KOR_civic_effects.txt)는 구ID **OR 새 산업협력 완료** 뒤 같은helper를 호출한다. 기존 [on_actions](../common/on_actions/HOK_KOR_civic_on_actions.txt)는 수정하지 않았다. 직접 완료와 초기·월간 등록은 같은flag로 중복 가산을 막는 소스다.7874 A의 첫월60/35/20/40→70/35/25/45·두 번째월 비중복, B 등록완료fixture의 월간 비중복을 관측했다.4410 A 월간 저장Load 후04.11.07에도70/35/25/45를 유지했다. 자연 새 협력 완료도60/35/20/40→70/35/25/45와 일치했다. startup 즉시 등록·모든 기존저장 일반 호환은 미검증이다.

[호환용 정의](../common/national_focus/HOK_KOR_civic_legacy_focus.txt)는 구 ID를 `shared_focus`로 등록하되 한국 트리에 가져오지 않는다. `available = { always = no }`, AI factor 0, 빈 완료 보상으로 선택·재보상을 제공하지 않으며 기존 프로젝트 아이콘을 재사용한다. 구 노드의 설명용 기여 이력도 남겼다. 이는 **트리 노드 제거와 전역 ID 등록을 분리한 호환 시도**다. 설치 HOI4 1.19.3 shared-focus 예제에 대조했다. 외부 전버전 양성 fixture A에서 구 완료 조건 TRUE와 월간 등록을 실제 관측했지만, A 월간 후 새 저장의4410 게임 내 Load도 확인했다. B 재저장/재로드는 d2e6에서 확인했지만 모든 기존 저장의 일반 호환은 아직 입증하지 않았다.

구 완료를 새 정책 완료와 같다고 간주하지 않는다. 새 정책을 강제 선택하거나 산업·사회협약을 자동 완료하지 않으며 진입 150PP를 자동·중복 지급하지 않는다. 기존 등록 flag가 있는 저장은 주문의 이력 경로를 유지하고, flag가 없는 전버전 완료 저장은 shared ID 판정과 초기·월간 등록이 실제 성공하는지 별도로 검증해야 한다.

구 노드AI factor1을 진입에 복사하지 않았다. 진입/새협력factor2·협력 전쟁×3/파시즘×1.5는 보존했다. AI 구조상 고립 가설은 소스상DISPROVEN이다. 기존 역사적AI의 민주→김구→독립당이 새협약 OR선행에 닿고 신규중점 가중치는양수다. 역사적106개 우선순위목록에는 신규13개 직접참조0이므로 실제시기·정책선택·AI완주는UNPROVEN이다. 별도AI패치 없이 기존가중치를 보존했다.

## 6. 지도자 초상·이름·직위의 현재 대응 범위

지도자 매핑과 자산은 이번 개정에서 변경하지 않았다. 소스의11character·2name 고정 선택과 실제 민주 후보6명의 표시를 구분한다. 이승만 초기, 김구 정상 교체/자연저장 전체재시작, 안창호·윤보선·이강·여운형role fixture 뒤정치창/재열기 패널의 초상·이름·대통령 직위 일치를 관측했다.

| 표시 | 현재 방식 | 확인 범위와 한계 |
|---|---|---|
| 이름 | `[ROOT.GetLeader]` | 현재 지도자 이름을 읽는 연결 |
| 직위 | 인물·정부 조건의 scripted localisation | 민주 일반 직위는 대통령; 별도 분기 존재 |
| 초상 | 지도자 조건별 고정 GFX 선택 | 정치창의 현재 초상을 직접 복제하지 않음 |
| 미등록 지도자 | `GFX_HOK_KOR_civic_leader_unmapped` | 기존 `empty.dds`, 현재 이름·직위 |

알려진 민주 후보 **이승만·김구·안창호·윤보선·이강·여운형**은 모두 [기존 매핑](../common/focus_inlay_windows/HOK_KOR_civic_influence_inlay_window.txt)에 포함된다. 전체 초상 선택은 character ID11개(위6명, 인민위원회·박헌영·이범석·계연수·이은), 이름조건2개(Deoksugung Pyeonguihoe·Gim Teuleo)다. 추가4명은02.08.04/time0의role fixture이며 정상 선거/이벤트·각 인물 저장/전체재시작 검증이 아니다. 열린 패널의 교체순간 연속 갱신, 미등록지도자·같은인물의 다른초상 버전까지 자동 추적한다고 설명하지 않는다.

## 7. 영향력 패널의 하향 배치

사용자 화면에서 합성 고무 이름판과 패널 상단이 가까웠던 점을 반영하여 [한국 트리의 inlay](../common/national_focus/korea.txt) 위치를 **`(1050,1300)→(1050,1400)`**으로 옮겼다. [GUI](../interface/HOK_KOR_civic_influence.gui)의 `500×670` 크기와 내부 프레임·초상·명패·두 카드·버튼 위치는 보존했다. 합성 고무 중점 자체는 이 변경에서 이동하지 않았다. 지속적 중점 패널은 `(200,1700)` 그대로다.

**패널 UI 좌표와 중점 격자 좌표는 별도 설정**이다. 패널은 민주offset을 받는 자손중점이 아니며 고정inlay 위치를 유지한다. y=1400에서 A의 두카드·버튼·하단문구 스크롤 접근과 합성고무 여유를 관측했고 자연GUI 사용·지도자 패널재열기도 확인했다. 모든 배율/카메라·하단가지·지속중점과의 전체접근/무겹침을 확인한 것은 아니다.

## 8. 사용 조건 한글 표시 반영과 관측 범위

개정 전 사용자 첨부의 네 지원·견제 툴팁에서 초기화·해금·공통 대기 flag 3종의 raw 이름을 확인했다. 앞선 실행에서는 일부 기업·노동·공공 계약 후속의 정책 flag 3종도 노출되었다. 소스상의 추가 15종에는 이 정책 3종이 포함된다. 따라서 기존 검토는 **중복 없는 18개 조건명**이며 18개 화면 결함이나 전체 프로젝트 누락 총량을 뜻하지 않는다.

현재 [Korean UI locale](../localisation/korean/HOK_KOR_civic_ui_l_korean.yml)와 [English UI locale](../localisation/english/HOK_KOR_civic_ui_l_english.yml)에 기존18개+구·신 공용협력이력1개, **총19개 동일key**를 추가했다. 각각60키·UTF-8 BOM·CRLF·header 직후 동일note, 기존문자열과English UI영문대응을 유지한다. 실제한글tooltip은 공통3+정책3+감사2+계약/복구5+기관/증거/회복5+이력1=**19종 모두 최소1회 표시**됐다. 자연GUI/주문과 별도02.08.04 합성disabled-tooltip을 묶은 표시종류 수이며19gameplay 통과·모든flag참/거짓 조합·영문UI 검증이 아니다.

| 내부 조건명 | 추가한 한국어 긍정 상태명 | 개정 전 노출 근거 |
|---|---|---|
| `HOK_KOR_civic_system_initialized` | 내정 시스템 초기화 완료 | 네 버튼 실측 |
| `HOK_KOR_civic_panel_unlocked` | 세력 관리 기능 해금 완료 | 네 버튼 실측; 패널 표시 자체와 구분 |
| `HOK_KOR_civic_action_cooldown` | 지원·견제 공통 대기기간 중 | 네 버튼 실측; 실제 조건은 NOT |
| `HOK_KOR_policy_cooperation` | 재벌 산업협력 정책 선택 | 선경·삼성 실측 |
| `HOK_KOR_policy_civic_reform` | 독점 해체·시민 개혁 정책 선택 | 노동 실측 |
| `HOK_KOR_policy_public_ownership` | 공공 소유 정책 선택 | 공공 계약 실측 |
| `HOK_KOR_audit_active` | 독립 조달 감사 진행 중 | 소스상 가용 조건 후보 |
| `HOK_KOR_audit_cooldown` | 독립 조달 감사 재사용 대기 중 | 동일 |
| `HOK_KOR_procurement_contract_cooldown` | 급행 계약 공통 재사용 대기 중 | 동일; 계약 착수부터 |
| `HOK_KOR_air_contract_active` | 항공 급행 계약 진행 중 | 동일 |
| `HOK_KOR_rocket_contract_active` | 추진제 급행 계약 진행 중 | 동일 |
| `HOK_KOR_air_recovery_active` | 항공 조달 조사·복구 진행 중 | 동일; 경고의 독립 조사 포함 |
| `HOK_KOR_rocket_recovery_active` | 추진제 조달 조사·복구 진행 중 | 동일; 경고의 독립 조사 포함 |
| `HOK_KOR_record_protection_active` | 검찰 권력망 증거 보전 진행 중 | 동일; 보전 완료 상태와 구분 |
| `HOK_KOR_capture_reform_active` | 기관 장악망 해체 진행 중 | 동일 |
| `HOK_KOR_capture_reform_completed` | 기관 장악망 해체 완료 | 동일 |
| `HOK_KOR_prosecutorial_takeover` | 검찰 권력망의 국정 장악 상태 | 동일; 위기·저지와 구분 |
| `HOK_KOR_civilian_restoration_active` | 시민적 위임 회복 진행 중 | 동일 |
| `HOK_KOR_legacy_cooperation_registered` | 기업 협력 이력이 등록됨 | 이번 주문 이력 조건; 구·신 협력 공용 |

긍정 상태명은 flag가 참인 의미다. 기존 **NOT·정책OR·정치력50 이상**과 비용·범위·90/180/365일·보상·AI를 보존했다. 합성PP50에서 원본 시민지원50→0·60/70/18/43·공통90일을 실제 확인하여 이버튼의≥50경계를 검증했다.19종 표시와 일부 독립NOT색은 확인했지만 모든UI/참·거짓 조합·다른버튼 정확50효과·정상 감사/사고/기관job 완료로 확장하지 않는다.

`Focus ID`·`debug key`·이벤트 ID, visible-only·AI·숨김 조건, 내부 변수·flag 변경 효과는 누락 결함 수에 포함하지 않는다. `check_variable`의 이름이 locale에 없다는 사실만으로 툴팁 노출을 확정하지 않는다. 정변 mission 취소 조건은 기존 18개 가용 조건 집계 밖의 별도 화면 확인 항목이다. 사건창 선택지 잘림은 번역과 구분한 기존 UI 문제다.

## 9. 정적 확인, 실제 관측과 원본 보호

외부 증거 루트는 **`C:/hoi/test/civic-revision-20261012`**다. 기존 자료를 열람하여 다음 결과를 기록했다. 이번 문서 갱신은 게임·검사 실행을 하지 않았다. 앞선 주문 최소 수정 단계에서는 기존 외부 82개 정적 검사를 재실행했다.

| 증거 | 확인된 범위 | 결과 |
|---|---|---|
| `revision-static-review.json` | 주문·once 등록·참조·BOM/CRLF·기여 note·19개 paired key·보존 | 82 통과·0 실패 |
| `layout-current-review.json` | 현재 소스 구조 및 격자·직교선 후보 모델 | 구조 498 통과·0 실패; 40 정적 모델의 비관련 충돌 후보 0 |
| `coordinate-metadata-audit.json` | 현재 472개·7 absolute/465 relative·순서·좌표·역사 metadata | 17 통과·0 실패 |
| `user-protection-before.json` | 프로필 3개 SHA 및 보호 대상 저장 71개 기준 | 기준 캡처 |
| `user-protection-blocked-phase.json` | 프로필 3 SHA·저장 71 이름/길이/정밀 UTC 시간·진단 loader 부재 | 75 통과·0 실패; 게임 미실행 단계 |
| `TEST_REPORT.md` | 초기 정적 확인·ACL 차단 통합 기록 | 최신 통합보고 갱신은 root 소유 |
| `RUNTIME_OBSERVATIONS.md` | 7874/4410 정상·합성·재시작·표시의 단계별 관측 | incident와 최신 범위·대기 기록 |

초기 차단 단계의Windows ACL 거부와blocked-phase75/0은 과거 게임미실행 기록이다. 이후HALFYEAR settings와임시loader/dlc_load로7874를7월 이전 종료하는 bounded run으로 실행했고 자연게임05.31부터SHOW/fixture검사까지UI autosaveNEVER를 유지했다. autosave는 UI에서 반년으로 Apply하고02.08.04 정상Quit/process0 뒤 원본settings SHA332B… 복귀를 확인했다. 이후 HoK only·disabled_dlcs빈배열·진단loader제거·HALFYEAR를 적용했으나 frontend 종료에서 엔진의loading-screen2배열 재기록으로 settings SHA26B…가 됐다. 당시 UI 복귀·최종복구 대기와 아래 최종감사의 원본71보호·설정 기능복귀·settings byte복원 제한을 구분한다. 과거 실패한 `-userdir` 재시도·Windows 보안 변경은 하지 않았다.

7874(36 DLC·2 mods·29 진단 정의)의 A는 1936.02.16.15/PP21, 정책·협약 미완료에서 시작했다. 준비 결정 없이 첫 월간 뒤 70/35/25/45를 관측했다. 합성 선행은 자유당 단독집권뿐이며 협약 자체는 03.06.16에 정상 Start했다. 명목 35일에 저장된 중점 진척 10일이 반영된 진행에서 04.01.20 완료 popup/PP189, 04.04.20 명시 pause/PP192·금색 협약·패널 행동 해금을 관측했다. 소스의 150PP 보상과 정합성은 강하게 지지되지만 일일 PP를 분리한 정확한 전후 delta 검사는 아니다. 04.04.20 패널 70/35/25/45로 두 번째 월간의 협력 가산 중복이 없었다. B는 02.18.10 첫 로드 PP23·70/35/25/45 뒤, 준비 결정0으로 03.02.07 같은 수치·03.05.03 pause/PP41을 관측했다. 7874 정상 Quit와 process 없음, settings의 원본SHA332B18BF10DA2A26CED075EC1678E2FF7D20B699149F4D5D735AF821C2B3AC49 복귀 및 runtime-7874-exit/logs 보존을 root가 확인했다. 다른 임시 프로필2개의 최종복원과 보호71개 최종metadata는 별도다.

실제 userdata는 `C:/Users/jaewo/OneDrive/문서/Paradox Interactive/Hearts of Iron IV`다. 현재 보호 기준 **71개 저장**에는 앞선 실행에서 보존한 `KOR_1937_02_06_17_temp.hoi4`도 포함된다. 이번 보호 검사는 기존 저장의 이름·길이·정밀 UTC 수정시간을 대조한 것이며 저장 내용 71개 전체의 SHA 비교가 아니다. 최종 종료 뒤 root가 프로필 SHA2개 일치·기존71저장 metadata 차이0·임시loader 제거·새test temp총5개 보존을 확인했다. settings는 로딩화면28개 순서만 다르고 byte복원은 접근거부로 제한됐다.

4410에서 구 완료 A의 즉시 주문 표시와 A 재로드 후 월간 비중복을 확인했다. 합성 fixture 없는 자연 독립당 경로로 협약·산업협력을 완료하고 원래 주문 3개를 각 100PP로 사용했다. 90일 타이머의 만료 후 삼성 재사용, 자연 저장의 전체 프로세스 재시작에서 93PP·70/45/23/45·공통 대기90일·주문90일·김구 유지도 관측했다. SHOW 민주 중점 전후의 같은 카메라15점 유지, 한글 상태명19종의 최소1회 tooltip 표시, 등록 민주6명의 제한된 표시 범위를 확인했다.

startup 즉시 등록·모든 기존 저장의 일반 호환, 정확150PP delta·정확 만료 순간·국가 총modifier 제거·현대/선경2회 사용, 모든 표시 전환/배율/클릭·조건 참/거짓 조합·영문UI, 추가4명의 정상 선출/저장재시작·열린 패널의 연속 갱신, 장기AI·DLC 차이·멀티플레이는 미검증이다. 최종 원본71저장metadata 보호와 설정 기능복귀는 확인했으며 settings byte복원 제한은 최종절을 따른다. y1400 접근은 관측한 화면 범위에 한정한다. 새temp저장 외부복사/해시의 자동승인 거절을 재시도하지 않고 원래위치Load로 진행했다. 경로·크기·UTCmetadata만 기록하며 저장내용 비교를 주장하지 않는다.

DLC 비활성 프로필 시도는 debug/비debug 전체 재시작 모두 frontend-only(SP world0)였고 system은36DLC·2mods·4410을 계속 열거했다. 따라서 DLC 비활성 gameplay 통과가 아니다. 일부 DLC asset/BLT validation 차이 때문에 JSON 완전 무시를 단정하지 않으며 원인은UNPROVEN이다. debug 제거만으로 해결된다는 가설도 지지되지 않았다. 정확한두snapshot(151/63·147/59),프로필단계와로그경로는[incident](incidents/2026-10-12-korean-civic-revision.md#autosave-ui-복귀dlc-비활성-시도와-최종-hash-대기)를 따른다.

앞선 `C:/hoi/test/civic-influence-20261012-authorized-runtime/TEST_REPORT.md`는 **개정 전 473개 소스**의 관측 기록이다. 합성 선행 아래 신규 13개 각각의 진행과 일부 보상·상태·save reload 증거는 이번 이관·배치·locale·호환 shared definition의 통과 증거가 아니다. 앞선 startup 81 assertion은 엔진 로그에서 PASS/FAIL 표식이 소실되어 판정 불가였으며 81 PASS로 집계하지 않는다. 사건창 선택지 잘림·정식 저장 rename 실패·전체 캠페인/AI/DLC/멀티플레이 미검증도 별도 이슈로 유지한다.

## 10. 추가 디시전 아이콘 변경 요청과 구현

2026-10-12 첨부 화면을 바탕으로 먼저 문서화만 수행했다. 아래10.1–10.4는 당시 제안·미실행 상태를 보존한다. 이후 사용자가 명시 승인한 구현과 실제 확인 결과는10.5 및 전용 기록을 따른다. 앞선 내정 개정과 아이콘 변경의 증거는 분리한다.

### 10.1 재벌과 시민사회 카테고리의 제목줄 아이콘

‘재벌과 시민사회’ 제목줄 왼쪽의 빨간 아이콘을 사용자 첨부의 공구·톱니·금색 테두리 배지로 교체한다. 대상은 `HOK_KOR_civic_balance` 하나다. 현재 [카테고리 정의](../common/decisions/categories/HOK_KOR_civic_categories.txt:3)는 `GFX_HOK_KOR_decision_category_communist_governance`를 참조한다. 그 [기존 GFX](../interface/HOK_KOR_communist_governance_icons.gfx:57)의 DDS는 `gfx/interface/decisions/HOK_KOR/communist_governance/category.dds`이고 현재 크기는51×40이다.

사용자 첨부 그림을 우선적인 외형 기준으로 둔다. 재사용 후보는 산업·사회협약의 `GFX_HOK_KOR_focus_civic_industrial_compact` → `gfx/interface/goals/HOK_KOR/integrated_production_planning.dds`다. 연결은 [civic focus GFX](../interface/HOK_KOR_civic_focus.gfx:4), 기존100×88 자산의 출처는 [자산 크레딧](HOK_KOREAN_CHAEBOL_CIVIL_SOCIETY_ASSET_CREDITS.md)과 기존 focus manifest를 따른다. 후보 파일과 첨부 이미지의 동일성은 확정하지 않았으며 구현 단계에서 실제 그림을 대조한다.

큰 중점 텍스처를 제목줄에 직접 연결하지 않고 **전용51×40 DDS**로 구성한다. 배지의 구성요소 비율·금속 테두리·투명 여백을 유지하고 작은 화면에서도 중심 그림을 읽을 수 있도록 구성한다. 제목·접기 버튼과의 간격, 잘림 여부를 확인한다. 공산주의 내정 카테고리도 현재 빨간 category 자산을 공유하므로 원본과 기존 공용 GFX를 유지하고 이 카테고리에 전용 연결을 둔다.

### 10.2 네 지원·견제 디시전의 원형 배경을 파란색으로 통일

변경 대상은 첨부 화면에 나온 **네 디시전 왼쪽 원형 아이콘**이다. 초록색 결정 행·실행 버튼·정치력 표시의 배경색을 바꾸는 요청으로 해석하지 않는다.

| 화면 이름 | 유지할 결정 ID | 현재 아이콘 지정 |
|---|---|---|
| 재벌 지원 | `HOK_KOR_support_chaebol` | [civic decisions 4행](../common/decisions/HOK_KOR_civic_decisions.txt:4) |
| 재벌 견제 | `HOK_KOR_suppress_chaebol` | [16행](../common/decisions/HOK_KOR_civic_decisions.txt:16) |
| 시민사회 지원 | `HOK_KOR_support_civic` | [28행](../common/decisions/HOK_KOR_civic_decisions.txt:28) |
| 시민사회 견제 | `HOK_KOR_suppress_civic` | [40행](../common/decisions/HOK_KOR_civic_decisions.txt:40) |

네 결정은 현재 모두 `GFX_HOK_KOR_decision_yeo_labor_compact`를 사용한다. [공용 GFX](../interface/HOK_KOR_communist_governance_icons.gfx:61)는 `gfx/interface/decisions/HOK_KOR/communist_governance/yeo_labor_compact.dds`를 가리킨다. 기존32×32 이미지의 저울·원형 금속 테두리·붉은 배경 구성은 [small decision manifest](data/HOK_KOREAN_SMALL_DECISION_ICON_MANIFEST.json)와 자산 크레딧에 기록돼 있다.

저울 문양과 원형 금속 테두리를 유지하고 **원 내부 배경만 파란색**으로 바꾼 전용32×32 버전을 네 결정에 공통으로 연결하는 계획이다. 전체 완성 이미지에 색조 필터를 적용하지 않고 배경을 별도 처리한다. 민주주의 가지의 푸른 색 계열을 따르되 정확한 색상값은 구현 때 작은 크기의 대비를 보고 기록한다. 투명도·테두리·그림 비율과 기존 상태 표현을 보존한다.

현재 빨간 저울 자산은 공산주의 노동 협약과 시민 내정의 증거 보전·기관 장악망 해체·시민적 위임 회복·정변 카운트다운에도 쓰인다. 이번 요청은 그 콘텐츠까지 모두 파랗게 바꾸는 범위가 아니다. 따라서 공용 빨간 DDS/GFX를 덮어쓰지 않고 네 지원·견제 결정에만 전용 파란 버전을 연결한다. 조달 카테고리·기업 주문·영향력 패널 카드·다른 국민정신의 그림도 이 요청 밖이다.

### 10.3 후속 구현 범위와 출처 기록

추후 구현이 승인되면 전용 작은 자산을 `gfx/interface/decisions/HOK_KOR/civic/` 아래에 저장하고 프로젝트 소유 `GFX_HOK_KOR_decision_*` 연결을 사용한다. 해당 디렉터리·새 DDS·새 GFX 이름은 이번 문서화에서 생성하거나 확정하지 않았다. 범주와 네 결정의 아이콘 참조만 바꾸며 기존 결정 ID·이름·해금 조건·정치력50·공통90일 대기·영향력/비리/기관 효과·AI를 유지한다.

원래 소재와 작가·기존 합성 기록은 [자산 크레딧](HOK_KOREAN_CHAEBOL_CIVIL_SOCIETY_ASSET_CREDITS.md), 공산주의 아이콘 크레딧 및 관련 manifest에 남긴다. 후속 파란 배경 가공은 원작 그림의 저작자로 새로 표기하지 않고 선택·합성·배경색 변경 기여로 구분한다. 실제 생성된 파일의 원본·최종 경로, 색상값,32×32/51×40 크기, 투명도, GFX 연결과 해시는 구현 후 기록한다. 현재 크레딧의 기존 빨간 자산 표를 새 파란 자산의 완료 기록으로 바꾸지 않는다.

### 10.4 최초 확인 계획 — 문서화 당시 미실행

- 제목줄의 새 배지와 한국어 제목·접기 버튼이 겹치거나 잘리지 않는지 확인.
- 네 아이콘이 같은 파란 배경을 쓰고 저울·금속 테두리·투명 여백이 유지되는지 실제 크기로 확인.
- 공산주의 내정과 이번 범위 밖의 다른 civic 결정이 기존 그림을 유지하는지 확인.
- 사용 가능·불가·활성 표시와 카테고리 접기/펼치기를 실제 게임에서 확인하고 엔진의 상태별 색조와 자산 배경색을 구분.
- 아이콘 교체가 조건·비용·대기기간·효과·AI·저장 연결을 바꾸지 않았는지 제한된 소스 비교로 확인.

위 목록은 최초 문서화 시점의 확인 계획이다. 앞선82/0·498/0과 내정 진행·저장 결과를 새 아이콘의 통과 근거로 사용하지 않는다. 후속 구현에서 실제 수행한 항목과 한계는 아래10.5를 따른다.

### 10.5 적용·검증 결과

전용51×40배지와32×32파란 저울을 `gfx/interface/decisions/HOK_KOR/civic/`에 적용했다. `interface/HOK_KOR_civic_decisions.gfx`의 전용 sprite2개를 카테고리1곳과 네 지원·견제에 연결했다. 첨부 배지와 기존 산업·사회협약 그림의 구성을 직접 대조하고 동일 소재를 작은 캔버스에 재구성했다. 공용 빨간 그림과 다른 소비자는 보존했다.

독립 소스 확인19/0과 DDS·알파·배경 마스크 확인을 통과했다.575f 소스만의 전체 재시작에서 배지·네 불가 행·접기/펼치기를, 별도2430 외부 표시 fixture에서 네 가능 행과 지원 실행 후 표시를 실제 확인했다. 원래 지원은 정치력93→43으로50을 소모했다. 화면 확인은 한국어1600×900 GUI1.0의 선택된 저장/상태이며 일반 진행·모든 DLC/배율의 통과로 확대하지 않는다.

테스트 로더 제거·원래 모드 목록 바이트 복원을 완료했다. 이번 시작 대비 settings해시 동일, 기존76저장 metadata차이0·신규저장0이다. 외부 fixture·로그·백업은 증거로 보존하며 로드되지 않는다. 상세 경로·해시·출처·검증 구분과 한계는 [아이콘 구현 기록](incidents/2026-10-12-korean-civic-decision-icons.md)과 [전용 매니페스트](data/HOK_KOREAN_CIVIC_DECISION_ICON_MANIFEST.json)를 따른다.
