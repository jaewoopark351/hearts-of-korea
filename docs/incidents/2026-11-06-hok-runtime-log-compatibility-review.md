# 2026-11-06 HOK 실행 로그와 HOI4 1.19.4.2 원본 비교

상태: **문서화만 완료 / 아래 호환성 수정은 미구현 / 새 실행·재현·수정 후 검증 미실행**.

이 상태는 구현 승인 전 검토 시점의 이력이다. 이후 사용자가 구현을 요청한 작업을 이어서 확인할 때는 [별도 구현·검증 기록](2026-11-06-hok-runtime-compatibility-implementation.md)을 먼저 읽는다. 아래의 관측·미구현 제안을 수정 후 결과로 바꿔 쓰지 않는다.

사용자는 기존 실행 로그 중 Hearts of Korea와 관련된 항목을 검토하고, 설치된 원본과 비교해 대응 방향을 설명한 뒤 **문서화 작업만** 진행하도록 요청했다. 이 문서는 그 검토의 근거와 후속 수정 제안을 기록한다. 코드·자산·설정·저장·원본·Workshop 파일은 변경하지 않았으며, 게임 실행·테스트·진단 계측·커밋·푸시·업로드도 하지 않았다. 아래 수정 방향과 검증 목록은 실행 결과나 구현 승인이 아니다.

## 1. 기준과 원본 위치

| 별칭·항목 | 위치 또는 확인한 값 |
|---|---|
| `<PROJECT>` | `C:\hoi\hearts_of_korea`; 수정이 승인되면 작업할 저장소 |
| `<VANILLA>` | `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`; 읽기 전용 비교 원본 |
| `<HOI4_USER_DATA>` | `<USERPROFILE>\OneDrive\문서\Paradox Interactive\Hearts of Iron IV`; 사용자가 지정한 실제 사용자 데이터 위치. 개인 계정명은 별칭으로 생략 |
| 라이브 로그 원본 | `<HOI4_USER_DATA>\logs\error.log`, `system.log`; 원래 위치에서 읽기만 함 |
| 활성 HOK launcher descriptor | `<HOI4_USER_DATA>\mod\hearts of korea.mod`; `path="C:/hoi/hearts_of_korea"` |
| 활성 영문 번역 모드 | `C:\hoi\Hearts of Korea English Translation Anime Modder's Edition`; 별도 모드이며 이번 검토의 스크립트 경로 `common/history/events`를 제공하지 않음 |
| 문서화 전 Git | `feat/korean-focus-expansion-ai`, HEAD `ab0f6fb9822944378375d01610912b50af7b6353`; 작업 트리 clean |
| 실행 버전·체크섬 | `system.log:139`의 `Operation Postern v1.19.4.2.2da5 (0329)`; 이 실행의 모드 포함 체크섬이며 순정 체크섬으로 취급하지 않음 |
| 활성 모드 | `system.log:178–179`에 영문 번역과 HOK 2개. `dlc_load.json`의 기록 순서는 HOK → 영문 번역. 이것만으로 최종 VFS 우선순위 전체를 입증하지 않음 |
| DLC·언어 | `system.log:140`의 활성 DLC 36개, `dlc_load.json`의 `disabled_dlcs=[]`, `settings.txt:2`의 `l_korean` |
| descriptor | 버전 `1.0.0`, `supported_version="1.19.*"`, `Korean Language` 의존 선언, `remote_file_id="3793992662"`; 저장소·HOK launcher descriptor에 `replace_path` 선언 없음. 모두 그대로 유지 |
| 의존성 확인 한계 | `Korean Language`는 이번 활성 모드 목록에 없음. 이 사실을 위 스크립트 오류의 원인으로 단정하거나 의존 선언 변경으로 연결하지 않음 |
| 미확인 실행 조건 | launcher playset 이름, historical AI 설정, 전체 game rule·실행 옵션, 재현용 저장 상태 |

기존 사용자 실행의 로그와 파일을 `Get-Content`, `rg`, 파일 목록·수정 시각 조회로 읽고 원본과 대조했다. 새 대조 실행, 게임플레이 validator, 진단 스크립트는 실행하지 않았다. 문서화 중 마지막으로 읽은 `error.log`는 **21,250 bytes**, 수정 시각 **2026-11-06 14:28:50 KST**였고, 말미에는 게임 날짜 `1940.06.07.06`의 AI 명령 메시지가 있었다. 이 말미의 존재는 모든 진행 구간을 검증했다는 뜻이 아니다.

