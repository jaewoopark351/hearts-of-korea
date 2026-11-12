# 2026-11-12 한국 신규 첩보원 초상화 구현

이 문서는 최초 구현 당시 그림과 시험 결과를 보존한다. 같은 날 후속 배경·복장 편집으로 DDS 8장이 갱신됐으며, 현재 그림의 출처·해시·표시 확인은 [배경·복장 수정 기록](2026-11-12-korean-operative-outfit-background.md)을 따른다.

2026-11-12(KST). [전용 초상화 계획](../HOK_KOREAN_OPERATIVE_PORTRAIT_PLAN.md)에 따라 한국을 초상화 기준 국가로 삼는 신규 무작위 첩보원에게 남성 4장·여성 4장의 전용 그림을 연결했다. 본체에 어울리는 사실적 화풍의 가상 성인 8명이며, 이번 작업은 신규 초상화 선택을 바꾸는 후속 개발이다. 기존 인물·이름·호출부호·특성·성별 확률·비용·슬롯 규칙은 변경하지 않았다.

현재 상태는 **구현 완료 / 정상 남녀 모집·채용과 임시 저장 재로드 확인 / 13개 cosmetic tag의 강제 생성 표본 확인**이다. 남녀 8개 그림 모두 게임 후보 화면에서 확인했고 애니 조합에서 저장된 남녀 표시도 확인했다. 일반 저장 파일의 이름 변경 실패, 자연스러운 정치 경로·외국 현지 모집의 미검증 범위는 아래에 구분한다.

## 기준 소스와 실행 조건

- 브랜치: `feat/korean-focus-expansion-ai`
- 시작 HEAD: `f1282d701bc47e47c119ca31faa6082e9e6ed1e6`
- 구현 시작 전 변경: `AGENTS.md` 수정과 미추적 `docs/HOK_KOREAN_OPERATIVE_PORTRAIT_PLAN.md`. 선행 문서 작업을 보존했다.
- 작업 소스: `C:/hoi/hearts_of_korea/`. 바닐라와 Workshop 설치본은 읽기 전용 근거다.
- 설치본: HOI4 `Operation Postern v1.19.4.2.2da5`, Steam build `26409260`. 설치 메타데이터의 괄호 값 `0bdb`, 선행 RT56 실행 기록의 `de4b`, 이번 본체 메뉴 체크섬 `04d2`는 서로 다른 출처다.
- 실제 사용자 데이터: `C:/Users/jaewo/OneDrive/문서/Paradox Interactive/Hearts of Iron IV/`.
- 본체 시험: `Korean Language` → 본체 순서, DLC 36개와 La Resistance 활성, `l_korean`, 1280×720 창 모드, GUI scale 1.0. 최초 정상 모집은 PID `15644`, 전체 재시작·재로드는 PID `20716`에서 확인했다.

시작 당시 `dlc_load.json`은 RT56 호환판 → RT56 한국어 번역 → RT56 → 국뽕팩을 선택했다. 해당 설정·로그·메타데이터는 아래 `baseline-runtime/`에 보존했고 이번 본체 실행 증거로 사용하지 않는다. 시험 설정 `runtime/main-test-dlc_load.json`은 `mod/ugc_2743487021.mod`와 `mod/hearts of korea.mod`를 기록한다. 전자는 Workshop `2743487021`의 `Korean Language`, 후자는 이 저장소를 가리킨다. RT56 호환판·국뽕팩으로의 이식은 수행하지 않았다.

## 변경한 연결과 보존 대상

| 대상 | 적용 내용과 근거 |
|---|---|
| [한국 초상화 목록](../../portraits/00_portraits_KOR.txt) 41행 | 기존 `KOR` 블록에 `operative.female`·`operative.male`을 추가. 성별별 `01`~`04`만 등록 |
| [전용 GFX](../../interface/HOK_KOR_operative_portraits.gfx) | `GFX_HOK_KOR_operative_{female,male}_NN` 8개를 프로젝트 DDS에 연결 |
| `gfx/leaders/operatives/HOK_KOR/` | `portrait_HOK_KOR_operative_{female,male}_01`~`04.dds`, 총 8개 |
| [국가 초기화](<../../history/countries/KOR - Korea.txt>) 249~267행 | La Resistance 조건, 윤봉길·이봉창의 고정 GFX·국적·특성·모집 설정 유지 |
| [고정 첩보원 GFX](../../interface/leader_portraits_HoK.gfx) | 윤봉길·이봉창의 기존 DDS 연결 유지 |
| 기존 육군·해군·과학자 목록 | 첩보원 추가 부분을 제외한 한국 목록의 바이트가 기준선과 동일 |

