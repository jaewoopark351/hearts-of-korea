# 2026-11-11 한미 방위비 2단계 협상 구현·검증 기록

## 범위와 기준

사용자의 `AGENTS.md, /docs 읽고 구현해줘` 요청으로 기존 조약·주둔 중점에 협상, 국민정신, 결과 사건과 뉴스, AI 생성 이미지를 추가했다. 앞선 문서 전용 단계와 구분한다. 커밋·푸시·게시 작업은 이 요청의 범위에 없다.

- 소스: `C:/hoi/hearts_of_korea`, `feat/korean-focus-expansion-ai`, 기준 커밋 `e2009b635d79c80a67fed0370d5fe36a823b656f`.
- 착수 당시 변경: `README.md` 및 새 [방위비 명세](../HOK_KOREAN_US_DEFENSE_COST_SHARING_SPEC.md). 이전 문서 작업을 보존하고 현재 구현 상태로 갱신했다.
- 설치 게임: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV`, `Operation Postern v1.19.4.2.2da5 (0bdb)`, Steam build `26409260`. 문법과 자치령·소비재 계수의 1차 참조이며 수정하지 않았다.
- 역사 원본: `C:/Program Files (x86)/Steam/steamapps/workshop/content/394360/2898629778`, 읽기 전용. 업로드 대상으로 사용하지 않았다.
- 실제 사용자 데이터: `C:/Users/jaewo/OneDrive/문서/Paradox Interactive/Hearts of Iron IV`.
- 활성 모드 순서: 본체 저장소 → `C:/hoi/Hearts of Korea English Translation Anime Modder's Edition`. 번역 기준 `main`, `11ec9e2096af906a086f5c076949f2da1a1c790d`이며 신규 영어 현지화 파일만 추가한다.
- 검증·진단·중간 파일: `C:/hoi/test/us-defense-sharing-20261111-01/`. 원본 소스·로그·설정·기존 저장 목록은 `baseline/`, 정적 검사는 `validation/`, 이미지 변환 증거는 `art/`, 게임 검증은 `runtime/`에 둔다. 영어 번역 검증 사본은 `C:/hoi/test/hok-english-translation-anime/us-defense-sharing-20261111-01/`에 있다.

## 확정한 행동

조약 수락 시 한국 +5%, 미국 −5%의 소비재 공장 계수 국민정신을 지급한다. 기존 보장·통행권·한국 통보와 AI 10/0을 유지한다. 주둔 중점은 미국의 응답 전에는 사단을 지급하지 않는다.

| 미국의 주둔 응답 | 한국 / 미국 소비재 공장 계수 | 종속 상태 | 사단 / KATUSA | 통보·뉴스 |
|---|---|---|---|---|
| 협정·배치 | 최종 +35% / −15%, 기존 단계 교체 | 기존 상태 유지 | 기존 한국 소유 3개 사단 / 허용 | 협정 통보 및 방위비 협정 뉴스 |
| 자치령 | 조약 단계 +5% / −5% 유지 | 미국의 `autonomy_dominion` | 동일 3개 사단 / 허용 | 한국에 수락 1개인 확인 사건 및 51번째 주 뉴스 |
| 주둔 거부 | 조약 단계 +5% / −5% 유지 | 기존 상태 유지 | 추가 사단 없음 / 차단 | 한국에 배치 무산 통보 |

한국 +35%는 조약 +5%에서 추가 +30%로 사용자가 확정했다. 이 수치는 공장을 양국 사이에 직접 이전하는 효과가 아닌 각국 `consumer_goods_factor`이다. 자치령은 합병이나 미국의 실제 주로 전환하는 기능이 아니다. 새 주둔 사건의 AI 가중치는 10/0/0이며 자치령·거부는 플레이어 선택으로 남긴다.

국민정신은 시간 제한 없이 유지하되 상대국 소멸 또는 양국 간 전쟁 시 취소한다. 평화 회복만으로 복구하지 않는다. 기존 저장에 조약 비용을 일괄 소급하지 않는다. `station_requested`가 없는 기존 저장에는 KATUSA의 기존 진입 조건을 유지하고, 새 요청부터 미응답·거부를 차단한다.

### 응답 시 재검증과 배치 무산