로그는 계속 갱신되는 원본이며 **NOT ARCHIVED**다. 증거 사본·해시 manifest·새 테스트 디렉터리를 만들지 않았다. 아래 행 번호는 당시 읽은 파일의 주소이며 이후 실행·업데이트로 달라질 수 있다. 과거 검증에서 보존한 로그와 이번 라이브 로그를 동일 증거로 취급하지 않는다.

## 2. 원본을 가져오는 범위

권장 방향은 **현행 설치본을 기준으로 필요한 정의·초기화 방식을 HOK에 부분 병합**하는 것이다. 원본 폴더 자체를 수정하거나, 현재 HOK 파일을 일괄 삭제하거나, 원본 파일을 통째로 덮어쓰자는 뜻이 아니다.

- HOK 전용 한국 9도 판정, 몽골 장군·고위 지휘관, 일본 민주 분기, 기존 보상과 ID를 보존한다.
- 원본의 정의를 가져올 때도 해당 디렉터리의 loader, 입력 scope, 호출 경로와 DLC 조건을 확인한다. 파일 이름을 달리해 추가하면 항상 안전하게 합쳐진다고 가정하지 않는다.
- 원본의 기술·교리 체계가 달라졌다면 기존 혜택과 적용 시점을 확인해 이식한다. 비슷한 이름으로 기계 치환하거나 잘못된 참조를 없애는 김에 보상을 줄이지 않는다.
- 기존 [중국·일본 정렬 정책](../CHINA_JAPAN_VANILLA_ALIGNMENT_POLICY.md)의 1.19.2 적용 결과는 과거 기록이다. 이번 1.19.4.2 비교가 그 문서의 검증 범위를 확대하거나 전체 최신 정렬을 완료한 것은 아니다.

## 3. 확인 사항과 수정 제안

### 3.1 일본 AI 트리거 누락

**CONFIRMED — 정의 누락과 호출 불일치.** `error.log:15–32`는 원본 `common/ai_strategy/JAP.txt:2531–2612`의 세 트리거 호출을 인식하지 못한다. `<VANILLA>/common/scripted_triggers/JAP_scripted_triggers.txt:524,534,544`에는 각각 다음 정의가 있지만, [HOK의 같은 파일](../../common/scripted_triggers/JAP_scripted_triggers.txt)은 442행에서 끝나며 정의가 없다.

- `JAP_pacific_approach_breached`
- `JAP_western_approach_breached`
- `JAP_northern_approach_breached`

HOK의 같은 상대경로 파일이 현행 정의를 가리는 상황이다. 호출 파일이 원본이라는 이유로 HOK와 무관한 오류로 제외하면 안 된다. 실제 방어 AI의 전선·명령에 미친 영향은 관측하지 않았다.

**미구현 제안:** 세 정의를 원본의 ID·조건 그대로 복구하고, [HOK 한국 지역 판정](../../common/scripted_triggers/JAP_scripted_triggers.txt:74)의 `1082–1084` 등 기존 차이는 보존한다. AI 가중치를 바꾸거나 실패 조건을 `always`로 대체할 이유는 없다.

같은 비교에서 `JAP_is_main_home_islands_state`, `JAP_boeitai_beachhead_state`, `JAP_boeitai_threatened_state`, `JAP_boeitai_coastal_state`(원본 76–121행), `JAP_state_is_soviet_bloc_controlled`, `JAP_borders_the_soviet_bloc`(488–521행)의 추가 누락도 확인했다. 이 여섯 개는 현재 로그의 세 오류와 구별하고, 실제 caller와 전이 의존성을 추적한 뒤 후속 병합 범위를 정한다.

### 3.2 몽골 인물 초기화와 승계

**CONFIRMED — 초기 모집 누락.** [HOK 몽골 history](../../history/countries/MON%20-%20Mongolia.txt:14)의 초기 목록에는 `MON_khorloogiin_choibalsan`이 없다. 모집은 같은 파일 109행의 `1939.1.1` 시작 설정 안에만 있다. 원본 동명 파일은 34행에서 처음부터 모집한다.

