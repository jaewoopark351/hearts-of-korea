# 한미 방위비 협정 자산 출처와 제작 기록

작성일: 2026-11-11. 이 문서는 한미 조약·주둔 모듈의 실제 채택 이미지, 생성 프롬프트, 참조 입력과 게임용 변환을 기록한다. 게임 동작은 [한미 방위비 명세](HOK_KOREAN_US_DEFENSE_COST_SHARING_SPEC.md)를 따르고, 선택 원본 6개·런타임 자산 8개의 파일 기록은 [통합 자산 manifest](data/HOK_KOREAN_US_DEFENSE_ASSET_MANIFEST.json)에 보존한다. 아래 사진·아이콘은 **AI 생성 창작물**이며 실제 역사 사진이나 다른 HOI4 모드의 원화가 아니다.

## 후속 실제 게임 화면 확인

2026-11-11 런타임 담당이 HOI4 `v1.19.4.2.2da5`, 한국어 UI의 run3 및 한국 플레이어 진단 저장 재로드에서 아래 자산 표시를 관찰했고, run4 정상 중점 진행에서 한국 II 아이콘을 추가 관찰했다. 실행 체크섬은 run3 `1b0d`, run4 `1402`다. 앞서 수행한 제작 담당의 정적 원본·작은 크기 검사 이력도 그대로 보존한다. run3의 외부 진단 모드 분기 검증과 run4의 정상 중점 진행 결과는 [구현·검증 기록](incidents/2026-11-11-korean-us-defense-sharing.md)에서 구분하여 관리한다.

화면 증거 기준 경로는 `C:/hoi/test/us-defense-sharing-20261111-01/runtime/screenshots/`다. 사진 4종과 아이콘 3종은 실제 표시를 관찰했으며, 나머지 아이콘 1종은 현재 정적 자산 검사까지만 확인했다.

| 런타임 자산 | 실제 화면 확인 | 보존한 UI 증거 |
|---|---|---|
| `us_defense_talks` | 조약·주둔 협상 국가 사건의 사진 표시 | `01-treaty-offer.png`, `02-stationing-options.png` |
| `us_defense_agreement_news` | 방위비 협정 뉴스 사진 표시 | `03-agreement-news.png` |
| `us_defense_dominion` | 한국 자치령 통보의 사진과 단일 수락 선택지 표시 | `11-korean-dominion-single-accept.png` |
| `us_defense_dominion_news` | 미국·한국 관점의 자치령 뉴스 사진 표시 | `06-dominion-news.png`, `12-korean-dominion-news.png` |
| `HOK_KOR_us_defense_cost_sharing_1` | 한국의 1단계 국민정신 아이콘 관찰 | `09-kor-tier1-after-refusal.png` |
| `HOK_KOR_us_defense_cost_sharing_2` | run4에서 한국의 2단계 국민정신 양국 국기 아이콘과 소비재 공장 계수 +35.0% 툴팁 관찰 | `22-normal-kor-tier2-35percent.png` |
| `HOK_KOR_korean_defense_contribution_1` | 미관찰 — 정적 원본·실제 크기·DDS 검사 유지 | — |
| `HOK_KOR_korean_defense_contribution_2` | 미국의 2단계 국민정신 아이콘과 소비재 공장 계수 −15.0% 툴팁 관찰 | `04-usa-tier2.png` |

이 색인은 실제로 표시된 자산과 관찰 화면의 범위다. 사건 효과·저장 상태·AI·재처리·정상 진행 검증은 위 구현 기록과 각각의 런타임 증거를 따른다. 이미지 파일·생성 원본·출처·해시는 이 후속 색인 추가로 변경하지 않았다.

## 사건·뉴스 사진

사진은 기본 제공 `image_gen.imagegen`으로 서로 다른 장면 두 개를 생성하고, 같은 도구로 국기와 구도를 보정했다. 실제 모델명은 도구 결과에 노출되지 않았으므로 기록하지 않는다. 생성·편집일은 모두 2026-11-11이다. 제작·선정·통합은 continuation contributor `kpopmodder` 작업이며 원작 HOK의 기존 사진 저작권·크레딧을 대체하지 않는다.

- 협정 장면: 양국 대표가 방위 협정서에 서명하는 장면. 조약/주둔 협상 국가 사건 및 방위비 협정 뉴스에 사용한다.
- 자치령 장면: 양국 대표가 문서를 발표하는 장면. 대한민국 자치령 전환 통보 및 같은 결과의 세계 뉴스에 사용한다. 합병·51개 별 국기를 묘사하지 않는다.
- 공통: 1930~40년대 복식, 흑백 기록사진풍, 태극기와 성조기. 제목·본문·선택지·수치·워터마크는 그림에 넣지 않았다.

### 채택 원본과 실제 생성 경로

도구의 기본 출력은 그대로 보존했다. 아래 프로젝트 사본은 선택한 PNG와 바이트가 같은 원본 보존본(각 1536×1024)이다. 최초 시안은 사괘 또는 문서 위치 확인 뒤 편집했으므로 런타임에 사용하지 않는다. 최초 시안·변환 helper·미리보기·검증 기록은 `C:/hoi/test/us-defense-sharing-20261111-01/art/photos/`에 보관한다.

