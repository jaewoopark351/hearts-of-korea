# 2026-11-06 HOK 실행 로그 호환성 수리 구현·검증

상태: **코드 적용·정적 대조·1936→1939 자연 승계·한정 저장 검증·진단 없는 전체 재시작 완료 / 월간 경고의 후보 소진 상태 확인 / UI·기존 저장 역호환성·다른 환경은 미검증**.

사용자는 [구현 전 검토 기록](2026-11-06-hok-runtime-log-compatibility-review.md)과 단계별 설명을 확인한 뒤 `AGENTS.md`, `docs/`, 현행 설치본과 원작 Workshop 자료를 읽고 구현하도록 요청했다. 이전 문서화 전용 요청과 이번 구현 승인을 구분한다. 이번 작업은 확인된 호환성 오류 수리이며 중점 확장·재배치·보상 재조정·원본 전체 교체·배포 작업이 아니다. 커밋·푸시·업로드는 요청되지 않았고 실행하지 않았다.

## 1. 작업 기준과 자료 위치

| 역할 | 위치·상태 |
|---|---|
| 작업 저장소 | `C:\hoi\hearts_of_korea`; branch `feat/korean-focus-expansion-ai`, 시작 HEAD `ab0f6fb9822944378375d01610912b50af7b6353` |
| 시작 작업 트리 | README·중국/일본 정렬 정책의 수정과 11월 6일 검토 문서의 미추적 상태가 있었으며 보존했다. production 파일은 그 상태에서 추가 수정했다 |
| 현행 원본 | `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`; 읽기 전용 참조. 실행 버전 `Operation Postern v1.19.4.2.2da5` |
| 원작 자료 | `C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\2898629778`; 읽기 전용 역사적 출처. 이 ID는 업로드 대상이 아니다 |
| 실제 사용자 데이터 | `<USERPROFILE>\OneDrive\문서\Paradox Interactive\Hearts of Iron IV`; 이하 `<USER_DATA>` |
| 수정 전 로그 | `<USER_DATA>\logs` 원본을 읽고 외부 `user-logs-before/`에 복사했다. 원본 로그는 새 실행에 의해 갱신되므로 사본과 구분한다 |
| 이번 외부 작업 루트 | `C:\hoi\test\hok-compatibility-20261106-01`; 이하 `<TASK>` |
| 기준 사본·manifest | `<TASK>/source-before/`, `user-config-before/`, `user-saves-before/`, `user-save-inventory-before.json`, `baseline.json`, `baseline-manifest.json` |
| 실행별 증거 | `<TASK>/runs/<실행명>/launch.json`, `logs/`, 해당 실행의 `captured-save.hoi4`·검증 JSON. raw 로그·세이브·스크립트는 저장소에 추가하지 않았다 |
| 의존성·표시 환경 | 원래 선택은 저장소 HOK → 영문 번역 모드, 비활성 DLC 목록 없음. 실제 로그의 활성 DLC 36개, 언어 `l_korean`. 선언된 `Korean Language`는 이 선택 목록에 없으며 의존 선언은 변경하지 않았다 |

저장소·launcher descriptor의 지원 버전, 의존 선언, `remote_file_id`, path 관계는 그대로다. 실행에는 원래 모드 2개에 외부 진단 overlay 1개를 추가했다. 진단용 descriptor의 `replace_path="tests"`는 원본의 다른 시험 bundle 대신 이번 capture bundle만 실행하기 위한 외부 설정이며 production descriptor에는 추가하지 않았다.

테스트 중 자동저장은 꺼 기존 사용자 자동저장을 덮어쓰지 않았다. 엔진의 문서화된 test-fail capture를 이용해 고유 이름 `TEST_FAIL_HOK_COMPAT_CAPTURE_20261106_...`으로 시험 저장을 만들었다. 이 capture의 의도적 `FAIL`은 production 동작 실패 판정이 아니다. 이름 변경 `errno 2`가 발생한 경우 실제로 남은 `_temp.hoi4`의 내용·날짜를 확인하고 외부 증거 사본으로 보관했다.

## 2. production 변경

