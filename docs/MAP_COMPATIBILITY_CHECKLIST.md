# 맵 호환성 점검표

## 핵심 원칙

현재 목표 버전의 바닐라 맵을 기준으로 사용하고, Hearts of Korea의 승인된 한국 변경만 의미 단위로 합친다. 중국·만주·일본은 [중국·일본 1.19.2 바닐라 정렬 정책](CHINA_JAPAN_VANILLA_ALIGNMENT_POLICY.md)에 따라 target을 상속하고 한국에 필요한 최소 접점만 예외로 둔다. 구버전 전역 맵 파일을 현재 버전에 통째로 덮어쓰지 않는다.

현재 프로젝트의 구체적인 target-first 구성안, state 의미 매핑과 영향 파일은 [Hearts of Korea 1.19.2 맵 재구성 설계](HOK_MAP_RECONSTRUCTION_PLAN.md)에 기록한다.

province 또는 state ID의 영구 변경은 단순 정리가 아니라 마이그레이션이다. 세이브, 스크립트, 이벤트, 포커스, AI, 철도, 보급, 서브모드까지 영향을 받을 수 있으므로 사용자의 명시적 승인 전에는 적용하지 않는다.

## 1. 기준 버전과 소유권

- [ ] 목표 HOI4 버전, 빌드, 체크섬을 기록했다.
- [ ] 바닐라 파일은 Steam 설치 경로의 정확한 목표 버전에서 읽었다.
- [ ] 게임 원본과 Workshop 모드를 수정하지 않는다.
- [ ] save, playset, settings와 기존 로그를 승인·백업 없이 덮어쓰거나 삭제하지 않는다.
- [ ] 모드 descriptor와 필수 의존 모드 버전을 기록했다.
- [ ] 저장소와 launcher descriptor의 모든 `replace_path`를 감사하고, 런처가 실제 로드한 물리적 모드 복사본을 확인했다.
- [ ] 각 맵 파일이 바닐라 전체를 대체하는지, 일부 데이터만 추가하는지 확인했다.
- [ ] Hearts of Korea가 의도적으로 변경한 지리 범위를 문서화했다.
- [ ] `V_OLD`, 불변 `HOK_ORIGINAL`, `V_TARGET` 각각의 식별 정보·물리 경로·파일 목록·SHA-256 manifest를 검증했다.

## 2. Province ID와 `definition.csv`

- [ ] 현재 바닐라의 최대 province ID와 전체 ID 집합을 구했다.
- [ ] 모드 전용 province ID를 바닐라와 비교했다.
- [ ] 같은 ID가 의도적으로 같은 바닐라 객체를 override하는지, 서로 다른 province를 뜻하는 실제 충돌인지 구분했다.
- [ ] `provinces.bmp`에 있는 모든 RGB가 `definition.csv`에 정확히 한 번 존재한다.
- [ ] `definition.csv`의 모든 사용 province RGB가 `provinces.bmp`에 존재한다.
- [ ] ID `0`의 합법적인 `(0,0,0)` sentinel과 실제 province를 구분하고, ID 0 이외의 중복 RGB·의도치 않은 검은 픽셀·잘못된 구분자·빈 필드를 검사했다.
- [ ] land/sea/lake 유형과 continent 값이 목표 버전 기준으로 유효하다.
- [ ] coastal 플래그가 실제 인접 관계와 일치한다.
- [ ] 새 ID 후보는 전체 대상 데이터와 의존 모드 ID 공간을 다시 스캔한 후에만 확정한다.

## 3. `provinces.bmp`

- [ ] 이미지 형식, 비트 깊이, 크기, 압축 방식과 팔레트 유무가 목표 버전과 맞는다. 현재 1.19.2 설치본의 기대값도 실제 파일에서 별도로 기록한다.
- [ ] 안티앨리어싱이나 의도하지 않은 새 RGB가 없다.
- [ ] 한 province RGB가 서로 끊긴 불필요한 영역으로 분산되지 않는다.
- [ ] 1픽셀 province, 교차점, 잘못된 해안선 등 형태 오류를 검사했다.
- [ ] 변경 영역 밖의 픽셀이 목표 바닐라와 동일하거나 차이가 설명돼 있다.
- [ ] 로컬 기하 변경은 관련 state, strategic region, buildings, units, supply 데이터와 함께 검증한다.
- [ ] `V_OLD`·`HOK_ORIGINAL`·`V_TARGET`을 동일 좌표로 비교해 원작 변경 후보, 이후 바닐라 변경, 양쪽이 다르게 바꾼 same-pixel conflict를 분리했다.
- [ ] same-pixel conflict와 검토된 변경 범위 밖의 픽셀 차이는 자동 병합하지 않고 수동 판정표에 남겼다.

## 4. State

