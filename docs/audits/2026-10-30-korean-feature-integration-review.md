# 한국 기능 연동 비교 감사 — 영국·독일 1.19.3 원본 기준

작성: 2026-10-30 (Asia/Seoul). 상태: **소스 검토·문서화 완료 / 게임 코드 수정 미실시 / 실행 검증 NOT RUN**.

> 후속 상태 — 2026-10-31: 사용자가 전체 후속 설계·구현을 승인하여 A1–A3와 B1/C1–C4의 소스 구현을 진행했다. [확정 명세](../HOK_KOREAN_FEATURE_INTEGRATION_SPEC.md)와 [구현·검증 기록](../incidents/2026-10-31-korean-feature-integration.md)의 실제 적용·검증 범위를 따른다. 아래 내용은 수정 전 감사 기준과 증거로 보존하며 현재 소스의 누락 목록으로 재사용하지 않는다.

## 요청 범위와 결론

사용자는 함장 훈장처럼 한국에 빠진 기능 연동을 설치된 HOI4 영국·독일과 비교해 확인하되, 코드는 수정하지 말라고 요청했다. 후속 요청은 이 조사 결과의 문서화다. 이번 작업은 게임 코드·자산·설정·플레이셋을 변경하거나 향후 구현을 승인하는 작업이 아니다.

| 구분 | 확인 수 | 의미 |
|---|---:|---|
| 기능 연결 누락 | 2개 계통 | 함장·함정 훈장, 시작 교리 초기화의 현행 체계 이식 |
| 해금 안내 누락 | 1건 | 비전 1950의 기존 1단계 결정 안내 |
| 미완성 콘텐츠 흔적 | 1건 | 소양강댐 수문 조절 범주·문구에 대응하는 결정 정의 부재 |
| 국가 전용 콘텐츠 차이 | 4개 영역 | 고유 MIO 특성, 연구시설·과학자 육성 중점, 고유 습격, 세력 템플릿 |

이는 **8개의 버그나 전체 모드의 결함 총수**를 뜻하지 않는다. 교리의 여러 구형 ID와 파생 국가의 같은 초기화 문제는 하나의 계통으로 묶었다. 훈장 4종과 함장 경험치 처리도 같은 훈장 계통이며 별도 결함으로 중복 계산하지 않았다. 국가 전용 콘텐츠 차이는 기능을 사용할 수 없다는 판정과 분리한다.

검토 범위는 훈장·교리·사관단·장비 설계와 OOB·MIO·특별 프로젝트와 과학자·정보기관·습격·세력·중점과 결정의 주요 연결 및 AI 계획이다. 모든 장비·중점·이벤트의 모든 경로, 맵 전체와 모든 DLC·의존 모드 조합을 전수검증하지 않았다.

## 기준 소스와 실행 경계

| 항목 | 조사 기준 |
|---|---|
| 작업 저장소 `<PROJECT>` | `C:/hoi/hearts_of_korea` |
| 브랜치 | `feat/korean-focus-expansion-ai` |
| 기준 HEAD | `860efe7a3513148dc6964b7e0e3dfafd19addfb7` |
| 조사·문서화 시작 작업 트리 | clean |
| 비교 원본 `<VANILLA>` | `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV` |
| 설치 버전 | `Operation Postern v1.19.3.0.c01a`, Steam build `25205862` |
| 설치 메타데이터 체크섬 | `5632` — 이번 소스의 실제 실행 체크섬이 아님 |
| 버전 근거 | `<VANILLA>/launcher-settings.json:4–5`, `steamapps/appmanifest_394360.acf:13` |
| 저장소 descriptor | `supported_version="1.19.*"`, 의존성 `Korean Language`, `replace_path` 없음, 기록된 후속 Workshop ID `3793992662` |
| 저장소용 launcher 파일 | `<HOI4_USER_DATA>/mod/hearts of korea.mod`의 `path`는 `<PROJECT>` |
| 조사 당시 구성·기존 로그 | `dlc_load.json`은 별도 `hearts_of_korea_Road_to_56.mod`와 추가 모드 2개를 선택하며, 기존 `system.log:180`도 RT56 호환판을 기록 |
| 실제 플레이셋 이름·필수 의존 모드 로드 순서 | 이번 저장소의 실행 구성으로 확정하지 않음 |
| DLC·언어 실행 조건 | 조사 당시 구성의 `disabled_dlcs`는 빈 목록이나, 이번 저장소를 실행하지 않았으므로 해당 실행의 활성 DLC 집합·한국어 표시를 검증하지 않음 |