| 역할 | 실제 도구 출력 | 프로젝트 보존본 | SHA-256 |
|---|---|---|---|
| talks_selected | `C:/Users/jaewo/.codex/generated_images/01a1c9ad-e7d7-7250-bc9a-426b3a5c025e/exec-b0454617-9992-46ed-b5c5-36e242a90eee.png` | [us_defense_talks_selected.png](assets/us-defense-sharing/generated/photos/us_defense_talks_selected.png) | `B9678134BFCC74A2765E08725BE8F9AAACA8D38DFF1E1DEEEA17BAA8A0841C67` |
| dominion_selected | `C:/Users/jaewo/.codex/generated_images/01a1c9ad-e7d7-7250-bc9a-426b3a5c025e/exec-d991b6b5-c69f-49a3-9186-a492398a2c34.png` | [us_defense_dominion_selected.png](assets/us-defense-sharing/generated/photos/us_defense_dominion_selected.png) | `D211C4073F8B5582826C44B9335ECE1667D3DACCA4A724FF0F2D8E3C639FB2FB` |

최초 협정 시안 `C:/Users/jaewo/.codex/generated_images/01a1c9ad-e7d7-7250-bc9a-426b3a5c025e/exec-cc287111-77da-49b1-a9d4-340cfec17bae.png`의 SHA-256은 `EAB110AC2DBE84DAF5758A9B3E3F2415794795F8F96A8476B46C72C9AF034C0F`이며 외부 보존본은 `C:/hoi/test/us-defense-sharing-20261111-01/art/photos/talks_initial_generated.png`다. 최초 자치령 시안 `C:/Users/jaewo/.codex/generated_images/01a1c9ad-e7d7-7250-bc9a-426b3a5c025e/exec-53277031-54f2-4dd6-ad87-98643179980f.png`의 SHA-256은 `F344986E3AE84ADFD4EF878A406DB1DA1C80E4CC8B1E787166590D820DB02B16`이며 외부 보존본은 `C:/hoi/test/us-defense-sharing-20261111-01/art/photos/dominion_initial_generated.png`다.

### 참조 국기

두 편집 작업에서만 아래 국기 PNG를 형태 참조로 사용했다. 새 사진의 인물·배경·사진 장면은 AI 생성이며 게임/다른 모드의 사진을 복사하지 않았다. 국기 TGA를 BGRA 픽셀 그대로 PNG로 변환했으며 색상·형태를 편집하지 않았다. 두 참조는 82×52이고, 프로젝트 내부에 입력과 원본을 함께 보존한다.

| 입력 | 출처·역할 | 보존본과 해시 |
|---|---|---|
| 대한민국 | 프로젝트 기존 `gfx/flags/KOR_democratic.tga`의 태극기. 계승 자산이며 새로 창작했다고 주장하지 않는다. | [원본](assets/us-defense-sharing/generated/photos/references/KOR_democratic_project.tga) `3BCDB104244BF78B2DAE3F6DED909781F0A7997910BE4C42F9623623F6210A5A`; [도구 입력 PNG](assets/us-defense-sharing/generated/photos/references/reference_KOR_democratic.png) `AF6790C595BF232218520349DD5716A1553C07A55EF0B6A342109E234AE96818` |
| 미국 | 읽기 전용 설치본 `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/flags/USA_democratic.tga` (HOI4 1.19.4.2). Paradox 게임 자산을 시대에 맞는 국기 형태의 참조로 사용했으며 독립 공개 소재 팩의 원화/라이선스로 표시하지 않는다. | [원본](assets/us-defense-sharing/generated/photos/references/USA_democratic_vanilla_1.19.4.tga) `329EBC817D1CFC141883357CC99EAC36AF32AA08EC3B970D1791E91D211D2559`; [도구 입력 PNG](assets/us-defense-sharing/generated/photos/references/reference_USA_democratic.png) `4E1BD6BD5E1DED80E34683C2993C1FFF998C701E9FF0711E2B80A4C50492FB7C` |

참조 국기 도안과 기존 게임 자산의 권리는 원 권리자에게 남는다. 이 문서는 새 라이선스나 다른 게임/모드 자산 전체의 재사용 허가를 선언하지 않는다. 원본 설치본과 Workshop 파일은 수정하지 않았다. 런타임 사진에는 참조 TGA 픽셀을 직접 합성하지 않았다.

### 게임용 변환과 연결

설치본 `interface/eventwindow.gui`에서 국가 사건의 그림은 `bottom_Window/event_picture` (x5,y5), 선택지 영역은 x215로 확인했다. 같은 설치본의 뉴스 그림은 x59,y91이고 제목은 y260이다. 프로젝트 기존 `report_event_K003.dds`(210×176), `newsk_event_001.dds`와 설치본 `news_event_072.dds`(397×153)의 DDS 헤더로 아래 규격을 대조했다.

원본에서 각각 크롭한 뒤 PowerShell `System.Drawing`의 `HighQualityBicubic`으로 리샘플링했다. DDS는 기존과 같은 **비압축 BGRA32, 1프레임, mipmap 없음, 알파 255**다. 이미지 편집·보정은 image_gen으로만 수행했고 Python은 사용하지 않았다. 변환 helper는 외부 작업 경로의 `export-photos.ps1`, 국기 형식 변환은 `tga-to-png.ps1`이다. source 좌표는 원본 PNG 기준 `[x,y,width,height]`다.

