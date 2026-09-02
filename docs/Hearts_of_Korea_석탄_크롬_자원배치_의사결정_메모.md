# Hearts of Korea 석탄·크롬 자원 배치 및 구현 가이드

> 문서 상태: **구현 승인 전 설계 문서 — 게임 코드 미적용**  
> 대상 버전: **HOI4 Operation Postern 1.19.2.0.a729 (d245)**  
> 저장소 기준: `main` / `21a9143`  
> 작성 기준일: 2026-09-03  
> 관련 문서: [검토용 DOCX](./Hearts_of_Korea_석탄_크롬_자원배치_의사결정_메모.docx)

이 문서는 한반도의 석탄과 크롬을 고증에 맞는 방향으로 추가하면서도, 1.19 에너지 경제와 멀티플레이 밸런스를 과도하게 완화하지 않기 위한 **구체적인 구현 명세**다. 아래의 Paradox Script는 구현 예시일 뿐이며 이 문서 작성 과정에서는 production 파일을 수정하지 않았다.

## 1. 최종 권고

기본안은 **시작 석탄 10 → 개발 후 석탄 15**, **함경 시작 크롬 1**이다.

| 주 | state ID | 시작 석탄 | 개발 추가 | 개발 후 석탄 | 시작 크롬 |
|---|---:|---:|---:|---:|---:|
| 평안 | 527 | 5 | +1 | 6 | 0 |
| 함경 | 1028 | 4 | 0 | 4 | 1 |
| 강원 | 1029 | 1 | +3 | 4 | 0 |
| 전라 | 1082 | 0 | +1 | 1 | 0 |
| 경기·충청·경상·황해·제주 | - | 0 | 0 | 0 | 0 |
| **합계** | - | **10** | **+5** | **15** | **1** |

구현은 다음 두 층으로 나눈다.

1. 1936년 시작값은 `history/states`의 정적 `resources` 블록에 넣는다.
2. 생산 설비·운송망 확충분은 기존 국토개발종합계획 결정 3개의 완료 효과에 넣는다.

이 수치는 역사적 생산 톤수의 환산값이 아니다. 사료로 **배치 지역과 상대적 비중**을 정하고, 게임 수치는 HOI4 1.19.2의 에너지 경제를 고려해 낮게 잡은 디자인 판단이다.

## 2. 구현 경로를 먼저 확정한 이유

이 작업에는 새 자원 정의, 새 state, 새 중점, 새 결정이 필요하지 않다.

- `coal`과 `chromium`은 이미 게임에 존재하는 자원 타입이다.
- 시작 자원은 기존 state 파일의 `resources` 블록에 키만 추가하면 된다.
- 프로젝트에는 평안·강원·전라를 각각 개발하는 일회성 결정이 이미 있다.
- 해당 결정들은 `fire_only_once = yes`이고 각 state의 통제를 요구한다.
- 프로젝트 중점과 1.19.2 바닐라 모두 state scope의 `add_resource` 사용례를 제공한다.
- 따라서 새 ID, 새 현지화 키, 새 플래그를 만들지 않는 것이 최소 변경이다.

### 선택한 후속 개발 방식

후속 석탄 `+5`는 다음 기존 결정에 분배한다.

| 기존 결정 | 파일 위치 | 기존 대상 state | 추가 효과 |
|---|---|---:|---:|
| `KOR_develop_pyeongan` | `common/decisions/KOR_decision.txt:1285-1311` | 527 | coal +1 |
| `KOR_develop_gangwon` | `common/decisions/KOR_decision.txt:1312-1338` | 1029 | coal +3 |
| `KOR_develop_jeolla` | `common/decisions/KOR_decision.txt:1161-1191` | 1082 | coal +1 |

이 방식은 세 지역의 개발을 같은 시스템에서 처리한다. 기존 함경·강원 지하자원 중점에 일부 보상만 섞으면 평안과 전라를 위한 별도 처리 경로가 필요해지고, 같은 `+5`가 중점과 결정 양쪽에서 중복 적용될 위험이 커진다.

## 3. 확인된 현재 상태