운영체제는 Windows이며 사용자 데이터는 OneDrive로 연결된 문서 폴더 아래다. 개인 식별 경로는 `<HOI4_USER_DATA>`로 표기한다. 버전 선언만으로 호환성을 판단하지 않았고, 현재 RT56 로그를 이 저장소의 실행 증거로 사용하지 않았다. 소스 부재 검색은 저장소와 지정 설치본 범위이며, 활성 RT56·다른 외부 모드가 보충하는 내용까지 판정하지 않는다.

읽기 전용 `rg` 검색, `Get-Content` 열람, 공통 덮어쓰기 파일의 줄 비교, Git 상태 조회를 사용했다. 검사기·검증 스크립트·게임은 실행하지 않았다. 원본 게임·Workshop·런처·로그·세이브를 수정하거나 복사하지 않았다. 아래 줄 번호는 기준 HEAD와 이 설치본에 대한 위치이며 향후 수정 시 다시 확인해야 한다.

## A. 확인된 기능 연결·안내 누락

### A1. 함장·함정 훈장 연결

**CONFIRMED — 한국 훈장에 해군 수여용 정의가 없다.** 실제 게임 화면에서의 수여·경험치·진급 확인은 NOT RUN이다.

- [한국 훈장](../../common/unit_medals/hok_medal_default.txt)의 7·26·44·62행은 화랑·충무·을지·태극무공훈장을 정의한다. 네 정의 모두 `unit_modifiers`만 있고 `ship_modifiers`는 없다.
- [훈장 분류 조건](../../common/scripted_triggers/unit_medals_scripted_triggers.txt)의 63행은 한국 고유 훈장 조건, 83행은 공용 훈장 제외에 사용하는 고유 훈장 보유국 묶음에 한국을 포함한다.
- 원본 `common/unit_medals/00_default.txt:25`는 어느 한 군종의 modifier만 있으면 다른 군종에 수여할 수 없다고 명시한다. 공용 훈장은 같은 파일 1977행 등에서 `should_have_any_unique_medals_trigger = no`를 요구한다.
- 원본 독일 훈장 4종은 같은 파일 466행부터, 영국 훈장 4종은 718행부터 정의된다. 독일 첫 훈장의 해군 효과는 478행, `officer_xp = 100`은 485행이며, 영국 첫 훈장의 대응 위치는 730·733행이다.
- 한국은 20–21행 등에서 `one_time_effect = { add_divisional_commander_xp = 100 }`를 쓴다. 원본 26행은 함정에 훈장을 수여할 때 `one_time_effect`가 실행되지 않는다고 명시하므로, 해군 이식 시 경험치 경로도 함께 검토해야 한다.

**현재 육군 훈장 경험치도 고장 났다는 결론은 내리지 않는다.** 원본 `documentation/effects_documentation.md:1135`에는 `add_divisional_commander_xp`가 여전히 수록돼 있다. 함장 훈장을 추가한다는 이유로 기존 육군 보상·정치력 비용·ID·그림을 바꾸거나 경험치를 중복 지급하는 구현은 승인된 상태가 아니다.

### A2. 시작 교리 초기화의 현행 체계 이식

**CONFIRMED — 구형 교리 기술 참조와 한국의 대체 초기화 부재. STRONGLY_SUPPORTED — 의도한 시작 교리가 지급되지 않을 가능성.** 엔진 자동 기본값과 실제 시작 화면은 UNPROVEN이다.

| 출처 | 확인 내용 |
|---|---|
| [한국 history](../../history/countries/KOR%20-%20Korea.txt), 81–84행 | `set_technology` 안에서 `superior_firepower`, `trade_interdiction`, `formation_flying`을 지급 |
| 원본 `common/technologies/` | 위 세 ID의 기술 정의를 발견하지 못함 |
| 원본 `common/doctrines/grand_doctrines/land_grand_doctrines.txt:120` | 현재 `superior_firepower`는 기술이 아닌 대교리 정의 |
| 원본 `common/doctrines/_documentation.md:15` | 초기화 effect로 `set_grand_doctrine` 설명 |
| 원본 `history/countries/GER - Germany.txt:34–36` | `new_mobile_warfare`, `new_convoy_raiding`, `new_battlefield_support`를 `set_grand_doctrine`으로 지정 |
| 원본 `history/countries/ENG - Britain.txt:142–143` | `grand_battleplan`, `new_fleet_in_being`을 같은 방식으로 지정 |
| 저장소 한국 관련 history·common·events | 한국의 대체 `set_grand_doctrine` 설정을 발견하지 못함 |