| 파일 | 적용 내용 | 보존한 부분 |
|---|---|---|
| [일본 scripted trigger](../../common/scripted_triggers/JAP_scripted_triggers.txt:444) | 현행 원본의 Pacific·Western·Northern breach 정의 3개 추가 | 기존 전체 정의와 한국 9도 판정, AI 호출·가중치 |
| [몽골 국가 history](../../history/countries/MON%20-%20Mongolia.txt:34) | 초이발산 초기 모집, 1939 지도자 역할 생성·승계 flag, 같은 1939 블록의 현행 대교리 설정 | HOK 전용 장군 9명·고위 지휘관 2명, 기존 인물 ID와 나머지 시작 지급 |
| [일본 국가 history](../../history/countries/JAP%20-%20Japan.txt:784) | HOK 민주 인물 7명을 WTT·NCNS 조건 아래 시작 시 등록 | shared root와 같은 DLC 범위, 기존 일본 초기화·1939 설정 |
| [일본 민주 shared focus](../../common/national_focus/HOK_JAP_democratic_shared.txt:77) | root reward의 7개 모집을 history 등록으로 이동 | root 보상·flag·relayout 순서, 후속 중점과 character 정의의 기존 `allowed`·`visible` 조건 |
| [한국 해군 중점](../../common/national_focus/korea.txt:2381) | 유효하지 않은 `cl_tech` 참조만 정리 | 순양함 `ca_tech`와 구축함 `dd_tech` 각각 보너스 1.0·2회, MIO·설계사·연구시설 효과 |
| [핀란드 강화 on_action](../../common/on_actions/finnppong_on_actions.txt:451) | 구 교리 기술 2개를 현행 대교리의 미선택 시 초기화로 이식, obsolete 포대 참조 정리, 아래 항공기 지급 오류 국소 수정 | 강화 옵션·FIN scope·기존 선택 교리·지급 수량·생산국·설계·다른 효과 |
| `music/Sinarirang.ogg` | 48kHz → 44.1kHz 재표본화 | 기존 등록·volume·stereo·nominal 320kbps·DATE/TRACKNUMBER metadata. 음량 조정·정규화 없음 |

생산 텍스트 6개는 변경 블록 근처에 `#20261106_kpopmodder: ...` 기여 주석을 두었다. 허용된 국소 변경을 역변환하면 기준 파일 바이트와 일치하는지 확인했고 UTF-8/BOM 여부와 CRLF를 보존했다. 기존 주석·ID·파일명·네임스페이스·현지화·레이아웃을 변경하지 않았다.

### 일본 추가 누락 6개를 이번에 넣지 않은 이유

구현 전 검토에서 발견한 다른 일본 trigger 6개는 현행 원본의 focus/decision에서 호출되지만 HOK가 제공하는 실제 두 파일과 `common/events/history`에는 호출이 없었다. 복구한 breach 3개도 이 여섯 개에 의존하지 않는다. 현재 유효 caller가 있는 세 정의만 추가했으며 전체 일본 snapshot을 최신화했다고 주장하지 않는다.

### 몽골·핀란드 교리의 적용 시점

몽골은 원본과 같이 **1939 시작 설정**에서 `mass_assault`·`new_strategic_destruction`을 설정한다. 이를 1936 시작의 추가 혜택으로 옮기거나 옛 기술 수를 숙련도·경험치로 환산하지 않았다.

핀란드는 기존 강화 옵션 안에서 `has_any_grand_doctrine = land/naval`을 확인하고 비어 있을 때만 `grand_battleplan`·`new_fleet_in_being`을 설정한다. 이미 선택한 다른 교리는 보존한다. 공군 교리를 이번 수리에 추가 지급하지 않았다. `basic_medium_battery`는 기존 `basic_battery`·`basic_heavy_battery`가 필요한 포대를 해금하므로 해당 참조만 정리했다.

### 실제 강화 옵션 실행에서 추가로 확인한 PL.7 오류

`fin-empty-on` 실행은 FIN 강화의 `add_equipment_to_stockpile`이 구체 장비 대신 archetype `cv_small_plane_naval_bomber_airframe`를 지정한다는 오류를 기록했다. 이 잘못된 블록은 수정 전 사본과 원작 Workshop에도 있다. 현행 원본 FRA history와 실제 시험 저장에는 `PL.7`이 `cv_small_plane_naval_bomber_airframe_0`으로 등록돼 있었다.

