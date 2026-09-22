# 파시즘 참모업무 아이콘 출처

2026-09-22. 참모업무 F2 중점 4개와 연결 국민정신 I·II 2개를 위한 신규 DDS 6개다. 기준은 `feat/korean-focus-expansion-ai` / `691ffa37740237feddf0b44fc68cfa47b10d76bf` 위에 있던 미커밋 F1 군수조달 구현 상태다. 기존 F1과 다른 이미지·GFX·매니페스트, 게임플레이와 종합 문서는 이 이미지 작업에서 수정하지 않는다. 결정·범주 그림은 이번 범위에 없다.

제작 방법은 **허용된 로컬 PNG 부품 재사용·새 합성과 직접 그린 지휘봉·야전무전기 도형**이다. AI 생성·새 다운로드·도구 설치는 하지 않았다. ID와 스프라이트, 소재별 원본·최종 해시, 배치 좌표와 도형 제작 소스는 [전용 매니페스트](data/HOK_KOREAN_FASCIST_STAFF_ICON_MANIFEST.json)에 기록했다.

## 원본과 재사용 근거

[Globvs / Ultimate HOI4 GFX](https://github.com/Globvs/Ultimate-HOI4-GFX)의 고정 커밋 `3626dc83c8573d6603fa497138090b04b64a15ba`에서 이미 보존한 PNG 6개를 사용했다. 원본은 프로젝트 내부 `.local-artifacts/korean-focus-icons/sources/Ultimate-HOI4-GFX/`에 있으며 기존 source-manifest의 SHA-256과 일치하는 파일만 사용했다.

[고정 커밋 CREDITS.txt](https://github.com/Globvs/Ultimate-HOI4-GFX/blob/3626dc83c8573d6603fa497138090b04b64a15ba/CREDITS.txt)는 기여자 동의와 자유로운 사용을 명시한다. [원문 보존본](assets/korean-focus-icons/UPSTREAM_CREDITS.txt)의 SHA-256은 `cf220dc66463d75163f7690ad77b02b662d0c05ca5d53dc62d33ed504512a7f5`다. 이 근거는 채택한 팩 파일에 한정한다. 기여자가 참여한 다른 모드·작품의 포괄적 허가나 별도 MIT·CC 라이선스를 추정하지 않는다.

원 기여 표시는 **Globvs / Ultimate HOI4 GFX contributors**다. 파일별 작가 대응 자료가 없어 각 파일의 개별 원저자는 미상이다. 보존된 전체 명단은 Globvs, HOI4 GFX Modding Database, ThePinkPanzer, Gunnar von Pontius, Pacifica, That Guy Called Curly, Deathlinger, Edouard_Saladier, scarecroww, joshyflip, Indycyclone77, grestin, AtomicSoviet이다. 모두를 각 이미지의 공동 제작자라고 단정하지 않는다. CREDITS의 The New Order 언급을 그 모드의 다른 그림에 대한 허가로 확대하지 않는다.

배경 원본은 `Focus Backgrounds/Circle with Ribbon2.png`와 `National Spirit Backgrounds/Circle.png`다. 중앙 부품은 `Focus & National Spirits Pieces/`의 `Paper.png`, `Map with Sextant.png`, `Blueprints.png`, `Book Open.png`다. 실제 원본 접촉표로 문서, 지도·디바이더, 청사진·제도도구, 펼친 책의 형태를 확인했다. 팩의 `Walkie Talkie.png`를 명칭만 보고 채택하지 않고 야전 통신기를 직접 구성했다.

## 정책별 구성

| 대상 | 소재와 의미 |
|---|---|
| 참모보직 정비 | 보직 명부와 직접 그린 교차 지휘봉 |
| 작전기획국 | 작전 지도·디바이더와 청사진·제도도구 |
| 야전보고 체계 | 직접 그린 야전무전기·수화기·안테나와 지도 |
| 참모업무 규정 | 펼친 업무 교범과 지도 |
| 참모업무 체계 I·II | 규정 중점과 같은 교범·지도 소재, 실제 강화 단계 배지 |

계속개발 **kpopmodder**의 기여는 의미별 소재 선정, 크기별 레이어 합성, 배경색 가공, 새 지휘봉·무전기 도형, DDS 변환과 통합이다. 원래 부품의 원화를 후속 팀의 새 창작으로 표시하지 않는다. 무전기는 실제 장비 모델의 정확한 복원이 아닌 기능을 나타내는 일반적인 야전 통신 장비 그림이다. 기존 `IconRenderer.cs`·`BackgroundColors.cs`는 수정하지 않았다. 새 도형 소스 `StaffMarks.cs`와 전체 `build-icons.ps1`, 원본 검수표·중간 PNG는 `.local-artifacts/korean-fascist-staff-icons/`에 보존했다.

## 색상·형식·참조

F1 군수조달과 같은 정치 가지의 **차콜·갈색 RGB(70,60,48)**을 원판 배경에만 적용했다. 배경 명암·알파를 유지하고 중앙 소재·금속 테두리·월계에는 색 필터를 적용하지 않는다. 이 참모 모듈은 정치 가지이므로 공통 육군 분야의 녹색 대신 파시즘 배경색을 사용하며, 현재 집권 이념에 따라 바뀌지 않는다. 배경 마스크·파생본·최종 출력 해시를 매니페스트에 남겼다.

- 중점: `gfx/interface/goals/HOK_KOR/fascist_staff/`의 100×88 DDS 4개.
- 국민정신: `gfx/interface/ideas/HOK_KOR/fascist_staff/`의 60×68 DDS 2개. 실제 I·II 강화만 표시한다.
- `interface/HOK_KOR_fascist_staff_icons.gfx`의 일반 6개, `_shine.gfx`의 광택 4개 스프라이트는 모두 프로젝트 내부 상대 경로를 사용한다.

모든 출력은 알파를 포함한 BGRA32 DDS 단일 프레임이다. 동종 프로젝트 DDS의 128바이트 헤더를 그대로 사용했다. 중점은 mipmapCount 1과 행 피치, 정신은 mipmapCount 0과 전체 선형 크기를 유지하며 실제 페이로드는 기본 해상도 한 장이다. 추가 축소 밉맵 레벨은 없다.

광택은 기존 내부 파일 `gfx/interface/goals/HOK_KOR/shine_overlay.dds`를 공유한다. 원본은 **Paradox Interactive / HOI4 1.19.3**의 `gfx/interface/goals/shine_overlay.dds`이며 SHA-256은 `bb416649358c73d34aacd46bad61bc44211fac8111627b56e25f385ad98f4448`이다. 이번에 복사·수정하지 않았다. 공개 팩의 CREDITS와 별개인 바닐라 모드용 재사용 자산으로 기록한다.

## 검수 범위

[실제 크기 접촉표](assets/korean-fascist-staff-icons/contact-sheet.png)는 6개 출력 DDS를 확대 없이 보여 준다. 명부·작전·통신·교범 구분, 어두운 배경과 금속 테두리 대비, 연결 정신의 소재와 I·II 배지를 정적으로 확인했다. 게임 화면으로 표시하지 않는다.

DDS 형식·헤더·크기·알파·해시, 스프라이트 중복과 내부 참조·대소문자, 광택 오버레이, 원본 해시, 배경 마스크 밖 픽셀과 알파 보존, I·II의 배지 밖 불변, 기존 runtime DDS 불변을 점검했다. 결과는 `.local-artifacts/korean-fascist-staff-icons/validation.json`을 따른다. 이미지 담당자는 게임을 실행하지 않았다. 잠김·진행·완료·광택·정신 교체의 실제 표시와 기타 런타임 검증은 root의 별도 기록과 구분한다.