[KCH](../../history/countries/KCH%20-%20Korean%20China.txt), [KJP](../../history/countries/KJP%20-%20Korean%20Japan.txt), [RKY](../../history/countries/RKY%20-%20Ryukyu.txt)도 15–17행과 1939 블록 110–121행에 구형 교리 기술 참조가 남는다. 이 세 국가의 첫 참조는 한국의 `superior_firepower`와 달리 `mobile_warfare`다. 개별 ID·국가를 별도 기능 결함으로 세지 않으며, 1939 블록이 있다는 사실만으로 해당 시작일 지원을 입증하지 않는다.

[2026-09-09 일본 통합 기록](../incidents/2026-09-09-japan-democratic-focus-integration-implementation.md)의 217행은 당시 대만의 같은 종류 구형 교리 기술 참조를 `Invalid tech`로 관측하고 정리했다고 기록한다. 이는 **과거 대만의 실행 증거**이며 이번 한국 소스의 새 실행 결과가 아니다.

원본 `common/ideas/navy_spirits.txt:46–51`처럼 교리를 조건으로 하는 사관단 정신도 있어, 시작 교리 미지급은 초기 선택지에 영향을 줄 수 있다. 사관단 전체가 없다는 뜻은 아니다. 향후 수정에는 현재 의도한 육·해·공 교리를 먼저 확정하고, 구형 기술과 현행 교리 이름을 일괄 치환하지 않아야 한다.

### A3. 비전 1950의 기존 1단계 결정 해금 안내

**CONFIRMED — 중점 효과의 개별 결정 해금 안내 누락. 결정 정의·사용 경로 자체의 부재는 아니다.**

- [한국 중점](../../common/national_focus/korea.txt)의 2883–2888행은 국민정신·해군 경험치를 주고 신규 `HOK_KOR_enact_emergency_special_shipbuilding`만 `unlock_decision_tooltip`으로 안내한다.
- [한국 결정](../../common/decisions/KOR_decision.txt)의 701행에는 기존 `KOR_vision_1950_step_1`이 있으며, 727행은 같은 중점 완료를 표시 조건으로 쓴다. 함대 규모에 따른 별도 사용 조건은 유지돼 있다.
- 2·3단계는 앞 단계의 완료 플래그로 열리므로, 중점이 직접 해금하는 결정의 안내 누락으로 중복 계산하지 않는다.
- 비교 원본 `common/national_focus/germany.txt:7686`은 `unlock_decision_tooltip = GER_refit_convoys_to_cruisers`로 개별 결정 해금을 안내한다.

향후 안내를 추가하더라도 범주 전체나 즉시 사용 가능을 약속하지 않고, 기존 함대 조건·비용·플래그·보상은 보존해야 한다. [긴급 특별 건함계획 구현 기록](../incidents/2026-10-20-korean-emergency-shipbuilding.md)의 기존 기능 검증을 이번 안내 누락 수정의 완료 증거로 사용하지 않는다.

## B. 미완성 콘텐츠 흔적

### B1. 소양강댐 수문 개방·정상화

**CONFIRMED — 대응 결정 정의 부재. UNPROVEN — 원래 미완성이었는지, 과거 작동하던 기능이 소실됐는지.**

- [결정 범주](../../common/decisions/categories/KOR_decision_categories.txt)의 82–92행은 `KOR_soyanggangdam_category`를 정의하고 소양강댐 중점 완료 후 표시하도록 한다.
- [한국어 문구](../../localisation/korean/replace/korea_decisions_l_korean.yml)의 53–56행에는 수문 조절 범주·설명과 `KOR_inundate_the_water_lines`, `KOR_drain_the_water_lines` 명칭이 있다.
- 저장소와 설치 원본의 결정 정의에서 두 결정 ID를 발견하지 못했다. 저장소 common·events에도 이를 실행하는 대응 정의는 발견하지 못했다.
- [소양강댐 중점](../../common/national_focus/korea.txt)의 446–492행은 공장·기반시설·댐을 건설하며, [중점 설명](../../localisation/korean/korea_focus_l_korean.yml)의 21행은 전력·수도 공급을 설명한다. 수문 결정 해금은 약속하지 않는다.

