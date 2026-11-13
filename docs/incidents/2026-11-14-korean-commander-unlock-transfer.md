# 2026-11-14 한국 지휘관 해금 이관 구현·검증 기록

**구현과 해당 범위 검증·설정 복원을 완료했다. 최종 다섯 파일 정적 101 PASS / 0 FAIL, 전체 재시작 재로드를 거친 기존 국뽕 지휘 유지 총 150시간·새 국뽕 중점 전 미해금 총 106시간을 확인했다. 초기 네 파일의 세 설정 완료 검증은 해당 소스의 이력이다. 기존 로그 오류와 장기·다른 환경의 미검증 범위는 아래에 남긴다.**

사용자가 「다음 전쟁의 준비」 중점의 지휘관 해금 이관 계획을 제시하고 `AGENTS.md, /docs 읽고 구현해줘`라고 요청했다. 세 지휘관의 사용 시점을 검토하거나 후속 수정·검증을 진행할 때 [이관 계획](../HOK_KOREAN_COMMANDER_UNLOCK_TRANSFER_PLAN.md)과 이 기록을 함께 읽는다. 2026-11-13의 문서화 결과와 2026-11-14의 구현 결과는 각 날짜의 상태로 기록한다.

## 기준 소스와 위치

| 항목 | 확인한 기준 |
|---|---|
| 작업 원본 | `C:/hoi/hearts_of_korea/` |
| 브랜치·기준 커밋 | `feat/korean-focus-expansion-ai`, `065b5550448d6415901456503ef28b27f4530cc1` |
| 착수 당시 변경 | 앞선 문서 작업의 `docs/HOK_KOREAN_SECOND_WAVE_PLAN.md`와 새 이관 계획이 미커밋 상태였음 |
| 설치본 | `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/` |
| 설치 메타데이터 | `Operation Postern v1.19.5.0.7c6c (c184)`, Steam build `26479645`. `c184`는 설치 메타데이터의 값이며 시험 모드 조합의 런타임 체크섬은 후속 관측에 기록함 |
| 역사 원본 | `C:/Program Files (x86)/Steam/steamapps/workshop/content/394360/2898629778/`. 원작 출처 경로이며 현행 구문은 설치본에서 확인함 |
| 실제 사용자 데이터 | `C:/Users/jaewo/OneDrive/문서/Paradox Interactive/Hearts of Iron IV/` |
| 실행 로그 원본 | 위 사용자 데이터의 `logs/` |
| 외부 작업·증거 | `C:/hoi/test/hok-commander-unlock-20261114-01/` |

착수 시 `dlc_load.json`은 HOK 본체 → `C:/hoi/Hearts-of-Korea-anime/` → Workshop `1862018480`의 Anime History를 선택했다. 시험 구성은 Korean Language `2743487021` → HOK 본체 저장소 → 해당 외부 시험 프로필 순서로 설정한다. `disabled_dlcs`는 빈 배열이며 실제 DLC 조건과 조합별 로드는 실행 증거에 기록한다.

## 적용한 코드

기본·중견국·일반 국뽕의 새 게임에서 세 군사 역할은 `KOR_prepare_for_the_next_war` 완료를 해금 조건으로 사용한다. 초기 이관 네 파일에 기존 저장 호환 조건과 국가 역사 표식을 추가해 최종 수정 대상은 다섯 파일이다.

| 파일·사용처 | 적용 내용 |
|---|---|
| [한국 인물 정의](../../common/characters/KOR.txt) 1431–1440행 | `KOR_Beomdo_Hong` 원수의 중점 완료 조건과 표식 도입 전 국뽕 저장 보존 조건 |
| 같은 파일 1460–1469행 | `KOR_Jwajin_Kim` 장군의 같은 표시 조건 |
| 같은 파일 1489–1498행 | `KOR_Junggeun_Ahn` 장군의 같은 표시 조건 |
| [한국 역사](<../../history/countries/KOR - Korea.txt>) 6–7행 | 새 게임 국가 표식 `HOK_KOR_commander_focus_unlock_v1` 추가 |
| [한국 중점](../../common/national_focus/korea.txt) 5484–5487행 | 완료 효과에 세 인물의 `show_unit_leaders_tooltip` 안내를 추가 |
| [Korean 국뽕 설명](../../localisation/korean/HoK_start_game_setup_l_korean.yml)·[English 국뽕 설명](../../localisation/english/HoK_start_game_setup_l_english.yml) 25행 | `GOOKPPONG_ENABLED_TEXT_DESC`의 시작 지휘관 지급 문구를 수정하고 양 채널 헤더 바로 아래 동일한 기여 주석을 추가 |

새 게임은 국가 역사에서 새 표식을 받으므로 중점 완료가 세 군사 역할의 단독 해금 조건이다. 기존 국뽕 전역 플래그가 있고 새 국가 표식이 없는 저장은 기존 군사 역할 사용을 유지한다. `OR`의 두 경로는 중점 완료와 이 한정된 기존 저장 보존 조건이다. 기존 저장의 배치·미배치·재배치를 보존하며 강제 은퇴·재모집·표식 주입은 추가하지 않았다.

세 인물은 [한국 역사](<../../history/countries/KOR - Korea.txt>) 240–242행의 기존 등록을 사용한다. 홍범도 정치고문은 같은 인물의 기존 `political_advisor` 역할에서 대상 중점 완료를 평가한다.

중점 접근은 자유당 단독집권 또는 독립당 단독집권의 민주주의 선행 분기를 따른다. 완료 이력이 군사 역할의 해금 근거이며, 현재 정부를 검사하는 추가 조건은 없다. 완료 뒤 정권 변경의 실제 표시·지휘 결과는 실행 검증 항목에 포함한다.

## 초기 네 파일의 소스 대조 결과

기존 저장 호환 조건 추가 전의 외부 검토 결과는 **55 PASS / 0 FAIL**이다. 당시 네 파일의 실제 diff를 읽고 다음 범위를 대조했다. 최종 다섯 파일의 후속 검토는 별도로 기록한다.

- 세 군사 역할의 조건 변경과 중점의 세 안내 추가를 확인했다.
- 기존 인물 ID·정치고문·능력·특성·초상화와 중점의 기존 속성·보상을 대조했다.
- 한국 역사 모집, 일반 국뽕·중견국 시작 처리, 게임 규칙, 국민정신, 역사 AI, 국방장관 특성, GFX, 인물명 두 채널의 10개 파일에 대해 수정 전 해시와 바이트를 대조했다.
- 국뽕 플래그의 다른 소비자인 연구 슬롯 중점 우회와 특수부대 보상 분기를 대조했다.
- 두 현지화 파일의 변경 범위·동일 기여 주석·UTF-8 BOM·CRLF를 확인했다.

근거는 외부 경로의 `agent-review/static-review.json`, `agent-review/production-diff.txt`, `baseline/source-hashes.json`이다. 위 횟수는 소스·바이트 확인에 한정한다. 지휘관 화면·부대 지휘·정치고문 임용·저장 재로드의 결과는 아래 실행 기록에 각각 기록한다.

현행 설치본에서는 `common/characters/BEL.txt` 950–953행의 `corps_commander.visible.has_completed_focus`, `common/national_focus/belgium.txt` 1354행의 완료 보상 `show_unit_leaders_tooltip`, `common/characters/SPR.txt` 2325–2336행의 `field_marshal.visible` 완료 중점 조건을 구문 근거로 확인했다.

