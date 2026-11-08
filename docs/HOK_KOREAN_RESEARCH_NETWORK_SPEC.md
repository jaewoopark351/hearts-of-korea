# 한국 연구시설·과학자 성장 연계 명세

**2026-11-08 현행 소스 구분:** 남북도 분할 뒤 해군 우선 주는 경상남도 `1086`, 핵 우선 주는 함경남도 `1028`이다. 아래 적용 표는 현재 소스에 맞추며, 2026-10-31의 해군 `1030` 지급·해시·실행 수치는 당시 분할 전 이력으로 보존한다. 실제 우선 주와 옛 툴팁 ID의 불일치를 수리할 때는 [현행 지도 기준 코드 정렬 계획](HOK_STATE_REFERENCE_ALIGNMENT_PLAN.md)의 D-01을 먼저 읽는다. 해당 현지화 수리와 현행 우선 주의 신규 실행 검증은 아직 수행하지 않았다.

작성: 2026-10-31 (Asia/Seoul). 설치본 HOI4 `Operation Postern 1.19.3.0.c01a`, Steam build `25205862` 기준. 2026-10-30 감사의 C2를 사용자가 후속 개발 범위로 승인한 뒤 구현한다. 호환성 복구 A1/A2와 구분하는 의도적인 보상 추가다.

별도 후속 [민간 핵 연구 중점2개](HOK_KOREAN_CIVIL_NUCLEAR_RESEARCH_SPEC.md)를 구현하여 전체 소스는474개가 됐다. 후속 사용자 요청으로 첫 중점의5일 감산을 제거하고 핵 기술 선행 연구 불이익2년 감소1회를 추가했다. 현재는 서울대 아래 기본35일 핵 혁신1.00+이1회 연구 혜택 → 기본245일 민간 원자로 건설 기술 지급이다. 첫 보상에 자동 기술 획득·별도 연구 속도 보너스는 없으며 기존 시설·과학자 보상을 옮기지 않는다. 기존 저장 감산은 자동 회수하지 않고 기완료 첫 중점의 새 보상도 소급하지 않는다. 후속 변경은 정적 대조만 수행했으며 새 혜택·245일 정상 진행의 런타임은 미검증이다.

감산 제거 전1.19.4.1.99a5/build26282552·DLC36의 `ff98`에서 핵 원시값0→10000·감산5, 둘째 정상240회 일일 진행의 기술 지급·강원 건설 대기열1개를 확인했다. 실제 경과5742시간과 정확5760시간을 구분한다. 진단 없는 두 모드 `1b1c`의 당시 저장 재로드24/0·기보유 미선택/활성 합성 입력 통과 각19/0은 별도 확인이며 연속 실행의 같은 틱 작동을 뜻하지 않는다. 별도 GDR 제외 새 한국 초기 HIDE와 빨간 조건을 관측했고, DLC만의 시작 차단은 준비 저장 로드 제한으로 미검증이다. 원래 프로필·저장 해시 보존을 확인했으며 이전 후보 실패·완료ID 손실 원인 미확인·시험 저장 파싱 오류와 장기 검증 한계도 남긴다.

2026-10-31 민간 핵 가지 통합 시점에는 새 가지가 연구망 helper를 호출하지 않고 기존 효과 SHA-256 `185874FC8EEE0A5256E654ECF25EAFD258C487D8E8DA53EAFF5C579B43DCEE87`를 유지했다. 이 해시는 남북도 분할 후 현행 파일의 해시를 뜻하지 않는다. [별도 구현·검증 기록](incidents/2026-10-31-korean-civil-nuclear-research.md)의 감산 제거 전 소스506/0·정상240회14/0·재로드·통과 판정과 아래 기존 연구망 실행 결과를 합산하지 않는다.

## 적용 단위

기존 중점 네 개에 시설·과학자 육성 보상을 연결한다. 중점 추가, 좌표·아이콘·선행·배타·기간·AI 변경은 하지 않는다. 기존 보상은 전부 유지하며 새 연구시설과 과학자 성장은 `Gotterdammerung` 보유 시에만 실행한다.