따라서 댐 건설 자체가 실패한다거나 업데이트로 수공 기능이 사라졌다고 단정하지 않는다. 범주가 실제로 빈 상태로 표시되는지도 이번에 관측하지 않았다. 복원 또는 새 수공 개발은 역사적 의도·피해 범위·AI·비용과 조건을 별도로 정해야 하며, 문구만 근거로 구현하지 않는다.

## C. 국가 전용 콘텐츠 차이 — 결함 집계 제외

아래는 영국·독일에 있는 전용 연계와 비교한 개발 후보다. 국가별 설계 차이일 수 있으며 현재 공용 기능을 사용할 수 없다는 뜻이 아니다. 추가 개발·재설계·보상 강화는 이번 문서화 요청의 범위에 포함하지 않는다.

| 항목 | 한국에서 확인한 상태 | 영국·독일 비교 근거 | 판정 경계 |
|---|---|---|---|
| C1. MIO 고유 특성 | [한국 MIO](../../common/military_industrial_organization/organizations/KOR_organization.txt)는 공용 조직 트리를 `include`하며 별도 `add_trait`, `override_trait`, `initial_trait`는 발견하지 못함 | 원본 `common/military_industrial_organization/organizations/ENG_organization.txt:76–135`, `GER_organization.txt:78` 이후 | MIO 15개와 공용 성장 기능은 이미 존재. 국가 전용 특성의 차이 |
| C2. 연구시설·과학자 육성 중점 | 돌파점·프로젝트 속도 보상은 있으나 한국 중점에서 연구시설 지급·건설 및 과학자 레벨 성장 연계는 발견하지 못함 | 원본 `common/national_focus/uk.txt:752–803`의 실험시설, `germany.txt:19061–19121`의 과학자·시설 연계 | 기본 과학자·프로젝트 사용을 막는 결함 아님. 별도 강화 설정의 [gookppong_on_actions](../../common/on_actions/gookppong_on_actions.txt) 787행 시설 지급 주석도 구현 완료 증거가 아님 |
| C3. 한국 고유 습격 | 한국 전용 습격과 중점 해금은 발견하지 못함 | 원본 `common/national_focus/germany.txt:4827`, `6298`의 고유 습격 공개 안내 | 공용 습격 정의를 상속. 고유 작전 콘텐츠의 차이 |
| C4. 한국 세력 템플릿 | [한국 중점](../../common/national_focus/korea.txt) 4460·6530행과 [한국 이벤트](../../events/korea.txt) 1267행 등은 `create_faction` 사용. 전용 목표·규칙 템플릿은 발견하지 못함 | 원본 `history/countries/ENG - Britain.txt:605`, `GER - Germany.txt:871`은 템플릿 생성. `common/factions/templates/allies.txt:2`, `axis.txt:1`에 목표·규칙 정의 | 원본 `common/factions/_documentation.md:273–274`는 구형 effect를 obsolete로 설명하며, `templates/generic_factions.txt:1–8`에는 fallback 템플릿이 존재. 각 구형 생성 지점에서 실제 적용되는 템플릿·목표·규칙은 실행 미확인 |

## D. 이미 연결돼 있어 누락으로 세지 않은 기능

여기서 연결 확인은 소스의 정의·호출·공용 상속 경로 확인이다. 모든 UI·보상·DLC 조건의 실행 검증 통과를 뜻하지 않는다.