한국 scope의 `HOK_KOR_can_finalize_us_defense_stationing`이 양국 존재·한국 독립·양국 내전 없음·한미 전쟁 없음·한국 소유/통제 및 완전 통제 후보 주를 확인한다. 미국이 1·2번을 선택한 실제 처리 시점에 이 공통 trigger를 재평가하며, 요청 후 조건이 사라졌으면 기존 무산 helper로 resolved 처리한다. 이 경우 승인·자치령 표식, 새 경제 효과·사단·뉴스 없이 한국에 `.4` 통보를 예약한다. 중점 완료 시 미국이 아예 없으면 미국 사건을 보내는 대신 같은 무산 helper를 실행한다.

`.4` 제목·본문·선택지와 `refused_tt`는 미국의 정상 거부 또는 양국 상황 변화로 배치가 성립하지 않은 결과에 공용한다. 이 결과 helper가 기존 조약·보유 정신을 직접 변경하지 않는 것과, 전쟁·소멸 시 정신의 취소 조건이 따로 작동하는 것을 구분한다. 본체 두 언어 채널과 활성 en-GB 모두 같은 범위로 수정했고 신규 키 없이 각각 36키를 유지한다.

## 변경 범위와 후보 처리

| 후보·호출 경로 | 처리 | 근거·의미 |
|---|---|---|
| `KOR_rok_us_mutual_defense_treaty` → `kor_events.45` → 기존 46/47 | 변경 / 기존 외교 효과 유지 | 요청·수락 안내와 조약 정신을 추가. 기존 namespace/사건 ID·대소문자·AI·보장·통행권 보존 |
| `KOR_usfk` → `HOK_KOR_us_defense.1` | 변경 | 직접 사단 지급을 요청 상태 기록과 미국 사건으로 전환 |
| `KOR_katusa` | 변경 | 새 요청에서는 `station_approved` 필요. 이전 저장 예외 유지 |
| 신규 6개 사건 및 5개 scripted effect helper | 변경 | KOR 입력 scope, 미국 수신 scope, 3개 분기, 한국 통보, 세계 뉴스, 중복 방지 |
| 공통 scripted trigger 1개·수락 helper의 무효 처리 | 변경 | 응답 시 존재·독립·내전·전쟁·생성 후보 재검증. 무효 요청은 추가 보상 없이 배치 무산으로 종료 |
| 기존 주둔 사단 템플릿·이름·경험치·한국 소유 | 의도적 유지 | 원래 보상을 공통 helper로 옮기고 미국 사건에서 실행할 때 통제 확인 국가를 명시적 KOR로 고정 |
| 사단 지급 표식의 iterator 내 scope | 변경 | 생성 명령 다음에 `KOR = { set_country_flag = HOK_KOR_us_defense_units_granted }`로 기록. state scope 직접 설정 오류를 수정했으며 후보가 없으면 지급 표식도 설정하지 않음 |
| 사단 생성의 `prioritize = { 835 }` | 의도적 유지 | 현행 vanilla 835는 Hararghe. 상속된 우선 후보를 이번 협상 범위에서 바꾸지 않음. 실제 후보는 한국 소유·통제 및 완전 통제 주 중 선택. 지도·지리 수리의 증거로 간주하지 않음 |
| 4개 국민정신 / 8개 sprite·DDS | 변경 | 단계별 고정 수치, 소멸·전쟁 취소. 모든 신규 정신 아이콘에 양국 국기 |
| 본체 `l_korean`·`l_english`와 활성 별도 영어 번역 | 변경 | 본체 두 채널은 한국어 본문 동일, 별도 번역은 영어. 각 36키와 BOM 보존 |
| 선택적 `HOK_KOR_us_defense_waiting_tt` | 의도적 유지 | 예약 안내 키이며 현재 소비자가 없다. 런타임 표시 누락으로 판단하지 않음 |
| 다른 중점·배치·AI·지도·일반 경제 균형·다른 번역 파일 | 제외 | 승인 범위 밖. 기존 474개 중점의 순서·ID·좌표·offset과 허용 3개 밖 본문 보존 |

선택한 AI 원본과 국기 참조, 프롬프트·가공·해시는 [이미지 크레딧](../HOK_KOREAN_US_DEFENSE_ASSET_CREDITS.md)과 [통합 manifest](../data/HOK_KOREAN_US_DEFENSE_ASSET_MANIFEST.json)에 기록했다. 프로젝트 내부 채택 원본은 6개, 게임 런타임 DDS는 8개다. 외부 중간 출력과 채택 원본을 구분한다.