| 기존 중점 | 보존할 기존 보상 | 추가 시설과 우선 주 | 성장할 기존 과학자 |
|---|---|---|---|
| `KOR_create_add` / 국방과학연구소 설립 | `generic_secret_weapons_ns` | 육군 실험시설 1개, 경기 `525` | `KOR_Yonggwan_Kim`, 육군 전문화 +1 |
| `KOR_invitation_of_foreign_naval_designers` / 해외 함선 설계사 초빙 | 순양함·구축함 연구 혜택과 기존 MIO/설계사 안내 | 해군 실험시설 1개, 경상남도 `1086` | `KOR_Bugil_Hwang`, 해군 전문화 +1 |
| `KOR_korean_jet_engine` / 현대의 신기전 | 항공 돌파점 진행도 +0.5, 로켓·제트 연구의 선행 기간 혜택 | 항공 실험시설 1개, 강원 `1029` | `KOR_Gyeongyeon_Jo`, 항공 전문화 +1 |
| `KOR_mugunghwa_kkochi_pieossseubnida` / 무궁화 꽃이 피었습니다 | 핵 돌파점 진행도 +0.75, 핵 연구 혜택, 기존 뉴스 이벤트 | 핵 실험시설 1개, 함경남도 `1028` | `KOR_Sanglok_Do`, 핵 전문화 +1 |

원래 과학자 수준이 그대로라면 육군·해군·항공은 1→2, 핵은 2→3이 된다. 플레이 중 이미 성장했다면 당시 수준에 +1을 적용하며 특정 수준으로 덮어쓰지 않는다. 과학자 자동 모집, 새 과학자 생성, 자동 시설 배정이나 프로젝트 완료는 하지 않는다. 이 추가 보상은 원래 수치의 대체가 아니며, 보상 지침의 기존 혜택 보존 규칙을 따른다.

## 시설 배치와 중복 방지

국가 범위의 `has_facility_specialization`으로 해당 전문분야 시설의 보유 여부를 먼저 확인한다. 이미 보유하면 같은 전문분야 시설을 더 주지 않는다. 보유하지 않았다면 `random_owned_controlled_state`에서 아래 조건을 모두 만족하는 주를 선택하며 위 우선 주를 `prioritize`에 지정한다.

- 현재 국가의 소유·핵심 주이며 완전히 통제 중이다.
- `can_construct_building`이 해당 시설의 건설을 허용한다.
- 육군·해군·항공·핵 시설이 모두 0이다. 다른 분야 시설을 교체하지 않는다.
- 해군 시설은 추가로 해안 주여야 한다.

우선 주가 조건을 만족하지 못하면 같은 조건의 다른 소유·통제 핵심 주가 후보가 된다. 후보가 없으면 시설을 주지 않는다. 시설이 이미 있거나 배치할 곳이 없어도 해당 과학자의 성장 보상은 별도로 적용한다. 각 중점의 효과 문구에 이 조건을 명시한다.

`construct_building_in_random_province = { <facility> = 1 }`로 해당 주의 유효한 프로빈스에 시설 수준 1을 설정한다. 설치본의 `state_max = 1`, `group_by = special_project_facility` 계약과 현재 지도 배치를 사용한다. 경기·강원·함경남도에는 현재 `map/buildings.txt`의 `special_project_facility_spawn`, 경상남도에는 해군 시설이 쓰는 `naval_base_spawn`이 존재한다. 이번 모듈에서 지도 파일을 바꾸지 않는다. 실제 시설 지도 표시와 배정은 엔진 관측으로 별도 확인한다.

## 과학자와 저장 상태

네 과학자는 기존 `common/characters/KOR.txt`에 정의되어 있고 한국 시작 history에서 모집한다. `has_character`로 현재 국가의 보유를 확인한 뒤 해당 character 범위에서 `add_scientist_level`을 실행한다. 과학자가 없으면 새로 만들거나 타국에서 데려오지 않는다.

중점별 과학자 성장 플래그는 아래와 같다. 실제 과학자 성장 후 설정하여 같은 보상 helper를 재실행해도 경험 수준을 중복 지급하지 않는다.

