# 2026-09-09 일본 제국 영향력 inlay 화면 이탈 진단 및 최소 수정

## 1. 현재 판정

- 상태: **MINIMAL FIX IMPLEMENTED / FRESH STARTUP ACCEPTED / UI CONFIRMATION PENDING**
- 사용자 관찰: HoK `문민정부 강화` 완료 전 보이던 `제국의 영향력` 패널이 완료 후 중점 화면에서 보이지 않음 — `CONFIRMED`
- 수정 전 직접 source 결함: HoK 완료 상태용 `inlay_window.override_position` 누락 — `CONFIRMED`
- 화면 이탈 메커니즘: 패널이 기본 `X = 10000`에 남아 축소된 가로 스크롤 범위 밖으로 빠짐 — `STRONGLY_SUPPORTED`
- 패널 정의 삭제 또는 HoK reward의 직접 제국 영향력 modifier 제거 가설 — `DISPROVEN`
- 적용값: `HIDE` + HoK 완료/선택 flag 전용 `x = 2000`, `y = 700` override — source·정적 기하와 fresh startup `CONFIRMED`, 실제 UI 적합성 `UNPROVEN`
- 실제 runtime 영향력 state와 수정 후 동작 — `UNPROVEN / NOT RUN`

이 사건은 [HoK 일본 민주주의 전체 분기 통합 구현 기록](2026-09-09-japan-democratic-focus-integration-implementation.md)의 후속 UI 회귀다. 기존 기록의 미검증 항목이었던 `jap_imperial_influence_inlay_window`를 사용자 화면과 현재 source로 다시 조사했다.

## 2. 승인 범위

최초 요청은 문서화만 승인했으며 production은 변경하지 않았다. 후속 요청에서 AGENTS.md와 관련 `/docs`를 기준으로 D-JAP-18 최소 구현을 명시적으로 승인했다.

- production Paradox Script: `common/national_focus/japan.txt`의 HoK 전용 위치 override 1개만 수정
- localisation, GFX, descriptor, focus reward, gameplay state: 수정하지 않음
- 구현 단계의 게임 재실행, console 명령, save/load와 자동화: 당시 실행 중인 수정 전 세션을 임의 종료하지 않았으므로 수행하지 않음. 후속 23:24 세션은 사용자가 실행
- Git: 후속 요청에서 production과 문서의 분리 commit 및 `main` push 승인. tag와 Workshop 작업은 승인·수행하지 않음
- 수행한 작업: 기존 진단 증거 보존, production 최소 수정, 설치된 1.19.2 UI 기하 대조, 정적 검증과 문서 갱신

적용한 `x = 2000`은 target UI 수치와 현재 focus 좌표로 산정한 1순위다. fresh startup은 통과했지만 실제 화면을 확인하지 않았으므로 최종 runtime 좌표로 확정하지 않는다.

## 3. 기준선과 재현 증거

- 저장소: branch `main`, 조사 시작 시 HEAD `494bc15e354c8bcc210ea1afb00928e151213d8c`, working tree clean
- 관련 production 구현 commit: `b51df1e` (`feat(japan): restore HoK democratic focus branch for 1.19.2`)
- target: HOI4 `Operation Postern v1.19.2.0.a729 (8e71)`
- current log: 2026-09-09 22:03 시작, DLC 36개, active mod 1개인 Hearts of Korea, 1936 single-player 진입
- post-fix log: 2026-09-09 23:24 시작, 같은 HOI4 build `(68eb)`, DLC 36개, active mod 1개인 Hearts of Korea, 1936 single-player 3회 진입
- descriptor dependency: `Korean Language`; current log의 active mod 1개만으로 dependency의 실제 VFS 로드 여부는 증명하지 않음
- source 지원 경계: HoK root는 `Waking the Tiger`와 `No Compromise, No Surrender`를 모두 요구하고 player에게만 열림

`system.log` 273–275행과 298·312행은 위 target, DLC와 active mod 상태를 기록하며, `game.log` 8–9행은 1936 single-player 시작을 기록한다. 사용자가 제공한 전·후 화면에서는 완료 전 `제국의 영향력` 패널과 완료 후 HoK·SEA 공통 계통만 남은 중점 화면을 확인했다.