## 검증 단계와 증거

### 정적 검사

독립 검사 `validation/verify_static.py`의 최신 결과는 `validation/static-results.json`: **scope 수정 후 144 PASS / 0 FAIL**이다. 현재 소스는 사건 6개·scripted effect helper 5개·공통 trigger 1개·현지화 36키로 구성한다. 신규 ID의 본체·활성 번역·vanilla 중복, 474개 중점 보존, 3개 분기·4개 수치·AI, 사단 이관·pending 조건·지급 표식의 명시적 한국 scope, 현지화 채널·토큰·BOM, 8개 sprite·DDS 경로·규격·알파를 bounded source/artifact 검사로 대조했다.

| 순서 | 보존 파일 — `validation/` 아래 | 결과와 한계 |
|---|---|---|
| 최초 검사 helper | `static-results.initial.json` | 124 PASS·helper 오탐 1개. 이관된 사단 편제의 x/y를 중점 좌표로 오집계했으며 실제 focus 필드만 대조하도록 helper를 수정 |
| pending 보강 전 | `static-results.before-pending-guard.json` | 130 PASS·0 FAIL. 당시 소스의 정적 이력이며 뒤에 추가한 pending 처리나 엔진 scope 검증의 증거가 아님 |
| pending 보강 뒤, scope 수정 전 | `static-results.before-state-flag-scope-fix.json` | 144 PASS·0 FAIL이었지만 state iterator에서 `set_country_flag`를 직접 실행하는 잘못된 scope를 놓침 |
| scope 수정·검사 보강 뒤 | `static-results.before-font-separator-fix.json` | 2026-11-11 08:48:44 UTC 기록: 144 PASS·0 FAIL. 지급 표식을 명시적 KOR scope로 감싼 소스와 보강한 검사로 재실행 |
| 툴팁 구분 문자 수정 뒤 | `static-results.json` | 신규 현지화 세 파일의 조약 요청 툴팁에서 em dash를 ASCII 콜론으로 교체한 뒤 144 PASS·0 FAIL, source_stable=true. run4의 수정 전 로드 문구에서 물음표가 보인 관측과 수정 후 UI는 구분 |

루트 로그 검토가 17:46:33에 `Invalid scope type for effect set_country_flag`를 보고했고, 최신 정적 JSON의 `verification_history`에도 이 실패와 후속 수정을 남겼다. 앞선 144 PASS는 엔진이 effect scope를 검증했다는 뜻이 아니었다. 후보 state iterator 안에서 국가 표식을 설정하려면 국가 scope로 전환해야 하므로 현재는 `KOR` wrapper를 사용한다. 수정 뒤 같은 수의 정적 검사가 통과한 것과 실제 엔진에서 오류·중복 사단 문제가 해소된 것은 별개 판정이다.

scope 수정 후 전체 재시작한 run3에서 세 주둔 분기의 실제 효과·저장·한국 수신 화면을 아래와 같이 확인했다. 정적 통과와 게임 로드·UI·실제 효과·저장·멀티플레이는 별개 증거다. 정상 중점 진행은 별도 run4로 확인하며 run3의 강제 준비와 혼합하지 않는다.

### 실제 게임 검증

`runtime/fixture/`는 외부 진단 모드이며 생산 모드에 포함하지 않는다. 기존 설정과 로그를 먼저 보존하고, 임시 진단 모드 및 텍스트 저장·자동 저장 해제·사건 시 일시정지를 검증 세션에만 적용했다. 실제 효과, 강제 준비, 일반 진행, 저장·재로드를 구분한다.

run3은 `-start_tag=USA`, 한국어 UI, 본체·영어 번역·외부 진단 모드 순서의 전체 프로세스 재시작이다. 실행 중 게임 체크섬은 `1b0d`이며 설치 메타데이터의 `0bdb`와 다르다. 이 실행에서는 진단 모드가 contact·조약 중점을 강제 준비하고, 조약 수락 후 주둔 중점을 강제 완료했다. 따라서 아래 분기 결과는 실제 미국 선택지 클릭·실제 엔진 효과의 증거이며 35일 중점 정상 진행의 증거가 아니다.

