# 파시즘 병역·필수인력 정책 아이콘 출처

2026-09-22. F3 중점 4개, 병역행정 체계 I·II와 필수인력 배치정책 국민정신 3개를 위한 신규 DDS 7개다. 기준은 `feat/korean-focus-expansion-ai` / `691ffa37740237feddf0b44fc68cfa47b10d76bf` 위의 미커밋 F1 군수조달·F2 참모업무·정치 압축 구현 상태다. 기존 이미지·GFX·매니페스트는 보존했다. 결정·범주 그림은 이번 범위에 없다.

제작 방법은 **허용된 로컬 PNG 부품 재사용·새 합성과 직접 그린 헬멧·군번표·소집 달력 도형**이다. AI 생성·새 다운로드·도구 설치는 하지 않았다. ID·스프라이트, 부품별 원본·최종 해시, 합성 좌표와 도형 소스는 [전용 매니페스트](data/HOK_KOREAN_FASCIST_MOBILIZATION_ICON_MANIFEST.json)에 기록한다.

## 원본과 재사용 근거

[Globvs / Ultimate HOI4 GFX](https://github.com/Globvs/Ultimate-HOI4-GFX)의 고정 커밋 `3626dc83c8573d6603fa497138090b04b64a15ba`에서 이미 프로젝트 내부 `.local-artifacts/korean-focus-icons/sources/Ultimate-HOI4-GFX/`에 보존한 PNG 5개를 사용했다. 모든 원본을 기존 source-manifest의 SHA-256과 렌더링 전에 대조했다.

[고정 커밋 CREDITS.txt](https://github.com/Globvs/Ultimate-HOI4-GFX/blob/3626dc83c8573d6603fa497138090b04b64a15ba/CREDITS.txt)는 기여자 동의와 자유로운 사용을 명시한다. [원문 보존본](assets/korean-focus-icons/UPSTREAM_CREDITS.txt)의 SHA-256은 `cf220dc66463d75163f7690ad77b02b662d0c05ca5d53dc62d33ed504512a7f5`다. 이 근거는 채택한 팩 파일에 한정한다. 기여자가 참여한 다른 모드·작품 전체의 허가나 별도 MIT·CC 라이선스를 추정하지 않는다.

원 기여 표시는 **Globvs / Ultimate HOI4 GFX contributors**다. 파일별 작가 대응 자료가 없어 각 파일의 개별 원저자는 미상이다. 보존된 전체 명단은 Globvs, HOI4 GFX Modding Database, ThePinkPanzer, Gunnar von Pontius, Pacifica, That Guy Called Curly, Deathlinger, Edouard_Saladier, scarecroww, joshyflip, Indycyclone77, grestin, AtomicSoviet이다. 모두를 각 이미지의 공동 제작자라고 단정하지 않으며, CREDITS의 The New Order 언급을 그 모드의 다른 그림에 대한 허가로 확대하지 않는다.

배경 원본은 `Focus Backgrounds/Circle with Ribbon2.png`와 `National Spirit Backgrounds/Circle.png`다. 중앙 부품은 `Focus & National Spirits Pieces/`의 `Paper.png`, `Factories2.png`, `Worker.png`다. 실제 원본과 기존 접촉표를 열어 명부·공장·모자 쓴 전신 노동자의 모습을 확인했다. 노동자 원본의 가로세로 비율과 색을 유지했다.

## 정책별 구성

| 대상 | 소재와 의미 |
|---|---|
| 병역행정 명부 | 명부와 직접 그린 금속 군번표·연결 고리 |
| 예비인력 소집계획 | 직접 그린 일반적인 예비군 헬멧과 소집 날짜를 표시한 달력 |
| 필수인력 배치기준 | 숙련노동자·공장·인사명부 |
| 병역행정 일원화 | 통합 명부와 군·공장을 나타내는 헬멧·공장 |
| 병역행정 체계 I·II | 일원화 중점과 같은 명부·헬멧·공장 소재, 실제 강화 단계 배지 |
| 필수인력 배치정책 | 배치기준 중점과 같은 노동자·공장·명부 소재. 단일 정신이므로 단계 배지 없음 |

계속개발 **kpopmodder**의 기여는 의미별 부품 선정, 크기별 레이어 합성, 배경색 가공, 새 헬멧·군번표·달력 도형, DDS 변환과 통합이다. 팩 부품의 원화를 후속 팀의 새 창작으로 표시하지 않는다. 새 헬멧과 군번표는 특정 실물·군복 체계의 정확한 복원을 주장하지 않는 일반적인 병역행정 상징이다. 새 도형은 `ManpowerMarks.cs`에 곡선·금속 명암·테두리·표식 좌표로 기록했다.

기존 `IconRenderer.cs`와 `BackgroundColors.cs`는 변경하지 않았다. F3 전용 `build-icons.ps1`, `ManpowerMarks.cs`, 입력 명세, 중간 PNG·마스크·검수 결과는 `.local-artifacts/korean-fascist-mobilization-icons/`에 보존했다. F1·F2의 기존 제작 스크립트를 재실행하거나 수정하지 않았다.

## 색상·형식·참조

F1·F2와 같은 정치 가지의 **차콜·갈색 RGB(70,60,48)**을 원판 배경에만 적용했다. 배경 명암·알파와 금속 테두리·월계를 유지하고 중앙 원본 부품에는 색 필터를 적용하지 않는다. 새 헬멧·군번표·달력은 이 금속색 계열에 맞춰 직접 그렸다. 분야 소재가 군·산업이어도 파시즘 정치 가지에 속하므로 배경색은 이 계열에 고정된다. 현재 집권 이념에 따라 바뀌지 않는다.

- 중점: `gfx/interface/goals/HOK_KOR/fascist_mobilization/`의 100×88 DDS 4개.
- 국민정신: `gfx/interface/ideas/HOK_KOR/fascist_mobilization/`의 60×68 DDS 3개. 병역행정 체계에만 실제 I·II 강화를 표시한다.
- `interface/HOK_KOR_fascist_mobilization_icons.gfx`의 일반 7개와 `_shine.gfx`의 광택 4개 스프라이트는 모두 프로젝트 내부 상대 경로를 사용한다.

모든 출력은 알파를 포함한 BGRA32 DDS 단일 프레임이다. 동종 프로젝트 DDS의 128바이트 헤더를 그대로 사용했다. 중점은 mipmapCount 1과 행 피치, 정신은 mipmapCount 0과 전체 선형 크기를 유지하며 실제 페이로드는 기본 해상도 한 장이다. 추가 축소 밉맵 레벨은 없다. 정신은 중점을 통째로 축소하지 않고 소재 배치를 별도로 구성했다.

광택은 기존 내부 파일 `gfx/interface/goals/HOK_KOR/shine_overlay.dds`를 공유한다. 원본은 **Paradox Interactive / HOI4 1.19.3**의 `gfx/interface/goals/shine_overlay.dds`이며 SHA-256은 `bb416649358c73d34aacd46bad61bc44211fac8111627b56e25f385ad98f4448`이다. 이번에 복사·수정하지 않았다. 공개 팩의 CREDITS와 별개인 바닐라 모드용 재사용 자산으로 기록한다.

## 검수 범위

[실제 크기 접촉표](assets/korean-fascist-mobilization-icons/contact-sheet.png)는 7개 출력 DDS를 확대 없이 보여 준다. 명부·군번표, 헬멧·달력, 노동자·공장, 통합 명부의 차이와 어두운 원판의 금속 테두리 대비를 확인했다. 병역행정 I·II는 배지 밖 픽셀이 동일하며 필수인력 정신에는 배지가 없다. 접촉표는 게임 화면이 아니다.

DDS 형식·헤더·크기·알파·해시, 스프라이트 중복과 내부 참조·대소문자, 광택 오버레이, 원본·제작 소스 해시, 배경 마스크 밖 픽셀과 알파 보존, I·II의 배지 밖 불변, 기존 runtime DDS 불변을 점검했다. 결과는 `.local-artifacts/korean-fascist-mobilization-icons/validation.json`을 따른다. 이미지 담당자는 게임을 실행하지 않았다. 잠김·진행·완료·광택·정신 교체의 실제 표시는 별도 런타임 검증 대상이다.
