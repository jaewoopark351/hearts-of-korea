# 2026-08-31 시작 크래시 맵 fresh scan 감사

## 실행 식별

- 사건: `2026-08-31-startup-crash`
- 실제 재산출일: `2026-09-01` (Asia/Seoul)
- 작업 모드: **Diagnostic**
- 저장소: branch `main`, 시작 HEAD `91e1a7b62d046ba209fc6e35c0e405c65e07355a`
- 목표 게임: HOI4 `1.19.2.0.a729 (d245)`, Steam build `23969257`
- 스캔 구성: `V_TARGET -> Korean Language -> 현재 HoK`의 exact-relative-path 정적 overlay
- 런타임 호환성: **UNPROVEN**
- 정적 결과: **FAIL**
- 3-way 상태: **BLOCKED** — `V_OLD 1.16.8` 실제 파일 미확보
- production 맵 수정·ID 변경·게임 실행: **수행하지 않음**

실행 명령:

```powershell
python -B -m tools.map_fresh_scan `
  --vanilla-root "C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV" `
  --mod-root "C:\hoi\hearts_of_korea" `
  --dependency-root "C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\2743487021" `
  --output "C:\hoi\hearts_of_korea\.local-artifacts\audits\2026-09-01-map-fresh-scan-v15"
```

전체 산출물은 아래 ignored 로컬 진단 폴더에 보존했다.

`<PROJECT>/.local-artifacts/audits/2026-09-01-map-fresh-scan-v15/`

| 파일 | SHA-256 |
|---|---|
| `summary.json` | `CE1CC0A0C23E5B57249FFF61D5674C1352F279A9B1B8B29A34BFD192A942116B` |
| `inputs.tsv` | `D4D1949DD91AD8346A107DF0EC9BE1D3C6AD0746CD145913E4D55FCEE985FB35` |
| `findings.tsv` | `F29B76C2244EFF3869F2CFEBAD4686456E001461015B376E51B6461B8248D5ED` |
| `references.tsv` | `27AF425790F9DE8EE8FA1AC4A0D36A2D53DBD5A4CACCB7BC32DAEB441DA97FDE` |
| `three_way_files.tsv` | `0C75E927E80B1E3505B2F392E325F993F9FB5E99687C966BA890FE89C8C13E28` |

산출물 5개에는 NTFS read-only 속성을 설정했다. 이는 실수 방지 장치이며 WORM 저장소를 뜻하지 않는다. 각 파일의 SHA-256이 재식별 기준이다.

같은 입력과 옵션으로 새 `2026-09-01-map-fresh-scan-v16` 디렉터리에 다시 실행한 결과 위 5개 파일의 SHA-256이 모두 v15와 일치했다. 따라서 이 입력 집합에서 tool version `8` 산출물의 결정성은 PASS다. v1–v14는 reference 의미·target bitmap 수집·3-way identity gate를 단계적으로 보강하기 전 산출물이므로 폐기하지 않고 보존하되, 현재 판정 자료는 v15/v16이 대체한다.

## 입력과 overlay 경계

| 입력 | 물리 경로 | 상태 |
|---|---|---|
| `V_TARGET` | `<HOI4_INSTALL>` | CONFIRMED, `1.19.2.0.a729 (d245)` |
| `Korean Language` | `<STEAM_WORKSHOP>/2743487021` | CONFIRMED, version `25.11.23`, declared `1.17.*` |
| HoK 작업 복사본 | `<PROJECT>` | CONFIRMED |
| `V_OLD` | 미확보 | BLOCKED |

scanner는 파일 시스템의 정확한 상대 경로가 같은 경우에만 상위 layer가 하위 layer를 대체한다고 모델링했다. 모드 루트의 개발 전용 최상위 폴더(`.git`, `.local-artifacts`, `docs`, `tests`, `tools` 등 기록된 allowlist)는 입력에서 제외했다. `replace_path`, launcher discovery, 디렉터리별 엔진 merge 규칙, Windows의 대소문자 동작은 모델링하지 않았다. 따라서 이 감사의 “effective”는 재현 가능한 정적 모델이며 실제 엔진 VFS의 완전한 증명은 아니다.

이 overlay는 선언된 의존 모드를 포함한 **지원 구성 후보의 정적 inventory**이며, 역사적 `D-PRE`의 실제 VFS를 재구성한 것이 아니다. `D-PRE`는 `Korean Language`가 비활성인 HoK 단독 구성으로 기록돼 있다. 설치된 `Korean Language`에는 `map/`과 `history/` 파일이 각각 0개이므로 이 dependency가 아래 map definition·membership을 직접 만든다는 가설은 정적 파일 범위에서 `DISPROVEN`이다. UI·font·localisation과 그 밖의 런타임 기여는 이 감사의 판정 범위가 아니다.