| 런타임 파일 | sprite | 크기 | 원본 크롭 | SHA-256 |
|---|---|---|---|---|
| [us_defense_talks.dds](../gfx/event_pictures/HOK_KOR/us_defense/us_defense_talks.dds) | `GFX_HOK_KOR_us_defense_talks` | 210×176 | `[157, 0, 1222, 1024]` | `11EDFFFB5588C9ED4319244984DA8AD4447207412513C440193F5A75B91ED650` |
| [us_defense_agreement_news.dds](../gfx/event_pictures/HOK_KOR/us_defense/us_defense_agreement_news.dds) | `GFX_HOK_KOR_us_defense_agreement_news` | 397×153 | `[0, 320, 1536, 591.96]` | `453FFC5867B00200EAA53F142DE539E133EA6B85FE24152EDF182653BD4C66AC` |
| [us_defense_dominion.dds](../gfx/event_pictures/HOK_KOR/us_defense/us_defense_dominion.dds) | `GFX_HOK_KOR_us_defense_dominion` | 210×176 | `[157, 0, 1222, 1024]` | `8B13E50096E50F72103296D193ED4ABCFA680435A7CB25ACDDDA1F2EDB1DFA69` |
| [us_defense_dominion_news.dds](../gfx/event_pictures/HOK_KOR/us_defense/us_defense_dominion_news.dds) | `GFX_HOK_KOR_us_defense_dominion_news` | 397×153 | `[0, 110, 1536, 591.96]` | `510BA0E1FC4E0EAA7323C5BC71EA7676DFD331E5F06DB267F52930A681B2A2A5` |

GFX는 [프로젝트 전용 사건 사진 정의](../interface/HOK_KOR_us_defense_event_pictures.gfx)이고 모든 texturefile은 위 프로젝트 내부 파일을 모드 루트 기준 상대 경로로 참조한다. 외부 설치본·생성 기본 폴더에 의존하는 런타임 경로는 없다.

### 실제 확인과 남은 확인

2026-11-11 사진 담당 작업에서 채택 원본과 210×176·397×153 실제 크기 PNG 네 개를 각각 열어 확인했다. 두 국기와 대표/협정 모티프가 식별되며 문구·워터마크가 관찰되지 않았다. 태극기 사괘는 형태 참조에 맞춰 보정했으며 흑백과 작은 화면에서는 국기 색상과 별 개수를 픽셀 수준으로 입증하는 검사를 주장하지 않는다. 뉴스용 크롭은 국기 일부와 주변 보좌관을 잘라내되 두 국가와 주요 행위를 유지한다.

네 DDS의 헤더·크기·채널 마스크·파일 길이·불투명 알파를 확인했고, 각 DDS RGB 픽셀은 검수한 PNG와 전부 일치했다(불일치 0). 프로젝트 interface에서 네 sprite 정의 충돌은 발견되지 않았다. 이 결과는 **정적 자산/작은 크기 검사**다. 사진 담당은 게임을 실행하지 않았으며 실제 국가 사건/뉴스 창의 엔진 표시·오버레이·텍스트와의 간섭 검증은 별도 런타임 결과를 따른다.

외부 증거: `C:/hoi/test/us-defense-sharing-20261111-01/art/photos/photos-proof.json`. 이 경로는 중간 자료/검증 기록이며 배포용 파일이 아니다. 이 작업에서 커밋·푸시·업로드를 수행하지 않았다.

### 생성·편집 프롬프트 전문

#### 1. talks_initial — new generation

도구: `image_gen.imagegen (built-in)`. 참조: 없음 (신규 생성).

```text
Use case: historical-scene
Asset type: original archival-style event and newspaper photograph for the Hearts of Iron IV alternate-history mod Hearts of Korea, not a real historical photograph.
Primary request: a serious Korean-American defense treaty negotiation and signing in the late 1930s to early 1940s. A Korean civilian diplomat and an American civilian diplomat seated closely at a wooden table, each in period dark wool suits, studying and signing a defense agreement, with two quiet aides behind them. Natural elderly and middle-aged faces, believable hands and fountain pens, restrained expressions.
Scene/backdrop: modest period government meeting room, wood paneling, plain curtains, understated desk lamps.
Flags are essential: one recognizable Republic of Korea Taegeukgi and one recognizable period United States 48-star flag standing directly behind the two principal diplomats. Taegeukgi has a plain light field, central red-over-blue taegeuk and exactly four correct black trigrams in the corners; US flag has rectangular star canton and alternating stripes. Flags must look like actual cloth flags, not abstract designs.
Style/medium: convincing black-and-white silver-gelatin press photograph with light natural film grain, soft restrained archival contrast and realistic optical detail, not an illustration.
Composition/framing: horizontal 3:2 landscape, medium-wide press camera at eye level. Keep BOTH flags, the two principal faces, signing hands and treaty in a compact central group entirely within the central 70% width and central 55% height. Flags just behind heads, not high above them. Surrounding room is expendable crop space. Must remain clear when cropped both to a near-square 210:176 country event and to a shallow 397:153 newspaper photo. Avoid extreme depth of field and do not split into panels.
Lighting/mood: dignified, sober state negotiations; diffuse window light; meaningful midtone separation.
Constraints: new fictional scene, anonymous period officials, historically plausible clothing. No Donald Trump or any contemporary public figure; no modern items, color posters, printed titles, subtitles, watermark, border, signage, visible legible writing, captions, propaganda slogan or extra flag. No deformed hands or duplicated people. The document may have indistinct small lines but no invented readable text.
```

#### 2. talks_selected — flag correction edit

도구: `image_gen.imagegen (built-in)`. 참조: `C:/Users/jaewo/.codex/generated_images/01a1c9ad-e7d7-7250-bc9a-426b3a5c025e/exec-cc287111-77da-49b1-a9d4-340cfec17bae.png`, `C:/hoi/test/us-defense-sharing-20261111-01/art/photos/reference_KOR_democratic.png`, `C:/hoi/test/us-defense-sharing-20261111-01/art/photos/reference_USA_democratic.png`.

