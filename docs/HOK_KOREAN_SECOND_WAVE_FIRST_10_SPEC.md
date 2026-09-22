# 2차 첫 정책 묶음 — 공산 경제 중점 10개

작성: 2026-09-22. 구현 대상 HOI4 1.19.3. 이 첫 묶음 적용 당시 전체 중점은 336개였으며, 본 문서는 그중 신규 10개를 정의한다. 이후 [후속 내정 9개](HOK_KOREAN_COMMUNIST_GOVERNANCE_SPEC.md), [기술보급·계획행정 9개](HOK_KOREAN_COMMUNIST_DEVELOPMENT_SPEC.md), [파시즘 군수계약 4개](HOK_KOREAN_FASCIST_PROCUREMENT_SPEC.md), [파시즘 참모업무 4개](HOK_KOREAN_FASCIST_STAFF_SPEC.md), [병역·필수인력 4개](HOK_KOREAN_FASCIST_MOBILIZATION_SPEC.md)를 추가한 현재 전체는 366개다. 아래 ID는 `HOK_KOR_` 접두사만 생략한다. 기간은 모두 cost5·기본 35일이다. F3의 이전 배치 소스에서 강제 보상 검사 130 PASS / 0 FAIL과 초기 HIDE의 완료 중점·정신 표시를 확인했다. 이후 확대 HIDE에서 F2 합류선과 F3 진입선의 공선이 발견되어, 새 4개만 군내 극우인사 포섭의 상단 옆가지로 옮겼다. 을해군란 완료 조건·보상·전체 140일은 유지한다. 최종 소스의 추가 정적 검사 44건·강제 보상 재검사 130건이 통과했고 진단 없는 새 게임 로드(53b0)의 신규 정규화 오류는 0건이다. 2026-09-23에는 최종 상단 배치의 HIDE 화면과 병역행정 명부의 UI 시작·35일 정상 진행·완료를 관측했다. 별도의 정치 분기 완료 합성 새 게임에서 최종 상단 구역의 SHOW도 확인하여 네 중점·부모·을해군란·F2 및 인접 왕정 구역 사이의 연결선·아이콘·명판 가림을 관측하지 않았다. HIDE/SHOW는 각각 별도 상태 관측이며 정치 선택 전환 검사는 아니다. 나머지 3개 중점·최종 AND 차단·전체 140일·장기 AI는 미검증이며 [F3 구현 기록](incidents/2026-09-22-korean-fascist-mobilization.md)의 범위를 따른다.

공통 조건: 공산정부, 내전 없음, 해당 기존 지도자 선택 완료, 항복 중 진행 불가. 조건 상실 시 진행을 취소한다. 기존 경로의 중점 보상·선행·상호배타는 보존한다.

2026-09-22 후속 보상 조정: 아래 수치는 사용자가 지정한 최종값이며 변경 전 보상에 추가하는 값이 아니다. 기존 326개, 중점·정신·결정 ID, 배치와 이미지는 유지한다. 기존 부가효과는 아래에 명시한 대로 보존한다. 정적 검토와 변경 후 네 정책의 실행 효과 검사 149 PASS/0 FAIL을 확인했다. 정상 UI의 비용 지불·연구 보너스 소모 등은 별도 검증 대상이다.

| ID | 이름 | 선행 | 기본 절대 좌표 | 보상 |
|---|---|---|---|---|
| `yeo_cooperative_registry` | 협동조합 등록망 | `KOR_rural_support_plan` | 75,10 | 산업 연구 150% 1회 |
| `yeo_joint_purchasing` | 연합 공동구매 우선 | 등록망 | 73,11 | 공동구매 I; 자율금융과 상호배타 |
| `yeo_rural_credit` | 지역 자율금융 우선 | 등록망 | 77,11 | 자율금융 I; 공동구매와 상호배타 |
| `yeo_cooperative_workshops` | 협동 작업장 | 공동구매 또는 자율금융 | 75,12 | 두 경로 모두 전자 연구 100% 1회; 공동구매는 기존 산업 연구 75% 1회도 유지 |
| `yeo_cooperative_federation` | 전국 협동조합 연합 | 협동 작업장 | 75,13 | 선택 정신만 II로 교체; 선택한 사업 해금 |
| `pak_machine_tool_allocation` | 공작기계 배치계획 | `KOR_heavy_industry_concentration` | 98,10 | 산업 연구 150% 1회 |
| `pak_capital_goods_board` | 군수설비 확충 우선 | 배치계획 | 96,11 | 설비확충 I; 현행생산과 상호배타 |
| `pak_steel_delivery_schedules` | 현행 생산계획 우선 | 배치계획 | 100,11 | 현행생산 I; 설비확충과 상호배타 |
| `pak_industrial_reporting` | 공업통계 보고망 | 설비확충 또는 현행생산 | 98,12 | 전자 연구 100% 1회 |
| `pak_heavy_industry_dispatch` | 중공업 종합배정 | 공업통계 보고망 | 98,13 | 선택 정신만 II로 교체; 선택한 사업 해금 |

여운형은 `KOR_yeo_woon_hyung_as_the_leader`, 박헌영은 `KOR_park_heon_young_as_the_leader` 완료를 각 중점의 조건으로 확인한다. 중점당 한 개 선행 그룹의 두 ID는 OR다. 상호배타 두 쌍은 양쪽에 대칭으로 정의한다. 배치 기준과 선행 조건을 혼동하지 않으며, 각 상대 기준은 해당 중점보다 먼저 선언한다.

## 국민정신

모든 정신은 해당 정책색과 중심 소재를 공유한다. I·II는 동시 중첩하지 않는다. 아래 II 수치는 I에 추가하는 값이 아니라 교체 후 최종값이다. 공산정부 상실 시 제거하며, 복귀 시 자동 재지급하지 않는다.