핵심 map 입력 해시:

| layer | 파일 | bytes | SHA-256 |
|---|---|---:|---|
| mod | `map/definition.csv` | 478,498 | `9976cdcd2e46adc06ac3df22698587b7bc64b1bd53230e996b31d11680ba34e2` |
| mod | `map/provinces.bmp` | 34,603,062 | `21f92dc01c41f31cb2381f3a7c745e51d109edcc6f4b9f81d1d1e286e7f1fe42` |
| vanilla (target reference; mod에 shadowed) | `map/provinces.bmp` | 34,603,062 | `e131d30e5dcb13d9c2a8598f820a2de0ae9828f3a24f2bddc1bcfff40f71660a` |
| mod | `map/heightmap.bmp` | 11,535,414 | `cec86c8e65d77ec4db792bc8257f3731d1380796d2a8b7ed689983aa2cfa4068` |
| mod | `map/terrain.bmp` | 11,535,410 | `2a4ffa7b4cae4cc2c5daeb1fb9251a14fbbb13df508916cddb4cbf31014cda5c` |
| mod | `map/adjacencies.csv` | 11,292 | `c3843214fa8efd8d1988132e810f9a2c6a4174fa253973b0a27a1a49a0a92cc4` |
| mod | `map/railways.txt` | 28,900 | `8a6926ef933637f0db3bcc0f2250fd4e2ebbc1e8dedc656c8e08dc1ad64262ae` |
| mod | `map/supply_nodes.txt` | 6,644 | `ef3bbd6226f1d0cc10207e87cef105141b980e01c08482cbc547bcebaacc88bc` |
| mod | `map/buildings.txt` | 3,028,618 | `f785d56aa013b355cd412c8fbd3f26fc0f5ada5af791bc2020c53e7e79e99079` |
| mod | `map/unitstacks.txt` | 10,443,808 | `8e9cecb9477eac0744f638638e9ecb6065c99b859610f99dada76c082afeb8f1` |
| vanilla | `map/rivers.bmp` | 11,535,416 | `4491190a65771592ebffdb3479eae519b3b5623bfaca41500b1e2e4a38caba71` |
| vanilla | `map/cities.bmp` | 11,535,412 | `b1d03542e837b3f1e591b158f3fc344d8c9fac9e90199e2402909f07bab59153` |
| vanilla | `map/trees.bmp` | 992,362 | `3c575ad3c55cf786aa16ca7f0bc5216fc33001f260700ce031a64838bfaecf2f` |
| vanilla | `map/world_normal.bmp` | 8,650,808 | `0a050aa615dcf087ddf127b0d3ffdb2cbc24921a1c503405edb1a2aa141b5b87` |

`heightmap.bmp`와 `terrain.bmp`는 `5632 x 2048`, 8-bit, uncompressed로 읽혔다. 상속되는 `rivers.bmp`와 `cities.bmp`도 `5632 x 2048`이다. `trees.bmp`와 `world_normal.bmp`는 엔진 용도가 다른 크기를 사용한다. 이 값과 해시는 CONFIRMED지만 팔레트 의미, 픽셀 정렬과 지형 동작은 아직 UNPROVEN이다.

### 외부 전달자료의 map artifact 대조

2026-09-01에 전달된 GitHub source ZIP에서 확인한 두 map entry는 현재 HEAD의 대응 Git blob과 일치한다. 이 source package는 원본 Workshop archive가 아니므로 두 산출물을 혼동하지 않는다.

| artifact | bytes | SHA-256 | 판정 |
|---|---:|---|---|
| GitHub ZIP 내부 LF `map/definition.csv` | 465,088 | `67A710821CA8A883818B0F691C2D9EDAD9AF195274F5C6DBC5D164FB2E160F60` | current Git blob과 동일 |
| 현재 checkout CRLF `map/definition.csv` | 478,498 | `9976CDCD2E46ADC06AC3DF22698587B7BC64B1BD53230E996B31D11680BA34E2` | LF 13,410개가 CRLF로 checkout된 동일 텍스트 |
| GitHub ZIP 및 checkout `map/provinces.bmp` | 34,603,062 | `21F92DC01C41F31CB2381F3A7C745E51D109EDCC6F4B9F81D1D1E286E7F1FE42` | byte-identical |
| 불변 `HOK_ORIGINAL` Workshop archive ZIP | 70,486,687 | `4683E8E2D8BBAAD8AEFA5C1E335DFB6346FEE269300E0FDDE34AEA7F012118F9` | 1,049개 원본 파일 총 224,994,293 bytes를 담은 별도 canonical archive |