### 3.1 프로젝트 state와 자원

| 주 | 확인 위치 | 현재 `resources` | 판정 |
|---|---|---|---|
| 평안 | `history/states/527-North Korea.txt:1-6` | aluminium 5 | coal 없음 |
| 함경 | `history/states/1028 - Hamgyong.txt:2-8` | steel 15, tungsten 28 | coal·chromium 없음 |
| 강원 | `history/states/1029 - Gangwon.txt:1-10` | tungsten 23, steel 4 | coal 없음 |
| 전라 | `history/states/1082 - Jeolla.txt:2-42` | `resources` 블록 없음 | 시작 coal 없음 |

state 이름과 ID는 `localisation/korean/replace/HoK_state_name_l_korean.yml:4-12`에서도 교차 확인했다. 파일명이 `527-North Korea.txt`여도 현재 프로젝트에서 state 527의 표시명은 **평안**이다. 파일이나 state ID를 이 작업에서 바꾸지 않는다.

### 3.2 대상 버전 바닐라와의 차이

설치된 1.19.2 바닐라의 `history/states/1028 - Hamgyong.txt:7-10`에는 다음 값이 있다.

```txt
resources = {
    steel = 10
    tungsten = 10
    coal = 4
}
```

현재 모드는 같은 state 1028을 전체 정의하지만 `coal = 4`를 포함하지 않는다. 따라서 target 바닐라에서 보이는 함경 석탄 4가 모드 적용 시 사라진다.

- 함경 `coal = 4`: **CONFIRMED — 1.19.2 target 정렬값**
- 평안·강원의 석탄과 함경 크롬: **DESIGN JUDGMENT — 고증 기반 신규 밸런스**
- 함경 석탄 4를 과거 모드 동작의 “복원”이라고 부르는 것: **부정확함**

### 3.3 1.19.2 에너지 수치

설치된 `common/defines/00_defines.lua:624-628`의 원시 정의값은 다음과 같다.

| 정의 | 값 | 의미 |
|---|---:|---|
| `RESOURCE_TO_ENERGY_COEFFICIENT` | 9.0 | coal 1의 기본 에너지 변환계수 |
| `BASE_COUNTRY_ENERGY_PRODUCTION` | 10.0 | 국가 기본 에너지 생산 |
| `ENERGY_SCALING_COST_BY_FACTORY_COUNT` | 0.0225 | 공장 수에 따른 소비 스케일링 |
| `BASE_ENERGY_COST` | 0.25 | 공장 기본 에너지 소비 |
| `ENERGY_COST_CAP` | 6.6 | 공장 에너지 소비 상한 |

현재 9개 한국 state의 시작 건물 정의를 합산하면 민간공장 9, 군수공장 4, 조선소 1로 **총 14개**다. DOCX의 “총 13개(민간 9·군수 3·조선소 1)” 표기는 현재 working tree 기준으로 바로잡았다.

coal 1이 곧바로 플레이어 가용 에너지 9를 뜻하는 것은 아니다. 기반시설, 무역, 수출, 점령·통제, 기술과 기타 수정치가 실제 표시량과 가용량을 바꾼다. 그래도 시작 coal 15는 초기 한국에 상당히 후한 자립 보정이 될 가능성이 높으므로 기본안에서는 10으로 제한한다.

## 4. 역사적 근거와 해석 한계

### 석탄

한반도 북부의 평안·함경권은 주요 탄전 지역이었다. 남부에서는 삼척·영월의 강원권, 화순의 전라권, 문경·은성의 경상권 순으로 알려진 생산 기반이 있었다.

USGS의 1940년 남한 무연탄 생산 표는 삼척·영월 986천 톤, 화순 180천 톤, 문경·은성 26천 톤을 제시한다. 이는 남부 합계에서 각각 약 82.7%, 15.1%, 2.2%다. 다만 이 표는 1936년 자료도 아니고, 한반도 전체와 모든 탄종을 비교한 자료도 아니다. 따라서 남부 개발의 방향을 정하는 근거로만 사용한다.

