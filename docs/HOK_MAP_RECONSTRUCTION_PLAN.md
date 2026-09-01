# Hearts of Korea 1.19.2 맵 재구성 설계

## 문서 상태

- 작업 단계: **Implementation 적용 / static validation 완료 / D-POST 통과 / C-POST 대기**
- 목표 게임: HOI4 `1.19.2.0.a729 (d245)`
- 목표 방식: **V_TARGET-first HoK 지리 재구성**
- production 맵 수정: **사용자 명시 승인 / 적용**
- province·state 영구 ID 마이그레이션: **사용자 명시 승인 / 적용**
- 정확한 `V_OLD` 3-way: **BLOCKED**
- 런타임 완료 판정: **PARTIAL — D-POST PASS, C-POST NOT RUN**

이 문서는 현재 1.19.2 바닐라 전역 맵을 보존하면서 HoK의 한국·만주·쓰시마 지리를 다시 이식하기 위한 설계, 증거 등급, 영향 범위와 승인 게이트를 고정한다. 2026-09-01 사용자가 이 문서의 target-native 정책, 개별 ID 매핑, 새 게임 전용 호환성 정책과 production 구현을 명시적으로 승인했다. 실제 적용과 정적 검증 결과는 [target-native 맵 구현 기록](incidents/2026-09-01-target-native-map-implementation.md)에 기록한다.

이 문서는 시작 크래시 복구 당시의 구현 기준과 현재 적용 상태를 보존한다. 후속 중국·만주·일본 정렬에서는 [중국·일본 1.19.2 바닐라 정렬 정책](CHINA_JAPAN_VANILLA_ALIGNMENT_POLICY.md)이 우선한다. 현재 적용된 만주 state `1085–1087`과 관련 delta는 target 복구 후보지만 KOR 기능 disposition과 persistent ID 승인을 받기 전에는 되돌리지 않는다. 해당 후속 정책은 아직 문서화만 됐고 production 데이터에는 적용되지 않았다.

관련 문서:

- [크래시 디버깅 런북](CRASH_DEBUGGING_RUNBOOK.md)
- [맵 호환성 점검표](MAP_COMPATIBILITY_CHECKLIST.md)
- [중국·일본 1.19.2 바닐라 정렬 정책](CHINA_JAPAN_VANILLA_ALIGNMENT_POLICY.md)
- [2026-09-01 fresh 맵 격리 사건](incidents/2026-09-01-fresh-map-isolation.md)
- [2026-09-01 target-native 맵 구현 기록](incidents/2026-09-01-target-native-map-implementation.md)
- [기존 시작 크래시 사건](incidents/2026-08-31-startup-crash.md)
- [맵 fresh scan 감사](audits/2026-08-31-map-fresh-scan.md)

## 1. 결론

HoK의 구형 `map/` 폴더를 1.19.2에 그대로 덮는 방식으로는 복구할 수 없다. 최종 후보는 다음 원칙으로 만든다.

```text
V_TARGET 전역 맵
+ 검토된 HoK 한국 province geometry
+ 의미 기반 state 재분할
+ 검토된 전략 지역·철도·보급·위치 delta
+ 문맥별 ID 참조 마이그레이션
= 1.19.2용 HoK successor map candidate
```

`provinces.bmp`와 `definition.csv`는 파일 내부 일부만 런타임에서 patch되는 구조가 아니다. 모드가 같은 상대경로의 파일을 제공하면 완성된 전역 파일이 로드되므로, 최종 산출물은 **1.19.2 전 세계 데이터를 포함한 완전한 target-derived 파일**이어야 한다. 한국 부분만 HoK 의도에 따라 달라져야 한다.

## 2. 현재 진단 근거