```text
Use case: precise-object-edit
Asset type: AI-generated black-and-white period diplomatic photograph for a Hearts of Iron IV event.
Edit target: image 1, the Korean-American treaty signing scene. Supporting references: image 2 is the exact Korean flag design, image 3 is the exact period United States flag design. These two small flag designs are geometry references only.
Change only the two flag designs in the photograph so that the existing cloth flags faithfully carry the reference designs in correct upright orientation. In particular the Taegeukgi must have exactly four correctly placed trigrams: upper-left three solid bars; upper-right broken/solid/broken; lower-left solid/broken/solid; lower-right all three broken. Its central taegeuk is the normal upright symbol. The United States flag is 48 stars arranged six rows of eight, with thirteen alternating stripes. Render the designs naturally following the current gentle folds, retaining the same monochrome photograph.
Keep the original anonymous diplomats, faces, hands, pens, papers, clothing, lighting, furniture, background, composition, and image proportions unchanged. No added text, borders, watermark, stars outside the US canton or new flag. Do not convert the photo into a drawing or a poster.
```

#### 3. dominion_initial — new generation

도구: `image_gen.imagegen (built-in)`. 참조: 없음 (신규 생성).

```text
Use case: historical-scene
Asset type: original archival-style event and newspaper photograph for the alternate-history Hearts of Iron IV mod Hearts of Korea; a fictional 1930s to early 1940s scene, not a real historical photograph.
Primary request: a solemn public announcement of Korea entering a new American dominion relationship while its own Korean administration continues to exist. An American civilian official and a Korean civilian delegate stand side by side, both in late-1930s dark suits, facing assembled press. The American official holds out a closed plain document folder and the Korean delegate receives it; their hands meet naturally at waist height. Two secondary officials stand slightly behind, restrained diplomatic expressions.
Scene/backdrop: modest official government reception hall, paneled wall and simple curtains, a pair of period cylindrical metal press microphones at the lower front; no contemporary equipment.
Flags are essential: a large Republic of Korea Taegeukgi and a period United States 48-star flag displayed SIDE BY SIDE directly behind the principal officials, lightly draped so both central designs are clearly visible. Taegeukgi geometry: white field, ordinary upright central taegeuk, exactly four black trigrams: upper-left three solid bars; upper-right broken/solid/broken; lower-left solid/broken/solid; lower-right three broken bars. American flag: rectangular canton containing six rows of eight stars and thirteen alternating stripes, not a 51-star design. No third flag.
Style/medium: black-and-white silver-gelatin press photograph, authentic mild film grain and soft archival contrast, crisp period wool fabrics, natural faces and credible human anatomy, sober documentary camera, no painterly brushwork.
Composition/framing: horizontal 3:2 landscape, eye-level mid-length press photo, principal group compact in the center 68 percent of width. Arrange flags just over shoulder level behind heads. The main faces, recognizable flag designs and folder presentation must all lie within the central 55 percent of height, leaving expendable ceiling and floor crop margins. Designed to crop independently to a near-square 210:176 country event and shallow 397:153 newspaper photo.
Mood: official and somewhat imposing, the formal start of an unequal political relationship. No battle, cheering masses, annexation map, conquest, humiliation, modern partisan campaign or military assault.
Constraints: anonymous fictional historical officials, no Donald Trump, no contemporary politician, no caricature, no readable writing on documents, no embedded title or caption, watermark, picture border, numbered state badge, modern clothing or digital microphones. Two countries retain their distinct flags and the Korean delegation remains visible.
```

#### 4. dominion_selected — flag correction and folder positioning edit

도구: `image_gen.imagegen (built-in)`. 참조: `C:/Users/jaewo/.codex/generated_images/01a1c9ad-e7d7-7250-bc9a-426b3a5c025e/exec-53277031-54f2-4dd6-ad87-98643179980f.png`, `C:/hoi/test/us-defense-sharing-20261111-01/art/photos/reference_KOR_democratic.png`, `C:/hoi/test/us-defense-sharing-20261111-01/art/photos/reference_USA_democratic.png`.

```text
Use case: precise-object-edit
Asset type: fictional black-and-white late-1930s diplomatic press photograph, prepared for a shallow newspaper picture.
Edit target: image 1, the standing American and Korean officials holding a plain document folder. Image 2 is an exact Korean flag geometry reference, image 3 is an exact period American flag geometry reference.
Make two tightly bounded corrections:
1. Correct both hanging flags to the reference designs. Taegeukgi must have upright taegeuk and exactly four trigrams: upper-left three solid, upper-right broken/solid/broken, lower-left solid/broken/solid, lower-right all broken. American flag must have thirteen stripes and exactly FORTY-EIGHT stars in SIX horizontal rows of EIGHT stars, in the canton only. Preserve monochrome cloth shading and natural gentle drape.
2. The two principal men now hold the SAME closed plain folder HIGHER, at mid-chest level, between them; bend their elbows naturally and preserve realistic hands. This brings the folder near the faces and flag symbols so the scene remains meaningful in a shallow horizontal newspaper crop.
Preserve every man's identity, facial expression, 1930s suit, positions, backgrounds, period microphones, camera framing, aspect ratio and archival grain. Keep aides secondary. No extra people, extra fingers, visible text, caption, number, watermark, poster border or modern item. This is a new fictional alternate-history scene, not a real photograph of a historical event.
```

## 국민정신 아이콘

2026-11-11 아이콘 담당이 `image_gen.imagegen (built-in)`으로 생성·편집한 네 채택본을 기록한다. 실제 모델명은 도구 결과에 노출되지 않았다. 그림과 국기 보정, 수입 모티프, 실제 강화 단계 I/II의 편집은 image_gen에서 수행했으며 이후에는 결정적 리사이즈/DDS 출력만 적용했다. 다른 모드의 아이콘·테두리·배경을 복사하지 않았다.

