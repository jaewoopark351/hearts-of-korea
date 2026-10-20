# 비전 1950 긴급 특별 건함계획 구현·검증 기록

작성: 2026-10-20. 상태: **구현·정적 확인 및 기록한 조건의 기능 검증 완료**.

## 범위와 기준

사용자의 「AGENTS.md, /docs 읽고 구현해줘」 요청에 따라 [설계](../HOK_KOREAN_VISION_1950_EMERGENCY_SHIPBUILDING_PLAN.md)의 해군 정책을 구현했다. 디시전은 「긴급 특별 건함계획 시행」, 국민정신은 「긴급 특별 건함계획」이며 회당 정치력 150, 180일간 함정 생산 비용 −50%, 횟수 제한 없는 반복이 목표다. 수송선에 대한 후속 답변 「보통 수송선에도 적용되지 않아?」를 반영해 수송선도 포함했다.

- 시작 브랜치: `feat/korean-focus-expansion-ai`.
- 기준 HEAD: `d4031aaa0c1f85bb89b0e6ca21d041beade8bd26`.
- 구현 시작 시 앞선 문서화 작업의 README 수정과 미추적 설계 문서가 있었다. 이 작업을 보존하고 그 위에 기능과 자산을 추가했다.
- 작업 원본: `C:/hoi/hearts_of_korea`. 실제 launcher `hearts of korea.mod`의 `path`도 이 저장소다. Workshop 원본과 게임 설치 파일은 수정하지 않았다.
- 설치 HOI4: `Operation Postern v1.19.3.0.c01a`, Steam build `25205862`, 설치 메타데이터 체크섬 `5632`. 실행 중 표시된 체크섬과 구분한다.
- 실제 사용자 데이터: `C:/Users/jaewo/OneDrive/문서/Paradox Interactive/Hearts of Iron IV`.
- 시작 시 게임은 메인 메뉴였으며 관측 체크섬은 `b244`였다. 활성 DLC 36개, 로컬 Hearts of Korea와 `Hearts of Korea English Translation (Anime Modder's Edition)` 2개 모드 구성이었다.
- descriptor가 요구하는 `Korean Language`는 이 실행 구성에 활성화되어 있지 않았다. 의존성을 제거하거나 playset을 바꾸지 않았으며 필수 의존성 포함 구성의 검증으로 주장하지 않는다.
- 작업 시작 시 사용자 데이터의 `save games` 디렉터리는 없었고 저장 수는 0이었다. 이후 이 검증에서 만든 저장과 구분하며 과거 기록의 저장 71개를 시작 인벤토리로 사용하지 않는다.
- 진단·백업·로그·화면·테스트 도구는 `C:/hoi/test/vision1950-20261020-01/`에 둔다.

이는 기존 결함의 호환성 수리가 아니라 명시적으로 요청된 계속개발이다. 기존 비전 1950과 단계별 해군 목표는 보존하며 새 한시 정책을 추가한다.

## 소스 변경과 의도

| 파일 | 변경 및 보존 내용 |
|---|---|
| [한국 중점](../../common/national_focus/korea.txt), 2883~2888행 | 기존 국민정신·해군 경험치 50 뒤에 새 **개별 디시전**의 `unlock_decision_tooltip`을 추가했다. 중점 ID·35일·선행조건·배치·AI는 보존했다. |
| [한국 디시전](../../common/decisions/KOR_decision.txt), 681~700행 | 기존 `KOR_vision_1950_category`에 `HOK_KOR_enact_emergency_special_shipbuilding`을 추가했다. 중점 완료 후 표시·사용, 비용 150, `fire_only_once = no`, 추가 대기기간 0이다. |
| [새 국민정신](../../common/ideas/HOK_KOR_emergency_shipbuilding.txt) | `HOK_KOR_emergency_special_shipbuilding`을 별도 정의했다. 8개 함정 archetype에 `build_cost_ic = -0.5`, `instant = yes`를 지정했다. |
| [한국어](../../localisation/korean/HOK_KOR_emergency_shipbuilding_l_korean.yml)·[영어 헤더 쌍](../../localisation/english/HOK_KOR_emergency_shipbuilding_l_english.yml) | 확정 이름과 건함 목적, 정치력·지속기간·반복 조건을 같은 한국어 본문으로 제공한다. 각 locale 헤더와 UTF-8 BOM, 동일 기여자 메모를 갖춘다. |
| [전용 GFX](../../interface/HOK_KOR_emergency_shipbuilding_icons.gfx) | 프로젝트 내부 상대경로로 소형 디시전 및 국민정신 자산을 연결했다. 기존 비전 1950 그림은 유지했다. |