| 검증 | 실제 관측·저장 증거 | 판정 |
|---|---|---|
| 조약 수락 | 기존 `kor_events.45`의 두 선택지와 새 사진 표시, 미국 수락 클릭. `BEFORE.hoi4`에서 KOR tier1=1 / USA tier1=1, 사단 0 | CONFIRMED |
| 협정·배치 | 미국 .1의 세 선택지 중 1번 클릭. 체크포인트 양국 tier2·approved·units_granted. `AGREEMENT.hoi4`에서 각 tier2 1개·tier1 0개, 한국 소유 이름 사단 정확히 3개·미국 소유 0개, 한국 독립 | CONFIRMED |
| 기존 조약 외교 연계 | 지연된 기존 .46 경로 후 `AGREEMENT.hoi4`의 양국 active_relations에 상호 guarantee·military_access 존재 | CONFIRMED. 기존 ID 대소문자 혼용을 보존한 실제 실행 경로 |
| 협정 뉴스·아이콘 | .5 제목·본문·기사 사진 표시. 미국 「대한민국 방위비」 양국 국기 아이콘과 −15.0% 실제 툴팁 | CONFIRMED |
| 자치령 | 같은 BEFORE를 재로드해 미국 2번 클릭. `DOMINION.hoi4`에서 양국 tier1 유지, 한국 사단 3개·미국 0개, 미국 쪽 puppet 레코드의 first=USA / second=KOR / autonomy_dominion. 엔진 트리거도 subject·dominion YES | CONFIRMED |
| 자치령 뉴스 | .6 「미국의 51번째 주 대한민국!」 제목·본문·별도 기사 사진 표시 | CONFIRMED |
| 주둔 거부 | 같은 BEFORE 재로드 후 미국 3번 클릭. `REFUSED.hoi4`에서 양국 tier1 각 1개, tier2 0개, requested/resolved 존재·approved/units_granted 부재, 사단 0개·한국 독립 | CONFIRMED |
| 한국 거부 통보·KATUSA 차단 | 한국 시점 사본 재로드 후 `.4` 배치 무산 통보와 사건 사진, 한국 tier1 아이콘·+5% 툴팁 표시. KATUSA 상세창의 주둔 승인 조건이 빨간 X이며 시작 불가 | CONFIRMED |
| 한국 자치령 통보·KATUSA 허용 | 한국 시점 사본에서 `.3`의 단일 「수락」, `.6` 뉴스, 정치 화면의 미국 종주국·「자치령」 표시. KATUSA 상세창의 승인 조건이 초록 체크이며 시작 가능 | CONFIRMED. KATUSA 완료 보상 실행과는 구분 |

UI 증거는 `runtime/screenshots/01-treaty-offer.png`부터 `14-katusa-available-as-dominion.png`까지다. 01–06은 미국 선택·뉴스·미국 상위 정신, 07–10은 한국 조약/거부 통보·기본 정신·KATUSA 차단, 11–14는 한국 자치령 단일 수락·뉴스·종속 지위·KATUSA 승인 조건이다. 실제 저장 사본과 범위별 추출은 `runtime/saves/{BEFORE,AGREEMENT,DOMINION,REFUSED}.hoi4` 및 각각 `.evidence.json`이다. 추출기 `runtime/extract_save_evidence.py`는 country별 politics·flags·units·diplomacy를 분리한다. puppet 관계가 종주국 쪽에만 기록되는 형식을 확인하고 알려진 PHI 종속 레코드로 판별을 보강했다. 전체 문자열 검색이나 종속국 자기 블록의 부재만으로 독립을 판단하지 않는다.

한국 수신 화면 검증을 위해 `KOR_DOMINION_PENDING.hoi4`, `KOR_REFUSED_PENDING.hoi4` 외부 진단 사본은 헤더의 player 및 player_countries 태그 두 곳만 USA→KOR로 바꿨다. 각각 6바이트 변경이며 나머지 게임 상태·예약 사건은 바이트 단위 동일하다. 해당 `.header-diff.json`에 원본·사본 해시와 변경 범위를 보존했다. 원본 저장을 편집하지 않았다. 변환된 사본을 실제 로드해 위 표의 한국 UI를 관찰했으며, 변환 바이트 검증과 화면 관찰을 구분한다.

### 정상 중점 진행과 별도 반복·전쟁 진단