| 분야 | 일회 지급 플래그 |
|---|---|
| 육군 | `HOK_KOR_land_scientist_training_awarded` |
| 해군 | `HOK_KOR_naval_scientist_training_awarded` |
| 항공 | `HOK_KOR_air_scientist_training_awarded` |
| 핵 | `HOK_KOR_nuclear_scientist_training_awarded` |

이미 중점을 완료한 기존 저장에 소급 지급하는 `on_action`이나 일회 마이그레이션은 없다. 기존 저장 호환성 검증은 새 게임 저장·재로드와 별개이며 이번 문서만으로 주장하지 않는다.

## 호출 계약과 파일

각 중점의 `completion_reward` 국가 범위에서 아래 효과를 한 번 호출한다. helper의 `ROOT`는 그 중점을 완료하는 국가다. 타국 이벤트의 다른 `ROOT` 아래에서 임의로 재사용하지 않는다.

| 중점 | 호출 |
|---|---|
| `KOR_create_add` | `HOK_KOR_establish_land_research_network = yes` |
| `KOR_invitation_of_foreign_naval_designers` | `HOK_KOR_establish_naval_research_network = yes` |
| `KOR_korean_jet_engine` | `HOK_KOR_establish_air_research_network = yes` |
| `KOR_mugunghwa_kkochi_pieossseubnida` | `HOK_KOR_establish_nuclear_research_network = yes` |

- 효과: `common/scripted_effects/HOK_KOR_research_network_effects.txt`. 위 네 효과 안에 각 분야의 시설·전문화·우선 주 ID를 직접 적은 배치 블록을 둔다. 공통 매개변수 배치 helper와 매개변수 호출은 사용하지 않는다. 해군 블록에만 `is_coastal = yes`를 추가한다.
- 문구: `localisation/korean/HOK_KOR_research_network_l_korean.yml`, `localisation/english/HOK_KOR_research_network_l_english.yml`. UTF-8 BOM, 각 locale header, 같은 contributor note를 유지한다. 기존 프로젝트 계약에 맞춰 양쪽에 한국어 문구를 제공한다.
- 표시 키: `HOK_KOR_land_research_network_tt`, `HOK_KOR_naval_research_network_tt`, `HOK_KOR_air_research_network_tt`, `HOK_KOR_nuclear_research_network_tt`.
- 기존 중점 그림을 유지하므로 새 이미지·sprite를 추가하지 않는다.

## 설치본 근거

원본 경로는 사용자가 지정한 `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV`이며 읽기 전용이다.

- `common/national_focus/uk.txt:752–803`: 실험시설·돌파점 보상과 기존 시설 유무 검사.
- `common/national_focus/germany.txt:19061` 이후: character 범위의 `add_scientist_level = { specialization = ... level = 1 }` 보상.
- `common/national_focus/australia_taog.txt:2262–2271`: `random_owned_controlled_state`, 완전 통제·건설 가능 조건, `prioritize`, `construct_building_in_random_province` 조합.
- `common/national_focus/china_nationalist_sea.txt:14272–14307`: 해군 시설의 기존 시설 4종 검사와 해안 핵심 주 대안.
- `common/national_focus/persia.txt:2365`, `belgium.txt:5011`: 국가의 전문분야 시설 중복 방지.
- `documentation/triggers_documentation.md:1920,3853`: `can_construct_building`의 STATE/ROOT 계약, `has_facility_specialization`의 COUNTRY 계약.
- `documentation/effects_documentation.md:2083,2925`: 과학자 수준 증가와 프로빈스 시설 설정 effect 계약.
- `common/buildings/00_buildings.txt:126–148,501–580`: 시설별 전문분야, 해안 제약과 공통 슬롯 상한.

## 검증 상태