국가별 역할 목록의 구문 근거는 설치본 `dlc/dlc028_la_resistance/portraits/027_lar_portraits.txt` 275행의 `RAJ.operative`다. 아시아 공용 풀과 타국 목록을 수정하지 않았다. 두 production 텍스트에 `#20261112_kpopmodder:` 기여 주석을 붙였다. 기존 한국 목록의 CRLF·BOM 없음·마지막 줄바꿈 없음은 보존했고 새 GFX는 CRLF·BOM 없음이다. 기존 과학자 GFX의 LF 형식은 변경하지 않았다.

애니 서브모드는 `gfx/leaders/KOR`를 `replace_path`로 선언한다. 이번 신규 경로는 그 밖에 있으며 본체의 사실적 DDS를 공급한다. 별도 애니 그림이나 서브모드 변경은 추가하지 않았다. 아래 애니 조합 실행에서 저장된 남녀 두 그림의 표시를 확인했다.

## 그림 제작과 출처

[자산 manifest](../data/HOK_KOREAN_OPERATIVE_PORTRAIT_ASSET_MANIFEST.json)에 8개 각각의 생성 프롬프트, 원본·보존본 경로와 해시, 가공 방식, 스프라이트, 최종 경로와 해시를 기록했다. 생성 도구는 `image_gen.imagegen`, 노출된 모델명은 없음, 참조 이미지는 없음이다. AI 생성 그림으로 기록하며 외부 공개 자산이나 기존 작가 작품의 재사용으로 표시하지 않는다.

선택한 PNG 원본은 아래 외부 작업 경로의 `art/generated/`에 보존했다. 도구 원본은 `C:/Users/jaewo/.codex/generated_images/01a1cf1e-a773-7480-b988-8c8652f01d70/` 아래에 있으며, 원본에서 외부 보존본으로의 개별 경로·SHA-256 대응은 `art/generation-provenance.json`과 자산 manifest를 따른다.

설치된 남녀 아시아 첩보원 DDS 헤더를 규격 근거로 읽었다. 선택 PNG를 중앙 종횡비 crop과 bicubic 축소로 156×210에 맞추고, 알파가 있는 uncompressed BGRA32 DDS로 변환했다. 각 파일은 131,168바이트이며 mipmap 헤더 값은 0이다. 변환본은 `art/final-dds/`에 보존한 뒤 저장소 런타임 경로로 복사했다. 규격 근거는 `art/reference/operative-dds-header-evidence.json`, 변환별 기록은 `art/final-dds/conversion-manifest.json`이다.

원본 크기의 정적 검수는 `art/final-dds/native-contact-sheet.png`를 기준으로 했다. `art/native-preview-review.json`에는 머리·머리카락의 캔버스 내 배치, 작은 크기에서의 얼굴 식별, 시대에 맞는 민간 복장, 어두운 배경의 알파 경계, 불필요한 글자·프레임·다른 인물 부재를 확인한 결과가 있다. 이 검수는 게임 화면 확인과 구분한다.

## 정적 확인 결과

외부 증거 기준 디렉터리는 `C:/hoi/test/hok-operative-portraits-20261112-01/`다. 아래 경로는 그 디렉터리 기준이다.

| 기록 | 실제 확인과 결과 |
|---|---|
| `integration/baseline.json`, `integration/source-before/` | 관련 production 원문을 바이트 복사하고 SHA-256 대조. 시작 브랜치·HEAD·선행 변경 기록 |
| `integration/static-source-integration.json` | 최초 코드 연결 단계 23 PASS, 0 FAIL. 이때 DDS는 아직 0/8이며 최종 자산 확인과 구분 |
| `validation/operative-asset-manifest-validation.json` | 생성·보존 PNG, 변환본, 저장소 DDS, 목록·GFX 연결 8개 PASS, 0 FAIL |
| `integration/final-source-integration.json` | 자산 배치 뒤 36 PASS, 0 FAIL. 8/8 경로·대소문자·해시·DDS 헤더, ID·목록 순서·괄호·따옴표·기여 주석 확인 |
| 같은 최종 기록 | 본체의 정의 8개, 바닐라/DLC·필수 Korean Language·애니 참고본·현 RT56 번역에서 새 ID 충돌 0. 변경 런타임 파일은 목록·GFX 2개와 DDS 8개 |
| 같은 최종 기록 | 고정 첩보원 초기화·GFX, 과학자 GFX, descriptor의 기준선 해시 보존. `git diff --check` 통과 |
| `integration/final-source-coverage-ledger.json` | cosmetic tag 13개/설정 지점 18곳의 호출자·효과 경로, 고정 인물 2명, 외국 현지 모집 8곳 기록 |