## 최종 다섯 파일의 소스 대조 결과

호환 조건을 추가한 최종 소스는 `agent-review/static-review-v2.json`에서 **101 PASS / 0 FAIL**이다. 실제 diff는 `agent-review/production-diff-v2.txt`에 있다. 세 `visible`의 중점 완료 또는 기존 국뽕·새 표식 부재 조건, 정적 8상태 진리표, 세 새 게임 설정의 완료 전·후 예상값을 확인했다. 이는 소스의 조건 계산이며 실제 새 게임이나 저장 로드의 실행 결과가 아니다.

한국 역사 파일은 국가 표식 한 개와 기여 주석을 추가했다. 이 변경을 제거해 재구성한 바이트가 수정 전 원본 해시와 일치하는지 확인했다. 기존 모집·정치고문·능력·특성·ID·국뽕의 다른 기능은 유지했다. 초기 `55/0` 보고서는 그대로 보존하며 두 횟수를 합산하지 않는다.

## 현재 적용 기준의 변경 영향 대장

아래 대장은 2026-11-14의 호환 조건 추가 후 적용 소스와 확보한 실행 자료의 상태다. 이관 계획에 남긴 2026-11-13 대장은 당시 조사·설계 이력으로 읽는다. 초기 네 파일 검증과 최종 다섯 파일 재검증을 구분한다.

| 대상·호출 경로 | 처리 상태와 기대 의미 | 확인 근거·남은 항목 |
|---|---|---|
| 홍범도 원수 표시 | 수정 적용. [인물 정의](../../common/characters/KOR.txt) 1431–1440행의 중점 완료·기존 저장 보존 조건 | 최종 소스 101/0. 기존 국뽕 저장 115시간 지휘 유지·새 국뽕 게임 52시간 중점 전 미표시 확인. 초기 세 설정 완료 UI는 앞선 소스의 결과 |
| 김좌진 장군 표시 | 수정 적용. 같은 파일 1460–1469행의 같은 조건 | 최종 소스·기존 국뽕 115시간·새 국뽕 52시간 확인. 초기 기본·국뽕 배치와 저장 이력 보존 |
| 안중근 장군 표시 | 수정 적용. 같은 파일 1489–1498행의 같은 조건 | 최종 소스·기존 국뽕 115시간·새 국뽕 52시간 확인. 초기 중견국·국뽕 배치와 저장 이력 보존 |
| 새 게임 국가 표식 | 수정 적용. [한국 역사](<../../history/countries/KOR - Korea.txt>) 6–7행의 새 게임 표식 | 최종 새 국뽕 저장 한 개·기존 저장 입력/115시간 후 모두 부재 확인. 새 게임·기존 저장 재로드 후속 확인 중 |
| 중점 효과 화면 | 수정 적용. [중점 정의](../../common/national_focus/korea.txt) 5484–5487행의 세 지휘관 해금 안내 | 이름·역할 참조와 실제 중점 효과 UI 확인 |
| 국뽕 설명 두 채널 | 수정 적용. [Korean](../../localisation/korean/HoK_start_game_setup_l_korean.yml)·[English](../../localisation/english/HoK_start_game_setup_l_english.yml) 25행의 시작 지휘관 지급 문구 정리 | 양 채널의 값·토큰·기여 주석·BOM·CRLF 대조. 별도 영어 번역 UI는 이번 실행 범위 밖 |
| 홍범도 정치고문·기존 인물 정의 | 의도적 유지. 같은 인물의 정치고문 고용·능력·특성·초상화·ID 사용 | 소스·바이트 대조, 국뽕의 150PP 실제 고용과 원수 지휘, v3의 실제 임명 링크 확인 |
| 역사 모집과 인물명·GFX | 의도적 유지. 한국 역사의 세 등록과 기존 이름·초상화 연결 사용 | 초기 관련 파일 바이트 대조·저장 각 한 개/KOR 확인. 역사 파일은 새 표식 추가로 변경됐으며 기존 모집 구문은 유지 |
| 기존 중점 보상·선행·기간·배치·AI | 의도적 유지. 기존 국민정신과 정치 경로의 접근·진행 사용 | 소스 대조, UI 35일 표시와 실제 선택·진행·완료, 기본 저장의 국민정신 판독 확인. 장기 AI 행동은 별도 범위 |
| 국뽕 플래그의 다른 소비자·시작 처리 | 의도적 유지. 연구 슬롯 중점 우회·특수부대 보상 분기·기존 시작 강화 사용 | 소스·바이트 대조. 기본의 두 강화 플래그 부재, 중견국·국뽕의 해당 표식 판독 확인 |
| 원래 플레이셋의 직접 덮어쓰기 후보 | 의도적 유지. 로컬 anime·Workshop `1862018480`·Korean Language `2743487021`의 현재 소스 읽기 확인 | `CONFIRMED`: 전체 txt/yml의 대상 중점·세 인물·국뽕 설명 키 검색과 관련 인물·중점·역사·현지화 상대 경로 검사에서 후보 0건. Anime descriptor의 `replace_path`는 sound·gfx 여섯 개, 나머지 두 descriptor는 없음. 전체 anime 런타임 호환성은 미검증 |
| 다른 정치 경로의 새 해금·서브모드 이식·지도 변경 | 제외. 이번 범위는 기존 중점으로 세 군사 역할의 사용 조건을 이전하는 작업 | 새 공통 해금 경로·서브모드 코드 이식·지도 수정은 적용 범위 밖. 해당 환경의 전체 호환성은 미검증 |
| Production-only 최종 저장 재로드 | 수정 적용한 조건의 재로드·시간 경과 확인 | PID 14084의 새 국뽕 저장은 추가 54시간·총 106시간 미해금 유지, 기존 국뽕은 추가 35시간·총 150시간 지휘 유지. 제한된 v4 대조는 각각 125일치/3직렬화차이, 140일치/차이0 |
| 최종 프로세스 종료·설정 복원 | 의도적 유지. 원래 설정 복원 확인 | 최종 PID 14084 정상 UI 종료·프로세스 부재. `dlc_load.json`·`settings.txt` 원본 해시 일치, 시험 포인터 제거 |
| 장기·다른 환경 검증 | 미확인. 이번 단기 한국 실행의 관측 범위 밖 | 1939 시작·정치 선행 경로 전체 정상 진행·장기 AI·다른 DLC·다른 모드 조합·멀티플레이 별도 미검증 |

## 외부 증거와 시험 프로필

아래 상대 경로의 기준은 `C:/hoi/test/hok-commander-unlock-20261114-01/`이다. 실제 helper·로그·저장·스크린샷·생성 보고서는 이 외부 경로에 둔다.