최초 매개변수 helper 소스는 교리 이식과 함께 수행한 외부 정적 검사에서 **33 PASS / 0 FAIL**이었다. 이는 ordered entry·정의 개수·참조·인코딩 검사를 통과했다는 기록이며 엔진 등록 통과가 아니다. 이후 활성 DLC 목록 0개인 외부 실행 사본(`Gotterdammerung` 조건은 거짓)의 완전 재시작에서 이 소스의 등록 실패가 실제로 관측됐다. 이 구성은 모든 `has_dlc`가 거짓이라는 뜻이 아니다. 통합된 `Man the Guns`의 `has_dlc`는 참으로 관측됐으며, `dlc_load.json`에서 모든 DLC를 비활성화했다는 주장도 하지 않는다. DLC 조건 내부의 실행 여부와 별개로 등록 중 `$SPECIALIZATION$`, `$FACILITY$`, `$ALLOW_INLAND$`, `$PREFERRED_STATE$`가 전개되지 않은 토큰으로 처리됐고, 호출의 인자 이름도 잘못된 effect로 기록됐다. 해당 로그의 실행별 보존 위치와 나머지 기준선은 통합 작업 기록을 따른다. 이 관측만으로 모든 매개변수 effect나 다른 맥락의 지원 여부를 일반화하지 않는다.

이 실제 오류의 가장 이른 원인에 맞춰 공통 배치 helper를 제거하고 네 기존 효과에 리터럴 배치 블록을 넣었다. 네 호출 ID, 표시 문구, DLC·중복·주 소유/핵심/완전 통제·빈 시설 슬롯 조건, 우선 주와 대체 주, 과학자 +1 및 일회 플래그는 유지했다. 해군의 해안 조건도 유지한다. 수정 전 helper·명세는 저장소 밖 `C:/hoi/test/feature-integration-20261031/validation/c2-parameterized-pre-fix/`에 보존했다. 수정 후 효과 파일 SHA-256은 `185874FC8EEE0A5256E654ECF25EAFD258C487D8E8DA53EAFF5C579B43DCEE87`이다.

수정 후 외부 정적 검사 결과는 **42 PASS / 0 FAIL**이다. 검사 범위는 교리 외 기존 history의 ordered entry 보존, 설치본 독일 1939 교리 전환과의 일치, history BOM/CRLF 보존, 효과 4개의 정의, 미전개 script 매개변수 부재, 각 리터럴 배치의 분야·주 일치, 수정 전 과학자 보상·플래그·문구·DLC 조건 보존, 양쪽 locale BOM/header·4개 키·문구 일치, 참조 과학자·건물·주별 map spawn 존재다. 검사기와 JSON 결과는 저장소 밖 `C:/hoi/test/feature-integration-20261031/check_doctrine_research.py`, `doctrine-research-static-checks.json`에 둔다.

shared `korea.txt`의 네 호출을 통합했고 원래 보상은 보존했다. 최초 정적 통과 이후 실제 등록 실패가 있었으므로, 정적 결과나 조용한 텍스트 검사만으로 수리 완료를 주장하지 않는다.

### 실제 DLC 실행의 지급·중복 검사

실제 설치 실행 파일과 사용자 프로필을 사용하는 진단에서 활성 DLC 36개를 확인했다. `Gotterdammerung`과 `No Compromise, No Surrender`는 실제 활성 목록에 있고, `has_dlc`를 우회하지 않았다. 최초 실제 실행 PID `13828`에서는 진단 전용 `has_scientist_level`의 `level = N` 비교 20곳이 엔진 등록 중 거부됐다. 이때 연구 검사는 `SKIP`이었으며 C2 지급 통과로 계산하지 않는다. 원본 오류·로그·당시 진단 파일은 저장소 밖 `real-dlc/runs/pid13828-c2-fixture-equality-registration/`에 보존했다. 이는 production 효과의 추가 실패가 아니라 진단 조건의 실패다.

진단의 정확한 정수 수준 비교만 같은 character 범위의 `level > N-1`과 `NOT = { ... level > N }`으로 바꾸고 완전히 재시작했다. PID `7736`, 화면 체크섬 `bd1a`, 활성 DLC 36개, 게임 날짜 `1936.01.01.12`에서 **C2 8 PASS / 0 FAIL / 0 SKIP**을 관측했다. 네 기존 중점을 강제 완료하지 않고 `ROOT = KOR`인 숨김 국가 이벤트에서 production 효과를 직접 호출했다. 따라서 C1 중점 조건도 변경하지 않았다.

