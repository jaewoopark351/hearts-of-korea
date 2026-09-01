# 2026-09-01 target-native 맵 구현 기록

> 후속 상태: 이 문서는 시작 크래시를 제거한 당시 구현과 검증의 역사적 기록이다. 이후 결정된 중국·만주·일본 target 정렬 범위는 [중국·일본 1.19.2 바닐라 정렬 정책](../CHINA_JAPAN_VANILLA_ALIGNMENT_POLICY.md)에 기록한다. 해당 정책은 현재 문서화만 됐으며, 이 기록에 나온 state `1085–1087`과 관련 production delta는 아직 되돌리지 않았다.

## 판정

- 작업 모드: **Implementation / static and runtime validation**
- 목표 게임: HOI4 `1.19.2.0.a729 (d245)`
- 구현 정책: **V_TARGET-first target-native reconstruction**
- production 맵 구현과 persistent province/state ID 마이그레이션: **사용자 명시 승인 / 적용**
- 정적 맵 무결성: **PASS — mod-introduced ERROR 0**
- `D-POST`: **PASS — HoK 단독, 새 게임·맵 진입·unpause 후 최소 1937.01.01까지 진행**
- `C-POST`: **NOT RUN**
- 시작 크래시 제거: **CONFIRMED — 동일 HoK 단독 구성에서 재현되지 않음**
- 직접 크래시 원인: **CONFIRMED — target 1.19.2와 불일치한 `buildings.txt` 파싱/항구 위치 데이터**
- 기존 세이브·persistent map ID를 참조하는 서브모드: **비호환으로 선언**

정적 검증 뒤 실제 엔진의 `D-POST`에서 `13448` province 로드, 싱글플레이 시작, map render 복원, 30일 이상 진행을 통과했다. 수정 전과 같은 access violation crash와 새 crash directory가 생기지 않았고 맵 관련 대상 오류도 0건이었다. 다만 필수 의존성을 포함한 실제 지원 구성 `C-POST`는 아직 실행하지 않았다.

## 승인 범위와 기준선

- Git branch: `main`
- 구현 시작 HEAD: `07bba722b6541c9b2316bee29a450ee4e08b888a`
- 구현 시작 시 `origin/main`: 같은 commit
- target root: `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`
- production mod root: `C:\hoi\hearts_of_korea`
- 정확한 `V_OLD`: 미확보
- 선택된 예외 정책: 정확한 1.16 `INTENDED_DELTA` 복원 주장이 아닌 target-native reconstruction
- base game, Workshop 관리 복사본, 기존 launcher playset: 수정하지 않음
- localisation 언어 header/namespace migration: 이번 작업에서 수행하지 않음
- Git commit·push: 수행하지 않음

현재 `dlc_load.json`은 `mod/hearts of korea.mod` 하나를 활성화하고, 해당 launcher descriptor는 `C:/hoi/hearts_of_korea`를 가리킨다. 따라서 아래 런타임은 production 저장소를 직접 로드한 `D-POST`다. `Korean Language`는 이 실행에 활성화하지 않았다.

## 적용한 ID 정책

### Province

target province `0–13413`을 보존하고 HoK 전용 34개 entity를 RGB·geometry별로 검증해 `13414–13447`에 배정했다. old `13376–13409`와 new `13414–13447`이 순서상 1:1 대응하지만, 구현은 전역 `+38` 치환이 아니라 참조 문맥과 entity registry를 개별 확인해 적용했다.

### State

| 의미 | old HoK ID | 적용 ID |
|---|---:|---:|
| 경기 | `1017` | `525` |
| 평안 | `1021` | `527` |
| 함경 | `527` | `1028` |
| 강원 | `1018` | `1029` |
| 경상 | `1020` | `1030` |
| 충청 | `1019` | `1031` |
| 전라 | `525` | `1082` |
| 황해 | `1022` | `1083` |
| 제주 | `1023` | `1084` |
| 젠다오 | `1024` | `1085` |
| 안둥 | `1025` | `1086` |
| 헤이허 | `1026` | `1087` |
| 쓰시마 | `1027` | `1088` |

## 구현 내용

### Province와 상속 맵 자산