| 정신 ID (`HOK_KOR_`) | I | II |
|---|---|---|
| `yeo_joint_purchasing_1/2` | 민간공장 건설 속도 +15% | 민간공장 건설 속도 +15%, 일일 정치력 +0.5 |
| `yeo_local_credit_1/2` | 일일 정치력 +1.2 | 일일 정치력 +1.2, 민간공장 건설 속도 +2% |
| `pak_plant_expansion_1/2` | 군수공장 건설 속도 +15% | 군수공장 건설 속도 +15% |
| `pak_current_output_1/2` | 군수공장 생산량 +10% | 군수공장 생산량 +10% |

자율금융 II의 별도 정치력 추가 강화값은 지정되지 않았으므로 I의 일일 정치력 +1.2를 그대로 승계하고, 기존 민간공장 건설 속도 +2%를 유지한다. 설비확충과 현행생산도 지정된 I·II 최종값을 각각 적용한다. 상위 단계에서 임의로 추가 수치를 만들지 않는다.

공산주의 기존 보상 및 공통 산업 보상에 더해진다. 박헌영 현행 생산은 보병장비에만 적용되는 효과가 아니라 모든 군수공장 생산량 보정이다. 미결 보병장비 보상을 대체하지 않는다.

## 정책 실행 결정

카테고리 `HOK_KOR_communist_policy_projects`는 한국 원국가에서 두 말단 중 하나 완료 후 표시한다. 현재 정부가 바뀌어도 카테고리는 남아 취소·재착수 조건을 확인할 수 있다. 시작·취소 조건은 결정 자체에서 검사한다.

모든 사업의 기간은 90일이며, 아래 비용으로 시작한 뒤 진행 중에만 `modifier`를 적용한다. 모든 사업을 통틀어 최대 하나만 진행할 수 있다. 정상 종료·취소 모두 공통 진행 플래그를 해제하고 90일 대기 플래그를 설정한다. 정치력 환급·무료 공장·일회성 재화의 반복 지급은 없다.

| 결정 ID (`HOK_KOR_`) | 선택된 정책 | 90일 효과 | 정치력 비용 | 민공 점유 | AI의 최소 가용 민공 |
|---|---|---|---:|---:|---|
| `yeo_joint_purchasing_project` | 공동구매 | 민간공장 건설 속도 +15% | 150 | 0 | 요건 없음 |
| `yeo_rural_credit_project` | 자율금융 | 전체 건설 속도 +10% | 75 | 2 | 24 |
| `pak_plant_expansion_project` | 설비확충 | 군수공장 건설 속도 +15% | 150 | 0 | 요건 없음 |
| `pak_current_output_project` | 현행생산 | 군수공장 생산량 +10% | 75 | 2 | 6 |

공동구매 조달과 군수설비 집중 건설은 사람과 AI 모두 민공 수량 요건이 없고 민공을 점유하지 않는다. 자율금융과 현행생산은 사람에게 가용 민공 2개 이상을 요구하며, AI에는 표의 공장 여유 기준을 적용한다. 네 사업 모두 기존 AI 정치력 150 이상 조건과 기본 가중치 0.5를 유지한다. 공산정부 상실·내전·항복·경로 상실 시 취소한다. 민공을 점유하는 두 사업에서도 진행 중 민공 총량 감소만으로 자동 취소하지 않는다. 이 경우의 공장 배분은 실제 게임에서 별도 확인한다.

## 구현·검증 파일

- `common/national_focus/korea.txt`: 중점10개, 기존 위치 관련 수정6블록.
- `common/ideas/HOK_KOR_communist_policy.txt`: 단계 정신8개.
- `common/decisions/HOK_KOR_communist_policy.txt` 및 `categories/HOK_KOR_communist_policy.txt`: 사업4개·카테고리1개.
- `localisation/korean/HOK_KOR_communist_policy_l_korean.yml` 및 영어 채널 대응 파일: 한국어 본문 53키, UTF-8 BOM 유지.
- `interface/HOK_KOR_second_wave_icons.gfx`, `interface/HOK_KOR_second_wave_icons_shine.gfx`: 새 이미지 및 결정 매핑. 결정은 [크기 수정](incidents/2026-09-22-korean-decision-icon-size.md)에 따라 카테고리 51×40·개별 결정 32×32의 전용 DDS를 사용한다.
- [이미지 매니페스트](data/HOK_KOREAN_SECOND_WAVE_ICON_MANIFEST.json), [좌표 데이터](data/HOK_KOREAN_SECOND_WAVE_COORDINATES.json), [검증 기록](incidents/2026-09-22-korean-second-wave-first-policies.md).

설치본 근거: `common/decisions/AST.txt:3135`·`ENG.txt:1807`·`HOL.txt:139`의 기간제 수정치, `GER.txt:1568`의 민공 사용·취소 처리. 이식한 것은 문맥과 생애주기 구조이며 다른 국가의 사건·변수·보상 체계를 복제하지 않았다. 기존 한국의 단계 교체 및 연구 보너스 구조와 대조했다.

기존 진단의 149 PASS/0 FAIL은 조정 전 기록으로 보존한다. 변경 후에도 새 기대값으로 네 정책을 별도 실행하여 149 PASS/0 FAIL을 확인했다. 새 결과와 한계는 [보상 변경 검증 기록](incidents/2026-09-22-korean-policy-rewards.md)을 따른다. 정상 35일 진행, UI 비용 지불, 연구 보너스 소모, 90일 종료·재착수는 해당 스크립트 검사로 증명하지 않는다.
