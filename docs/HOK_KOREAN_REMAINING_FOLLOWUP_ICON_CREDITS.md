# 잔여 확장 82개 중점과 연계 이미지 출처

작성: 2026-09-23. 기준은 `feat/korean-focus-expansion-ai` / `3f3b70686175516469f7ae51fd34a12240c871d9`, 기존 한국 중점 378개다. 이번 후속 확장은 입헌군주 14·전제군주 14·환제국 14·만주 20·공통 산업/군사 20개에 해당한다. 신규 DDS는 **중점 82, 국민정신 32, 주 동적 수정치 12, 소형 결정 4, 범주 1 — 총 131개**다. 기존 게임 이미지·기존 합성기·광택 오버레이는 보존한다.

제작 방법은 기존에 허용된 **로컬 공개 팩 부품의 새 합성·배경 레이어 색상 가공**, 그리고 승인된 원작 프로젝트 이미지의 왕관·태극 부분 재사용이다. AI 생성·새 다운로드는 사용하지 않았다. 원화의 저자를 후속 제작자로 바꾸어 표시하지 않는다. 내용 ID·원본과 출력 해시·스프라이트·색상·합성 좌표는 [매니페스트](data/HOK_KOREAN_REMAINING_FOLLOWUP_ICON_MANIFEST.json)에 기록한다.

## 공개 팩과 원작 자산의 구분

