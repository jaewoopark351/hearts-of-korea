# 한국 신규 중점·국민정신 이미지 적용

> 후속 색상 구현 — 2026-09-22: 신규 60개·29개의 배경색을 정치 가지·정책 분야별로 구분했다. DDS 82개를 수정하고 기존 해군·공군 국민정신 7개를 유지했으며 게임 코드·GFX 참조는 유지했다. [색상 구현·검증 기록](2026-09-22-korean-focus-icon-colors.md), [새 색상 비교](../assets/korean-focus-icon-colors/index.html)를 따른다. 아래 기록과 UI 캡처는 색상 변경 전 아이콘 구현의 증거다. 새 색상은 정적 검증 통과이며 이번 작업의 런타임은 미실행이다.

작업일: 2026-09-22. 상태: **구현 완료 / 정적 검증 통과 / 1936 한국 중점 화면 표본 검증 / 국민정신 획득·교체 후 UI 및 중점 상태별 전체 검증 미완료**.

## 범위

사용자가 [초기 아이콘 계획](../HOK_KOREAN_FOCUS_SPIRIT_ICON_PLAN.md)을 바탕으로 구현을 요청했다. 신규 중점 60개와 국민정신 정의 29개의 이미지 참조를 교체했다. 원작 중점 266개, 기존 국민정신, 게임 효과·보상·AI·좌표·선행조건·상호배타·기간·이벤트·결정·현지화는 유지한다. 새 아이콘의 도입은 후속 시각 개선이며 호환성 복구나 밸런스 조정이 아니다.

29개에는 교체 단계 및 외국 협정 수혜국용 정의가 포함된다. 한국에 동시에 29개를 표시하도록 바꾸지 않았다. 최초 확장 기록의 28개는 당시 수량으로 보존한다.

## 기준선

| 항목 | 확인한 상태 |
|---|---|
| 소스 | `feat/korean-focus-expansion-ai`, `698b6eb160efbaa04a4d43846330ba002f5e8cc7` |
| 작업 전 변경 | `README.md`의 기존 계획 링크 1줄, untracked 초기 아이콘 계획서. 원래 내용을 보존하고 후속 링크·상태 안내만 추가 |
| 설치본 | Operation Postern `v1.19.3.0.c01a`, 설치 메타데이터 checksum `5632`, Steam build `25205862` |
| 이전 실제 실행 | 2026-09-22 03:16, `1.19.3.0.c01a (68ca)` |
| 이번 실행 | 새 프로세스, 메인 메뉴 표시 `1.19.3.0.c01a (5e4e)`, 1936-01-01 한국, 일시정지 상태 |
| 표시 환경 | Windows, 1600×900 게임 영역, `l_korean`, 설치된 DLC 36개 활성 |
| 활성 모드 | `mod/hearts of korea.mod` 1개; 실제 경로는 저장소. 플레이셋의 표시 이름은 확인하지 않음 |
| 언어 모드 | descriptor가 `Korean Language`를 선언하지만 현재 활성 목록에는 없음. 사용자 설정·의존성은 변경하지 않음 |
| descriptor | `supported_version="1.19.*"`, `remote_file_id="3793992662"`, `replace_path` 없음; 수정하지 않음 |
| 원작 Workshop | `2898629778`은 출처용. 원작·설치본은 수정하지 않음 |

실제 사용자 데이터는 사용자가 지정한 OneDrive 문서의 HOI4 디렉터리에서 확인했다. 기존 로그와 수정 대상 4파일, README, descriptor, 계획서는 `.local-artifacts/korean-focus-icons/before/`에 보존했다. 로그·스크린샷·작업 스크립트·다운로드 원본은 `.local-artifacts/`에 두어 Git에서 제외한다.

## 확인된 문제와 적용 방향

`CONFIRMED`: 이전 신규 중점 60개는 아이콘 참조 29종, 국민정신 29개는 그림 참조 9종이었다. 산업 국민정신 11개 중 10개와 전체 29개 중 14개가 `generic_production_bonus`를 참조했다. 서로 다른 정책의 의미가 같은 그림에 집중된 것을 시각적으로 구분하는 작업이다. 엔진 오류를 수정했다고 주장하지 않는다.