run4는 `-start_tag=KOR`, nondebug, 한국어 UI의 전체 프로세스 재시작이며 실제 체크섬은 **1402**다. 외부 모드를 `runtime/fixture-normal/`로 교체했으므로 run3의 1b0d와 구분한다. 시작 시 「미국과의 접촉」 선행만 완료하고 정치력 300을 더했다. 조약·주둔 중점은 직접 시작하고 게임 시간을 진행해 완료했으며 두 중점의 `complete_national_focus`를 진단 모드에서 실행하지 않았다. 중점이 없던 기간에 쌓인 게임 기본 저장 진행도도 사용됐으므로 두 중점 모두 정확히 35일의 달력 간격을 따로 측정했다는 주장은 하지 않는다.

| 단계 | 관측과 근거 | 판정·한계 |
|---|---|---|
| 정상 조약·미국 AI | 중점 시작·완료 화면 15–16, 1936-02-05 한국의 기존 .46 수락 통보 화면 17. 미국은 AI이며 사용자가 미국 선택지를 클릭하지 않음 | CONFIRMED. 선행 준비부터 시작한 해당 실행의 수락 결과 |
| 정상 주둔·미국 AI | 35일 상세 안내 화면 18, 1936-03-29 중점 완료 화면 19. 03-30 협정 뉴스 20와 한국 승인 통보 21. 03-29 02시 엔진 체크포인트에서 양국 tier1 NO/tier2 YES, 요청·처리·승인·지급 표식 YES, 자치령 NO | CONFIRMED. AI가 협정 결과로 진입함. 미국 옵션 번호 자체를 로그가 출력한 것은 아님 |
| 최종 한국 정신·아이콘 | 04-06 한국 「미국 방위비」 양국 국기 아이콘과 소비재 공장 변동치 **35.0%** 툴팁 화면 22 | CONFIRMED |
| 5일 지연 재처리 | 외부 진단이 04-03 02시에 다섯 생산 helper를 다시 호출. 직후 양국 tier1 NO/tier2 YES, resolved·approved·units_granted YES, dominion NO. 이후 전쟁 저장에도 한국 명명 사단 3개·미국 0개 | CONFIRMED: 관측한 반복 호출에서 하위 정신·종속 분기·추가 사단 없음. 전쟁 전 정상 저장의 정확한 정신 개수를 추출한 증거와는 구분 |
| 전쟁 취소 | 외부 진단이 04-08 02시 한국의 대미 전쟁을 실행. 04-09 02시 체크포인트에서 양국 tier1/tier2 모두 NO. 한국 UI에서도 정신 제거 확인(23) | CONFIRMED. 정상 AI 전쟁 선택이 아닌 별도 강제 진단 |
| 저장·재로드 | 04-11 01시 `KOR_1936_04_11_01HOKNORMAL_temp.hoi4` 저장. 외부 `NORMAL_REPLAY_WAR.hoi4` 추출에서 두 중점 완료·양국 정신 0·한국 사단 3/미국 0·1936-04-08 02시 시작 war_relation 확인. 게임의 로드 목록에서 현재 저장은 불일치 경고가 없었고 직접 로드해 04-11 화면 24 관찰 | CONFIRMED: 해당 신규 전쟁 저장의 재로드. 변경 전 구저장 검증이나 정상 최종 파일명 저장 성공을 뜻하지 않음 |

증거는 `runtime/launch4/logs/`, `runtime/screenshots/15-normal-treaty-start.png`–`24-normal-save-reloaded.png`, `runtime/saves/NORMAL_REPLAY_WAR.hoi4` 및 추출 JSON에 보존했다. `runtime/normal-verdict.json`은 저장·트리거 로그·UI와 run3의 수량 증거를 분리한다. run4 도중 신규 현지화 세 파일의 조약 요청 툴팁 구분 문자만 콜론으로 수정했다. 실행 중 이미 로드된 문구와 수정 후 파일을 구분하며 수정 후 전체 재시작 UI·en-GB UI는 확인하지 않았다. 다른 생산 게임플레이 소스는 scope 수정 뒤의 상태를 유지했다.

### 실행 환경의 별도 오류

