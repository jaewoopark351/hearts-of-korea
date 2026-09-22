# 2026-09-22 기존 한국 중점 326개 검증 기록

이 문서는 신규 공산 정책 10개를 추가하기 **전** 326개 기준의 정적 검사와 일반판 초기 진단 실행을 기록한다. 이후 336개 구현과 정책 4개 시나리오 결과를 포함하지 않는다. 판정은 **정적 참조 확인 + 초기 실행 105 PASS / 2 FAIL, 장기·정상 플레이 검증 미완료**다. 최초 326개 전체를 정상 진행으로 완료했다는 뜻이 아니다.

## 기준 소스와 실행 환경

- branch: `feat/korean-focus-expansion-ai`; 검사 시작 HEAD: `f43769cd9957d4f331b4d591506d52f5da485f79`.
- 기준 `common/national_focus/korea.txt` SHA256: `830C58121C359CD48D9343F312EB8B05C5CCEEE37E308E86F0CC74EED98EC579`. 보존본은 `.local-artifacts/korean-focus-expansion/second-wave-20260922/baseline/source/common/national_focus/korea.txt`이다. 정적 검사 당시 생산 파일과 같았고, 실행 기록 `baseline-general-1/diagnostic-hashes.json`도 같은 해시를 기록했다.
- Windows 11, HOI4 `Operation Postern v1.19.3.0.c01a (053d)`, build time `Sep 9 2026 09:10:08`, 설치 Steam build `25205862`. 게임 버전·실행 체크섬 근거는 `baseline-general-1/system.log:289`, OS는 같은 로그 1행이다. 체크섬은 임시 진단 파일이 포함된 이 실행의 값이다.
- 활성 DLC 36개와 일반판 Hearts of Korea 1개: 같은 로그 290–328행. 필수로 선언된 `Korean Language`는 **이 실행에서 비활성**이었다. 따라서 정상 필수 의존성 조합을 완전히 검증한 실행으로 취급하지 않는다. DLC별 비활성 조합도 검사하지 않았다.
- 실제 로드 설정은 `mod/hearts of korea.mod` 1개였다. 앞서 Road to 56 조합이 관측됐지만 이 실행 전에 일반판 1개로 바뀐 상태가 관측됐다. 변경 주체와 런처 플레이세트 표시 이름은 확인하지 않았다. 검증 작업에서 사용자 설정을 전환하지 않았으며 `baseline-general-1/dlc_load-before.json`과 `dlc_load-after.json`의 SHA256은 모두 `BC81B8FFCD932E9F21B4C44EBA79A484A2019FAC4D1EB6698CF414143EFA182D`이다.
- 새 1936 KOR 게임, 창 모드 1600×900으로 실행했다(`system.log:44–47`). GUI scale과 실제 한국어 화면 표시는 별도 확인하지 않았다. `noai` 인자를 사용했지만 fixture 안내 로그만으로 AI 비활성화를 독립 입증하지 않는다.

이하 `baseline-general-1/…`은 저장소의 `.local-artifacts/korean-focus-expansion/second-wave-20260922/baseline-general-1/…`을 뜻한다. 로그·원본 진단 파일·설정 사본은 ignored 진단 자료이며 배포 파일이 아니다. 최초 실행에 임시 복사한 `common/on_actions/HOK_secondwave_test.txt`, `events/HOK_secondwave_test.txt`는 실행 담당자가 원본 해시 대조 후 제거했다. 사용자 설정, 기존 작업, 원작 Workshop 복사본을 변경하지 않았고 commit/push/upload를 수행하지 않았다.

## 정적 검사