이 결과는 소스 참조와 자산 파일의 연결을 입증한다. 엔진 등록·실제 그림 선택·저장 동작을 대신하지 않는다. 원본과 helper·변환 중간물·화면 증거는 외부 작업 경로에 두었다.

## 본체 실행에서 관측한 범위

다음은 전체 프로세스 시작 뒤 본체 조합에서 정상 UI로 진행한 관측이다. 강제 생성 효과는 실행하지 않았다. 화면 경로는 외부 작업 경로의 `runtime/screenshots/` 기준이다.

| 조건과 관측 | 화면 증거 |
|---|---|
| 메인 메뉴 체크섬 `04d2`, 한국 1936년 진입 | `main-menu-04d2.png`, `main-korea-1936-setup.png` |
| 정보기관을 정상 UI에서 창설, 30일 진행 표시 확인 | `main-agency-normal-start.png` |
| 1936-03-16 01:00 모집 후보에 고정 윤봉길·이봉창과 신규 `Hyeja Hong`(여성 04), `Jaehyun Hwang`(남성 04), `Dowon Yun`(남성 02)이 함께 표시 | `main-candidates-fixed-and-new.png` |
| `Hyeja Hong`을 정상 채용, 여성 04 그림 표시 | `main-normal-female04-hyeja-hong-hired.png` |
| 염동진 고문을 정상 채용해 슬롯 2 확보 후, 1936-05-03 06:00 후보 `Sungjin Yun`(남성 02)을 정상 채용 | `main-second-candidates-male02-sungjin-yun.png`, `main-normal-female04-male02-hired.png` |
| 1936-05-12 02:00까지 진행, 여성 04·남성 02 명단과 그림 유지 | `main-pair-before-save-19360512.png` |
| 저장 후 전체 게임 프로세스 재시작, 같은 날짜의 명단과 두 그림 복원 | `main-restart-menu-04d2.png`, `main-restart-selected-temp-save.png`, `main-restart-reloaded-pair-19360512.png` |

남성 정상 채용을 확인하기 위해 염동진을 고문 UI에서 150 정치력으로 채용했다. 정치력은 165→15로 변했고 슬롯 2를 확보한 뒤 다음 모집의 30일 진행을 기다렸다. 이 고문과 날짜 진행은 시험 저장 안에서만 발생했다.

저장 UI에서 기존 일반·임시 파일이 모두 없는 새 이름 `KOR_1936_05_12_02`를 확인한 뒤 저장했다. 게임은 47,304,967바이트의 `KOR_1936_05_12_02_temp.hoi4`를 만들었지만 일반 이름으로 바꾸는 단계에서 errno 2를 기록했다. `continue_game.temp` 이름 변경도 실패했으며 선행 과학자 시험에 같은 종류의 관측이 있다. 원인은 확정하지 않았고 이번 초상화 수정으로 귀속하거나 수정하지 않았다. 일반 이름의 저장 완료를 통과로 기록하지 않는다.

게임이 만든 임시 저장을 외부 `runtime/saves/main-normal-pair-temp.hoi4`에 복사했다. SHA-256은 `D09A5A869E970893FE566A545AC5B14BAF149B7BFB61E5258C8C93665F5F9BC2`다. PID `15644` 종료와 Steam의 플레이 복귀를 확인한 뒤 PID `20716`을 새로 시작했다. 게임의 로컬 불러오기 목록에서 해당 임시 저장을 선택해 1936-05-12 02:00의 두 첩보원과 그림을 복원했다. 따라서 **게임 생성 임시 저장의 전체 재시작 재로드는 확인**, **일반 저장 파일의 이름 변경 완료는 실패**로 구분한다. 재시작 뒤 원본 임시 저장의 해시는 동일했다.

Space·grave 입력으로 기대한 일시정지·콘솔 반응이 나타나지 않았고 마우스 UI는 작동했다. `main-console-key-no-console.png`에 화면을 보존했다. 강제 효과·직접 성별 생성·cosmetic tag 진단을 실행한 증거로 취급하지 않는다.

