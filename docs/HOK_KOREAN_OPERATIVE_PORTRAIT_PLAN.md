# 한국 신규 모집 첩보원 전용 초상화 계획

같은 날 후속 요청으로 신규 남녀 8명의 그림을 《도깨비》 저승사자풍 검은 중절모·정장·코트 차림으로 편집하고, 후보 카드에서 드러나던 흰 배경을 불투명 회색 배경으로 수정했다. 현재 그림의 제작·출처·확인 범위는 [배경·복장 수정 기록](incidents/2026-11-12-korean-operative-outfit-background.md)을 따른다. 외부 증거 경로는 `C:/hoi/test/hok-operative-outfit-background-20261112-01/`다.

2026-11-12(KST) 최초 문서화 후 같은 날 구현 요청에 따라 **한국 전용 남녀 목록 → 프로젝트 GFX → 전용 DDS** 연결을 적용했다. 남성 4장·여성 4장의 사실적 화풍 AI 생성 초상화이며 본체의 정상 모집·채용, 게임 생성 임시 저장의 전체 재시작 재로드, 애니 조합의 저장된 남녀 표시를 확인했다. 일반 저장 파일의 이름 변경은 errno 2로 실패했다. 실제 관측과 한계는 [구현·검증 기록](incidents/2026-11-12-korean-operative-portraits.md), 그림별 출처·프롬프트·해시는 [자산 manifest](data/HOK_KOREAN_OPERATIVE_PORTRAIT_ASSET_MANIFEST.json)를 따른다.

추가 격리 진단에서 기본 한국과 13개 cosmetic tag의 남녀 28명이 한국 전용 그림을 표시했고, 남녀 8종 모두 게임 후보 화면에서 확인했다. JAP·RAJ 초상화 기준 대조 4명은 외국 그림을 표시했다. 자연스러운 정치 경로와 외국 현지 모집 결정 자체는 미검증이다. 시험 프로세스는 모두 종료했고 원래 모드 선택을 복원했다. `settings.txt`의 게임 자동 로딩 배경 기록 두 줄은 OS 쓰기 거부로 복원하지 못했으며 상세 복원 기록에 구분했다.

아래는 구현 전 조사와 초기 설계를 보존한 기록이다. 초기의 `대기`·`미확인`·`후속` 표현은 당시 상태이며, 현재 적용 여부와 분기별 최종 판정은 위 구현 기록을 우선한다. 최종 런타임 경로는 제안 경로와 동일하고, 애니 조합은 본체의 사실적 그림을 공유한다. 별도 애니 변형은 제공하지 않았다. 외부 작업·증거 경로는 `C:/hoi/test/hok-operative-portraits-20261112-01/`다.

## 목표와 적용 범위

한국을 초상화 기준 국가로 삼는 신규 첩보원이 한국 전용 그림을 선택하도록 구성한다. 엔진의 일반 모집 흐름에서 국가별 목록을 선택하게 하며, 남녀별 후보를 제공한다. 최종 장수·화풍·제작 방식은 후속 구현에서 정한다. 과학자의 남성 4장·여성 4장은 기존 구성의 참고 사례다. [과학자 계획](HOK_KOREAN_SCIENTIST_PORTRAIT_PLAN.md)

첩보원의 국적은 `nationalities`, 무작위 초상화의 기준 국가는 `portrait_tag_override`, 고정 초상화는 `GFX` 지정으로 각각 추적한다. 외국 현지 모집은 해당 생성 지점의 기준 국가를 따르므로, 적용 대상을 초상화 선택 경로별로 정의한다.

