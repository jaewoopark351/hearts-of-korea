# 공산주의 농촌 기술보급·계획행정 아이콘 출처

2026-09-22. 대상은 여운형 농촌 기술보급(Y3) 중점 5개, 박헌영 계획행정(P3) 중점 4개, 연결된 국민정신 I·II 4개, 기간제 결정 4개의 전용 소형 이미지다. 기준은 `feat/korean-focus-expansion-ai` / `b300b4090b4a779878332c7ec463170bbe16f4d8`이며 작업 시작 당시 작업 트리는 깨끗했다. 기존 이미지와 기존 GFX·매니페스트는 이 작업에서 수정하지 않는다.

새 17개 DDS는 **허용된 로컬 PNG 부품의 재사용·새 합성 및 계속개발 제작 도형**을 결합했다. AI 생성·신규 다운로드·도구 설치는 하지 않았다. 실제 ID·그림·스프라이트·소재별 출처와 원본/최종 해시, 완전한 레이어 배치와 도형 레시피는 [전용 매니페스트](data/HOK_KOREAN_COMMUNIST_DEVELOPMENT_ICON_MANIFEST.json)에 기록한다.

## 원본과 사용 근거

원본 소재는 [Globvs / Ultimate HOI4 GFX](https://github.com/Globvs/Ultimate-HOI4-GFX)의 고정 커밋 `3626dc83c8573d6603fa497138090b04b64a15ba`다. 프로젝트 내부 `.local-artifacts/korean-focus-icons/sources/Ultimate-HOI4-GFX/`에 이미 보존된 PNG 15개를 재사용했다. 기존 source-manifest와 바이트 해시가 일치하는 원본만 채택했다.

[고정 커밋의 CREDITS.txt](https://github.com/Globvs/Ultimate-HOI4-GFX/blob/3626dc83c8573d6603fa497138090b04b64a15ba/CREDITS.txt)는 기여자 동의와 자유로운 사용을 명시한다. 원문 [보존본](assets/korean-focus-icons/UPSTREAM_CREDITS.txt)의 SHA-256은 `cf220dc66463d75163f7690ad77b02b662d0c05ca5d53dc62d33ed504512a7f5`다. 이 근거를 채택된 팩 파일에만 적용하며, 기여자가 참여한 다른 모드 전체의 사용 허가로 확대하지 않는다. 별도의 MIT·CC 라이선스를 추정하지 않는다.

원 기여 표시는 **Globvs / Ultimate HOI4 GFX contributors**다. 파일별 작가 대응이 upstream에 없어 개별 원저자는 미상으로 기록한다. 전체 CREDITS의 명단은 Globvs, HOI4 GFX Modding Database, ThePinkPanzer, Gunnar von Pontius, Pacifica, That Guy Called Curly, Deathlinger, Edouard_Saladier, scarecroww, joshyflip, Indycyclone77, grestin, AtomicSoviet이다. 이 목록을 이번 모든 파일의 공동 제작자 목록으로 단정하지 않는다. AtomicSoviet의 일부 제공 경위에 The New Order가 기록되어 있어도 그 모드의 다른 그림을 채택한 것은 아니다.

배경은 `Focus Backgrounds/Circle with Ribbon2.png`와 `National Spirit Backgrounds/Circle.png`다. 부품은 `Focus & National Spirits Pieces/`의 `Paper.png`, `Wheat2.png`, `Cog Wheel.png`, `Book Open.png`, `Blueprints.png`, `Book.png`, `Magnifying Glass.png`, `Map with Sextant.png`, `Worker.png`, `Clock.png`, `Wrench.png`, `Circular Arrows.png`, `Factories2.png`다. 실제 그림의 내용과 무관한 파일명 추정으로 부품을 선택하지 않았다. 예를 들어 곡식은 잘못 이름 붙은 `Wheat.png`가 아닌 `Wheat2.png`다.

## 정책별 구성과 계속개발 제작

| 대상 | 구성과 구분 |
|---|---|
| 농촌 공동업무 조사 | 직접 제작한 클립보드·금속 집게에 조사 서류와 곡식을 배치 |
| 조합 기술상담소 | 생산 톱니바퀴와 펼친 기술 교범 |
| 작업장 기술회보 | 회보 서류와 공학 도해. 일반 등록 서류와 구분 |
| 공동업무 회계 공개 | 열린 회계 장부를 비추는 확대경 |
| 전국 조합 기술보급망 | 교범·서류·기어를 잇는 직접 제작 연결선과 접점 |
| 국가계획 사무국 | 계획 장부와 직접 제작 행정 인장 |
| 지방계획 연락소 | 지방 지도·문서와 직접 제작 전달 경로 |
| 현장 기술대표단 | 작업자와 공학 설계도. 특정 실제 인물의 초상이 아님 |
| 계획실적 검토회의 | 계획 장부·검토 인장·주기 확인용 시계 |
| 조합 기술보급 I·II | 작은 크기에 맞춘 같은 교범·기어 소재와 단계 배지 |
| 계획행정 I·II | 같은 계획 장부·인장 소재와 단계 배지 |
| 순회 기술교육 결정 | 교범·공구, 32×32 전용 구성 |
| 농촌 기반시설 지원 결정 | 직접 제작한 도로·차선과 곡식, 32×32 |
| 생산공정 전환 관리 결정 | 순환 화살표·기어, 32×32 |
| 신규 생산선 가동 지원 결정 | 공장과 직접 제작 평행 생산선·작업 단위, 32×32 |

계속개발 **kpopmodder**의 기여는 의미별 소재 선정, 새 배치, 비율 유지 크기 조정, 배경색 가공, 클립보드·인장·연결선·도로·생산선 도형 제작과 DDS 변환이다. 원본 부품의 원화를 새 창작으로 표시하지 않는다. 인장의 기호는 새로 만든 추상적 행정 표식이며 실제 기관의 인장이나 글자로 주장하지 않는다. 원래 제안의 마을 지붕·위원회 원탁은 그대로 그렸다고 기록하지 않고 실제 채택한 곡식·현장 작업자·교범 구성으로 구체화했다.

기존 `IconRenderer.cs`와 `BackgroundColors.cs`는 바꾸지 않고 재사용했다. 새 도형은 `.local-artifacts/korean-communist-development-icons/DevelopmentMarks.cs`, 구성은 같은 경로의 `build-icons.ps1`에 보존한다. 매니페스트에 그 소스 해시와 도형 좌표·레이어 순서를 기록했다. I·II는 실제 교체되는 4개 국민정신에만 붙이며, 중점과 결정에 장식용 단계를 넣지 않았다.

## 색상·형식·연결

이 정치 가지의 배경은 공산 계열 **RGB (116,45,48)**이며, 현재 집권 이념에 따라 바뀌지 않는다. 배경의 적색 원판만 별도 마스크로 선택하고 원래 명암에 비례해 색을 조정했다. 금속 테두리와 중앙 부품 전체에 색 필터를 씌우지 않았고 알파도 보존했다. 정확한 선택식·배경 파생본·마스크 해시는 매니페스트에 있다.

- 중점 9개는 `gfx/interface/goals/HOK_KOR/communist_development/`의 100×88 DDS다.
- 정신 4개는 `gfx/interface/ideas/HOK_KOR/communist_development/`의 60×68 DDS다.
- 결정 4개는 `gfx/interface/decisions/HOK_KOR/communist_development/`의 **32×32 전용 DDS**다. 큰 월계·리본을 생략한 작은 금속 원판 위에 핵심 소재를 다시 구성했다. 큰 중점 이미지를 결정 스프라이트에 직접 연결하지 않는다.
- `interface/HOK_KOR_communist_development_icons.gfx`는 17개 일반 스프라이트, `_shine.gfx`는 중점 광택 9개를 정의한다. 기존 후속 내정 카테고리를 사용하므로 카테고리 그림은 추가하지 않는다.

모든 출력은 BGRA32 단일 프레임이며 추가 축소 밉맵 레벨 없이 알파를 포함한다. 중점·정신·결정은 각각 기존 동종 프로젝트 DDS의 128바이트 헤더를 그대로 사용한다. 중점은 mipmapCount 1과 행 피치, 정신은 mipmapCount 0과 전체 선형 크기, 결정은 mipmapCount 0과 행 피치를 기록하는 차이를 유지한다. 각 헤더의 플래그에 따라 크기 필드를 해석하며 실제 페이로드는 모두 기본 해상도 한 장이다. 결정의 32×32 캔버스는 기존 HOI4 1.19.3 검증 기준(일반 행 높이 41·중심 30,19·제목 x63; 기간제 행 높이 40·중심 32,20·제목 x62)에 맞춘 것이다. [결정 아이콘 크기 수정 기록](incidents/2026-09-22-korean-decision-icon-size.md)을 따른다.

광택은 기존 내부 파일 `gfx/interface/goals/HOK_KOR/shine_overlay.dds`를 공유한다. 원본은 **Paradox Interactive의 HOI4 1.19.3** 광택 오버레이며 SHA-256은 `bb416649358c73d34aacd46bad61bc44211fac8111627b56e25f385ad98f4448`이다. 이번에는 복사·수정하지 않았다. HOI4 모드 안에서 재사용하는 바닐라 자산이며 공개 PNG 팩의 CREDITS 허가에 포함시키지 않는다.

## 검수 범위

[실제 크기 접촉표](assets/korean-communist-development-icons/contact-sheet.png)는 중점 100×88, 정신 60×68, 결정 32×32를 확대 없이 보여 준다. 새 9개 소재가 직전 내정 묶음과 구분되는지, 연결된 두 정신 계열과 I·II, 작은 결정의 핵심 소재·테두리·여백을 확인했다.

DDS 헤더·피치·밉맵·크기·알파·해시, 스프라이트/내부 상대 경로·대소문자, 배경 마스크 밖의 픽셀과 알파 보존, 기존 로컬 runtime DDS의 해시를 점검했다. 결과는 `.local-artifacts/korean-communist-development-icons/validation.json`을 따른다. 이미지 담당자는 게임을 실행하지 않았으며, 실제 잠김/진행/완료/광택 상태·정신 교체·결정 목록/진행 상태의 검증은 root 런타임 기록과 구분한다. 정적 확인을 실제 게임 표시의 증거로 대체하지 않는다.