따라서 같은 지급의 type만 `_0`으로 맞췄다. **120대·생산국 FRA·변형명 PL.7·BBA 조건은 그대로**다. 수리 후 저장의 FIN 재고에서 해당 구체 변형 120대를 확인했다. 처음에는 북마크가 다른 1939 실행으로 확인했으므로 이를 엄격한 단일 변경 대조라고 표현하지 않았다. 이후 동일 1936·옵션·DLC 조건의 `fin-empty-on-final-1936`으로 원래 오류의 재발 부재와 120대 지급을 다시 확인했다.

### 음원 변환의 범위

기존 설치된 Ultimate Vocal Remover의 FFmpeg를 사용했으며 새 도구를 설치하지 않았다. 변환본 전체 디코드와 Vorbis header를 확인했다. Ogg granule상 길이는 `140.294979 → 140.310658초`로 약 **15.68ms**의 codec tail 차이가 있고, 재인코딩 RMS 차이는 약 **+0.0252dB**다. 청취로 내용·음질을 확인했다고 주장하지 않는다. 상세 도구 경로·입출력 해시·메타·디코드 결과는 `<TASK>/doctrine-assets/audio-validation.json`에 있다.

## 3. 수행한 확인

### 정적·소스 대조

- 원본 동등성·정의 유일성·scope·괄호/따옴표·UTF-8/BOM·개행·허용 구간 밖 바이트 보존을 확인했다. `git diff --check`를 통과했다.
- `<TASK>/source-attribution/scoped-source-static-validation.json`은 일본·몽골 국소 변경 검토다.
- `<TASK>/doctrine-assets/static-validation.json`의 최종 **14 PASS / 0 FAIL**은 소스·media 확인 항목이며 게임플레이 시험 횟수가 아니다. PL.7 수리 전 13/0은 이전 단계로 구분한다.
- `<TASK>/character-review/independent-source-review.json`은 최초 7파일 diff의 독립 정적 검토다. 그 뒤의 PL.7 한 줄 수리는 별도 `fin-carrier-bomber-repair.json`에 근거를 남겼다.

### 엔진 실행·실제 저장

아래 16/0·17/0·6/0 및 후속 19/0은 각 검증 도구의 확인 항목 수이며 게임 실행 횟수가 아니다. 서로 합산해 플레이 검증 횟수나 전체 호환성 통과 수로 쓰지 않는다.

| 실행·구분 | 확인한 결과 | 한계 |
|---|---|---|
| `fresh-default-forced-final` | 시작 몽골 인물·HOK 명단 확인. 일본 breach 3개를 실제 production trigger로 참/거짓 전환해 확인. 강제 몽골 역할·교리 효과 실행. 일본 민주 root·실제 내전 이벤트·새 장교 중점을 강제 실행한 뒤 7명 JAP 소속과 고문 역할 3개 유지 확인 | 정상 중점 선택·기간·내전 플레이나 UI 증거가 아니다. 강제 내전 때 엔진 front assertion 1건이 있었으므로 전체 무오류 실행으로 부르지 않는다 |
| 같은 실행의 `reward-validation.json` | **16/0**. FIN 옵션 꺼짐/빈 교리 유지. 실제 한국 중점 완료 효과 호출 뒤 보너스 지급. 1936.1.7 시험 저장에서 KOR의 `cr_bonus`·`dd_bonus` 각각 **1.0, uses=2, ca_tech/dd_tech** 확인 | 단순 `has_tech_bonus` 존재만으로 배율·횟수를 판정하지 않았다. 실제 연구 소비·UI는 미검증 |
| `fin-empty-on` | **17/0**. FIN 옵션 켜짐·비어 있던 육/해군 교리 초기화·MTG 포대 기술 지급·한국 보너스의 실제 저장값 확인 | PL.7 수리 전 실행으로 기존 stockpile 오류가 기록됐다 |
| `fin-empty-on-final-1936` | PL.7 수리 뒤 처음 오류가 났던 **동일 1936 시작·FIN 옵션 켬·DLC 구성**을 재실행했다. 보상 확인 **17/0**. 같은 `1936.1.2.1` 저장 비교에서 PL.7 재고 없음→120대, 해당 archetype 오류 1→0, 기존 두 교리 유지 확인. 보관 자료 비교 **19/0** | 두 실행의 인자·DLC mask·모드 목록·FIN history·보상/속도 fixture가 일치하고 capture 식별자만 다르다. 새 게임별 seed·프로세스·체크섬 차이는 별도 기록했다 |
| `fin-selected-native-1939-final` | **6/0은 FIN 교리·PL.7 관련 후속 확인 항목**이다. 선택한 `superior_firepower`·`new_convoy_raiding`이 실제 저장에도 유지되고 PL.7 120대가 있으며 해당 archetype 지급 오류가 없다. 별도로 같은 실행의 실제 1939.8.14 초기화에서 몽골 모집·지도자·승계 flag·두 교리를 엔진 로그로 확인했다 | 테스트용 기본 시작일·bookmark metadata와 dated FIN seed를 사용한 history 초기화 검사다. 1936 자연 승계·UI bookmark 선택·재로드와 구분한다 |
| `normal-1936-to-1939` | **자연 승계 PASS**. 실제 플레이 국가는 KOR이며 몽골은 AI로 진행했다. 1936 초기 등록·조기 승계 없음부터 강제 지도자/중점 효과 없이 진행했고, 1939년 1월 자연 승계를 관측했다. 실제 `1939.1.11.1` 저장에서 승계 flag·초이발산 stalinism 역할·몽골 집권 공산당의 인물 참조가 일치한다 | 벽시계 속도만 가속한 해당 싱글플레이 환경이다. UI·저장 재로드·기존 저장 복구·멀티플레이와 구분한다 |
| `clean-source-two-mods` | 진단 overlay를 제거하고 원래 HOK·영문 번역 **2개 모드**로 전체 재시작, `1.19.4.2.2da5 (8aa0)`·1936.1.1.12 일시정지 진입·device restore 완료 확인. 수정 대상 시작 오류는 보관 error.log에 없다 | 다른 등록 모드 descriptor·현지화 충돌·종료 시 로그 rename 등 9행은 남는다. 전체 무오류나 실제 화면 검수 결과가 아니다 |