원본 `common/characters/MON.txt:56–80`의 해당 인물은 원수 역할을 가지고 있으며 지도자 역할은 없다. HOK 1939 설정은 109–111행에서 모집 → `promote_character` → 아마르 은퇴를 실행하지만, 원본은 102–113행에서 아마르 은퇴 → 지도자 역할 생성·승격 → `MON_choibalsan_ascended_flag` 설정을 한다.

`error.log:105`의 `1939.01.30.01` 오류는 [HOK `SEA_Japan.txt:12592`](../../events/SEA_Japan.txt:12592)의 `add_country_leader_role`을 지목한다. 파일명과 달리 이 구간은 몽골 승계 이벤트 `SEA_japan_popup_events.44`이며, 해당 역할 부여는 현재 원본의 대응 구간과 같다.

**STRONGLY_SUPPORTED — 이번 인물 오류의 원인.** 1936 시작에 모집되지 않은 인물을 1939 승계 이벤트가 사용한 것으로 뒷받침된다. 시작일을 구성하는 history 블록을 1936 게임의 도중에 실행되는 예약 이벤트로 취급하면 안 된다. 실제 저장 상태와 정상 진행 재현은 확인하지 않았다.

**미구현 제안:** 초기 모집을 원본에 맞추고, 1939 북마크의 승계 부분만 현행 지도자 역할 생성·승격·flag 구조로 이식한다. [HOK 전용 장군 9명·고위 지휘관 2명](../../history/countries/MON%20-%20Mongolia.txt:35)은 유지한다. 이름이 비슷한 `MON_horloogiyn_choybalsan`(HOK 27행, 원본 character 304행)은 참모총장용 별도 ID이므로 합치거나 이름을 바꾸지 않는다. 이 건만으로 이벤트·캐릭터 파일 전체를 바꿀 근거는 없다.

### 3.3 한국 해군 중점의 연구 범주

**CONFIRMED — 없는 기술 범주 참조.** `error.log:40`은 [「독일 조선공 포섭」의 `add_tech_bonus`](../../common/national_focus/korea.txt:2381)에서 `cl_tech`를 인식하지 못한다고 기록한다. 원본 `common/technology_tags/00_technology.txt:41–42`에는 `dd_tech`, `ca_tech`가 있고 `cl_tech`는 없다. 원본 `common/technologies/naval.txt:201,382`의 경·중순양함과 `MTG_naval.txt:742`의 순양함 선체는 `ca_tech`를 사용한다. 원본 일반 중점 `common/national_focus/generic.txt:915–921`도 순양함 보너스에 이를 사용한다.

**미구현 제안:** 같은 보상 블록의 유효한 `ca_tech`를 유지하고 잘못된 `cl_tech` 참조만 정리한다. 순양함 보너스 **100% 2회**, 구축함 보너스 **100% 2회**, MIO 안내와 다른 기존 혜택은 유지한다. 현재 원본에 맞춘 범주 대응은 확인했으나 실제 연구 보너스의 지급·소비는 미검증이다.

### 3.4 구형 교리·포대 ID 7종

**CONFIRMED — 현행 기술로 등록되지 않은 참조.** `error.log:33–44`의 일곱 ID는 HOK 소스에도 남아 있다. 로그의 파싱 메시지만으로 선택형 핀란드 강화가 실제 실행됐다고 판단하지 않는다.

| 위치 | 구형 ID | 원본 대조와 미구현 대응 방향 |
|---|---|---|
| [몽골 1939 기술 지급](../../history/countries/MON%20-%20Mongolia.txt:71) | `air_superiority`, `mass_assault`, `pocket_defence`, `defence_in_depth` | 원본 동명 history 59–62행은 구 지급을 주석 처리하고, 같은 1939 블록 79–80행에서 `set_grand_doctrine = mass_assault`, `set_grand_doctrine = new_strategic_destruction`을 사용한다. 해당 시작 연도를 유지해 현행 방식으로 맞추는 방향이다. |
| [핀란드 강화 교리 지급](../../common/on_actions/finnppong_on_actions.txt:461) | `trench_warfare`, `fleet_in_being` | `FINNPPONG_ENABLED`의 `on_startup` 옵션 범위를 유지한다. 원본 핀란드 history 499–501행의 현행 육·해군 교리 설정을 참고하되, 기존 선택을 무조건 덮어쓰지 않도록 초기화·재로드 조건을 먼저 확인한다. 이번 두 참조 수리가 원본의 공군 교리까지 추가 지급하는 근거는 아니다. |
| [핀란드 강화 포대 지급](../../common/on_actions/finnppong_on_actions.txt:503) | `basic_medium_battery` | 같은 블록의 `basic_battery`·`basic_heavy_battery`가 현행 포대를 해금한다. 원본 `MTG_naval_Support.txt:37–42,402–416`과 HOK Helsinki Class의 `ship_medium_battery_2` 사용(662·671행)을 대조하면 이 구 ID만 제거해도 해당 설계의 포대 해금이 보존됨은 소스상 확인된다. 실제 설계 사용은 미검증이다. |