공개 팩은 기존 [Globvs / Ultimate HOI4 GFX 고정 커밋](https://github.com/Globvs/Ultimate-HOI4-GFX/tree/3626dc83c8573d6603fa497138090b04b64a15ba)의 로컬 보존본을 사용한다. [보존 CREDITS](assets/korean-focus-icons/UPSTREAM_CREDITS.txt)의 SHA-256은 `cf220dc66463d75163f7690ad77b02b662d0c05ca5d53dc62d33ed504512a7f5`다. 해당 문서는 기여자 동의와 자유로운 사용을 명시한다. 이 근거는 선택한 팩 소재에 한정하며 다른 기여 모드의 전체 저작물이나 별도 MIT·CC 라이선스를 추정하지 않는다.

이번에 확인한 팩 원본은 CREDITS를 포함한 39개다. 배경 2개와 중심 부품 36개를 사용했으며 `source-manifest.json`의 고정 SHA-256과 대조했다. 공개 팩 기여 표시는 **Globvs / Ultimate HOI4 GFX contributors**다. CREDITS에 있는 Globvs, HOI4 GFX Modding Database, ThePinkPanzer, Gunnar von Pontius, Pacifica, That Guy Called Curly, Deathlinger, Edouard_Saladier, scarecroww, joshyflip, Indycyclone77, grestin, AtomicSoviet의 기여를 유지한다. 파일별 작가 대응 정보가 없어 각 파일의 개별 원저자는 미상이며 모든 이름을 각 부품의 공동 저자로 단정하지 않는다.

다음 두 소재는 공개 팩과 별개인 **상속한 Hearts of Korea 프로젝트 자산**이다. 계속개발 권한과 선택한 내부 소재 가공 승인에 따라 재사용하며, 원작의 개별 이미지 작가는 미상이다.

| 용도 | 실제 원본 | 가공 |
|---|---|---|
| 왕정·황실 상징 | `gfx/interface/goals/focus_kor_urihwangsilsaranghoe.dds` | `(7,0,55,29)`의 상단 왕관을 잘라 투명 부품으로 사용. 원래 금속색 유지 |
| 환제국 상징 | `gfx/flags/KOR_Hwan_neutrality.tga` | 82×52 BGRA TGA를 읽어 중앙 `(30,15,23,23)` 태극을 원형 알파로 분리. 원래 태극색 유지 |

후보 명세의 ‘용문 인장’·‘삼족오’는 이번에 실제 사용한 부품이 아니다. 완성 이미지에서는 각각 **왕관·행정 문서**, **원작의 태극·제국 운영 소재**로 구분한다. ‘견장·철모’ 등의 제안은 실제 보존 부품인 군인·명부·교범으로, 악천후·연막은 비행기·함선·빙결 화살표로 표현했다. 매니페스트는 `planned_motif`와 `actual_components`를 함께 남겨 실제 그림과 계획의 차이를 숨기지 않는다. 이 소재 선택은 게임의 정치·형성·군사 효과를 변경하지 않는다.

계속개발 **kpopmodder**의 기여는 내용별 부품 선정, 크기별 구성, 배경색 가공, 두 내부 소재의 선택적 자르기, DDS 내보내기와 연결이다. `.local-artifacts/korean-focus-icons/IconRenderer.cs`와 `.local-artifacts/korean-focus-icon-colors/BackgroundColors.cs`는 수정하지 않았다. 신규 입력·빌드·검수 스크립트와 중간 PNG는 `.local-artifacts/korean-remaining-followup-icons/`에 보존한다.

## 색상·단계·크기

색은 현재 집권 이념이 아니라 해당 가지와 분야를 기준으로 고정한다. 배경의 붉은 원판 픽셀만 마스크로 골라 밝기와 알파를 유지하며, 중심 그림과 금속 장식에는 색조 필터를 적용하지 않는다.

| 분류 | 배경 기준 RGB | 적용 |
|---|---|---|
| 민주주의 | 53,91,126 | 입헌군주 및 기존 다민족 포용에서 이어지는 민주 만주 M2 |
| 비동맹 왕정 | 155,159,162 | 전제군주·환제국; 밝은 회색 바탕의 명암과 금속 윤곽 유지 |
| 산업·지역 운영 | 100,100,95 | 만주 M1·M3·M4, 수출·원료 순환, 공통 결정 범주 |
| 육군 | 70,85,45 | 기동부대 운용 |
| 해군 | 40,59,82 | 함대 이탈·해상 구조 |
| 공군 | 138,162,183 | 계기·악천후 비행 |

입헌 경로의 정책은 왕정에서 시작해 민주정부가 되는 기존 구조를 반영해 청색을 유지한다. M2는 모든 이념에 공통인 지역 정책이 아니라 기존 민주 다민족 포용에 연결된 후속 정책이다. 전제·환제국의 밝은 원판은 순백으로 채우지 않았으며 금색 테두리와 원본 소재의 대비를 유지했다.

- 중점 82개: **100×88**, `gfx/interface/goals/HOK_KOR/remaining_followup/`.
- 국민정신 32·주 수정치 12개: **60×68**, `gfx/interface/ideas/HOK_KOR/remaining_followup/`.
- 결정 4개: **32×32**, 범주 1개: **51×40**, `gfx/interface/decisions/HOK_KOR/remaining_followup/`.

결정은 중점 완성 이미지를 통째로 축소하지 않고 원형 프레임과 중심 부품을 작은 캔버스에서 재배치했다. 원본의 큰 월계수·리본을 사용하지 않으며 투명 여백을 남겼다. 기존 결정 GUI나 행 높이는 변경하지 않는다.

실제 강화 관계에 해당하는 17쌍에만 I·II를 표시한다. 네 기간제 집중 사업 수정치는 상위 III가 아니므로 로마 숫자를 넣지 않고 시계로 기간제임을 구별한다. 나머지 단일 정신과 중점·결정에는 단계를 만들지 않는다. I·II는 같은 중심 소재와 배경을 공유한다.

## 형식·프로젝트 내부 연결

131개 DDS는 알파를 포함한 비압축 BGRA32 단일 기본 해상도 이미지다. 중점·정신은 기존 프로젝트 동종 파일의 검증된 DDS 헤더를 사용한다. 결정·범주는 기존 소형 아이콘 제작 때 보존한 32×32·51×40 기술 헤더를 사용하며 바닐라 결정의 그림 픽셀을 복사하지 않는다. 헤더가 기록하는 mipmapCount는 기존 템플릿의 0 또는 1이며 추가 축소 밉맵은 없다.

일반 GFX 131개는 `interface/HOK_KOR_remaining_followup_icons.gfx`, 중점 광택 82개는 `interface/HOK_KOR_remaining_followup_icons_shine.gfx`에 정의한다. `texturefile`, `animationmaskfile`, `animationtexturefile`은 프로젝트 내부 실제 파일의 상대 경로다. `picture = HOK_KOR_icon_*` 정신과 `icon = GFX_idea_HOK_KOR_icon_*` 주 수정치 모두 해당 로컬 스프라이트에 연결한다.

광택은 기존 `gfx/interface/goals/HOK_KOR/shine_overlay.dds`를 변경 없이 공유한다. 원본은 Paradox Interactive / HOI4 1.19.3의 동명 이미지이며 SHA-256은 `bb416649358c73d34aacd46bad61bc44211fac8111627b56e25f385ad98f4448`이다. 기존의 내부 바닐라 사본이며 공개 팩 CREDITS를 재사용 근거로 적용하지 않는다.

## 정적·시각 검수

실제 크기 접촉표를 직접 확인했다: [입헌](assets/korean-remaining-followup-icons/constitutional.png), [전제](assets/korean-remaining-followup-icons/absolute_monarchy.png), [환제국](assets/korean-remaining-followup-icons/hwan.png), [만주 중점](assets/korean-remaining-followup-icons/manchurian_focuses.png), [공통 중점](assets/korean-remaining-followup-icons/shared_focuses.png), [지역·공통 정신](assets/korean-remaining-followup-icons/regional_and_shared_spirits.png), [소형 결정](assets/korean-remaining-followup-icons/small_decisions.png). 접촉표는 게임 화면이 아니다.

131개 DDS의 형식·해상도·알파·해시, 213개 sprite의 유일성, 132개 내부 이미지 경로(신규 131+기존 광택 1)의 존재·정확한 대소문자, 입력 계약의 ID·단계·색상 연결을 검사했다. 17개 I·II 쌍은 각각 배지 내부 54픽셀만 달라지고 배지 외부는 동일하다. 배경 파생 12개 모두 마스크 밖 픽셀 변화 0·알파 변화 0이다. 이전 `HOK_KOR` 실행용 DDS 190개와 원작 crop 소재 2개, 공개 팩 원본 39개, 공유 오버레이·기존 합성기 해시를 대조했다.

접촉표에서 정책별 소재·6개 색상군, I·II, 기간제 시계, 작은 결정의 여백을 확인했다. 수출 정신의 처음 3부품 구성은 작은 크기에서 책이 과하게 작아져 무역 지구본·화물 상자로 간소화한 후 다시 확인했다. 최종 상태의 알파·경로 검사를 통과한 파일만 프로젝트에 복사한다. 상세 검사 결과는 작업 폴더의 `validation.json`과 `background-validation.json`에 보존한다.

이미지 담당자는 HOI4를 실행하지 않았다. 실제 잠금·진행·완료·광택, 정신과 주 수정치 화면, 결정의 가능/불가/활성 상태 및 다른 GUI 배율은 통합 런타임 검증에서 따로 기록해야 한다. 정적 접촉표와 DDS 검사를 전체 플레이 검증으로 표현하지 않는다.
