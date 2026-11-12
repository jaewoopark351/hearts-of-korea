# 한국 신규 모집 과학자 전용 초상화 구현

2026-11-12(KST). [최초 계획과 바닐라 근거](../HOK_KOREAN_SCIENTIST_PORTRAIT_PLAN.md)에 대한 사용자 구현 요청으로 한국의 신규 모집 과학자용 초상화 풀을 추가했다. 남성 4장과 여성 4장은 이 작업에서 정한 구성이다. 본체에 어울리는 사실적 그림체의 신규 AI 생성 인물을 사용하며 현재 애니 서브모드 조합도 같은 신규 풀을 공급받도록 배치했다.

같은 날 후속 [이름 현지화 작업](2026-11-12-korean-random-name-localisation.md)에서는 한글 직접 표기를 시험한 뒤, 사용자의 후속 요청으로 신규 이름 목록을 원래 로마자 표기로 복원했다. 고정 과학자 네 명의 한글 현지화는 유지한다. 아래 로마자 이름과 사실적 신규 그림은 이 초상화 시험 당시의 관측이다. 후속 이름 시험에서는 애니 서브모드의 같은 신규 DDS 경로에 별도 그림 8개가 존재하는 조건을 기록했으며, 이를 아래 시험에 소급 적용하지 않는다.

## 기준 소스와 작업 범위

시작 브랜치는 `feat/korean-focus-expansion-ai`, 커밋은 `cdc022eee15fbf7404d4cb30cf2d0102d29e550c`다. 시작 시 `AGENTS.md`의 계획 문서 링크와 미추적 `docs/HOK_KOREAN_SCIENTIST_PORTRAIT_PLAN.md`가 앞선 문서화 작업으로 존재했다.

설치본은 HOI4 `Operation Postern v1.19.4.2.2da5`, Steam build `26409260`이다. 사용자 선행 실행과 이번 시험의 메인 메뉴 체크섬은 각각 `0a55`로 관측했다. 활성 DLC는 36개이며 `Gotterdammerung`을 포함한다. 실제 사용자 데이터 위치는 `C:/Users/jaewo/OneDrive/문서/Paradox Interactive/Hearts of Iron IV/`, 언어는 `l_korean`, 원래 모드 순서는 HOK → `Hearts-of-Korea-anime`다. 런처의 두 `.mod` 파일은 각각 작업 저장소와 `C:/hoi/Hearts-of-Korea-anime/`를 가리킨다.

시험·생성 원본·변환 중간물·보고서의 기준 경로는 `C:/hoi/test/hok-scientist-portraits-20261112-01/`다. 이 문서의 외부 증거 경로는 해당 디렉터리 기준이다.

## 적용한 연결과 자산 출처

| 파일 | 적용 내용 |
|---|---|
| [00_portraits_KOR.txt](../../portraits/00_portraits_KOR.txt) | 기존 `KOR` 블록에 남성·여성 각 4개의 `scientist` 스프라이트 목록 추가 |
| [HOK_KOR_scientist_portraits.gfx](../../interface/HOK_KOR_scientist_portraits.gfx) | 프로젝트 소유 스프라이트 8개와 DDS 상대 경로 연결 |
| `gfx/leaders/scientists/HOK_KOR/portrait_HOK_KOR_scientist_{male,female}_01~04.dds` | 새로 제작한 런타임 초상화 8개 |
| [자산 manifest](../data/HOK_KOREAN_SCIENTIST_PORTRAIT_ASSET_MANIFEST.json) | 각 생성 프롬프트·원본 경로·SHA-256·변환 과정·DDS 규격·최종 해시 기록 |

목록의 ID는 `GFX_HOK_KOR_scientist_{male,female}_01`부터 `04`까지다. 생산 텍스트의 두 변경 단위에 `#20261112_kpopmodder` 기여자 주석을 붙였다. 기존 육군·해군 목록의 바이트를 보존했고 원래 한국 파일의 UTF-8 BOM 없음·CRLF·EOF 개행 없음 형식을 유지했다.

초상화는 `image_gen.imagegen`으로 각각 생성했다. 도구가 실제 모델명을 노출하지 않아 manifest의 모델 값은 `not_exposed`다. 생성 입력 참조 이미지는 없으며 가상의 한국 과학자를 시대에 맞는 복장과 서로 다른 연령·인상으로 그렸다. 기존 바닐라·고정 인물 DDS는 규격과 화면 구성의 참고 자료다.

선택한 생성 PNG는 `art/generated/`에 보존했다. 생성 도구의 기본 저장 위치와 외부 보존본의 경로·해시 대응은 `art/generation-provenance.json`과 자산 manifest에 있다. 중앙 종횡비 crop과 bicubic 축소로 각각 156×210, uncompressed BGRA32, mipmap 1, 131,168바이트 DDS로 변환했다. 외부 변환 결과는 `art/final-dds/`, 실제 크기 검수 이미지는 `art/final-dds/native-contact-sheet.png`다. 최종 DDS는 저장소의 런타임 경로에 복사하고 변환 결과와 해시를 대조했다.