- target `provinces.bmp`에서 시작해 검증된 한국 영역 안의 1,889 pixel만 변경했다.
- target 한국 영역 밖에서 변경된 pixel은 0이다.
- `definition.csv`는 target `0–13413`과 새 `13414–13447`을 포함한다.
- 구형 `heightmap.bmp`, `terrain.bmp`, `ambient_object.txt`, `adjacencies.csv` override를 제거해 target 1.19.2 파일을 상속한다.
- 새 province 34개는 모두 실제 RGB pixel을 가지며 단일 연결 성분이다.
- coast 판정이 달라진 기존 province 5개는 실제 target sea edge에 맞췄다.

### State와 역사

- 충돌하는 HoK state `1017–1027` 파일을 제거했다.
- target 상대 경로와 정확히 같은 `525`, `527`, `1028–1031` 파일에 HoK 의미 분할을 이식했다.
- 새 state `1082–1088`을 추가했다.
- stale target override `408`, `529`, `533`, `535`, `609–612`를 제거해 1.19.2를 상속한다.
- state `528`은 target 1.19.2에서 쓰시마 province `10011`만 분리했다.
- state `717`은 HoK history와 밸런스를 보존하고 target residual province 22개로 membership만 조정했다.
- state `328`, `714`, `716`은 최종 content hash가 구현 전 Git blob과 같다.
- target state `714`에서 `1087`로 이동한 province `7848`, `1693`의 현행 victory point도 함께 이동해 target 데이터를 보존했다.

### Strategic region, 철도와 보급

- 새 province `13414–13447`은 region `186`에 각각 한 번 배정했다.
- 안둥 province `3970`, `6860`, `6910`, `6981`은 region `155`에서 `243`으로 옮겼다.
- 제주 `1177`은 region `186`, 쓰시마 `10011`은 target region `300`을 유지한다.
- rail은 target 1.19.2를 기준으로 로컬 단절 6개 edge를 새 topology 경로로 교체했다.
- 새 중복 edge, unknown/non-land province, 합법 adjacency를 고려한 비인접 신규 edge는 0이다.
- supply는 target 727행을 보존하고 HoK node 7개를 추가했다. 기존 target node `9897`을 포함한 요구 node 8개가 각각 정확히 한 번 존재한다.

### 위치와 content 참조

- `buildings.txt`는 target 66,664행을 기준으로 영향 state 1,122행을 검사하고 state 첫 필드 294행을 최종 geometry에 맞췄다. 첫 runtime crash 뒤에는 1.19.2 parser가 요구하는 파일 끝 개행 없음, 누락된 해안 province 12개의 `naval_base_spawn`, 누락 state의 air-base 7개와 `rocket_site_spawn` 8개를 함께 복구했다. 최종 좌표/state 불일치와 대상 `MAP_ERROR`는 0이다.
- `unitstacks.txt`는 target 전체에 새 province용 536행을 추가했다. 빈 ID, unknown ID와 중복 `(province, zoom)`은 0이다. target 행 뒤에 custom 행을 단순 append해 생긴 전역 `(slot, province)` 순서 역전 1개는 같은 265,891행 multiset을 유지한 stable sort로 수정했다. 이 수정만으로는 crash가 사라지지 않았으므로 단독 원인으로는 반증됐다.
- target `common/on_actions/14_sea_on_actions.txt`를 exact-path 기준본으로 고정하고, 현 geometry에서 state `1086`으로 이동한 Great Wall province `9848`, `6910`만 해당 state block으로 옮겼다. additive on_action으로는 잘못된 vanilla 실행을 막을 수 없어 이 파일은 1.19.2 version-coupled override다.
- KOR capital, OOB, focus, event, decision, AI, on_action, achievement와 localisation의 map ID 참조를 문맥별로 이전했다.
- 일본 focus의 province `1025`, `jungppong_on_actions`의 province/path `1018·1027`, 안정 localisation key `STATE_KR_1024–1027`은 state ID가 아니므로 보존했다.
- localisation 파일은 UTF-8 BOM과 기존 `l_english:` 계약을 유지한다.

## 정적 검증

### 자동 검사

