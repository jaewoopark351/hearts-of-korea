# 포항 제철소 확장의 포항제철 중점 연계 구현

작성: **2026-11-07 (Asia/Seoul)**. 상태: **소스 적용·독립 소스 검토·핵심 실행 검증 및 시험 환경 복구 완료**.

이 기록 이후 사용자가 강원·포항 설명문의 별도 이용 안내 문단을 삭제하도록 요청하여 배경 문단만 남겼다. 설명문을 검토·수정할 때는 [최신 설명문 정리](../HOK_KOREAN_REPEATABLE_RESOURCE_PROSPECTING_SPEC.md#12-2026-11-07-강원포항-설명문-간소화)를 먼저 읽는다. 아래의 수치·조건 설명문 화면과 소스 해시는 간소화 전 검증 이력이며, 후속 문구 변경을 재실행한 증거가 아니다.

## 승인 범위와 이전 기록

사용자는 「포항제철」 중점을 완료한 뒤 「포항 제철소 확장」에 착수하도록 하는 동작과 설명문을 먼저 설명·문서화하도록 요청했다. 그 단계의 미구현 상태는 [반복 자원 탐사 명세 10절](../HOK_KOREAN_REPEATABLE_RESOURCE_PROSPECTING_SPEC.md#10-2026-11-07-포항제철-중점-연계와-설명문--문서화만)에 남겼다. 이후 같은 구현 설명을 인용해 **“AGENTS.md, /docs 읽고 구현해줘”**라고 요청하여 이번 소스 적용과 필요한 검증을 진행했다. 커밋·푸시·Workshop 게시·원본 수정은 승인 범위에 포함되지 않는다.

이 작업은 의도적인 후속 콘텐츠 조건 변경이다. 엔진 호환성 결함 수리가 아니며, [중점 연계 전 두 사업의 구현·검증 기록](2026-11-06-korean-repeatable-resource-prospecting.md)을 새 중점 조건의 검증으로 사용하지 않는다.

## 기준과 출처

| 역할 | 위치·확인 내용 |
|---|---|
| 작업 소스 | `C:\hoi\hearts_of_korea` |
| 브랜치·HEAD | `feat/korean-focus-expansion-ai` / `f927b3a5defe046967413da05069a0f92823fbec` |
| 시작 작업 트리 | 기존 README·과거 자원 메모 변경, 미추적 자원 탐사 소스·명세·자산·검증 기록을 보존. 이번 작업은 그 파일들을 기준으로 이어감 |
| 실제 launcher HOK 경로 | 사용자 데이터 `mod/hearts of korea.mod` → `C:/hoi/hearts_of_korea` |
| 실제 활성 순서 | `mod/hearts of korea.mod` → `mod/Hearts of Korea English Translation Anime Modder's Edition.mod` |
| 활성 번역 물리 경로 | `C:\hoi\Hearts of Korea English Translation Anime Modder's Edition`; 읽기 전용. 이번 디시전 정의·설명 키나 한국 중점 파일의 대체본은 없음 |
| 설치 원본 | `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`; 읽기 전용 |
| 역사적 원작 | `C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\2898629778`; 읽기 전용. 원작 포항 중점의 강철 +25 보상 확인. 원작의 옛 주 ID를 현행 코드에 옮기지 않음 |
| 실제 사용자 데이터 | `C:\Users\jaewo\OneDrive\문서\Paradox Interactive\Hearts of Iron IV` |
| 설치 build | Steam build `26409260` |
| 실행 전 남아 있던 로그 | `Operation Postern v1.19.4.2.2da5 (5d1b)`, DLC 36개·모드 2개. `game.log` 마지막 날짜 `1936.12.02.03`, `error.log` 마지막 날짜 `1936.12.09.16`. 새 조건의 실행 증거가 아님 |
| 표시 환경 | `l_korean`, 1280×720, GUI 1.0 |
| descriptor | HOK는 `supported_version="1.19.*"`, `Korean Language` 의존성, successor ID `3793992662`. HOK·활성 번역에 `replace_path` 없음. 이번에 변경하지 않음 |

시작 시 HOI4·dowser·Paradox Launcher 프로세스는 없었고 Steam만 실행 중이었다. Steam의 녹색 플레이 버튼을 확인했다. 선언된 Korean Language 의존성과 실제 두 모드 구성의 차이는 변경하지 않았다.

설치 원본의 같은 문맥 근거는 다음과 같다.

- `common/decisions/resource_prospecting.txt:84–103`: 국가 scope의 `available` 안에서 `has_completed_focus`를 검사하는 `establish_jaykaynagar_aliminium_smelters`.
- 같은 파일 `:3775–3795`: `develop_katanga_cobalt_deposits`의 중점 완료 검사.
- `common/national_focus/sweden.txt:167–194`: `completion_reward`의 단일값 `unlock_decision_tooltip = SWE_urbanization_decision`.

## 적용한 변경

| 파일 | 변경 |
|---|---|
| [디시전 정의](../../common/decisions/HOK_KOR_resource_prospecting.txt) | 포항 디시전의 국가 scope `available`에 `KOR_pohang_iron__steel_company` 완료 조건 추가. 기존 `visible`의 경상 소유 조건 유지 |
| [한국 중점](../../common/national_focus/korea.txt) | 「포항제철」의 국가 scope `completion_reward`에 포항 디시전 해금 안내 추가. 경상 강철 +25 보상 유지 |
| [한국어 현지화](../../localisation/korean/HOK_KOR_resource_prospecting_l_korean.yml) | 포항제철 설립 이후의 증설 배경과 중점 완료·건설 II 요구를 포함하는 설명문 적용 |
| [영문 헤더 현지화](../../localisation/english/HOK_KOR_resource_prospecting_l_english.yml) | 기존 프로젝트 계약에 따라 같은 한국어 본문 적용 |

포항 디시전은 경상 소유 등 기존 표시 조건을 충족하면 중점 미완료 상태에서도 목록에 표시되고, 새 중점 조건과 기존 착수 조건을 모두 충족해야 실행할 수 있도록 설계했다. 해금 안내는 개별 디시전을 가리키며 범주 전체 해금이나 즉시 공사 시작 효과가 아니다.

기존 정치력 25·민공 9개 점유·90일·경상 기본 강철 +9·상한 없는 반복·취소·환불·AI는 보존했다. 새 중점 조건을 취소 조건에 추가하지 않았다. 강원 디시전 전체, 기존 포항 중점 배치·선행 관계·보상, 국가·주·중점·디시전·현지화 ID도 보존했다. production 변경 위치에는 `#20261107_kpopmodder: ...` 기여 주석을 추가하고 앞선 주석을 유지했다.

## 외부 증거와 소스 검토

이번 작업 루트는 **`C:\hoi\test\hok-pohang-focus-gate-20261107-01\`**다. 이전 작업 루트 `C:\hoi\test\hok-resource-prospecting-20261106-01\`는 중점 연계 전 증거로 그대로 보존했다. 과거 helper는 실행하지 않았으며 새 시험의 출력·설정 백업을 새 작업 루트로 분리했다.

- `baseline.json`, `source-before/`, `source-before-manifest.json`: 시작 브랜치·HEAD·작업 트리와 게임 파일 4개·문서·descriptor 등의 변경 전 사본 및 해시.
- `baseline-logs/`: 새 실행 전에 보존한 기존 로그 사본. 실제 로그 원본을 지우거나 회전시키지 않음.
- `user-config-before/`, `config-before-manifest.json`: 시작 설정 4개 원본과 해시.
- `user-saves-before.json`: 기존 사용자 저장 34개의 길이·SHA-256. 게임 생성 저장 원본은 실제 사용자 데이터에 두고 시험 증거 사본만 외부 작업 루트에 둠.
- `apply_pohang_gate.py`, `source-applied-manifest.json`: 정확한 변경 전 바이트를 확인하고 4개 파일만 국소 변경한 helper와 적용 후 해시.
- `independent-source-review.json`: 독립 읽기 검토 **24개 통과·실패 0개**. 추가한 두 행씩을 제거하면 디시전·중점이 각각 변경 전 사본과 바이트 일치. 현지화는 새 주석과 포항 설명문만 되돌리면 변경 전 바이트와 일치.
- `final-source-manifest.json`, `independent-source-review-final.json`: 실제 UI의 모서리 괄호 표시 문제를 보정한 최종 4파일 해시와 독립 읽기 검토 **26개 통과·실패 0개**. 초기 해시·검토는 덮어쓰지 않았다. 두 현지화에서 중점 이름을 `§Y포항제철§!`로 강조한 부분만 최초 적용 이후 바뀌었다.

소스 검토에서 gate와 해금 안내의 국가 scope, 기존 비용·기간·보상·AI·강원 블록 보존, 현지화 BOM·CRLF·헤더 직후 동일 기여 주석·같은 본문, 키·ID 중복과 활성 번역 덮어쓰기 부재를 확인했다. `git diff --check`도 통과했다. 이 검토는 실제 UI·보상·저장 호환성의 통과를 뜻하지 않는다.

## 실행 검증과 마감

### 외부 준비와 실제 UI

`profile.py apply`는 현재 설정 사본과의 일치를 확인한 후 고유한 임시 launcher descriptor `HOK_pohang_gate_20261107_test.mod`를 만들고, 원래 두 모드 뒤에 외부 `runtime-probe/`만 추가했다. 자동 저장을 끄고 텍스트 저장을 사용하도록 한 임시 변경도 같은 백업을 복구 기준으로 삼는다. 시험 game PID는 **13584**, 인자는 `-debug -start_tag=KOR -start_speed=0 -force_text_save`, 체크섬은 **d6c3**, DLC는 36개였다. `-ai_testing`은 사용하지 않았다.

외부 fixture는 새 한국 게임에 건설 II·정치력 500·합성 offsite 민공 30개를 한 번 준비하고, 상태 기록과 실제 포항제철 중점 강제 완료 버튼만 제공한다. 생산 디시전·보상·기간은 복제하거나 단축하지 않았다. 일일 관측은 시작·종료 전환과 30일 간격으로 제한하고 400일 뒤 중단한다. 벽시계 진행을 위한 속도 define은 시험 overlay에만 있다. 원본의 COUNTRY `complete_national_focus` 근거는 `documentation/effects_documentation.md:2870`, 실제 사용은 `events/AAT_Denmark.txt:2179`다. 이 준비는 정상 연구·건설·35일 중점 진행의 검증이 아니다.

초기 준비 직후 가용 민공은 아직 집계 전이었다. 실제 달력을 1936.1.3.4까지 진행한 다음 포항 툴팁에서 **포항제철 완료만 거짓**, 비항복·건설 II·가용 민공·경상 소유·완전통제는 참인 것을 확인했다. 강원 사업은 사용 가능했다. `ui/before-focus-blocked-glyph-issue-0.jpg`가 이 시점의 증거다. 같은 화면에서 설명문의 `「」`가 `?`로 표시되어 두 현지화의 그 이름만 게임 강조 표기로 보정했다. debug 재표시에서 정상 글자를 관측했지만 최종 확인은 완전 재시작 결과와 구분한다.

실제 포항제철 중점 상세 창과 툴팁에는 **결정 잠금 해제: 포항 제철소 확장**과 기존 **경상 강철 +25**가 함께 표시됐다(`ui/pohang-focus-reward-and-unlock-0.jpg`). 외부 조작판으로 실제 중점을 강제 완료한 뒤 같은 날짜에 포항 조건이 충족됐고(`ui/after-focus-available-0.jpg`), 실제 포항 사업 버튼을 눌러 UI 정치력 **502→477**과 **90일**을 확인했다. 활성 툴팁은 민공 9개·강철 +9·반복·취소 및 보정한 설명문을 표시했다(`ui/first-expansion-active-tooltip-0.jpg`).

### 저장과 두 차례 정상 완료

저장 원본은 사용자 데이터 `save games`에 그대로 두고 새 작업 루트의 `saves/`에 증거 사본을 보존했다. 파일별 `*-copy-manifest.json`과 `*-analysis.json`에서 원본/사본 해시와 분석 중 입력 불변을 확인했다. `analyze_pohang_saves.py`는 정확한 최상위 `states/1030`, `states/1029`, `countries/KOR`만 판정한다. 누락된 직렬화 자원 필드를 0으로 추정하거나 보정된 생산량을 기본 자원 증가분으로 사용하지 않는다.

| 원본 → 외부 사본 | 확인 |
|---|---|
| `KOR_1936_01_03_04_temp.hoi4` → `saves/before-focus.hoi4` | 1936.1.3.4, 중점 완료 목록 없음, PP502.402, 대상 활성 사업 없음. 두 주의 런타임 자원 필드 미직렬화 |
| `KOR_1936_01_05_19_temp.hoi4` → `saves/first-active.hoi4` | 포항제철 완료, 경상 런타임 `resources/steel=25`, PP479.804, 포항 활성 사업 `days=88`. 공사 시작 직후의 90일 UI와 구분 |
| `KOR_1936_04_10_20_temp.hoi4` → `saves/after-cycle1.hoi4` | 경상 `resources/steel=34`, 포항제철 완료 유지, 대상 활성 사업 없음. 직전 25에서 **+9** |
| `KOR_1936_07_18_07_temp.hoi4` → `saves/after-cycle2.hoi4` | 경상 `resources/steel=43`, 포항제철 완료 유지, 대상 활성 사업 없음. 직전 34에서 다시 **+9** |

첫 종료는 1936.4.3.24에 관측됐다. 관측 tick은 시작3→종료93이며, 같은 총 민공40인 상태끼리 가용16→25로 **9개 반환**을 확인했다. 실제 재사용 항목과 raw 저장의 +9를 결합해 정상 완료 1회로 판정했다. 종료 전환 자체는 완료·취소를 구분하지 않으므로 단독 증거로 삼지 않는다.

1936.4.10.20에 실제 재사용 버튼을 눌렀을 때 UI 정치력은 **593→568**, 공사는 다시 **90일**로 시작했다(`ui/second-expansion-started-0.jpg`). 두 번째 종료는 1936.7.9.24, 관측 tick100→190으로 **90일**이었다. 같은 총 민공40에서 가용16→25로 **9개 반환**, 실제 재사용 항목(`ui/second-completed-reusable-0.jpg`), 저장의 **34→43**을 함께 확인했다. 두 회 모두 생산 디시전을 실제 UI에서 시작하고 정상 달력 진행으로 완료했으며, 강제 기간 종료·자원 지급은 사용하지 않았다. 관측기의 보정된 최종 생산량 대신 저장의 기본 자원 필드를 증가량 근거로 사용했다.

강원 사업은 두 회 동안 실행하지 않았다. 소스의 강원 블록은 변경 전과 바이트 일치했고, 관측기의 강원 활성값은 0, 보정된 석탄 생산량은 5.52로 유지됐다. 이를 강원 사업의 새 반복·취소 실행 검증으로 확대하지 않는다.

### 완전 재시작과 로그

첫 시험을 정상 종료한 뒤 `profile.py clean`으로 원래 두 모드 선택을 복구했다. 최종 게임 PID는 **24260**, 인자는 `-start_tag=KOR -start_speed=0 -force_text_save`였다. `-debug`와 외부 fixture가 없는 완전 재시작에서 **Operation Postern v1.19.4.2.2da5 (0f96)**, DLC36·활성 모드2개를 확인했다. 1936.1.1.12에 최종 설명문의 강조된 포항제철 이름·비용·기간·보상·반복·취소 문구가 정상 표시됐고, 목록에 보이는 포항 사업이 중점 미완료 조건으로 차단됐다(`ui/clean-final-description-and-gate-0.jpg`). 이 최종 새 게임에서는 건설 II·가용 민공도 미충족이었다. 중점 조건만 분리한 검증과 두 회 반복은 앞선 준비 시험의 결과다.

게임 종료 후 안정 로그를 각각 `runs/probe-01/logs/`, `runs/clean-02/logs/`에 수집하고 독립적으로 검토했다(`runtime-log-review-probe.json`, `runtime-log-review-clean.json`). 첫 시험의 `error.log` 17행은 등록 descriptor 6행, debug 현지화 충돌 요약 1행, 저장 및 random 로그 rename 10행이었다. 최종 일반 실행의 8행은 같은 descriptor 6행과 종료 시 random 로그 rename 2행이었다. **포항 조건·해금 안내·대상 현지화·fixture 문법을 지목하는 오류는 없었고**, 최종 오류의 정규화 메시지는 모두 이 작업의 기준 로그에 있던 종류였다. `setup.log`는 디시전 파일의 정의 2개 등록을 기록했고 최종 로그에는 fixture 흔적이 없었다. graphics의 작은 강 문제와 game의 Conflict Risk 메시지도 별도로 기록했으며, 조용한 대상 로그만으로 전체 모드가 오류 없다고 판단하지 않는다.

이 환경의 게임 저장은 `_temp.hoi4` 원본에서 최종 이름으로 바꾸는 단계에서 rename 오류가 발생했다. 실제 생성된 텍스트 `_temp` 4개를 읽고 해시를 확인했으며 이 저장 경로 문제를 이번 조건 변경의 결함으로 귀속하거나 수리하지 않았다. `runs/clean-02/summary.json`의 새 저장 4개 목록은 최초 저장 목록 대비 다시 수집한 **첫 시험의 동일한 4개**이며, 최종 실행에서 추가 저장을 만든 결과가 아니다.

### 환경 복구와 검증 한계

두 시험 게임을 정상 종료했다. `profile.py restore`는 `settings.txt`, `dlc_load.json`, `pdx_settings.txt`, `gameplaysettings.txt`를 이번 백업과 SHA-256이 같도록 복구하고, 자기 고유 표식이 있는 임시 descriptor만 제거했다(`profile-restore.json`). 기존 사용자 저장 **34개는 모두 같은 해시**였고 시험에서 생성한 새 저장 4개는 실제 사용자 데이터에 남긴 채 증거 사본도 보존했다.

debug 게임13584가 만든 메모장18236→21148은 경로 오류 알림을 표시했다. 알림을 닫자 메모장이 복원한 기존 사용자 탭이 나타났으므로 내용을 변경하거나 폐기하지 않고 창을 정상 종료했다. 시험 게임·launcher·해당 메모장이 남지 않은 것을 확인했고, Steam도 **녹색 플레이**로 돌아왔다(`ui/steam-restored-play-0.jpg`). 설정 복구·저장 보존·최종 소스 해시·잔존 프로세스 확인은 `final-verification.json`에 기록한다. 저장소의 기존 시험 산출물 정리 대상은 이번 조사에서 발견되지 않았으며 시험 helper·백업·로그·분석·화면은 외부 작업 루트에 보관했다.

이번에 확인한 범위는 독립 소스 검토26개, 준비된 조건에서의 미완료 차단·완료 후 허용·중점 보상 안내, 두 차례 정상 90일 완료·회당 정치력25·민공9 점유와 반환·기본 강철+9, 최종 원래 모드 구성의 완전 재시작 UI와 로그다. **정상 연구·건설·중점 경로 진행, 변경 전 저장이나 진행 중 사업의 호환성, 정확한 민공8/9 경계, 취소 경로 재실행, 다른 DLC·언어 UI·해상도, 장기 AI·멀티플레이는 이번에 검증하지 않았다.** 영문 헤더 파일의 한국어 본문은 소스 검토했고 실제 UI는 `l_korean`에서 확인했다. 이전 여섯 회 실행·취소·재로드는 중점 연계 전의 별도 증거로 유지한다. 커밋·푸시·게시·업로드는 수행하지 않았다.