한반도 석탄의 상당 부분은 무연탄 또는 저등급탄이었다. 이를 고품질 제철용 코크스탄의 완전 자급으로 해석해서는 안 된다. HOI4의 coal은 산업 에너지의 추상화다.

### 크롬

1940년 자료는 함경북도 부령군의 두 곳에서 크롬철석 산출과 과거 소규모 가행을 기록한다. 동시에 광체가 불규칙하고 산재하며 잔존 광량이 적어 추가 탐사가 필요하다고 평가한다.

- 부령 일대 크롬 산출의 존재: **STRONGLY SUPPORTED**
- 1936년 경제적 상업 생산 규모: **UNPROVEN**
- 함경 `chromium = 1`: **DESIGN JUDGMENT**
- 시작 크롬 2 이상 또는 반복 증산: **권장하지 않음**

## 5. 구현 대상 파일

기본안을 구현할 경우 production 변경 대상은 정확히 4개다.

| 파일 | 변경 내용 | 변경 분류 |
|---|---|---|
| `history/states/527-North Korea.txt` | 평안 시작 coal 5 추가 | 신규 밸런스 |
| `history/states/1028 - Hamgyong.txt` | 함경 시작 coal 4, chromium 1 추가 | target 정렬 + 신규 밸런스 |
| `history/states/1029 - Gangwon.txt` | 강원 시작 coal 1 추가 | 신규 밸런스 |
| `common/decisions/KOR_decision.txt` | 평안 +1, 강원 +3, 전라 +1 | 단계적 개발 밸런스 |

다음은 변경하지 않는다.

- `history/states/1082 - Jeolla.txt`: 전라 coal은 시작값이 아니라 결정 보상이다.
- `common/national_focus/korea.txt`: 기본안은 기존 결정을 사용한다.
- `localisation/**/*.yml`: 기존 결정명과 카테고리를 그대로 쓰므로 필수 변경이 없다.
- `map/`, province/state ID, `common/resources/`, `descriptor.mod`, `replace_path`
- 바닐라 설치 폴더와 Steam Workshop 관리 복사본

## 6. 정적 시작 자원 — 정확한 삽입 형태

> 아래 블록은 **구현 후 목표 형태**다. 기존 `resources` 내용을 교체하지 말고 필요한 줄만 추가한다. 각 state에 두 번째 `resources` 블록을 만들지 않는다.

### 6.1 평안 — state 527

대상: `history/states/527-North Korea.txt:4-6`

```txt
resources={
    aluminium=5.000
    coal=5.000
}
```

### 6.2 함경 — state 1028

대상: `history/states/1028 - Hamgyong.txt:5-8`

```txt
resources={
    steel=15.000
    tungsten=28.000
    coal=4.000
    chromium=1.000
}
```

### 6.3 강원 — state 1029

대상: `history/states/1029 - Gangwon.txt:7-10`

```txt
resources={
    tungsten=23.000
    steel=4.000
    coal=1.000
}
```

### 정적 자원에서 지켜야 할 사항

- `resources`는 state 루트에서 `history`와 같은 단계에 둔다.
- 기존 aluminium, steel, tungsten 값을 보존한다.
- 시작값에는 `add_resource`를 사용하지 않는다.
- 기존 소유권, 코어, 건물, 승점, province 목록을 건드리지 않는다.
- state ID와 파일명을 바꾸지 않는다.
- 파일 전체를 재정렬하거나 줄바꿈을 일괄 변환하지 않는다.

## 7. 후속 개발 — 기존 일회성 결정에 넣는 형태

설치된 1.19.2의 `documentation/effects_documentation.md:2056-2070`은 `add_resource`의 지원 scope를 `STATE`, `COUNTRY`로 명시한다. state 숫자 블록 안에서는 별도 `state = ...`를 쓰지 않아도 된다.

```txt
add_resource = {
    type = coal
    amount = 1
}
```

`amount`는 목표 총량이 아니라 **현재 값에 더할 증분**이다. `days`를 지정하면 임시 자원이 되므로 영구 개발 보상에는 `days`를 넣지 않는다.

### 7.1 전라 개발 결정 — coal +1