- 도구 단위 테스트: `21/21 PASS`
- effective state files/IDs: `1088/1088`
- duplicate state ID: 0
- duplicate province state membership: 0
- unknown province in state: 0
- land state 누락: target baseline의 sentinel `0` 외 0
- state history의 소속 밖 building/VP province 참조: 0
- changed Paradox Script brace/quote 오류: 0
- localisation duplicate key: 0
- definition ID: `0–13447` 연속
- definition ID/RGB 중복: 0
- bitmap RGB가 없는 실제 province: 0
- strategic region 누락·중복: 0
- rail 신규 비인접·중복 edge: 0
- supply duplicate/unknown/non-land node: 0
- buildings 좌표/state 불일치: 0
- buildings 파일 끝 개행: 없음
- effective state의 air-base/rocket-site spawn 누락: 0
- unitstacks 형식·unknown ID·중복·전역 순서 역전: 0
- high-confidence stale migration ID 참조: 0

### Fresh scan 증거

- output: `<PROJECT>/.local-artifacts/analysis/china-map-2026-09-01/post-building-sites-great-wall-scan-v4/`
- tool version: `11`
- `summary.json` SHA-256: `CF9065891C784716C654E14A341B58DA0D9B056C3958FBB3E6B5A2BF724866B9`
- `findings.tsv` SHA-256: `794D4A1C637DC61E972DA6298B3C06B33EDE54CE461CCEBAB272EC3C89650E03`
- scanner 총 ERROR: 118
- vanilla-only control과 같은 lake-in-state ERROR: 118
- mod가 추가한 ERROR: 0

scanner는 geometry 연결성, 정확한 좌표와 rail adjacency를 완전히 증명하지 않으므로 별도 독립 검사로 보완했다. 독립 검사에서도 남은 fatal/major map integrity finding은 없었다.

### 주요 산출물 SHA-256

| 파일 | SHA-256 |
|---|---|
| `map/provinces.bmp` | `A00EC0E8C18E9F405FC7E7EA59A77848870F03C79E9E5F78CF6E12272D867600` |
| `map/definition.csv` | `0DD53CE40928593FA59C4661863EA4257BDC1E3EC8FDA6D3F790C319A2F8F228` |
| `map/railways.txt` | `5550CEEC8C00A578E6B5B20BD2D3FBF8530723CA43B33E4A9D97AF6049FE309D` |
| `map/supply_nodes.txt` | `4546B826655F0E89F731A13288E394170EF4C2BB1FE387A63A98C4187BF258AB` |
| `map/buildings.txt` | `71F352E34FDF89B8417F77FE734C3B54865E2E3B6BE6B07E053530A03078ED0D` |
| `map/unitstacks.txt` | `2A794AAC4EFD8752E70FF1E72235A16904A2860B6C41D801EED8DF39AF2413D9` |
| `common/on_actions/14_sea_on_actions.txt` | `D59A7A1D7F8C4AA743EE50DE84A4CBB622BEE4AEC90E12D907BFCAFCB7BC4180` |

## 남은 위험과 별도 사건

1. `D-POST` engine discovery, parser, map render와 30일 이상 진행은 통과했다. 다만 state·보급·철도·항구·건물·유닛 위치의 전체 육안 검수는 아직 기록하지 않았다. 1936.07.01과 1937.01.01 autosave에서 OneDrive user-data 경로의 rename `errno 2`가 발생해 save/reload 검증도 별도 환경 사건으로 남는다.
2. 정확한 `V_OLD`가 없어 이 결과를 원작자의 1.16 `INTENDED_DELTA` 정밀 복원이라고 부를 수 없다.
3. 기존 세이브와 persistent map ID를 직접 참조하는 서브모드는 의도적으로 호환되지 않는다.
4. 기존 target unitstack 중 10개 좌표는 자기 province 밖이지만 old HoK에도 동일했던 inherited placement이며 이번 migration 신규 결함은 아니다.
5. 상속되는 Vanilla 한국 판정 로직 일부는 새 `1082`, `1083`, `1084`를 아직 열거하지 않는다. scripted trigger, 저항 modifier, KOR decision과 WTT Japan 소유권 이전의 후속 gameplay compatibility 사건으로 분리한다. startup crash 수정과 같은 patch에서 검증 없이 전체 Vanilla script를 덮지 않는다.
6. `Korean Language` descriptor는 `1.17.*`를 선언하며 1.19.2 runtime UI/font/localisation 호환성은 `C-POST` 전까지 미확인이다.
7. state `1029`에는 서로 다른 유효 `rocket_site_spawn`이 2개 있다. 이번 15행 복구가 만든 중복은 아니며 runtime 오류도 없지만 시각 검수 대상이다.
8. 쓰시마 state `1088`의 rocket site는 원본 좌표가 현행 해상 province가 되어 가장 가까운 `10011` land pixel로 옮긴 합성 좌표다. 엔진 검증은 통과했지만 화면 위치를 확인해야 한다.
9. `common/on_actions/14_sea_on_actions.txt` exact-path override는 target 1.19.2에 결합되어 있으므로 이후 게임 버전마다 원본과 다시 비교해야 한다.