`runtime/log-review.json`은 초기 debug 실행에서 드러난 외부 진단 on_actions BOM 토큰 오류와 사단 지급 표식의 state scope 오류를 구분한다. 진단 파일 BOM을 없애고, 생산 helper의 표식을 실제 주 iterator 내부 `KOR` 국가 scope에 설정하도록 수정한 뒤 전체 재시작했다. `runtime/log-review.launch3.json`의 18:05:57 snapshot에는 새 생산 모듈·진단 모드 parser/scope 오류가 0건이다. 보존 로그를 재검토한 `log-review.launch3-final.json`은 최종 20행을 기존 descriptor 6건·rename 14건으로 분리하며 신규 모듈·fixture 오류는 0건이다. 중간 snapshot과 최종 보존 파일의 해시·행 수를 혼합하지 않는다.

기존 다른 모드 descriptor 6건과 save·continue_game·random 로그 이름 변경의 `errno 2`는 남는다. OneDrive의 한국어 사용자 경로가 로그에서 깨져 표시되지만 경로·OneDrive 자체를 원인으로 확정하지 않는다. 생성된 `_temp.hoi4`는 완전한 `HOI4txt` 파일이었으며 외부 증거 사본을 남겼다. 재로드용으로 검증 전용 새 파일 `HOK_USDEF_BEFORE.hoi4`에 바이트 그대로 복사해 실제 로드했다. 정상 파일명 확정 저장까지 성공했다고 주장하지 않는다.

`runtime/log-review.launch4-final.json`은 보존 로그 20개를 색인하며 최종 error.log 11행을 기존 descriptor 6건·rename 5건(continue 1/save 1/random 3)으로 구분한다. 새 방위비 모듈·외부 fixture 오류는 0건이다. 게임 체크섬 1402와 단계별 트리거 기록은 로그 근거이며, 중점 완료·선택 결과·재로드 화면은 별도 UI 근거다.

이전 debug 실행의 함장 현지화 중복과 `map/buildings.txt:66858`은 [로그 검토 안내](../HOK_LOG_REVIEW_SKILL.md)의 출처 구분 규칙에 따라 기존 파일·이전 기록과 대조했다. 새 협상 모듈 오류와 분리하며, nondebug 실행에 없다는 이유로 기존 문제를 수리했다고 판단하지 않는다.

### 테스트 종료와 사용자 환경 복원

run4 PID 24832를 게임 창에서 종료한 뒤 창 목록과 프로세스 부재를 확인하고 최종 로그를 보존했다. 검토한 외부 `runtime/restore-test-profile.ps1`의 명시 허용목록으로 이번 작업의 저장 8개와 임시 launcher descriptor 1개만 보존·정리했다. 복구 전 검증에서 Windows PowerShell 스크립트 실행 정책 및 JSON 배열의 Count 처리 문제가 각각 작업 전 차단됐으며, 영구 정책 변경 없이 단일 프로세스로 실행하고 배열 읽기를 수정한 뒤 복구했다. 이 두 차단 단계에서는 설정·저장을 변경하지 않았다.

`runtime/restore-result.json`의 최종 결과는 2026-11-11 18:44:54 KST **complete**다. `settings.txt`·`dlc_load.json`을 baseline과 바이트/해시 동일하게 복원했고, 기존 저장 **82개 전체의 크기·SHA-256이 동일**했다. 허용목록 밖 신규 저장은 0개다. 테스트 당시 설정·descriptor·8개 저장의 검증 사본은 `runtime/restore-preserved/20261111T0944271228081Z/`에 남겼다. 일반 게임 생성 로그·continue_game 파일과 다른 사용자 앱·기존 저장은 정리 대상에 넣지 않았다.

현재 구현의 남은 확인 범위는 조약 거부 .47 실제 수신, 응답 대기 중 모든 무효 사유의 엔진 분기, 기본 단계 정신을 보유한 상태의 전쟁 취소, 상대국 소멸 시 취소·평화 후 비복구, 변경 전 대표 저장의 grandfather 왕복, USA 기본 정신 아이콘 개별 화면, 콜론 수정 뒤/영어 UI, 다른 DLC 조합·멀티플레이·장기 캠페인이다. 상위 두 정신의 전쟁 취소를 기본 두 정신의 보유 중 취소 관측으로 확대하지 않는다. 이 항목은 소스 정책 또는 정적 확인과 실제 관찰을 구분하며 성공으로 간주하지 않는다. 커밋·푸시·업로드는 수행하지 않았다.
