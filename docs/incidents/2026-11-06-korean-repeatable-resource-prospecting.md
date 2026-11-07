# 한국 반복 자원 탐사 구현·검증 기록

작성 시작일은 2026-11-06이며 실행 검증은 2026-11-07에도 이어졌다. 이 작업은 사용자가 명세 설명 후 **“AGENTS.md, /docs 읽고 구현해줘”**로 승인한 신규 콘텐츠 구현이다. 원본 복구·기존 자원 재배치와 별개다. 확정 요구와 실제 파일은 [명세](../HOK_KOREAN_REPEATABLE_RESOURCE_PROSPECTING_SPEC.md)를 참고한다.

**2026-11-07 후속 작업 안내:** 「포항제철」 중점 완료 조건과 새 설명문을 검토·수정하거나 검증할 때는 [명세 10절의 문서화 당시 요구](../HOK_KOREAN_REPEATABLE_RESOURCE_PROSPECTING_SPEC.md#10-2026-11-07-포항제철-중점-연계와-설명문--문서화만)와 [후속 구현·검증 기록](2026-11-07-pohang-focus-gate.md)을 먼저 읽는다. 후속 작업은 처음에 문서화만 허용됐고, 이후 별도 구현 요청에 따라 소스·현지화에 적용했다. 아래의 실행 결과는 **중점 연계 전 구현**에 대한 기록으로 보존하며, 새 중점 조건이나 새 설명문을 검증한 결과로 취급하지 않는다.

## 소스와 실행 환경

- 작업 소스: `C:\hoi\hearts_of_korea`, 브랜치 `feat/korean-focus-expansion-ai`, 시작 HEAD `f927b3a5defe046967413da05069a0f92823fbec`.
- 시작 작업 트리의 README·과거 석탄/크롬 메모 수정과 새 명세는 앞선 문서화 작업 결과였다. 이를 보존하며 구현 상태를 갱신한다. 커밋·push·업로드는 수행하지 않는다.
- 설치 원본: `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`. 관측 버전 `Operation Postern v1.19.4.2.2da5`, Steam build `26409260`. 추가 전 로그 checksum `8aa0`와 진단 overlay 실행 checksum은 구분한다.
- 원작 Workshop `2898629778`의 다운로드는 읽기 전용 역사 자료다. 현행 descriptor의 후속 항목 `3793992662`는 이 작업에서 변경하거나 업로드하지 않는다.
- 실제 사용자 데이터: `C:\Users\jaewo\OneDrive\문서\Paradox Interactive\Hearts of Iron IV`.
- 실제 활성 순서: `mod/hearts of korea.mod` → `mod/Hearts of Korea English Translation Anime Modder's Edition.mod`. 첫 경로는 저장소, 두 번째는 `C:\hoi\Hearts of Korea English Translation Anime Modder's Edition`을 가리킨다. 선언된 Korean Language 의존성과 실제 활성 목록의 차이는 유지했다. 관측 환경은 `l_korean`, DLC 36개다.

기존 게임 PID 9488 종료에 관해 사용자가 허용한 뒤 직접 종료했다고 알렸다. 프로세스 부재와 Steam의 플레이 버튼을 관측한 후 검증용 게임을 별도로 실행했다.

## 적용 범위

새 전용 파일에서 기존 `prospect_for_resources`에 두 정의만 누적한다. 설치 원본의 AST·SOV 등에서도 같은 범주를 여러 파일에 나누는 사례를 확인했으며, 실제 UI에서 기존 장진 텅스텐 탐사와 새 두 디시전이 함께 나타났다.

| 디시전 ID | 대상 | 매회 조건·비용 | 기간·보상 |
|---|---|---|---|
| `HOK_KOR_expand_gangwon_coal_mines` | 강원 1029 | 건설 II / PP25 / 민공9 | 90일 / coal +9 |
| `HOK_KOR_expand_pohang_steelworks` | 경상 1030 | 건설 II / PP25 / 민공9 | 90일 / steel +9 |

국가 조건은 `original_tag = KOR`다. 해당 주 소유 시 표시되며, 비항복·소유·완전 통제와 가용 사업 민공 9개 이상을 착수 때 검사한다. 별도 중점 해금은 추가하지 않았다. 각 사업은 하나씩 진행하고 두 사업 병행은 허용한다. 병행 민공 점유는 합계 18개다. 기간·비용·보상 증가나 횟수 상한 변수는 없다.

항복·소유권 상실·완전 통제 상실 시 취소하고 PP를 환불하지 않는다. 취소에는 자원 보상이 없으며, 정상 제거 보상에서도 같은 영토 조건을 재확인한다. AI는 기본 0.5, PP80 미만이면 0, 해당 자원 1 미만이면 5배를 사용한다. 이는 사용자가 지정한 수치 이외의 일상적 통합 선택이며 장기 AI 품질을 보증하지 않는다.

기존 시작 자원, 포항 중점의 steel +25, 강원 지하자원 중점, 기존 지역개발은 수정하지 않았다. 새 한국어/영문헤더 현지화는 프로젝트 관례에 따라 동일 한국어 본문이며 UTF-8 BOM·CRLF와 동일 기여 주석을 갖는다.

새 sprite 두 개는 프로젝트 내부 DDS를 참조한다. 설치 원본의 소형 석탄·강철 그림을 바이트 그대로 복사했으며 원본 크기를 보존했다. 출처·해시·행 경계 계산은 [자산 기록](../HOK_KOREAN_RESOURCE_PROSPECTING_ASSET_CREDITS.md)과 [매니페스트](../data/HOK_KOREAN_RESOURCE_PROSPECTING_ASSET_MANIFEST.json)에 있다. 새 AI 그림이나 전체 GUI 변경은 없다.

## 증거 위치와 검증 구분

모든 helper·백업·로그 사본·검토 그림·진단 overlay·저장 사본의 작업 루트는 **`C:\hoi\test\hok-resource-prospecting-20261106-01\`**다. 게임 생성 저장 원본은 실제 사용자 데이터의 `save games`에 남겨 두며, 기존 사용자 저장을 덮어쓰거나 옮기지 않는다. 저장소에는 이 유지 기록과 런타임 파일만 둔다.

- `baseline.json`, `source-before/`, `source-before-manifest.json`: 시작 소스·파일 해시·경로.
- `user-config-before-launch/`: 기존 게임 종료 후 실제 설정 4개 원본. 처음 실행 중 얻은 `user-config-before/`와 구분하며, 최종 복구는 전자를 사용한다.
- `user-save-inventory-before-launch.json`: 기존 저장 30개의 길이·SHA-256.
- `source-validation.json`: 제한된 정적 검사 47개 통과·0개 실패. 이는 파서·엔진 수명주기 검증을 대신하지 않는다.
- `independent-source-review.json`: 실제 소스 6파일 해시와 원본 근거를 포함한 독립 읽기 검토. 중대한 수정 필요 사항은 발견하지 못했으며 runtime 판정과 구분했다.
- `assets/`: 바이트 일치 결과와 소형 아이콘·행 배치 검토용 PNG. 설명용 행 배치 그림을 게임 화면으로 취급하지 않는다.
- `runtime-probe/`, `prepare_resource_probe.py`, `resource_probe_control.py`, `RESOURCE_PROBE_PROCEDURE.md`: 외부 전용 진단 준비·관측·수집. production 디시전·보상·90일 기간은 복제하거나 단축하지 않는다.
- `analyze_resource_saves.py`, `schema-notes.json`: 읽기 전용 저장 구조 검사. `states/1029`, `states/1030`, `countries/KOR`의 정확한 경로만 판정한다.

진단 준비는 건설 II·PP500·offsite 민공30을 시험 저장에 부여한다. 따라서 기술과 산업을 정상 연구·건설한 캠페인 검증으로 주장하지 않는다. 관측용 `resource@coal`/`resource@steel`은 보정 후 생산량이므로 raw 증가량과 혼동하지 않는다. 저장의 `states/.../resources`도 시작 자원과 런타임 추가분을 분리해 읽는다. 이전 Wallonie 저장과 원본 중점 보상의 대조 근거를 `schema-notes.json`에 남겼다.

## 실행 이력

1. `ui-main-01`: 외부 Lua fixture의 잘못된 `#` 주석으로 로드 오류. 증거는 해당 run의 `preliminary-load-error-logs`다. fixture를 `--`로 고친 뒤 프로세스를 완전히 재시작했다. 이 시도는 통과가 아니다.
2. `ui-main-02`: PID 14996, `-debug -start_tag=KOR -start_speed=0 -ai_testing -force_text_save`. 실제 UI에서 두 버튼·전용 아이콘·툴팁을 확인하고 각각 클릭했다. PP101→76→51, 두 사업 모두 90일 표시. AI testing이 기존 한국 AI 소비도 실행하므로 PP500→최초 클릭 직전 감소를 새 디시전 비용으로 오인하지 않는다.
3. `ui-main-02`에서 엔진 저장 원본 `KOR_1936_01_04_06_temp.hoi4`를 생성했다. 기존 동일 파일 부재를 확인한 뒤 저장했다. 원본은 사용자 데이터에 있고 외부 사본은 `runs/ui-main-02/active-before-reload.hoi4`다. 분석 JSON에서 날짜 `1936.1.4.6`, PP51.203, 두 `decision_to_remove` 항목의 `days=90`을 확인했다.
4. `ui-main-03`: PID 20652, `-ai_testing` 없이 새 프로세스에서 위 엔진 저장을 UI로 실제 불러왔다. 날짜·PP51·두 사업의 90일 표시가 유지됐다. 재초기화로 PP500을 지급하지 않았다. 관측 snapshot의 가용 사업 민공은 5개였다(두 사업 점유 합계18).

Windows 입력 자동화에서 게임 키보드 입력의 효과를 확인할 수 없어 외부 전용 `ZZ HOK TEST CONTROLS` 조작판을 추가했다. 이는 시험 준비·상태 기록·통제 이전에만 사용하고 production 사업 선택은 실제 목록에서 클릭한다. 초기 observer의 decision-timeout dynamic token 경고 두 종류는 외부 관측 표현식에서 발생했으며, ui-main-03에서는 그 표현식을 제거했다. 이를 production 결함 수리로 기록하지 않는다.

엔진의 `continue_game.temp`와 수동 저장 `_temp.hoi4` rename 오류도 발생했다. 실제 생성된 `_temp.hoi4`를 대조하고 UI 불러오기에 사용했으며, 정상 최종 파일명이 생성됐다고 주장하지 않는다. 이 사용자 데이터 환경의 기존 저장 동작 문제는 자원 디시전 변경 범위에 포함하지 않는다.

`diagnostic-log-review-ui-main-03.json`은 게임일1936.09.03.24까지 읽은 독립 관측이다. 신규 디시전 두 개의 setup 등록을 확인했고 신규 디시전·GFX·DDS를 지목하는 오류는 발견하지 못했다. 기존 함장 현지화13키·26항목과 바닐라 한국어 키의 충돌, 등록 모드 descriptor 오류, rename 오류, 출처를 확정할 수 없는 AI `merge_navies` 경고5건은 따로 남겼다. 기준 `text.log`가 비어 있으므로 그 충돌이 기준 실행에도 동일하게 기록됐다고 주장하지 않는다. 이는 전체 무오류 판정이나 최종 overlay 없는 실행의 결과가 아니다.

## 최종 결과

소스 적용과 아래의 실제 UI·반복·저장·취소 검증을 수행했다. 정확히 민공 8/9개인 경계, 통제권만 잃은 경우와 항복 취소, 장기 AI·다른 DLC·기존 저장·멀티플레이 검증은 포함하지 않는다. 정적 통과나 오류 키워드 부재를 이 미검증 항목의 통과로 확대하지 않는다.

### 정상 기간 진행 중 확인

첫 완료의 수동 저장은 `KOR_1936_04_07_19_temp.hoi4`이며, 외부 사본 `runs/ui-main-03/after-cycle1.hoi4`와 `cycle1-analysis.json`에서 강원 `resources/coal=9`, 경상 `resources/steel=9`를 확인했다. 이는 각각 시작값에 더해진 직렬화 추가분이다. 두 사업 활성 때 사업 가용 민공5 → 첫 완료 후23으로 합계18개가 반환됐다. 첫 완료 뒤 실제 UI에서 두 사업을 다시 눌러 PP213→188→163과 각각90일을 확인했다. 두 번째 완료 후에도 재사용 버튼이 표시됐고 세 번째는 PP311→286→261, 각각90일로 착수했다.

`days_remove=90`, 초기 UI·저장 타이머90, 달력에 따라 감소한 타이머를 각각 확인했다. 일일 observer가 시작/종료를 처음 발견하는 시각에는 최대 한 번의 일일 평가 차이가 있으므로 그 `elapsed_daily_ticks`를 정확한 시간 단위 공사 기간으로 환산하지 않는다. 첫 재로드 사업의 observer 결과91을 근거로 production을89일로 바꾸지 않는다. 원본 엔진의 90일 설정을 유지한다.

### 여섯 회 정상 완료와 경계 시험

`ui-main-03`에서는 실제 자원 탐사 버튼을 매회 눌러 두 사업을 각각 여섯 번 완료했다. 2~6회 착수 때 UI 정치력은 각각 213→188→163, 311→286→261, 406→381→356, 503→478→453, 602→577→552였고 두 타이머는 매회 90일로 시작했다. 여섯 번째 완료 후 1937.7.26.18의 `KOR_1937_07_26_18_temp.hoi4`를 생성했다. 외부 사본 `runs/ui-main-03/after-cycle6.hoi4`, `cycle6-analysis.json`에서 강원 coal 추가분 54·경상 steel 추가분 54와 분석 schema 실패 0을 확인했다. 이는 최종 채굴량이나 시작값 포함 총량 54라는 뜻이 아니다. 실제 UI에 두 재사용 버튼이 다시 나타났고, 뒤의 비용 경계 시험에서는 강원 7회차도 착수했다. 무한한 회수를 실행한 것은 아니며 상한 없는 소스와 5회 이후 실제 반복을 함께 확인한 것이다.

종료 후 안정된 로그는 `runs/ui-main-03/evidence-20261106T155954351476Z/`, 읽기 전용 요약은 `six-cycle-summary.json`에 있다. 요약의 ENDED는 원래 완료와 취소를 구분하지 않으므로 화면·저장과 결합해서 판정한다. 첫 여섯 종료 관측일은 1936.4.4, 7.6, 10.10, 1937.1.11, 4.16, 7.20(각 24시)이었다. observer 경과값 91/90/90/90/90/89는 일일 관측 해상도와 명시 snapshot 시점 차이이며 엔진 설정 90일을 바꾸는 근거가 아니다.

정치력 24에서는 두 버튼이 차단됐고, 25에서는 허용됐다. 일시정지 상태에서 실제 강원 버튼을 눌러 25→0과 90일을 확인했다(`pp24-blocked.jpg`, `pp25-available.jpg`, `pp25-paid-coal-active.jpg`). `pp25-to-zero-coal-started.jpg`는 클릭 직후 목록 배치가 바뀌어 원본 장진 툴팁을 캡처한 중간 화면이므로 차감 증거로 쓰지 않는다.

기술 제거용 외부 `set_technology construction2=0` 조작 뒤에도 UI는 건설 II 충족으로 표시됐다. `construction2-removed-blocked.jpg`라는 중간 파일명은 실제 차단을 입증하지 않으며 이 시도는 미판정이다. `set_state_controller_to=JAP`도 지도의 색·생산량은 바꾸었으나 6일 후 production 취소 툴팁은 여전히 거짓이고 공사는 84일로 진행 중이었다. 이 준비만으로 소유권·완전통제 상실을 재현했다고 판정하지 않는다. 아래의 별도 초기 상태·영토 이전 준비로 재확인했다. production 코드는 이 준비 실패 때문에 변경하지 않았다.

### 실제 영토 상실·취소와 완료 후 재로드

`boundary-main-04`(PID 12144)는 완전 재시작 후 여섯 회 완료 저장을 UI에서 불러왔다. 외부 fixture의 영토 조작만 설치 원본의 COUNTRY `transfer_state`로 바꾸었고, production과 동일한 취소 OR와 소유·완전통제의 ROOT/literal KOR 판정을 별도로 기록했다. 이 실행의 fixture 사본·해시는 `runs/boundary-main-04/fixture-snapshot/`, `fixture-manifest.json`에 있다. 원본 근거는 `documentation/effects_documentation.md:8323`과 `events/Japan.txt:576`이다.

1937.8.5.24에 두 실제 사업을 착수해 PP715→690→665, 각각90일을 관측했다. 로그 snapshot은 시작 전715.837과 두 착수 후665.837을 기록하며 중간690.837은 별도 snapshot에 없으므로 독립 로그의 직접 관측값으로 쓰지 않는다. 같은 일시정지 시점에 강원·경상을 일본으로 이전하자 두 주의 소유·완전통제 판정이0, 취소 OR가1로 바뀌었다. 다음 일일 관측1937.8.6.24에 두 사업이 비활성으로 바뀌었다.

첫 비활성 PP667.390은 착수 후665.837에 일일 증가1.553만 더한 값이며 환불25/50의 점프가 없었다. 영토 이전으로 총 민공이42→40으로 변했으므로 단순 전후 차이를 반환량으로 계산하지 않는다. 같은 총 민공40인 관측끼리 사업 가용량7→25, 즉 점유18개 해제를 확인했다. 두 주를 한국에 복원한 뒤 총42·사업 가용26으로 돌아왔다.

취소 후 생성한 원본은 `KOR_1937_08_11_17_temp.hoi4`, 외부 사본은 `runs/boundary-main-04/after-cancellation.hoi4`다. `after-cancellation-analysis.json`과 독립 `boundary-main-04-review.json`에서 강원 coal54·경상 steel54가 유지되고 두 활성 `decision_to_remove` 기록이 없는 것을 확인했다. 기존 여섯 회 보상에 중단된 사업의 보상9가 추가되지 않았다. 이 결과는 소유·완전통제 상실을 함께 만든 시험이며 통제 단독 상실이나 항복 경로의 실제 통과를 뜻하지 않는다.

안정된 로그 사본은 `runs/boundary-main-04/evidence-20261106T162320343364Z/`다. 민공8 준비 helper는 같은 시간에 이전 가용량26을 사용해 offsite30을 모두 제거했고 다음 tick에서 가용량6이 됐다. 정확한 엔진 내부 원인은 미확정이며, 이 준비는 ‘8개 차단/9개 허용’ 검증에 실패했다. 제한은60회 조정 횟수이지 실제60시간 검증이 아니다. 준비 실패를 production의 `> 8` 조건 결함으로 취급하거나 조건을 바꾸지 않았다.

### 외부 fixture 없는 최종 실행

`profile.py clean`으로 원래 두 모드 선택만 복원한 후 `clean-main-05`(PID 19108)를 완전 재시작했다. 기술·PP·offsite 민공 준비와 진단 observer는 로드하지 않았다. 실제 UI의 기존 자원 탐사에서 두 이름·아이콘·원본 장진 탐사가 함께 표시됐고, 1936.1.1.12의 두 툴팁은 건설II와 민공9 조건을 각각 불충족으로 표시했다. 당시 PP1도 부족했으므로 기술 하나만 다른 조건으로 격리한 실험으로 부르지는 않는다. 증거는 `runs/clean-main-05/ui/*unresearched-clean-tooltip.jpg`다.

1936.1.15.5까지 실제 달력을 진행하고 창을 정상 종료했다. 이 일반 실행은 짧은 시작·표시·차단 확인이며, 여섯 회 보상 검증은 앞의 준비된 시험 저장에서 수행했다. 직접 시작한 테스트 저장의 난이도는 저장 메타데이터상 normal이고, 사용자 원설정 백업의 very_easy와 구분한다. 사용자 원설정은 아래 복구 대상으로 보존했다.

최종 일반 로그 사본은 `runs/clean-main-05/evidence-20261106T163318955530Z/`다. `diagnostic-log-review-ui-main-03-final.json`에는 앞선 반복 실행의 오류51행을 descriptor6·현지화요약1·rename7·AI merge_navies33·일반변경1·스페인 인물2·unlock_trait1로 분류했다. 새 자원 파일·ID·아이콘 오류 지목은 없었지만 전체 무오류나 다른 경고의 HOK 무관성을 입증한 결과는 아니다. 일반 실행의 독립 `clean-main-05-review.json`은 체크섬 **5d1b**, DLC36개, 실제 활성 모드2개와 fixture 부재를 확인했다. 일반 실행 오류9행은 기존 descriptor6·함장 현지화 충돌요약1·종료rename2이며 새 자원 콘텐츠를 지목하는 오류는 없었다. 초기 짧은 실행에서 AI 경고가 없다는 사실로 1937년 반복 실행의 AI 경고를 수리했다고 주장하지 않는다.

### 복구·보존과 마감

모든 검증용 HOI4 프로세스를 정상 종료한 뒤 `profile.py restore`로 `user-config-before-launch/`의 `settings.txt`, `dlc_load.json`, `pdx_settings.txt`, `gameplaysettings.txt`를 복원했다. `profile-restore.json`, `final-verification.json`, 마지막 `session-cleanup.json`에서 네 파일의 SHA-256 일치와 원래 두 모드 선택·very_easy 설정 복구, 임시 launcher descriptor 제거를 확인했다. 처음 게임 실행 중 얻은 `user-config-before/`의 settings.txt와 달랐던 점은 유지하고, 종료 후 확정한 before-launch 원본을 복구 기준으로 사용했다.

기존 사용자 저장30개의 길이·SHA-256이 모두 유지됐다. 이번 게임이 생성한 별도 저장 원본4개는 사용자 데이터에 남겨 두었고, 각 증거 사본은 외부 작업 루트의 해당 run 아래 보존했다. 저장소의 `tests`, `.local-artifacts`, `runtime-probe` 경로는 존재하지 않았으며 새 진단 파일을 저장소에 남기지 않았다. 이 작업에서는 기존 파일 정리나 저장 삭제를 수행하지 않았다.

HOI4 프로세스가0인데 Steam 표시가 남아 정상 Stop을 사용했다. 정지 중이 계속되어 다른 게임 실행이 없고 다운로드0·네트워크/디스크0인 것을 확인한 뒤 Steam을 정상 종료·재실행했다. 최종 녹색 **플레이** 버튼 복귀를 관측했다(`runs/clean-main-05/ui/steam-library-play-restored.jpg`). 사전에 있던 별도 Crash Reporter나 다른 앱을 강제 종료하지 않았고 Windows 종료·재시작도 하지 않았다.

`git diff --check`는 통과했고 production6파일은 독립 검토 해시와 일치했다. 작업 브랜치·HEAD는 시작 상태 그대로이며 변경은 커밋하지 않은 작업 트리에 있다. 기존 production·사용자 launcher descriptor의 내용은 변경하지 않았고 진단용 임시 launcher descriptor만 생성 후 제거했다. 커밋·push·Workshop 업로드·게시를 수행하지 않았다.

| 판정 | 범위 |
|---|---|
| CONFIRMED — 소스 | 두 사업에 확정된 수치, 상한·기간 증가 없는 반복 정의, 기존 자원·중점·지역개발 보존, 현지화·이미지 연결 |
| CONFIRMED — 실제 실행 | 두 사업 병행, 회당 PP25·민공9 점유·90일 표시, 각6회 정상 완료와 추가분54, 이후 재사용, 진행 중·완료 후 저장 재로드, PP24/25 경계, 영토 상실 취소·무보상·무환불·민공 반환 |
| CONFIRMED — 최종 일반 실행·복구 | fixture 없는 두 모드 실행과 미연구 조건 표시, 1936.1.15.5까지 진행, 새 콘텐츠 오류 지목 없음, 네 설정 원복·기존 저장30개 보존·게임 종료·Steam 플레이 복귀 |
| UNPROVEN | 민공8/9 정확 경계, 통제권만 상실·항복 취소, 전쟁 중 부분 점령, AI의 장기 사용 품질, 다른 DLC·언어 조합·해상도, 변경 전 사용자 저장 호환성, 멀티플레이 |
