# CNDP 남북도별 개발 디시전 아트워크

2026-11-08. 새 주별 사업13개에 전용 **32×32 결정 행 아이콘**을 제작하고 프로젝트 소유 GFX를 등록했다. 이 문서는 그림의 제작·연결 기록이며 게임플레이 구현·실행 결과와 구분한다. [CNDP 개편 문서](HOK_KOREAN_CNDP_STATE_DEVELOPMENT_PLAN.md)를 보완하며, 해당 문서의 과거 계획·검증 상태를 새 그림의 실행 증거로 취급하지 않는다.

## 제작과 출처

공통 소재는 국토개발을 나타내는 크레인과 공장, 중성 회색 바탕, 청동 금속 테두리다. 각 주의 실루엣과 대표 지역 표식으로13개를 구별한다. 기존 완성 아이콘을 축소하거나 공개 이미지 팩 부품을 조합하지 않고, 이번 작업에서 SVG·프로그램 도형을 새로 작성했다. AI 이미지 생성 도구도 사용하지 않았다. 계속개발팀/kpopmodder의 새 도안·프로그램 드로잉·연결 작업이며 코드 작성에 Codex의 지원을 사용했다.

지역 윤곽은 현재 저장소의 `history/states` 소속 목록과 `map/provinces.bmp`·`map/definition.csv`를 **지리 데이터**로 읽어 만들었다. 원본 이미지의 색상·삽화 픽셀을 그림 부품으로 복사하지 않았다. 기존 HOK 원작과 바닐라 지도 계통의 저작·출처는 그대로 보존하고 외부 모드 그림의 포괄 사용 허가를 주장하지 않는다. 대표점은 사업 식별을 돕는 그림 요소이며 새로운 수도·승점·건물 위치를 정의하지 않는다.

정확한 색상, 도별 지리 입력, 도안·원본·레시피·DDS 해시는 [CNDP 아이콘 매니페스트](data/HOK_KOREAN_CNDP_ICON_MANIFEST.json)에 기록했다. 공통 산업 바탕 기준색은 `#64645f`, 금속 강조색은 `#ead5a4`·`#ae8955`·`#5b4129`다.

## 파일과 보관 역할

- 런타임 DDS13개: `gfx/interface/decisions/HOK_KOR/cndp/cndp_<region>.dds`.
- 프로젝트 GFX: [HOK_KOR_cndp_icons.gfx](../interface/HOK_KOR_cndp_icons.gfx). 모든 참조는 모드 루트 상대경로다.
- 신규 사업 ID: `HOK_KOR_cndp_develop_<region>`; 스프라이트: `GFX_HOK_KOR_decision_cndp_<region>`.
- 새 SVG 원본·지리 도안 JSON·C#·PowerShell·Python 레시피: `C:/hoi/test/hok-korean-cndp-state-development-20261108-01/artwork/sources/`와 그 부모의 helper 파일.
- 채택 원본 PNG256×256: `C:/hoi/test/hok-korean-cndp-state-development-20261108-01/artwork/renders/originals/`.
- 실제 크기 PNG와13개 비교표: `C:/hoi/test/hok-korean-cndp-state-development-20261108-01/artwork/renders/png/` 및 `renders/contact-sheet.png`.

작업 원본·비교표·helper는 이번 외부 시험 경로에 보존한다. 이는 [개발 자료 보관 안내](HOK_DEVELOPMENT_ARTIFACT_ARCHIVE.md)와 현행 AGENTS의 필수 외부 산출물 규칙에 따른 것이며, 런타임에서는 외부 파일을 참조하지 않는다. 이전 `.local-artifacts` 보관본을 실행하거나 수정하지 않았다. 기존 원작 그림·카테고리 그림·중점·국민정신 그림은 변경하지 않았다.

## 도별 대응

| 지역 | state | 대표 표식 province | 스프라이트 뒤 이름 |
|---|---:|---:|---|
| 전라북도 | 1082 | 13430 | `jeollabuk` |
| 전라남도 | 1088 | 13424 | `jeollanam` |
| 경상북도 | 1030 | 7121 | `gyeongsangbuk` |
| 경상남도 | 1086 | 4056 | `gyeongsangnam` |
| 충청남도 | 1031 | 11977 | `chungcheongnam` |
| 충청북도 | 1087 | 13446 | `chungcheongbuk` |
| 황해남도 | 1083 | 13438 | `hwanghaenam` |
| 황해북도 | 1091 | 11915 | `hwanghaebuk` |
| 평안남도 | 527 | 4052 | `pyeongannam` |
| 평안북도 | 1089 | 11835 | `pyeonganbuk` |
| 함경남도 | 1028 | 6928 | `hamgyeongnam` |
| 함경북도 | 1090 | 6822 | `hamgyeongbuk` |
| 강원도 | 1029 | 13418 | `gangwon` |

## 확인한 범위

13개 모두32×32,4224바이트, 단일 프레임·단일 레벨의 알파 포함 비압축 BGRA32 DDS다. 피치는128, mipmapCount는0이다. DDS 헤더·마스크·파일 길이·알파 범위·외곽1픽셀 투명 여백,13개 출력 해시의 구별, 스프라이트 이름의 유일성, 파일 경로와 대소문자를 확인했다.

설치본 `interface/countrydecisionview.gui`의 일반 행 높이41·중심(30,19)·이름 시작x63, 기간제 행 높이40·중심(32,20)·이름 시작x62를 읽었다. 새32×32 텍스처의 정적 범위는 각각x14–46/y3–35와x16–48/y4–36이다. GUI나 행 크기를 확대하지 않았다. 과거 [크기 수리 기록](incidents/2026-09-22-korean-decision-icon-size.md)의 전용 소형 이미지 방침을 따른다.

외부 비교표에서13개를 실제32×32와4배 확대 상태로 직접 확인했다. **게임 실행·엔진 등록·실제 사용 가능/불가/진행 중 표시 검증은 이 아트워크 작업에서 수행하지 않았다.** 이후 root의 실행 로그와 실제 화면 확인을 별도 기록해야 한다. 정적 비교표는 게임 스크린샷이나 실제 UI 검증의 대체 증거가 아니다.