진단 overlay의 후반 실행은 `GAME_SPEED_SECONDS`만 모두 0으로 설정해 벽시계 대기 시간을 줄였다. production에는 이 define을 넣지 않았고 시작 날짜·보상·이벤트 날짜 조건을 뛰어넘었다고 간주하지 않는다. 정상 진행 검증에서는 강제 지도자·교리·중점 효과를 호출하지 않는다.

동일 1936 조건의 PL.7 전후 비교는 `<TASK>/doctrine-assets/fin-empty-on-final-1936-regression.json`에 있다. 전후 모두 구체 변형 자체는 등록돼 있었으며 FIN 재고의 지급 여부와 오류가 달랐다. 이 비교도 정상 한국 중점 선택·기간·연구 소비를 검증한 것은 아니다.

자연 승계의 독립 streaming 검토는 `<TASK>/normal-review/natural-1939-succession-verification.json`에 있다. 저장의 global flag 날짜는 `1939.1.10.1`, 관찰 flag는 `1939.1.10.4`, 실제 저장 날짜는 `1939.1.11.1`이다. char `3245`의 `MON_khorloogiin_choibalsan`·MON 소속·stalinism 역할·특성과 MON 집권 참조가 일치한다. 로그 2892행의 첫 접두 시각과 중첩된 최종 시각이 달라 첫 접두만으로 이벤트 발생일을 단정하지 않았고 저장 상태와 함께 판정했다. 저장 SHA-256은 `0dbdf83eebb9bf98d94008cdee1df0688f8ad3da30dc81253f2df590d96a64c6`다.

자연 진행에는 `1936.02.04.01`의 `Scope does not have a Leader or it's of the wrong type` 내부 assertion도 기록됐다. MON 일별 관찰이 없었던 별도 새 게임 실행에서도 같은 날짜·`Fully cantons activated` 메시지와 함께 발생했다. 이것만으로 MON 관찰 또는 이번 일본 인물 이동을 원인으로 확정하지 않았다. `<TASK>/normal-review/assertion1733-review.json`에 비교와 원인 미확정 상태를 남겼으며 이 별도 현상을 숨기기 위해 production 조건을 삭제하지 않았다.

### 실패한 진단 준비도 이력으로 보존