최초 문서화 때는 22:03 user-data 로그나 사용자 화면을 fixture로 복사하지 않았다. 후속 구현 시작 전에 실행 중인 22:03 세션의 `system.log`, `setup.log`, `game.log`, `error.log`, `code_revisions.log`를 `.local-artifacts/incidents/2026-09-09-d-jap-18/pre-implementation-2203-active/`에 보존했다. 이 폴더는 `.gitignore` 대상이며 화면 증거는 현재 대화에만 남아 있다. 보존 당시 게임 프로세스가 실행 중이었으므로 이 사본은 세션 최종본이 아니라 구현 전 활성 snapshot이었다.

23:24 post-fix 세션이 종료된 뒤 같은 5개 로그의 최종본을 `.local-artifacts/incidents/2026-09-09-d-jap-18/post-implementation-2324-final/`에 보존했다. `system.log:273-312`는 1.19.2 `(68eb)`, DLC 36개와 Hearts of Korea 단독 실행을, `game.log:8-9,22-23,36-37`은 1936 single-player 3회 진입을 기록한다. 관련 `inlay`, `focus`, `layout`, `relative_focus`, `mark_focus` parser 오류는 0건이다. 수정본 startup은 `CONFIRMED`지만 로그가 UI 위치를 기록하지 않으므로 패널 표시 성공은 `UNPROVEN`이다.

현재 로그는 `obsolete_focus_branches_visibility`의 실제 선택값을 출력하지 않는다. 다만 target `common/game_rules/00_game_rules.txt:3481-3488`의 기본값이 `HIDE`이고, 사용자 화면의 경쟁 정치 계통 제거와 source의 완료 후 relayout 결과가 `HIDE` 경로와 일치하므로 이 재현의 `HIDE` 조건은 `STRONGLY_SUPPORTED`로 둔다.

## 4. Source 증거

| 사실 | 근거 | 판정 |
|---|---|---|
| HoK root ID는 바닐라와 다른 `HOK_JAP_strengthen_civilian_government`다. | `common/national_focus/HOK_JAP_democratic_shared.txt:3` | `CONFIRMED` |
| HoK root는 바닐라 정치 root 6개와 상호배타다. | 같은 파일 `:6-13` | `CONFIRMED` |
| 완료 reward는 `HOK_JAP_democratic_branch_selected`를 먼저 설정하고 `HIDE`에서 `mark_focus_tree_layout_dirty = yes`를 실행한다. | 같은 파일 `:60-75` | `CONFIRMED` |
| relayout 때 경쟁 정치 계통은 HoK 완료/flag 조건으로 숨겨진다. | `common/national_focus/japan.txt:273-291`, `:7216-7233` 등 | `CONFIRMED` |
| SEA 공통 산업 root는 같은 HoK 완료/flag 조건에서 `x = -83`만큼 이동한다. | 같은 파일 `:25286-25299` | `CONFIRMED` |
| inlay 기본 위치는 `X = 10000`, `y = 700`이다. | 같은 파일 `:107-110` | `CONFIRMED` |
| 수정 전 9개 위치 override는 비HoK 또는 바닐라 정치 focus만 검사하며 HoK root ID와 선택 flag 참조는 0개였다. | 수정 전 같은 파일 `:112-226` | `CONFIRMED` |
| 기능상 대응하는 바닐라 `JAP_strengthen_civilian_government`만 `HIDE`에서 `x = 1500` override를 받는다. | 같은 파일 `:204-213` | `CONFIRMED` |
| 수정본은 기존 9개 override 뒤에 `HIDE` + HoK 완료/선택 flag 전용 10번째 override를 정확히 1개 추가한다. | 같은 파일 `:228-242` | `CONFIRMED` |
| target inlay 정의의 최상위 `visible = {}`는 비어 있고 `IS ALWAYS VISIBLE`로 표시돼 있다. | target `common/focus_inlay_windows/jap_imperial_influence_inlay_window.txt:7-9` | `CONFIRMED` |
| 일본 history는 `JAP_imperial_influence_dm`을 시작 시 추가하며 HoK root reward는 이를 제거하지 않는다. | `history/countries/JAP - Japan.txt:15-19`, HoK shared 파일 `:60-85` | `CONFIRMED` |