국민정신 적용 중에는 `NOT = { has_idea = HOK_KOR_emergency_special_shipbuilding }`가 사용을 막는다. 표시 자체는 유지하며, 만료 뒤 같은 비용으로 다시 사용할 수 있다. 중첩·기간 갱신과 추가 cooldown 없이 무제한 반복하는 구현 방식이다. 이 세부 방식은 최초 명명·수치 요구와 구분해 설계에서 제안했고 후속 구현 범위에서 채택했다.

`complete_effect`에서 `add_timed_idea = { idea = HOK_KOR_emergency_special_shipbuilding days = 180 }`를 실행한다. 별도 180일 사업 타이머나 삭제 효과를 두지 않아 국민정신 만료가 재사용 조건을 결정한다. AI는 `factor = 1`로 같은 비용과 사용 조건을 따른다. 별도 전쟁·연도·정부 이념·함대 수량 조건은 추가하지 않았다.

적용 archetype은 `ship_hull_light`, `ship_hull_cruiser`, `ship_hull_heavy`, `ship_hull_carrier`, `ship_hull_submarine`, `support_ship_hull`, `repair_ship_hull`, `convoy`다. 초중전함·개장 항모·특수 잠수함 등은 해당 선체의 archetype을 따른다. 미사일 자체나 함재기는 대상에 추가하지 않았다.

기존 `KOR_vision_1950`의 조선소 생산량 +20%는 별도로 유지한다. 새 −50%는 생산 비용 보정이며 조선소 생산량 +50%로 대체하지 않는다. 기존 1~3단계의 함대 규모 조건·일회 보상·전역 플래그·뉴스·업적 연결을 수정하지 않았다. 새 중점은 없으며 전체 중점 수 472개도 유지했다.

## 대상 버전의 문법 근거

다음은 설치된 HOI4의 직접 소스·문서에서 확인했다(`CONFIRMED`). 경로는 게임 설치 루트 기준이다.

| 근거 | 확인한 내용 |
|---|---|
| `common/ideas/usa.txt:751~788`, `bureau_of_ships_focus` | country idea의 `equipment_bonus`에서 전투함 5개 archetype에 `build_cost_ic`와 `instant = yes`를 함께 사용한다. |
| `common/ideas/britain.txt:366~367`, `common/ideas/usa.txt:1007~1009` | `convoy`에 같은 생산 비용 감소 형식을 사용한다. |
| `common/units/equipment/ship_hull_heavy.txt:576~580` | 초중전함 `ship_hull_super_heavy_1`의 archetype은 `ship_hull_heavy`다. |
| `common/units/equipment/ship_hull_submarine.txt:1165~1169` | `nuclear_missile_submarine`의 archetype도 `ship_hull_submarine`이다. |
| `common/units/equipment/ship_hull_light.txt:372~375` | 구형 명칭 `destroyer_1`도 `ship_hull_light`를 사용한다. 같은 선체군을 구형·MTG 이름으로 중복 나열하지 않았다. |
| `common/units/equipment/support_ships.txt:3,22,24,71`, `repair_ships.txt:3,22,24,69` | 지원함·수리함은 `type = support_ship`인 별도 archetype이다. |
| `documentation/effects_documentation.md:1180,1188` | 장비 보너스는 국민정신과 같은 사용법이다. `instant = yes`는 즉시 적용하며 생략하면 새 variant 생성에 적용한다고 설명한다. |
| `documentation/effects_documentation.md:2244~2263` | `add_timed_idea`는 country scope에 기간제 국민정신을 부여한다. |
| `common/decisions/ENG.txt:7205~7240` | 중점으로 표시하고 국민정신 보유 중 차단하며 180일 국민정신을 즉시 주는 반복 디시전 사례다. |

지원함·수리함을 `equipment_bonus`로 변경하는 같은 바닐라 국민정신 사례는 찾지 못했다. 유효 archetype에 같은 형식을 적용하는 구현이며 이 두 함종의 실제 비용은 별도 관측 대상이다. 문법 사례만으로 모듈 포함 설계 비용·개장 비용·생산선 진행률·비용 하한·만료 재계산을 확인했다고 주장하지 않는다.

## 이미지와 출처