| 경로 | 원본·사본과 용도 |
|---|---|
| `baseline/config/` | 시험 전 사용자 설정과 런처 `.mod`의 증거 사본. 복원 대조의 기준 |
| `baseline/logs-original/` | 새 실행 전 실제 사용자 데이터 로그의 증거 사본 |
| `baseline/source/`·`baseline/source-hashes.json` | 수정 전 생산 네 파일과 앞선 문서 두 파일의 사본·생산 소스 해시 |
| `baseline/save-inventory.json`·`baseline/saves-at-risk/` | 시험 전 기존 저장 목록과 기존 임시·자동 저장의 보관 사본 |
| `agent-review/` | 정적 검토 helper, 결과와 생산 diff |
| `agent-review/static-review-v2.json`·`agent-review/production-diff-v2.txt` | 기존 저장 호환 조건·새 게임 표식을 포함한 최종 다섯 파일의 101/0 정적 대조. 초기 55/0 보고서는 별도 보존 |
| `runtime-support/inspect_commander_save.py` | native text 저장의 세 인물·중점·지휘 참조 읽기 도구. 역할 기록만으로 UI 가용성을 확정하지 않음 |
| `runtime-support/inspect_commander_save_v3.py` | 실제 `appointed_advisors` 링크를 등록된 역할·상태와 구분하는 후속 읽기 도구. SHA-256 `8359da4befc8c0df0f469e25441b6ec390defc4d8ab87e4b9fe8b4b35a714047` |
| `runtime-support/fixture/` | 선행 정치 경로를 합성 준비하고 상태를 관측하는 외부 진단 모드 원본 |
| `baseline-gook-fixture/` | 수정 전 생산 네 파일의 정확한 사본과 일반 국뽕 기본 선택을 결합한 원본 조건 대조 프로필 |
| `baseline-gook-fixture-profile-preparation.json` | 원본 대조 프로필의 초기 사본 일치·게임 규칙 키 두 개 변경·해시 기록. 후속 descriptor 의존성 보정은 실행별 사본에서 확인 |
| `profiles/default/`·`profiles/middle/`·`profiles/gook/` | 기본·중견국·일반 국뽕의 수정 후 실행 프로필. 생산 인물·중점·국뽕 현지화는 본체 저장소에서 공급 |
| `profiles-manifest.json` | 세 프로필 초기 생성 시의 파일 목록·기본 선택·해시·게임 규칙 변경 내역 |
| `profiles-political-power-seed-update.json` | 고문 채용 시험용 정치력 300을 선행 준비 결정 두 개에 추가한 뒤의 프로필별 소스·양 진단 설명 해시 |
| `control_run.ps1`·`control_run.py` | 외부 실행 helper. PowerShell 파일 실행 정책 거부 이력과 Python helper 준비 상태는 아래 기록을 따름 |
| `runs/original-gook/trial-classification.json` | PID 7412의 수동 국뽕 초기화 관측, 인물 소스 우선순위 미확정과 저장 형식·해시 기록 |
| `runs/original-gook-dependency-fixed/` | PID 19412의 의존성 보정 포인터 `launcher.mod`와 `process.json` |
| `runs/original-gook-correct-dependency/` | PID 19412의 첫 유효 원본 대조. UI·배치 스크린샷, 저장 사본, `commander-save-inspection.json`, `dlc_load.json`, 내부 descriptor·런처 포인터의 증거 사본 |
| `runs/patched-three-settings-ui/` | PID 376에서 UI로 설정을 선택한 수정 후 세 시작 설정의 중점·지휘·고문·합성 정권 변경 관측. `process.json`, `screenshots/`, `saves/`와 저장 캡처·분석 기록 |
| `runs/patched-three-settings-ui/patched-gook-post-unlock-save-capture.json` | 1936-02-07 06:00 게임 생성 임시 저장의 안정된 사본·크기·SHA-256과 읽기 전후 원본 일치 기록 |
| `runs/patched-three-settings-ui/patched-gook-post-unlock-inspection-v2.json` | 국뽕 후속 저장의 중점 완료·세 인물·국가 소속·지휘 링크 판독. `appointed_advisors`는 같은 저장 원문에서도 대조 |
| `runs/original-gook-correct-dependency/commander-save-inspection-v3.json`·`runs/patched-three-settings-ui/patched-gook-post-unlock-inspection-v3.json` | 같은 v3 분석기로 수정 전 국뽕의 고문 미임명과 수정 후 국뽕의 홍범도 정치고문 임명을 판독한 결과 |
| `runs/patched-three-settings-ui/patched-default-post-unlock-inspection-v3.json` | 기본 설정의 중점 완료·국뽕/중견국 플래그 부재·세 인물·김좌진 지휘·홍범도 고문 미임명 판독 |
| `runs/patched-three-settings-ui/patched-middle-post-unlock-save-capture.json`·`runs/patched-three-settings-ui/patched-middle-post-unlock-inspection-v3.json` | 중견국의 안정된 저장 사본·해시와 중점 완료·강화 표식·세 인물·안중근 지휘 판독 |
| `agent-review/default-factory-spirit-observation-v2.json` | 기본 설정 저장의 `politics/ideas` 국민정신과 한국 소유 15주의 명시 직렬화 공장 수준 합계를 판독한 보조 결과 |
| `agent-review/default-factory-spirit-observation-initial-scope-note.json` | 최초 보조 reader가 국민정신 scope를 잘못 찾아 false를 낸 경위와 후속 v2 사용 기준. 원 보고서도 보존 |
| `agent-review/middle-ahn-infantry-native-observation.json` | 중견국 저장의 안중근 군·두 사단·공유 보병 편제 참조를 native 저장에서 추적한 보조 결과 |
| `runs/patched-three-settings-final/logs/`·`agent-review/final-collected-log-review.json` | 세 설정 시험 종료 후 보존한 로그 20개와 유효 원본 대조의 오류 종류·변경 범위 비교. 재로드 실행 로그와 구분 |
| `runs/production-reload/` | 진단 모드 없이 Korean Language·HOK로 전체 재시작한 PID 21132의 메타데이터, 새 저장 재로드·시간 진행·재저장 사본과 변경 전 저장의 시간 경과 후 비표시·지휘 해제 UI |
| `agent-review/patched-gook-production-reload-comparison-v3.json` | 새 완료 저장의 production-only 재로드 후 상태 비교. 139항목 일치·군사 역할 `gfx` 3항목 직렬화 차이 |
| `runs/production-reload/legacy-gook-failed-before-guard-inspection-v3.json`·`agent-review/legacy-gook-before-guard-failure-comparison-v3.json` | 호환 조건 추가 전 기존 저장의 7시간 후 비표시·지휘 해제와 native 지휘 연결 상실 판독. 인물·군사 역할 기록은 유지 |
| `agent-review/production-reload-log-review.json` | 초기 `87af` 재로드의 실제 네 경고와 입력 저장 참조 검토. 세 설정 새 게임 로그·최종 `6aa1` 로그와 별도 기록 |
| `apply_legacy_preservation.py`·`legacy-preservation-patch.json` | 기존 저장의 시간 경과 후 비표시·지휘 해제 재현 뒤 적용한 제한된 호환 조건·새 게임 표식 패치와 변경 기록 |
| `baseline/source-before-legacy-preservation/KOR-history.txt` | 새 국가 표식 추가 전 한국 역사 파일의 증거 사본. 최초 소스 대조 시점과 후속 다섯째 파일 변경을 구분하는 기준 |
| `runtime-support/inspect_commander_save_v4.py` | 기존 v3를 보존하고 국가 표식·범위를 명시한 후속 읽기 도구. SHA-256 `e62fdd1fb62785cd9cd8f60d9ee7ee80d40ea647f5d0202e9489a2246b02872f` |
| `runs/legacy-guard-final/` | 최종 `6aa1` production-only PID 20340의 설정·로그·UI, 기존 국뽕 115시간 유지와 새 국뽕 중점 전 52시간 저장·v4 판독 |
| `agent-review/legacy-gook-final-guard-comparison-v4.json` | 원본 기존 저장과 최종 호환 조건에서 115시간 경과한 저장의 제한된 비교. 140항목 일치·군사 역할 `gfx` 3항목 직렬화 차이 |
| `agent-review/legacy-guard-final-log-review.json` | 최종 `6aa1` PID 20340의 보존 로그 비교. 후속 PID 14084 재로드 로그와 구분 |
| `runs/final-save-reload/` | 같은 최종 `6aa1`의 production-only 전체 재시작 PID 14084. 새 게임·기존 국뽕 저장의 실제 재로드·시간 진행 UI, 저장 사본·v4 판독·종료 후 로그 |
| `agent-review/new-gook-final-reload-comparison-v4.json`·`agent-review/legacy-gook-final-reload-comparison-v4.json` | 최종 새 게임·기존 국뽕 저장의 재로드 전·후 제한된 저장 대조. 자기 비교와 구분 |
| `agent-review/final-save-reload-log-review.json` | PID 14084의 마지막 보존 로그를 유효 원본 대조와 직전 최종 호환 실행 각각에 비교한 결과 |
| `restoration.json` | 시험 종료 후 원래 `dlc_load.json`·`settings.txt`의 SHA-256 일치 대조 |
| `agent-review/compare-helper-v3-appointed-self-smoke.json`·`agent-review/compare-helper-v3-unappointed-self-smoke.json` | v3 helper의 임명·미임명 자기 비교. 게임 호환 결과에 합산하지 않는 분석기 형식 확인 |
| `runs/` | 실행별 실제 로그·설정·관측·저장 사본의 인덱스 |

