# 한국 군수산업조직 고유 특성 명세

작성: 2026-10-31 (Asia/Seoul). 사용자 승인 범위 C1의 후속 개발이다. 호환성 복구 A1/A2와 구분하여 기존 한국 군수산업조직 15개에 고유 특성을 하나씩 추가한다. 설치본은 HOI4 `Operation Postern 1.19.3.0.c01a`, Steam build `25205862`다. 기준 브랜치·커밋은 `feat/korean-focus-expansion-ai` / `860efe7a3513148dc6964b7e0e3dfafd19addfb7`이며, 다른 승인 모듈의 미커밋 변경은 이 명세의 기준선에 섞지 않는다.

## 보존 계약과 선택 방식

기존 15개 조직의 ID, 이름·그림, `include`, 장비·연구 범주, 최초 특성, 기존 특성 트리, `allowed`, `available`을 보존한다. 공용 조직 파일 `00_generic_organization.txt`는 수정하지 않는다. 새 `add_trait` 한 개와 바로 위 contributor note만 각 한국 조직에 삽입했다. 이 추가 블록 15개를 제거하면 수정 전 한국 조직 파일의 모든 바이트가 재현된다.

추가 특성의 표시는 기본값인 항상 보임을 사용하며, `available = { FROM = { has_completed_focus = ... } }`가 해당 중점의 완료를 검사한다. 입력 범위는 군수산업조직이고 `FROM`은 소유 국가다. 중점을 완료해도 특성을 무료 지급하지 않는다. 기존 선행 특성과 조직 성장으로 얻는 특성 포인트를 갖추고 별도로 선택해야 한다. 기존 조직의 특성 구매 비용, 성장 요구량과 기존 특성의 조건·효과를 바꾸지 않는다.

새 보너스는 선택한 조직의 장비·생산 보정이며 국가 전체의 장비 성능을 일괄 수정하지 않는다. 장비 변형 갱신, 기존 생산선 적용과 이미 생산된 장비의 처리는 원래 MIO 시스템을 따르며, 정적 검사만으로 그 시점과 저장 동작을 검증했다고 주장하지 않는다. 기존 저장의 특성 자동 선택이나 소급 지급을 추가하지 않는다.

## 특성·보상·중점 연결

수치는 새 특성 하나의 추가 효과다. 같은 조직의 기존 효과와 합산되며 다른 조직의 보너스를 동시에 묶어 계산하지 않는다. 기존 중점 보상은 전부 보존한다.

| 조직 | 고유 특성 | 추가 효과 | 선택 가능해지는 기존 중점 |
|---|---|---|---|
| 대우중공업 | 호환 부품 체계 | 신뢰도 +5%, 생산 비용 −5% | `KOR_army_augmentation` |
| 현대정공 | 중전차 장갑 접합 | 장갑 +10% | `KOR_armored_focus` |
| 유경기계공업 | 보병 엄호 사격설계 | 돌파 +10% | `KOR_armored_focus` |
| 두산중공업 | 기동전용 동력계 | 최대 속도 +10% | `KOR_mobile_infantry` |
| 한국항공우주산업 | 기민한 국산 기체 | 공중 기동성 +10% | `KOR_korea_aerospace_industry` |
| 한진항공 | 장거리 항법 표준 | 항속거리 +10% | `KOR_daehanminguk_gonggun` |
| 진해 해군항공공창 | 해상 뇌격 조준기 | 해상 공격 조준 +10%, 해상 공격 +5% | `HOK_KOR_naval_air_coordination` |
| 대우조선해양 | 대구경 포탑 지지대 | 중포 공격 +10% | `KOR_large_surface_fleet` |
| 현대중공업 | 항공모함 블록 건조 | 항공모함 생산 비용 −10% | `KOR_carrier_focus` |
| 대한조선공사 | 호위함 수중탐지 체계 | 잠수함 탐지 +10%, 대잠 공격 +5% | `KOR_daehanminguk_haegun` |
| 경원마린시스템즈 | 습격함 어뢰 사격통제 | 어뢰 공격 +10% | `KOR_commerce_raiding` |
| 국군부산조병창 | 소총 정밀 가공 | 대인 공격 +10% | `KOR_new_model_rifle` |
| 한국화약 | 포병 탄약 일관성 | 대인 공격 +10% | `KOR_improved_artillery` |
| 기아자동차 | 경제적인 수송 구동계 | 연료 소비 −10% | `KOR_mobile_infantry` |
| 군인공제회 | 지원장비 공동규격 | 생산 비용 −10% | `KOR_expansion_of_non_combat_support_units` |