| 경로 | 계획한 처리 | 확인 기준 |
|---|---|---|
| 한국을 기준으로 하는 일반 신규 모집 | 한국 전용 `operative.female`·`operative.male` 목록 연결 | 정상 모집 후보와 채용 후 명단 |
| 윤봉길·이봉창 | 개별 GFX와 기존 인물 정의를 보존 기준으로 사용 | 고정 초상화·국적·특성·모집 설정 대조 |
| 외국 현지 모집 | 바닐라의 모집지 소유국 기준 선택을 보존 기준으로 사용 | `nationalities`와 `portrait_tag_override` 및 실제 모집 결과 |
| 한국의 cosmetic tag | 정치·형성국·종속국 분기에서 기본 목록 선택 또는 상속 확인 | 해당 분기의 실제 초상화 선택 |
| 애니 서브모드 | 지원 범위에 포함할 때 같은 상대 경로의 대응 DDS 제공 | 본체와 애니 조합의 실제 선택 파일·화면 |

이름·호출부호·성별 선택 확률·능력·특성·모집 비용·첩보원 슬롯은 이번 초상화 계획의 구현 대상에서 제외한다. 이름 표시나 생성 목록을 후속 변경할 때는 현재 로마자 표기와 이름 제외 정책을 먼저 확인한다. [이름 표시와 제외 기록](incidents/2026-11-12-korean-random-name-localisation.md)

## 기준 소스와 로드 구성

문서화 시작 시 저장소는 `feat/korean-focus-expansion-ai` 브랜치, 커밋 `f1282d701bc47e47c119ca31faa6082e9e6ed1e6`이며 작업 트리는 clean이었다. 저장소의 `descriptor.mod`는 `supported_version="1.19.*"`와 `Korean Language` 의존성을 선언한다. 설치본 `launcher-settings.json` 4행의 버전 표기는 `Operation Postern v1.19.4.2.2da5 (0bdb)`다. 괄호 안 값은 설치 메타데이터에서 읽은 값이다.