`definition.csv`의 두 해시는 의미 변화가 아니라 줄바꿈 표현 차이다. GitHub ZIP 파일의 각 LF 앞에 CR을 넣으면 현재 checkout과 바이트 단위로 일치한다. 따라서 `67A710…`을 현재 물리 checkout 파일의 raw hash로 기록하거나 `C1790…` GitHub ZIP을 `HOK_ORIGINAL` archive로 사용하지 않는다.

## 핵심 findings

총 8,547개 실제 입력 파일을 해시했고, 734개 finding과 39,631개 후보 reference row를 보존했다. finding은 `ERROR 348`, `WARNING 364`, `INFO 22`다.

### CONFIRMED

1. effective `map/definition.csv`는 HoK 파일이며 13,410개 nonempty record가 ID `0–13409`에 연속으로 존재한다. 중복 ID와 중복 RGB는 없다.
2. effective HoK `provinces.bmp`와 target vanilla `provinces.bmp`는 모두 `5632 x 2048`, 24-bit, uncompressed다. HoK bitmap은 13,409개, target bitmap은 13,413개의 distinct RGB를 포함하며, RGB set 비교는 target-only 38개와 HoK-only 34개를 확인했다. 두 definition의 record 수보다 bitmap RGB 수가 하나 적은 것은 각각 ID `0`의 `(0,0,0)` sentinel 한 행 때문이다. bitmap-only 미정의 RGB와 ID 0 이외의 definition-only RGB는 없다. 이 결과는 RGB 집합과 기본 일대일 대응만 확인하며 각 색의 지리적 동일성·geometry는 UNPROVEN이다.
3. 현재 바닐라 state와 strategic region은 province `13410`, `13411`, `13412`, `13413`을 각각 참조하지만 effective definition에는 이 ID가 없다.

| province | state 참조 | strategic region 참조 |
|---:|---|---|
| `13410` | `history/states/1062 - Kelantan.txt:42` | `map/strategicregions/188-Malaya.txt:6` |
| `13411` | `history/states/741-Cambodia.txt:33` | `map/strategicregions/228-South Indochina.txt:6` |
| `13412` | `history/states/726-Samoa.txt:31` | `map/strategicregions/178-West Polynesia.txt:6` |
| `13413` | `history/states/2-Italy.txt:47` | `map/strategicregions/23-Italy.txt:6` |

4. state ID `1017–1027`은 exact-path overlay 뒤에도 현재 바닐라의 서로 다른 11개 state와 HoK state가 동시에 정의되어 `DUPLICATE_STATE_ID` 11건이다.
5. 파싱된 effective membership에서 land province 103개가 둘 이상의 state에, province 104개가 둘 이상의 strategic region에 들어 있다. strategic region이 없는 province도 5개(`4010`, `4114`, `7129`, `7200`, `9956`)다.
6. 현재 effective definition에서 non-land로 분류되지만 state가 포함하는 membership이 117건이다.
7. HoK와 목표 바닐라의 같은 province ID 중 정적 definition 필드가 다른 ID가 321개다. 여기에는 `13376–13409` 34개가 모두 포함된다. “필드가 다름”은 CONFIRMED지만 각 차이가 원작 의도인지 구형 바닐라 잔재인지는 `V_OLD` 없이는 UNPROVEN이다.
8. bounded scanner가 각 파일에서 명시적으로 검사하는 province/state ID 위치에는 railway, supply node, adjacency, buildings, unitstacks 관련 unknown-ID finding이 없었다. 이는 그 파일들의 전체 필드·스키마가 정상이라는 뜻이 아니며, 철도 연속성, 좌표의 실제 province, 항구의 coastal 여부 또는 렌더링도 증명하지 않는다.
9. 이 정적 overlay에서는 HoK의 전역 `definition.csv`, `provinces.bmp`, `heightmap.bmp`, `terrain.bmp`, `buildings.txt`, `unitstacks.txt`, `railways.txt`, `supply_nodes.txt`, `adjacencies.csv`가 사용되는 동시에, 모드에 대응 파일이 없어 target layer에서 남는 `rivers.bmp`, `trees.bmp`, `cities.bmp`, `world_normal.bmp`와 state `1062`, `741`, `726`, `2`가 함께 존재한다. 즉 구형 HoK 전역 맵과 target-layer 데이터의 **partial composition 현상**은 이 exact-path 정적 모델에서 `CONFIRMED`다. 각 target-layer 파일이 1.16 이후 새로 생긴 것인지는 이 결과만으로 단정하지 않는다. 실제 `D-PRE` 물리 복사본과 완전한 엔진 VFS의 동일성도 계속 `UNPROVEN`이다.