- 첫 호출 4건: 육군 경기 `525`, 해군 경상 `1030`, 항공 강원 `1029`, 핵 함경 `1028`에 해당 시설이 있고, 소유 주 전체의 해당 분야 시설 수가 각각 정확히 1임을 검사했다. 김용관·황부길·조경연은 해당 전문화 1→2, 도상록은 핵 전문화 2→3이며 각각 일회 지급 플래그가 설정됨을 함께 확인했다.
- 반복 호출 4건: 같은 production 효과를 다시 불러도 분야별 시설 수가 1이고 과학자 수준이 첫 호출 후의 값과 같음을 확인했다. 시설 중복과 과학자 수준 재지급은 이 시나리오에서 발생하지 않았다.
- 당시 `error.log`에는 `HOK_KOR`·`HOK_FIDLC` 관련 행이 없었다. 이는 해당 모듈의 오류 부재 확인이며 기존 모드의 모든 오류가 없어졌다는 뜻은 아니다.

전체 로그·활성 진단 파일·production 효과 사본은 저장소 밖 `C:/hoi/test/feature-integration-20261031/real-dlc/runs/bd1a-corrected-startup/`에 실제 UI 후속 작업 전에 복사했다. `research_factions_capture_manifest.json`에는 보존한 37개 파일의 크기·SHA-256, `research_factions_assessment.json`에는 검사 수와 한계를 기록했다. 보존된 production 효과는 위 `185874...CEE87`, 수정된 이벤트 진단은 `E10F3D0AC54E74E20F1BAF41EECADE54B7C03574776DC237D157374E044C3F26`이다. 같은 실행의 C4 8/0은 네 템플릿의 합성 한국 생성·목표·규칙·해산 검사이며, C2 검사 수에 합산하지 않는다.

위 8건의 직접 효과 검사에는 대체 주 선택, 건설 가능한 공간이 전혀 없는 경우, 과학자 부재, DLC 음성 경로, 시설 지도·UI·배정·프로젝트 완료가 포함되지 않는다. 같은 실행에서 뒤이어 관측한 실제 배정과 별도 새 게임의 edge 진단은 아래에 각각 기록한다. 또한 기존 한국 중점의 정상 소요 기간·클릭 진행과 실제 미·독 생성 호출·초대 경로는 직접 효과 진단으로 대체하지 않는다.

### 실제 UI 과학자 배정 3건

같은 PID `7736` / 체크섬 `bd1a`의 합성 게임에서 소양강 수문 정상화가 정상 14일 경과로 완료된 뒤, `1936.02.04.14`에 일시정지하고 연구 화면의 실험시설 목록을 열었다. 준비 효과로 만든 시설 4곳이 목록에 표시됐으며, 아래 세 시설의 빈 과학자 칸에서 해당 기존 과학자를 선택해 실제 UI로 배정했다. 추가 과학자를 모집하거나 새로 만들지 않았다.

| 시설·위치 | 실제 선택한 과학자 | 저장된 시설 program ID / 과학자 ID |
|---|---|---|
| 경기 육상전 연구소, 프로빈스 `13416` | 김용관 `KOR_Yonggwan_Kim`, 육군 수준 2 | `6` / `2856` |
| 경상 조선공학 연구소, 프로빈스 `7121` | 황부길 `KOR_Bugil_Hwang`, 해군 수준 2 | `7` / `2853` |
| 강원 공기역학 및 항공전자 연구소, 프로빈스 `13418` | 조경연 `KOR_Gyeongyeon_Jo`, 항공 수준 2 | `8` / `2854` |

배정 전 선택 목록과 배정 후 시설 카드 화면은 저장소 밖 `C:/hoi/test/feature-integration-20261031/runtime-ui/bd1a-c2-{land,naval,air}-scientist-{selection,assigned}.jpg` 6장이다. 배정 후 카드에는 해당 인물·전문화 수준과 시설의 기본 연구 보너스 안내가 표시됐다. 이는 실제 배정과 UI 표시 관측이며, 안내된 일일 수치가 시간 경과로 누적됐다는 증거는 아니다.