| 시스템 | 소스 근거와 확인 범위 |
|---|---|
| MIO 15개 | [한국 조직](../../common/military_industrial_organization/organizations/KOR_organization.txt)의 전차 4·항공 3·함정 4·군수품 4개. [중점](../../common/national_focus/korea.txt) 1960–1980행 등은 AAT 보유 시 MIO, 미보유 시 기존 설계사로 분기하며 공개 조건도 존재 |
| 과학자 4명 | [한국 인물](../../common/characters/KOR.txt) 1487·1500·1513·1526행에 역할 정의, [history](../../history/countries/KOR%20-%20Korea.txt) 237–241행에서 모집 |
| 특별 프로젝트 보상·장갑 지원차량 | [중점](../../common/national_focus/korea.txt) 1112·1145행의 항공·핵 돌파점, [결정](../../common/decisions/KOR_decision.txt) 957행의 프로젝트 속도, [SP 효과](../../common/scripted_effects/SP_scripted_effects.txt) 102·211·336·497행의 한국 지원차량 변형 |
| 정보기관·첩보원 | [기관 정의](../../common/intelligence_agencies/00_intelligence_agencies.txt) 812–816행, [history](../../history/countries/KOR%20-%20Korea.txt) 244–266행의 DLC 분기·첩보원, [중점](../../common/national_focus/korea.txt) 7320행의 기관 생성 |
| 전차·함선·항공 설계와 OOB | [한국 history](../../history/countries/KOR%20-%20Korea.txt) 41–64행의 NSB·MTG·BBA 분기 및 이후 기술·variant 정의. 전체 장비 완전성은 미검증 |
| 일반 사관단 정신·수뇌부 | 원본 `common/ideas/army_spirits.txt`, `navy_spirits.txt`, `air_spirits.txt`를 해당 경로에서 덮어쓰지 않음. [한국 인물](../../common/characters/KOR.txt) 273·390·430·495·973행 등에 참모총장·최고사령부·이론가 역할 존재. A2의 교리 조건 영향은 별도 |
| 육군 사령부·연대 지원 | 원본 `common/units/hq_support.txt:8,32`, `common/technologies/infantry.txt:1567–1573`의 공용 정의·기술 조건을 상속. 한국 전용 파일 부재를 기능 부재로 세지 않음 |
| 공용 습격 | 저장소에 `common/raids` 덮어쓰기 없음. 원본 `common/raids/air_raids.txt:41–47`, `paratrooper_raids.txt:42–47`은 DLC·기술 등 조건을 쓰며 ENG/GER 전용 제한이 아님 |
| 역사·비역사 AI | [역사 계획](../../common/ai_strategy_plans/KOR_historical_strategy_plan.txt), [대체 계획](../../common/ai_strategy_plans/KOR_alternate_strategy_plan.txt) 존재. 장기 실행 품질까지 입증하지 않음 |
| 교리 할인 보상 | 한국의 `add_doctrine_cost_reduction`은 이름만으로 구형 무효 효과라 판단하지 않음. 원본 `common/national_focus/germany.txt:2938,4972,6408`도 같은 effect 사용 |

## 향후 작업 구분과 검증 필요 사항

아래는 후속 요청의 범위를 정할 때 사용할 제안이며, 이번에 수행하거나 승인받은 구현·테스트가 아니다.

| 대상 | 후속 범위 | 필요한 확인 |
|---|---|---|
| A1 | 기존 한국 훈장 ID·육군 보상을 보존하며 해군 효과·경험치 경로 설계 | 함정 수여 가능/불가 조건, 실제 비용·효과·함장 경험치, 육군 경험치 중복 여부, 제독 진급·저장 후 상태 |
| A2 | 한국 및 파생 국가별 시작 교리 의도 확인 후 최소 이식 | 깨끗한 새 게임의 교리·사관단 선택지, 관련 오류의 기준선 비교, 지원 시작일·DLC별 상태. 기존 저장 변경 여부는 별도 판단 |
| A3 | 기존 1단계 개별 결정의 해금 안내만 추가 | 중점 tooltip의 명칭·해금 표시, 별도 함대 사용 조건과 기존 보상·플래그 보존 |
| B1 | 원래 미완성 여부와 복원·제외·새 개발 중 범위 결정 | 역사적 소스·의도 조사. 구현 결정 전에는 방류 피해·비용·AI를 임의로 정하지 않음 |
| C1–C4 | 요청된 항목별 후속 개발·현대화 | 국가 고유 보상·시설·작전·세력 목표를 각각 명세하고 공용 상속과 실행 동작 확인 |

## 작업·검증 기록

- **완료:** 앞선 읽기 전용 조사 결과의 문서화, 핵심 출처·줄 번호 재확인, README 문서 목록 연결, 문서 diff 수동 검토.
- **NOT RUN:** 게임 실행, 새 게임·정상 진행·UI 확인, 강제 효과 진단, 게임플레이 검사기·테스트·검증 스크립트.
- **NOT RUN / NOT CLAIMED:** 저장 호환·장기 AI·DLC 조합·의존 모드 포함 실행·멀티플레이 동기화.
- **생성·수정 문서:** 이 감사 문서와 루트 `README.md`의 문서 목록 항목.
- **유지:** 게임 코드·localisation·GFX·자산·descriptor·게임 원본·Workshop·런처·설정·세이브·기존 로그.
- **Git 작업:** commit·push·tag·브랜치 변경·업로드 없음. 문서 변경만 작업 트리에 남김.

이 문서의 완료 상태는 **조사 결과의 기록 완료**이며, A1–A3의 수리 완료나 B1·C1–C4의 개발 완료가 아니다.