- [ ] 최종 유효 로드 결과에서 state ID당 정의가 하나이며, 같은 상대경로의 의도적 override와 서로 다른 지역을 뜻하는 실제 ID 충돌을 구분했다.
- [ ] 모든 land province가 정확히 하나의 state에 속한다.
- [ ] 하나의 province가 둘 이상의 state에 포함되지 않는다.
- [ ] 존재하지 않는 province ID를 참조하지 않는다.
- [ ] state 파일명과 내부 `id` 일치는 프로젝트 명명 규약과 리뷰 보조 조건으로 확인하고, 엔진 불변조건으로 단정하지 않는다.
- [ ] owner, core, claim, manpower, category, resources가 의도대로 보존된다.
- [ ] victory point와 building 위치가 해당 state의 province에 속한다.
- [ ] 현재 바닐라가 새로 추가한 한국·일본 인근 state와 의미 충돌을 해결했다.

## 5. Strategic region과 supply area 계열

- [ ] 최종 유효 로드 결과에서 strategic region ID당 정의가 하나이며, 의도한 기존 region override인지 기록했다.
- [ ] province 소속이 목표 버전의 지역 구조와 모드 의도를 함께 만족한다.
- [ ] ID `0` sentinel을 제외한 land/sea/lake의 모든 실제 province가 정확히 한 strategic region에 속하며 누락·중복·존재하지 않는 province·빈 region이 없다.
- [ ] 날씨 및 naval terrain 설정을 목표 바닐라 기준으로 보존했다.
- [ ] 구버전 supply area 파일이 현재 보급 시스템과 충돌하는지 확인했다.

## 6. Adjacency, railway, supply node

- [ ] `adjacencies.csv`의 양 끝 province가 존재한다. 단, 목표 버전 형식의 합법적인 `-1` sentinel과 종료 행은 예외로 구분한다.
- [ ] adjacency 유형, through province 또는 합법적인 `-1` sentinel, 좌표, 주석 형식이 유효하다.
- [ ] 목표 바닐라에 이미 반영된 구버전 adjacency를 중복 추가하지 않는다.
- [ ] 모든 railway 경로 province가 존재하며 육로상 연속된다.
- [ ] railway 레벨과 경로 길이 형식이 유효하다.
- [ ] 모든 supply node가 존재하는 육지 province를 참조한다.
- [ ] state 경계 변경 후 보급망 단절이나 의도하지 않은 해상 연결이 없다.

## 7. Buildings와 unit positions

- [ ] `buildings.txt`의 첫 필드인 state ID가 유효하고, 좌표가 의도한 province 위에 놓이며 새 state 소속 관계와 일치한다.
- [ ] 항구는 실제 coastal province에 놓인다.
- [ ] bunker, air base, naval base, supply 관련 위치가 맵 밖이 아니다.
- [ ] `unitstacks.txt`의 province와 좌표가 유효하다.
- [ ] 기하가 바뀐 province의 위치 데이터는 목표 버전 형식으로 재생성하거나 검증한다.
- [ ] Nudger가 필요하면 사용자에게 실행 및 산출물 반영 승인을 먼저 받는다.

## 8. Heightmap, terrain, rivers, ambient objects

- [ ] 각 비트맵의 크기, 형식, 팔레트/색상 규칙을 목표 바닐라와 비교했다.
- [ ] 구버전 헤더나 팔레트를 현재 파일에 원시 바이트 단위로 복사하지 않는다.
- [ ] 변경 영역 밖의 픽셀 차이를 조사했다.
- [ ] 모드가 덮지 않아 바닐라에서 상속되는 `rivers.bmp`, `trees.bmp`, `cities.bmp`, `world_normal.bmp` 등도 변경 영역과 정렬되는지 감사했다.
- [ ] 목표 바닐라에서 없거나 비어 있는 `positions.txt` 등을 근거 없이 새로 만들지 않는다.
- [ ] 지형 색상이 유효한 terrain 정의를 가리킨다.
- [ ] 강의 연결, 방향, 합류점과 바다 도달을 검사했다.
- [ ] ambient object의 이름, 좌표와 연결 asset이 존재한다.

## 9. 참조 마이그레이션

ID 변경이 승인된 경우에만 수행한다.

- [ ] `old ID -> new ID` 표를 먼저 고정했다.
- [ ] state 문맥과 province 문맥을 분리한 참조 목록을 만들었다.
- [ ] 숫자 occurrence를 `state_ref`, `province_ref`, `coordinate`, `date_or_count`, `other_numeric`, `unknown`으로 분류하고 `unknown`은 자동 변경 대상에서 제외했다.
- [ ] 파일 전체 숫자 치환을 사용하지 않는다.
- [ ] `history/states`, `map`, `events`, `common`, `history/units`, `localisation` 및 의존 모드를 문맥별로 검색했다.
- [ ] 이벤트 target, trigger, effect, focus, decision, AI 전략과 scripted 데이터 참조를 확인했다.
- [ ] 파일명에 포함된 state ID도 함께 처리했다.
- [ ] 세이브 및 서브모드 비호환 가능성을 사용자에게 알렸다.
- [ ] 이전 ID가 남아야 하는 바닐라 province 등 예외를 별도로 기록했다.

## 10. 정적 완료 조건