대상 anchor: `KOR_develop_jeolla` → `remove_effect` → `1082 = { ... }`

```diff
  1082 = {
      set_state_category = large_town
      add_extra_state_shared_building_slots = 1
+     add_resource = {
+         type = coal
+         amount = 1
+     }
      add_victory_points = {
          province = 13429
          value = 1
      }
```

### 7.2 평안 개발 결정 — coal +1

대상 anchor: `KOR_develop_pyeongan` → `remove_effect` → `527 = { ... }`

```diff
  527 = {
      set_state_category = large_city
      add_extra_state_shared_building_slots = 1
+     add_resource = {
+         type = coal
+         amount = 1
+     }
      add_victory_points = {
          province = 9790
          value = 1
      }
```

### 7.3 강원 개발 결정 — coal +3

대상 anchor: `KOR_develop_gangwon` → `remove_effect` → `1029 = { ... }`

```diff
  1029 = {
      set_state_category = town
      add_extra_state_shared_building_slots = 1
+     add_resource = {
+         type = coal
+         amount = 3
+     }
      add_victory_points = {
          province = 1148
          value = 1
      }
```

### 이 효과가 일회성인 이유

세 결정에는 이미 다음 조건이 있다.

- `fire_only_once = yes`
- 해당 state에 대한 `controls_state = ...`
- `has_tech = construction3`
- `num_of_civilian_factories_available_for_projects > 5`
- 비용 150, 기간 180일, 민간공장 5개 사용
- `KOR_comprehensive_national_development_plan` 완료 후 표시

따라서 기본안에서는 새 플래그를 만들 필요가 없다. 나중에 `fire_only_once = no`로 바꾸거나 다른 국가도 같은 개발 결정을 쓰게 만들 경우에는 target 바닐라 `common/decisions/JAP.txt:4515-4570`처럼 state flag를 가시 조건과 완료 효과에 함께 사용해야 한다.

### `remove_effect`를 유지하는 이유

현재 KOR 개발 결정은 180일짜리 결정의 보상을 모두 `remove_effect`에 둔다. target 바닐라의 석탄 개발 결정도 `remove_effect` 안의 state scope에서 `add_resource`를 사용한다. 이 작업만을 위해 기존 효과를 `complete_effect`로 이동하면 결정 생명주기와 취소 동작까지 바꾸는 불필요한 리팩터링이 된다.

현재 세 결정의 `controls_state`는 결정을 시작할 때 확인하는 `available` 조건이며, 180일 공사 중 통제권 상실을 검사하는 `cancel_trigger`는 없다. 따라서 공사 도중 해당 state를 잃더라도 지정된 숫자 state에 보상이 적용될 가능성이 있다. 기존 도시화·슬롯·승점 보상도 이미 같은 구조이므로 자원 추가만의 신규 문제는 아니지만, 이를 고치려면 target 바닐라 `common/decisions/JAP.txt:4547-4549`와 같은 취소 조건을 별도 동작 변경으로 검토해야 한다.

## 8. 문법 근거

### 프로젝트 내부의 동일 문법

`history/states/528-Nagasaki.txt:8-11`에는 정적 `resources` 블록 안에 `chromium`과 `coal`을 함께 두는 직접적인 예가 있다.

```txt
resources = {
    chromium = 32
    coal = 15
}
```

`common/national_focus/korea.txt:476-487`에는 state 1028에 steel과 tungsten을 더하는 효과가 있다.

```txt
1028 = {
    add_resource = {
        type = steel
        amount = 15
    }
    add_resource = {
        type = tungsten
        amount = 5
    }
}
```

`common/national_focus/korea.txt:505-516`에는 state 1029에 steel과 aluminium을 더하는 같은 구조가 있다. 즉, 이 모드에서 숫자 state scope와 `add_resource`의 조합은 이미 사용 중이다.

### target 1.19.2의 동일 문법

- `documentation/effects_documentation.md:2056-2070`: `add_resource`의 scope와 선택 인자
- `common/national_focus/belgium.txt:7543-7553`: 중점 완료 시 state coal 추가
- `common/decisions/JAP.txt:4515-4570`: 기간형 결정의 `remove_effect`에서 state coal 추가 및 state flag 설정
- `history/states/1028 - Hamgyong.txt:7-10`: 정적 `coal = 4`