## 애니 조합 실행

본체 두 세션을 종료한 뒤 `Korean Language` → 본체 → `mod/Hearts of Korea anime.mod` 조합으로 PID `27200`을 시작했다. `runtime/anime-test-dlc_load.json`과 `runtime/anime-process.json`에 구성과 프로세스를 기록했다. 메뉴 체크섬은 `04d2`였다.

위 본체 임시 저장을 로드해 1936-05-12 02:00의 여성 04·남성 02가 동일하게 표시되는 것을 확인했다. 지도자와 고문은 애니 그림으로 표시되어 해당 서브모드의 적용도 화면에서 확인했다. 증거는 `anime-menu-04d2.png`, `anime-selected-main-pair-save.png`, `anime-reloaded-female04-male02.png`, `anime-leader-and-operative-pair.png`다. 이 세션에서는 날짜 진행이나 새 저장을 하지 않았다. 별도 애니 변형의 제작·선택이나 애니 조합의 신규 정상 모집을 통과로 확대하지 않는다.

## 분기와 남은 검증

| 항목 | 현재 판정과 남은 확인 |
|---|---|
| 한국 신규 남녀 풀 | 여성 04·남성 02 정상 모집·채용, 날짜 진행, 임시 저장 전체 재시작 재로드 확인 |
| 고정 윤봉길·이봉창 | 기존 정의·GFX 해시 보존, 본체 후보 목록에서 공존 확인. 전체 채용·이후 동작의 보증은 아님 |
| 외국 현지 모집 8곳 | `nationalities`·`portrait_tag_override = FROM.OWNER` 의도적 유지. JAP·RAJ override 남녀 대조 후보가 한국 전용 그림을 사용하지 않음. 실제 현지 모집 결정의 비용·대상 scope·정상 완료는 미검증 |
| cosmetic tag 13개 | 각 태그 적용 블록에서 남녀 1명씩 강제 생성한 26명 모두 한국 전용 그림 표시. 실제 정치·형성국·종속국 경로의 자연 진행은 미검증 |
| 아시아 공용·타국·육군·해군·과학자 | 관련 소스 보존 확인. 외국 override 대조 4명 관측. 육군·해군·과학자 신규 UI 회귀 시험은 이번에 수행하지 않음 |
| 8개 전부의 실제 선택 | 진단 후보 UI에서 남성 01~04·여성 01~04 전부 표시 확인. 전부의 정상 채용을 뜻하지 않음 |
| 애니 조합 | 본체 사실적 그림 공유. 전체 프로세스 시작 뒤 기존 시험 저장의 여성 04·남성 02 표시 확인. 별도 애니 변형·애니 조합의 신규 정상 모집은 미검증 |
| 저장·재로드와 기존 저장 | 일반 저장 이름 변경 errno 2 실패. 게임 생성 임시 저장은 전체 재시작 재로드로 명단·그림 보존 확인. 구현 전 저장 호환·장기 진행·멀티플레이는 미검증 |
| 실행 로그·설정·종료 | 아래 최종 기록을 따름. 본체·애니·진단을 서로 다른 실행 증거로 구분 |

cosmetic 후보는 정치·형성국 8개와 종속국 5개다. 종속국의 `on_puppet`·`on_release_as_puppet`는 설치본 `common/on_actions/00_on_actions.txt` 1554·1592행의 ROOT/FROM 설명을 scope 근거로 사용했다. 각 호출 위치와 Hwan 조건 분기는 외부 소스 대장을 따른다. 상속을 미리 확정해 태그별 목록을 복제하지 않았다.

## 격리한 태그·외국 기준 진단

정상 모집과 별도로 외부 작업 경로의 `diagnostic/mod/`에 시험 모드를 만들었다. 본체 파일에는 진단 코드를 넣지 않았다. 설치본의 `on_startup`·`create_operative_leader`·`gender`·`set_cosmetic_tag` 구문을 사용하고, 1936년 첫날·La Resistance·사람이 조작하는 한국·일회성 표식 조건으로 한정했다. 준비 소스·기대값은 `diagnostic/vanilla-references.json`, `verification.json`, `intent-and-name-map.json`에 보존했다.