- 전력, 숙련공, 야간학교, 양산, 유연생산, 검사·품질을 서로 다른 소재로 구성했다.
- 함대 수리·호위·보급 및 편대·항공정비를 구분했다. 작은 가로 실루엣으로 잘 보이지 않던 수리·기동훈련·조선의 함선은 정면 함선 소재로 보완했다.
- 실제 교체 계열에만 I·II·III 배지를 붙였다. 연결된 중점과 국민정신은 같은 중심 소재를 사용한다.
- 통합 생산계획은 양산과 유연생산 모두를 나타내는 설계도·기어·전환 화살표를 사용한다. 선택하지 않은 정책을 시각적으로 강요하지 않는다.
- 의료지원은 가방과 의료 표식, 동계훈련은 철모와 눈송이, 농촌교육은 책과 밀 이삭, 관세는 통상·서류, 면허는 설계도·서명 소재로 구성했다.

## 출처와 가공

[Ultimate HOI4 GFX](https://github.com/Globvs/Ultimate-HOI4-GFX)의 커밋 `3626dc83c8573d6603fa497138090b04b64a15ba`에서 실제 사용한 PNG는 **48개**다. CREDITS의 기여자 동의·자유 사용 선언을 해당 팩 범위의 근거로 사용했다. [원문 사본](../assets/korean-focus-icons/UPSTREAM_CREDITS.txt)을 byte-exact로 보존했다. 개별 파일의 원저자를 임의로 추정하지 않고 모음집 기여자 명단을 보존한다.

PNG 부품을 그대로 완성 DDS라고 소개하지 않는다. 실제 작업은 알파 영역 정리, 비율 유지 크기 조절, 프레임·중심 소재 합성, 단계·의료·검사·눈송이 표식 추가, 잠수함 명암 보완, DDS 변환이다. 원본 소재와 후속 가공의 기여를 구분했다. AI 이미지 생성은 사용하지 않았다. Europe Anew·Kaiserreich·Road to 56 자산은 이번 산출물에 포함하지 않는다.

이름이 실제 그림과 다른 부품을 직접 검수했다. `Boot.png`는 철모, `Hammer.png`는 의사봉으로 사용했다. 현대 스마트폰·현대식 고층병원·만주 상징 등 주제에 맞지 않는 후보는 제외했다. 정확한 파일·URL·원본 해시·출력 해시는 [자산 매니페스트](../data/HOK_KOREAN_FOCUS_ICON_MANIFEST.json), 기여자와 상세 가공 내역은 [크레딧](../HOK_KOREAN_FOCUS_ICON_CREDITS.md)을 따른다.

## 변경 파일과 엔진 연결

| 파일·경로 | 변경 |
|---|---|
| `common/national_focus/korea.txt` | 신규 60개 정의의 `icon` 및 바로 위 기여자 주석 |
| `common/ideas/HOK_KOR_industry_expansion.txt` | 11개 `picture` 및 기여자 주석 |
| `common/ideas/HOK_KOR_military_expansion.txt` | 12개 `picture` 및 기여자 주석 |
| `common/ideas/HOK_KOR_democratic_expansion.txt` | 6개 `picture` 및 기여자 주석 |
| `interface/HOK_KOR_focus_icons.gfx` | 전용 일반 sprite 60개 |
| `interface/HOK_KOR_focus_icons_shine.gfx` | 전용 광택 sprite 60개 |
| `interface/HOK_KOR_spirit_icons.gfx` | 전용 국민정신 sprite 29개 |
| `gfx/interface/goals/HOK_KOR/` | 100×88 DDS 60개 |
| `gfx/interface/ideas/HOK_KOR/` | 60×68 DDS 29개 |

새 파일·sprite에 기존 `HOK_KOR_` 접두사를 사용했다. 전역 바닐라 sprite를 덮어쓰거나 새 모드 의존성을 추가하지 않았다. 국민정신의 `picture`는 `GFX_idea_` 접두사의 전용 sprite로 연결한다.

DDS는 설치된 1.19.3의 `focus_generic_electrification.dds` 및 `generic_production_bonus.dds` 헤더와 동일한 비압축 32-bit BGRA·알파·크기를 사용했다. 일반 sprite는 `interface/goals.gfx` 및 `ideas.gfx`, 광택은 `goals_shine.gfx:67003`의 전력 아이콘 사례를 따른다. 광택은 동일 DDS 마스크, `buttonstate.lua`, `shine_overlay.dds`, ±90° scrolling 두 블록, 0.75초, 2×1 및 1×1 scale, `legacy_lazy_load=no`를 보존한다.

## 검증

| 항목 | 결과 |
|---|---|
| 범위·내용 보존 | `PASS`: 기존 4파일에서 새 참조·이번 주석을 되돌리면 수정 전 바이트와 동일. 별도 ordered-token 검사도 동일 |
| 수량·연결 | `PASS`: 대상 60/29, 텍스처 89, sprite 149. 누락·중복 참조 없음 |
| 실제 이미지 구별 | `PASS`: 중점 DDS 해시 60종, 국민정신 DDS 해시 29종. 단계별 공통 소재는 유지 |
| 문법·파일 형식 | `PASS`: 괄호·따옴표·BOM·개행, DDS 치수·크기·RGBA masks·비어 있지 않은 알파·투명 배경·경로 대소문자 |
| 충돌 | `PASS`: 저장소·바닐라·활성 모드 및 설치된 Korean Language sprite 이름 검색에서 새 ID 충돌 없음 |
| 전수 정적 시각 검수 | `PASS`: 4개 전후 비교표에서 89개 이미지 확인. 겨울 표식·함선 소재를 보완하고 다시 검수 |
| 새 프로세스 로드 | `PASS`: 1.19.3 메인 메뉴 및 1936 한국 새 게임 진입 |
| 중점 UI 표본 | `PASS`: 산업·군사·민주 내정·아시아 외교 가지의 화면에 새 이미지 표시, 생산품 품질보증 상세창의 정상 이미지·35일·차단 선행조건 확인 |
| 로그 비교 | `PASS`: 시간·게임날짜를 제외한 새 오류 유형 0개, 증가한 유형 0개. 신규 sprite·DDS 경로 오류 0개 |
| 중점 상태별 전수 | `NOT RUN`: 60개 각각의 진행·완료·잠금/해제·광택 재생 전체 조합 |
| 국민정신 실제 획득·교체 | `NOT RUN`: 국가 화면에서 29개 단계별 획득·교체, 외국 협정 수혜국 표시 |
| 기타 | `NOT RUN`: 1939, 다른 DLC 구성·언어 모드 활성 구성, 장기 진행, 기존 세이브, 멀티플레이 |

정적 결과는 `.local-artifacts/korean-focus-icons/validation.json`에 보존한다. UI 증거는 같은 작업 폴더의 `runtime/industry.png`, `military.png`, `democratic.png`, `diplomacy.png`, `quality-detail.png`다. 이는 화면에 실제로 보이는 표본의 증거이며 60개 전수 런타임 검수로 확대하지 않는다.

로그 비교 결과는 같은 폴더의 `runtime/log-comparison.json`을 따른다. 기존 별도 콘텐츠 오류를 이번 아이콘 작업에서 수정하거나 전체 로그가 깨끗하다고 주장하지 않는다.

비교 대상은 이전 344줄·62종과 이번 128줄·40종이다. 이전 로그가 더 긴 게임플레이를 포함하므로 총 줄 수 감소를 개선 성과로 해석하지 않는다. `setup.log`의 6·11·12개 국민정신 파일 로드와 실제 UI 표본은 확인했지만, 개별 GFX 등록 이름을 setup 로그에서 확인했다고 주장하지 않는다.

## 산출물과 남은 범위

- [89개 전후 비교 갤러리](../assets/korean-focus-icons/index.html): HTML에 그림을 내장하여 독립 열람 가능. 게임 캡처와 구분한 정적 비교다.
- [산업 중점](../assets/korean-focus-icons/focus-industry.png), [군사 중점](../assets/korean-focus-icons/focus-military.png), [민주 중점](../assets/korean-focus-icons/focus-democratic.png), [국민정신](../assets/korean-focus-icons/national-spirits.png) 비교표.
- 공개 원본의 정확한 사용 근거·크레딧·해시와 각 대상의 가공 내역을 함께 기록했다. 다운로드한 나머지 미채택 소재는 게임 패키지에 넣지 않았다.

게임 효과·ID를 유지했다는 정적 증거만으로 세이브·멀티플레이 호환성을 입증하지 않는다. 현재 구성에서 확인한 중점 UI 표본 외의 런타임 항목은 위 표에 남겼다. 업로드·외부 계정·제작자 연락·커밋·푸시는 수행하지 않았다.

검수용 새 게임은 1936-01-01 일시정지 상태로 남겼다. 기존 저장을 불러오거나 덮어쓰지 않았으며, 테스트용 국민정신 강제 부여·중점 강제 완료·영구 진단 스크립트 추가는 하지 않았다.