애니 서브모드의 `replace_path="gfx/leaders/KOR"`와 신규 자산 경로의 범위를 확인했다. 신규 DDS는 `gfx/leaders/scientists/HOK_KOR/`에서 공급한다. 고정 황부길·조경연·도상록·김용관은 현재 `characters_HoK.gfx`의 개별 연결을 회귀 확인 기준으로 사용했다.

## 정적 확인

| 확인 | 결과와 증거 |
|---|---|
| 목록·GFX와 기존 육군·해군 부분 | 11 PASS. `production-text/source-checks.json` |
| DDS 헤더·크기·형식·알파·해시 | 8개 PASS, 0 FAIL. `art/final-dds/dds-format-validation.json` |
| 생성 원본·외부 보존본·변환 결과·저장소 DDS와 참조 연결 | 8개 PASS, 0 FAIL. `validation/scientist-asset-manifest-validation.json` |
| 독립 최종 소스 검토 | 26 PASS, 0 FAIL. 최초 `validation/source-final-review.json`과 최종 `validation/source-final-review-post-whitespace.json`. 기존 고정 과학자 정의·스프라이트·DDS, 육군·해군, 공용 바닐라 풀 보존 포함 |
| 실제 크기 그림 | 남녀 8장의 얼굴·머리 배치와 투명 경계를 contact sheet에서 확인 |

바닐라의 국가별 `PAK`·`RAJ` 과학자 목록은 이 구성의 구문 근거다. 한국의 cosmetic tag 후보 13개는 형성·정치·환국 8개와 종속국 on_action 5개다. 각 ID·호출 위치·유지/제외/미해결 분류는 `validation/source-final-review.json`의 대장에 있다. 별도 cosmetic 초상화 블록은 추가하지 않았으며 상속 동작은 실행 미검증이다. 정적 검토 초기의 Git LF 원문과 작업 파일 CRLF 비교 실패는 `source-final-review-initial.json`에 보존했고, 최종 결과는 checkout 필터를 적용한 Git 기준본과 비교했다.

실행 검증 뒤에는 새 과학자 블록 앞 빈 줄의 탭 1바이트만 제거했다. 수정 전 사본은 `production-text/00_portraits_KOR.before-whitespace-fix.txt`에 있다. 위 최종 정적 검토 26개와 `git diff --check`가 통과했다. 런타임 관측은 이 공백 정리 전 파일에 대한 것이며, 초상화 ID·목록·스프라이트·DDS에는 이후 변경이 없다.

## 실행 검증 결과

사용자가 먼저 시작한 HOI4 PID `3460`과 선행 런처는 14시 34분 재조회에서 종료 상태였다. 이 작업에서 해당 세션을 조작한 기록은 없다. 종료 후 로그 20개와 설정·런처 연결 기준선은 `baseline-runtime/`에 보존했다. 이후 작업 소유 시험 PID `2124`를 `-debug`로 실행했다.

실제 관측 범위는 원래 HOK → 애니 서브모드 조합의 1936년 한국이다. 게임을 완전히 재시작해 변경된 파일을 읽었고, 콘솔 효과 없이 UI의 정상 모집과 자연 정치력 수입을 사용했다.

| 관측 | 결과와 증거 |
|---|---|
| 새 게임·고정 과학자 | 정상 진입. 황부길·조경연·도상록·김용관의 기존 애니 초상화 4개 표시. `runtime/screenshots/anime-initial-four-scientists.png` |
| 첫 정상 모집 | 1936.02.18.13, 정치력 107 → 7. `Chae-won Hwang`의 `female_04` 영입·명단 표시. `runtime/screenshots/anime-normal-female-hired.png` |
| 두 번째 정상 모집 | 1936.04.08.22, 정치력 115 → 15. `Shinwoo Choe`의 `male_03` 영입·명단 표시. 여성 표본과 함께 표시된 `runtime/screenshots/anime-normal-hired-pair-clear.png` |
| 모집 후보 | 위 두 자산과 `Yeojin Choe`의 `female_03` 표시. `runtime/screenshots/anime-normal-hire-one.png`, `anime-normal-pool-two.png`는 영입 완료 화면이 아닌 후보 화면 |
| 추가 정상 모집·날짜 진행 | 재시작한 PID `21128`에서 1936.05.17.17 정치력 101로 `Yoon-Gi Gang`의 `male_03`를 100 정치력에 영입. 05.26.23까지 진행한 후 여성 표본과 명단 6명 확인. `runtime/screenshots/anime-second-male-after-date-progress.png` |
| 날짜 진행 후 임시 저장의 같은 프로세스 UI 재로드 | `Chae-won Hwang`과 `Yoon-Gi Gang`의 이름·각 전용 초상화, 명단 6명 유지. `runtime/screenshots/anime-ticked-pair-after-reload.png`. 아래 저장 제한을 함께 적용 |