한국 「미국 방위비」 I/II는 밖으로 나가는 분리된 금화로 지출을 나타내고, 미국 「대한민국 방위비」 I/II는 안으로 향하는 화살표와 쌓인 금화로 수입을 나타낸다. 네 아이콘 모두 온전한 태극기와 성조기를 함께 포함한다. I/II는 같은 국가의 실제 기본→강화 정신 교체에 대응하며 서로 다른 국가를 단계로 취급한 것이 아니다.

민주 외교 가지의 짙은 청색 에나멜(참조색 `#355b7e`, RGB 53/91/126), 닳은 은색 테두리와 억제된 황동 장식을 사용했다. 이는 생성 시 참조한 팔레트이며 완성 그림 전체의 색상을 단일 값으로 고정하거나 전체 색조 필터로 바꿨다는 뜻이 아니다.

### 아이콘 채택 원본과 런타임 파일

네 채택 PNG는 각 1180×1333이며, 아래 실제 도구 출력의 프로젝트 보존본이다. 문서 병합 때 프로젝트 PNG와 실제 도구 파일의 SHA-256 일치를 다시 확인했다.

| 국민정신·대상·단계 | 채택 원본 | 실제 도구 출력 | 원본 SHA-256 |
|---|---|---|---|
| `HOK_KOR_us_defense_cost_sharing_1` / KOR / I | [PNG](assets/us-defense-sharing/generated/icons/HOK_KOR_us_defense_cost_sharing_1.png) | `C:/Users/jaewo/.codex/generated_images/01a1c9ae-2e46-72e3-9bd0-858baa1c9052/exec-b8db45f7-a512-4d7b-a908-ba51ab0f399a.png` | `E7F457B7B9CA1DEAB5FD3CD708356CF85B1974988ADB5018CEA27F3108D81226` |
| `HOK_KOR_us_defense_cost_sharing_2` / KOR / II | [PNG](assets/us-defense-sharing/generated/icons/HOK_KOR_us_defense_cost_sharing_2.png) | `C:/Users/jaewo/.codex/generated_images/01a1c9ae-2e46-72e3-9bd0-858baa1c9052/exec-8a2cc54f-78f3-414b-97b3-38ee2b24cb46.png` | `BB0FA453F4B6D09A1F813BE5A13D25393A52DCA62C48B70628DEE71CC35713E6` |
| `HOK_KOR_korean_defense_contribution_1` / USA / I | [PNG](assets/us-defense-sharing/generated/icons/HOK_KOR_korean_defense_contribution_1.png) | `C:/Users/jaewo/.codex/generated_images/01a1c9ae-2e46-72e3-9bd0-858baa1c9052/exec-1d5e831b-5d85-4549-a79c-a37d6bc1b722.png` | `72AEC05A4DEE0AE929C71BC730B7C0075D986CFC2D4BB0D7DB5D7B9B10A7C11F` |
| `HOK_KOR_korean_defense_contribution_2` / USA / II | [PNG](assets/us-defense-sharing/generated/icons/HOK_KOR_korean_defense_contribution_2.png) | `C:/Users/jaewo/.codex/generated_images/01a1c9ae-2e46-72e3-9bd0-858baa1c9052/exec-abf806da-e3f8-4a29-b684-69a66fa14a87.png` | `2D8F1E155158B0FE22C9E7BF6456C6CA48E04B1228F5EF68AB1C68511587AF49` |

원본을 자르지 않고 비율을 유지해 58×66 영역 안에 `HighQualityBicubic`으로 맞춘 뒤 60×68의 (1,1)에 배치했다. 가장자리 여백과 투명/부분 투명 알파를 보존했다. 출력은 비압축 BGRA32 DDS (`DDPF_RGB|DDPF_ALPHAPIXELS`), 1프레임, mipmap 없음, 각 16,448바이트다. 결정적 출력 helper는 `C:/hoi/test/us-defense-sharing-20261111-01/art/icons/export-icons.ps1`다.

| 국민정신·sprite | 런타임 파일 | 규격 | DDS SHA-256 |
|---|---|---|---|
| `GFX_idea_HOK_KOR_us_defense_cost_sharing_1` | [HOK_KOR_us_defense_cost_sharing_1.dds](../gfx/interface/ideas/HOK_KOR/us_defense/HOK_KOR_us_defense_cost_sharing_1.dds) | 60×68 | `2946E53D923C42DB60D333CE494495DA261C287C7ACF31CC9CB98B2D3D21DFFA` |
| `GFX_idea_HOK_KOR_us_defense_cost_sharing_2` | [HOK_KOR_us_defense_cost_sharing_2.dds](../gfx/interface/ideas/HOK_KOR/us_defense/HOK_KOR_us_defense_cost_sharing_2.dds) | 60×68 | `CBFF7B3B7C07C76137673948DABC575F5DE33FF66A03D19FEE1E1D097EA14AF6` |
| `GFX_idea_HOK_KOR_korean_defense_contribution_1` | [HOK_KOR_korean_defense_contribution_1.dds](../gfx/interface/ideas/HOK_KOR/us_defense/HOK_KOR_korean_defense_contribution_1.dds) | 60×68 | `3D840300F6FE23C8585DC3A68842460F7E92F836EF68870EDE5A4A3F5B74F391` |
| `GFX_idea_HOK_KOR_korean_defense_contribution_2` | [HOK_KOR_korean_defense_contribution_2.dds](../gfx/interface/ideas/HOK_KOR/us_defense/HOK_KOR_korean_defense_contribution_2.dds) | 60×68 | `188A7AC2840354F33382B9FC2AF39F0D0B913F8BC09CF070090A60371EF358DE` |