따라서 이 문서의 구현 형태는 다른 Paradox 게임이나 과거 버전의 추측 문법이 아니라, 설치된 1.19.2와 현재 프로젝트 양쪽에서 확인한 문법이다.

## 9. 하면 안 되는 구현

- `common/resources`에 coal이나 chromium을 새로 정의하지 않는다.
- `resources`를 `history = { ... }` 안에 넣지 않는다.
- 한 state에 `resources` 블록을 두 개 만들지 않는다.
- `amount = 15`를 “최종 15”로 생각해 결정에 넣지 않는다. `add_resource`는 증분이다.
- 영구 자원에 `days = ...`를 넣지 않는다.
- 중점과 결정 양쪽에 같은 `+5`를 넣지 않는다.
- 크롬을 2 이상 주거나 반복 증산하지 않는다.
- `supported_version` 변경을 호환성 수정으로 취급하지 않는다.
- `replace_path`를 추가하지 않는다.
- 지도 비트맵, province ID, state ID를 건드리지 않는다.
- 기존 steel, tungsten, aluminium 보상을 석탄으로 교체하지 않는다.
- 바닐라 설치 파일이나 Workshop 복사본을 수정하지 않는다.

## 10. 구현 순서

1. Git branch, HEAD, 기존 dirty 상태를 기록한다.
2. 런처가 실제로 로드하는 로컬 개발 모드 경로와 플레이세트를 확인한다.
3. 수정 전 로그를 별도 보존한다.
4. 함경 `coal = 4`만 먼저 적용하고 새 게임에서 target 정렬을 확인한다.
5. 평안 `coal = 5`, 강원 `coal = 1`, 함경 `chromium = 1`을 적용한다.
6. 시작 자원 합계가 coal 10, chromium 1인지 확인한다.
7. 기존 세 개발 결정에 coal `+1/+3/+1`을 추가한다.
8. 각 결정을 하나씩 완료해 최종 합계와 기존 보상을 검증한다.
9. 저장·불러오기와 로그 회귀를 확인한다.
10. 멀티플레이 호환성을 주장할 경우 체크섬과 동기화를 별도로 검증한다.

target 정렬과 신규 밸런스를 한 번에 적용하더라도 diff와 변경 기록에서는 두 성격을 구분한다.

## 11. 검증 기준

### 11.1 정적 검사

- [ ] production diff가 위 4개 파일로 제한된다.
- [ ] 평안·함경·강원의 `resources` 블록이 각각 하나다.
- [ ] 시작 coal은 `5 + 4 + 1 = 10`이다.
- [ ] 시작 chromium은 함경 1뿐이다.
- [ ] 기존 aluminium, steel, tungsten 값이 그대로다.
- [ ] decision 증분은 `1 + 3 + 1 = 5`다.
- [ ] `days`가 추가되지 않았다.
- [ ] 세 결정의 `fire_only_once`, 비용, 기간, 조건, 기존 보상이 보존됐다.
- [ ] 중점 ID, decision ID, state ID, localisation key가 바뀌지 않았다.
- [ ] 괄호, 블록 위치, 파일 인코딩과 줄바꿈에 우발 변경이 없다.

### 11.2 신규 게임 검사

- [ ] 런처가 저장소의 의도한 로컬 모드 복사본을 로드한다.
- [ ] 정확한 1.19.2 빌드와 DLC·의존 모드·로드 순서를 기록한다.
- [ ] 평안 coal 5가 표시된다.
- [ ] 함경 coal 4와 chromium 1이 표시된다.
- [ ] 강원 coal 1이 표시된다.
- [ ] 다른 한국 state의 시작 coal은 0이다.
- [ ] 시작 총량이 coal 10, chromium 1이다.
- [ ] 기존 공장, 건물, 자원, 소유권과 코어가 유지된다.

### 11.3 결정 보상 검사