수정 전 일반 국뽕 대조 프로필은 `baseline/source/`의 인물·중점·양 국뽕 설명 네 파일을 같은 상대 경로로 공급한다. 수정 후 세 시험 프로필은 진단 파일 일곱 개와 게임 규칙 파일 하나로 구성한다. 중견국·일반 국뽕 프로필은 원래 `DEFAULT` 블록의 `default` 키와 선택할 옵션 블록의 `option` 키 두 개를 교환한다. 옵션의 `name`·문구·나머지 규칙을 대조한 결과는 각 manifest에 있다.

후속 시험 준비에서 선행 정치 경로 결정 두 개에 고문 채용 시험용 정치력 300을 각각 추가했다. 이는 시험 상태를 만드는 root의 선택이며 진단 설명 양 채널에도 수량을 반영했다. 대상 중점의 실제 35일 진행과 고문 채용을 관측하기 위한 합성 입력이다. 초기 프로필 manifest와 이 변경 후 해시를 각각 기록한다.

## 실행 이력과 확인 범위

아래 `7e87`의 세 설정 시험과 `87af`의 첫 production-only 재로드는 호환 조건 추가 전 네 파일 이관 소스의 관측이다. 당시 새 게임에는 후속 표식이 없으므로 최종 표식·기존 저장 보존 분기의 검증으로 합산하지 않는다.

| 항목 | 현재 확인 상태 |
|---|---|
| 첫 임시 포인터 | Windows 역슬래시 경로로 로더 경고가 발생한 시도. `runs/invalid-pointer/`에 보관하며 유효 대조 실행에서 제외 |
| 첫 규칙 프로필 | 옵션 이름을 교환한 구성에서 실제 기본 설정이 시작됨. `runs/profile-name-swap-invalid/`에 규칙·로그를 보관하며 일반 국뽕 대조에서 제외 |
| 보정 프로필의 CLI 직접 시작 | PID 7412는 실제 공장 14개를 표시했고 원본 사본의 우선순위도 미확정이었음. `runs/original-gook-invalid-control/`에 보관하며 일반 국뽕 대조에서 제외. 저장의 빈 `game_rules` 값은 별도 관측이며 선택 누락의 판정 근거로 삼지 않음 |
| PID 7412의 메뉴 수동 국뽕 | 만주 편입·공장 65개·함선 267척의 실제 초기화를 관측했으나 지휘관 목록에서 세 인물을 확인하지 못함. 당시 포인터와 내부 descriptor에 본체 의존성이 없어 원본 인물 사본의 우선순위가 미확정. `runs/original-gook/`에 보관하며 지휘관 대조 PASS·FAIL에서 제외 |
| PID 19412의 의존성 보정 대조 | 첫 유효한 수정 전 국뽕 대조 확보. 체크섬 `9c31`, 대상 중점 미완료, 세 인물 각 한 개, 국뽕 전역 플래그 값 1을 저장에서 확인. 홍범도 집단군 아래 김좌진의 두 사단과 안중근의 별도 군 두 사단 배치를 UI에서 관측하고 텍스트 저장을 확보함. 정상 UI 종료·창 소멸·프로세스 부재 확인 |
| 수정 후 일반 국뽕의 해금 | 완료 전·후 지휘관 목록 이미지와 완료 후 세 역할의 UI, 세 지휘 배치·홍범도 고문 임명·native text 저장 상태 확인 |
| 수정 후 기본 설정의 해금 | 실제 DEFAULT 규칙 선택, 중점 정상 UI 진행과 완료 후 세 역할 표시·김좌진 두 사단 배치·native text 저장 상태 확인 |
| 수정 후 중견국의 해금 | 실제 중견국 규칙 선택, 독립당 선행 합성 준비와 대상 중점 정상 UI 진행 뒤 세 역할 표시·안중근 두 사단 배치·native text 저장 상태 확인 |
| 대상 중점의 진행과 안내 | 국뽕에서 1936-01-01 정상 UI 시작, UI 기간 35일·초기 `focus_progress` 1, 1936-02-04 24:00 완료 후 첫 관측 기록. 선행 정치 경로는 합성 준비 |
| 수정 후 세 지휘관의 실제 부대 지휘 | 1936-02-07 06:00에 홍범도 집단군 아래 김좌진 군 두 사단, 안중근 별도 군 두 사단의 UI 관측과 저장된 지휘 링크 확인 |
| 홍범도 정치고문 채용과 원수 지휘 조합 | 국뽕에서 정치력 150을 지불한 고문 채용과 집단군 지휘의 동시 UI 관측 확보 |
| 완료 후 정부 변경 | 외부 진단 결정으로 비동맹 정부를 합성 설정한 뒤 같은 세 지휘관의 배치 UI 관측 확보 |
| 초기 새 저장·기존 국뽕 저장 재로드 | 첫 production-only의 새 완료 저장은 6시간 유지. 기존 미완료 국뽕 저장은 7시간 후 비표시·지휘 해제 관측. 해당 실패 뒤 호환 조건 추가 |
| 최종 기존 저장 시간 경과 | `6aa1`에서 표식 도입 전 국뽕 저장을 불러와 115시간 후 세 지휘관·배치 유지, target 미완료·새 표식 부재 native 확인 |
| 최종 새 게임 중점 전 | 일반 국뽕을 실제 선택한 새 게임의 52시간 후 세 역할 미표시 UI, target 미완료·새 국가 표식 한 개·국뽕 전역 표식 native 확인 |
| 최종 저장 재시작 재로드 | PID 14084에서 새 Jan3_16→Jan5_22 추가 54시간 미해금 유지, 기존 Jan6_19→Jan8_06 추가 35시간 지휘 유지. 초기 시작부터 각각 106시간·150시간 |
| 시험 프로세스 종료·설정 복원 | 최종 PID 14084 정상 UI 종료·프로세스 부재, 원래 설정 두 파일의 해시 일치와 시험 포인터 제거 확인 |

