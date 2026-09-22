# 파시즘 후속 정책 F4–F6 아이콘 출처

2026-09-23. 점령 행정·삼군 조정·재건예산의 중점 12개와 국민정신 8개를 위한 신규 DDS 20개다. 기준은 `feat/korean-focus-expansion-ai` / `e511f3196df287f3dd9a103cbb310762bdbc7072`와 그 위의 미커밋 작업 방식 문서다. 기존 이미지와 GFX는 보존했으며, 결정·범주 아이콘은 이번 묶음에 없다.

제작 방법은 **허용된 로컬 PNG 부품의 재사용·새 합성·배경 레이어 색상 가공**이다. 새 원화·AI 이미지 생성·추가 다운로드는 하지 않았다. 소재별 원본 해시, 합성 좌표, 내용 ID·스프라이트와 최종 파일 해시는 [전용 매니페스트](data/HOK_KOREAN_FASCIST_FOLLOWUP_ICON_MANIFEST.json)에 기록했다.

## 원본과 재사용 근거

[Globvs / Ultimate HOI4 GFX](https://github.com/Globvs/Ultimate-HOI4-GFX)의 고정 커밋 `3626dc83c8573d6603fa497138090b04b64a15ba`에서 이미 보존한 PNG 15개를 사용했다. 프로젝트 내부 작업 원본은 `.local-artifacts/korean-focus-icons/sources/Ultimate-HOI4-GFX/`에 있다. 렌더링 전에 선택한 원본과 `CREDITS.txt` 16개를 기존 source-manifest의 SHA-256과 대조했다.

[고정 커밋 CREDITS.txt](https://github.com/Globvs/Ultimate-HOI4-GFX/blob/3626dc83c8573d6603fa497138090b04b64a15ba/CREDITS.txt)는 기여자 동의와 자유로운 사용을 명시한다. [원문 보존본](assets/korean-focus-icons/UPSTREAM_CREDITS.txt)의 SHA-256은 `cf220dc66463d75163f7690ad77b02b662d0c05ca5d53dc62d33ed504512a7f5`다. 이 근거는 채택한 팩 파일에 한정한다. 참여자가 기여한 다른 모드·작품 전체의 허가나 별도 MIT·CC 라이선스를 추정하지 않는다.

원 기여 표시는 **Globvs / Ultimate HOI4 GFX contributors**다. 파일별 작가 대응 자료가 없어 개별 원저자는 미상이다. 보존된 전체 기여 명단은 Globvs, HOI4 GFX Modding Database, ThePinkPanzer, Gunnar von Pontius, Pacifica, That Guy Called Curly, Deathlinger, Edouard_Saladier, scarecroww, joshyflip, Indycyclone77, grestin, AtomicSoviet이다. 모두를 각 파일의 공동 제작자라고 단정하지 않으며, CREDITS의 The New Order 언급을 그 모드의 다른 이미지에 대한 허가로 확대하지 않는다.

배경은 `Focus Backgrounds/Circle with Ribbon2.png`와 `National Spirit Backgrounds/Circle.png`다. 중앙 부품은 `Focus & National Spirits Pieces/`의 `Paper.png`, `Book Open.png`, `Shield.png`, `Scales.png`, `Crate.png`, `Anchor.png`, `Aircraft Fighter.png`, `Cannon Twins.png`, `Truck.png`, `Parliament.png`, `Coins.png`, `Blueprints.png`, `Factories2.png`다. 기존 원본 접촉표를 직접 열어 부품의 형태를 확인했다. 의회 건물 부품은 공공 행정기관을 나타내는 일반적인 건물 상징으로 사용했다.

## 정책별 구성

| 중점 | 중심 소재 |
|---|---|
| 군정 실무편람 | 펼친 업무 교범과 방패 |
| 민생물자 관리소 | 생활물자 상자와 배분 저울 |
| 민원·보상 기록부 | 민원 문서와 권리·보상 저울 |
| 군정 행정규정 | 공공기관과 행정 교범 |
| 삼군 연락사무국 | 포신·닻·항공기의 삼군 상징 |
| 삼군 군수조정회의 | 공통 보급상자와 닻·항공기 |
| 통합 청구·수송 명부 | 수송 명부와 트럭 |
| 삼군 군수업무 규정 | 공통 군수 교범과 닻·항공기 |
| 재건행정 사무국 | 공공기관·사업 문서·제도도구 |
| 행정예산 우선배정 | 회계 장부와 청동색 동전 |
| 건설예산 우선배정 | 공장·설계도·제도도구 |
| 재건예산 정례화 | 공장과 정기 예산 장부·동전 |

점령행정 체계 I·II는 군정 행정규정과, 삼군 군수조정 I·II는 삼군 군수업무 규정과 소재를 공유한다. 재건 행정예산 I·II와 재건 건설예산 I·II는 각각 실제 선택한 예산 가지의 회계·건설 소재를 유지한다. 네 쌍에만 실제 강화 단계 I·II를 붙이고, 중점 그림에는 단계 배지를 붙이지 않았다. 국민정신은 중점 이미지를 통째로 축소하지 않고 60×68 화면에 맞춰 부품을 따로 배치했다.

계속개발 **kpopmodder**의 기여는 정책별 소재 선정, 크기별 새 레이어 합성, 배경색 가공, DDS 변환과 통합이다. 원래 부품의 원화를 후속 팀의 새 창작으로 표시하지 않는다. 기존 `IconRenderer.cs`와 `BackgroundColors.cs`는 변경하지 않았다. 새 `build-icons.ps1`, 입력 명세, 중간 PNG·배경 마스크·검수 결과는 `.local-artifacts/korean-fascist-followup-icons/`에 보존했다. F1–F3 제작 스크립트와 기존 이미지는 재생성하지 않았다.

## 색상·형식·내부 참조

F1–F3와 같은 정치 가지의 **차콜·갈색 RGB(70,60,48)**을 원판 배경에만 적용했다. 배경의 명암·알파와 금속 테두리·월계를 유지하며 중앙 부품에는 색 필터를 적용하지 않는다. 군·산업 소재도 파시즘 정치 가지에 속하므로 이 배경색에 고정되며 현재 집권 이념에 따라 바뀌지 않는다.

- 중점: `gfx/interface/goals/HOK_KOR/fascist_followup/`의 100×88 DDS 12개.
- 국민정신: `gfx/interface/ideas/HOK_KOR/fascist_followup/`의 60×68 DDS 8개.
- 일반 20개는 `interface/HOK_KOR_fascist_followup_icons.gfx`, 광택 12개는 `interface/HOK_KOR_fascist_followup_icons_shine.gfx`에 정의했다. 이미지 참조는 모두 프로젝트 내부 상대 경로다.

출력은 알파를 포함한 BGRA32 DDS 단일 프레임이다. 기존 동종 프로젝트 DDS의 128바이트 헤더를 유지했다. 중점은 mipmapCount 1과 행 피치, 정신은 mipmapCount 0과 전체 선형 크기를 유지하며 실제 페이로드는 기본 해상도 한 장이다. 추가 축소 밉맵은 없다.

광택은 기존 내부 파일 `gfx/interface/goals/HOK_KOR/shine_overlay.dds`를 공유한다. 원본은 **Paradox Interactive / HOI4 1.19.3**의 `gfx/interface/goals/shine_overlay.dds`이며 SHA-256은 `bb416649358c73d34aacd46bad61bc44211fac8111627b56e25f385ad98f4448`이다. 이번에 복사·수정하지 않았다. 공개 팩 CREDITS와 별개인 기존 바닐라 모드용 재사용 자산이다.

## 검수 범위

[실제 크기 접촉표](assets/korean-fascist-followup-icons/contact-sheet.png)는 20개 최종 DDS를 확대 없이 보여 준다. 행정·생활물자·민원, 삼군·수송, 회계·건설 소재의 차이와 어두운 배경의 금속 윤곽, 정신의 I·II 배지 표시를 확인했다. 이 접촉표는 실제 게임 화면이 아니다.

정적 검수는 DDS 헤더·해상도·알파·해시, 스프라이트 32개의 중복, 내부 경로와 정확한 대소문자, 광택 오버레이, 원본과 제작 소스 해시, 배경 마스크 밖 픽셀·알파 보존을 통과했다. 네 I·II 쌍은 각각 배지 안의 54픽셀만 다르고 배지 밖의 차이는 0이다. 기존 runtime DDS 170개를 대조했으며 변경된 파일은 0개다. 상세 결과는 `.local-artifacts/korean-fascist-followup-icons/validation.json`에 보존했다.

이미지 담당자는 게임을 직접 실행하지 않았다. 이후 root가 별도 게임에서 완료 상태 HIDE와 신규 중점 미완료 SHOW의 F4–F6 및 이웃 구역, F4 영토 없음 차단, F5 네 중점의 자연 완료·AND 잠금과 해제·정신 I→II 교체를 관측했고 이미지 담당자는 저장된 화면을 다시 확인했다. F5 정신 I의 세 소모 보정 −10%와 II의 −15%, II 획득 후 I 아이콘이 없는 상태를 확인했다. 이 진행 증거는 표시 필터 수정 전 소스에 해당한다.

필터 수정 후 최종 소스는 진단 없는 새 게임 `clean-final-02`(체크섬 `38c4`)에서 1936-01-01 12시에 일시정지한 채 상단 SHOW와 삼군 연락사무국의 현지화된 필터를 확인했다. 최종 중점의 AND 조건·효과 화면도 보존했지만 해당 화면에 필터 줄이 보이지 않아 그 필터 표시까지 확인했다고 주장하지 않는다. GUI 종료 후 기존 저장 13개·설정·플레이세트·런처와 production 파일 68개의 보존 감사를 통과했다. 앞선 장기 UI 시험의 자동 저장 1개 덮어쓰기와 원본 복구는 [구현 기록](incidents/2026-09-23-korean-fascist-followup.md)에 별도로 기록한다. 전체 광택·모든 정신 교체·원래 정치 경로의 선택 전후 이동을 검증한 상태는 아니다.