UI로 저장한 배정 후 상태는 `real-dlc/runs/bd1a-ui/c2-three-scientists-assigned-Feb4-14.hoi4`, SHA-256 `781d546d298f60b1cd695f9b020fb680cf8f849766009848056d0a1986d8e9a3`이다. 같은 시각의 배정 전 `normal-soyang-drain-completed-Feb4-14.hoi4`와 비교해 세 시설의 빈 과학자 연결이 위 ID로 바뀌었고, 각 기존 character의 `scientist/is_assigned = yes`와 시설 program의 `scientist/scientist` 연결이 일치함을 확인했다. 이후 실제 해군 훈장 4개를 수여한 같은 시각의 별도 저장 `post-four-naval-medals-Feb4-14.hoi4`, SHA-256 `b5d77bd423424a385b2480bf5d977e0a3761b776ecc5cb607b460169e8b0d5c1`에서도 세 배정이 유지됐다. 후자의 저장 비교는 같은 실행의 상태 유지이며 저장 재로드 검사로 기록하지 않는다.

함경 핵 연구소는 목록에서 존재만 확인했고 과학자를 배정하지 않았다. 저장된 핵 program `9` / 프로빈스 `848`에는 과학자 ID가 없고 도상록 `2855`의 배정 상태도 설정되지 않았다. 핵 전문화 수준 3은 앞선 직접 효과 검사의 성장 보상이며 실제 핵 시설 배정 결과가 아니다. 세 배정 전후에는 시간을 진행하지 않았으며 프로젝트 선택·착수·돌파점 누적·완료는 검증하지 않았다.

별도 증거 파일 `C:/hoi/test/feature-integration-20261031/validation/c2-actual-three-scientist-assignments.json`에 세 실제 클릭 관측, 화면 6장의 SHA-256, 세 저장의 해시와 원래 직렬화 연결, 핵 미배정 및 검증 한계를 기록했다. 이 세 배정 관측을 앞선 시설·성장·중복 검사 8건과 섞어 중점 정상 진행이나 프로젝트 검증 완료로 계산하지 않는다.

### 별도 새 게임의 대체 주·공간 없음 검사

실제 실행 파일과 전체 DLC 프로필을 다시 시작한 `guard-c2-edge-raid-AB` 실행의 `1936.01.01.12`에서, 숨김 국가 이벤트 `HOK_FIDLC_research_factions.2`가 **6 PASS / 0 FAIL / 0 SKIP**을 기록했다. 실제 로그 시각은 `03:32:30`이며 BEGIN과 END가 모두 있다. 중점을 완료하지 않고 기존 production 효과를 직접 호출했으며, 진단이 시설을 배치해 아래 두 경계 조건을 만들었다.

| 검사 | 실제 엔진에서 확인한 결과 |
|---|---|
| 핵 선호 주 차단 준비 | 함경 `1028`에 육군 시설이 있고 핵 시설은 없음 |
| 핵 대체 주 선택 | 차단 시설을 보존하고 다른 소유·완전 통제 핵심 주에 핵 시설을 정확히 1곳 건설, 도상록 핵 수준 2→3 |
| 핵 반복 호출 | 핵 시설 수 1과 도상록 수준 3 유지 |
| 항공 건설 공간 없음 준비 | 시설이 없는 적격 주를 육군 시설로 채운 뒤 항공 시설 건설 조건을 만족하는 주가 없음을 확인 |
| 공간 없는 항공 첫 호출 | 항공 시설은 0곳, 조경연 항공 수준 1→2와 일회 지급 플래그 설정 |
| 공간 없는 항공 반복 호출 | 항공 시설 0곳과 조경연 수준 2·일회 지급 플래그 유지 |

6건 중 2건은 진단의 사전조건 구성 검사이고 4건은 production 효과의 결과 검사다. 앞선 지급·반복 8건이나 실제 UI 배정 3건과 구분한다. 이번 관측은 대체 주 및 공간 없음 분기를 확인하며, 과학자 부재·DLC 음성 경로·정상 중점 진행·프로젝트 진행·저장 재로드를 증명하지 않는다.