## 첫 유효한 수정 전 국뽕 대조

포인터와 내부 descriptor에 HOK 본체의 정확한 모드 이름을 의존성으로 명시한 뒤 PID 19412를 frontend로 시작했다. 원본 사본을 공급하는 조건에서 세 지휘관의 실제 표시·배치를 관측했다.

| 항목 | 확보한 관측 |
|---|---|
| 게임 버전·체크섬·날짜 | `Operation Postern v1.19.5.0.7c6c (9c31)`, `1936.1.1.24` |
| 대상 중점 | `KOR_prepare_for_the_next_war` 미완료 |
| 인물 수 | `KOR_Beomdo_Hong`·`KOR_Jwajin_Kim`·`KOR_Junggeun_Ahn` 각각 한 개 |
| 국뽕 표식 | 저장 105행의 전역 `kor_hok_gookppong_enabled_flag` 값 1 |
| 실제 지휘 배치 | 홍범도 집단군 → 김좌진의 보병 두 사단, 안중근의 별도 군 두 사단 |
| 저장 사본 | `runs/original-gook-correct-dependency/saves/original-gook-three-assigned-Jan01-24-temp.hoi4` |
| 저장 크기·형식 | 71,600,913바이트, native text |
| 저장 SHA-256 | `e959ba89cde7888ef965eab49b34357572e93a188fbc2e60f143fd815a6e3bf3` |
| 읽기 근거 | 같은 실행 디렉터리의 `commander-save-inspection.json`과 `screenshots/` |
| 종료 | 정상 UI 종료, 창 부재와 `Get-Process` 결과에서 PID 부재 확인 |

이 자료는 수정 전 일반 국뽕의 중점 미완료·지휘관 기배치 저장으로 확보했다. 수정 후 본체의 production-only 실행에서 처음 로드된 직후에는 세 배치가 보였으나 시간 경과 뒤 지휘관이 사라졌다. 해당 결과는 아래 재로드 기록에 구분한다.

## 초기 네 파일의 일반 국뽕 UI와 저장 상태

PID 376의 실행 프로필은 `profiles/gook/`이며 한국어 UI의 중점·지휘관·정치고문 관측을 진행했다. 자료는 `runs/patched-three-settings-ui/`에 있다. 이후 같은 프로세스에서 사용자 게임 규칙을 실제로 바꿔 기본·중견국의 새 게임을 각각 진행했다. Production-only 재로드는 후속 실행으로 구분한다.

| 항목 | 확보한 관측·자료 |
|---|---|
| 중점 시작과 효과 안내 | 1936-01-01에 실제 중점 UI로 시작. `gook-target-start-Jan01-12.png`, `gook-focus-tooltip-35days-benefits-three-names.png` |
| 진행 관측 | 시작 진행도 `focus_progress` 1과 UI 35일 표시. `gook-target-progress-Jan17-19.png`와 완료 후 첫 관측 시각 `1936.2.4.24`를 기록 |
| 완료 후 지휘관 | `gook-post-hong-visible-advisor-icon.png`, `gook-post-kim-ahn-visible.png`에서 완료 후 세 역할 표시를 관측 |
| 홍범도 고문 | 정치력 409에서 비용 150을 지불하고 259가 된 실제 채용 UI. `gook-hong-advisor-available-cost150-pp409.png`, `gook-hong-advisor-hired-slot-pp259.png` |
| 실제 지휘 배치 | 1936-02-07 06:00에 홍범도 집단군 아래 김좌진 군 두 사단과 안중근 별도 군 두 사단을 관측 |
| 정부 변경 | 외부 진단의 비동맹 정부 전환 후 같은 배치 UI를 확인. `gook-neutral-government-commanders-retained.png` |
| 저장 사본 | `saves/patched-gook-post-unlock-three-assigned-advisor-Feb07-06-temp.hoi4`, 72,812,553바이트, native text |
| 저장 SHA-256 | `8bd5e7a8db9553a6cbadd42d6f7d4d817df5980f7803f9e8150b7364921c5c2f` |
| 저장 캡처 범위 | `patched-gook-post-unlock-save-capture.json`에 읽기 전후 원본 크기·수정 시각의 일치와 사본 해시를 기록. 게임 생성 `_temp.hoi4`만 관측했으며 일반 이름의 최종 파일 rename은 미관측 |
| 저장된 완료·설정 | `patched-gook-post-unlock-inspection-v2.json`에서 날짜 `1936.2.7.6`, 체크섬 `7e87`, 대상 중점 완료, 국뽕 플래그 값 1, 중견국 플래그 부재 확인 |
| 저장된 인물 | 세 인물 각 한 개, 국가 KOR. native character ID는 2851·2852·2853, 군사 역할 ID는 658·659·660 |
| 저장된 지휘 | 홍범도 집단군 498 → 군 1, 김좌진 군 1 → 사단 2786·2787, 안중근 군 499 → 사단 2128·2137 |
| 저장된 고문 | 같은 저장 원문의 1,331,455–1,331,459행과 v3 결과의 `KOR/characters/appointed_advisors`에서 `political_advisor` → character 2851/type 73 임명 링크 확인 |

선행 정치 중점 네 개와 정치력 300은 외부 진단 결정의 합성 입력이다. 대상 중점은 실제 UI에서 선택하고 날짜를 진행했다. 실제 경과는 시작 진행도 1과 완료 후 최초 관측 시각을 함께 사용해 해석한다. 정부 변경도 진단 결정으로 준비한 상태이며 자연 정치 경로 전환의 관측과 구분한다. 이 단계의 저장 판독은 직렬화된 상태의 확인이었으며 엔진 재로드는 당시 대기였다. 후속 실제 재로드는 아래 초기 `87af` 실행에 기록했다.

## 초기 네 파일의 기본 설정 관측

같은 시험 프로세스에서 새 게임 사용자 규칙을 DEFAULT로 직접 선택했다. 로그 `01:34:38`의 규칙 관측은 DEFAULT YES·일반 국뽕 NO·중견국 NO다. 자유당 선행 경로를 합성 준비하고 1936-01-01 12:00에 대상 중점을 실제 UI로 시작했다.

| 항목 | 확보한 관측·자료 |
|---|---|
| 중점 진행 | UI 기간 35일. 완료 후 첫 관측 `1936.2.4.24`에서 대상 중점·국민정신 YES, 일반 국뽕·중견국 플래그 NO |
| 완료 후 실제 UI | 1936-02-11 13:00에 세 군사 역할의 표시와 김좌진의 보병 두 사단 정상 배치를 관측. `screenshots/default*.png` |
| 저장 사본 | `runs/patched-three-settings-ui/saves/patched-default-post-unlock-Kim-assigned-Feb11-13-temp.hoi4`, 72,690,346바이트, native text |
| 저장 SHA-256 | `8526c210606319afa69b6d750eb80ee285a96e7191d73b516405b7e086b8a88e` |
| 저장된 완료·설정 | v3에서 날짜 `1936.2.11.13`, 체크섬 `7e87`, 대상 중점 완료, 일반 국뽕·중견국 전역 플래그 모두 부재 확인 |
| 저장된 인물·지휘 | 세 인물 각 한 개·KOR 소속. 김좌진 군 1/type 53 → leader 659/type 4713 → 사단 2139·2130/type 51 |
| 저장된 고문 | 홍범도의 실제 정치고문 임명 링크 없음 |
| 국민정신·공장 보조 판독 | 실제 `politics/ideas` 아래 대상 국민정신 확인. 한국 소유 15주의 명시 직렬화 공장 수준 합계는 민간 9·군수 4·조선소 1 |