[GFX 정의](../interface/HOK_KOR_us_defense_ideas.gfx)는 위 네 프로젝트 내부 DDS를 상대 경로로 연결한다. GFX SHA-256은 `039199D12B6F67D2E4DD05A37532F6C23A38FE169997159B99D62426141BD0A6`이다. 각 파일의 알파 픽셀 개수(완전 투명/완전 불투명/부분 투명)는 다음과 같다.

| 아이콘 | 투명 | 불투명 | 부분 투명 |
|---|---|---|---|
| `HOK_KOR_us_defense_cost_sharing_1` | 1223 | 189 | 2668 |
| `HOK_KOR_us_defense_cost_sharing_2` | 1218 | 184 | 2678 |
| `HOK_KOR_korean_defense_contribution_1` | 1209 | 185 | 2686 |
| `HOK_KOR_korean_defense_contribution_2` | 1193 | 194 | 2693 |

### 아이콘 국기 참조와 생성 이력

국기 형태 참조는 사진 부분에 기록한 동일한 프로젝트 태극기와 설치본 미국 48성기다. 아이콘의 도구 입력 PNG는 [태극기](assets/us-defense-sharing/generated/icons/references/KOR_democratic.png) (`AF6790C595BF232218520349DD5716A1553C07A55EF0B6A342109E234AE96818`)와 [성조기](assets/us-defense-sharing/generated/icons/references/USA_democratic.png) (`4E1BD6BD5E1DED80E34683C2993C1FFF998C701E9FF0711E2B80A4C50492FB7C`)다. 두 입력은 사진에 보존한 PNG와 각각 해시가 같으며, 동일한 원본 TGA·권리/출처 구분을 따른다. 별도 공개 소재 팩을 사용하거나 국기 원저작권을 새로 주장하지 않는다.

최초 한국 지출/미국 수입 시안은 성조기 별이 42개로 생성되어 탈락했다. 국기 보정 뒤 한국 I를 채택했고, 이를 바탕으로 한국 II와 미국 수입 I/II를 만들었다. 미국 수입 첫 보정 시도 역시 별 개수가 유지되어 탈락했다. 아래 프롬프트 이력은 제작 근거이며, 탈락 시안은 통합 manifest의 채택 원본·런타임 자산 수에 포함하지 않는다.

아이콘 담당 기록에서는 네 채택 원본의 태극·사괘, 성조기 6×8=48개 별과 13개 줄무늬, 양국 국기 전체, 지출/수입 및 I/II를 육안 확인했다. 60×68 실제 크기와 2배 미리보기를 `#202326` 배경에서 함께 확인했으며, DDS를 해독한 픽셀은 검수 PNG와 일치했다. 문서 병합 때 원본/실제 도구 파일과 DDS의 해시·규격도 다시 대조했다. 이 기록은 정적 자산 검사이며 실제 게임의 국민정신 창·툴팁 표시 검증을 대신하지 않는다.

외부 제작 manifest는 `C:/hoi/test/us-defense-sharing-20261111-01/art/icons/manifest.json`, 정적 검사 증거는 `C:/hoi/test/us-defense-sharing-20261111-01/art/icons/static-verification.json`, 실제 크기 미리보기는 `C:/hoi/test/us-defense-sharing-20261111-01/art/icons/actual-size-preview.png`다. 후속 작업이 외부 경로만 의존하지 않도록 아래 프롬프트 전문과 [프로젝트 통합 자산 manifest](data/HOK_KOREAN_US_DEFENSE_ASSET_MANIFEST.json)에 원본·출처·해시·가공을 함께 보존했다. 통합 manifest의 인벤토리는 선택한 사진 원본 2개+아이콘 원본 4개, 런타임 사진 4개+아이콘 4개다.

### 아이콘 생성·편집 프롬프트 전문

#### 아이콘 1. exec-a246c251-6977-4f0f-b1d6-edae1a303c68.png — 미채택

도구: `image_gen.imagegen (built-in)`. 날짜: 2026-11-11. 방식: `generate`. 모델: 도구 결과에 노출되지 않음.
실제 출력: `C:/Users/jaewo/.codex/generated_images/01a1c9ae-2e46-72e3-9bd0-858baa1c9052/exec-a246c251-6977-4f0f-b1d6-edae1a303c68.png`.
참조: `C:/hoi/test/us-defense-sharing-20261111-01/art/icons/KOR_democratic.png`, `C:/hoi/test/us-defense-sharing-20261111-01/art/icons/USA_democratic.png`.
미채택 근거: Rejected: US canton has 42 rather than 48 stars.

```text
Use case: stylized-concept. Asset type: Hearts of Iron IV national-spirit icon, one isolated small military-diplomatic enamel badge.
Create ONE compact shield badge for South Korea's payments of US defense costs. Hand-painted 1930s-1950s grand-strategy game UI art, worn silver and subdued brass ornament, muted deep-blue shield enamel (reference blue #355b7e). On a TRUE TRANSPARENT background, no square backdrop or checkerboard. Badge centered with 6% transparent margin; the entire ornament must remain inside frame. It will be downsampled to 60x68 pixels, so bold simple silhouettes, crisp high contrast, no thin clutter.
At the upper half, two broad nearly-flat miniature flags, South Korean Taegeukgi left and US flag right, equally prominent and readable. Image1 and Image2 are ONLY flag accuracy references, not compositions to reproduce. Preserve their symbols precisely: white Korean flag, red-over-blue circular taegeuk and four black trigrams with correct broken/solid bars; US flag blue canton at upper-left, 13 alternating red-white stripes, 48 white stars suitable for period. Keep whole flag rectangles visible.
At lower center a short parchment treaty scroll and three clearly separated gold coins flowing OUTWARD to the right along a small broad outward arrow, representing Korea paying defense expenses. The coins and treaty form one legible motif below flags, without covering flags. A tiny dark metal plate at bottom displays just Roman numeral "I" in light silver. No other text, letters, logos, numbers, percentages, title or watermark. Metallic relief, painterly shading matching HOI4 national spirits, restrained realism, no cartoon, no modern glossy app style. One single badge, not a sheet, no duplicates.
```