| 실행 | 구성 | 관찰 | 판정 |
|---|---|---|---|
| `A-FRESH-2026-09-01` | 바닐라, `--debug`, DLC 36 | province 13,414개, 양쪽 history 단계와 startup 완료, exit code 0, 새 crash 없음 | 바닐라 control `PASS` |
| `D-FRESH-2026-09-01` | 현재 저장소 HoK만, `--debug`, DLC 36 | province 13,410개, 첫 history 단계에서 종료, `C0000005`, `IsMapInGoodState: no` | `FAIL` |
| `D-NOMAP-FRESH-2026-09-01` | HoK에서 `map/`과 `history/states/`만 제외 | province 13,414개, 양쪽 history 단계와 startup/session change 완료, 새 crash 없음 | 시작 경계 통과. 실행 harness·exit code 부재로 제한적 |
| `D-MAPONLY` | HoK의 `map/`과 `history/states/`만 포함 | 아직 실행하지 않음 | `NOT RUN` |
| `D-POST` | target-native HoK 단독 | 새 게임·맵 진입·unpause 후 최소 1937.01.01까지 진행, 새 crash 없음 | `PASS` |
| `C-POST` | 수정 HoK + `Korean Language` | 아직 실행하지 않음 | `NOT RUN` |

현재 증거 등급은 다음과 같다.

- **CONFIRMED** — HoK 맵을 로드한 `D-FRESH`에는 state ID 충돌, malformed province, 중복·누락 membership과 실제 crash가 있다.
- **CONFIRMED** — 바닐라 `A-FRESH`는 같은 설치본과 DLC 집합에서 startup을 완료했다.
- **CONFIRMED** — `D-NOMAP`에서는 맵 오류가 사라지고 원래 crash 경계를 통과했다.
- **STRONGLY_SUPPORTED** — HoK의 `map/` + `history/states/` 묶음은 `D-FRESH` 시작 crash의 필수 기여 요인이다.
- **UNPROVEN** — 어느 단일 map invariant 또는 엔진 함수가 `C0000005`를 직접 일으켰는지.
- **CONFIRMED** — 적용된 재구성안은 `D-POST`에서 기존 시작 crash 경계를 통과했다.
- **UNPROVEN** — 실제 지원 구성 `C-POST`가 같은 결과를 내는지.

`D-NOMAP`에 남은 MIO, 일본 decision/focus/character, doctrine와 technology 오류는 startup을 막지 않았다. 이들은 맵 복구 뒤 [중국·일본 바닐라 정렬 정책](CHINA_JAPAN_VANILLA_ALIGNMENT_POLICY.md)과 별도 후속 사건으로 처리한다.

## 3. HoK가 지도를 구성한 방식

HoK는 작은 한국 전용 patch 파일만 제공하지 않는다. 같은 크기의 전 세계 bitmap과 여러 전역 데이터 파일을 구형 바닐라 기준으로 보유한다.

```text
map/provinces.bmp
  RGB 픽셀로 province geometry 정의
        ↓
map/definition.csv
  RGB ↔ province ID·유형·해안·지형·대륙 연결
        ↓
history/states/*.txt
  province를 state로 묶고 owner/core/resource/building/VP 부여
        ↓
map/strategicregions/*.txt
  province를 전략 지역에 배정
        ↓
map/railways.txt + map/supply_nodes.txt
  province 기반 보급망 구성
        ↓
map/buildings.txt + map/unitstacks.txt
  state/province 및 실제 좌표 배치
        ↓
country history / OOB / focus / event / decision / AI / localisation
  persistent ID를 게임 콘텐츠에서 참조
```

현재 HoK가 제공하는 전역 또는 맵 연관 파일은 다음과 같다.

- `map/definition.csv`, `map/provinces.bmp`
- `map/heightmap.bmp`, `map/terrain.bmp`
- `map/adjacencies.csv`, `map/ambient_object.txt`
- `map/buildings.txt`, `map/unitstacks.txt`
- `map/railways.txt`, `map/supply_nodes.txt`
- strategic region `76`, `143`, `154`, `155`, `186`, `243`, `244`
- 한국·만주·쓰시마 관련 `history/states`

HoK에 없는 `rivers.bmp`, `trees.bmp`, `cities.bmp`, `world_normal.bmp` 등은 target 바닐라에서 상속된다. 따라서 구형 HoK의 `heightmap.bmp`·`terrain.bmp`와 현재 상속 파일을 혼합하면 부분 합성 위험이 있다.