현대중공업 특성은 추가로 `limit_to_equipment_type = { mio_cat_eq_all_carrier }`를 사용한다. 다른 특성은 해당 조직이 원래 지원하던 장비 범주를 따른다. 일부 모듈에 의존하는 함정 공격·탐지 수치는 그 능력이 있는 장비에 적용하는 MIO 계약을 보존한다. 기존 육군·해군·항공 중점의 선행·배타·기간·좌표와 AI는 C1에서 변경하지 않는다. 소총과 포병처럼 원래 상호배타 중점에 걸린 보상은 선택한 정책의 해당 특성만 열리며, 두 경로의 혜택을 동시에 얻는 것으로 계산하지 않는다.

공유 중점 파일의 각 대응 `completion_reward`에는 AAT 조건 안에서 `mio:<조직 ID> = { unlock_mio_trait_tooltip = <특성 ID> }`를 표시한다. 효과는 선택 가능 안내만 담당한다. 같은 블록에 `custom_effect_tooltip = HOK_KOR_mio_specialization_purchase_tt`를 표시하여 별도 선택과 선행 특성·특성 포인트 요건을 알린다. 정확한 13개 중점→15개 호출 매핑은 [기계 판독 명세](data/HOK_KOREAN_MIO_SPECIALIZATION_ICON_MANIFEST.json)의 `focus_reward_snippets`에 있다. 중점 삽입과 실제 화면의 결과는 통합 기록을 따른다.

## 기존 트리와 배치

아래 parent와 anchor는 동일하며 `generic_mio_` 접두사를 생략했다. 경원은 `trait_long_range_raiding`을 배치 anchor로 사용하고 선행은 장거리 또는 고속 습격 중 하나를 허용한다. 따라서 원래의 두 상호배타 경로 모두 새 특성에 접근할 수 있다. 배치 관계가 선행 조건을 대신하지 않으며 두 값은 각각 명시한다.

| 조직 | 기존 parent/anchor | 상대 x/y | 해석한 x/y |
|---|---|---|---|
| 대우중공업 | `trait_simplified_suspension` | −1/+1 | 0/1 |
| 현대정공 | `trait_wide_tracks` | −1/+1 | 0/1 |
| 유경기계공업 | `trait_battle_tank_specifications` | +2/0 | 8/0 |
| 두산중공업 | `quality_assurance_routines` | −1/+1 | 3/2 |
| 한국항공우주산업 | `trait_advanced_aerodynamics` | +2/0 | 8/0 |
| 한진항공 | `trait_conservative_designs` | +2/0 | 6/0 |
| 진해 해군항공공창 | `trait_navigation_equipment` | +2/0 | 6/0 |
| 대우조선해양 | `trait_primary_battery_layout` | +2/0 | 10/0 |
| 현대중공업 | `trait_primary_fire_director_control` | +2/0 | 10/0 |
| 대한조선공사 | `trait_submarine_hunters` | +2/0 | 3/0 |
| 경원마린시스템즈 | `trait_long_range_raiding` | +3/+1 | 4/1 |
| 국군부산조병창 | `trait_drum_pattern_sights` | −1/+1 | 0/1 |
| 한국화약 | `trait_advanced_barrel_forging` | −1/+1 | 5/1 |
| 기아자동차 | `trait_medium_machinegun_mounts` | −1/+1 | 3/1 |
| 군인공제회 | `trait_private_scientists_program` | −2/0 | 3/0 |