공장 수는 저장에 명시된 수준 합계이며 UI의 가용 공장 수와 구분한다. 최초 보조 reader는 `ideas`를 국가의 직접 자식에서만 찾아 false를 기록했다. 실제 저장의 `politics/ideas` 경로를 확인해 v2로 정정했고, 원 보고서와 `default-factory-spirit-observation-initial-scope-note.json`을 함께 보존했다. 국민정신 판정에는 후속 v2를 사용한다.

## 초기 네 파일의 중견국 설정과 분석기 확인

다음 새 게임에서 사용자 규칙의 중견국 옵션을 실제 선택했다. 로그 `01:47:10`은 중견국 YES·일반 국뽕 NO·대상 중점 미완료를 기록한다. 독립당 선행 경로를 합성 준비한 뒤 1936-01-01 12:00에 대상 중점을 정상 UI로 시작했다.

| 항목 | 확보한 관측·자료 |
|---|---|
| 완료 후 첫 일일 관측 | 로그 `01:51:53`, 게임 날짜 `1936.2.4.24`에서 대상 중점·국민정신·중견국 표식 YES, 일반 국뽕 표식 NO |
| 실제 UI 확인 시각 | 1936-03-08 19:00에 완료 팝업·세 역할 표시와 안중근 군의 보병 두 사단 배치를 확인. `middle-independent-focus-completed.png`, `middle-post-hong.png`, `middle-post-kim-ahn.png`, `middle-ahn-commanding-two-divisions.png` |
| 저장 사본 | `runs/patched-three-settings-ui/saves/patched-middle-post-unlock-ahn-assigned-Mar08-19-temp.hoi4`, 72,772,462바이트, native text |
| 저장 SHA-256 | `42c10702ac584befe5ef8f6a3c298ba6e99b5dd3ef2769fda24fbd47a4e65319` |
| 저장된 완료·설정 | v3에서 날짜 `1936.3.8.19`, 체크섬 `7e87`, 대상 중점 완료, 중견국 플래그 값 1, 일반 국뽕 플래그 부재 확인 |
| 저장된 인물·지휘 | 세 인물 각 한 개·KOR 소속. 군 1/type 53 → 안중근 leader 660/type 4713 → 사단 2137·2128/type 51 |
| 실제 사단 편제 연결 | 두 사단의 native 참조가 모두 편제 608/type 52 `Bobyeong-Sadan`으로 연결됨. 편제에 명시된 보병 연대 9개를 보조 판독에서 확인 |
| 저장된 고문 | 홍범도의 실제 정치고문 임명 링크 없음 |
| 저장 캡처 범위 | 이 단계에서 읽기 전후 원본 크기·수정 시각 일치와 사본 해시를 확인함. 일반 이름의 최종 파일 rename은 미관측이며 중견국 저장 자체의 엔진 재로드는 이번에 별도 수행하지 않음 |

일일 observer는 조건이 참인 것을 처음 관측한 콜백 시각을 기록한다. 정확한 중점 완료 순간은 이 기록만으로 산출하지 않는다. 중견국의 완료 팝업은 실제 날짜 진행 후 늦게 확인한 화면이며, 완료 후 첫 일일 관측과 UI 확인·저장 날짜를 각각 기록한다. 대상 중점은 실제 UI 선택과 날짜 진행으로 완료했다.

v3는 실제 고문 임명 링크를 등록된 역할·상태와 구분한다. 같은 분석기로 수정 전 국뽕 저장의 대상 중점 미완료·홍범도 미임명과 수정 후 국뽕 저장의 완료·홍범도 임명을 각각 확인했다. 임명·미임명 상태의 자기 비교는 각각 142항목 일치·차이 0이며 분석기 smoke에 한정한다. 이 횟수는 실제 게임 호환 검증 횟수에 더하지 않는다.

## 초기 세 설정 실행의 보존 로그

PID 376 종료 뒤 로그 20개를 `runs/patched-three-settings-final/logs/`로 보존했다. `agent-review/final-collected-log-review.json`은 유효 원본 대조의 로그와 이 사본을 비교한 결과다. Error 행은 원본 22행·세 설정 실행 48행이며, 시각만 정규화한 새 정확 키 9개는 날짜·파일명이 달라진 기존 rename 종류다. 새 오류 종류는 0개, 변경 범위와 일치한 오류 항목은 0개다.

Frontend 관련 행은 9→27, rename 관련 행은 합계 4→12였다. 원본의 한 차례 새 게임·저장과 수정 후 세 차례 메뉴 선택·저장은 횟수가 달라 발생률로 비교하지 않는다. 일반 이름의 저장 rename `errno2`는 두 로그에서 모두 관측했으며, 파일시스템·엔진 원인과 이번 변경의 책임은 미확정이다. 이 로그 대조는 UI·실행 효과·저장 판독·전체 재시작 재로드의 각각의 증거와 함께 읽는다.

## 초기 87af 재로드에서 발견한 기존 저장 문제

PID 21132는 외부 진단 모드를 제외하고 Korean Language·HOK 본체만 선택한 전체 재시작 실행이다. 런타임 체크섬은 `87af`다. 첫 로드 직후 표시와 시간 경과 후 상태를 각각 관측했다.

| 대상 | 관측·확인 범위 |
|---|---|
| 수정 후 국뽕 완료 저장 입력 | `1936.2.7.6`의 세 지휘 배치·홍범도 고문 임명 저장 |
| 실제 UI와 시간 진행 | 재로드 뒤 세 지휘 배치·홍범도 고문을 확인하고 6시간 진행해 `1936.2.7.12`에 재저장 |
| 출력 저장 사본 | `runs/production-reload/saves/patched-gook-reloaded-Feb07-12-temp.hoi4`, 72,721,078바이트 |
| 출력 SHA-256 | `0ad71e94f83380fff3e7110cacf21bb1e8d458744e5608159463542efcfb7e58` |
| 제한된 저장 대조 | v3 비교 139항목 일치·3항목 차이. 인물 ID·소속·역할·실제 저장된 능력·특성·진행 중 특성·개별 초상화와 고문 실제 임명·지휘 참조는 일치 |
| 세 직렬화 차이 | 세 군사 역할의 `gfx="GFX_portrait_unknown"`이 후속 저장에 명시되지 않음. 기본값 동등성이나 엔진 원인은 확정하지 않음 |
| 별도 캐시 관측 | 군 499의 `plan_value` 1→0.7, `our_power` 0→476.17177. 제한된 지휘관 동일성·연결 비교 밖의 관측으로 기록 |
| 변경 전 국뽕 미완료 저장 | `1936.1.1.24` 저장 로드 직후 세 지휘관과 기존 배치를 UI에서 확인 |
| 변경 전 저장의 시간 경과 | 7시간 뒤 `1936.1.2.7`에 세 지휘관 초상화 비표시·군 무지휘관 UI를 관측. `original-gook-commands-removed-after-seven-hours.png` |