두 그림은 내장 `image_gen.imagegen`으로 각각 새로 만든 AI 래스터 자산이다. 원작자 그림으로 표시하거나 외부 작가·라이선스를 임의로 부여하지 않았다. 해군 남색·슬레이트 계열, 디시전은 군함과 망치, 국민정신은 조선소 크레인과 건조 중인 선체다.

- 디시전 DDS: `gfx/interface/decisions/HOK_KOR/emergency_shipbuilding/emergency_special_shipbuilding.dds`, 32×32.
- 국민정신 DDS: `gfx/interface/ideas/HOK_KOR/emergency_special_shipbuilding.dds`, 60×68.
- 채택 원본: `docs/assets/korean-emergency-shipbuilding/`. 프롬프트·생성일·도구·참조 없음·실제 모델 식별자 비공개 상태를 보존했다.
- 제작·기여·해시·변환·정적 미리보기의 상세 범위는 [이미지 출처 기록](../HOK_KOREAN_EMERGENCY_SHIPBUILDING_ASSET_CREDITS.md)과 [매니페스트](../data/HOK_KOREAN_EMERGENCY_SHIPBUILDING_ICON_MANIFEST.json)에 있다.

## 정적 확인과 독립 검토

`validation/static_review.py`의 결과 `validation/static-review.json`은 **86 PASS / 0 FAIL**이다. 두 경로는 위 외부 테스트 루트 아래에 있다. 검사 범위는 순서를 보존한 구조·참조·수치·인코딩·기존 콘텐츠 보존이며 완전한 엔진 스키마 검증이 아니다.

기존 중점 블록·선언 순서·좌표·AI·보상과 관련 없는 바이트 보존, 기존 디시전 단계 보존, 새 해금·비용·기간·반복·8개 archetype, 현지화 쌍·BOM·스프라이트 연결을 확인했다. ID·스프라이트 유일성 검사는 저장소, 설치 바닐라, 활성 영어 번역 모드 `C:/hoi/Hearts of Korea English Translation Anime Modder's Edition`, 선언된 `Korean Language` 다운로드 사본 `Workshop/394360/2743487021` 범위에서 충돌이 없었다. 이 범위의 결과를 모든 외부 모드에 대한 보장으로 확대하지 않는다.

`git diff --check`도 통과했다. 외부 `validation/profile-preservation.json`은 작업 전후 `settings.txt`·`dlc_load.json`·launcher `mod/hearts of korea.mod`의 SHA-256이 모두 같음을 기록한다. 게임 설정·playset·로컬 descriptor를 변경하지 않았다.

독립 소스 검토에서도 이 범위에서 수정이 필요한 결함은 발견하지 못했다. `instant = yes`와 적용 형식은 설치 근거에 부합한다. 실제 비용 합산·하한, 개장, 만료 뒤 복원은 이 검토의 통과 주장에 포함하지 않는다. 이미지 정적 검수와 실제 게임 내 표시는 구분한다.

## 실제 실행 관측과 진행 중인 검증

### 임시 진단이 없는 초기 새 게임

최종 기능·자산 소스로 프로세스를 완전히 다시 시작한 `-debug` 실행에서 체크섬 **0655**, 활성 DLC 36개·모드 2개가 기록됐다. 1936 한국을 새로 시작하여 일시정지 상태로 진입했다. 이 단계에는 임시 테스트 디시전이 없었다.

외부 `validation/logs-clean-paused/error-comparison.json` 비교는 기존·현재 모두 오류 128개, 정규화한 고유 오류 40개이며 **새 정규화 오류 0개**, 사라진 고유 오류와 기존 빈도 차이도 없었다. 이는 같은 기존 실행 구성의 로드 비교이며 바닐라·필수 의존성 전용 대조나 새 기능 실행 증명이 아니다.

중점 완료 전 초기 디시전 목록에서 신규 항목은 보이지 않았다. 생산 화면의 적용 전 비용은 외부 `runtime-ui/01-before-focus.png`~`04-submarine-costs-before.png`에 기록했다.

### 강제 조건 준비와 실제 첫 사용

입력 경로에서 마우스는 작동하지만 grave·Escape·space 키가 기대한 동작을 만들지 못해 콘솔 명령 대신 한정 수동 fixture를 사용했다. 기존 한국 디시전 분류 안에 AI 가중치 0의 임시 버튼 4개를 삽입해 중점 완료·정치력 149/500·관측 조건을 준비했다. 실제 신규 정책 버튼은 fixture가 실행하지 않았으며 사용자가 보는 원래 디시전 UI에서 직접 클릭했다. 도구·원본 백업·임시 블록은 외부 `validation/manual-fixture/`에 보존했다. 이 hot reload는 탐색 진단이며 최종 재시작 검증과 구분한다.