경원 특성의 초기 검토 좌표 4/0은 기존 장거리·고속 습격 상호배타 연결 위였으므로 실제 구현은 4/1을 사용한다. 선행 조건과 보상은 그대로다. 새 노드 중심은 기존 노드와 중복되지 않고 기존 선행·상호배타 연결의 직선 모델 위에 있지 않다. 새 연결의 직선 모델도 관계없는 기존 노드 중심을 지나지 않는다. 이는 실제 엔진의 곡선·꺾은선, 아이콘 사각형, 이름판, 클릭 영역과 스크롤을 관측한 결과가 아니다.

모든 기존 좌표를 보존한다. 새 특성 때문에 세로 경계가 증가한 트리는 없으며, 가로 경계의 변화는 각 조직별로 기계 판독 명세의 `before_bounds`와 `after_bounds`에 기록했다. 같은 위치를 쓰는 기존 경원의 MTG 유무 대체 노드는 그대로 유지한다.

## 그림·문구·저장 파일

- 조직 정의: `common/military_industrial_organization/organizations/KOR_organization.txt`.
- Sprite: `interface/HOK_KOR_mio_specializations.gfx`. 신규 15개 이름은 `GFX_HOK_KOR_mio_trait_*`이며 기존 글로벌 sprite를 덮어쓰지 않는다.
- Runtime 그림: `gfx/interface/military_industrial_organization/HOK_KOR/*.dds` 15개. 설치본 MIO 능력치 그림 중 각각의 전문화와 맞는 그림을 골라 바이트 그대로 복사했다. 원본 크기 48×48, 32비트·알파·DDS 헤더와 mip 데이터를 보존한다. 원본을 재압축하거나 색상을 바꾸지 않았다.
- 선택한 원본 사본: `docs/assets/mio-specializations/source/`. 동일한 비용·공격 능력치 그림의 재사용은 해당 기능을 나타내며 새로 그린 회사 로고가 아니다.
- 그림 출처·원본/최종 SHA-256·sprite·전문분야·조건·좌표: [이미지 및 구현 manifest](data/HOK_KOREAN_MIO_SPECIALIZATION_ICON_MANIFEST.json).
- 원작자: **Paradox Interactive**. 같은 HOI4 게임의 모드 안에서 원본 게임 자산을 재사용한다. 공개 이미지 팩이나 새 AI 생성물로 기록하지 않으며 다른 용도의 포괄적인 그림 라이선스를 주장하지 않는다. 후속 기여는 특성 설계, 그림 선정·로컬 복사, sprite·문구·중점 연계다.
- 검토 그림: [48px 원본 크기와 2배 표시](assets/mio-specializations/preview.png). 실제 크기에서 각 능력치 기호, 알파 여백과 어두운 UI 배경 대비를 확인했다. 게임 UI 화면의 결과는 아니다.
- 문구: `localisation/korean/HOK_KOR_mio_specializations_l_korean.yml`, `localisation/english/HOK_KOR_mio_specializations_l_english.yml`. UTF-8 BOM·각 언어 header·동일 contributor note, 31개 동일 key를 유지한다. 프로젝트의 기존 언어 계약에 따라 두 파일 모두 한국어 문구를 제공한다.

## 설치본 문법 근거

원본 디렉터리 `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV`는 읽기 전용으로 사용했다.