| 항목 | 기존 326개 기준 결과 | 범위와 제한 |
|---|---|---|
| 중점 ID | 326개, 고유 326개 | 저장소 및 설치 vanilla focus 파일에서 해당 ID 중복 없음 |
| prerequisite / mutex / relative anchor | 대상 ID 누락 0개 | 그룹 구조를 보존해 목록화. 존재 검사는 아래 선언 순서 오류까지 해결하지 않음 |
| 직접 idea 참조 | 97개 모두 정의 또는 조언자 토큰 확인 | add/remove/timed/swap/show 참조. 재귀 scripted effect 전체 검사는 아님 |
| Sprite 참조 | 고유 387개 모두 프로젝트 또는 설치 vanilla 정의 존재 | 326 focus icon과 신규 60 shine·29 spirit을 포함. 프로젝트 내 검사 대상 Sprite 중복 없음 |
| 이미지 경로 | 검사한 프로젝트 Sprite의 로컬 누락 경로는 당시 shine overlay 1개 | vanilla에는 존재. 159개 legacy Sprite는 vanilla 정의만 존재하므로 326개 전체가 자체 이미지 규칙을 충족한다는 의미는 아님 |
| 이름·설명 번역 | 언어별 요구 키 710개 존재, 해당 키 중복 없음 | 326 focus + 29 spirit의 이름·설명; 저장소 English/Korean 검사 |
| 확장 번역 파일 | 4쌍 8개 모두 BOM/header 정상, 쌍별 키 일치 | 민주 83·산업 74·군사 74·navigation 8 = 언어별 239개 |

초벌 idea 검사에서 보류된 9개는 직접 확인으로 해소했다. 조언자 6개는 `common/characters/KOR.txt`의 `idea_token`(558, 579, 604, 624, 647, 1411행), 소련 idea 3개는 설치 vanilla `common/ideas/SOV.txt`의 1529, 2760, 2860행이다. 자체 scanner가 vanilla `powerbalanceview.gfx`, `persia.txt`, `SOV.txt`, `switzerland.txt` 전체 구조를 처리하지 못한 제한을 기록하고 필요한 참조만 수동 보완했다. vanilla 전체의 문법·중복 인증을 주장하지 않는다.

당시 누락 경로는 `gfx/interface/goals/shine_overlay.dds`이며 기준 `interface/HOK_KOR_focus_icons_shine.gfx:10,22` 등에 쓰였다. 설치 vanilla 파일이 있어 외부 fallback이 가능하다는 사실과 프로젝트 자체 이미지 통합 완료 여부는 별개다. 이후 로컬 overlay 통합은 이 baseline의 소급 성공으로 기록하지 않는다.

재현 자료는 ignored 경로 `second-wave-20260922/audit-current326.ps1`, `current326-static-audit.json`, `current326-static-audit-followup.json`이다. 각 focus의 ID·선행 그룹·상호배타·앵커·아이콘·idea 참조, Sprite 정의/이미지 경로, 번역 키 확인을 보존했다. 엔진 파일 로드 우선순위, DLC archive 전체, 의존 모드 전체, 모든 간접 참조와 실제 UI 표시를 대체하는 검사는 아니다.

## 초기 진단 실행: 105 PASS / 2 FAIL

원본 `baseline-general-1/game.log`의 `HOK_SW_BASELINE` 기록을 집계했다. 1936-01-01 13시 시작, 마지막 검사는 01-05 10시다. 58개 신규 중점을 **스크립트로 강제 완료**했고, 필요한 기존 중점 일부도 unlock/complete했다. prerequisite·소요 시간·가용성·정상 선택 경로를 모두 거친 실행이 아니다.

| 관측 항목 | PASS 수 | 증명하는 것 |
|---|---:|---|
| 신규 중점 완료 상태 | 58 | 해당 scripted completion 뒤 완료 상태 |
| 국민정신 단계·교체 | 15 | 해당 시점의 추가 및 이전 단계 제거 |
| modifier 합계 변화 | 20 | 기준값 대비 검사한 modifier 변화 |
| 시민교육 공장 | 3 | 주 525/1082/1031 각각 민간공장 +2 |
| 지역 사업 초기 활성 | 4 | 각 scripted activation 직후 결정 상태 |
| 평안 사업 취소·미지급·재시작 | 3 | 소유권 상실 후 취소, 공장 +0, 소유 복구 뒤 재시작 |
| 정부·세력 준비 / 미선택 대안 부재 | 2 | fixture 준비와 선택하지 않은 2개 중점의 부재 |
| **합계** | **105** | 전체 테스트 계획 통과가 아님 |

