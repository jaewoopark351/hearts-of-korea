# 파시즘 군수조달 아이콘 출처

2026-09-22. 군수조달 F1 중점 4개, 연결 국민정신 I·II 2개, 결정 2개와 사업 범주 1개를 위한 신규 DDS 9개다. 기준은 `feat/korean-focus-expansion-ai` / `691ffa37740237feddf0b44fc68cfa47b10d76bf`이며 작업 시작 시 작업 트리는 깨끗했다. 기존 이미지·GFX·매니페스트와 게임플레이 코드는 이 이미지 작업에서 수정하지 않는다.

제작 방법은 **허용된 로컬 PNG 부품 재사용·새 합성 및 직접 제작한 클립보드와 연결선**이다. AI 생성·새 다운로드·도구 설치는 하지 않았다. ID, 스프라이트, 레이어 좌표, 소재별 원본 및 최종 해시와 가공법은 [전용 매니페스트](data/HOK_KOREAN_FASCIST_PROCUREMENT_ICON_MANIFEST.json)에 기록한다.

## 원본과 재사용 근거

[Globvs / Ultimate HOI4 GFX](https://github.com/Globvs/Ultimate-HOI4-GFX)의 고정 커밋 `3626dc83c8573d6603fa497138090b04b64a15ba`에서 이미 프로젝트 내부 `.local-artifacts/korean-focus-icons/sources/Ultimate-HOI4-GFX/`에 보존된 PNG 10개를 사용했다. 모든 원본은 기존 source-manifest의 SHA-256과 대조했다.

[고정 커밋 CREDITS.txt](https://github.com/Globvs/Ultimate-HOI4-GFX/blob/3626dc83c8573d6603fa497138090b04b64a15ba/CREDITS.txt)는 기여자 동의와 자유로운 사용을 명시한다. [원문 보존본](assets/korean-focus-icons/UPSTREAM_CREDITS.txt) SHA-256은 `cf220dc66463d75163f7690ad77b02b662d0c05ca5d53dc62d33ed504512a7f5`다. 이번 사용 근거는 선택한 팩 파일에만 한정한다. 기여자의 다른 작품·모드 전체에 대한 허가나 별도 MIT·CC 라이선스를 추정하지 않는다.

원 기여 표시는 **Globvs / Ultimate HOI4 GFX contributors**다. 개별 파일과 작가를 대응하는 upstream 정보가 없어 파일별 원저자는 미상이다. 원문 명단은 Globvs, HOI4 GFX Modding Database, ThePinkPanzer, Gunnar von Pontius, Pacifica, That Guy Called Curly, Deathlinger, Edouard_Saladier, scarecroww, joshyflip, Indycyclone77, grestin, AtomicSoviet이다. 이 명단의 모두를 각 파일의 공동 작가라고 단정하지 않는다. CREDITS의 The New Order 언급을 그 모드의 다른 그림에 대한 허가로 확대하지 않는다.

배경 원본은 `Focus Backgrounds/Circle with Ribbon2.png`, `National Spirit Backgrounds/Circle.png`다. 중앙 부품은 `Focus & National Spirits Pieces/`의 `Paper.png`, `Paper Sign.png`, `Book.png`, `Magnifying Glass.png`, `Crate.png`, `Clock.png`, `Factories2.png`, `Steel.png`다. 원본 접촉표로 서명 손, 장부, 화물상자, 시계, 공장, 강철 주괴의 실제 그림을 확인했다.

## 정책별 구성

| 대상 | 소재와 의미 |
|---|---|
| 군수조달 실무정비 | 직접 제작한 클립보드·금속 집게, 계약 서류와 서명 손 |
| 군수계약 원가심사 | 원가 장부와 확대경 |
| 군수 납기 조정 | 화물상자와 납기 시계 |
| 통합 군수계약 체계 | 공장·서명 계약서와 직접 제작 연결선 |
| 군수계약 감독 I·II | 같은 공장·서명 계약 소재를 60×68로 다시 구성하고 실제 단계 배지 적용 |
| 긴급 군수납품 결정 | 납기 중점과 연결되는 화물상자·시계, 전용 32×32 |
| 원자재 계약조정 결정 | 계약 서류와 강철 주괴, 전용 32×32 |
| 구국군 군수계약 사업 범주 | 공장·계약 소재, 전용 51×40 |

계속개발 **kpopmodder**의 기여는 소재 선정, 각 크기별 새 구성, 배경색 가공, 직접 제작한 클립보드와 연결선, DDS 변환 및 통합이다. 원래 부품의 그림을 계속개발 팀의 새 원화로 표시하지 않는다. 기존 `IconRenderer.cs`·`BackgroundColors.cs`를 수정 없이 사용했고 새 도형과 전체 재현 스크립트는 `.local-artifacts/korean-fascist-procurement-icons/ProcurementMarks.cs` 및 `build-icons.ps1`에 보존했다.

## 색상·형식·참조

파시즘 가지의 **차콜·갈색 RGB(70,60,48)**을 배경 원판에만 적용했다. 원판의 기존 명암을 유지하고 금속 테두리·월계·중앙 부품·알파에는 색 필터를 적용하지 않는다. 밝은 금속 테두리와 계약·화물 소재가 어두운 게임 화면에서 구별을 돕는다. 색은 이 정치 가지에 고정되며 집권 이념에 따라 바뀌지 않는다. 선택 마스크와 파생 배경 해시를 매니페스트에 보존했다.

- 중점: `gfx/interface/goals/HOK_KOR/fascist_procurement/`, 100×88.
- 국민정신: `gfx/interface/ideas/HOK_KOR/fascist_procurement/`, 60×68. 실제 강화 I·II만 표시.
- 결정·범주: `gfx/interface/decisions/HOK_KOR/fascist_procurement/`, 각각 32×32와 51×40. 월계·리본 없이 금속 원판과 중심 소재를 작게 다시 구성했다.
- `interface/HOK_KOR_fascist_procurement_icons.gfx`의 일반 스프라이트 9개와 `_shine.gfx`의 광택 4개는 모두 내부 상대 경로를 사용한다.

각 출력은 알파가 있는 BGRA32 DDS 단일 프레임이다. 기존 동종 프로젝트 DDS의 128바이트 헤더를 그대로 사용했다. 중점은 mipmapCount 1·행 피치, 정신은 mipmapCount 0·전체 선형 크기, 결정·범주는 mipmapCount 0·행 피치를 유지한다. 실제 페이로드는 모두 기본 해상도 한 장이며 추가 축소 밉맵 레벨은 없다. 전용 소형 그림은 HOI4 1.19.3의 검증된 목록·범주 기준을 따른다: 일반 행 높이 41·아이콘 중심(30,19)·제목 x63, 기간제 행 높이 40·중심(32,20)·제목 x62, 범주 높이 58·좌상단(10,16)·제목 x74. [기존 크기 수정 기록](incidents/2026-09-22-korean-decision-icon-size.md)을 참조한다.

광택은 기존 내부 파일 `gfx/interface/goals/HOK_KOR/shine_overlay.dds`를 공유한다. 원본은 **Paradox Interactive / HOI4 1.19.3**의 `gfx/interface/goals/shine_overlay.dds`이며 SHA-256은 `bb416649358c73d34aacd46bad61bc44211fac8111627b56e25f385ad98f4448`이다. 이번에 복사·수정하지 않았다. 바닐라의 모드용 재사용 자산이며 공개 PNG 팩의 CREDITS 허가와 구분한다.

## 검수 범위

[실제 크기 접촉표](assets/korean-fascist-procurement-icons/contact-sheet.png)는 확대하지 않은 9개 DDS의 모습이다. 계약·원가·납기·통합 계약 구분, 정신 I·II, 작은 결정과 범주의 소재·테두리·여백을 정적으로 확인했다. 게임 화면으로 표시하거나 주장하지 않는다.

DDS 크기·헤더·채널·알파·해시, 스프라이트 중복·존재·내부 상대 경로와 정확한 대소문자, 광택 오버레이, 배경 마스크 밖 픽셀·알파 보존, I·II 배지 밖 불변, 원본 PNG/CREDITS와 기존 runtime DDS 불변을 점검한다. 결과는 `.local-artifacts/korean-fascist-procurement-icons/validation.json`에 보존한다. 이미지 담당자는 게임을 실행하지 않았다. 잠김·진행·완료·광택·정신 교체·결정 목록/진행 표시는 root의 별도 런타임 기록을 따라야 한다.
