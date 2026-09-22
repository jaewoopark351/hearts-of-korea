# 공산주의 결정·카테고리 아이콘 크기 수정

2026-09-22. 사용자 제공 게임 화면에서 새 공산주의 경제정책·후속 내정의 결정 이미지가 옆 글자와 위아래 행을 가렸다. 별도 소형 이미지를 제작해 연결하는 변경이다. 보상·비용·기간·선행조건·AI·현지화·중점 배치는 변경하지 않는다.

## 기준과 원인

- 브랜치 `feat/korean-focus-expansion-ai`, 기준 커밋 `d8558937db1e9c984a16e75eed35d5a6f8914bb2`. 앞선 공산 내정 9개 확장의 미커밋 작업이 있는 상태에서 시작했고 이를 보존한다.
- 설치 게임은 앞선 검증과 같은 HOI4 1.19.3이다. 현재 `dlc_load.json`에는 `mod/hearts of korea.mod` 한 항목과 빈 `disabled_dlcs`가 있으며, launcher descriptor의 실제 경로는 `C:/hoi/hearts_of_korea`다. 이번에는 새 게임을 실행하거나 체크섬·DLC 활성 상태를 다시 측정하지 않았다.
- **CONFIRMED:** 두 GFX 파일의 결정·카테고리 10개가 100×88 중점 DDS를 직접 참조했다. 설치된 바닐라 GUI의 해당 아이콘 블록에는 자동 축소를 위한 `size`/`scale`이 없고 `clipping = no`다. 사용자 화면의 넘침과 원본 크기가 일치한다.
- 원인 분류: 결정 UI 크기에 맞지 않는 GFX 텍스처 재사용. 게임 로직·이념 선택·보상 문제와 구분한다.

## 설치된 바닐라에서 확인한 크기

기준 파일은 게임 설치의 `interface/countrydecisionview.gui`와 `interface/decisions.gfx`다. 바닐라 파일을 수정하거나 GUI 전체를 덮어쓰지 않는다.

| 위치 | 바닐라 배치와 실제 DDS 예 | 이번 크기와 경계 |
|---|---|---|
| 카테고리 | GUI 84~102행: 높이 58, 아이콘 왼쪽 위 (10,16), 제목 x74. `decision_category_generic.dds` 51×40 | 51×40. x10~61, y16~56, 제목까지 13픽셀 |
| 일반 결정 | GUI 401~431행: 높이 41, 아이콘 중심 (30,19), 이름 x63. `decision_generic_decision.dds` 26×29, 정치 아이콘 32×31 | 32×32. x14~46, y3~35, 이름까지 17픽셀 |
| 기간제 결정 | GUI 588~632행: 높이 40, 아이콘 중심 (32,20), 이름 x62 | 32×32. x16~48, y4~36, 이름까지 14픽셀 |

위 경계는 소스 좌표로 계산한 정적 결과다. 바닐라 결정 이미지는 모두 같은 크기가 아니며, `GFX_decision_unknown`의 실제 텍스처는 `decision_generic_decision.dds`다.

## 수정과 출처

- `interface/HOK_KOR_second_wave_icons.gfx`: 경제정책 카테고리 1개·결정 4개의 텍스처 참조만 교체.
- `interface/HOK_KOR_communist_governance_icons.gfx`: 후속 내정 카테고리 1개·결정 4개의 텍스처 참조만 교체.
- 전용 DDS 10개를 `gfx/interface/decisions/HOK_KOR/communist_policy/`와 `communist_governance/`에 저장하고 프로젝트 내부 상대경로로 연결.
- 큰 중점 리본·월계 장식을 줄이고 짙은 적색 원판·금속 테두리·주요 상징으로 다시 구성. 원본 중점 100×88와 국민정신 60×68 이미지는 그대로 유지.
- 이미 허용 범위를 기록한 Globvs / Ultimate HOI4 GFX 부품과 기존 합성 방식을 사용한다. 새 다운로드나 AI 이미지 생성은 없다. 원화의 기여자를 계속 표시하고, 계속개발 기여는 소형 재구성·내보내기로 구분한다.

소재별 원본·허용 근거·가공 레시피·최종 해시는 [소형 아이콘 매니페스트](../data/HOK_KOREAN_SMALL_DECISION_ICON_MANIFEST.json)에 기록한다. 이전 [경제정책](../HOK_KOREAN_SECOND_WAVE_ICON_CREDITS.md)·[후속 내정](../HOK_KOREAN_COMMUNIST_GOVERNANCE_ICON_CREDITS.md) 출처 기록도 함께 보존한다.

## 검증

정적 검수 **PASS**: 새 DDS 10개의 크기·BGRA32 채널·피치·단일 프레임·알파·파일 길이·해시와 대소문자를 포함한 내부 경로를 확인했다. 기존 스프라이트 이름은 각각 유일하며, 두 GFX의 나머지 중점·정신 블록은 바이트가 동일하다. 이전 중점·정신 DDS 121개를 포함해 이번 작업 시작 때 기록한 게임 로직·현지화·원본 이미지 **255개 파일의 해시가 모두 동일**하다. 기존 두 매니페스트의 중점·정신 기록을 보존하고 결정 10개만 새 경로·해시로 갱신했다. `git diff --check`도 통과했다.

[실제 크기 비교 이미지](../assets/korean-small-decision-icons/contact-sheet.png)를 직접 확인했다. 작은 원판·핵심 소재·투명 여백을 검수한 결과이며 게임 스크린샷이 아니다. 상세 로컬 결과는 `.local-artifacts/korean-small-decision-icons/artwork-validation.json`과 `validation.json`에 남겼다.

사용자 게임을 종료하거나 새로 실행하지 않았다. 게임 재시작 후 새 텍스처를 불러와 결정 목록·카테고리·툴팁과 사용 가능/불가/진행 상태를 확인해야 한다. 앞선 공산 내정의 199개 런타임 검사 결과는 게임 로직에 대한 기록이며, 이번 소형 이미지의 실제 표시를 검증한 결과로 취급하지 않는다. 커밋·푸시는 수행하지 않았다.
