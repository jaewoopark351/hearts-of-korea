# 한국 신규 모집 과학자 이름 현지화

**현재 상태 — 로마자 표기·확인된 현대 정치인 중복 후보 제외.** 사용자가 21세기 정치인 이름을 시대 배경에 맞지 않는 것으로 지적하여, 앞서 삭제한 `Geunhye`에 더해 아래 후속 기록의 이름 토큰 20개를 제외했다. 현재 입력 수는 남성 56·여성 11·성 14개, 합계 81개다. 로마자 표기를 사용하며, 아래 102개·101개 및 한글 화면 수치는 각각 당시 소스의 이력이다. 이번 제외 후 실제 게임 화면은 다시 확인하지 않았다.

**현재 상태 — 원래 로마자 표기로 복원.** 같은 날 사용자의 후속 요청에 따라 신규 생성용 한국 이름·성 목록을 원래 표기로 되돌렸다. 고정 과학자 네 명의 이름 현지화와 초상화는 유지했다. 아래 한글 표시 성공은 복원 전 소스의 검증 이력이다. 현재 결과는 [로마자 복원 기록](#후속-요청에-따른-로마자-복원)을 따른다.

2026-11-12(KST). 사용자의 이름 localisation 적용 요청에 대한 작업 기록이다. [신규 과학자 초상화 구현](2026-11-12-korean-scientist-portraits.md)과 구분하여 이름 표시만 다룬다. 최초 부분 이름 키 방식은 실제 모집에서 실패했다. 한국 이름 목록에 한글을 직접 제공하도록 교정한 뒤 전체 프로세스 재시작·정상 모집 창에서 남녀 이름과 성의 한글 표시를 확인했다. 정상 채용 후 명단에서도 한글 이름이 유지됐다. **한글 신규 이름 표시 구현과 해당 정상 모집 검증을 완료**했으며 아래 미검증 범위는 별도로 남긴다.

## 기준과 증거 위치

- 작업 소스: `C:/hoi/hearts_of_korea/`, 브랜치 `feat/korean-focus-expansion-ai`, HEAD `cdc022eee15fbf7404d4cb30cf2d0102d29e550c`.
- 시작 시 `AGENTS.md`, 한국 초상화 목록과 앞선 초상화 작업의 새 문서·GFX·DDS가 미커밋 상태였다. 이 작업의 수정과 구분하여 보존한다.
- 설치본: `Operation Postern v1.19.4.2.2da5`, 앞선 사용자 실행 체크섬 `0a55`, DLC 36개, 언어 `l_korean`.
- 실제 모드 순서: HOK → `Hearts-of-Korea-anime`. 두 launcher `.mod`의 물리 경로는 작업 저장소와 `C:/hoi/Hearts-of-Korea-anime/`다. 바닐라·Workshop 관리본은 읽기 전용이다.
- 실제 사용자 데이터: `C:/Users/jaewo/OneDrive/문서/Paradox Interactive/Hearts of Iron IV/`.
- 새 외부 작업 경로: `C:/hoi/test/hok-scientist-name-localisation-20261112-01/`. 아래 시험 파일·원본 사본·보고서는 이 경로 기준이다.

선행 사용자 게임 PID `6416`은 16:07:19(KST)에 시작됐고 이 작업에서 입력하거나 종료하지 않았다. 실행 중 기준선 `baseline/`에 로그 34개와 설정·descriptor를 포함한 42개 사본을 보존했다. 사용자가 세션을 종료한 뒤 16:17:24.907(KST) 프로세스 0개를 재확인하고 `baseline/post-user-exit/`에 로그·설정·launcher 사본 40개를 추가 보존했다. 두 묶음의 사본은 각각 공유 읽기 snapshot과 SHA-256 대조를 완료했다.

시험 전 설정 사본은 `runtime/settings.before-root.txt`, SHA-256은 `DE97534FED2150477EE0B9144888B0794FC70379FE0A780C1E1C523F5B4F3088`이다. 초기 실행 중 설정과 종료 후 설정의 차이는 엔진 생명주기 표시 `graceful_exit=no` 제거뿐이었다. 게임 생성 원본은 사용자 데이터에 유지하고 외부 경로에는 증거 사본만 둔다.

## 연결 방식과 표시 영향

현재 [한국 이름 풀](../../common/names/00_names.txt)의 원문은 남성 71개, 여성 17개, 성 14개, 총 102개 토큰이다. `Hee-Seok`과 `Heeseok`처럼 철자가 다른 같은 발음의 항목도 각각 유지한다. 이름과 성을 합치는 순서는 엔진의 기존 동작을 따른다.

최초 구현은 `HOK_KOR_RANDOM_NAME_<원문>` 키 102개와 두 채널의 대응 현지화 파일을 연결했다. 그러나 새 프로세스의 정상 모집 창에서 네 후보 모두 부분 이름 키를 그대로 표시했다. 키·값 파일의 구조가 맞아도 이 소비 경로에서 이름 조각을 각각 번역하지 않는다는 반증이다. 이 구성을 최종 구현으로 남기지 않는다.

최종 방식은 `KOR` 목록의 이름과 성에 한글 문자열을 직접 제공하는 것이다. `Shin-Woo`와 `Shinwoo`는 각각의 목록 자리를 유지하면서 둘 다 `신우`로 표기한다. 엔진의 기존 이름·성 조합 순서를 유지하며 성 우선 배치나 새 이름 생성 효과는 추가하지 않는다. 고정 character ID와 기존 저장의 인물 ID도 이관하지 않는다. 언어별 `.yml` 조각 치환이 아니라 이름 생성 입력의 한글화이므로 다른 언어로 실행해도 이 목록 자체는 한글이다.

| 파일 | 역할 |
|---|---|
| [common/names/00_names.txt](../../common/names/00_names.txt) | `KOR` 블록의 남성 71·여성 17·성 14개 자리를 한글 문자열로 제공 |
| 최초 `localisation/{korean,english}/HOK_KOR_random_names_l_*.yml` | 실제 표시 실패한 미사용 파일. 최종 런타임에서 제외하고 외부 `source-rejected-prefix/`에 보존 |

원문 `Lee`, `Kim`, `Bora`, `Jang`, `Hong`은 다른 14개 국가의 15개 이름 풀 사용처에도 있다. 한국 블록 안에서만 문자열을 바꾸고 전역 원문 키에 번역을 추가하지 않는다. 다른 국가 블록은 유지한다. 조사 목록·행 번호는 `validation/name-token-impact-source-review.json`에 있다.

| 후보·분기 | 처리 | 확인할 범위 |
|---|---|---|
| KOR 남성 71·여성 17·성 14 | 변경 | 원래 목록 자리의 순서·개수·성별을 보존하여 한글 표기 |
| 같은 KOR 이름 풀을 쓰는 일반 무작위 한국 인물 | 의도적 공통 적용 | 과학자 외 인물도 같은 이름 토큰을 선택하면 같은 한글 표기를 사용 |
| 다른 국가의 공유 원문 토큰 5개·사용처 15개 | 의도적 유지 | KOR 외 블록의 바이트와 기존 원문 표기 보존 |
| 황부길·조경연·도상록·김용관과 다른 고정 인물 이름 | 의도적 유지 | 기존 character ID·기존 이름 localisation 보존 |
| 초상화·스프라이트·특성·모집 비용·선택 가중치 | 제외 | 이 작업에서 변경하지 않음 |
| 과거 저장에서 이미 생성된 인물 이름·cosmetic tag·다른 언어와 번역 모드 | 미확인 | 새 게임의 신규 생성과 별도 검증 필요 |

현재 원문·한글 대응과 파일 해시는 [이름 유지관리 manifest](../data/HOK_KOREAN_RANDOM_NAME_LOCALISATION_MANIFEST.json)에 있다. 최초 원문·거부된 부분 키·한글 대응은 외부 `validation/implemented-name-mapping.json`, 최초 분기 대장은 `validation/name-localisation-coverage-ledger-source.json`에 있다. 이들은 첫 구현의 기록이며 최종 `validation/direct-korean-name-mapping.json`과 구분한다. 같은 발음의 로마자 변형은 한글에서 같은 문자열이 된다. 입력 항목은 71·17·14개지만 고유 한글값은 각각 65·10·14개다. 목록 자리 보존을 엔진의 중복 조합 배제·선택 확률까지 동일하다는 증거로 해석하지 않는다.

## 검증 기록

설치된 바닐라의 `common/names/00_names.txt:3369`에는 무작위 이름 `Pablo`가 있고 `localisation/korean/names_l_korean.yml:2`에는 `Pablo: "파블로"`가 있다. 이 존재 대응만으로 한국 과학자 이름 조각의 개별 번역을 추론한 것은 잘못이었다. 실제 실행 반증을 우선한다. 설치된 이름 목록에는 Unicode 원문 이름이 있지만 `$KEY$`·`[...]` 확장 사례는 없었다. `documentation/effects_documentation.md:4458`의 `generate_scientist_character`도 초상화·성별·능력·특성만 설명하고 부분 이름 현지화 옵션을 제공하지 않는다. 확인하지 않은 다른 방식까지 불가능하다고 단정하지 않는다.

첫 시험 PID `23464`는 16:21:39(KST)에 시작한 `-debug` 실행이다. 메인 메뉴 `Operation Postern v1.19.4.2.2da5 (bec7)`를 확인하고 1936년 한국 새 게임에서 일시정지 상태·정치력 2로 모집 창을 열었다. 후보 네 명 모두 `HOK_KOR_RANDOM_NAME_...`를 표시했다. `runtime/screenshots/first-run-raw-name-keys.png`가 UI 실패 증거다. 채용·시간 진행·저장은 하지 않았다.

첫 구현의 정적 검사 36 PASS와 독립 검사 35 PASS는 키·값·인코딩·변경 범위에 한정된다. 실제 UI 실패를 취소하지 않는다. 해당 프로세스를 종료하고 `runtime/run1-failed-prefix/`에 로그 34개를 포함한 사본 40개를 보존했으며 SHA-256 40개가 일치했다. 종료 후 프로세스 0개, 기존 저장 85개의 메타데이터와 설정·모드 선택 불변을 확인했다. 오류 로그는 11행이며 기준선 대비 추가 고유 메시지 두 종은 현지화 충돌과 지도 건물 경고다. 이 이름 변경과의 인과 관계는 입증하지 않았다.

현재 애니 서브모드에는 본체와 같은 상대 경로의 신규 과학자 DDS 8개가 존재하며 16:04(KST) 수정시각과 본체와 다른 해시를 확인했다. 이번 시험의 후보 그림은 해당 애니 변형이 표시됐다. 이 이름 작업에서 자산을 변경하지 않았고, 앞선 초상화 시험의 사실적 그림 관측과 별도 조건이다. `runtime/run1-failed-prefix/portrait-source-metadata.json`에 물리 파일·해시를 기록했다.

한글 표기 초안 작성 중 셸을 경유한 외부 JSON의 한글이 실제 `?`로 손상된 것을 생산 파일 수정 전에 발견했다. UTF-8 원본 `validation/korean-name-token-values.utf8.json`에서 다시 파생했고 102개 값의 문자 코드포인트를 확인했다. 손상 초안과 교정 기록을 외부에 구분 보존했으며 손상된 값을 생산 파일에 반영하지 않았다.

### 최종 직접 표기 소스와 실제 화면

최종 생산 수정은 `common/names/00_names.txt` 한 파일이다. `#20261112_kpopmodder: Display Korean random names directly in the KOR source pool.` 주석과 한국 블록의 102개 토큰 외 바이트를 보존했다. UTF-8 BOM 없음·CRLF·마지막 CRLF, 기존 인용 형태, 빈 callsigns와 타국 블록을 확인했다. 소스 SHA-256은 `f428e6a66553c62b721f68433dd3e49d1463dd3b58890a710d3451d428d8af64`다.

- 직접 표기 정적 검사: 24 PASS, 0 FAIL. `validation/direct-korean-name-source-checks.json`.
- 독립 최종 소스 검사: 27 PASS, 0 FAIL. `validation/independent-direct-korean-name-review.json`.
- 실패한 prefix 소스와 두 `.yml` 파일: 외부 `source-rejected-prefix/` 보존. 두 파일의 명시 경로·해시 확인 후 이동 기록은 `source-rejected-prefix/move-record.json`에 있다. 런타임 저장소에는 미사용 `.yml`을 남기지 않았다.

두 번째 시험 PID `6884`는 16:35:20.725(KST)에 위 해시의 소스로 시작했다. 메인 메뉴 버전은 `Operation Postern v1.19.4.2.2da5`이며 체크섬은 `16ea`다. 최초 화면 판독에서 `1eea`로 잘못 읽은 값을 최종 `system.log:155`와 대조하여 바로잡았고, 화면 파일도 `direct-main-menu-16ea.png`로 이름을 수정했다. 구성은 동일한 HOK → 애니, DLC 36개, `l_korean`이다. 1936년 한국 새 게임에서 다음을 확인했다.

| 관측 | 결과·외부 화면 증거 |
|---|---|
| 메인 메뉴 버전·체크섬 | `runtime/screenshots/direct-main-menu-16ea.png`, 최종 `system.log:155` |
| 고정 과학자 네 명 | 황부길·조경연·도상록·김용관의 기존 이름·그림 표시. `runtime/screenshots/direct-initial-fixed-four.png` |
| 정상 모집 창·1936.01.01.12·정치력 2 | `소라 이`, `경희 최`, `지영 박`, `동준 홍` 표시. 여성·남성 이름 목록 표본과 서로 다른 성이 한글로 표시됐고 내부 키나 로마자 이름은 보이지 않음. `runtime/screenshots/direct-normal-candidates-korean.png` |
| 정상 채용·1936.02.27.10 | 자연 정치력 수입으로 127 확보 후 `소라 이`를 100 정치력에 채용하여 27로 감소. 확인창에도 한글 이름 표시. 채용 후 고정 4명과 신규 1명의 명단에서 이름 유지. `runtime/screenshots/direct-normal-hire-confirmation.png`, `direct-hired-name-and-fixed-scientists.png` |

이 UI 결과는 이름·성의 정상 신규 생성과 채용 후 표시를 확인한 것이다. 이번 실행에서는 저장하거나 재로드하지 않았다. 전체 102개 값의 화면 표본, 모든 선택 확률, 과거 저장의 이름 소급 변경, 다른 언어·cosmetic tag·본체 단독·멀티플레이를 검증한 것은 아니다. 저장·재로드의 이전 초상화 작업 기록도 이번 이름 변경의 증거로 대체하지 않는다.

### 최종 로그·설정·세션 마감

`runtime/run2-direct-korean-final/`에 로그 34개·1,421,285 bytes를 포함한 사본 40개를 보존했고, 공유 읽기 원문과 사본의 SHA-256 40개가 일치했다. `assessment.json`의 오류 로그는 11행이다. 첫 실패 실행과 정규화한 고유 메시지의 추가·제거는 각각 0개였으며 이름 관련 오류는 0행이었다. 초기 사용자 종료 기준선에 비해 추가된 두 고유 메시지는 앞서 구분한 현지화 충돌과 지도 건물 경고이고, 이번 이름 변경의 원인이라는 증거는 없다. 조용한 이름 로그를 UI 검증으로 대신하지 않았다.

시험 소유 PID `6884`를 창의 정상 닫기로 종료했다. 16:41:13(KST) root 조회와 16:43:21.451(KST) 독립 조회에서 HOI4·관련 런처 프로세스가 0개였고, 생산 이름 소스 해시는 실행 시작 시 값과 같았다. `settings.txt`·`pdx_settings.txt`·`gameplaysettings.txt`, `dlc_load.json`, launcher `.mod` 두 개가 종료 후 기준선과 일치했다. 기존 저장 85개의 이름·개수·크기·수정시각은 추가 0·삭제 0·변화 0이었다. 기존 85개 전체의 작업 전 내용 해시를 확보한 것은 아니므로 이를 바이트 단위 보존 시험으로 표현하지 않는다.

Steam에는 게임 프로세스 종료 후에도 실행 중 표시가 남았다. 정상 정지와 확인 뒤에도 중지 중으로 남아, 다른 게임 실행 없음과 다운로드 진행·대기 0개 및 네트워크·디스크 0bps를 확인한 후 Steam 메뉴의 정상 종료를 사용했다. 앱 목록에서 Steam 종료를 확인하고 등록된 Steam 앱을 재시작했다. 새 창 `198380`의 HOI4 라이브러리에서 초록 `플레이` 버튼과 실행 중·중지 중 표시 해제를 직접 관측했다. 사용자 앱은 남겨 두었으며 시험 소유 게임·helper 프로세스의 강제 종료는 하지 않았다.

Steam 최종 관측 도구는 화면 영역 두 개를 반환해 단일 PNG 저장 분기가 실행되지 않았다. 따라서 별도 최종 Steam 파일이 있다고 기록하지 않는다. 외부 `runtime/screenshots/final-steam-play-state.png`는 파일명과 달리 중지 중 화면이므로 복구 증거로 사용하지 않는다. 최종 Steam 복구는 root의 실제 UI 관측 기록이며 후보·영입 화면 파일과 구분한다.

Steam 복구 후 16:49:29.654(KST)의 최종 읽기 확인에서도 관련 게임 프로세스 0개, 시험 전 설정 해시 일치, 실행 시작 시 생산 이름 소스 해시 일치를 확인했다. 최종 판정과 이 확인은 `runtime/run2-direct-korean-final/assessment.json`의 `SteamCleanup`·`FinalReadOnlyChecks`를 따른다.

문서·manifest·실제 화면과 로그의 독립 마감 대조는 15 PASS, 0 FAIL이었다. `validation/final-documentation-consistency-review.json`에 후보·채용·비용·체크섬·미검증 범위·Steam 증거 구분과 후속 링크의 일치를 기록했다.

이번 이름 작업의 helper·원문/실패 사본·검사 결과·스크린샷은 모두 외부 작업 경로에 있다. 저장소에는 생산 이름 파일과 유지관리 문서·대응표만 반영했다. 작업 중 저장소에 기존 테스트 산출물로 판단할 파일은 발견하지 않았으며, 무관한 정리 작업은 수행하지 않았다. Git 브랜치·HEAD는 위 기준과 같고 기존 초상화·AGENTS 변경을 보존한 미커밋 상태다.

Git commit·push·패키징·게시와 AVG 설정 변경은 이 작업의 범위에 포함하지 않는다.

## 후속 요청에 따른 로마자 복원

2026-11-12(KST). 사용자가 신규 과학자 이름을 다시 영어로 적도록 요청하여 `common/names/00_names.txt`의 `KOR` 이름·성 목록을 한글화 이전 로마자 원문으로 복원했다. 남성 71·여성 17·성 14개 항목의 철자·순서·하이픈·인용 형태와 빈 callsigns를 원작업 사본과 바이트 단위로 대조했다. 같은 목록을 쓰는 다른 한국 무작위 인물도 원래 표기를 사용한다. 과학자만의 새 이름 생성 시스템은 추가하지 않았다.

- 변경: 앞서 한글화한 `KOR` 신규 생성 이름·성 102개 항목을 원문으로 복원.
- 의도적 유지: 황부길·조경연·도상록·김용관의 고정 인물 정의와 Korean·English 두 채널의 기존 한글 현지화. 해당 3개 파일과 초상화 목록·전용 GFX의 해시가 복원 전과 일치한다.
- 제외: 타국 이름 목록, 초상화 자산·능력·특성·모집 비용, 게임 설정, 기존 저장의 인물 이름 변경.
- 검증: `KOR` 블록이 한글화 전 사본과 바이트 단위로 동일하며, 복원 전 소스의 다른 부분은 새 기여자 주석 1줄 외 그대로다. UTF-8 BOM 없음·CRLF와 이전 기여자 주석을 보존했다. `git diff --check`가 통과했다.
- 실행 범위: 이번 원문 복원 후 게임·로그·저장 검증은 실행하지 않았다. 위 한글 표시 화면을 복원 후 로마자 화면 증거로 사용하지 않는다.

이번 외부 증거 경로는 `C:/hoi/test/hok-scientist-name-roman-restore-20261112-01/`다. 복원 전 한글 소스는 `00_names.before-roman-restoration.txt`, 보존 파일 해시는 `preserved-files.before.json`, 최종 대조 결과는 `restoration-verification.json`에 있다. 원문 참조는 이전 작업의 `C:/hoi/test/hok-scientist-name-localisation-20261112-01/source-before/common/names/00_names.txt`이며 SHA-256은 `1a7a0e06f26ec3e03bea00ea7ea37b23ae138a575706d84bed0304e889eb3662`다. 복원 전 소스 해시는 `f428e6a66553c62b721f68433dd3e49d1463dd3b58890a710d3451d428d8af64`, 복원 후 해시는 `7659d5eab0428cf1548dc37737c6f82564a936546af6ce054c9efa3266c36a6c`다. 이전 검증 자료와 미커밋 작업은 보존했으며 commit·push는 하지 않았다.

## 사용자 지정 이름 제외

2026-11-12(KST). 사용자가 지목한 `Geunhye`(근혜) 1개만 `KOR.female.names`에서 삭제했다. 여성 후보는 17개에서 16개로 줄었으며 다른 이름·성·고정 과학자 현지화·초상화는 유지했다. 같은 `KOR` 이름 풀을 쓰는 신규 한국 인물에도 이 제외가 적용된다. 다른 흔한 이름을 특정 정치인으로 추정하여 추가 삭제하지 않았다. 이미 생성된 인물이나 저장 파일을 수정한 작업은 아니다.

삭제 전 사본과 최소 변경 대조는 `C:/hoi/test/hok-scientist-name-geunhye-removal-20261112-01/00_names.before.txt`, `removal-verification.json`에 보존했다. 삭제 후 소스 SHA-256은 `08c6cad04ded79dfd18dd49ae32e8d68570d77ff78db0bee3e1ded17d6745c8d`다. 원문에서 해당 토큰 1개 제거와 기여자 주석 1줄 추가 외의 바이트는 동일함을 확인했다. 이번 단일 이름 제외 후 게임 실행·저장 검증은 하지 않았다.

## 현대 정치인 실명과 겹치는 조합 후보 제외

2026-11-12(KST). 사용자의 「21세기 정치인 이름이 2차세계대전에 끼면 안 된다」는 후속 요구에 따라, 확인된 현대 정치인 실명과 같은 조합을 만들 수 있는 이름 부분을 한국 공용 생성 풀에서 제외했다. 정치 성향을 선정 기준으로 사용하지 않는다. 일반적인 이름 자체가 정치적이라는 뜻이나 원래 목록 작성자가 해당 정치인을 의도했다는 판정은 아니다. 이번 수정은 실명 중복을 피하기 위한 사용자의 콘텐츠 기준을 적용한 것이다.

성·이름을 독립 선택하는 기존 구조를 유지하여 이름 부분을 삭제했다. 따라서 해당 정치인의 성과 결합할 때뿐 아니라 다른 성과의 조합에서도 그 이름 부분은 생성되지 않는다. 남성 토큰 15개·여성 토큰 5개를 이번에 제거했으며, 같은 발음의 `Yoon-Gi`/`Yoongi`, `Ji-young`/`Jiyoung`, `Kyung-hee`/`Kyunghee`는 양쪽 철자를 함께 제외했다. 앞서 삭제한 `Geunhye`도 계속 제외된 상태다.

| 삭제한 이름 토큰 | 확인된 실명 중복 예 | 공식 자료 |
|---|---|---|
| `Sanghoon` | 김상훈 | [국회도서관 자료](https://www.nanet.go.kr/attachfiles/bodo/library/1707264989699.pdf) |
| `Sungmin`, `Sunghoon`, `Junghoon`, `Minsoo` | 박성민·박성훈·조정훈·김민수 | [국민의힘 공식 자료](https://m.peoplepowerparty.kr/about/people_center) |
| `Jaeyoung` | 이재영 | [국민의힘 공식 자료](https://www.peoplepowerparty.kr/news/comment_view_all/16561?gubun_list=all&page=2796) |
| `Jinho` | 박진호 | [국민의힘 공식 자료](https://www.peoplepowerparty.kr/news/comment_view/BBSDD0001/108617) |
| `Sungho` | 박성호 | [국민의힘 공식 자료](https://www.peoplepowerparty.kr/news/comment_view_all/16109?gubun_list=all&page=2899) |
| `Minseok`, `Jiwon`, `Jungho` | 김민석·박지원·김정호 | [국회도서관 자료](https://dl.nanet.go.kr/detail/PAMP10000000077313) |
| `Gun` | 김건 | [국회도서관 자료](https://ampos.nanet.go.kr/activityCongressDetail.do?congress_no=G1899888) |
| `Woong` | 김웅 | [국회도서관 자료](https://ampos.nanet.go.kr/activityCongressDetail.do?congress_no=G1899713) |
| `Yoon-Gi`, `Yoongi` | 김윤기 | [정의당 공식 자료](https://www.justice21.org/newhome/board/board_view.html?num=166848&page=5) |
| `Ji-young`, `Jiyoung` | 류지영 | [국회도서관 자료](https://ampos.nanet.go.kr/materialSeminarDetail.do?control_no=PAMP1000040049) |
| `Kyung-hee`, `Kyunghee` | 정경희 | [국민의힘 공식 자료](https://www.peoplepowerparty.kr/news/lawmaker_inspection_view/98548?page=3) |
| `Bora` | 김보라 | [안성시 공식 자료](https://www.anseong.go.kr/mayor/contents.do?mId=0101000000) |

확인 범위는 위 조합과 공식 자료에 한정한다. 남아 있는 모든 흔한 한국 이름이 전·현직 지방의원·출마자 등을 포함한 모든 현대 정치인과 우연히 겹치지 않는다고 보증한 전수 조사는 아니다. 새 이름을 추가할 때도 현대 정치인을 본뜬 이름을 넣지 않고 시대 적합성과 알려진 실명 조합을 먼저 검토한다.

| 기능·경로 | 처리 | 확인 범위 |
|---|---|---|
| `KOR.male.names`·`KOR.female.names` | 변경 | 위 토큰 20개 삭제, 남성 71→56·여성 16→11 |
| `KOR.surnames`·남은 이름 순서와 철자 | 의도적 유지 | 성 14개와 남은 토큰의 기존 순서·인용 형태 유지 |
| 같은 KOR 이름 풀을 소비하는 다른 신규 한국 인물 | 의도적 공통 적용 | 과학자 전용 필터가 아니므로 같은 후보 제외를 적용 |
| 다른 국가 이름 블록 | 의도적 유지 | KOR 외 바이트 동일; 다른 국가의 `Bora` 등을 삭제하지 않음 |
| 고정 과학자 네 명·두 언어 채널의 기존 이름·초상화 | 제외 | 관련 파일 해시가 직전 기준선과 일치 |
| 기존 저장의 이름·최종 모집 UI·새 선택 확률 | 미검증 | 이번 변경 후 게임 실행이나 저장 편집을 하지 않음 |

소스 정적 확인은 삭제한 토큰의 부재, 남은 이름·성의 순서·인용 형태, 빈 callsigns, KOR 밖 바이트와 UTF-8 BOM 없음·CRLF 보존을 대상으로 했다. `git diff --check`도 수행했다. 이전 한글 이름 화면과 초상화 시험을 이번 제외 후 화면의 증거로 사용하지 않는다.

외부 증거 경로는 `C:/hoi/test/hok-scientist-modern-name-exclusions-20261112-01/`다. 변경 전 사본은 `00_names.before.txt`, `name-manifest.before.json`, `name-record.before.md`, 보존 파일의 기준 해시는 `preserved-files.before.json`, 정적 대조 결과는 `removal-verification.json`에 있다.

소스 SHA-256: `08c6cad04ded79dfd18dd49ae32e8d68570d77ff78db0bee3e1ded17d6745c8d` -> `32aa863816ee3eacc02aa448e9ccbf0a4fcdb1af92809ce23bdf2cc5dd096b9f`.