구 교리 개수를 새 교리 숙련도 단계나 경험치로 임의 환산하지 않는다. `mass_assault`는 기술 ID로는 잘못됐더라도 대교리 ID로 쓰는 다른 문맥이 있으므로 전역 삭제·치환하지 않는다.

### 3.5 일본 월간 요구의 모든 후보 확률 0

**CONFIRMED — HOK 제공 파일에서 반복 발생.** `error.log:55–81`은 `1937.05`부터 `1938.11` 사이의 월별 경고를 기록한다. [HOK `14_sea_on_actions.txt:2280`](../../common/on_actions/14_sea_on_actions.txt:2280)의 `on_monthly_JAP` 안 2300행 `random_list`에 해당하며, 이번 호출에서 모든 후보가 0이 돼 효과가 실행되지 않았다는 사실을 확인했다.

원본의 대응 목록은 같은 상대경로 2340행이다. HOK에는 원본의 요구 flag 1095일 만료 처리(예: 원본 2370행 대비 HOK 2330행)가 없고 해군 요구 flag 이름에도 차이가 있다. **차이는 확인됐지만 그 차이가 이번 모든 후보 차단의 직접 원인인지는 UNPROVEN**이다. 당시 flag·세력 단계·보유량·활성 요구 상태를 읽지 않았다.

**미구현 제안:** 당시 상태에서 각 후보를 막은 조건을 좁힌 다음, 필요한 원본 수정만 HOK 차이와 대조해 병합한다. 월별 callback 전체 교체, 가중치 임의 변경, 빈 선택지 추가, 존재 검사를 덧붙여 메시지만 숨기는 수정을 먼저 하지 않는다. 원본의 만료 처리만 복사하면 이 경고가 해결된다고 약속하지 않는다.

### 3.6 일본 민주 인물 모집·음원 경고

**CONFIRMED — 경고 존재, 실제 인물 실패는 미확인.** `error.log:8–14`는 [HOK shared focus:77–83](../../common/national_focus/HOK_JAP_democratic_shared.txt:77)의 인물 7명 모집에 대해 시작 history에서만 실행할 것을 권고한다. 이 경고는 실제 인물 7명이 모두 등장하지 않았다는 증거가 아니다.

**미구현 제안:** 초기 소속 등록과 중점에 따른 역할·노출·기용 해금을 나누는 구조를 검토한다. [현재 character 정의](../../common/characters/HOK_JAP_democratic_characters.txt:29)의 advisor `allowed`와 지휘관 `visible`, 후속 중점·내전 소속을 함께 확인해야 한다. 일곱 줄을 history로 옮기기만 하면 기존 등장 시점과 동작이 보존된다고 단정하지 않는다.

`error.log:7`의 `Sinarirang`은 [HOK 음원 정의](../../music/hok_music.asset:2)의 44.1kHz 권장 경고다. 기능 수리 뒤 별도 음원 변환 대상으로 검토할 수 있으나, 이번에는 원본 음원·자산·크레딧을 건드리지 않았다.

## 4. HOK 원인으로 확정하지 않은 메시지