저장소 밖 `C:/hoi/test/feature-integration-20261031/real-dlc/runs/guard-c2-edge-raid-AB/startup/`에 로그 20개를 보존했고, `c2-edge-assessment.json`과 `c2-edge-capture-manifest.json`에 실제 행·검사 의미·해시·한계를 기록했다. C2 production 효과는 기존 SHA-256 `185874FC8EEE0A5256E654ECF25EAFD258C487D8E8DA53EAFF5C579B43DCEE87` 그대로이며 시작 시 보존 사본과 일치한다. C2 이벤트·on_action·집계 효과도 실행 전 보존 사본과 일치한다.

보존한 `error.log`에는 C2 관련 오류 행이 없다. 별도 소양강 진단 `events/HOK_FIGUARD_soyang.txt`의 `=` 비교 오류 5건은 그대로 보존하고 C2 결과와 분리했다. 이는 전체 모드의 오류 부재나 소양강 진단의 성공을 뜻하지 않는다.

### 진단 모드 제거 후 실제 프로세스 재시작·배정 유지

통합 담당자가 실제 게임을 완전히 종료하고 한국어 의존 모드와 저장소 모드만으로 다시 시작한 PID `21700` / 체크섬 `032c`, 실제 DLC 36개 환경에서 자신의 2월 4일 시험 저장을 UI로 불러왔다. `post-SSM5-promotion-Feb4-14.hoi4`의 SHA-256은 `C72709581AD87F5F7EDAD066A7D500DB76EB852A8EC4AA3F0606630A2A22ABD2`다. 시간을 진행하지 않고 같은 `1936.02.04.14`에 UI로 다시 저장한 외부 사본은 `C:/hoi/test/feature-integration-20261031/real-dlc/runs/final-clean-production/captain-mio-reloaded-resaved-Feb4-14.hoi4`, SHA-256 `5D56B3FCA8287BC62D7D235AC1F8A294974C87E109C9D522E436E7E2535B6653`이다.

두 실제 저장의 관측된 native 구조를 읽기 전용으로 비교하여 **13 PASS / 0 FAIL**을 확인했다. 이는 위 실제 UI 배정 3건의 과학자 ID·`is_assigned = yes`·시설 program 연결, 시설 4곳의 ID·위치·종류·과학자 연결 전체, 과학자 4명의 전문화 수준 벡터, 같은 게임 시각을 대조한 결과다. 김용관 `2856`은 경기 육상 시설 program `6` / `13416`, 황부길 `2853`은 경상 해군 시설 `7` / `7121`, 조경연 `2854`는 강원 항공 시설 `8` / `13418`에 유지됐다. 함경 핵 시설 `9` / `848`과 도상록 `2855`는 계속 미배정이었다. 배정·시설 준비·성장·edge 검사의 수에 이 유지 비교를 독립적인 신규 기능으로 합산하지 않는다.

증거는 `C:/hoi/test/feature-integration-20261031/real-dlc/runs/final-clean-production/c2-actual-process-reload-persistence.json`, SHA-256 `4BF12C244EDAFA053EB10D70A46DDEC8B9D7E041B08904768F707214BFF92075`에 있다. C2 production 효과의 SHA-256도 `185874FC8EEE0A5256E654ECF25EAFD258C487D8E8DA53EAFF5C579B43DCEE87`로 유지됐다. 이는 진단으로 시설을 준비한 같은 합성 게임의 실제 배정이 프로세스 재시작 후 남는지 확인한 결과다. 핵 과학자 배정, 프로젝트 선택·진행·돌파·완료나 다른 과거 저장의 호환성을 증명하지 않는다.

정상 중점 소요 기간, 실제 프로젝트 배정·완료, 시설·과학자 성장의 장기 균형, 다른 기존 저장 호환·DLC 조합·멀티플레이는 해당 시나리오를 관측하지 않고 완료로 기록하지 않는다. Git commit·push·배포는 이 구현의 일부가 아니다.