- [ ] 의도한 override를 적용한 최종 유효 `definition.csv`에서 province ID와 RGB가 각각 고유하다.
- [ ] 존재하지 않는 province/state/region 참조가 없다.
- [ ] 모든 land province의 state 소속이 정확히 하나다.
- [ ] railway와 supply node가 존재하는 올바른 유형의 province만 참조하고, adjacency는 합법적인 sentinel을 제외하면 유효한 province만 참조한다.
- [ ] 변경 범위 밖의 바닐라 데이터 차이가 없거나 모두 설명돼 있다.
- [ ] 정적 검사 결과를 `PASS`, `FAIL`, `NOT RUN`, `BLOCKED`로 기록했다.

## 11. 승인된 런타임 맵 검증

게임 실행이 승인된 경우에만 수행하며 각 항목을 `PASS`, `FAIL`, `NOT RUN`, `BLOCKED`로 기록한다.

- [ ] 최소 유효 playset과 실제 로드된 물리적 모드 경로를 기록했다.
- [ ] 원래 실패 구성의 `D-POST`를 먼저 실행해 `D-PRE`와 비교한 뒤 실제 지원 구성 `C-POST`를 실행했다.
- [ ] 새 게임을 시작하고 관련 bookmark에서 한국을 선택해 실제 맵에 진입했다.
- [ ] 영향 지역의 state 경계, owner/core/claim, victory point, 지형과 해안선을 확인했다.
- [ ] supply, railway, naval base, building과 unit 위치를 각각 표시해 검사했다.
- [ ] 일시정지를 해제하고 1일, 7일, 30일 지점까지 승인된 범위에서 확인했다.
- [ ] persistent ID 또는 map 데이터가 바뀌었다면 새 저장, 프로세스 종료, 재실행, reload와 추가 진행을 확인했다.
- [ ] 같은 구성의 clean start를 최소 두 번 반복해 같은 결과를 확인했다.
- [ ] 선언된 `Korean Language` 계약을 유지한다면 `C-POST`에서 실제 Korean UI, 글꼴과 localisation 표시를 확인했다.
- [ ] 실행 직후 `error.log`, `game.log`와 새 WER 유무를 실행 ID로 묶어 baseline/control과 비교했다.
- [ ] 이전 핵심 `Malformed token` 항목이 사라졌고 새 fatal/assert/map 오류가 없다.
- [ ] 성공 시 새 WER가 생성되지 않았음을 확인했다. 계속 크래시한 경우에만 이전 예외 코드·오프셋과 비교했다.

## 현재 프로젝트의 승인 이후 상태

2026-09-01 fresh 진단과 target 파일 대조에서 계산된 다음 후보는 이후 사용자의 별도 persistent ID 결정으로 **승인·적용**됐다.

- target province `13376–13413`은 그대로 보존하고, HoK 전용 province 34개를 새 entity로 `13414–13447`에 개별 배정
- target 한국 state `525`, `527`, `1028–1031`을 의미에 맞게 재사용하고, 전라·황해·제주·젠다오·안둥·헤이허·쓰시마 7개를 `1082–1088`에 배정
- HoK old state `1017–1027`을 연속 offset으로 이동하지 않고, 지역 의미·province 집합·target counterpart를 기준으로 개별 매핑

구체적인 번호와 근거는 [맵 재구성 설계](HOK_MAP_RECONSTRUCTION_PLAN.md), 역사적 [fresh 맵 격리 사건](incidents/2026-09-01-fresh-map-isolation.md)과 [target-native 맵 구현 기록](incidents/2026-09-01-target-native-map-implementation.md)에 있다. 일반적인 구현 승인만으로 persistent ID를 바꾸는 것은 여전히 금지되며, 이번 변경은 해당 결정을 별도로 받은 사례다. `D-POST`는 통과했고 실제 지원 구성 `C-POST`가 남아 있다.

후속 중국·만주·일본 정렬에서 간도·안둥·헤이허 state `1085–1087` 제거와 target source states 복구가 승인·적용됐다. 최초 후속 구현은 쓰시마를 `1088`에 남겨 effective state ID `1085–1087` 구멍을 만들었고, 첫 `D-CJ-POST`가 20:58:22 map load에서 실패해 이 원인이 확인됐다. 사용자가 승인한 두 번째 후속 마이그레이션은 쓰시마를 `1088 → 1085`로 옮겨 state ID를 `1–1085`로 연속화한다. 이는 이 점검표의 과거 적용 기록을 지우는 것이 아니라 별도의 persistent ID·gameplay 마이그레이션 연쇄다. KOR 기능 disposition, 실패 증거, production 참조와 검증 상태는 [중국·일본 정렬 정책](CHINA_JAPAN_VANILLA_ALIGNMENT_POLICY.md)과 [구현 기록](incidents/2026-09-01-china-japan-vanilla-alignment-implementation.md)을 따른다. 기존 세이브·해당 ID를 참조하는 서브모드 호환성은 주장하지 않는다. scanner v12 targeted static 검증과 post-fix `D-CJ-POST-FIX`의 map 진입·1/7/30일 진행·정상 종료는 `PASS`이며, `C-CJ-POST`와 save/reload는 `NOT RUN`이다.