- `common/military_industrial_organization/organizations/_documentation.md:126–200`: 추가 특성의 parent, `available`의 MIO/FROM 범위, 장비 제한, 보너스 종류와 상대 좌표.
- 같은 파일 `:219–240`: `include`에 `add_trait`를 추가하는 loader 계약. 기본 특성 트리 수정과 신규 특성 추가를 구분한다.
- `ENG_organization.txt:87–119`: 추가 고유 특성, 기존 parent를 기준으로 한 상대 배치, 생산 효율 보상.
- `ENG_organization.txt:560–576`: 탐지·해상 조준 같은 복수 능력치 보상.
- `GER_organization.txt:1204–1210`: `available` 안의 `FROM = { has_completed_focus = ... }`와 장비 범주 제한.
- `GER_organization.txt:1683,1859,1962,2021,2591`: 항공모함 제한, 기동성·항속거리·연료 소비·해상 공격 보상.
- `documentation/effects_documentation.md:8507–8521`: `unlock_mio_trait_tooltip`은 `INDUSTRIAL_ORG` 범위의 표시 효과다. 실제 특성을 구매·완료하는 effect가 아니다.
- `common/national_focus/germany.txt:3799,3911–3912`: 중점에서 `mio:<ID>` 범위를 사용한 특성 선택 가능 안내.

## 검증 결과와 남은 범위

C1 전용 소스·자산 정적 검토는 **201 PASS / 0 FAIL**이다. 조직 15개와 특성 15개, 공용 parent 존재·상대 좌표 해석·새 중심 중복 및 직선 연결 모델, 기존 조직 파일의 바이트 보존, 중점 ID 유일성, 15개 sprite의 로컬 그림 연결, 15개 원본·선택 사본·runtime SHA-256 일치, DDS 크기·헤더·투명/비투명 픽셀, 양쪽 localisation BOM·header·31개 key를 확인했다. 외부 검토 결과는 `C:/hoi/test/feature-integration-20261031/c1/static-review.json`에 있다. 이 숫자는 통합 검사나 다른 모듈의 결과에 중복 합산하지 않는다.

수정 전 조직 파일 SHA-256은 `87052e3ad3c21fcc97c4f697b6a682cdf04e44eefa0160ac15e280a317873959`이며 별도 외부 기준선에 보존했다. 최종 조직 파일과 이미지의 해시는 manifest가 기록한다. 공유 중점 파일의 기존 보상 보존은 통합 검토가 따로 확인한다.

### 2026-10-31 실제 DLC 실행과 UI 구매

실제 설치본 `Operation Postern 1.19.3.0.c01a` / build `25205862`, 한국어 환경에서 Hearts of Korea와 한국어 의존 모드를 사용하는 시험 playset을 실행했다. 이 실행은 실제 DLC 36개를 활성화했고 Arms Against Tyranny의 원래 DLC 조건을 통과했다. 실행 체크섬은 `bd1a`이며, 외부에서 동결한 진단 fixture와 선택형 해군 훈장 진단 define이 함께 적용된 합성 새 게임이다. 배포용 단독 체크섬으로 기록하지 않는다. C1 조직 소스는 SHA-256 `057374d4cbbd30ae88a5e61036b01a52efe9d72226457340ca656470a6b589a8`인 동결 소스를 사용했다. 실제 사용자 실행 프로필의 백업·임시 전환·복구는 통합 기록에서 관리한다.

엔진 진단은 **135 PASS / 0 FAIL / 0 SKIP**이다. 새 게임의 60개 검사는 조직·특성 등록, 신규 특성 미취득, 중점 전 사용 불가를 각각 15개씩 확인했다. 이어 C1-1 준비 결정의 75개 검사는 중점 강제 완료 후 잠금 해제, 기존 부모 미취득 시 구매 차단, 부모 준비 후 구매 가능, 새 특성 미취득 유지, UI 구매용 조직 규모 준비를 각각 확인했다. 중점과 기존 부모 특성 및 조직 규모는 진단 효과로 준비했으며 자연 진행·정상 성장의 검증으로 기록하지 않는다. 이 준비 효과는 새 `HOK_KOR_` 특성을 완료하지 않는다.