| 로그 대상 | 파일 출처 확인 | 이번 판정 |
|---|---|---|
| `events/LAR_Spain.txt:6959,7344` | HOK·번역 모드에 해당 파일 없음; 원본의 `SPR_anarchist_commune` 승격 | 원본 코드에서 발생했지만 순정 단독 재현 없이 원본 자체 버그로 확정하지 않음 |
| `common/decisions/GER.txt:382–383` | HOK·번역 모드에 해당 파일 없음; 원본의 저항·순응도 효과 | 같은 이유로 HOK 직접 수정 대상에 자동 편입하지 않음 |
| `common/technologies/support.txt:928` 등 | HOK·번역 모드에 해당 파일 없음; 원본의 HQ 편제 변경 | 원본 코드의 경고이며 실제 상태와 순정 대조는 미확인 |
| `AI tried to post an invalid command` | 국가·호출 파일이 로그에 표시되지 않음 | HOK 원인·무관 모두 미확정 |
| `continue_game`·`autosave` 이름 변경 실패 `errno 2` | 실제 사용자 데이터 경로의 파일 처리 | 실제 저장 파일의 갱신·재로드를 별도 확인할 문제. OneDrive나 HOK를 원인으로 단정하지 않음 |
| 타 Workshop descriptor의 `supported_version`·`thumbnail` | 로그 1–6행의 별도 등록 모드 descriptor | 이번 HOK 코드 수리 범위에서 제외 |

## 5. 후속 우선순위와 검증 계약 — 모두 미실행

1. 원인이 명확한 일본 AI 정의·몽골 인물 초기화·한국 연구 범주부터 작은 호환성 변경으로 다룬다. 몽골 1939 교리 이식은 인물 수리와 구분해 기록한다.
2. 핀란드 강화의 원래 혜택과 조건을 보존해 교리·장비 참조를 정리한다. 일본 월간 요구는 상태 확인으로 원인을 좁힌 뒤 수정 범위를 결정한다.
3. 일본 민주 인물 lifecycle과 음원 경고는 별도 기능 단위로 검토한다. 로그 행 수 감소를 기능 정상화로 취급하지 않는다.

구현·검증이 요청된 뒤에는 [프로젝트 검증 점검표](../VALIDATION_CHECKLIST.md)를 읽고 다음 항목을 구분해 기록해야 한다. 이 목록은 이번 작업의 PASS 결과가 아니다.

- 동일 버전·DLC·언어·모드 순서의 기준과 수정 후 로그, 필요시 순정·의존 모드 대조. `Korean Language` 의존 선언과 실제 활성 선택도 기록한다.
- 몽골 1936 새 게임의 정상 1939 승계, 1939 북마크의 지도자·역할·flag, HOK 전용 인물 유지.
- 일본 AI 정의 등록과 관련 방어 판정의 동작, 한국 9도 판정 유지. 누락 정의 외 추가 차이의 실제 호출 여부.
- 한국 해군 중점의 표시·정상 완료·연구 보너스 적용·소비, Man the Guns 유무의 범위.
- 핀란드 강화 기본/활성, 기존 대교리 선택·재로드, Man the Guns 유무와 함정 설계 유지.
- 일본 월간 요구의 발생 가능한 상태와 모든 후보가 막힌 상태, 요구 수명·재발·장기 진행.
- 일본 민주 인물의 해금 전후·내전 소속·지도자·지휘관·고문 동작. 실제 저장·재로드와 장기 AI·멀티플레이는 필요한 범위별로 별도 기록.

초기 history 수정은 이미 시작한 저장을 자동 복구하는 절차가 아니다. 진행 중인 저장 복구·마이그레이션은 새 게임 검증과 구분하고 별도 범위로 다룬다. 향후 테스트·로그 사본·스크립트·백업은 `C:\hoi\test\<task-or-run-id>\`에 두며 저장소나 배포 패키지에 생성하지 않는다. 이번 문서화에서는 그 디렉터리도 만들지 않았다.

## 6. 과거 기록과 이번 문서의 경계

- [2026-09-09 일본 UI 사건](2026-09-09-japan-imperial-influence-inlay-offscreen.md:83)은 인물 모집 경고 7건과 `cl_tech`가 당시에도 있었음을 기록한다.
- [2026-10-31 민주 배치 검증](2026-10-31-korean-democratic-focus-compaction.md:141)은 기존 일본 모집·전략 트리거·구 교리·장비·연구 범주·음원 경고가 남았다고 기록한다. 당시 배치의 검증을 이번 수리의 검증으로 재사용하지 않는다.
- 이번 문서는 최신 원본과의 읽기 전용 비교 및 미구현 제안의 유지 기록이다. 전체 HOK 무오류, 새 오류 0, 수정 완료, 현재 저장 호환성을 주장하지 않는다.