`validation/logs-manual-first-use/game.log`의 원시 로그에는 **11개 PASS**가 있다. 중점 완료, 기존 국민정신 존재, 신규 국민정신 부재, 기존 조선소 보상 +0.2 및 해군 경험치 +50, 실제 사용 후 정치력 −150·잔액 350·신규 국민정신 존재·기존 국민정신과 기록한 보상 유지의 검사다. 초기 조선소 보정 −0.099→0.101, 경험치 0→50을 기록했다. `has_dlc = "Man the Guns"`도 실제 참으로 기록됐다. 강제 완료이므로 선행 중점과 35일 정상 진행은 증명하지 않는다.

엔진이 로그 문자열의 대괄호 prefix를 해석하면서 제거해 보존 도구의 prefix 필터는 `diagnostic_lines = []`를 남겼다. 이것을 진단 미실행으로 해석하지 않는다. 위 PASS와 `MAN_THE_GUNS_ENABLED`, `actual_UI_pp_delta=-150`은 원시 `game.log`에서 직접 확인했다.

| 실제 UI 관측 | 증거·범위 |
|---|---|
| 중점 강제 완료 후 정치력 149에서 표시되지만 사용 불가 | `runtime-ui/05-unlocked-blocked-at-149.png` |
| 일시정지 상태 정치력 500에서 실제 정책 클릭 → 350 | `06-first-use-pp350.png`, 원시 로그의 `actual_UI_pp_delta=-150` |
| 신규 국민정신 그림·이름과 8개 함종군 생산 비용 −50% 표시 | `07-spirit-effects-expiry-june30.png`. UI 효과 목록 관측이며 모든 설계의 실제 비용 검증과 구분 |
| 만료일 툴팁 1936년 6월 30일 | 같은 화면. 정확한 만료 시각은 이 툴팁만으로 판단하지 않으며 아래 자연 진행 결과와 구분 |

기존 설계 선택 화면의 비용도 변경됐다. 아래는 `02-production-costs-before.png`~`04-submarine-costs-before.png`, `08-submarine-costs-active.png`·`09-production-costs-active.png` 및 자연 만료 뒤 `13-production-costs-restored.png`·`14-submarine-costs-restored.png`의 실제 표시값이다.

| 생산 대상 | 적용 전 | 적용 중 | 자연 만료 뒤 |
|---|---:|---:|---:|
| 수송선 | 70 | 35 | 70 |
| Chungmugong Yi Sunshin Class | 7962 | 4777 | 7962 |
| Yi Sabu Class | 2857 | 1587 | 2857 |
| Eulji Mundeok Class | 3687 | 2182 | 3687 |
| Incheon Class | 1150 | 650 | 1150 |
| Type VII-K Class | 495 | 270 | 495 |
| Type II-K Class | 440 | 240 | 440 |

−50%는 생산 비용 보정으로 합산된다. 예를 들어 잠수함의 기존 비용 +10%에 −50%가 더해지므로 적용 전 표시 비용의 정확한 절반이 아닌 495→270·440→240이 된다. 기존 설계 비용이 즉시 변하는 것은 확인했지만 실제 생산 완료·진행 중 생산선·모듈별 및 개장 비용까지 이 표로 증명하지 않는다. 항공모함·지원함·수리함 등 나머지 함종의 실제 비용도 별도 확인 대상이다.

### 저장 실패 구분과 진단 제거 후 재불러오기

1936년 1월 1일 첫 사용 상태에서 정상 저장 UI를 실행했으나 엔진이 `continue_game.temp`→`continue_game.json`, `KOR_1936_01_01_12_temp.hoi4`→최종 저장명 변경에 각각 `errno 2`를 기록했다. 저장 완료 성공으로 표시하지 않는다. 사용자 데이터 안에서 파일을 수동 복사·이동·이름 변경하지 않았다. 남은 임시 저장은 외부 `save-evidence/first-use-temp.hoi4`에 먼저 백업했다. 원본은 45,571,274바이트, SHA-256 `e1aaada62cc1293896e499f55f317785d70f626a177bc07485ecd8385c7c23b7`이다.