## 4. Province 기준선과 재구성 정책

### 4.1 확인된 기준선

- target `provinces.bmp`: `5632×2048`, 24-bit RGB
- HoK `provinces.bmp`: `5632×2048`, 24-bit RGB
- target `definition.csv`: ID `0–13413`, province 13,414개
- HoK `definition.csv`: ID `0–13409`, province 13,410개
- HoK 전용 지리 후보: old province `13376–13409`, 34개
- fresh scan RGB 집합 비교: target-only RGB 38개, HoK-effective-only RGB 34개, geometry identity는 아직 `UNPROVEN`

현재 바닐라는 ID `13376–13409`를 동남아시아·중국 등 다른 실제 province로 사용하며 `13410–13413`도 사용한다. 따라서 target의 `13376–13413`은 그대로 보존한다.

### 4.2 승인·적용 정책

1. target `provinces.bmp`를 base로 사용한다.
2. HoK-only 34개 RGB가 차지하는 픽셀을 식별한다.
3. 각 픽셀이 검토된 한국 변경 영역 안에 있는지, target 한국 landmass를 벗어나지 않는지 검사한다.
4. 연결 성분, 1픽셀 조각, 해안, land/sea 분류와 인접 관계를 검사한다.
5. 검증된 픽셀만 target bitmap에 overlay한다.
6. HoK province 34개에는 target 최대 ID 뒤의 새 ID 후보를 개별 배정한다.
7. 각 새 ID의 RGB, geometry, state, strategic region과 모든 참조를 entity registry에 기록한다.

예약 구간 `13414–13447`과 개별 old ID → new ID registry는 사용자 승인 뒤 적용됐다. 숫자 배열은 연속이지만 old `13376–13409`에 무조건적인 전역 `+38` 치환을 적용한 것이 아니다. 각 province의 지리적 정체성, RGB와 참조 문맥을 개별 확인했다.

### 4.3 `V_OLD`가 없는 한계

정확한 Vanilla 1.16.x `V_OLD`가 없으므로 HoK와 target의 전역 bitmap 차이를 모두 원작자의 의도로 판정할 수 없다.

- `V_OLD`를 확보하면 정식 3-way로 `INTENDED_DELTA`를 산출한다.
- `V_OLD` 없이 진행하려면 사용자가 **target-native reconstruction**을 별도로 선택해야 한다.
- 이 경우에도 HoK-only 34개 RGB와 한국 내 geometry를 근거로 제한하며, 결과를 “정확한 1.16 원형 delta”로 표현하지 않는다.
- 구형 전역 `heightmap.bmp`, `terrain.bmp`, `ambient_object.txt`를 자동 승계하지 않는다.

## 5. State 의미 매핑 — 승인·적용

target 바닐라 한국은 `525`, `527`, `1028–1031`의 6개 state로 구성되며, 이 여섯 state의 province 집합은 HoK 한국 state에서 custom 34개를 제외한 기존 province 69개를 정확히 분할한다.

| target state | target 파일 의미 | province 수 | 1936 history |
|---:|---|---:|---|
| `525` | South Korea | 4 | JAP owner, KOR core |
| `527` | North Korea | 19 | JAP owner, KOR core |
| `1028` | Hamgyong | 20 | JAP owner, KOR core |
| `1029` | Gangwon | 8 | JAP owner, KOR core |
| `1030` | Gyeongsang | 8 | JAP owner, KOR core |
| `1031` | Chungcheong Jeolla | 10 | JAP owner, KOR core |

합계는 69개다. HoK는 이 기존 집합을 다시 나누고 한국 내부에 custom province 34개를 추가했다.

HoK 한국은 경기·강원·충청·경상·평안·황해·제주·전라·함경의 9개 state로 구성된다. 젠다오·안둥·헤이허·쓰시마까지 포함하면 이식 대상은 13개 의미 state다.