- `monthly-original-save`: `-start_save=<절대 경로>`가 실제 사용자 저장을 불러왔다는 증거를 얻지 못했다.
- `fresh-default-forced`: 외부 CORE/REWARDS fixture의 BOM이 파싱을 방해했고 bracket 로그 표식이 확장돼 사라졌다. fixture만 BOM 없는 UTF-8·plain 표식으로 고쳐 전체 재시작했다. 이 예비 실행을 최종 PASS에 합산하지 않았다.
- `fin-selected-native-1939`: undated FIN seed가 native 1939 history보다 먼저 적용돼 기본 교리로 바뀌었다. production guard 실패의 증거로 쓰지 않았고, seed를 1939.8.14 dated 입력으로 바꾼 위 final 실행에서 확인했다.
- `original-save-bare-start-save`: task 전용 입력 사본·임시 resume index와 bare flag도 원래 저장 대신 1936 새 게임을 시작했다. 이 결과는 기존 저장 진단·역호환성의 증거가 아니다.

## 4. 일본 월간 요구 — 재현 후 production 유지

`common/on_actions/14_sea_on_actions.txt`는 이번에 변경하지 않았다. HOK·원본의 22개 후보를 대조하면 다섯 후보에 flag·보유량·경제법 조건 차이가 있다. 그러나 실제 정상 진행의 **1937.05.01.01**에 같은 경고를 재현했을 때, HOK와 현행 원본 조건 모두 유효 후보가 0개였다. 이번 재현에서 이 조건 차이가 직접 원인이 아니라는 사실을 확인했다. 사용자의 이전 저장 자체를 불러온 결과와는 구분한다.

실제 1936 초기 관측은 민간23·군수15·조선소14, 영향력 육군20·해군15·재벌15·정부10, 네 세력 모두 tier2, 요구0이었다. HOK·원본 조건 모두 22개 차단이지만 tier3+ 진입 조건 자체가 거짓이므로 원래 추첨은 실행되지 않는 상태다. 이것을 원경고 재현으로 취급하지 않는다.

실제 경고 시점에는 육군이 tier3, 다른 세력은 해군2·재벌2·정부1, 요구1개·누적2개, cooldown 없음으로 추첨 진입 조건은 참이었다. 육군 7개 후보는 각각 군수22>조선소17, 육군 참모총장 기용, 평시, 이전 병력 요구 flag, 트럭 재고>149, 기갑 개편 중점 미완료, 이전 포병 요구 flag/현재 mission에 막혔다. 다른 세력의 15개 후보는 tier 미달이었다. 원본의 1095일 flag도 1936년에 생긴 flag를 1937년 5월에 만료시키지 않으므로 만료 처리 복사로 이 재현을 해결할 수 없다.

**CONFIRMED — 이번 재현의 후보 소진과 추첨 진입 조건의 조합.** 효과는 실행되지 않았으며, 이를 HOK의 누락 정의나 잘못된 가중치 때문에 선택이 실패한 것으로 바꾸어 설명하지 않는다. 따라서 가중치·빈 선택지·flag 수명·실제 요구 규칙을 바꾸는 production 수정은 하지 않았다. 현행 원본에도 이 상태의 후보가 없다는 관측을 전체 일본 시스템 무결성이나 미래 flag 차이의 안전성으로 확대하지 않는다.

후보별 근거·두 조건군·동일 시각 로그는 `<TASK>/japan-monthly/normal-progress/first-all-zero-19370501.json`과 해당 문서가 가리키는 원시 스냅샷에 보존했다. 정상 진행의 월별 관측은 1939년 5월 전으로 한정한다. 기존 사용자 저장의 직접 상태 진단·다른 후보 조건 차이의 후속 정렬은 별도 범위다.

## 5. 검증 환경·설정·저장 정리

Computer Use native pipe는 재시도와 JavaScript kernel 재초기화 뒤에도 연결되지 않았다. 별도 Windows UI automation을 만들지 않고 설치된 게임의 자동 시작·on_action/event·문서화된 test capture로 검증했다. 실제 화면·툴팁·고문 기용 클릭·잠김/해금 표시·음원 청취는 관측하지 못했다.

검증 전 `settings.txt`, `dlc_load.json`, `pdx_settings.txt`를 외부에 보관했다. 다만 게임이 자동 갱신한 `gameplaysettings.txt`의 사전 사본은 빠뜨렸다. 이를 알린 뒤 사용자가 원복할 필요가 없다고 했으므로 **보통·철인 끔·역사적 AI 켬**은 현재 값으로 유지한다. 검증용 모드·autosave·text-save 설정과 사용자 원래 선택의 정리는 이 게임플레이 선호와 구분한다.