#### 아이콘 2. exec-4ccd6927-0ae0-42f2-8671-2038b2a82e17.png — 미채택

도구: `image_gen.imagegen (built-in)`. 날짜: 2026-11-11. 방식: `generate`. 모델: 도구 결과에 노출되지 않음.
실제 출력: `C:/Users/jaewo/.codex/generated_images/01a1c9ae-2e46-72e3-9bd0-858baa1c9052/exec-4ccd6927-0ae0-42f2-8671-2038b2a82e17.png`.
참조: `C:/Users/jaewo/.codex/generated_images/01a1c9ae-2e46-72e3-9bd0-858baa1c9052/exec-a246c251-6977-4f0f-b1d6-edae1a303c68.png`, `C:/hoi/test/us-defense-sharing-20261111-01/art/icons/KOR_democratic.png`, `C:/hoi/test/us-defense-sharing-20261111-01/art/icons/USA_democratic.png`.
미채택 근거: Rejected: US canton has 42 rather than 48 stars.

```text
Use case: stylized-concept. Generate ONE new HOI4 national-spirit icon for the United States receiving South Korean defense contributions. Image1 is a style/composition reference ONLY: keep its compact muted deep blue enamel shield (#355b7e family), worn silver rim, brass leaves, top star, two equal broad flags and tiny bottom Roman-numeral plate. Image2 Korean flag and Image3 US flag are SYMBOL ACCURACY references: reproduce the exact trigrams, taegeuk and 48-star/13-stripe pattern, not invented marks. Korean flag on left, US flag on right, whole flat flag rectangles visible and readable.
Change lower central theme to INCOME: treaty parchment on left, broad gold arrow points INWARD from the left toward one small solid stack of gold coins at right (receiving contribution), unlike outflow coins. Simple bold uncluttered motif for actual 60x68 UI. Bottom plate just "I".
Hand-painted 1930s-1950s grand-strategy game badge, restrained metallic relief, crisp silhouettes. TRUE TRANSPARENT background with 6% transparent margin, complete ornament fully inside frame. One badge only. No text besides Roman "I", no title, no watermark, no square backdrop, no checkerboard. Preserve South Korean flag red-over-blue taegeuk with EXACT top-left three solid, top-right broken/solid/broken, bottom-left solid/broken/solid, bottom-right three broken trigrams; keep symbols black. US flag EXACT 48 stars in 6 rows of 8 and 13 horizontal red-white stripes starting/ending red, upper-left blue canton.
```

#### 아이콘 3. HOK_KOR_us_defense_cost_sharing_1 — 채택

도구: `image_gen.imagegen (built-in)`. 날짜: 2026-11-11. 방식: `edit`. 모델: 도구 결과에 노출되지 않음.
실제 출력: `C:/Users/jaewo/.codex/generated_images/01a1c9ae-2e46-72e3-9bd0-858baa1c9052/exec-b8db45f7-a512-4d7b-a908-ba51ab0f399a.png`.
참조: `C:/Users/jaewo/.codex/generated_images/01a1c9ae-2e46-72e3-9bd0-858baa1c9052/exec-a246c251-6977-4f0f-b1d6-edae1a303c68.png`, `C:/hoi/test/us-defense-sharing-20261111-01/art/icons/KOR_democratic.png`, `C:/hoi/test/us-defense-sharing-20261111-01/art/icons/USA_democratic.png`.

```text
Use case: precise-object-edit. EDIT target Image1 only. Keep the entire badge, shape, blue background, parchment, flowing coins, arrow, numeral I, metal frame, all positions and transparent alpha EXACTLY unchanged.
Correct ONLY the miniature US flag in its existing rectangle. The previous flag erroneously has 7 columns and 6 rows =42 stars. Replace its star field by EXACTLY EIGHT columns and SIX straight rows =48 white stars, all aligned, with eight stars on every row. Visually count them. Make the blue canton a little wider within the same flag rectangle if needed to fit eight stars. US flag has exactly THIRTEEN red and white horizontal stripes, seven red and six white, beginning and ending red. Image3 is exact flag pattern reference. Do not make a modern staggered 50-star field.
Also ensure Korean trigrams MATCH Image2 precisely: top-left three solid, top-right broken-solid-broken, bottom-left solid-broken-solid, bottom-right all three broken. Keep taegeuk red upper half and blue lower half. Preserve white field and placement.
Return ONE same badge, transparent outside. No added graphics or text.
```

#### 아이콘 4. HOK_KOR_us_defense_cost_sharing_2 — 채택

도구: `image_gen.imagegen (built-in)`. 날짜: 2026-11-11. 방식: `edit`. 모델: 도구 결과에 노출되지 않음.
실제 출력: `C:/Users/jaewo/.codex/generated_images/01a1c9ae-2e46-72e3-9bd0-858baa1c9052/exec-8a2cc54f-78f3-414b-97b3-38ee2b24cb46.png`.
참조: `C:/Users/jaewo/.codex/generated_images/01a1c9ae-2e46-72e3-9bd0-858baa1c9052/exec-b8db45f7-a512-4d7b-a908-ba51ab0f399a.png`.