이전 [2026-10-12 기록](2026-10-12-korean-civic-revision.md)의 같은 최종명 변경 실패와 임시 파일 직접 불러오기 사례를 확인했다. Unicode·OneDrive가 원인이라는 가설은 격리 검증하지 않았으므로 `UNPROVEN`이다. 당시 사례만으로 현재 저장이 정상이라고 판단하지 않고 실제 Load를 진행했다. 읽기 전용 조사 내용은 외부 `validation/save-rename-review.json`에 있다.

임시 진단 블록을 정확히 제거하고 한국 디시전 파일을 최종 소스 SHA-256 **`fd620cc464f8f5c6229a000e6987d010a4bacf2de560435e295b2fd5c8cb929c`**로 복구했다. 정적 검사를 다시 실행해 **86 PASS / 0 FAIL**을 얻었다. 전체 프로세스를 다시 시작한 PID 13584의 체크섬은 **0655**였다.

최종 소스의 정상 불러오기 UI에서 사용자 데이터의 원래 `KOR_1936_01_01_12_temp.hoi4`를 직접 선택하자 로드됐다. 정치력 350, 기존·신규 국민정신, 6월 30일 만료일이 유지됐다(`runtime-ui/10-final-source-reload-spirit-timer.png`). 이는 이번 신규 합성 저장의 재불러오기이며 변경 전 기존 저장 호환 증명은 아니다.

다만 이 로드에는 삭제된 임시 디시전 ID가 저장에 남아 **추가 오류 8개·고유 메시지 5개**가 발생했다. `validation/logs-final-source-save-reload/error-comparison.json`은 기준 128/40에서 136/45로 증가했으며 invalid decision·decision_to_remove·duplicate decision 메시지를 보존한다. fixture가 들어 있던 저장의 잔재 경고로 구분하며 **조용한 최종 소스 로드라고 주장하지 않는다**. 아래 최종 새 게임 재시작과 별도 실행이다.

불러온 게임을 자연 진행한 1월 21일, 국민정신 적용 중 정책 버튼을 눌러도 정치력 394가 유지됐다. 목록의 `NOT has_idea` 조건은 빨간색으로 표시됐다(`runtime-ui/11-active-blocked-after-reload.png`). 적용 중 실제 재사용 차단을 확인했다.

### 자연 만료·비용 복귀와 두 번째 실제 사용

임시 진단을 제거한 최종 소스 PID 13584에서 정상 UI 속도 5/4로 시간을 진행했다. 국민정신 제거·기간 단축·날짜 이동 명령은 사용하지 않았다. 마지막으로 일시정지한 6월 23일에는 신규 국민정신과 사용 차단이 남아 있었고, 다음 일시정지인 **7월 4일 13시**에는 디시전이 녹색 사용 가능 상태로 돌아왔다. 자연 만료와 해제는 관측했으나 6월 30일의 정확한 만료 시각은 직접 보지 못했다. 180일은 소스와 만료일 툴팁으로 확인한 범위다.

`runtime-ui/12-expired-decision-available.png`에서 정치력 754와 사용 가능 상태를 확인했다. 같은 일시정지 상태의 `13-production-costs-restored.png`·`14-submarine-costs-restored.png`에서 위 7개 대상 비용이 적용 전 값으로 모두 복귀했다. 단일 국민정신 만료 뒤 기존 설계 비용이 복원되는 것을 확인했으며 나머지 함종·개장·진행 중 생산선까지 확장하지 않는다.

같은 7월 4일 일시정지 상태에서 원래 정책 버튼을 다시 클릭하자 **정치력 754→604**, 정확히 150이 차감됐다(`15-second-use-pp604.png`). 다시 받은 국민정신에는 8개 효과 −50%와 **12월 31일 만료일**이 표시됐다(`16-second-spirit-expiry-dec31.png`). 기존 비전 1950 국민정신과 해군 경험치 50도 남아 있었다. 횟수 상한을 두지 않은 소스와 실제 두 번째 사용은 확인했지만 두 번째 만료나 임의 횟수의 장기 반복까지 실행한 것은 아니다. 추가 대기기간 0은 소스로 확인했고 실제 사용 가능은 7월 4일에 보았으며, 만료 직후 같은 시간 단위에 재사용했는지는 관측하지 않았다.