위 3–6번과 9번은 기존 `D-PRE` 로그의 malformed province와 state 충돌 판단을 더 강하게 뒷받침한다. 다만 시작 크래시의 엔진 내부 원인과 수정 후 소멸은 런타임 재현 전이므로 크래시 인과 등급은 계속 **STRONGLY_SUPPORTED**다.

### reference inventory 정의

`references.tsv`는 고유 ID 수가 아니라 **entity type별 물리 토큰 occurrence row**다. row identity는 `(entity_type, entity_id, source_layer, relative_path, line, column)`이며, 같은 토큰을 structured/source/lexical detector가 함께 찾으면 `context`를 세미콜론으로 합치고 가장 높은 confidence 하나를 기록한다. 파일 경로 자체의 숫자 후보는 `line=0`, LOW로 기록한다. 따라서 detector-pass 중복 row는 없지만 같은 숫자가 state와 province 후보에 모두 해당하면 entity type별로 두 row가 될 수 있다. state/province definition, membership, railway, supply, buildings, unitstacks와 일반 텍스트의 lexical 후보를 구분하고, 일반 숫자는 `HIGH / MEDIUM / LOW` confidence를 붙였다.

| 대상 집합 | 전체 rows | layer+파일 수 | mod rows | mod 파일 수 | HIGH | MEDIUM | LOW |
|---|---:|---:|---:|---:|---:|---:|---:|
| province `13376–13409` | 941 | 64 | 712 | 18 | 847 | 16 | 78 |
| state `1017–1027` | 4,656 | 192 | 3,310 | 38 | 845 | 99 | 3,712 |

LOW row에는 날짜, 좌표, 수량, 주석 또는 다른 종류의 ID가 섞일 수 있다. 따라서 이 수치를 곧바로 마이그레이션 치환 수로 사용하지 않는다. 개별 매핑표를 만들 때 `HIGH`, `MEDIUM`, `LOW`를 검토하고 state와 province 문맥을 분리한다. 기존의 `307`, `712` 추정치와도 정의가 다르므로 단순 증감 비교하지 않는다.

## 3-way 및 마이그레이션 판정

`V_OLD 1.16.8` 실제 depot 파일이 없어 `three_way_files.tsv`는 header만 있고 `three_way_status=BLOCKED`다. 현재 확보된 것은 build/depot manifest 후보 메타데이터뿐이다. scanner는 향후 3-way에서 `V_OLD`와 별도 `HOK_ORIGINAL` root 각각에 대해 독립 per-file manifest, 예상 manifest SHA-256과 식별 label을 모두 요구하고 실제 root를 manifest와 대조한다. tool version `8`은 `HOK_ORIGINAL`과 현재 `--mod-root`의 resolved 경로가 같거나 서로 포함되는 경우도 거부하므로, 현재 mutable 작업 트리를 원본으로 가장할 수 없다. 다만 label의 역사적 버전·build 진위는 별도 Steam/depot 증거로 확정해야 한다.

- build ID: `18550822`
- content depot `394361`: manifest `2512503158411563220`
- Windows depot `394362`: manifest `4372532302181969559`

따라서 다음은 여전히 수행하지 않는다.

- `INTENDED_DELTA` 자동 추론 또는 적용
- province `13414–13447` 또는 state 신규 구간 후보의 예약 확정. 후속 설계의 `1082–1088` 의미 매핑안도 이 scanner가 승인한 결과가 아님
- `+38`, `+65` 또는 다른 전역 숫자 치환
- production `map/`, `history/states/` 수정
- save/submod 호환성 정책 결정 없는 persistent ID 변경

## scanner 한계와 다음 게이트

- 이 도구는 HOI4 parser가 아닌 bounded lexer다.
- 연결 성분, 해안 topology, railway 연속성, 건물·유닛 좌표의 실제 위치를 판정하지 않는다.
- `replace_path`, 디렉터리별 merge와 실제 launcher VFS를 완전히 모델링하지 않는다.
- static `FAIL`은 데이터 관계 오류를 뜻하지만 그 자체로 WER의 정확한 엔진 함수나 assert를 특정하지 않는다.
- `Korean Language`의 UI/font/localisation 런타임 호환성을 증명하지 않는다.

다음 production 게이트는 정확한 `V_OLD` 확보와 SHA-256 manifest 또는 원형 복원과 구분된 target-native reconstruction 선택, 개별 entity ID 매핑표 및 save/submod 정책 승인이다. 구체적인 후속안은 [맵 재구성 설계](../HOK_MAP_RECONSTRUCTION_PLAN.md)에 기록한다. 이후에도 수정 전과 같은 `D-POST`, 실제 지원 구성 `C-POST`, 새 게임·unpause·save/load 검증이 필요하다.
