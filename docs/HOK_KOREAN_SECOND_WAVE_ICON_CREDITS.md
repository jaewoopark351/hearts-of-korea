# 한국 2차 확장 첫 소묶음 아이콘 출처·가공 기록

2026-09-22. 범위는 여운형 협동조합 정책(Y2) 중점 5개, 박헌영 공작기계·생산 배정(P2) 중점 5개와 선택 국민정신 I·II 8개다. 기존 60개 중점·29개 국민정신 이미지는 재생성하지 않았다. 소스 기준 커밋은 `f43769cd9957d4f331b4d591506d52f5da485f79`이다.

이번 그림은 **허용된 공개 PNG 소재를 재사용하여 새로 합성한 그림**이다. 기존 부품의 원화를 계속개발 팀의 창작으로 표시하지 않으며, AI 이미지 생성은 사용하지 않았다. 최종 DDS, 개별 ID·참조·원본 해시·배치 레시피는 [전용 매니페스트](data/HOK_KOREAN_SECOND_WAVE_ICON_MANIFEST.json)에 기록했다.

## 원본과 허용 범위

- 원본: [Globvs / Ultimate HOI4 GFX](https://github.com/Globvs/Ultimate-HOI4-GFX), 고정 커밋 `3626dc83c8573d6603fa497138090b04b64a15ba`.
- 사용 근거: [그 커밋의 CREDITS.txt](https://github.com/Globvs/Ultimate-HOI4-GFX/blob/3626dc83c8573d6603fa497138090b04b64a15ba/CREDITS.txt)가 기여자 동의와 자유로운 사용을 명시한다. 원문 [보존본](assets/korean-focus-icons/UPSTREAM_CREDITS.txt)의 SHA-256은 `cf220dc66463d75163f7690ad77b02b662d0c05ca5d53dc62d33ed504512a7f5`다.
- 이 허가는 이번에 사용한 **해당 팩의 16개 PNG**에 한정한다. 기여자가 소속된 다른 모드 전체에 적용하지 않으며, MIT·CC 등의 별도 라이선스를 추정하지 않았다.
- 원 기여 표시는 **Globvs / Ultimate HOI4 GFX contributors**다. CREDITS에 개별 파일별 제작자가 연결되어 있지 않아 파일별 원저자는 미상으로 기록한다. 집합 명단은 Globvs, HOI4 GFX Modding Database, ThePinkPanzer, Gunnar von Pontius, Pacifica, That Guy Called Curly, Deathlinger, Edouard_Saladier, scarecroww, joshyflip, Indycyclone77, grestin, AtomicSoviet이며, 각자가 이번 모든 부품을 공동 제작했다고 뜻하지 않는다. AtomicSoviet의 일부 제공 경위에 The New Order가 명시되어 있어도 그 모드 전체 그림의 사용 허가로 해석하지 않는다.
- 기존에 내려받아 보존한 `.local-artifacts/korean-focus-icons/sources/Ultimate-HOI4-GFX/`의 원본을 읽었고, 원본 파일과 기존 source-manifest의 해시가 일치함을 확인했다. 새 다운로드는 하지 않았다.

## 정책별 소재와 제작

| 대상 | 중심 소재 | 관련 국민정신 |
|---|---|---|
| 협동조합 등록망 | 조합원 기록 서류와 밀 이삭 | 없음 |
| 연합 공동구매 우선 | 공동 설비 상자와 공구 | 연합 공동구매 I·II와 같은 상자·공구 |
| 협동 작업장 | 작업자와 톱니바퀴 | 없음 |
| 지역 자율금융 우선 | 열린 장부와 동전 | 지역 자율금융 I·II와 같은 장부·동전 |
| 전국 협동조합 연합 | 밀 이삭 사이의 맞잡은 손 | 선택에 따라 서로 다른 정신을 강화하므로 단계 배지 없음 |
| 공작기계 배치계획 | 큰 톱니바퀴와 공구 | 없음 |
| 군수설비 확충 우선 | 설계도와 새 생산시설 | 군수설비 확충 I·II와 같은 설계도·공장 |
| 현행 생산계획 우선 | 가동 공장과 강재 | 현행 생산계획 I·II와 같은 공장·강재 |
| 공업통계 보고망 | 작성 서류·필기하는 손·공장 | 없음 |
| 중공업 종합배정 | 배정 순환 화살표와 강재 | 선택 정신 두 계열을 강화하므로 단계 배지 없음 |

초안의 쟁기·선반·크레인·전신기라는 예시를 그대로 그렸다고 기록하지 않는다. 실제 허용된 로컬 소재 중 정책의 의미를 나타내는 상자·공구·설계도·작성 서류로 구체화했다. 원본 `Worker.png`의 작업자, `Wheat2.png`의 밀 이삭, `Paper.png`의 서류는 기존 소재 접촉표에서 실제 그림을 확인했다. 잘못 이름 붙은 `Wheat.png`와 현대 기기로 확인된 `Walkie Talkie.png`는 쓰지 않았다.

원본 배경은 중점 `Focus Backgrounds/Circle with Ribbon2.png`, 국민정신 `National Spirit Backgrounds/Circle.png`다. 원판의 적색 픽셀만 별도 배경 레이어에서 공산주의 **기준 RGB (116,45,48)**로 조정했다. 원래 명암은 `pow(luminance/60,0.9)`로 유지하고, 금속 테두리·중앙 그림·알파를 전체 색 필터로 바꾸지 않았다. 이 색은 현재 정부가 아닌 이 두 정치 가지의 고정 색이다.

계속개발 **kpopmodder**의 기여는 정책별 소재 선정, 새 레이어 구성, 투명 여백 정리, 비율 유지 크기 조정, 배경색 조정과 DDS 변환이다. 기존 `IconRenderer.cs`·`BackgroundColors.cs`를 그대로 재사용했다. 실제 교체되는 국민정신 4계열에만 기존 방식의 I·II 배지를 붙였고 중점에는 장식용 단계를 만들지 않았다.

모든 중점은 100×88, 국민정신은 60×68의 단일 프레임 BGRA32 DDS와 알파를 가진다. 최종 이미지는 각각 `gfx/interface/goals/HOK_KOR/second_wave/`, `gfx/interface/ideas/HOK_KOR/second_wave/` 아래에 있다. `interface/HOK_KOR_second_wave_icons.gfx`가 일반 중점·국민정신·결정 재사용 스프라이트를, `_shine.gfx`가 중점 광택 스프라이트를 정의한다.

## 결정 그림 및 바닐라 광택 레이어

4개 유료 정책 사업의 결정 그림은 각각 관련 선택 중점의 로컬 DDS를 재사용한다. 결정 카테고리는 협동조합 등록망 DDS를 재사용한다. 신규 DDS를 중복 생성하지 않고 전용 `GFX_HOK_KOR_decision_*` 5개를 연결했다. 결정 UI의 실제 표시 크기와 카테고리 배치는 중점/정신 접촉표 검수와 별도로 게임에서 확인해야 한다.

공유 광택 오버레이는 **Paradox Interactive의 설치된 HOI4 1.19.3 바닐라 이미지**다. 원본 `gfx/interface/goals/shine_overlay.dds`를 프로젝트 `gfx/interface/goals/HOK_KOR/shine_overlay.dds`에 바이트 그대로 복사했고 SHA-256은 양쪽 모두 `bb416649358c73d34aacd46bad61bc44211fac8111627b56e25f385ad98f4448`이다. HOI4 모드 안에서 사용하는 바닐라 자산이며 Ultimate HOI4 GFX 팩의 CREDITS 허가에 포함시키지 않는다. 2026-09-22 통합에서 복사와 기존 60개 광택 참조 정리를 완료했고 원본·프로젝트 해시 일치를 확인했다. 새 중점의 마스크는 각각의 로컬 DDS이며, 오버레이 경로도 프로젝트 소유 상대 경로다.

## 검수 범위

![정책 중점 10개와 국민정신 8개의 실제 크기 접촉표](assets/korean-second-wave-policy-icons.png)

`.local-artifacts/korean-second-wave-icons/contact-sheet.png`에서 새 18개를 **실제 텍스처 크기**로 확인했다. 공동구매/자율금융 및 신규 설비/현재 생산의 소재가 구별되고, 같은 계열 국민정신의 I·II와 테두리·투명 여백을 확인했다. 배경 마스크 밖의 픽셀 보존, DDS 헤더·크기·알파·파일 길이, 스프라이트 유일성·상대 경로·최종 해시는 별도 정적 점검 기록과 매니페스트를 따른다.

정적 확인은 게임 로더 등록, 잠김·선택 가능·진행 중·완료·광택 상태, 국민정신 툴팁·교체 이후 상태, 결정 UI의 표시를 입증하지 않는다. 런타임 검증 상태는 root의 해당 소묶음 실행 기록과 함께 읽어야 한다. 이 문서는 이미지 담당자가 게임을 실행했다는 주장을 하지 않는다. 기존 원작 그림, 다른 정치 경로, 게임 로직·현지화는 이 이미지 변경의 범위가 아니다.