첫 PID `21236`에서는 `enabled_mods`의 외부 절대 `.mod` 경로가 실제 활성 모드에 나타나지 않아 새 게임에 진입하지 않고 종료했다. 그 시도의 로그·설정은 `runtime/diagnostic-absolute-attempt-final/`에 따로 보존했다. 이후 원래 존재하지 않던 사용자 데이터의 `mod/HOK_operative_probe_20261112_01.mod`를 외부 시험 소스를 가리키는 임시 런처 설정으로 등록했다. 원본·사본·처리 조건은 `runtime/diagnostic-launcher-pointer.json`에 기록했다. 실제 시험 코드는 계속 외부 작업 경로에 있었다.

PID `22476`, 메뉴 체크섬 `1aa6`에서 진단 모드·Korean Language·본체의 활성 로그를 확인했다. 1936-01-01 12:00에 START 1회, BEGIN/END 각 16회, COMPLETE 1회가 남았다. 로그 문자열에서 소스의 `[HOK][OPDIAG]` 부분은 사라져 그 접두사를 찾는 초기 정규식은 false negative였다. 원문과 유효한 관측은 `diagnostic/runtime/callback-marker-observation.json`에 구분했다.

기준 한국 남녀 2명, 13개 cosmetic tag의 남녀 26명, `portrait_tag_override = JAP`·`RAJ` 남녀 4명을 만들었다. 강제 GFX는 지정하지 않았으며 국적은 32명 모두 `KOR`로 통제해 초상화 기준 국가의 효과를 분리했다. 각 태그 블록 뒤에는 기본 한국 cosmetic 상태로 복귀시켰다. 이것은 정치 경로 자체나 외국 현지 모집 결정을 정상 완료한 시험이 아니다.

1936-01-02 16:00에 새 이름 `KOR_1936_01_02_16`으로 저장을 시도했고 같은 이름 변경 실패로 임시 파일이 남았다. 외부 사본 `runtime/saves/diagnostic-32-candidates-temp.hoi4`는 46,581,225바이트, SHA-256 `066EEE4F240ACDE0E28B75EF33B2BAF49D19EC92E9635A05CB4193E9EE281113`이다. 바이너리 저장에 기대 이름 32개와 새 GFX 8개 문자열이 있으나 이 검사만으로 개별 매핑을 확정하지 않았다. 텍스트 저장 설정 변경은 OS의 접근 거부로 실패해 `save_as_binary=yes`를 유지했다. 보안 설정이나 ACL을 변경하지 않았다.

기관 창설·모집 대기 뒤 1936-03-14 18:00에 후보 목록을 스크롤해 32명 전부의 이름과 얼굴을 직접 대조했다. `runtime/screenshots/diagnostic-candidates-01.png`~`11.png`와 `diagnostic/runtime/ui-portrait-observation.json`에 관측자·이름·그림·화면 해시를 기록했다. 한국 풀 28명은 모두 지정 성별의 새 그림이며 8종이 전부 나타났다. JAP·RAJ 대조 4명은 한국 전용 그림과 다른 외국 그림을 표시했다. 외국 그림의 정확한 GFX 인덱스는 해독하지 않았다. 진단 후보는 채용하지 않았다.

| 생성 당시 조건 | 남성 / 여성의 새 그림 번호 |
|---|---|
| 기본 KOR | 03 / 04 |
| `KOR_Balhae` | 01 / 03 |
| `KOR_CHI` | 03 / 02 |
| `KOR_Goguryeo` | 01 / 02 |
| `KOR_Hwan` | 01 / 01 |
| `KOR_Hwan_neutrality` | 04 / 03 |
| `KOR_JAP` | 04 / 01 |
| `KOR_PRC` | 02 / 03 |
| `KOR_PRK_communism` | 02 / 02 |
| `KOR_SOV_communism` | 03 / 02 |
| `KOR_democratic` | 04 / 04 |
| `KOR_greater_Hwan_neutrality` | 04 / 02 |
| `KOR_neutrality` | 01 / 02 |
| `KOR_reichskommissariat_fascism` | 03 / 04 |

## 최종 로그와 작업 상태