그 뒤 1936-01-21 01:00에 일시정지한 상태에서 **15개 신규 특성을 모두 실제 UI로 구매**했다. 각 조직의 새 금색 테두리 노드를 열고 정확한 특성 이름·1점 비용이 표시된 확인 창에서 승인했으며, 특성 점수가 각각 1점 줄었다. 부모가 열린 준비 상태에서 구매한 결과이므로 실제 클릭과 비용 지불은 확인했지만, 중점과 부모를 자연 진행으로 취득한 결과는 아니다. 실제 포인트 변화는 대우중공업 3→2, 현대정공 4→3, 유경기계공업 4→3, 두산중공업 4→3, 한국항공우주산업 5→4, 한진항공 3→2, 진해 해군항공공창 3→2, 대우조선해양 3→2, 현대중공업 3→2, 대한조선공사 3→2, 경원마린시스템즈 3→2, 국군부산조병창 3→2, 한국화약 3→2, 기아자동차 3→2, 군인공제회 5→4다.

각 트리에서 새 아이콘·부모 연결·구매 확인 문구에 접근할 수 있었다. 대우조선해양과 현대중공업의 오른쪽 끝 새 노드는 원래 가로 스크롤로 접근했다. 이 관측은 15개 구매 경로의 접근성 증거이며 전체 트리의 모든 연결·클릭 영역·배타 경로를 검토한 결과는 아니다. 현대정공은 통합 담당자가, 나머지 14곳은 C1 담당자가 조작했다. `C:/hoi/test/feature-integration-20261031/runtime-ui/bd1a-mio-*-before.jpg`, `*-confirm.jpg`, `*-purchased.jpg`에 구매 전·확인 창·포인트 차감 후 화면이 있다. 현대정공은 `bd1a-mio-rotem-buy.jpg`와 `bd1a-mio-rotem-purchased.jpg`를 사용한다.

C1-2 관측 결정을 실제 오른쪽 실행 버튼으로 눌렀으며, `game.log`의 실제 시각 02:37:10 / 게임 시각 1936-01-21 01:00에 `C1_01`부터 `C1_15`까지 `new_trait_completed_yes` 15건을 기록했다. 이는 위 실제 클릭 증거와 대조하는 완료 상태 관측이다. 완료 트리거만으로 클릭 원인이나 비용을 증명하지 않는다. C1-3 결정도 같은 일시정지 상태의 02:37:18에 실행하여 국군부산조병창의 `FIDLC Rifle AFTER UI purchase`와 군인공제회의 `FIDLC Support AFTER UI purchase` 변형을 만들었다. 실제 생산 선택 목록에서 BEFORE/AFTER 변형과 해당 MIO 로고가 표시되는 것을 확인했다. 비교용 변형 생성·목록 표시는 실제 장비 능력치나 생산 비용 변화의 수치 검증으로 합산하지 않는다. 구매 확인 창의 장비 변형 갱신 체크는 기본 체크 상태를 유지했다.

구매·관측·비교용 장비 생성 뒤 실제 UI로 저장했다. 엔진의 기존 `_temp` 파일명 동작 때문에 이 작업이 앞서 만든 `KOR_1936_01_21_01_temp.hoi4`만 사용했고, 덮어쓰기 전 이를 외부에 다시 보존했다. 사용자 원래 1월 1일 저장 및 `autosave_temp.hoi4`는 이 구매 작업에서 수정하지 않았다. 최종 외부 저장은 `C:/hoi/test/feature-integration-20261031/real-dlc/runs/bd1a-ui/post-mio-purchases-and-probes-Jan21.hoi4`, SHA-256 `f20ab6806a75d1b17361e8c75dcb3a0a29934177deea775c1d3a0eaa989f7636`이다. 이 저장과 준비 후 기준선 `baseline-after-all-staging.hoi4`의 실제 직렬화 구조를 읽어 비교한 결과는 **150 PASS / 0 FAIL**이며, `C:/hoi/test/feature-integration-20261031/validation/mio-actual-purchases.json`에 기록했다. 15개 조직 모두 신규 특성의 정확히 1회 추가, 기존 특성 보존, 점수 1점 차감, 조직 ID·규모·자금 유지 등을 확인했다. 150개 저장 검사는 엔진 135개 검사와 일부 사실이 겹치는 별도 직렬화 증거이며 이를 합쳐 독립적인 285개 기능 검사로 주장하지 않는다.