```text
Use case: precise-object-edit. Image1 is the ONLY edit target. Change ONLY the bottom metal plate's Roman numeral from "I" to "II", centered in the identical plate. This is the tier-II upgrade of exactly the same HOI4 national-spirit icon. Preserve every other detail: outline, canvas proportions, transparent background and alpha, blue enamel, metal rim, gold leaves, star, parchment, three outward-moving gold coins and arrow, entire positions and sizes. Preserve BOTH flags precisely, including South Korean red-over-blue taegeuk and four trigrams, and the historical US flag's 48 stars arranged 6 rows of 8 with exactly 13 red-white stripes. Do not redraw their patterns or add/remove stars. No other changes, no new text or objects. Return one badge on true transparent background.
```

#### 아이콘 5. exec-a8a1b67a-7bf2-4e19-beee-b3552f248129.png — 미채택

도구: `image_gen.imagegen (built-in)`. 날짜: 2026-11-11. 방식: `edit`. 모델: 도구 결과에 노출되지 않음.
실제 출력: `C:/Users/jaewo/.codex/generated_images/01a1c9ae-2e46-72e3-9bd0-858baa1c9052/exec-a8a1b67a-7bf2-4e19-beee-b3552f248129.png`.
참조: `C:/Users/jaewo/.codex/generated_images/01a1c9ae-2e46-72e3-9bd0-858baa1c9052/exec-4ccd6927-0ae0-42f2-8671-2038b2a82e17.png`, `C:/Users/jaewo/.codex/generated_images/01a1c9ae-2e46-72e3-9bd0-858baa1c9052/exec-b8db45f7-a512-4d7b-a908-ba51ab0f399a.png`.
미채택 근거: Rejected: flag correction failed to change star count.

```text
Use case: precise-object-edit. EDIT target Image1 only. Keep the whole badge, shield outline, canvas, blue enamel, metal frame, gold leaves, parchment, inward arrow, receiving coin stack, numeral I and transparent alpha unchanged.
Correct ONLY the US flag star field in its existing rectangle: the previous flag wrongly has 7 columns x6 rows =42 stars. It must have EXACTLY EIGHT aligned columns and SIX straight rows =48 stars. Eight white stars on EVERY row, six rows, historical 48-state flag. Count them. Image2's flag panel already has the correct 8x6 layout; match this exact layout. Keep exactly THIRTEEN horizontal alternating red and white stripes, starting and ending red, with upper-left blue canton. Do not make a modern staggered star field.
Keep both complete flags, correct Korean red-over-blue taegeuk and four trigrams (top-left3solid, top-rightbroken-solid-broken, bottom-leftsolid-broken-solid,bottom-right3broken). Only one badge, true transparency outside, no new objects/text.
```

#### 아이콘 6. HOK_KOR_korean_defense_contribution_1 — 채택

도구: `image_gen.imagegen (built-in)`. 날짜: 2026-11-11. 방식: `edit`. 모델: 도구 결과에 노출되지 않음.
실제 출력: `C:/Users/jaewo/.codex/generated_images/01a1c9ae-2e46-72e3-9bd0-858baa1c9052/exec-1d5e831b-5d85-4549-a79c-a37d6bc1b722.png`.
참조: `C:/Users/jaewo/.codex/generated_images/01a1c9ae-2e46-72e3-9bd0-858baa1c9052/exec-b8db45f7-a512-4d7b-a908-ba51ab0f399a.png`.

```text
Use case: precise-object-edit. EDIT Image1, a complete HOI4 national spirit badge. Preserve EVERYTHING in upper half exactly pixel-faithfully: silver shield top and gold star, blue enamel, both framed flag rectangles, Korean taegeuk and trigrams, and especially the US flag with EIGHT stars per row in SIX rows (48 total) and 13 stripes. Keep the whole badge frame, leaves, bottom Roman "I" plaque, transparent background, and overall proportions.
Change ONLY the gold coins-and-arrow motif in the lower middle: replace the three separate coins flowing out with ONE stack of 3 gold coins on the right, and move a simple gold arrow so it flows from the parchment on left INTO that coin stack on right. This means contribution RECEIPTS for the United States, not spending. Keep parchment's existing position and scale.
Do not change flags, do not respace any stars. One badge, no other text, original true transparency outside.
```

#### 아이콘 7. HOK_KOR_korean_defense_contribution_2 — 채택

도구: `image_gen.imagegen (built-in)`. 날짜: 2026-11-11. 방식: `edit`. 모델: 도구 결과에 노출되지 않음.
실제 출력: `C:/Users/jaewo/.codex/generated_images/01a1c9ae-2e46-72e3-9bd0-858baa1c9052/exec-abf806da-e3f8-4a29-b684-69a66fa14a87.png`.
참조: `C:/Users/jaewo/.codex/generated_images/01a1c9ae-2e46-72e3-9bd0-858baa1c9052/exec-1d5e831b-5d85-4549-a79c-a37d6bc1b722.png`.

```text
Use case: precise-object-edit. Image1 is the ONLY edit target. Change ONLY the bottom metal plaque's Roman numeral from "I" to "II", centered inside the same plate. Tier-II upgrade of exactly the same HOI4 national-spirit badge. All other pixels/positions should remain unchanged: blue shield, worn silver rim, gold star/leaves, treaty scroll, inward gold arrow and received gold coin stack, canvas proportions, and TRUE transparent background. Preserve BOTH flags exactly: Taegeukgi's red-over-blue taegeuk and all four trigrams; the historical US flag's EXACTLY EIGHT white stars on each of SIX straight rows =48, 13 red/white stripes starting/ending red. Do not redraw flags, do not change stars or stripes. No other edits, no new objects or text, one badge only.
```
