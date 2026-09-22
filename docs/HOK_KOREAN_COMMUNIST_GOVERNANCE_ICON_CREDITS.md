# 공산주의 내정 후속 중점·국민정신 아이콘 출처

2026-09-22. 대상은 노농 협의·사회협약(Y1) 중점 4개, 국가 생산계획(P1) 중점 5개와 두 정신 계열의 I·II 4개다. 작업 기준은 `feat/korean-focus-expansion-ai` / `d8558937db1e9c984a16e75eed35d5a6f8914bb2`이며, 시작 당시 작업 트리는 깨끗했다. 이번 이미지 작업은 기존 60개·29개 및 앞선 Y2/P2 10개·8개 이미지를 바꾸지 않았다.

**제작 방식은 허용된 공개 PNG 부품의 재사용·새 합성과 간단한 계속개발 제작 도형의 결합**이다. AI 생성 이미지는 사용하지 않았다. 원본 부품의 원화를 계속개발 팀이 새로 그렸다고 표시하지 않는다. ID, 스프라이트, 실제 이미지 경로, 원본 해시, 레이어 레시피, 팔레트와 최종 해시는 [전용 매니페스트](data/HOK_KOREAN_COMMUNIST_GOVERNANCE_ICON_MANIFEST.json)에 기록했다.

## 원본·허용 범위·기여자