새 저장의 실제 재로드·시간 경과와 제한된 저장 대조를 확보했으며 전체 142항목 동일이나 기존 저장 호환 통과로 표기하지 않는다. 변경 전 저장의 첫 표시만으로 시간 경과 호환을 보장할 수 없음을 확인했다.

호환 조건 추가 전 실패 저장은 71,881,282바이트, SHA-256 `81e39859791d2de1e37e82e25338225213ed01317577c46f3571436e1b629b8a`다. 제한된 v3 대조는 123항목 일치·4항목 차이이며, 군사 역할 `gfx` 세 항목 생략과 대상 지휘 집합 `1/2/3`의 연결 부재가 차이다. 세 인물·군사 역할·능력·특성은 저장에 남아 있다. 이 실패는 실제 비표시·지휘 해제로 기록하며 인물 삭제나 스크립트 강제 은퇴로 표현하지 않는다.

초기 `87af` 재로드 로그에는 네덜란드의 빈 함대 1434와 참조 경고 두 행, `invalid decision_to_re_enable`와 빈/중복 결정 경고 두 행이 실제로 있다. 입력 저장에는 task force가 없는 네덜란드 제3함대와 제거된 진단 결정 `HOK_CMDIAG_20261114_stage_independent`의 `decision_to_re_enable`이 남아 있다. 결정 경고의 진단 모드 제거 설명은 강하게 지지되며, 일반 엔진 원인과 전체 무관 판정은 미확정이다. 원본 새 게임 22행·이 재로드 20행은 조건이 달라 발생률로 비교하지 않는다. 변경 범위 오류 일치 0과 전체 재로드 경고 0은 다른 결론이다.

## 최종 호환 조건과 6aa1 실행

변경 전 미완료 국뽕 저장의 세 지휘관 비표시·지휘 해제를 확인한 뒤, 새 게임은 새 국가 표식으로 구분하고 표식 도입 전 국뽕 저장은 기존 사용을 유지하는 조건을 추가했다. 이는 기존 저장 보존을 위한 의도적인 호환 수리다. 세 군사 `visible`은 중점 완료 또는 `국뽕 전역 플래그 있음 AND 새 국가 표식 없음`을 평가한다. 한국 국가 역사는 새 표식을 추가하며 기존 세 인물 모집과 다른 시작 정보는 유지한다.

호환 조건 추가 전 `55/0`과 세 설정 실행은 앞선 이관 조건의 결과로 보존한다. 최종 다섯 파일은 정적 101/0을 확인했고 `legacy-guard-final` 전체 재시작에서 아래 조건을 관측했다.

| 최종 조건 | UI·저장 근거 |
|---|---|
| 실행 구성 | PID 20340, Korean Language·HOK 본체, 진단 모드 없음, 체크섬 `6aa1` |
| 기존 저장 시간 경과 | `1936.1.1.24`→`1936.1.6.19`, 115시간 후 세 지휘 배치 유지 |
| 기존 저장의 조건 | 입력·출력 모두 중점 미완료·국뽕 표식 있음·새 국가 표식 없음. 이 기존 저장 로드에서 새 역사 표식이 소급 추가되지 않음 |
| 기존 저장 사본 | `saves/legacy-gook-preserved-Jan06-19-temp.hoi4`, 72,519,262바이트, SHA-256 `7a22701799dfa8877778fc2bcebce66c63dfbe3f72f48cb626a13f73a9a46680` |
| 기존 저장 제한 대조 | v4의 140항목 일치·군사 역할 `gfx` 세 항목 생략. native ID·능력·특성·진행 중 특성·개별 초상화·지휘 집단의 ID·leader·member·subordinate 보존 |
| 새 게임 선택과 경과 | 일반 국뽕을 UI로 직접 선택, `1936.1.1.12`→`1936.1.3.16`, 52시간 후 목록 상·하단에서 세 역할 미표시 |
| 새 게임 저장의 조건 | 중점 미완료·국뽕 표식 있음·새 국가 표식 한 개. 세 인물은 각 한 개로 등록돼 있음 |
| 새 게임 저장 사본 | `saves/new-gook-pre-focus-Jan03-16-temp.hoi4`, 72,379,670바이트, SHA-256 `1ef12d3a4fd9012d1814d332bb01d885b8404c84b0fd3390a5d85c836d1ae6f5` |
| 종료와 후속 | PID 20340 정상 UI 종료·프로세스 부재 확인. 후속 전체 재시작 PID 14084의 두 저장 재로드 결과는 다음 절에 기록 |

최종 호환 조건에서 중점 완료까지 다시 진행한 세 설정의 실행은 별도로 수행하지 않았다. 초기 네 파일의 세 설정 완료 UI·지휘·고문 관측과 최종 조건의 정적 진리표·새 국뽕 중점 전·기존 국뽕 유지 결과를 각각 기록한다.

`agent-review/legacy-guard-final-log-review.json`의 PID 20340 로그 대조는 원본 새 게임 22행·현재 26행이다. 시각만 정규화한 새 정확 키 6개는 기존 rename의 날짜·파일명 차이이며 새 오류 종류 0·변경 대상 오류 일치 0을 기록했다. Text·graphics 로그는 시각 정규화 후 같았다. 같은 프로세스의 기존 저장 로드와 새 국뽕 게임은 두 차례 메뉴 진입이며 두 번의 전체 재시작으로 세지 않는다. 이 보고서는 후속 PID 14084 재로드를 포함하지 않으며 초기 `87af`의 네 재로드 경고도 해당 이력으로 보존한다.

## 최종 저장 전체 재시작 재로드와 복원

PID 20340 종료 뒤 최종 다섯 파일·Korean Language·HOK 본체의 production-only 구성으로 PID 14084를 전체 재시작했다. 체크섬은 `6aa1`이며 외부 진단 모드는 없다. 두 저장을 실제 UI로 불러와 시간을 진행하고 다시 저장했다. 아래 상대 경로의 기준은 외부 `runs/final-save-reload/`다.