수정 전 production `japan.txt`의 inlay block은 앞의 contributor note를 제외하면 설치된 1.19.2 target의 기능 정의와 같았다. 수정본은 target의 기본 위치와 기존 9개 override를 byte-level diff상 그대로 두고, target에 없는 HoK 상태만 처리하는 10번째 override를 추가한다.

## 5. 원인 분류

### CONFIRMED — caller coverage 누락

HoK 이식은 별도 표시명과 ID를 가진 `HOK_JAP_strengthen_civilian_government`를 등록했다. 그러나 inlay의 위치 분기에는 기능상 대응하는 바닐라 ID `JAP_strengthen_civilian_government`만 남아 있다. 두 focus는 상호배타이므로 정상 HoK 진행에서 바닐라 완료 조건이 나중에 참이 되어 `x = 1500` 보정을 받는 경로도 없다.

완료 reward와 SEA 위치 offset에는 HoK 완료와 timing-safe flag를 모두 연결했지만, 같은 relayout의 소비자인 inlay 위치에는 그 조건을 연결하지 않았다. 직접 결함은 **ID 이식 뒤 inlay 위치 caller coverage를 갱신하지 않은 것**이다.

### STRONGLY_SUPPORTED — 화면 밖 잔류

HoK 완료 순간 경쟁 정치 계통이 숨겨지고 SEA 공통 계통이 `x = -83`으로 이동하면서 visible tree의 가로 범위가 축소된다. 일치하는 override가 없는 inlay는 full-tree용 기본 `X = 10000`에 남는다. 사용자 화면에서 패널이 없어지는 시점과 이 재배치 시점이 일치하므로, 패널이 새 스크롤 범위 밖에 남아 보이지 않는다는 설명이 가장 강하게 지지된다.

다만 엔진이 계산한 최종 inlay 좌표와 scroll bound는 로그에 출력되지 않았고 UI 디버그 값도 수집하지 않았다. 따라서 clipping 세부 메커니즘 자체는 `CONFIRMED`로 올리지 않는다.

### DISPROVEN, UNPROVEN 또는 관련 없음

- 패널 정의가 삭제되거나 `visible` trigger가 false가 됨: 정의가 존재하며 최상위 `visible`은 빈 블록이다. 이 가설은 `DISPROVEN`이다.
- HoK 완료 reward가 dynamic modifier를 직접 제거함: 시작 modifier는 source에 유지되며 해당 reward에 제거 effect가 없다. 이 직접 제거 가설은 `DISPROVEN`이다.
- 실제 runtime의 제국 영향력 modifier·tier·save state가 정상임: 이번 조사에서 runtime state를 조회하지 않아 `UNPROVEN`이다.
- parser 또는 focus-layout 오류로 창이 등록되지 않음: 현재 `error.log`에는 `inlay`, `layout`, `relative_focus`, `Error in focus`, `allow_branch` 또는 `mark_focus` 관련 오류가 없다.
- 현재 `recruit_character` 경고 7건과 별도 `cl_tech` 오류: 이 UI 위치 회귀와 직접 연결되는 증거가 없다.

## 6. 동작 영향

확인된 영향은 focus tree 안의 패널 접근성과 표시 위치다. 제국 영향력 수치, 네 세력의 tier, 관련 decision·focus 보너스와 save state의 실제 runtime 상태는 이번 조사에서 확인하지 않았으므로 `UNPROVEN`이다.

이 문제는 바닐라 inlay 자체의 고장이 아니라 새 HoK 정치 경로를 host tree에 통합하면서 빠진 경로별 위치 처리다. 따라서 target 좌표를 그대로 보존했다는 정적 검사는 통과했지만, HoK 완료 후 UI 계약은 실패했다.