| 의미 지역 | HoK old ID | proposed target ID | 근거 | 상태 |
|---|---:|---:|---|---|
| 경기 | `1017` | `525` | target 남부 한국의 수도권 의미를 기존 한국 ID에 보존 | 승인·적용 |
| 평안 | `1021` | `527` | target 북부 한국 ID에 평안 의미 보존 | 승인·적용 |
| 함경 | `527` | `1028` | target의 현재 Hamgyong ID 사용 | 승인·적용 |
| 강원 | `1018` | `1029` | target의 현재 Gangwon ID 사용 | 승인·적용 |
| 경상 | `1020` | `1030` | target의 현재 Gyeongsang ID 사용 | 승인·적용 |
| 충청 | `1019` | `1031` | target의 결합 state에서 충청 의미를 기존 ID에 보존 | 승인·적용 |
| 전라 | `525` | `1082` | target `1031`에서 분리되는 추가 state | 승인·적용 |
| 황해 | `1022` | `1083` | target `527`에서 분리되는 추가 state | 승인·적용 |
| 제주 | `1023` | `1084` | target 한국에서 분리되는 추가 state | 승인·적용 |
| 젠다오 | `1024` | `1085` | target source state `328`·`717`에서 분리 | 승인·적용 |
| 안둥 | `1025` | `1086` | target source state `328`·`716`에서 분리 | 승인·적용 |
| 헤이허 | `1026` | `1087` | target source state `714`에서 분리 | 승인·적용 |
| 쓰시마 | `1027` | `1088` | target source state `528`에서 분리 | 승인·적용 |

이 표는 현재 바닐라의 한국 ID 의미를 최대한 보존하고 충돌하는 target state `1017–1027`을 건드리지 않는 승인된 매핑이다. 숫자 전역 치환 규칙이 아니며, 기존 save와 persistent map ID를 참조하는 submod는 비호환으로 선언했다.

### 5.1 영향받는 target state 파일

한국 6개:

- `525-South Korea.txt`
- `527-North Korea.txt`
- `1028 - Hamgyong.txt`
- `1029 - Gangwon.txt`
- `1030 - Gyeongsang.txt`
- `1031 - Chungcheong Jeolla.txt`

주변 source state 5개:

- `328-Manchukuo.txt`: 젠다오·안둥 후보 province 일부를 내줌
- `714-Heilungkiang.txt`: 헤이허 후보 province를 내줌
- `716-Liaotung.txt`: 안둥 후보 province 일부를 내줌
- `717-Chuho.txt`: 젠다오 후보 province 일부를 내줌
- `528-Nagasaki.txt`: 쓰시마 province `10011`을 내줌

새 state를 추가할 때 source state에서 같은 province를 반드시 제거한다. 모든 land province는 최종 유효 로드 결과에서 정확히 한 state에만 속해야 한다.

## 6. Strategic region 정책

state 경계를 나누는 것만으로 strategic region membership을 바꿀 필요는 없다. province가 어느 state에 속하는지와 어느 strategic region에 속하는지는 별도 관계다.

- target 한국 기존 province 69개는 region `186`에 있다.
- 새 한국 custom province 34개는 검토 후 region `186`에 추가하는 것이 기본안이다.
- 젠다오 기존 province는 target region `243` 소속을 보존한다.
- 안둥 기존 province는 target region `155`와 `243` 소속을 보존한다.
- 헤이허 기존 province는 target region `242` 소속을 보존한다.
- 쓰시마 `10011`은 target region `300` 소속을 보존한다.

따라서 구형 HoK strategic region 7개를 통째로 이식하지 않는다. target 파일을 기준으로 실제 membership delta가 필요한 region만 수정한다. 현재 설계상 우선 후보는 새 custom province를 받는 region `186`이다.

## 7. 철도·보급·adjacency

### 7.1 Railway와 supply node

target `railways.txt`와 `supply_nodes.txt`를 base로 사용한다. HoK의 구형 전역 파일을 복사하지 않는다.