| 항목 | 최종 결과 |
|---|---|
| 새 국뽕 저장 실제 재로드 | `1936.1.3.16`→`1936.1.5.22`, 추가 54시간·새 게임 시작부터 총 106시간. 지휘관 목록 상·하단에서 세 역할 계속 미해금 |
| 새 저장 조건·등록 | 새 국가 표식 한 개·값 1, 국뽕 전역 표식 있음·중견국 표식 없음, 대상 중점 미완료. 세 인물 각 한 개·기존 역할은 등록돼 있으며 대상 지휘 집단 없음 |
| 새 저장 사본 | `saves/new-gook-reloaded-Jan05-22-temp.hoi4`, 72,468,176바이트, SHA-256 `98811210f381bbed96b8cf52b44150176f65f01ec1fe52e0a43d8e8aa64f0021` |
| 새 저장 제한 대조 | 125항목 일치·군사 `gfx` 세 항목 직렬화 생략 차이. 인물·역할·실제 저장된 능력·특성·개별 초상화 보존. 역할 객체의 존재를 해금 표시로 취급하지 않음 |
| 기존 국뽕 저장 실제 재로드 | `1936.1.6.19`→`1936.1.8.6`, 추가 35시간·원본 대조 저장부터 총 150시간. 세 지휘 배치와 김좌진의 보병 두 사단 지휘 UI 유지 |
| 기존 저장 조건 | 새 국가 표식 계속 부재, 대상 중점 미완료·국뽕 전역 표식 있음, 세 인물 각 한 개 |
| 기존 저장 사본 | `saves/legacy-gook-reloaded-Jan08-06-temp.hoi4`, 72,558,497바이트, SHA-256 `26b97f566459b403ae734372c0ccf8ac7401ce294bf274d0ab732672159d3c65` |
| 기존 저장 제한 대조 | 140항목 일치·차이 0. ID·소속·역할·실제 저장 능력·특성·진척·개별 초상화·군/집단군 ID·leader·사단·하위 군 참조 보존. `gfx` 세 필드는 입력부터 생략돼 추가 일치 횟수로 세지 않음 |
| UI 자료 | `screenshots/legacy-gook-reloaded-three-assigned-Jan08-06.png`와 같은 디렉터리의 새 국뽕 목록 관측 자료 |
| 종료·복원 | 최종 정상 UI 종료·프로세스 부재 확인. 외부 `control_run.py restore` 종료 코드 0, 시험 포인터 제거 |

`restoration.json`에서 원래 `dlc_load.json`의 SHA-256 `47b2da184f63a826b854373b961d69b7830263b8a4935d91dd05f9a252f30052`, `settings.txt`의 SHA-256 `de97534fed2150477ee0b9144888b0794fc70379fe0a780c1e1c523f5b4f3088`이 각각 복원 후 값과 일치했다. 설정 복원 대조와 저장별 native 상태 비교는 각각의 근거로 기록한다.

마지막 `agent-review/final-save-reload-log-review.json`은 PID 14084의 error 16행을 원본 22행·직전 최종 실행 26행과 각각 비교했다. 두 기준 대비 새 오류 종류 0·변경 대상 오류 일치 0이며, 시각만 정규화한 새 정확 키 각 6개는 기존 rename의 날짜·파일명 차이다. 현재 행은 descriptor thumbnail 3·지원 버전 4·현지화 충돌 1·지도 건물 1·계속하기 rename 2·저장 rename 2·난수 로그 rename 3이다. Text·graphics 로그는 시각 정규화 후 같았다.

초기 `87af`에서 실제 관측한 빈 함대·진단 결정 경고 네 행은 마지막 error 파일에 없었으며 당시 기록은 보존한다. 마지막 로그의 `SINGLEPLAYER` 표식 한 개를 실제 UI 저장 불러오기 횟수와 동일시하지 않는다. 두 실제 로드는 각각의 UI·게임 날짜 진행·새 native 저장으로 확인했다. 로그의 변경 대상 오류 일치 0을 모드 전체 무오류나 전체 저장 호환성으로 확대하지 않는다.

## 시험 준비와 저장 형식의 해석

키보드·문자 입력은 시험 창에서 반응을 만들지 못했고 마우스 조작은 메뉴 전환을 만들었다. 외부 결정은 선행 정치 경로의 합성 준비와 상태 관측을 제공한다. 대상 중점의 실제 UI 진행 관측은 위 세 시작 설정에 각각 기록했다.

보정 프로필의 직접 시작에서 만든 저장 사본은 `runs/original-gook-invalid-control/saves/default-1936Jan08-01-temp.hoi4`, 72,499,592바이트다. 공장 14개를 표시한 실제 상태와 원본 사본의 우선순위 미확정을 기록한 자료로 남긴다. 이후 유효한 PID 19412의 일반 국뽕 저장에도 `game_rules = {}`가 비어 있었으므로, 빈 값만으로 규칙 선택 누락이나 CLI 문제를 판정할 수 없다. 기본값의 직렬화 생략은 가능한 설명이며 엔진 동작으로 확정하지 않았다. 국뽕 적용은 실제 초기화·전역 표식·인물 표시와 배치 근거로 판단한다.

PID 7412의 수동 국뽕 저장 사본은 `runs/original-gook/saves/manual-gook-Jan02-14-temp.hoi4`, 46,524,515바이트이며 헤더는 `HOI4bin5`다. SHA-256은 `75489c53f17e4d244caf659e3783ff93b1084a62d17ec5553bc7fbc62767d2a6`이다. 원본 인물 override 우선순위의 미확정 때문에 이 저장은 지휘관 이관의 기존 저장 호환 근거로 확정하지 않았다. PID 7412는 정상 UI 종료와 프로세스 종료를 확인했다.

의존성을 명시하기 전 PID 7412의 공장 14개 시작과 수동 국뽕의 세 인물 미표시는 각 상태의 관측으로 기록한다. 당시 본체와 원본 사본의 우선순위가 미확정이었으며, 의존성 보정 뒤 PID 19412에서 첫 유효 원본 대조를 확보했다.

초기 `settings.txt`의 `save_as_binary=no` 쓰기는 OS 접근 거부가 발생해 당시 원래 `yes` 값으로 진행했다. PID 7412의 CLI 직접 시작 저장은 텍스트였고 같은 프로세스의 메뉴 새 게임 저장은 `HOI4bin5`였다. PID 19412의 원본 대조 저장과 PID 376의 수정 후 국뽕 저장에서는 native text를 확보했다. PID 376의 `process.json`은 `text_save_setting=true`와 시험 설정 해시를 기록한다. 저장 분석은 실제 파일 헤더와 실행 경로를 기준으로 기록한다. 보존된 1.19.4 텍스트 저장 읽기는 분석기의 형식 확인에 사용했으며 이번 1.19.5 실제 재로드는 위 별도 실행에 기록했다.

외부 `control_run.ps1`의 파일 실행은 호스트 ExecutionPolicy에서 거부됐다. 정책을 변경하지 않고 일반 inline 실행 명령으로 PID 19412를 시작했으며, 외부 `control_run.py`를 후속 실행 helper로 준비했다. 이후 UI 조작과 실제 형식별 저장 관측을 이어갔다.

## 남은 검증 범위

초기 네 파일의 세 설정 UI·실제 지휘·고문 임용·합성 정권 변경·저장 판독과 첫 production-only 재로드는 위 이력으로 보존한다. 최종 다섯 파일은 정적 101/0, 실제 전체 재시작을 거친 기존 국뽕 지휘 유지 총 150시간·새 국뽕 중점 전 미해금 총 106시간, 원래 설정 복원을 확인했다.

최종 조건에서 세 설정의 중점 완료까지 다시 진행하거나 기본·중견국의 완료 저장을 각각 재로드하지 않았다. 선행 정치 경로 전체의 정상 진행·자연 정권 변경, 1939 시작, 0보다 큰 경험치 축적과 장기 유지, 장기 AI, 다른 DLC·모드 조합과 멀티플레이는 별도 미검증이다. 기존 저장의 미배치 인물·해제 후 재배치를 각각 조작한 독립 시험도 이번 기록에 포함하지 않는다.

기존 `docs/assets/korean-fascist-mobilization-validation-20260923/`의 시험 PNG 네 개, 합계 815,391바이트는 앞선 작업의 정리 미결 자료다. 이번 지휘관 검증 산출물과 구분한다.