외부 `validation/logs-natural-expiry-second-use/error-comparison.json`은 오류 **138개·고유 47개**다. 추가분은 앞서 기록한 합성 저장의 진단 잔재 오류 8개와, 7월 1일 자동저장이 다시 기록한 `continue_game.temp` 및 `autosave_temp.hoi4` 최종명 변경 실패 2개다. 비교에서 새 정책 정의·효과의 생산 파일 오류는 추가로 발견되지 않았다. 이 실행 역시 조용한 새 게임 로그로 표시하지 않는다.

### 최종 소스의 일반 실행·새 게임 확인

임시 진단이 없는 최종 소스로 **전체 프로세스를 다시 시작**했다. 21시 11분 40초에 시작한 PID 25516은 `-debug` 없이 일반 실행했으며 메인 메뉴는 `Operation Postern v1.19.3.0.c01a (0655) (S)`를 표시했다. 디버그 표시는 없었다. 합성 저장을 불러오지 않고 정상 UI로 1936 한국을 새로 시작해 1월 1일 12시 일시정지 상태에 진입했다. 기존과 같은 DLC 36개·모드 2개 구성을 유지했다. 새 게임 화면과 중점 완료 전 디시전 목록은 외부 `runtime-ui/17-final-clean-newgame.png`·`18-final-preunlock-decisions.png`에 보존했다.

외부 `validation/logs-final-normal-clean-newgame/error-comparison.json`은 기준·현재 모두 오류 **128개·고유 40개**, 새 정규화 오류 **0개**, 사라진 고유 오류 **0개**, 기존 빈도 차이 없음이다. 합성 저장의 삭제된 진단 ID 경고와 재진행 자동저장 경고는 이 새 게임에서 나타나지 않았다. 이는 기존 경고가 남은 실제 playset과의 비교이며 오류 0개나 필수 언어 모드 포함 구성의 통과를 뜻하지 않는다.

검증을 마친 게임은 창 닫기로 종료했다. 게임이 만든 `KOR_1936_01_01_12_temp.hoi4`와 `autosave_temp.hoi4`는 실제 사용자 저장 폴더에 보존하고 외부 `save-evidence/`에도 복사했다. 파일·화면 해시와 최종 상태는 외부 `validation/final-status.json`에 기록했다. 사용자 설정·playset·로컬 descriptor는 `validation/profile-preservation.json`의 작업 전후 SHA-256이 모두 같다.

### 남은 검증

중점 보상 화면의 해금 안내와 원래 선행 중점·35일 정상 진행, 항모·지원함·수리함 등 8개 함종군 전체의 실제 설계 비용, 개장·생산 진행·정상 최종명 저장 성공, 정확한 만료 시각과 만료 직후 즉시 재사용, 장기 AI·여러 회 반복, DLC 비활성 조합, 변경 전 기존 저장 호환과 멀티플레이는 확인하지 않았다. 기록한 비용·첫 사용·적용 중 차단·재불러오기·자연 만료·두 번째 사용·최종 일반 실행 새 게임의 통과를 이 범위로 확대하지 않는다.

## Git·외부 작업 상태

변경은 작업 트리에 남아 있다. 커밋·푸시·태그·릴리스·Workshop 업로드나 메타데이터 변경을 수행하지 않았다. 구현과 기록한 조건의 기능 검증·최종 일반 실행 새 게임 확인은 마쳤으며 위 미검증 항목은 별도로 남긴다.

## 같은 날 후속 요청 — 비전 1950 조선소 생산량 강화

사용자의 「조선소 생산량 20% → 30%」 요청에 따라 `common/ideas/korea.txt`의 기존 `KOR_vision_1950`에 있는 `industrial_capacity_dockyard`만 `0.2`에서 `0.3`으로 변경하고 기여자 메모를 추가했다. 기존 ID·허용 조건·그림·해군 경험치 50·디시전 해금과, 별도 긴급 건함계획의 비용 −50%·정치력 150·180일·반복 조건은 유지했다. 현재 명세의 수치도 +30%로 갱신했다.

브랜치와 HEAD는 위 기준과 같으며 앞서 구현한 작업 트리를 보존했다. 변경 전 파일은 `C:/hoi/test/vision1950-dockyard30-20261020-01/before/korea.txt`에 보관했다. 소스 차이·줄바꿈·인코딩 보존과 공백 오류를 확인했으며 후속 조정에서 게임을 실행하지 않았다. 위 +20%·보상 차이 +0.2·체크섬 0655·86개 검사·실제 UI 관측은 강화 전 증거로 보존하며 +30%의 런타임 검증으로 재사용하지 않는다. 커밋·푸시·업로드는 하지 않았다.