| 물리 위치 | 역할 |
|---|---|
| `C:/hoi/hearts_of_korea/` | 이번 계획과 후속 본체 구현의 작업 소스 |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/` | 읽기 전용 바닐라 구문·자산 연결 근거. 아래 바닐라 경로의 기준 디렉터리 |
| `C:/hoi/Hearts-of-Korea-anime/` | 읽기 전용 애니 연동 참고 소스 |
| `C:/Users/jaewo/OneDrive/문서/Paradox Interactive/Hearts of Iron IV/` | 실제 사용자 데이터. 아래 런처 파일과 `dlc_load.json`의 기준 디렉터리 |
| `mod/hearts of korea.mod` | `path="C:/hoi/hearts_of_korea"`를 선언하는 본체 런처 연결 |
| `mod/Hearts of Korea anime.mod` | `path="C:/hoi/Hearts-of-Korea-anime"`를 선언하는 애니 런처 연결 |

이번에 읽은 `dlc_load.json`의 `enabled_mods` 배열은 다음 순서다. `disabled_dlcs` 배열은 비어 있다.

| 배열 순서 | 런처 파일 | 선언된 물리 경로 |
|---|---|---|
| 1 | `mod/hearts_of_korea_Road_to_56.mod` | `C:/hoi/hearts_of_korea_Road_to_56` |
| 2 | `mod/ugc_2769576030.mod` | `C:/Program Files (x86)/Steam/steamapps/workshop/content/394360/2769576030` |
| 3 | `mod/ugc_820260968.mod` | `C:/Program Files (x86)/Steam/steamapps/workshop/content/394360/820260968` |
| 4 | `mod/Hearts of Korea the greatest.mod` | `C:/hoi/Hearts-of-Korea-the-greatest` |

현재 설정은 Road to 56 호환판·번역·Road to 56·국뽕팩 조합을 가리킨다. 후속 실행 검증에서는 요청된 본체 또는 애니 조합의 실제 활성 파일을 다시 확인한다. Road to 56 호환판과 국뽕팩으로의 이식은 별도 작업 범위로 둔다. 과학자 시험 당시의 본체 → 애니 구성과 관측은 해당 기록의 조건을 따른다. [과학자 구현 기록](incidents/2026-11-12-korean-scientist-portraits.md)

## 현재 연결과 바닐라 근거

| 대상 | 확인한 소스 | 의미와 확인 상태 |
|---|---|---|
| 한국 국가별 목록 | `portraits/00_portraits_KOR.txt` 1행, 26행 | `army`·`navy`·`scientist` 정의를 확인. `operative` 추가 대상인 기존 `KOR` 블록 |
| 아시아 공용 첩보원 | 바닐라 `dlc/dlc028_la_resistance/portraits/027_lar_portraits.txt` 172행 | `continent = asia` 아래 여성·남성 각각 9개 스프라이트. 소스 정의 `CONFIRMED` |
| 국가별 첩보원 | 같은 파일 275행 | `RAJ` 아래 `operative.female`·`operative.male` 각각 5개. 국가별 구문 `CONFIRMED` |
| 공용 그림 연결 | 바닐라 `dlc/dlc028_la_resistance/interface/lar_portraits.gfx` 1067행, 1112행 | 아시아 여성·남성 스프라이트가 각각 `gfx/leaders/Asia/portrait_asia_generic_operative_{female,male}_1.dds` 한 장에 연결됨. 정적 GFX·DDS 연결 `CONFIRMED` |
| 생성 효과 | 바닐라 `documentation/effects_documentation.md` 3183행 | `create_operative_leader`의 국가 scope, `portrait_tag_override`, 명시적 GFX, 무작위 초상화 설명 |
| 외국 현지 모집 | 바닐라 `common/decisions/lar_agent_recruitment_decisions.txt` 117행 | `nationalities = { FROM.OWNER }`와 `portrait_tag_override = FROM.OWNER`를 함께 지정 |

현지 모집 파일에서는 초상화 기준 국가 지정이 120·248·377·506·635·792·921·1085행의 8개 생성 지점에 있다. 조사한 HOK `common/`·`events/`·`history/`의 텍스트에서는 아래 고정 첩보원 두 생성 블록을 확인했다. 일반 모집 UI의 내부 선택은 후속 실행 확인 항목이다.

한국 일반 모집이 아시아 공용 풀을 사용한다는 판단은 현재 국가별 목록과 바닐라 대륙 목록에 근거한 `STRONGLY_SUPPORTED`다. 한국 전용 풀의 실제 선택·cosmetic tag 상속·저장 동작은 `UNPROVEN` 상태다.

고정 인물은 `history/countries/KOR - Korea.txt` 249행의 `has_dlc = "La Resistance"` 조건 안에서 생성된다. 이름·GFX·국적의 대응은 다음과 같다. [국가 초기화](<../history/countries/KOR - Korea.txt>), [고정 첩보원 GFX](../interface/leader_portraits_HoK.gfx)

| 인물과 생성 위치 | GFX와 DDS | 국적 |
|---|---|---|
| 윤봉길, 국가 초기화 250행 | `GFX_portrait_bonggil_yoon` → `gfx/leaders/KOR/portrait_KOR_operative_Bonggil_Yoon.dds` | `KOR` |
| 이봉창, 국가 초기화 259행 | `GFX_portrait_bongchang_lee` → `gfx/leaders/KOR/portrait_KOR_operative_Bongchang_Lee.dds` | `KOR JAP` |

## 구현 대상과 자산 설계

기존 `KOR` 블록 안에 `operative` 역할과 그 아래 `female`·`male` 목록을 추가한다. 스프라이트 접두사는 기존 프로젝트의 `GFX_HOK_KOR_`를 따른다.

| 후속 대상 | 계획 |
|---|---|
| `portraits/00_portraits_KOR.txt` | 기존 `KOR` 블록에 첩보원 남녀 목록 추가 |
| `interface/HOK_KOR_operative_portraits.gfx` | 전용 스프라이트와 DDS 상대 경로를 연결하는 새 GFX 후보 |
| `GFX_HOK_KOR_operative_{female,male}_01`부터의 ID | 성별과 일련번호로 후보를 식별. 구현 시 본체·관련 의존성·바닐라에서 중복 확인 |
| `gfx/leaders/operatives/HOK_KOR/portrait_HOK_KOR_operative_{female,male}_01.dds`부터의 파일 | 신규 모집용 완성 자산의 제안 경로 |
| `docs/data/HOK_KOREAN_OPERATIVE_PORTRAIT_ASSET_MANIFEST.json` | 자산 제작 시 생성할 출처·입력·가공·최종 경로·해시 기록 후보 |

후속 이미지는 시대에 맞는 한국 첩보원으로 구분할 수 있는 얼굴과 복장을 사용한다. DDS 치수·압축·알파·프레임과 화면 구도는 설치본 첩보원 자산 및 실제 모집 UI를 기준으로 정한다. 과학자 이미지의 규격은 참고 자료로 삼는다.

이미지 제작이나 과거 입력 재사용에 착수할 때는 개발 자료 보관 안내를 먼저 읽는다. 제작 원본·프롬프트·변환 중간물·미리보기·백업·실행 증거의 작업 경로는 `C:/hoi/test/<작업 또는 실행 ID>/`에서 정하고, 자산 기록에 실제 원본 위치·사용 조건·제작 방법·최종 해시를 남긴다. [개발 자료 보관 안내](HOK_DEVELOPMENT_ARTIFACT_ARCHIVE.md)

애니 서브모드의 `descriptor.mod` 6행은 `replace_path="gfx/leaders/KOR"`를 선언한다. 제안한 `gfx/leaders/operatives/HOK_KOR/`는 이 교체 경로 밖에 있다. 애니 대응 그림을 제공할 때는 같은 신규 상대 경로에 DDS를 배치하고, 본체의 스프라이트가 선택하는 물리 파일을 확인한다. 서브모드 자산 작업에 착수할 때는 해당 저장소의 작업 지침과 자산 교체 스킬을 먼저 읽는다. [애니 작업 지침](../../Hearts-of-Korea-anime/AGENTS.md), [애니 자산 교체 스킬](../../Hearts-of-Korea-anime/.agents/skills/hok-anime-assets/SKILL.md)

## 분기별 적용과 확인 계획

| 기능과 후보 | 후속 처리 | 근거와 남은 확인 |
|---|---|---|
| 신규 한국 남녀 첩보원 풀 | 수정 예정 | 바닐라 `RAJ.operative` 구문을 사용. HOK 정상 모집에서 실제 선택 확인 |
| 윤봉길·이봉창과 La Resistance 생성 조건 | 의도적 유지 | 개별 GFX·특성·국적·모집 대기·첩보장 제공 설정을 소스와 UI의 대조 기준으로 사용 |
| 아시아 공용 풀과 타국 목록 | 의도적 유지 | 프로젝트 전용 스프라이트·DDS를 추가하는 설계. 공유 정의에 대한 영향은 최종 소스 차이에서 확인 |
| 바닐라 현지 모집의 8개 생성 지점 | 의도적 유지 | `FROM.OWNER` 기반 초상화 선택. 외국 현지 모집 사례로 회귀 확인 |
| 이름·호출부호·게임 수치와 모집 규칙 | 제외 | 이번 작업은 신규 초상화 선택 경로를 대상으로 함 |
| 정치·형성국 cosmetic tag | 미확인 | `common/national_focus/korea.txt`의 `KOR_Balhae`·`KOR_Goguryeo`·`KOR_PRK_communism`·`KOR_democratic`·`KOR_Hwan_neutrality`·`KOR_Hwan`·`KOR_neutrality`, `common/decisions/KOR_decision.txt`의 `KOR_greater_Hwan_neutrality`를 후보로 대조 |
| 종속국 cosmetic tag | 미확인 | `common/on_actions/HoK_cosmetic_tag_on_actions.txt`의 `KOR_JAP`·`KOR_CHI`·`KOR_PRC`·`KOR_reichskommissariat_fascism`·`KOR_SOV_communism`를 후보로 대조 |
| 애니 변형 | 미확인 | 최종 제공 범위와 그림을 정한 뒤 같은 상대 경로의 대체 파일·로드 순서·표시 확인 |
| 기존 저장의 첩보원과 신규 모집 | 미확인 | 생성 당시 초상화의 저장 방식과 기존 인물의 처리 결과를 실제 저장에서 확인 |
| Road to 56 호환판·국뽕팩 연동 | 제외 | 현재 활성 설정에 존재하는 별도 소스. 이식 요청과 해당 소스 기준이 필요 |

위 cosmetic tag 13개는 현재 호출처에서 수집한 확인 후보다. 후속 구현에서는 각 호출의 국가 scope와 적용·복귀 상태를 대조하고, 국가별 목록의 선택 결과에 따라 태그별 추가 목록의 필요성을 결정한다.

## 후속 구현 검증

| 확인 단계 | 필요한 확인 |
|---|---|
| 소스와 자산 | 목록의 모든 스프라이트가 고유한 정의와 실제 DDS에 연결되는지 확인. 성별별 목록·경로 대소문자·DDS 규격·투명 경계·출처 기록 대조 |
| 로드 구성 | 선택한 본체·의존성·La Resistance·언어·모드 순서·실제 물리 파일·게임 버전과 메뉴 체크섬 기록 |
| 정상 모집 UI | 전체 게임 프로세스를 재시작하고 한국의 정상 모집에서 남녀 표본을 확인. 후보 창과 채용 후 명단의 그림·잘림·비율·가독성 확인. 개별 DDS를 확인한 범위도 기록 |
| 고정 인물과 다른 목록 | 윤봉길·이봉창의 모집·초상화와 기존 과학자·육군·해군 목록 연결 대조. 공용 자산까지 변경하게 되면 영향받는 타국의 실제 모집 확인 |
| 대체 모집 | 외국 현지 모집의 국적과 그림 확인. cosmetic tag는 호출·상속 구조가 같은 후보를 묶은 근거와 실제 관측 범위를 기록 |
| 애니 조합 | 제공 범위에 포함하면 본체 단독과 애니 조합에서 신규 남녀·고정 인물·선택 파일을 각각 확인 |
| 새 저장과 재로드 | 패치 후 정상 모집한 인물을 저장하고 전체 프로세스 재시작 후 이름·그림·명단 보존 확인 |
| 기존 저장 | 기존 저장 호환을 제공 범위에 포함하면 대표적인 구현 전 저장에서 기존 인물과 추가 모집을 확인하고 별도 사본에 저장·재로드 |

실행 결과는 소스 대조, 실제 UI, 정상 채용, 저장·재로드별로 기록한다. 과학자 시험의 날짜·소스·애니 자산 조건과 결과는 해당 이력을 따른다. [과학자 구현 기록](incidents/2026-11-12-korean-scientist-portraits.md)

로그 검토가 필요한 실행 작업에서는 먼저 로그 검토 스킬을 읽고 해당 실행의 원본·기준선·오류 귀속을 확인한다. 임시 모드 선택과 설정의 백업·복원, 작업 소유 게임·런처의 종료는 프로젝트 실행 규칙을 따른다. [로그 검토 스킬](../.agents/skills/hok-log-review/SKILL.md), [프로젝트 작업 규칙](../AGENTS.md)

## 최초 문서화 결과와 인계 이력

국가별 `operative` 남녀 목록, 단일 DDS 연결, 고정 첩보원 두 명, 현지 모집의 초상화 기준 지정, 현재 런처 경로와 설정을 소스에서 확인했다. 새 스프라이트·DDS·자산 manifest는 위 제안 경로를 사용해 후속 구현에서 마련한다. 남은 설계 항목은 최종 장수·화풍·제작 방식과 애니 변형의 제공 범위다.

이후 같은 날 구현 요청으로 목록·GFX·DDS 8개를 추가했다. 실제 분기 대장과 실행 증거는 상단의 구현·검증 기록으로 이어진다. 최초 문서화 당시의 조사 범위는 그 문단의 조건에 한정한다.
