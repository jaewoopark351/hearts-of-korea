# 한국 신규 모집 과학자 전용 초상화 계획

2026-11-12 후속 구현으로 한국 전용 남성 4장·여성 4장의 DDS와 목록·GFX 연결을 추가했다. HOK+애니 조합에서 정상 모집한 남녀 표본의 전용 그림을 확인했고, 날짜 진행 후 만든 임시 저장의 같은 프로세스 UI 재로드에서도 두 표본이 유지됐다. 최초 즉시 저장의 남성 미표시와 저장 rename 오류는 미해결이며 cosmetic tag·본체 단독 등 미검증 범위를 구분한다. 실제 적용 내용과 실행 확인 상태는 [구현 기록](incidents/2026-11-12-korean-scientist-portraits.md), 자산 출처와 프롬프트는 [자산 manifest](data/HOK_KOREAN_SCIENTIST_PORTRAIT_ASSET_MANIFEST.json)를 따른다. 아래 설계와 미검증 표시는 최초 문서화 시점의 이력이다.

신규 인물 이름 표기를 수정하거나 확인할 때는 [이름 현지화 후속 기록](incidents/2026-11-12-korean-random-name-localisation.md)을 먼저 읽는다. 부분 이름의 `.yml` 키 방식 실패와 한글 직접 표기 성공을 기록한 뒤, 사용자의 후속 요청으로 신규 이름 목록은 원래 로마자 표기로 복원했다. 고정 과학자 네 명의 한글 현지화는 유지한다. 아래 초상화 설계와 이름 표시의 구현·검증 범위는 구분한다.

2026-11-12(KST) 문서화 단계. 한국의 「과학자 모집」으로 새로 생성되는 인물에 한국 전용 초상화 목록을 지정하는 방식을 기록한다. 바닐라는 국가별 `scientist` 목록을 사용하므로 한국도 육군·해군처럼 `KOR` 아래에 남성·여성 과학자 목록을 둘 수 있다. HOK 적용과 실제 모집 검증은 후속 구현 단계다.

## 소스 기준과 위치

문서 작성 전 저장소는 `feat/korean-focus-expansion-ai` 브랜치, 커밋 `cdc022eee15fbf7404d4cb30cf2d0102d29e550c`이며 작업 트리는 clean이었다. 아래 근거는 이날 읽은 파일 기준이다.