공장 관측은 `game.log:134–139`, 지역 사업은 140–143행, 취소·재시작은 147–150행이다. 미선택 대안 부재는 UI의 상호배타 표시나 실제 선택 차단을 검사한 것이 아니다. 관세 국민정신을 상대국에 직접 부여했으므로 외교 수락/거절도 검증하지 않았다. `activate_decision`/`activate_targeted_decision`은 정상 가용성·비용 검증을 대신하지 않는다.

### FAIL 1: 의용군 긴장도 기대값

`game.log:132–133`은 `modifier_send_volunteers_tension` FAIL과 실측 `-1`을 기록했다. **CONFIRMED: fixture 계산 오류.** fixture가 기존 `KOR_stop_moderate_diplomacy`와 `KOR_korean_volunteer_corps`를 모두 완료하며 `common/ideas/korea.txt:523,715`가 각각 -0.5를 준다. 합계 -1이 생산 소스와 일치한다. fixture의 -0.5 기대가 잘못됐으며 생산 보상을 변경할 근거가 아니다.

### FAIL 2: 동맹 사업 활성 조회

`game.log:145`의 `allied_initial_active` FAIL은 `activate_targeted_decision` 직후 bare `has_decision` 조회가 거짓이었다는 사실이다. **UNPROVEN: 활성화 실패인지, 조회/갱신 문제인지 아직 분리되지 않았다.** 별도 targeted 조회 문법을 임의로 만들지 않았다. 설치 vanilla에도 targeted 결정에 bare `has_decision`이 사용되므로 이 문법 자체가 틀렸다고 단정하지 않는다.

설치 `documentation/effects_documentation.html:693–700`은 targeted activation이 일반 trigger/cooldown 조건을 무시한다고 명시한다. `triggers_documentation.html:3159–3165`는 active selected decision이라는 일반 설명만 제공한다. 정상 UI 사용 및 비용과 180일 유지·완료는 별도 확인해야 한다.

두 FAIL 원본을 그대로 보존한다. 이후 ignored fixture의 긴장도 기대값을 -1로 고치고, targeted query를 관찰값으로 분리했다. 동맹 사업 시작 counter +1과 상대국 committed flag를 추가 검사해 생산 `complete_effect` 실행 여부를 구분하도록 했다. **수정 fixture의 엔진 재실행 전이며 기존 로그를 107 PASS로 바꾸지 않는다.** 수정본은 `runtime-fixture/fixture-revision-validation.json`에 해시·정적 괄호 검사만 기록했다.

## 기존 생산 로그에서 확인된 별도 오류

`baseline-general-1/error.log:15–18`은 두 중점의 상대 앵커 선행 선언 오류를 기록했다.

- 기준 korea.txt:264 `KOR_support_gaema_plateau` → 나중에 선언된 `KOR_hamgyeong_underground_resources`.
- 기준 korea.txt:437 `KOR_build_soyanggang_dam` → 나중에 선언된 `KOR_gangwon_underground_resources`.

**CONFIRMED:** 대상 ID 존재 여부만으로는 충분하지 않다. 이 설치 엔진은 해당 두 사례에 선행 선언을 요구했다. 후속 수리·신규 중점 검증에서 선언 순서도 확인해야 한다. 같은 로그에 기존 캐릭터 및 구 교리 database object 오류도 있으며 이번 문서는 전체 기존 오류 수리를 선언하지 않는다.

## 남은 검사

- 지역 90일 사업의 정상 완료·반복, 동맹 180일 사업의 완료·반복, 366일 영구 효과 유지.
- 대체 생산·외국 공군 경로, 정상 UI 가용성·정치력/장비 비용·취소 조건, 자발적 외교 수락/거절과 DLC별 조건.
- 일반/역사 AI의 실제 선택·막힘·장기 진행, save/load, 1939 시작, 멀티플레이.
- SHOW 및 이념 선택 후 HIDE 전환, 숨은 앵커·연결선·패널·아이콘 시각 상태와 한국어 표시.
- 필수 `Korean Language`를 포함한 기록된 정상 의존성 조합에서 재검증.

보병 장비만의 생산 보상처럼 아직 확정되지 않은 설계 항목과 후속 공산 10개 구현 결과는 별도 계획/사건 기록을 따른다.