남녀 전용 풀을 실제로 선택해 표시한 것은 `CONFIRMED`다. 8개 전부의 엔진 선택이나 확률 분포를 확인한 것은 아니다. 고정 인물 네 명과 신규 그림이 같은 명단에서 공존함도 확인했다. 기존 육군·해군은 소스 바이트 보존까지 확인했으며 해당 UI 회귀 시험은 하지 않았다.

### 저장·재로드의 서로 다른 결과

게임은 두 번 모두 일반 파일명으로 저장 완료하지 못하고 `_temp.hoi4`만 남겼다. `error.log`에는 `continue_game.temp → continue_game.json`과 해당 저장의 `_temp.hoi4 → .hoi4` rename 오류 `errno 2`가 기록됐다. 실제 사용자 데이터의 게임 생성 원본을 수정·이름 변경하지 않고, 외부 사본을 복사해 해시를 대조했다. 게임 UI는 이 임시 저장을 인식하여 불러왔다.

| 게임 생성 원본 이름 (`save games/` 아래) | 외부 증거 사본 | 크기·SHA-256 | 실제 결과 |
|---|---|---|---|
| `KOR_1936_04_08_22_temp.hoi4` | `runtime/saves/anime-normal-pair-temp.hoi4` | 47,095,888 bytes, `B10BB2FBD608E152FA19FDD5541A798718472367593345B22F318CFAF8FA53CC` | 일시정지 상태에서 남성 모집 직후 저장. 같은 프로세스 재로드와 완전 종료 후 PID `21128`의 재로드 모두 고정 4명·여성 표본은 보였지만 `Shinwoo Choe`가 명단에 보이지 않음 |
| `KOR_1936_05_26_23_temp.hoi4` | `runtime/saves/anime-ticked-pair-temp.hoi4` | 47,058,356 bytes, `38B5FD3F3F419F414410DB2BEC41F1808EA863A193EBA70FC85B594A1DBDF52A` | 추가 남성 모집 후 9일 진행한 저장. 같은 프로세스 재로드에서 여성·추가 남성 표본의 이름·그림과 명단 6명 유지 |

첫 저장의 남성 미표시는 `UNRESOLVED`, 원인은 `UNPROVEN`이다. 두 번째 결과는 해당 임시 저장과 같은 프로세스 UI 재로드 조건에서 확인된 남녀 표본의 보존이다. 시간 진행이 첫 현상의 원인을 입증하거나 모든 저장 문제를 해결했다는 뜻은 아니다. 두 번째 저장의 완전 재시작 재로드, 정상 파일명으로의 저장 완료, 과거 저장 호환성은 검증하지 않았다. 두 사본은 `HOI4bin5` 형식이며 텍스트 저장 분석 helper `validation/inspect_scientist_portraits.py`는 준비만 하고 실행하지 않았다.

첫 재로드 화면 `anime-normal-pair-after-reload.png`는 예상 결과를 붙인 파일명이며 실제로는 여성만 보이는 화면이다. 두 번째 재로드 중간 화면의 `anime-ticked-save-reload-female-preserved-male-not-listed.png`도 예상 이름과 실제 표시가 다르므로 판정에는 위 표의 결과와 `anime-ticked-pair-after-reload.png`를 사용한다.

시험 저장의 텍스트 분석을 위해 `settings.txt`의 `save_as_binary` 값을 바꾸려던 쓰기는 AVG의 문서 보호에 차단됐다. 사용자 화면과 파일 쓰기 오류가 일치했고, 이후 실제 파일과 변경 시도 전 사본 `runtime/settings.before-root.txt`의 SHA-256은 `DE97534FED2150477EE0B9144888B0794FC70379FE0A780C1E1C523F5B4F3088`로 동일했다. `save_as_binary=yes`를 유지했다. 보안 설정이나 앱 허용을 변경하지 않았고, 이후 검증은 게임 자체의 UI와 저장 기능을 사용했다. AVG의 설정 쓰기 차단과 게임 저장 rename 오류의 공통 원인은 입증되지 않았다.

키 입력 도구의 `grave`·`Escape`가 시험 게임에서 화면 변화를 만들지 못했다. 이 현상은 두 컴퓨터 사용 경로에서 확인했고, 마우스로 여는 메뉴·연구·과학자 명단은 동작했다. 사용자는 이후 마우스 검증으로 진행하도록 지시했다. `runtime/console/`에 준비한 성별 직접 생성·cosmetic tag 진단은 모두 미실행이다. 정상 모집 관측을 이 진단의 실행 증거로 대신하지 않는다.