- [ ] 결정 전 coal 총량은 10이다.
- [ ] 평안 개발 완료 시 state 527만 +1 된다.
- [ ] 강원 개발 완료 시 state 1029만 +3 된다.
- [ ] 전라 개발 완료 시 state 1082만 +1 된다.
- [ ] 세 결정 완료 후 coal 총량은 15다.
- [ ] chromium은 1에서 증가하지 않는다.
- [ ] 각 결정의 도시화·건물 슬롯·승점 보상도 정상 적용된다.
- [ ] 같은 결정 또는 같은 자원 보상이 반복 적용되지 않는다.
- [ ] 통제하지 않는 state의 결정은 시작할 수 없다.

### 11.4 로그·경제·저장 검사

- [ ] 수정 전후 `error.log`를 비교해 새 parser, scope, resource, state 오류가 없다.
- [ ] 메인 메뉴뿐 아니라 한국으로 새 게임에 진입해 unpause한다.
- [ ] 에너지 공급, 무역, 민간공장 사용량과 성장 구간을 관찰한다.
- [ ] 시작 coal 10이 산업 에너지 제약을 사실상 제거하는지 확인한다.
- [ ] 새 저장 → 진행 → 저장 → 재불러오기를 통과한다.
- [ ] 기존 저장 호환성을 주장하려면 대표 pre-change 저장으로 별도 왕복 검증한다.
- [ ] 멀티플레이 호환성을 주장할 경우 동일 playset의 체크섬과 OOS 여부를 확인한다.

현재 문서 작성 단계에서는 런타임 검사를 실행하지 않았다. 정적 state history 변경이 기존 저장에 자동 반영된다고 가정하지 않는다.

## 12. 대안안

### A. 엄격 고증형

- 시작: 함경 coal 4만 target 정렬
- chromium: 시작 0, 별도 탐사 후 +1
- 다른 석탄: 개발을 통해 총 10 안팎까지 추가

1936년의 실제 가동 생산 능력을 가장 보수적으로 본다.

### B. 풍부한 석탄형

- 시작 15: 평안 6, 함경 4, 강원 3, 경상 1, 전라 1
- 개발 후 20: 강원 +4, 함경 +1
- 함경 chromium 1

사용자가 처음 요청한 “석탄을 좀 많이”라는 체감은 가장 강하지만, 1.19.2 에너지 체계에서는 강한 자급 보정이다. 멀티플레이 기본값이나 역사적 생산량의 직환산으로 소개하지 않는다.

### C. 남한 한정 시작형

- 시작: 강원 coal 1
- 개발: 강원 +3, 전라 +1
- 개발 후 합계: coal 5
- chromium: 0

북부를 보유하지 않는 시나리오에서는 평안·함경 자원을 사용할 수 없어야 한다. 남한에 chromium을 주는 경우에는 고증값이 아니라 북부 상실 보정임을 명시한다.

### D. 정적 자원만 적용

- 시작 coal 10, 함경 chromium 1만 적용
- 개발 후 `+5`는 생략
- `common/decisions/KOR_decision.txt`는 변경하지 않음

결정 밸런스를 건드리지 않는 가장 작은 구현이지만, 단계적 개발 체감은 사라진다.

## 13. 되돌리기 계획

전체 저장소를 초기화하지 않고 이번 작업에서 추가한 줄만 역패치한다.

1. 평안에서 `coal=5.000`만 제거한다.
2. 함경에서 `coal=4.000`, `chromium=1.000`만 제거한다.
3. 강원에서 `coal=1.000`만 제거한다.
4. 세 결정에서 각각 추가한 `add_resource` 블록만 제거한다.
5. 기존 사용자 변경, 기존 자원과 기존 결정 보상은 그대로 둔다.
6. 역패치 후 정적 검사와 새 게임 확인을 다시 수행한다.

`git reset --hard`, `git clean`, 강제 체크아웃처럼 다른 변경까지 제거할 수 있는 명령은 사용하지 않는다.

## 14. 남은 위험