- target 한국에는 기존 supply node `4052`, `4056`, `6928`, `7125`, `11948`, `11977`이 있다.
- HoK는 custom old province `13380`, `13386`, `13398`에 추가 supply node를 둔다.
- HoK 철도는 old custom province를 포함한 여러 local route를 가진다.

각 HoK node와 route는 새 province 매핑 후 다음을 판정한다.

1. target 기존 node·rail과 중복인지
2. HoK 밸런스와 시작 보급 의도에 필요한지
3. 모든 경로 province가 존재하고 실제 육로로 인접하는지
4. state 분할 뒤 항구·수도·보급 중심 연결이 유지되는지

### 7.2 Special adjacency

target의 다음 연결은 기본적으로 보존한다.

- 한반도 `11948` ↔ 제주 `1177`
- 쓰시마 `10011` ↔ 규슈 `7110`

HoK custom `13376–13409`를 직접 사용하는 special adjacency는 현재 확인되지 않았다. 새 geometry가 실제 해협 연결을 요구한다는 증거가 있을 때만 행을 추가하거나 수정한다. 합법적인 `-1` sentinel과 종료 행을 보존한다.

## 8. Buildings, unitstacks와 좌표

`buildings.txt`와 `unitstacks.txt`는 전역 좌표 데이터다. 구형 파일 전체 복사나 state/province ID의 기계적 치환을 사용하지 않는다.

- target 파일을 기준으로 영향 state의 배치를 공간적으로 다시 분류한다.
- 새 province geometry 위의 naval base, floating harbor, bunker, air base 등 좌표를 확인한다.
- state ID가 바뀐 배치 행은 실제 좌표가 속한 새 state로 옮긴다.
- 새 province에 필요한 unit stack 위치는 target 형식으로 검증하거나 승인된 Nudger 산출물로 재생성한다.
- Nudger 출력은 user-data 경로에 생길 수 있으므로 별도 승인·검토 후 필요한 행만 가져온다.

## 9. Heightmap, terrain과 상속 파일

첫 구현 후보에서는 다음을 기본값으로 한다.

- `heightmap.bmp`: target 유지
- `terrain.bmp`: target 유지
- `rivers.bmp`, `trees.bmp`, `cities.bmp`, `world_normal.bmp`: target 상속 유지
- `ambient_object.txt`: `V_OLD` 3-way 또는 독립적인 원작 객체 증거가 있을 때만 국소 병합

HoK-only province가 기존 target 한국 land province를 내부적으로 세분하는 데 그친다는 geometry 검사가 통과하면, province 경계 이식만으로 heightmap 전체를 바꿀 이유가 없다. 해안선·landmass·고도 또는 terrain을 실제로 바꾼 픽셀이 발견되면 해당 bitmap을 별도 workstream으로 올린다.

## 10. 국가·스크립트·localisation 참조

영구 ID를 바꾸면 다음 문맥을 모두 의미 기반으로 이전한다.

- `history/countries/KOR - Korea.txt`의 `capital = 1017`
- state 파일명과 내부 `id`
- owner, controller, core, claim, victory point와 building block
- OOB, unit history, focus, event, decision, on_action
- scripted trigger/effect, AI strategy, achievement와 기타 numeric reference
- `STATE_1017–1027` 및 victory point localisation key

현재 `STATE_1017–1027`을 한국 지명으로 덮는 localisation을 그대로 두면 target의 베트남·일본·동남아·필리핀 state 이름이 한국 지명으로 표시된다. 새 state 의미에 맞춰 key를 이동하고 target `1017–1027` 의미를 침범하지 않아야 한다.

localisation의 언어 header와 `Korean Language` 의존 정책은 [별도 사건](incidents/2026-09-01-localisation-contract.md)에서 결정한다. 맵 ID migration과 언어 namespace migration을 한 번에 섞지 않는다.

## 11. 구현 work package 제안

각 package는 별도 diff와 검증 결과를 가진다.

1. **WP-0 — 기준선·결정**
   - `V_OLD` 확보 또는 target-native reconstruction 명시 선택
   - province/state registry와 save/submod 정책 승인