## D-POST 런타임 증거

`-debug`로 production HoK만 로드했다. 첫 crash 후 `unitstacks.txt` 순서만 고친 실행은 같은 `C0000005` / RVA `0xCDE510`으로 다시 crash해 그 가설을 단독 원인에서 제외했다. 이어서 `error.log`가 직접 지목한 `buildings.txt` 끝 빈 행과 해안 province의 port site를 고쳤고, 동일 조건에서 map 진입과 날짜 진행이 가능해졌다.

최종 site/Great Wall 보정 전 실행도 `1936.01.16.02`까지 진행됐고 새 crash directory가 없었다. 이 실행은 남은 map site 오류를 고정한 기준선이다.

- evidence: `<PROJECT>/.local-artifacts/incidents/2026-09-01-china-map-observation/D-POST-15DAY-PASS-MAP-SITE-ERRORS-182433/`
- bundle manifest SHA-256: `836B343C41F7FE808001644EAE8661C861C8082AFEE2A52F544D0635D0B68B53`

최종 보정 뒤 실행은 runtime checksum `83b2`로 `13448` province를 로드하고 `End RestoreDeviceObjects`를 통과했으며, `1936.02.13.13`까지 진행됐다. 이전 23개 `MAP_ERROR`, state `527` 항공 OOB 오류, Great Wall province scope 오류와 port/buildings 오류는 모두 0건이다. 캡처 시 프로세스가 정상 응답 중이어서 종료 성공까지 주장하지 않지만, 당시 최신 crash directory는 이 실행보다 앞선 `hoi4_20260901_180313`이었다.

- evidence: `<PROJECT>/.local-artifacts/incidents/2026-09-01-china-map-observation/D-POST-MAP-SITES-GREAT-WALL-PASS-183523-CORRECTED/`
- bundle manifest SHA-256: `A2AFEC51F122996451780480E52893273E14F40D35AC6F1084DC2ECCF43B51BA`
- `TARGETED_MAP_ERROR_MATCHES=0`

같은 이름의 최초 `...-LIVE` bundle은 이전 실행 checksum `c389`를 metadata에 잘못 기록했으므로 판정 자료로 사용하지 않는다. 원본 로그는 손대지 않고 corrected bundle이 이를 명시적으로 supersede한다.

게임은 이후에도 같은 프로세스에서 최소 `1937.01.01.02`까지 진행됐고 대상 맵 오류와 새 crash directory는 계속 0건이었다. 장기 실행 snapshot은 다음에 보존했다.

- evidence: `<PROJECT>/.local-artifacts/incidents/2026-09-01-china-map-observation/D-POST-LONG-RUN-PASS-1936-11-11-LIVE/`
- bundle manifest SHA-256: `6A42CA88219488D3E95750D670D3F81E16B2DFAB40FD46A77532F4A7A6FF9825`
- 별도 환경 오류: `continue_game.temp`와 `autosave_temp.hoi4` rename `errno 2`

## 다음 런타임 순서

1. 현재 D-POST 창에서 state·보급·철도·항구·건물·유닛 위치를 육안 검사한다.
2. OneDrive user-data의 autosave rename 오류를 별도 사건으로 확인한 뒤 save/reload를 검증한다.
3. production HoK + 정확한 `Korean Language`의 `C-POST`를 실행한다.
4. `C-POST`에서도 새 게임, 한국 선택, map 진입, 1일·7일·30일, save/reload와 새 crash/로그를 확인한다.
5. startup/map 사건을 닫은 뒤 Vanilla 한국 판정 누락과 남은 MIO·AI·기술·event·character/localisation 오류를 각각 별도 사건으로 처리한다.

## Git 상태

production 구현 파일과 이 기록은 working tree에 있으며 commit·push하지 않았다. 이전에 사용자가 요청한 문서 전용 commit `07bba722b6541c9b2316bee29a450ee4e08b888a`만 `origin/main`에 존재한다. pre-existing untracked `tests/`, `tools/`는 보존했고 이 구현에 포함해 commit하지 않았다.