### 로그와 시험 세션 종료

첫 세션 종료 후 `runtime/anime-first-session-final/`에 로그 34개 2,137,258 bytes와 설정·descriptor 사본을 보존했다. 로그 34개 모두 SHA-256 일치를 확인했다. 이 세션의 `assessment.json`에서 기준선 `baseline-runtime/post-preexisting-session/error.log` 9행과 최종 14행을 비교했다. 시각·게임 날짜 접두부만 제거한 신규 고유 메시지는 현지화 충돌, `map/buildings.txt:66858` 인수 수 오류, continue_game rename, 이번 저장 rename의 4종이며 제거는 0종이다. 기준선의 기존 `random.log` rename 오류는 새 저장 대상 오류의 동일 원인을 증명하지 않는다. 초상화·과학자 관련 오류 메시지는 0행이었으며 신규 현지화·지도 오류와 이번 변경의 인과 관계는 입증하지 않았다.

PID `2124`와 재시작 시험 PID `21128`을 각각 게임 UI의 정상 종료로 닫았다. 첫 종료 후 15:12:32, 최종 종료 후 15:24:42(KST) 프로세스 조회에서 게임·런처·dowser가 없음을 확인했다. Steam에 남은 실행 중 표시는 정상 Stop·확인으로 정리하고 두 번 모두 Play 버튼 복구를 관측했다. 최종 화면 증거는 `runtime/screenshots/steam-play-after-final-exit.png`다. 원래 열려 있던 Steam과 다른 사용자 앱은 유지했다.

두 번째 세션은 `runtime/anime-second-session-final/`에 로그 34개 1,466,211 bytes를 보존하고 34개 해시 일치를 확인했다. 해당 `assessment.json`의 최종 오류도 14행, 기준선 대비 신규 고유 메시지 4종·제거 0종, 초상화·과학자 오류 0행이다. 첫 세션과 비교하면 저장 오류의 대상 파일명이 두 번째 저장으로 바뀐 것이며 오류가 해결된 것이 아니다.

두 세션 모두 종료 후 `settings.txt`는 변경 시도 전 root 사본과 동일했고, 모드 선택·DLC·게임 설정·런처 연결도 기준선과 일치했다. 초기 agent 기준선에만 있던 `graceful_exit=no`는 사용자가 실행 중일 때 수집한 엔진 생명주기 표시이며 root의 실행 전 기준선과 구별했다. `runtime/anime-second-session-final/save-inventory-assessment.json`에서 저장 목록은 시작 83개 → 종료 85개였고 추가는 위 시험 임시 저장 2개뿐이다. 기존 83개는 이름·크기·수정시각(ms)이 모두 동일하고 삭제는 없었다. 사전 내용 해시가 없으므로 기존 저장 전체의 바이트 동일성까지 검증했다고 주장하지 않는다.

## 인계 범위와 남은 확인

구현한 동작은 한국에서 신규 모집하는 과학자가 한국 전용 남녀 목록을 선택하는 것이다. 공용 아시아 풀, 기존 고정 인물, 육군·해군 목록 및 원작자 자산은 유지했다. 애니 서브모드에 새 애니 그림을 추가하지 않았으며 현재 조합은 본체의 신규 사실적 그림을 함께 사용한다.

| 항목 | 상태 |
|---|---|
| 새 DDS 8개·GFX·KOR 목록 통합 | 완료, 정적·자산 대조 통과 |
| HOK+애니 정상 모집의 남녀 표본·고정 과학자 공존 | 확인 |
| 날짜 진행 후 임시 저장의 같은 프로세스 남녀 표본 보존 | 확인, 일반 저장 완료 및 전체 저장 호환성으로 확대하지 않음 |
| 최초 즉시 저장의 남성 미표시·두 저장의 rename 오류 | 미해결, 원인 미확정 |
| 13 cosmetic tag 상속·실제 분기 진행 | 미검증, 소스 후보 대장만 작성 |
| 본체 단독·8개 전부의 런타임 선택·과거 저장·멀티플레이 | 미검증 |
| 육군·해군 UI 및 다른 국가의 실제 모집 회귀 | 미검증, 관련 소스·공용 자산 보존만 확인 |

모든 helper·로그 사본·미리보기·중간물은 위 외부 시험 경로에 있다. 게임이 생성한 임시 저장 원본은 실제 사용자 데이터에 남겨 두고 외부 사본 위치를 함께 기록했다. 저장소의 기존 시험 산출물은 조사 범위에서 발견하지 않았고 별도 정리는 하지 않았다. Git commit·push·패키징·외부 게시는 수행하지 않았다.