| 위치 | 역할과 확인 내용 |
|---|---|
| `C:/hoi/hearts_of_korea/` | HOK 작업 소스. [한국 초상화 목록](../portraits/00_portraits_KOR.txt), [캐릭터 정의](../common/characters/KOR.txt), [스프라이트 연결](../interface/characters_HoK.gfx)이 현재 기준 |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/` | 읽기 전용 바닐라 근거. 아래 바닐라 파일명은 이 디렉터리 기준 상대 경로 |
| `C:/hoi/Hearts-of-Korea-anime/` | 읽기 전용 애니 서브모드 참고 소스. `descriptor.mod` 6행과 `gfx/leaders/KOR/`의 고정 과학자 DDS 네 장 확인 |

설치본 `launcher-settings.json` 4행은 `Operation Postern v1.19.4.2.2da5 (0bdb)`를 표기한다. 버전과 괄호 안 값은 설치 메타데이터에서 읽은 값이다. 사용자 데이터의 실제 위치는 `C:/Users/jaewo/OneDrive/문서/Paradox Interactive/Hearts of Iron IV/`다. 그 아래 `dlc_load.json`은 HOK → 애니 서브모드 순서를 기록하며, `mod/hearts of korea.mod` 13행과 `mod/Hearts of Korea anime.mod` 23행의 `path`는 위 두 로컬 저장소를 가리킨다.

## 구현 전 초상화 연결

| 구분 | 현재 파일 설정 | 근거 |
|---|---|---|
| 한국 국가별 목록 | `KOR` 아래 `army`·`navy` 목록 등록 | [00_portraits_KOR.txt](../portraits/00_portraits_KOR.txt) 1행 |
| 아시아 공용 과학자 | 여성 `01`부터 `08`, 남성 `01`부터 `08`까지 각 8장 | 바닐라 `portraits/998_scientist_portraits.txt` 138행 |
| 유럽 공용 과학자 | 여성·남성 각각 `01`부터 `16`까지 각 16장. 영국 신규 모집의 파일상 공용 목록 | 같은 파일 44행, 바닐라 `portraits/00_portraits.txt` 400행의 `ENG` 육군·해군 목록 |
| 한국 고정 과학자 네 명 | 초기 `recruit_character`와 개별 `large` 초상화 연결 | [KOR - Korea.txt](<../history/countries/KOR - Korea.txt>) 242행, [KOR.txt](../common/characters/KOR.txt) 1481행 |

아시아 공용 목록의 스프라이트는 바닐라 `interface/_scientists_portraits.gfx` 609행에서 `gfx/leaders/scientists/generic_scientists/portrait_generic_asia_female_01.dds` 등의 상대 경로로 연결된다. 남성·여성 `01`부터 `08`까지 실제 DDS 16개가 존재한다. 같은 목록을 참조하는 국가들이 이 자산을 공유한다. 유럽 공용 DDS 32개도 같은 디렉터리에 `portrait_generic_europe_{male,female}_01~16.dds` 이름으로 존재하며, 연결은 같은 GFX 파일 705행에 있다.

한국의 신규 모집에 아시아 공용 풀이 적용된다는 판단은 현재 `KOR` 목록에 `scientist`가 없는 점과 바닐라 아시아 목록에 근거한 `STRONGLY_SUPPORTED` 상태다. 국가별 목록과 실제 DDS의 존재는 `CONFIRMED`이며, 한국·영국의 이번 실제 모집 화면은 미검증이다.

고정 네 인물은 다음 연결을 사용한다. DDS 경로는 모두 `gfx/leaders/KOR/` 기준이며 본체와 애니 서브모드에 같은 파일명 네 장이 존재한다. 스프라이트의 실제 연결은 [characters_HoK.gfx](../interface/characters_HoK.gfx) 383행부터 확인한다.

| 인물과 캐릭터 ID | 스프라이트 | DDS 파일명 |
|---|---|---|
| 황부길 `KOR_Bugil_Hwang` | `GFX_Portrait_KOR_Bugil_Hwang` | `Portrait_KOR_scientist_Bugil_Hwang.dds` |
| 조경연 `KOR_Gyeongyeon_Jo` | `GFX_Portrait_KOR_Gyeongyeon_Jo` | `Portrait_KOR_scientist_Gyeongyeon_Jo.dds` |
| 도상록 `KOR_Sanglok_Do` | `GFX_Portrait_KOR_Sanglok_Do` | `Portrait_KOR_scientist_Sanglok_Do.dds` |
| 김용관 `KOR_Yonggwan_Kim` | `GFX_Portrait_KOR_Yonggwan_Kim` | `Portrait_KOR_scientist_Yonggwan_Kim.dds` |

영국도 제임스 채드윅·프랭크 휘틀·존 콕크로프트 등 고정 과학자 6명의 개별 DDS를 사용한다. 근거는 바닐라 `common/characters/ENG.txt` 2493행부터, `interface/_scientists_portraits.gfx` 99행부터의 `gfx/leaders/scientists/portrait_ENG_*.dds` 연결이다.

## 국가별 과학자 목록의 바닐라 근거

바닐라 `portraits/998_scientist_portraits.txt`는 `PAK` 218행과 `RAJ` 239행에 국가별 `scientist` 블록과 그 아래 `female`·`male` 스프라이트 목록을 둔다. 이 국가별 구문은 설치 소스에서 `CONFIRMED`다. 한국에 전용 목록을 구성하는 제안도 이 형식을 따른다.

기존 [00_portraits_KOR.txt](../portraits/00_portraits_KOR.txt)의 `KOR` 블록에 다음 `scientist` 블록을 추가하는 안을 사용한다. 아래 스프라이트 이름과 성별별 1장 구성은 문법 예시다. 최종 수량·그림체·제작 방식·파일명은 후속 구현 때 정한다.

```text
scientist = {
    female = {
        "GFX_HOK_KOR_scientist_female_01"
    }
    male = {
        "GFX_HOK_KOR_scientist_male_01"
    }
}
```

바닐라는 `PAK`의 육군·해군 목록을 `portraits/00_portraits.txt` 767행, 과학자 목록을 `998_scientist_portraits.txt` 218행에 나눠 정의한다. 파일 분할 예시는 존재한다. 같은 국가의 같은 역할을 중복 정의할 때의 병합·우선순위와 HOK 적용 결과는 미확인이다. 이번 제안은 현재 한국 파일의 기존 `KOR` 블록을 확장한다.

바닐라에는 `RAJ_UK` 260행, `SAF_COM` 411행처럼 cosmetic tag 이름의 별도 과학자 목록도 있다. 한국의 실제 cosmetic tag 사용처와 기본 `KOR` 목록의 상속 여부는 구현 시 확인 항목으로 남긴다.

## 후속 적용 파일과 자산 구성

| 대상 | 후속 적용안 |
|---|---|
| `portraits/00_portraits_KOR.txt` | 현재 `KOR` 블록의 육군·해군 목록과 함께 전용 `scientist` 남성·여성 목록을 등록 |
| `interface/HOK_KOR_scientist_portraits.gfx` | 새 파일 후보. 프로젝트의 `GFX_HOK_KOR_` 접두사를 사용하는 전용 스프라이트와 DDS 상대 경로 연결 |
| `gfx/leaders/scientists/HOK_KOR/` | 신규 모집용 완성 DDS의 제안 위치. 각 성별 목록에 등록한 스프라이트에 대응하는 파일을 저장 |
| 자산 출처 기록 | 실제 사용한 원본 위치·저작자·사용 조건·생성 또는 가공 방식·최종 파일 해시를 `docs/`의 관련 크레딧과 자산 목록에 기록 |

연결은 `KOR.scientist`의 스프라이트 목록 → 프로젝트 소유 GFX 정의 → 저장소 내부 DDS 순서다. 최종 이미지의 치수·DDS 형식·알파는 설치본 과학자 초상화와 해당 UI에 맞춰 확인한다. 현재 아시아 목록의 성별별 8장은 현행 공용 풀의 수량이며 한국 전용 풀의 최종 장수는 미정이다.

애니 서브모드는 `replace_path="gfx/leaders/KOR"`를 선언한다. 제안한 `gfx/leaders/scientists/HOK_KOR/`는 이 교체 경로 밖에 있어 신규 자산의 위치로 선택했다. 애니 전용 변형이 필요하면 서브모드에 같은 신규 상대 경로의 대응 DDS를 제공하는 안을 검토한다. 실제로 선택되는 물리 파일과 화면 표시는 적용 후 확인한다.

이미지 제작과 과거 입력 재사용에 착수할 때는 [개발 자료 보관 안내](HOK_DEVELOPMENT_ARTIFACT_ARCHIVE.md)를 먼저 읽는다. 완성 DDS는 위 런타임 경로에, 원본·생성 출력·변환 중간물·시험 증거는 `C:/hoi/test/<작업 또는 실행 ID>/`에 둔다. 고정 네 인물의 현재 연결은 위 표를 회귀 확인 기준으로 사용한다.

## 후속 구현 검증

다음은 한국 전용 풀 구현 후 필요한 확인 항목과 적용 조건이다. 이번 문서화의 실제 확인 범위는 위 소스와 경로의 읽기 검토다.

| 확인 대상 | 완료 판단에 필요한 관측 |
|---|---|
| 목록과 자산 연결 | 남성·여성 목록의 모든 스프라이트가 유일한 정의와 실제 프로젝트 DDS로 연결되고, 경로 대소문자·형식·치수·알파가 해당 UI와 일치 |
| 한국 신규 모집 | 전체 프로세스 재시작 후 한국에서 정상 「과학자 모집」으로 생성한 인물의 초상화 확인. 남성·여성으로 생성된 결과와 반복 모집 시 표시를 기록 |
| 한국의 다른 경로 | 실제 사용되는 cosmetic tag를 조사하고 대표 적용·복귀 상태에서 전용 목록의 적용 또는 상속 확인 |
| 기존 인물과 장교 | 고정 과학자 네 명의 개별 연결, 육군·해군 신규 장교 초상화의 정상 표시 확인 |
| 타국 공용 목록 | 소스 비교로 공용 목록·스프라이트에 미치는 영향 확인. 공용 대륙 목록이나 스프라이트까지 변경한 경우 영향받는 타국의 실제 신규 모집도 확인 |
| 애니 서브모드 | 본체 단독의 로드 경로·신규 모집·고정 인물 표시 확인. 애니 조합을 제공 범위에 포함하면 해당 조합에서도 같은 항목 확인 |
| 저장 후 재로드 | 패치 후 새로 모집한 과학자의 저장·재로드 표시 확인. 기존 저장 호환을 제공 범위에 포함하면 구현 전 저장의 기존 인물과 추가 모집 결과를 별도 기존 저장으로 확인 |

런타임 기록에는 정확한 게임 버전·활성 DLC·언어·모드 순서·실제 파일 출처를 함께 남긴다. 화면 관측과 저장 결과를 각각 기록하고, 기존 저장의 초상화가 자동으로 전환되는지 여부도 실제 관측에 따라 정리한다.