- 실제 런처가 현재 저장소 복사본을 로드하는지는 구현 시 다시 확인해야 한다.
- 시작 coal 10의 실제 체감은 인프라·무역·기술을 포함한 런타임 검증 전까지 확정할 수 없다.
- 기존 KOR 개발 결정은 `remove_effect` 방식을 사용하므로, 실제 완료·취소 경로는 target 런타임에서 확인해야 한다.
- 기존 저장의 정적 자원 반영과 이미 완료한 결정의 소급 적용은 검증되지 않았다.
- DLC, Korean Language 의존성, 호환성 서브모드, 멀티플레이 경로는 별도 검증이 필요하다.
- 크롬 광상의 존재는 근거가 있지만 1936년 상업 생산 규모는 확인되지 않았다.

## 15. 출처와 근거 파일

### 역사 자료

- [USGS Bulletin 1041-A/B — Coalfields of the Republic of Korea](https://pubs.usgs.gov/publication/b1041AB)
- [USGS Bulletin 1041-A/B PDF](https://pubs.usgs.gov/bul/1041a-b/report.pdf)
- [식민지기 조선 석탄산업 연구](https://doi.org/10.25024/review.2011.14.4.003)
- [남북 석탄 산지·탄질 교차검증 자료](https://www.jiia.or.jp/eng/upload/eng/JapanReview_Vol2_No2_03_Kimura.pdf)
- [함경북도 부령군 크롬철광 1940년 자료](https://www.jstage.jst.go.jp/article/denka/8/11/8_263/_article/-char/ja)
- [산업통상자원부 광산·광물 자료](https://branch.motie.go.kr/data/aboutMine13.do)
- [Paradox — Coal and Energy 개발자 설명](https://store.steampowered.com/news/app/394360/view/517465051240595900)
- [HOI4 1.19.2 패치 공지](https://steamcommunity.com/games/394360/announcements/detail/717908846920599779)

### 현재 프로젝트

- `history/states/527-North Korea.txt`
- `history/states/1028 - Hamgyong.txt`
- `history/states/1029 - Gangwon.txt`
- `history/states/1082 - Jeolla.txt`
- `common/decisions/KOR_decision.txt:1159-1366`
- `common/national_focus/korea.txt:460-516`
- `localisation/korean/replace/HoK_state_name_l_korean.yml:4-12`
- `descriptor.mod:9-12`

### 설치된 target 1.19.2

- `history/states/1028 - Hamgyong.txt:7-10`
- `common/resources/00_resources.txt:33-42`
- `common/defines/00_defines.lua:624-628`
- `documentation/effects_documentation.md:2056-2070`
- `common/national_focus/belgium.txt:7543-7553`
- `common/decisions/JAP.txt:4515-4570`

## 16. 구현 완료 기록 양식

실제 구현 시 아래를 복사해 결과를 기록한다.

```md
### 작업 기준

- 브랜치:
- 커밋:
- 작업 전 dirty 상태:
- 대상 HOI4 버전/빌드:
- DLC:
- 플레이세트:
- 의존 모드와 순서:
- 실제 로드된 모드 경로:

### 실제 변경

| 파일 | 변경 전 | 변경 후 | 변경 이유 |
|---|---|---|---|
|  |  |  |  |

### 검증 결과

- 정적 검사:
- 신규 게임 시작 자원:
- 결정 전 총량:
- 결정 후 총량:
- 저장/불러오기:
- 로그 비교:
- 멀티플레이:
- 미검증 항목:

### 되돌리기 정보

- 역패치 대상:
- 되돌리기 확인 결과:
- 기존 사용자 변경 보존 여부:
```

## 17. 승인 문구

구현 승인 시 요구사항은 다음처럼 고정한다.

> 한반도 전체 KOR 기준 시작 coal 10, Hamgyong chromium 1을 적용한다. Hamgyong coal 4는 HOI4 1.19.2 target 정렬로, 나머지는 고증 자료에 근거한 의도적 밸런스 변경으로 구분한다. 기존 평안·강원·전라 개발 결정을 통해 coal을 각각 +1, +3, +1 추가하고, 개발 후 총량은 15로 제한한다. 새 자원·state·중점·결정 ID는 만들지 않는다.