2. **WP-1 — Province topology**
   - target-derived `provinces.bmp`, `definition.csv`
   - 34개 geometry와 새 ID만 병합
3. **WP-2 — State topology/history**
   - 한국 6개 target state, source state 5개, 새 state 7개
   - owner/core/manpower/resource/building/VP 검토
4. **WP-3 — Strategic region·adjacency**
   - region `186` 중심의 최소 membership delta
   - target special adjacency 보존
5. **WP-4 — Railway·supply**
   - target 보급망에 검토된 HoK local delta 병합
6. **WP-5 — Position data**
   - buildings와 unitstacks 공간 재할당·검증
7. **WP-6 — Script/localisation migration**
   - 문맥별 old ID → new ID 적용
8. **WP-7 — Static validation**
   - RGB, membership, topology, references, 좌표 검사
9. **WP-8 — Runtime validation**
   - `D-POST`, `C-POST`, 새 게임, 1·7·30일, save/reload

WP-1부터 WP-6은 영구 map ID 마이그레이션과 production 구현이 명시적으로 승인된 뒤에만 시작한다.

## 12. 금지되는 구현 방식

- HoK 구형 `map/` 폴더 전체를 target에 덮어쓰기
- `definition.csv`에 `13410–13413` 네 줄만 추가
- old province에 `+38`, old state에 `+65`를 전역 적용
- `replace_path`로 충돌하는 target state나 region 전체를 숨기기
- 동일 숫자의 문맥을 확인하지 않은 일괄 search-and-replace
- target `13376–13413` province를 HoK 지리로 재사용
- target `1017–1027` state를 HoK 지리로 재사용
- `V_OLD` 없이 전역 heightmap·terrain 차이를 원작 의도로 간주
- 메인 메뉴 진입만으로 복구 완료 판정

## 13. 승인 기록과 남은 게이트

다음 결정은 서로 별도다.

1. 정확한 `V_OLD`를 확보해 3-way 복원을 기다릴지, 근거가 제한된 target-native reconstruction을 허용할지
2. HoK province 34개의 개별 old ID → new ID registry
3. 위 state 의미 매핑표
4. 기존 세이브와 서브모드를 비호환으로 선언할지, 별도 migration을 제공할지
5. production 맵 구현 시작
6. HOI4 런타임 검증 실행

일반적인 “크래시 수정” 승인을 persistent ID migration 승인으로 확대 해석하지 않는다.

2026-09-01 사용자는 위 1–5번의 target-native 선택, entity registry, state 매핑, 새 게임 전용 비호환 정책과 production 구현을 명시적으로 승인했다. 6번 중 HoK 단독 `D-POST`는 통과했지만 실제 지원 구성 `C-POST`, 육안 점검과 save/reload는 완료 판정의 남은 게이트다.

## 14. 완료 조건

정적 조건:

- province ID와 RGB가 각각 고유함
- bitmap의 모든 실제 RGB가 definition에 있고 역방향도 성립함
- 모든 land province가 정확히 한 state에 속함
- 모든 실제 province가 정확히 한 strategic region에 속함
- unknown province/state/region 참조가 없음
- railway가 존재하는 인접 land province로 연속됨
- supply node와 건물·유닛 위치가 유효함
- 변경 영역 밖의 target 데이터가 보존됨

런타임 조건:

- `D-POST`가 원래 `D-FRESH` crash 경계를 통과함
- 실제 지원 구성 `C-POST`가 startup을 통과함
- 한국 선택 후 맵 진입, unpause 1일·7일·30일 통과
- owner/core/VP/resource, 전략 지역, 보급, 철도, 항구, 건물과 유닛 위치가 의도대로 표시됨
- 새 저장, 프로세스 종료, 재실행, reload와 추가 진행 통과
- 새 관련 fatal/assert/map error와 새 WER가 없음
- 남은 비맵 오류는 별도 사건으로 분리됨

이 조건을 통과하기 전에는 `supported_version = 1.19.*` 또는 공개 제목을 실제 호환성 증거로 사용하지 않는다.