원본은 [Globvs / Ultimate HOI4 GFX](https://github.com/Globvs/Ultimate-HOI4-GFX)의 고정 커밋 `3626dc83c8573d6603fa497138090b04b64a15ba`다. 이번에 채택한 14개 PNG는 이미 프로젝트의 `.local-artifacts/korean-focus-icons/sources/Ultimate-HOI4-GFX/`에 보존되어 있었다. 원본 파일을 고치거나 새로 다운로드하지 않고, 기존 source-manifest의 해시와 일치하는지 확인해 사용했다.

[해당 커밋의 CREDITS.txt](https://github.com/Globvs/Ultimate-HOI4-GFX/blob/3626dc83c8573d6603fa497138090b04b64a15ba/CREDITS.txt)는 기여자 동의와 자유로운 사용을 명시한다. [바이트 보존본](assets/korean-focus-icons/UPSTREAM_CREDITS.txt)의 SHA-256은 `cf220dc66463d75163f7690ad77b02b662d0c05ca5d53dc62d33ed504512a7f5`다. 이 근거는 **해당 팩의 채택 파일**에만 적용하며 기여자가 참여한 다른 모드 전체로 확대하지 않는다. 별도의 MIT·CC 라이선스를 추정하거나 개별 제작자 허가를 새로 받았다고 주장하지 않는다.

원본의 기여 표시는 **Globvs / Ultimate HOI4 GFX contributors**다. upstream은 개별 파일별 작가를 연결하지 않으므로 파일별 원저자는 미상이다. 전체 CREDITS의 이름은 Globvs, HOI4 GFX Modding Database, ThePinkPanzer, Gunnar von Pontius, Pacifica, That Guy Called Curly, Deathlinger, Edouard_Saladier, scarecroww, joshyflip, Indycyclone77, grestin, AtomicSoviet이다. 이들이 이번 모든 파일을 공동 제작했다고 뜻하지 않는다. AtomicSoviet의 제공 경위에 The New Order가 기재되어 있어도 그 모드의 다른 그림은 채택하지 않았다.

| 채택 파일 | 사용 내용 |
|---|---|
| `Focus Backgrounds/Circle with Ribbon2.png` | 중점 금속 테두리와 배경 |
| `National Spirit Backgrounds/Circle.png` | 국민정신 원형 배경 |
| `Focus & National Spirits Pieces/Hammer.png` | 실제 그림은 의사봉이며 협의대회에 사용 |
| `Focus & National Spirits Pieces/Wheat2.png` | 노농 협의·협약의 곡식 |
| `Focus & National Spirits Pieces/Cog Wheel.png` | 산업 조정·생산계획·설비 점검 |
| `Focus & National Spirits Pieces/Scales.png` | 산업분쟁 조정의 저울 |
| `Focus & National Spirits Pieces/Paper.png` | 지역 문서·협약 서류 |
| `Focus & National Spirits Pieces/Paper Sign.png` | 서명·지역 협의 문서 |
| `Focus & National Spirits Pieces/Hands Shaking.png` | 노농 협약 |
| `Focus & National Spirits Pieces/Factories2.png` | 자산·생산계획의 공장 |
| `Focus & National Spirits Pieces/Book.png` | 국유자산 장부 |
| `Focus & National Spirits Pieces/Book Open.png` | 물자수급 대조 장부 |
| `Focus & National Spirits Pieces/Steel.png` | 조정 대상인 강재 |
| `Focus & National Spirits Pieces/Circular Arrows.png` | 생산계획의 순환 배정 |

## 계속개발 제작·합성

계속개발 **kpopmodder**의 기여는 정책별 소재 선정·배치, 비율을 유지한 크기 조정, 배경만의 색상 가공, DDS 변환과 다음 도형 제작이다. 기존 `IconRenderer.cs`와 `BackgroundColors.cs`는 변경 없이 재사용했다. 새 도형의 소스는 `.local-artifacts/korean-communist-governance-icons/GovernanceMarks.cs`이며, 실제 사용 레시피는 같은 작업 폴더의 `build-icons.ps1`에 남겼다.

| 중점 | 새 구성과 직접 제작 부분 |
|---|---|
| 노농 협의대회 | 의사봉·곡식 아래에 직접 제작한 청동·갈색 타원형 원탁 |
| 산업분쟁 조정위원회 | 저울을 앞에 두고 톱니바퀴·곡식을 배치 |
| 지방협의회 정례화 | 세 지역 문서 사이에 직접 제작한 연결선 |
| 노농 협약 정착 | 협약 서류·악수·곡식. 앞선 협동조합 연합의 좌우 대칭 곡식 구성과 구분 |
| 국유자산 실태조사 | 자산 장부 앞, 공장 뒤의 상하 배치 |
| 연간 생산계획 | 직접 제작한 달력·금속 고리·12칸 표시와 생산 톱니바퀴 |
| 물자수급 대조표 | 펼친 수급 장부와 강재 |
| 생산능력 정기점검 | 큰 톱니바퀴에 기존 계속개발 방식의 검사 확인표를 추가 |
| 국가 생산계획 조정 | 공장을 감싸는 순환 배정 화살표 |

국민정신 `yeo_social_compact_1/2`는 악수와 곡식, `pak_output_plan_1/2`는 공장과 순환 화살표를 공유한다. 작은 표시 크기에 맞춰 정신에서는 서류 등 보조 요소를 줄였다. 모듈의 중간 중점은 각각 조정의 절차·연간 일정을, 최종 중점과 정신은 정착된 협약·생산계획을 나타낸다. **I·II는 실제 교체되는 정신에만 표시**하며 중점에는 단계를 붙이지 않았다. 단계 쌍의 중앙 그림·색상·테두리는 동일하다.

## 팔레트·형식·프로젝트 내부 연결

이 두 정치 가지의 배경은 공산 계열 짙은 적색 **RGB (116,45,48)**이다. 국가의 현재 집권 이념에 따라 이미지가 바뀌는 로직은 없다. 원본 배경 레이어의 적색 원판 픽셀만 선택하고 `pow(luminance/60,0.9)`로 기존 명암을 살렸다. 중앙 부품·금속 테두리·단계 표시에 전체 색 필터를 씌우지 않았으며 알파를 유지했다. 정확한 선택식과 생성 배경·마스크 해시는 매니페스트를 따른다.

- 중점: 100×88, BGRA32 DDS, 단일 프레임, `gfx/interface/goals/HOK_KOR/communist_governance/`.
- 국민정신: 60×68, 같은 형식, `gfx/interface/ideas/HOK_KOR/communist_governance/`.
- 일반·정신·결정 스프라이트: `interface/HOK_KOR_communist_governance_icons.gfx`.
- 중점 광택: `interface/HOK_KOR_communist_governance_icons_shine.gfx`. 마스크는 해당 중점의 내부 DDS다.
- 최초 구현에서는 결정 4개와 카테고리 1개가 관련 100×88 중점 DDS를 직접 재사용했다. 사용자 화면의 겹침 문제를 수정한 2026-09-22 후속 작업에서는 같은 중심 소재를 작은 원판에 다시 구성하여 **카테고리 51×40, 결정 32×32의 전용 DDS 5개**를 `gfx/interface/decisions/HOK_KOR/communist_governance/`에 저장했다. 협의대회·산업분쟁 조정·지방협의회·수급 대조표·정기점검과의 소재 관계는 유지하되, 중점용 큰 리본·월계 장식과 단계 배지는 쓰지 않는다. 기존 스프라이트 이름과 중점·정신 DDS는 유지했다. 새 구성·해시는 [소형 아이콘 매니페스트](data/HOK_KOREAN_SMALL_DECISION_ICON_MANIFEST.json), UI 규격과 검증 한계는 [수정 기록](incidents/2026-09-22-korean-decision-icon-size.md)을 따른다.

광택 오버레이는 기존 프로젝트 파일 `gfx/interface/goals/HOK_KOR/shine_overlay.dds`를 공유한다. 원본은 **Paradox Interactive의 HOI4 1.19.3** `gfx/interface/goals/shine_overlay.dds`이며 SHA-256은 `bb416649358c73d34aacd46bad61bc44211fac8111627b56e25f385ad98f4448`이다. 이번 작업에서 복사하거나 수정하지 않았다. 이는 HOI4 모드에서 재사용하는 바닐라 자산으로, 공개 팩 CREDITS의 허가에 포함시키지 않는다.

## 검수와 한계

[실제 크기 접촉표](assets/korean-communist-governance-icons/contact-sheet.png)에서 9개 중점의 소재·적색 원판·금속 테두리와 4개 정신의 I·II를 확인했다. 배경 마스크 밖의 변경·알파 변경은 0이며, 두 정신 단계 쌍의 차이는 배지 영역으로 한정된다. DDS의 크기·BGRA 채널 마스크·알파·파일 길이·최종 해시와 스프라이트/프로젝트 내부 경로를 점검했다. 이전 로컬 runtime DDS의 해시는 별도 기준선과 대조한다. 결과는 `.local-artifacts/korean-communist-governance-icons/validation.json`에 남긴다.

이 정적 점검은 실제 게임 로더·잠김/선택 가능/진행/완료/광택 상태, 정신 툴팁과 교체 이후, 결정·카테고리 표시 크기의 검증을 뜻하지 않는다. 이미지 담당자는 게임을 실행하지 않았으며 해당 소묶음의 런타임 결과는 root 실행 기록을 따른다. 로직·보상·좌표·현지화·기존 이미지·게임 설정·Git 변경은 이 이미지 작업에서 수행하지 않았다.