기존 저장 자동 로드를 시도하며 수동 입력 사본 `HOK_COMPAT_20261106_ORIGINAL_INPUT.hoi4`를 사용자 저장 슬롯에 임시 배치한 것은 외부 fixture 보관 원칙과 맞지 않았다. 이 사본만 외부 `user-saves-before/autosave_temp.hoi4`와 SHA-256이 같음을 확인한 뒤 제거했다. 기존 사용자 저장은 수정·삭제하지 않았다. 처리 근거는 `<TASK>/manual-input-copy-cleanup.json`에 있다. 엔진이 직접 생성한 고유 이름 시험 저장 원본은 실제 사용자 데이터에 두고 증거 사본을 외부에 두는 규칙과 구분한다.

마지막 재시작을 포함해 이 작업이 시작한 `hoi4.exe` 프로세스가 모두 종료됐음을 확인했다. 원래 `settings.txt`, `dlc_load.json`, `pdx_settings.txt`는 사전 사본과 SHA-256이 같고, 외부 진단용 launcher descriptor와 이번에 만든 resume index는 제거했다. 사용자 지시에 따라 `gameplaysettings.txt`의 현재 선호는 유지했다. 엔진이 갱신한 로그·cache·최근 실행 temp 정보까지 원래 바이트와 동일하다고 주장하지 않는다.

기존 사용자 저장 **23개**의 존재·크기를 확인했고 기준 사본이 있는 자동저장은 SHA-256도 같았다. 엔진이 생성한 고유 이름 시험 저장 원본 **7개**는 `<USER_DATA>/save games/TEST_FAIL_HOK_COMPAT_CAPTURE_20261106_...`에 유지하며 각각의 증거 사본은 `<TASK>/runs/`에 있다. 수동 입력 사본과 구분한다. 저장소에는 새 테스트/진단 스크립트·raw 로그·저장을 만들지 않았다.

정리 근거는 `<TASK>/cleanup-latest.json`, `cleanup/profile-and-save-audit-*.json`, `cleanup/final-process-state.json`이다. Steam이 실행을 추적한 사실은 `cleanup/steam-gameprocess-log-final.txt`에 보존했으나, **Steam의 Play 버튼 복귀·Running/Stopping 표시는 UI 연결 불가로 직접 확인하지 못했다.** 게임 프로세스 부재를 Steam UI 검증 완료로 바꿔 쓰지 않는다. Windows나 Steam을 강제 종료하지 않았다.

최종 production 7파일과 수정 전 사본의 해시, 읽기 전용 참조 식별자는 `<TASK>/final-source-manifest.json`에 있다. 이는 참조한 원본 파일의 식별 기록이며 설치본·Workshop 전체를 전후 해시 감사했다는 뜻이 아니다. 마지막 동일 조건 회귀 뒤에도 production 소스는 이 manifest와 같고, 설정·선택을 다시 정리했다. 진단 없는 `8aa0` 실행과 이후의 마지막 동일 조건 회귀를 서로 다른 실행으로 보존했다.

## 6. 남은 범위

- 일본 월간 요구의 기존 사용자 저장 직접 상태 진단과, 이번 후보 소진 재현의 원인이 아니었던 다른 조건 차이의 후속 정렬.
- 실제 고문 고용·표시와 연구 보너스 소비, 모든 DLC 조합·다른 정치 경로·멀티플레이·기존 사용자 저장 복구.
- 1939 시작에서 함께 나타난 다른 국가의 equipment variant·MIO·AI 명령 경고. 이번 변경 대상과 원인을 별도로 추적해야 하며 전체 호환성 수리 완료로 묶지 않는다.
- 기존 사용자 자동저장·설정의 복원과 새 저장 round trip은 서로 다른 검증이다. 이번 history 수리가 기존 저장을 자동 마이그레이션하지 않는다.

전체 무오류, 새 오류 0, 모든 경로 정상화, 저장 역호환성 또는 배포 준비 완료를 주장하지 않는다. 이어서 이 오류군을 수정하거나 검증할 때는 본 기록과 구현 전 검토를 함께 읽고 최신 source·설치본·활성 선택을 다시 확인한다.