| 실행 증거 | 관측과 오류 판정 |
|---|---|
| `baseline-runtime/` | 작업 전 RT56 조합. 오류 684행·고유 643개. 다른 구성의 기록이므로 본체와 단순 증감으로 회귀를 판정하지 않음 |
| `runtime/main-first-session-final/` | 정상 모집·저장 시도, 오류 13행·고유 12개. 초상화·첩보원·과학자 관련 메시지 0개 |
| `runtime/main-restart-session-final/` | 같은 본체 조합에서 임시 저장 재로드. 오류 11행·고유 10개, 첫 본체 대비 새 메시지 0종. 저장을 시도하지 않아 continue_game·해당 저장 rename 2종은 없음 |
| `runtime/anime-session-final/` | 같은 저장의 애니 조합 재로드. 오류 11행·고유 10개, 직전 본체 대비 추가·제거 0종. 초상화 관련 0개. `source-fallback.json`에 본체 DDS 8개 존재·애니 대응 0개·replace_path 6개 밖임을 확인 |
| `runtime/diagnostic-registered-session-final/` | 태그·외국 기준 진단. 오류 13행·고유 12개, 초상화·첩보원·과학자 관련 0개. 첫 본체 대비 메시지 추가 1종·제거 1종은 저장 rename의 파일 경로 차이. START/COMPLETE 각 1회·BEGIN/END 각 16회 및 00~15 각 1회를 원문으로 확인 |

일반 실행에는 등록된 다른 모드 descriptor의 버전·thumbnail 경고, 현지화 충돌, `map/buildings.txt` 66858행 문제가 남아 있다. 초상화 추가와 직접 연결하는 근거는 없으며 이 작업에서 수정하지 않았다. 조용한 초상화 로그를 전체 모드의 무오류 판정으로 사용하지 않는다.

최종 설정·프로세스 기록은 `runtime/pre-restoration/restoration.json`이다. 복원 전 네 파일을 같은 외부 디렉터리에 보존했다. `dlc_load.json`은 원래 RT56 조합의 바이트와 SHA-256 `A035CE0F00E763F597E523D2F7298B1FE1DF4B643A3907BAB7F24506A27F79C9`로 복원됐다. `pdx_settings.txt`와 `gameplaysettings.txt`는 원본 기준선과 이미 같았다. 임시 런처 설정은 원래 부재와 시험 사본 해시를 확인한 뒤 해당 파일 하나만 제거했으며 부재를 재확인했다.

`settings.txt`의 원본 복원은 일반 `Copy-Item`에서도 `UnauthorizedAccessException`으로 거부됐다. 현재 SHA-256 `DE97534FED2150477EE0B9144888B0794FC70379FE0A780C1E1C523F5B4F3088`은 진단 전 사본과 동일하며, 작업 전 기준선 `15FD1454B060B0A781C8450FB922DF6D21BCC1DD03B9F2C90F2B354D04412C23`와 다른 내용은 게임이 갱신한 로딩 화면 배경 목록·가중치 두 줄이다. `save_as_binary=yes`를 포함한 시험 설정 변경은 적용되지 않았다. ACL·보안 설정·속성 변경이나 우회 복원은 수행하지 않았다. 원본 설정 사본은 `baseline-runtime/userdata/settings.txt`에 보존되어 있다. 따라서 **원래 모드 선택과 다른 설정 2개는 기준선 일치 / settings.txt의 게임 자동 기록 두 줄은 복원 미완료**로 보고한다.

시험 소유 PID `15644`·`20716`·`27200`·`21236`·`22476`은 전부 종료됐고 HOI4·dowser·Paradox Launcher 잔류 프로세스가 없었다. Steam은 `runtime/screenshots/final-steam-play-restored.png`에서 플레이 버튼 복귀를 확인했다. 기존 Steam과 관련 없는 다른 앱은 종료하지 않았다.

`runtime/final-save-inventory-assessment.json`에서 저장 목록은 작업 전 85개에서 87개가 됐다. 추가된 것은 이번 정상 모집·진단의 임시 저장 두 개뿐이고, 제거된 기존 저장은 없다. 기존 85개의 경로·크기·수정시각 변경은 0개다. 이 비교는 메타데이터 검사이며 기존 저장 전체의 내용 해시 일치를 주장하지 않는다. 최종 독립 읽기 검토에서 DDS 8개와 manifest의 해시·크기, JSON 파싱, 문서 UTF-8·상대 링크와 새 런타임 helper의 저장소 부재를 확인했고 `git diff --check`도 통과했다.

게임 생성 저장 원본은 실제 사용자 데이터에, 증거 사본·helper·진단 모드·로그는 외부 작업 경로에 보존한다. 저장소에 앞서 존재하던 `docs/assets/korean-fascist-mobilization-validation-20260923/` PNG 4개(815,391바이트)는 정리 미완료로 보고하며 이번 범위에서 이동·삭제하지 않았다. Git commit·push·패키징·외부 게시는 수행하지 않았다.