실행 로그 사본은 `C:/hoi/test/feature-integration-20261031/real-dlc/runs/bd1a-ui/game-after-mio-purchases.log`와 `error-after-mio-purchases.log`에 보존했다. 위 `bd1a` 구매 기록 자체는 현재 동결 소스의 등록·잠금·구매·저장까지 증명하며, 실제 재불러오기는 아래 별도 실행에서 확인했다. 실제 장비/생산 수치 비교, 정상 중점·조직 성장 순서, 모든 상호배타 경로, DLC 없음, AI 구매, 다른 기존 저장 호환성, 장기 플레이와 멀티플레이는 미검증이다. 기본 `ai_will_do`를 바꾸지 않고 엔진의 원래 MIO 보너스 가중치를 사용하며, AI의 실제 특성 선택은 별도 관측해야 한다. Git commit·push·공개 배포는 이 구현에 포함하지 않는다.

### 진단 모드 제거 후 실제 프로세스 재시작·저장 재불러오기

같은 날 실제 게임 프로세스를 완전히 종료한 뒤 한국어 의존 모드와 저장소 모드만 활성화하여 PID `21700` / 체크섬 `032c`로 다시 시작했다. 실제 DLC 36개는 유지했고 외부 진단 모드와 선택형 해군 훈장 define은 제거했다. 통합 담당자가 실제 UI로 자신의 `post-SSM5-promotion-Feb4-14.hoi4`를 불러온 뒤 `1936.02.04.14` 일시정지 상태에서 다시 저장했다. 원본 시험 저장의 SHA-256은 `C72709581AD87F5F7EDAD066A7D500DB76EB852A8EC4AA3F0606630A2A22ABD2`이며, 재저장 사본은 `C:/hoi/test/feature-integration-20261031/real-dlc/runs/final-clean-production/captain-mio-reloaded-resaved-Feb4-14.hoi4`, SHA-256 `5D56B3FCA8287BC62D7D235AC1F8A294974C87E109C9D522E436E7E2535B6653`이다. 불러오기와 재저장 사이에 시간을 진행하지 않았다.

앞서 실제 UI 구매한 1월 21일 저장과 이 재저장본의 원래 `countries/KOR/production/industrial_organisations` 구조를 비교한 결과는 **120 PASS / 0 FAIL**이다. 15개 조직 모두 동일한 엔진 조직 ID를 유지했고, 새 특성은 각각 정확히 1회 취득한 상태이며, 기존 부모 취득 기록과 유효한 잔여 점수·조직 규모가 남아 있었다. 비교 결과는 `C:/hoi/test/feature-integration-20261031/real-dlc/runs/final-clean-production/mio-actual-process-reload-persistence.json`에 기록했다. C1 조직 production 소스의 SHA-256은 이 재검사에서도 `057374D4CBBD30AE88A5E61036B01A52EFE9D72226457340CA656470A6B589A8`로 같았다.

이는 이번 합성 게임에서 실제 구매한 특성 15개의 시간 경과와 프로세스 재시작 후 저장 유지 검증이다. 120개 비교는 앞선 구매·상태 검사와 겹치는 유지 조건이므로 독립적인 신규 기능 수로 합산하지 않는다. 임의의 과거 버전 저장, 정상 중점·MIO 성장·AI 구매, 장비 능력치·생산 수치, 장기 플레이·멀티플레이의 검증으로 확대하지 않는다.