## 7. 적용한 최소 수정과 검증 계약

`common/national_focus/japan.txt`의 기존 마지막 바닐라 override 뒤에 다음 계약의 블록 하나만 추가했다.

1. `HIDE`에서만 발동한다.
2. `has_completed_focus = HOK_JAP_strengthen_civilian_government`와 `has_country_flag = HOK_JAP_democratic_branch_selected` 중 하나를 만족하면 `x = 2000`, `y = 700`을 사용한다.
3. 완료 reward가 flag를 먼저 설정하고 기존 `mark_focus_tree_layout_dirty = yes`를 실행하므로 완료 effect 안의 재배치도 같은 상태를 읽는다.
4. 기본 `X = 10000`, target의 기존 9개 override, `visible`, GUI/GFX/localisation, 영향력 수치·tier·결정과 SEA `x=-83` offset은 변경하지 않는다.

좌표는 설치된 target `interface/nationalfocusview.gui:493-497,631-639`의 focus item `165x128`, spacing `96x130`, center offset `(130,32)`와 `interface/JAP_imperial_influence_scripted_gui.gui:24-29`의 inlay `620x670`을 사용해 산정했다. `y=700` 창과 수직으로 겹치는 row 5~10에서 HoK 최우측 item 경계는 약 `1735px`, SEA/군부 최좌측 item 경계는 약 `2914px`다. `x=2000..2620`은 이 빈 회랑에서 좌우 약 `265px`, `294px`를 남긴다. `x=6800`은 활성 tree 우측 끝보다 창이 약 `885px` 더 나가므로 clipping과 불필요한 스크롤 폭 위험 때문에 사용하지 않았다.

정적 검증 결과는 다음과 같다.

- production diff: 16줄 추가, 삭제 0줄, 한 파일의 한 블록
- inlay override: 기존 9개 + HoK 전용 1개, HoK focus/flag 참조 각각 1개
- 모든 위치의 `y = 700` 유지
- UTF-8 BOM과 LF 유지
- comment-aware brace/quote 검사 정상, 최종 brace depth 0
- `git diff --check` 오류 0

23:24 fresh 실행은 새 inlay/focus/layout 오류 없이 startup과 1936 진입을 통과했다. 기존 error 종류는 반복됐고, 유일한 신규 종류는 gamestate reset 때 OneDrive의 `random.log`를 `random_1.log`로 바꾸지 못한 6건이다. D-JAP-18과 연결되는 증거는 없다.

후속 runtime에서는 완료 직후 dirty relayout, focus 화면 재진입, save/load, `SHOW`, 기존 바닐라 정치 경로, 여러 해상도·UI 배율·줌과 패널 상호작용을 확인해야 한다. 정상 clean 1936 positive path는 단순 70일 대기가 아니라 root 진행 중 56일 뒤의 아이자와 사건 mission → 2·26 사건 HoK option → `complete_national_focus` 순서다. `Focus.AutoComplete` 클릭은 빠른 probe로만 별도 기록한다.

## 8. Git와 외부 상태

- 조사 시작 Git: `main` / `494bc15`, `origin/main`과 일치, clean
- 구현 시작 Git: 같은 branch/HEAD, D-JAP-18 문서 5개가 미커밋 상태였으며 그대로 보존
- 이번 작업의 production code 변경: `common/national_focus/japan.txt`의 HoK 전용 위치 override 1개
- 이번 작업의 문서 변경: 이 진단 기록과 기존 정렬 정책·통합 계획·구현 기록·검증 체크리스트의 상태 동기화
- Git: production 변경은 `9a80c6f`로 별도 commit. 구현·정적 검증 단계에서는 push/tag를 수행하지 않았으며 후속 요청에서 문서 commit과 `main` push를 승인받음
- 게임/launcher/playset/save/settings: 구현 단계에서 `hoi4.exe` PID 27032의 수정 전 세션을 종료하거나 reload하지 않음. 이후 사용자가 23:24 fresh 세션을 실행했고 현재 프로세스는 종료됨
- Workshop upload/update 또는 metadata 변경: 수행하지 않음
