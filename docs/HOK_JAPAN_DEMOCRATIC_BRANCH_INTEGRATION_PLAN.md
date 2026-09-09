# HoK 일본 민주주의 전체 분기 1.19.2 통합 설계

> 문서 상태: **RUNTIME_CONFIRMED_HIDE — D-JAP-15 절대좌표 fallback 로드 + D-JAP-16/17 HoK 완료 후 HIDE 화면 확인; SHOW·역방향 잠금·save/load 미검증**
>
> 작성일: `2026-09-09`
>
> 목표 게임: HOI4 `Operation Postern v1.19.2.0.a729 (d245)`
>
> 저장소 기준선: branch `main`, HEAD `887930f6e88c80568d62dab9cfbe1ba8a498a252`
>
> 목표 결과: **1.19.2 바닐라 일본 중점 정의 보존 + 화면 옆의 시각적으로 독립된 HoK 민주주의 전체 분기 + HoK 확정 뒤 양립하지 않는 바닐라 정치 계통 정리**

이 문서는 원작 Hearts of Korea의 일본 민주주의 분기를 HOI4 1.19.2 일본 중점 화면에 복구하기 위한 설계, 범위, 위험과 검증 계약을 기록한다. 2026-09-09 사용자가 전체 구현과 후속 배치 변경을 승인해 production 소스에 적용했으며, 실제 변경과 정적 검사 결과는 별도 구현 기록에 남긴다. 바닐라 일반 focus를 HoK shared root의 `relative_position_id`로 사용한 배치안은 20:08 런타임에서 엔진 오류로 반증돼, root만 절대 `(10,0)`으로 두는 fallback으로 교정했다. 앞선 화면에서는 정상 공통 SEA 산업·군부 계통만 사라지고, 숨겨야 할 NCNS 정치 계통의 큰 하위 묶음은 남는 역전 현상도 확인됐다. 재감사 결과 자체 `allow_branch`를 가진 자식은 부모의 숨김 상태를 상속하지 않는 1.19.2 규칙이 원인이었다. 따라서 잘못 적용한 SEA 산업·군부 guard는 롤백하고, NCNS 정치 계통 안의 독립 `allow_branch` 경계 9개에 HoK 선택 조건을 전파하는 교정안을 적용했다. 20:18 fresh 실행과 사용자 제공 완료 화면에서 절대좌표 fallback의 로드, HoK 분기와 정상 SEA 계통의 유지, NCNS 정치 계통의 HIDE를 확인했다. `SHOW`, 역방향 잠금과 save/load는 아직 검증하지 않았다.

관련 문서:

- [중국·일본 1.19.2 바닐라 정렬 정책](CHINA_JAPAN_VANILLA_ALIGNMENT_POLICY.md)
- [수정 후 검증 점검표](VALIDATION_CHECKLIST.md)
- [환경 기준선](baselines/2026-08-31-environment-baseline.md)
- [1.19.2 dual localisation 계약](incidents/2026-09-01-localisation-contract.md)
- [중국·만주·일본 1.19.2 바닐라 정렬 구현 기록](incidents/2026-09-01-china-japan-vanilla-alignment-implementation.md)
- [일본 민주주의 전체 분기 구현 기록](incidents/2026-09-09-japan-democratic-focus-integration-implementation.md)

## 1. 확정 요구사항

사용자의 요구를 다음과 같이 고정한다.

1. 설치된 1.19.2의 `japan_wtt_focus`와 그 안의 바닐라 중점 전체를 유지한다.
2. 원작 HoK의 구형 `common/national_focus/japan.txt` 전체를 되살려 1.19.2 트리를 대체하지 않는다.
3. 원작 HoK 일본 민주주의 분기 전체와 그 실행에 필요한 종속성만 선별 이식한다.
4. 새 분기는 기존 일본 중점 화면의 옆 공간에 별도 구역으로 배치한다.
5. 새 분기는 화면상 기존 바닐라 가지와 섞이지 않고 독립된 묶음으로 식별돼야 한다.
6. 바닐라·HoK의 기존 ID와 충돌하지 않는 새 namespace를 사용한다.
7. 바닐라 설치 폴더와 원본 Workshop 폴더는 수정하지 않는다.
8. 한국 지도, 한국 9도, 쓰시마, 독립 한국 lifecycle과 기존 KOR bridge를 회귀시키지 않는다.
9. `HOK_JAP_strengthen_civilian_government` 완료 뒤 HoK 민주 루트와 양립하지 않는 바닐라 정치 계통은 `HIDE` 규칙에서 화면에서 제거하고 진행도 차단한다. SEA 산업·군부 공통 계통은 계속 표시·사용하며, 모든 정의는 보존한다.

여기서 “독립 중점트리”는 사용자 경험과 화면 배치를 뜻한다. 엔진 수준에서 일본이 동시에 두 개의 일반 `focus_tree`를 사용하는 설계를 뜻하지 않는다.

## 2. 목표 구조와 엔진 제약

목표 화면 구조는 다음과 같다.

```text
[HoK 민주주의 전체 구역]          [1.19.2 바닐라 일본 전체 중점 구역]
 문민정부 강화부터 독립 전개                  그대로 유지
```

HoK 경로가 확정된 뒤 `HIDE` 규칙에서의 목표 구조는 다음과 같다.

```text
[HoK 민주주의 전체 구역]          [양립 가능한 바닐라 구역]
 문민정부 강화부터 독립 전개       경쟁 정치 계통만 숨기고 공통 산업·군부는 유지
```

여기서 “바닐라 전체 중점 유지”는 448개 정의와 비HoK 경로의 기능을 보존한다는 뜻이다. 모든 정의를 HoK 경로에서도 항상 표시하거나 선택 가능하게 둔다는 뜻은 아니다.

정적 소스에서 확인된 1.19.2 구조는 다음과 같다.

- 설치본 `common/national_focus/japan.txt`에는 `focus_tree = { id = japan_wtt_focus ... }` 하나가 일본용 트리로 등록돼 있다.
- 설치본과 바닐라 예제에서는 별도의 `focus_tree`를 기존 트리에 자동 누적하는 패턴을 찾지 못했고, 국가별 tree 선택 후보로 쓰는 구조만 확인했다. 1.19.2 런타임 negative control은 아직 수행하지 않았다.
- 바닐라가 외부 분기를 재사용할 때는 대상 트리 안에 `shared_focus = <root-id>`를 명시하고, 정의는 별도 파일의 `shared_focus = { ... }`로 분리한다.
- 현행 일본 트리에는 HoK 분기를 받아들이는 `shared_focus` 참조가 없다.

따라서 채택해 구현한 구조는 다음과 같다.

```text
V_TARGET 1.19.2 japan_wtt_focus 전체
+ host tree 안의 최소 HoK shared-focus 참조
+ 별도 파일에 둔 HoK 민주주의 shared-focus 정의
+ 1.19.2에 맞춘 최소 event/idea/character/localisation/GFX 종속성
= 목표 일본 중점 화면
```

이 구조의 소스 연결과 참조 무결성은 정적으로 확인했고, 사용자 제공 화면으로 shared 분기가 실제 일본 트리에 로드되는 것도 확인했다. HoK root를 바닐라 일반 focus에 상대 배치하는 최종안도 정적으로 적용했지만, 이 교차 유형 상대참조와 전체 분기 진행은 런타임 `CONFIRMED`가 아니다.

### 2.1 채택 구현

| 항목 | 설계 |
|---|---|
| host | 설치된 정확한 1.19.2 `japan.txt`를 기준으로 만든 target-derived 파일 |
| HoK 분기 정의 | 별도 `common/national_focus/HOK_JAP_democratic_shared.txt`에 구현 |
| host 변경 | HoK shared root를 불러오는 최소 참조와 필요한 충돌 방지 조건만 허용 |
| 표시 | 바닐라 가지와 떨어진 좌측 별도 구역 |
| `replace_path` | 사용하지 않음 |
| 바닐라 설치본 | 수정하지 않음 |
| 원작 Workshop 복사본 | 수정하지 않음 |

별도 파일로 분기 본문을 격리할 수는 있지만, host tree에 참조를 넣기 위해 mod가 target-derived `japan.txt`를 소유하게 되는 위험은 남는다. 이후 HOI4 업데이트마다 바닐라 일본 트리와 다시 대조해야 한다.

### 2.2 기각하는 방식

| 방식 | 기각 이유 |
|---|---|
| JAP용 두 번째 일반 `focus_tree` 추가 | 기존 1.19.2 트리와 자동 병합된다는 근거가 없고 선택 경쟁·대체 위험이 있다. WP1 negative control 전에도 안전한 구현 후보로 채택하지 않는다. |
| 같은 `japan_wtt_focus` ID의 부분 정의를 별도 파일에 중복 | 병합 계약이 입증되지 않았고 중복 정의·무음 override 위험이 있다. |
| 원작 128-focus `japan.txt` 전체 복원 | 1.19.2의 448-focus target tree와 AI/event/decision 계약을 다시 구형 상태로 되돌린다. |
| `replace_path`로 바닐라 중점 폴더 차단 | 전역 범위가 너무 크며 관련 없는 바닐라 중점을 내릴 수 있다. |
| decision으로 별도 JAP `focus_tree`에 전환 | 전환 순간 바닐라 일본 트리가 사라져 사용자의 목표와 다르다. |

## 3. 기존 정책과의 관계

구현 전 production 상태는 [중국·일본 바닐라 정렬 정책](CHINA_JAPAN_VANILLA_ALIGNMENT_POLICY.md)의 결정에 따라 구형 일본 focus snapshot을 제거하고 설치된 1.19.2 일본 트리를 직접 상속했다. 현재는 정확한 target 1.19.2 일본 트리를 host 기준본으로 소유하고 승인된 HoK shared-focus delta만 연결한다.

이번 후속 구현은 다음 범위에서만 기존 제거 결정을 supersede한다.

- HoK 일본 민주주의 focus
- 해당 focus가 직접 또는 전이적으로 필요로 하는 event, news event, idea, character, localisation, GFX와 제한된 decision
- 분기를 1.19.2 host에 표시하기 위한 최소 통합부

다음은 자동 복구 대상이 아니다.

- 구형 HoK 일본 전체 중점 트리
- 일본 AI 시작 부대 buff
- 구형 일본 전용 AI 전략 전체
- 일본 구형 MIO
- 구형 평화회의 AI
- 1939년 대한전쟁 bridge 중 현재 별도로 유지되는 범위를 넘어선 시스템
- 원작 일본 state/OOB/character 전체 snapshot
- 원작 Workshop ID `2898629778`을 upload identity로 사용하는 설정

실제 supersede 범위와 target 대비 delta는 [2026-09-09 구현 기록](incidents/2026-09-09-japan-democratic-focus-integration-implementation.md)에 고정한다.

## 4. 기준선과 출처

| 구분 | 기준 |
|---|---|
| target 게임 | `<HOI4_INSTALL>` |
| target 버전 | `Operation Postern v1.19.2.0.a729 (d245)` |
| production 저장소 | `<PROJECT>` |
| launcher 개발 모드 | `<HOI4_USER_DATA>/mod/hearts of korea.mod` |
| launcher가 가리키는 경로 | `<PROJECT>` |
| 원작 읽기 참조 | `<STEAM_WORKSHOP>/2898629778` |
| successor ID | `3793992662`; 이번 문서 작업에서 외부 변경 없음 |
| 선언 의존성 | `Korean Language` |
| 현재 Git 시작 상태 | branch `main`, HEAD `887930f6e88c80568d62dab9cfbe1ba8a498a252`; 기존 문서 변경 2개와 본 설계 문서 untracked 상태 보존 |

원작의 장기 provenance는 [환경 기준선](baselines/2026-08-31-environment-baseline.md)에 기록된 ZIP과 `SHA256SUMS.tsv`가 우선한다. 구현 시작 전에는 그 archive의 실제 접근성과 대상 파일 hash를 다시 확인해야 한다. Steam Workshop live 폴더는 읽기 비교용이며 불변 기준본으로 간주하지 않는다.

target `japan.txt`의 실제 `focus = { ... id = JAP_* }` 정의는 448개다. 단순히 `id = JAP_*` 행을 세면 UI용 `jap_imperial_influence_inlay_window`까지 포함돼 449가 되므로, 검증에서는 focus block에서 추출한 ID 집합을 기준으로 삼는다.

설치된 target `<HOI4_INSTALL>/common/national_focus/japan.txt`의 2026-09-09 SHA-256은 `BF5EF4B6A17E70E4AD83030A0AAC4DE72105CB8803CA6F93A9BF3FCEF8662623`이다. 향후 host snapshot을 만들 때는 이 hash와 정확히 대응하는 파일만 기준으로 삼는다.

이번 설계 조사에서 읽은 Workshop live 파일의 SHA-256은 다음과 같다.

| 원작 파일 | 2026-09-09 읽기 hash |
|---|---|
| `common/national_focus/japan.txt` | `61726A271861E243FA100F071EA5657E6D0CA70513F8D4D88EBCE369F1ABCCA5` |
| `events/japan_HoK.txt` | `A9A3D9EACB87CC865421C70D465E4FD2BC1785C333F4A14C4E2D55A825CDA4EC` |
| `common/ideas/democratic_japan.txt` | `0E1B313A43E04A2CCAC9DFABB6B9F6824CED15AB61B467C80A19E7D4E1B3B145` |
| `localisation/english/replace/republican_japan_focus_l_english.yml` | `0136E1C5CDF22654C4B20EA27B26B1BA140EC3FAAA1BA66D73F04E0893C541CE` |

## 5. 이식 범위

### 5.1 민주주의 직결 분기 32개

원작 `common/national_focus/japan.txt:3568-4875`의 다음 32개 중점을 core scope로 삼는다.

원작 root의 `allow_branch`는 `Waking the Tiger` 보유를 요구한다. 첫 구현의 지원 기준은 WTT와 `No Compromise, No Surrender`가 모두 활성화된 정확한 1.19.2 구성으로 고정했다. 어느 하나라도 없는 구성은 별도 설계와 검증 전 지원 범위 밖이다.

#### 입구·연구·산업

```text
JAP_strengthen_civilian_government
├─ JAP_ally_with_the_zaibatsus
└─ JAP_research_spending
   └─ JAP_returning_home_SMCR_elite
      └─ JAP_invest_nigo_project
```

`JAP_returning_home_SMCR_elite`는 원작에서 `ally_with_the_zaibatsus`와 `research_spending`을 모두 요구한다.

#### 민주화와 내전

```text
JAP_strengthen_civilian_government
└─ JAP_oppose_peace_preservation_law
   ├─ JAP_memories_of_taisho_democracy
   └─ JAP_purge_the_militarists
      └─ JAP_pre_emptive_coup
         ├─ JAP_the_showa_constitution
         └─ JAP_proclaim_the_republic
```

`JAP_pre_emptive_coup`은 앞의 두 병렬 중점을 모두 요구한다. `JAP_the_showa_constitution`과 `JAP_proclaim_the_republic`은 상호배타다.

#### 문민 군제

```text
쇼와 헌법 또는 공화정 선포
└─ JAP_strength_civilian_control
   └─ JAP_new_officers
      └─ JAP_joint_staff_office
         └─ JAP_citizen_in_uniform
```

#### 외교·안보

```text
쇼와 헌법 또는 공화정 선포
└─ JAP_review_foreign_policy
   ├─ JAP_datsuonyua
   │  └─ JAP_go_with_korea
   │     └─ JAP_rok_jpn_free_trade_agreement
   └─ JAP_rebuild_anglo_japanese_alliance

JAP_datsuonyua 또는 JAP_rebuild_anglo_japanese_alliance
└─ JAP_pacific_guardian
   └─ JAP_anti_communist_bulwark
      ├─ JAP_liberation_of_manchuria
      └─ JAP_demand_sagaren
```

`JAP_datsuonyua`와 `JAP_rebuild_anglo_japanese_alliance`는 상호배타다. 원작의 `JAP_go_with_korea`는 두 노선 중 어느 쪽을 택해도 진입할 수 있다.

#### 정부·지방·식민지

```text
쇼와 헌법 또는 공화정 선포
├─ JAP_rebuild_the_goverment
└─ JAP_abolition_peace_preservation_law
   ├─ JAP_expansion_of_local_autonomy
   └─ JAP_disband_takumusho
      ├─ JAP_free_election_in_taiwan
      │  └─ JAP_develop_taiwan
      └─ JAP_integrate_nanyo_gunto
         └─ JAP_develop_nanyo_gunto
```

원작 ID의 `goverment` 오탈자는 provenance 기록에 남긴다. 새 ID에서는 의미가 바뀌지 않는 범위에서 `government` 철자를 사용할 수 있지만, 실제 migration table 확정 전에는 변경하지 않는다.

### 5.2 민주·공산 공유 본토경제 8개

원작 `common/national_focus/japan.txt:4877-5399`의 다음 8개는 민주 루트와 공산 루트가 공유한다.

```text
JAP_develop_home_island
├─ JAP_making_use_of_our_islands
│  └─ JAP_karafuto_oil_field
├─ JAP_home_island_agriculture
│  └─ JAP_development_tohoku_region
│     ├─ JAP_modernize_tatara_ironworks
│     └─ JAP_tohoku_dairy_farming
└─ JAP_sinkansen
```

사용자가 “원작 HoK 민주주의 전체”를 요청했으므로 민주 경로에서 접근 가능한 이 8개를 **포함**해 총 40개로 확정했다. 원작의 `JAP_develop_home_island`는 공산 root와도 연결됐지만 이번 구현에서는 HoK 민주 root만 prerequisite로 요구한다.

채택한 방식은 1번이다. 1.19.2의 대응 공산 경로에는 연결하지 않았고 공유 본토경제 8개를 별도 파일 안의 민주 모듈 자식으로 유지했다.

아무 결정 없이 구형 공산 focus ID를 그대로 참조하지 않는다.

이 8개의 일부 보상은 원작에서도 WTT 보유 여부에 따라 갈린다. D-JAP-05에서 WTT 활성 구성만 지원하더라도 각 조건부 효과를 target 1.19.2 의미와 비교하고, 도달하지 않는 WTT-off 블록을 무심코 보존하거나 삭제하지 않는다.

## 6. ID와 namespace 정책

1. 원작 ID는 출처와 migration ledger에 보존한다.
2. 새 focus 정의는 원칙적으로 앞의 `JAP_`를 `HOK_JAP_`로 바꾼 고유 ID를 사용한다.
3. 화면 표시명과 원작 서사는 유지하되 localisation key도 `HOK_JAP_*`로 분리한다.
4. 바닐라 ID를 같은 이름으로 다시 정의하지 않는다.
5. 원작 event namespace는 1.19.2에서 대소문자와 등록 계약을 검증한 뒤 유지 또는 일괄 migration한다.
6. idea, character, decision, category와 flag도 전역 충돌 검색 뒤 `REUSE_TARGET`, `PORT_UNCHANGED`, `PORT_RENAMED`, `ADAPT`, `OMIT`, `DEFER` 중 하나로 분류한다.

### 6.1 이미 확인된 충돌

| ID | target 상태 | 계획 |
|---|---|---|
| `JAP_strengthen_civilian_government` focus | 1.19.2 `japan.txt:1278`에 존재 | 새 focus는 `HOK_JAP_strengthen_civilian_government`로 구현 |
| `JAP_ally_with_the_zaibatsus` focus | 1.19.2 `japan.txt:2867`에 존재 | 새 focus ID 사용 |
| `JAP_research_spending` focus | 1.19.2 `japan.txt:3001`에 존재 | 새 focus ID 사용 |
| `JAP_pre_emptive_coup` focus | 1.19.2 `japan.txt:3033`에 존재 | 새 focus ID 사용 |
| `JAP_purge_the_militarists` focus | 1.19.2 `japan.txt:3126`에 존재 | 새 focus ID 사용 |
| `JAP_the_showa_constitution` focus | 1.19.2 `japan.txt:3171`에 존재 | 새 focus ID 사용 |
| `JAP_pacific_guardian` focus | 1.19.2 `japan.txt:3322`에 존재 | 새 focus ID 사용 |
| `JAP_anti_communist_bulwark` focus | 1.19.2 `japan.txt:3362`에 존재 | 새 focus ID 사용 |
| `JAP_strengthen_civilian_government` idea | 1.19.2에 이미 존재 | target idea 재사용 여부를 효과 비교 후 결정 |
| `JAP_tetsu_katayama` character | 1.19.2에 존재 | target character 재사용 우선 |
| `JAP_tomoyuki_yamashita` character | 1.19.2에 존재 | target character 재사용 우선 |
| `JAP_tamon_yamaguchi` character | 1.19.2에 존재 | target character 재사용 우선 |
| `JAP_kijuro_shidehara` character | 1.19.2에 존재 | target character와 advisor token 재사용 우선 |

현재 직접 확인된 focus ID 충돌은 최소 8개다. 충돌이 확인된 항목만 이름을 바꾸고 나머지 원작 focus ID를 유지하는 혼합 정책은 사용하지 않는다. focus 완료 조건과 이벤트 호출을 추적하기 어렵고 향후 target 추가 ID와 다시 충돌할 수 있기 때문이다. D-JAP-01에서 최종 이식 대상으로 확정된 focus 전부를 새 namespace로 옮기고 prerequisite, mutually-exclusive, `has_completed_focus`, AI 조건, 음악 조건과 scripted reference를 migration ledger로 함께 바꾼다.

### 6.2 이름 충돌과 별개의 의미 충돌

- target의 기존 `JAP_strengthen_civilian_government`는 `No Compromise, No Surrender`가 없을 때 열리는 구 WTT 분기 안에 있다. NCNS 활성 구성에서는 target의 새 정치 분기와 `JAP_revoke_the_peace_preservation_law`가 별도로 존재한다.
- 따라서 HoK의 같은 이름 중점은 target 정의를 재사용하지 않는다. 이름이 같아도 prerequisite, DLC gate, 후속 중점과 효과 계약이 다르다.
- 원작 HoK root의 상호배타 대상에는 `JAP_purge_the_kodoha_faction`이 들어가지만 target의 구 WTT 경로는 이를 `JAP_sea_purge_the_kodoha_faction`으로 바꿨다. NCNS 활성 시에는 해당 구 branch 자체가 숨겨진다.
- 새 HoK root는 구 WTT 민주 분기와 NCNS 정치 분기 양쪽을 모두 상대로 현재 정치 root 잠금을 새로 설계해야 한다. 특정 DLC 구성에서 바닐라 분기가 숨겨진다는 이유로 ID 충돌이 사라지거나 양쪽 경로의 동시 진행이 자동 차단되는 것은 아니다.

## 7. 직접·전이 종속성 disposition

### 7.1 이벤트

원작 `events/japan_HoK.txt:1-565`에는 `jap_hok_events.1`부터 `.23`까지의 연쇄가 있다.

| 진입점 | 주요 기능 | 초기 disposition |
|---|---|---|
| `.1 → .2` | 치안유지법 반대 시위와 후속 처리 | `ADAPT` |
| `.3 → .4` | 군국주의자 추방과 만주 측 반응 | `ADAPT` |
| `.5 → .6/.7→.8/.9→.10/.21` | 민주 내전, 만주·몽강·중국 영향, 여순·동허베이 반환 통지와 전후 처리 | `ADAPT_HIGH_RISK` |
| `.13 → .14` | 한일 자유무역협정 | `ADAPT` |
| `.15 → .16/.17` | 타이완 자유선거 결과 | `ADAPT_HIGH_RISK` |
| `.18 → .19/.20` | 북사할린 요구 결과 | `ADAPT` |
| `.22 → .12` | 공화국 명칭과 천황가 처리 | `ADAPT` |
| `.23` | 한국 동맹 관련 응답 | `ADAPT` |
| `.11` | 원작 파일에서 호출자가 확인되지 않은 내전 종료 이벤트 | `DEFER_UNTIL_CALLER_FOUND` |

원작은 `add_namespace = JAP_HoK_events`를 선언하면서 실제 ID와 호출은 `jap_hok_events.*`를 사용한다. 1.19.2의 대소문자 처리와 event namespace 등록 결과를 런타임에서 검증하기 전에는 그대로 복사하지 않는다.

현재 저장소의 `events/NewsEvents_KOR.txt:968-1110`에는 `newsj.1`부터 `.4`까지가 남아 있다. 이를 새로 중복 정의하지 않고, 내용·GFX·호출 범위와 localisation을 감사한 뒤 재사용 또는 새 namespace migration을 결정한다.

### 7.2 국민정신

원작 `common/ideas/democratic_japan.txt`에는 다음 7개가 있다.

- `JAP_returning_home_SMCR_elite`
- `JAP_democratic_hirohito_hok`
- `JAP_strength_civilian_control`
- `JAP_joint_staff_office`
- `JAP_citizen_in_uniform`
- `JAP_jpn_rok_free_trade_agreement`
- `KOR_rok_jpn_free_trade_agreement`

전체 파일을 복원하지 않고 각 idea를 target 1.19.2 modifier schema와 비교한다. 동일 의미의 target idea가 있으면 `REUSE_TARGET`, 없으면 HoK namespace로 `PORT_RENAMED`한다. 일본과 한국 양쪽에 적용되는 자유무역 국민정신은 KOR 밸런스 변경으로도 분류해 별도 회귀 검사를 요구한다.

분기 효과와 이벤트가 외부에서 재사용하는 다음 idea ID도 disposition ledger에 포함한다. 이들은 새로 복사할 목록이 아니라 target에서 같은 의미로 해소되는지 확인할 목록이다.

- `state_shintoism`
- `JAP_zaibatsus`, `JAP_nationalize_the_zaibatsus`, `JAP_zaibatsus_empowered`
- `JAP_militarism`, `MAN_militarism`, `MAN_kwantung_veto`
- `MAN_low_legitimacy_1`부터 `MAN_low_legitimacy_5`
- `FRA_strengthen_government_support_focus`

### 7.3 인물

target에 이미 있는 `JAP_tetsu_katayama`, `JAP_tomoyuki_yamashita`, `JAP_tamon_yamaguchi`, `JAP_kijuro_shidehara`는 target 정의 재사용을 우선한다. 원작 전용 인물은 전체 `common/characters/JAP.txt` snapshot을 복원하지 않고 additive 파일에 필요한 정의만 선별한다.

검토 대상은 다음과 같다.

- `JAP_japanese_national_liberation_committee`
- `JAP_tatsuji_fuse`
- `JAP_tadamichi_kuribayashi`
- `JAP_sigesaburo_miyazaki`
- `JAP_shin_yoshida`
- `JAP_mitsumasa_yonai_navy`
- `JAP_masatomi_kimura`
- `JAP_renya_mutaguchi`
- `JAP_random_industry_minister_1`: 본토경제 계열이 표시하는 원작 산업 장관

원작에서는 일부 인물 모집이 `history/countries/JAP - Japan.txt`에 의존한다. 현행 target-derived 일본 country history 전체를 다시 덮지 않고, focus 효과나 최소 additive lifecycle을 통해 필요한 인물만 안전하게 모집하는 방법을 설계해야 한다.

`JAP_mitsumasa_yonai_navy`는 target의 `JAP_mitsumasa_yonai`와 ID는 다르지만 같은 인물을 표현한다. target은 NCNS 여부에 따른 instance와 해군 역할까지 포함하므로, 원작 전용 character를 별도로 추가하면 같은 인물이 중복될 수 있다. target 인물의 현행 역할을 재사용·노출할지, HoK 전용 instance가 정말 필요한지 D-JAP-13에서 결정한다.

`JAP_random_industry_minister_1`은 원작 character·focus·history에는 있으나 원작 전체 검색에서 이름 localisation을 찾지 못했다. raw key 또는 빈 이름 표시 여부를 확인하기 전에는 그대로 노출하지 않는다.

원작이 직접 소비하는 `JAP_japanese_national_liberation_committee_trait`와 `JAP_champion`은 현행 `<PROJECT>/common/country_leader/00_hok_traits.txt`에 남아 있다. 두 정의를 `REUSE_EXISTING_REPO`로 확정했으며 새 파일에는 중복 정의하지 않았다.

또한 `jap_hok_events.3`는 특정 명단이 아니라 `JAP_samurai_lineage` 특성을 가진 일본 육군 지휘관 전체를 MAN으로 이전한다. 원작 캐릭터 파일의 해당 특성 occurrence는 8개였지만 1.19.2 target 파일에서는 15개다. 효과를 그대로 옮기면 숙청·이전 대상이 확대되므로 원작 대상 allowlist를 만들지, 현행 roster 전체를 대상으로 삼을지 명시적으로 결정해야 한다.

### 7.4 결정과 외교 효과

- `JAP_pacific_guardian`이 여는 결정은 원작 `common/decisions/JAP.txt` 전체를 복원하지 않고 관련 category와 decision만 target-derived로 이식한다.
- 원작 `common/decisions/JAP.txt:628-650`에는 `JAP_strengthen_civilian_government` 등 구 focus ID를 검사하는 조건이 있다. 필요한 결정만 별도 additive 파일로 옮기고 새 `HOK_JAP_*` ID로 참조를 갱신한다.
- `JAP_demand_sagaren` 후속 사할린 처리는 원작 JAP HoK decision 전체가 아니라 해당 chain만 선별한다.
- 원작 사할린 결정의 `set_state_name = "Sagaren"`에 대응하는 localisation key는 원작 전체 검색에서 확인되지 않았다. 키를 그대로 이식하지 말고 표시 결과를 먼저 확인한다.
- 한국 동맹과 자유무역은 현행 독립 KOR, 현재 faction 상태와 전쟁 상태를 기준으로 positive·rejection·already-in-faction 경로를 각각 검증한다.
- `MAN`, `MEN`, `CHI`, `PRC`, `KOR`, `SOV`, `ENG`, `HOL`, `INS`, `MAL`, `FRA`, `GUM`, `FSM` scope와 존재 조건을 target 1.19.2에서 다시 확인한다. `HOL/INS/MAL/FRA`는 태평양 수호자 결정을 유지할 때 필요한 범위다.
- 민주 내전 이벤트가 참조하는 `event_target:WTT_current_china_leader`는 target 1.19.2에서 생성 지점, 수명과 해당 이벤트 시점의 존재를 다시 입증한다.
- 원작 타이완 이벤트의 `set_autonomy`에는 다른 원작 호출과 달리 `autonomous_state`라는 매개변수가 한 곳 있다. `autonomy_state`의 오타인지 1.19.2에서 합법인 별도 키인지 target 예제로 검증한다.
- 원작이 호출하는 `generic.2`, `generic.5`, `wtt_japan.1`은 target 이벤트를 `REUSE_TARGET`하고 정의를 복사하지 않는다. 호출 scope와 옵션 결과만 회귀 검사한다.
- `jap_hok_events.6`은 `set_cosmetic_tag = man_restored`를 쓰지만 target 정의는 `MAN_restored`다. 대소문자 계약을 검증하고 명시적으로 올바른 ID로 migration한다.

### 7.5 로컬라이징

원작 `localisation/english/replace/republican_japan_focus_l_english.yml`에는 focus, event, news, idea, character, decision 문자열이 함께 있다. 기존 파일을 `replace` 경로로 통째로 복원하지 않는다.

계획은 현행 [1.19.2 dual localisation 계약](incidents/2026-09-01-localisation-contract.md)을 그대로 따른다.

- 새 HoK ID만 담은 English/Korean 한 쌍의 localisation 파일 사용
- `localisation/english/**/*_l_english.yml`의 `l_english:` 채널과 동일 상대경로의 `localisation/korean/**/*_l_korean.yml` `l_korean:` 채널 유지
- 두 채널 모두 UTF-8 BOM, `KEY:0 "Text"` 형식과 치환 token 보존
- 양 채널의 key set과 표시 문자열 body를 1:1로 유지
- target 문자열을 덮어쓰지 않음
- `Korean Language` 의존 모드가 실제 playset에 로드되는지 런타임 확인
- 원작 문구의 오탈자 수정은 복구와 분리하고 별도 승인 없이는 의미를 바꾸지 않음

### 7.6 GFX와 음원

현재 저장소에는 원작 민주 분기용 focus icon, shine, event picture와 portrait 일부가 남아 있다. 새 binary asset을 만들기 전에 기존 파일과 sprite 정의를 재사용할 수 있는지 확인한다.

- target과 이름이 겹치는 sprite는 중복 정의하지 않는다.
- HoK 전용 sprite는 실제 DDS 경로·casing·frame·shine mask를 확인한다.
- placeholder 이미지는 만들지 않는다.
- 과거 제거된 `Minshu_ikki` 음악 조건의 복구는 민주 분기 자체와 분리된 `DEFER` 항목으로 둔다.

### 7.7 국가·코스메틱·간접 소비자

| 종속성 | 확인된 사용 | 계획 |
|---|---|---|
| `TWN` 국가 태그와 정의 | `jap_hok_events.17`의 타이완 core·영토 이전·자치도 설정 | 현행 저장소의 태그, 국가 정의, history, 색상, 이름풀, 대·중·소 국기를 묶음으로 감사하고 누락 시 타이완 독립 선택지를 차단한다. |
| 공화국 cosmetic 3종 | 공화국 명칭 이벤트의 `JAP_yamato_kyowakoku`, `JAP_daiwa_mingoku`, `JAP_fuso_gasshukoku` | 각 cosmetic 이름과 대·중·소 국기를 함께 확인한다. |
| 세력명 localisation | 원작의 아시아 연합과 대청제국 명칭 | 새 세력 생성 효과를 유지할 때만 필요한 key를 선별한다. |
| 현행 `common/ai_strategy/KOR.txt:196-220` | 일본의 `JAP_strengthen_civilian_government` 완료 시 대일 적대 전략 중단 | HoK focus ID migration 후 의도에 맞는 조건을 별도 검토한다. 현행 바닐라 ID 조건을 무조건 치환하지 않는다. |
| 원작 `common/ai_strategy/JAP_HoK.txt` | 내전 전선, MAN 적대, JAP↔KOR 동맹, SOV/MAN 전쟁 억제 | 첫 구현 범위 밖이다. 제외 상태에서는 원작 AI 행동 parity를 주장하지 않는다. |
| 원작 `music/hok_songs.txt:132-146` | `JAP_proclaim_the_republic` 완료 시 `Minshu_ikki` 가중치 | 음악 복구 승인 시 새 focus ID로 조건도 함께 migration한다. |

`TWN`은 단일 이벤트 ID만 복사해서 성립하지 않는다. `common/country_tags`, `common/countries`, `history/countries`, `common/countries/colors.txt`, `common/names`, 국가명 localisation과 세 크기의 flags가 모두 하나의 기능 단위다. 이 가운데 하나라도 누락되면 “타이완 독립” 선택지는 완료된 것으로 간주하지 않는다.

## 8. 원작 효과 중 고위험 항목

다음은 이름만 옮기는 수준이 아니므로 그대로 복사하지 않는다.

| 효과 | 위험 |
|---|---|
| 민주 내전 | 정권, 전쟁 상대, army/navy 분할, 수도와 시작 states, 생성 부대, MAN/MEN/CHI 연쇄 효과 |
| 쇼와 헌법·공화정 | 지도자 승격, 천황 국민정신, cosmetic tag와 천황가 이벤트 |
| 한국 동맹·자유무역 | 독립 KOR 전제, faction leader scope, 양국 국민정신과 KOR 밸런스 |
| 태평양 수호자 | 외교 규칙 변경, decision category와 잠재 전쟁 확대 |
| 만주 해방 | `MAN` 정체·정권·독립 상태에 따라 전쟁 명분이 달라짐 |
| 타이완 자유선거 | state `524`, 독립/통합 분기와 후속 국가 상태 |
| 남양군도 통합 | state `647/684/633/646/648`, `GUM/FSM` annex와 core 변경 |
| 본토경제 | 일본 state와 건물·자원·victory point 변경 |
| 신간선 | 구형 province 경로를 직접 사용하며 현재 HoK 한국 지도와 충돌할 가능성 |
| 군국주의자 숙청 | 특성 기반 전군 검색 때문에 target의 늘어난 장군 roster까지 MAN으로 이전할 수 있음 |
| 타이완 자치도 설정 | 원작 내부에서도 `autonomous_state`와 `autonomy_state`가 불일치해 parser·효과 계약 확인 필요 |
| 연구 보상 | 원작 `JAP_strength_civilian_control`이 현행에서 찾지 못한 `JAP_duplicate_research_efforts`를 참조 |
| 공화국 후속 이벤트 | 원작 `.12`의 설명은 황실 처분을 말하지만 실제 효과는 정치력 또는 파시즘 지지도·안정도 변경뿐임 |
| 히로히토 판정 | 원작 coup는 `has_country_leader = { id = 700 }`으로 찾지만 1.19.2 target은 그 numeric leader ID 블록을 주석 처리하고 새 체계를 사용함 |
| 만주 cosmetic | 원작 이벤트의 `man_restored`와 target의 `MAN_restored` casing이 다름 |

원작 신간선 효과의 철도 path를 target 1.19.2 province/state topology와 대조한 결과 모든 경유지는 일본 내에 있고 province `12031`도 state `531`의 고베로 확인됐다. 따라서 path는 보존했으며 map 파일은 변경하지 않았다. 실제 철도 건설 결과는 runtime 미검증이다.

설치본의 state 파일명은 `555-Lagos.txt`지만 파일 본문은 `STATE_555 #Kuril Islands`, 소유국은 JAP, 한·영 localisation은 각각 `쿠릴 열도`와 `Kuril Islands`다. 따라서 원작의 state `555` 쿠릴 보상은 현재 확인 범위에서는 올바른 대상을 가리킨다. 이 사례처럼 파일명만으로 state 의미를 판정하지 않고 본문, localisation, 소유권과 province 구성을 함께 대조한다.

## 9. 독립성·배타성·AI 정책

화면상 독립 배치와 게임 논리상 완전 무관계는 서로 다르다. 아무 guard 없이 새 분기를 시작할 수 있게 하면 한 국가가 1.19.2 군국주의·황도파 경로와 HoK 민주 경로를 동시에 진행할 수 있다.

구현에서 확정한 정책:

| 질문 | 안전한 기본안 | 상태 |
|---|---|---|
| 새 root를 언제 열 것인가 | 1936 시작 시 표시하되, 상충하는 target 정치 경로 확정 전만 선택 가능 | `IMPLEMENTED` |
| target 정치 경로와 배타성을 어떻게 보장할 것인가 | target 정치 entry 6개의 reciprocal mutex/HIDE guard와, 부모 숨김을 덮어쓰는 NCNS 하위 `allow_branch` 경계 9개의 동일 guard | `CORRECTED_IMPLEMENTED_STATIC` |
| target SEA 산업·군부 계통을 HoK에서도 사용할 것인가 | 정치 노선과 별개인 공통 계통으로 유지. HoK mutex/HIDE guard를 두지 않음 | 잘못 적용한 guard `ROLLED_BACK`; target 동작 복원 |
| HoK와 양립하지 않는 계통을 언제 숨길 것인가 | 어느 쪽 root든 먼저 완료한 뒤 relayout. `SHOW`는 바닐라 UI 선택을 존중해 잠긴 계통을 표시 | `IMPLEMENTED_STATIC`; runtime `NOT RUN` |
| AI가 새 분기를 고를 수 있는가 | `is_ai = no`와 root AI weight 0의 player-only | `IMPLEMENTED` |
| historical AI를 바꿀 것인가 | 바꾸지 않음 | `IMPLEMENTED`; runtime 회귀 미검증 |
| 비역사 AI plan을 복원할 것인가 | 별도 승인 전 `DEFER` | `DEFER` |
| WTT가 없을 때도 지원할 것인가 | 첫 구현은 WTT 활성 구성만 지원 후보 | `OUT_OF_SCOPE` |
| NCNS가 없을 때도 지원할 것인가 | 첫 구현은 NCNS 활성 구성만 지원 후보 | `OUT_OF_SCOPE` |
| 기존 save를 지원할 것인가 | 새 게임 전용, 기존 save 호환 주장하지 않음 | `DECIDED` |

### 9.1 D-JAP-16 — NCNS 정치 계통의 중첩 `allow_branch` 교정

후속 사용자 화면과 production 소스를 다시 대조해 최초 분류가 잘못됐음을 확인했다.

- `JAP_ministry_of_commerce_and_industry` 이하 34개와 `JAP_the_imperial_defense_plan` 이하 61개는 특정 정치 노선 전용이 아니라 1.19.2 일본의 공통 SEA 산업·군부 계통이다.
- 이 두 root는 target에서 빈 `mutually_exclusive`를 가지거나 자체 `allow_branch`가 없고, 여러 정치 노선 완료 상태에 따라 위치만 옮기는 `offset`을 가진다. 따라서 HoK 경로에서도 유지해야 한다.
- 최초 D-JAP-16이 두 계통에 추가했던 HoK mutex, HIDE guard, `HOK_JAP_vanilla_sea_branch_selected`, 완료 후 relayout 및 군부 leaf 보강은 모두 잘못된 대상 변경으로 분류해 롤백했다.
- NCNS 정치 구간은 top 정치 root 3개의 prerequisite closure 297개와 prerequisite가 끊긴 고이소 내각 계통 4개, 합계 301개다.
- `allow_branch`가 false인 부모의 상태는 일반 prerequisite 자식에게 전파되지만, 자식이 자체 `allow_branch`를 가지면 부모 상태를 무시하고 자기 조건만 평가한다. 이것이 정치 root를 숨겼는데도 큰 하위 묶음이 남은 직접 원인이다.

교정한 구현 계약은 다음과 같다.

1. 기존 정치 진입점 6개와 HoK root 사이의 reciprocal mutex/HIDE guard는 유지한다.
2. NCNS 정치 계통 내부에서 자체 `allow_branch`로 상속을 끊는 다음 9개 경계에도 HoK 완료와 timing-safe 선택 flag 조건을 병합한다: `JAP_yatagarasus_guidance`, `JAP_embodying_empress_jinguu`, `JAP_solidify_tohokai_rule`, `JAP_the_koiso_cabinet`, `JAP_appoint_new_generals`, `JAP_implement_army_reforms`, `JAP_a_red_sun_rises_for_a_new_era`, `JAP_the_spirit_of_the_ikko_ikki`, `JAP_organize_a_general_election`.
3. 특히 장군 임명·육군 개혁·붉은 태양·총선의 네 경계는 1936 초기 조건에서 자체 `allow_branch`가 참이므로, 부모 정치 root가 숨겨진 뒤에도 최대 123개의 하위 focus를 다시 표시할 수 있다. 나머지 다섯 경계도 후속 flag 변화나 구 save에서 재등장하지 않도록 같은 guard를 가진다.
4. `JAP_the_koiso_cabinet`은 prerequisite가 없는 독립 경계이므로 별도 guard가 필수다.
5. WTT 구형 하위 경계 `JAP_national_mobilization_law`와 `JAP_national_defense_state`는 `No Compromise, No Surrender` 비활성 조건을 요구한다. HoK root는 해당 DLC 활성 환경만 허용하므로 이 두 경계에는 중복 guard를 추가하지 않는다.
6. `HIDE`에서는 HoK 선택 flag를 먼저 설정하고 `mark_focus_tree_layout_dirty`를 호출해 정치 root와 위 9개 경계를 다시 평가한다. `SHOW`에서는 바닐라 UI 규칙에 따라 정치 계통이 보일 수 있으나 reciprocal mutex로 진입은 차단한다.
7. SEA 산업·군부 95개의 효과·선행 조건·선택 가능성은 보존한다. 다만 `HIDE`에서 HoK가 선택되면 산업 root 하나에 `x=-83` 조건부 offset을 적용해 산업 범위를 `x=20..37`, 그 상대 자식인 군부 범위를 `x=39..65`로 함께 이동한다. HoK 범위 `x=6..18`과 최소 2열 간격을 둔다.

20:18:25 fresh 실행은 HOI4 1.19.2 `(bd08)`, DLC 36개, 활성 Hearts of Korea 모드 1개를 기록했고 20:18:50에 1936 single-player로 진입했다. clean `error.log`에는 `relative_focus_id`, `Error in focus`, `allow_branch` 또는 위치 관련 오류가 0개였다. 이어 사용자가 제공한 1936-01-01 `HIDE` 화면은 `문민정부 강화` 완료 상태에서 HoK 40개와 정상 SEA 산업·군부 계통은 남고 NCNS 정치 계통은 사라진 결과를 보여 준다. 이 범위는 `RUNTIME_CONFIRMED_HIDE`이며 `SHOW`, 역방향 잠금, 자연 70일 완료와 save/load는 `NOT RUN`이다.

`ai_will_do = 0` 하나만으로 historical behavior 보존을 확정하지 않는다. 실제 AI plan, focus availability와 대안 가중치를 함께 검사해야 한다.

원작 `JAP_demand_sagaren`은 `ai_will_do`의 base factor가 0인 상태에서 modifier factor 2를 곱하므로 정적 의미상 AI가 선택하지 않을 가능성이 높다. 이를 원작 행동으로 보존할지, 원작 버그로 분류해 고칠지는 AI 복구 승인과 분리해 결정한다.

## 10. 파일별 구현

| 파일/영역 | 구현 결과 |
|---|---|
| `common/national_focus/japan.txt` | 정확한 1.19.2 target-derived host. shared hook 1개, 정치 entry 6개의 mutex/HIDE guard, NCNS 정치 하위 자체 `allow_branch` 경계 9개의 HIDE guard와 HoK-HIDE용 SEA 공통 계통 위치 offset 1개만 delta로 유지 |
| `common/national_focus/HOK_JAP_democratic_shared.txt` | 민주 32개 + 공유경제 8개를 40개 shared focus로 격리하고 root는 절대 `(10,0)`, 하위 39개는 내부 상대좌표로 배치. 정치 entry 6개를 root mutex/HIDE 완료 검사에 포함하고 완료 reward에서 timing-safe 선택 flag를 설정 |
| `common/ideas/HOK_JAP_democratic_ideas.txt` | HoK 전용 idea 7개만 additive 정의 |
| `common/characters/HOK_JAP_democratic_characters.txt` | target에 없는 인물 7명만 additive 정의 |
| `common/country_leader/00_hok_traits.txt` | 기존 두 HoK trait 정의 재사용, 중복 정의 없음 |
| `events/HOK_JAP_democratic_events.txt` | 필요한 event 22개를 `hok_jap_democratic` namespace로 이식 |
| `events/NewsEvents_KOR.txt` | 기존 `newsj.1-.4` 정의 재사용, 중복 정의 없음 |
| JAP/KOR decision | 북사할린과 별도 Pacific Guardian category/결정 3개만 추가 |
| `common/ai_strategy/KOR.txt` | 기존 조건에 HoK root OR 한 곳만 추가 |
| TWN/cosmetic 정의와 flags | 기존 묶음을 재사용하고 TWN history의 제거된 doctrine tech만 정리 |
| localisation | English/Korean 각각 198개 key, 동일 body, UTF-8 BOM |
| GFX | 기존 원작/target asset을 재사용하며 binary 변경 없음 |
| country history/OOB/map | TWN history 최소 tech 정리 외 전체 복원 없음; OOB/map 변경 없음 |
| descriptor | 변경하지 않음 |
| AI plan | 첫 구현 범위에서 제외 |
| music | 별도 승인까지 제외 |

## 11. 구현·검증 작업 패키지

production 구현 승인에 따라 WP0과 WP2-WP6의 소스 작업을 적용했다. WP1은 사용자 제공 화면으로 초기 절대좌표의 좌단 잘림과 후속 `+8` 절대좌표 배치의 과도한 공백까지 확인했다. 이를 대체하려던 shared→ordinary 상대좌표 앵커 방식은 20:08 HOI4 1.19.2 실행에서 엔진 오류가 확인돼 폐기했고, 같은 계산 결과인 root 절대 `(10,0)` fallback을 production에 적용했다. 20:18 fresh 실행과 완료 화면으로 fallback startup 및 `HIDE` 후 배치를 확인했다. WP8 회귀는 일부만 수행됐고 WP7은 별도 승인까지 제외한다. 아래 순서는 후속 runtime 검증에서도 유지한다.

1. **WP0 — source freeze**
   - immutable original archive와 target 1.19.2 파일 hash 재확인
   - exact playset, DLC, language, launcher source 기록
2. **WP1 — host integration proof**
   - 효과 없는 고유 ID 한 개로 shared-focus 표시 여부 검증
   - 바닐라 일본 중점 수·연결·AI plan 유지 확인
3. **WP2 — focus skeleton — SOURCE COMPLETE**
   - core 32개와 D-JAP-01에서 포함 확정한 공유경제 focus의 고유 ID, 좌표, prerequisite, mutually-exclusive 구조만 이식
   - 후속 WP3-WP6에서 효과와 이벤트를 연결
4. **WP3 — 민주화와 내전**
   - 시위, 숙청, coup와 civil war chain 이식
   - MAN/MEN/CHI/KOR scope를 target에 맞게 검증
5. **WP4 — 전후 체제와 군제**
   - 쇼와 헌법/공화정, 지도자, 문민 군제, 관련 ideas 이식
   - 숙청 대상 allowlist와 공화국 cosmetic 3종 검증
6. **WP5 — 외교·식민지**
   - 한국/영국, 태평양, 만주/사할린, 타이완/남양군도 이식
   - `TWN` 기능 묶음과 KOR AI 간접 참조 검증
7. **WP6 — 경제·연구**
   - 연구와 본토경제 8개, state/province/철도 효과 검증
   - state 파일명과 실제 본문이 다른 경우 본문·localisation·소유권·province를 기준으로 판정
8. **WP7 — 선택적 AI·음악**
   - 사용자가 별도 승인할 때만 진행
9. **WP8 — 전체 회귀**
   - 새 게임, focus UI, branch behavior, historical AI, save/load와 MP 검증
10. **WP9 — HoK 경로의 NCNS 정치 계통 숨김 교정 — CORRECTED_IMPLEMENTED_STATIC**
   - 오대상이던 SEA 산업·군부 root의 mutex/HIDE guard·선택 flag·relayout과 군부 leaf guard를 전부 롤백
   - 정치 entry 6개의 기존 reciprocal mutex/HIDE guard는 유지
   - 부모 숨김을 덮어쓰는 NCNS 정치 하위 자체 `allow_branch` 경계 9개에 HoK 완료/선택 flag 조건 병합
   - 301개 정치 focus를 일괄 수정하지 않고 3개 NCNS top root와 9개 하위·독립 경계의 전파 구조로 관리
   - `HIDE`에서 산업 root 하나만 `x=-83` 이동해 복원한 SEA 95개를 HoK 오른쪽에 연속 배치
   - `HIDE`/`SHOW`, 완료 직후 relayout, SEA 95개 기능 유지와 새 게임 save/load를 별도 검증

각 패키지는 독립 diff와 검증 기록을 남기고, 앞 단계가 실패하면 뒤 단계로 확대하지 않는다.

## 12. 정적 검증 계약

- [x] target 1.19.2 일본 focus 448개의 ID 집합이 누락되지 않는다.
- [x] 새 HoK focus 수가 core 32개와 D-JAP-01에서 확정한 공유경제 수량의 합과 같고 ID가 모두 고유하다.
- [x] 확인된 target focus 충돌 8개와 모든 downstream 참조가 migration ledger에 들어 있다.
- [x] focus, event, idea, character, decision, flag, localisation과 sprite 중복 ID가 0이다.
- [x] 모든 prerequisite와 mutually-exclusive 대상이 실제 등록된다.
- [x] WTT·NCNS DLC gate가 D-JAP-05의 지원 범위와 일치한다.
- [x] 모든 event/idea/character/decision 참조가 실제 정의로 해소된다.
- [x] 외부 idea ID와 `generic.2`, `generic.5`, `wtt_japan.1`이 target 정의로 해소되고 올바른 scope에서 호출된다.
- [x] 원작 event chain의 entry와 후속 호출이 끊기지 않는다.
- [x] 필수 contributor 주석을 제외한 target-derived host 동작 차이가 승인된 HoK hook, 정치 entry 6개 및 NCNS 정치 하위 자체 `allow_branch` 경계 9개의 guard와 HoK-HIDE용 SEA 위치 offset 1개에만 해당한다.
- [x] `replace_path`가 새로 생기지 않는다.
- [x] English/Korean localisation 양쪽의 BOM, locale header, 상대경로와 key 형식이 유지된다.
- [x] English/Korean localisation의 key set과 표시 문자열 body 차이가 0이다.
- [x] 한국 state `1082–1084`, 쓰시마 `1085`와 기존 KOR bridge가 보존된다.
- [x] 구형 state/province/railway 참조를 target 의미로 오인해 일괄 치환하지 않는다.
- [x] state 참조는 파일명만이 아니라 본문·localisation·소유권·province 의미까지 대조했다.
- [x] `JAP_duplicate_research_efforts`, `Sagaren`과 `event_target:WTT_current_china_leader`가 정의·수명 또는 대체 근거 없이 남아 있지 않다.
- [x] 히로히토를 numeric leader ID `700`으로 검사하거나 제거하는 원작 로직이 남아 있지 않다.
- [x] `man_restored`/`MAN_restored` casing과 event namespace casing이 명시적으로 확정됐다.
- [x] 기존 `JAP_japanese_national_liberation_committee_trait`와 `JAP_champion`을 중복 정의하지 않는다.
- [x] `JAP_mitsumasa_yonai_navy`와 target `JAP_mitsumasa_yonai`가 같은 인물로 중복 등장하지 않는다.
- [x] 타이완 독립을 지원한다면 `TWN` 태그·정의·history·색상·이름풀·localisation·flags가 모두 해소된다.
- [x] 공화국 cosmetic 3종에 필요한 이름과 대·중·소 flags가 모두 해소된다.
- [x] 군국주의자 숙청의 대상 명단과 target roster 차이를 검토했다.
- [x] base-game과 Workshop 파일은 변경되지 않는다.
- [x] diff에 관계없는 formatting이나 line-ending 변환이 없다.
- [x] 정치 entry 6개의 reciprocal mutex/HIDE guard와 NCNS 정치 하위 자체 `allow_branch` 경계 9개의 HoK HIDE guard가 존재한다.
- [x] NCNS 정치 구간의 top-root prerequisite closure 297개와 독립 고이소 계통 4개를 식별했고, 자체 `allow_branch`가 부모 숨김을 덮는 모든 활성 경계 9개를 감사했다.
- [x] SEA 산업 34개·군부 61개의 효과·선행·가용성은 target과 같고 `HOK_JAP_vanilla_sea_branch_selected` 참조도 남지 않는다. 산업 root의 HoK-HIDE용 위치 offset 1개만 의도된 차이다.
- [x] HoK 선택 flag는 완료 reward의 relayout보다 먼저 설정되고, `has_completed_focus` fallback과 함께 HIDE 조건에서만 정치 계통 표시 여부에 영향을 준다.
- [x] HoK를 선택하지 않은 경우 바닐라 정치·산업·군부의 기존 offset, AI와 진행 내용이 target과 일치한다.

## 13. 런타임 검증 계약

게임 실행은 별도 승인 후에만 수행한다.

### 13.1 비교 구성

| 실행 ID | 구성 | 분리 검증 목적 |
|---|---|---|
| `A-JDEM-BASE` | 1.19.2 vanilla control | target 일본 focus·AI 기준선 |
| `B-JDEM-DEP` | 1.19.2 + 정확한 `Korean Language` | dependency 자체의 VFS·localisation 영향 |
| `D-JDEM-HOK` | 1.19.2 + Hearts of Korea 단독 | focus host·ID·HoK 자체 동작 |
| `C-JDEM-SUPPORTED` | 1.19.2 + 정확한 `Korean Language` + Hearts of Korea | 선언된 지원 playset 최종 동작 |

각 실행에서 checksum, DLC, language, playset, historical AI 설정과 game rules를 기록한다.

첫 지원 판정은 네 실행 모두 WTT와 NCNS를 활성화한 동일 DLC 조건에서 비교한다. WTT-off 또는 NCNS-off 호환성을 주장할 때만 각각 별도 DLC matrix를 추가한다.

### 13.2 일본 focus UI

- [ ] 1936 일본 선택 후 기존 1.19.2 전체 트리가 유지된다.
- [ ] HoK 민주 분기가 옆의 독립 구역에 표시된다.
- [ ] core 32개와 D-JAP-01에서 포함 확정한 공유경제 노드의 연결선, 상호배타, icon과 한국어 문자열이 맞는다.
- [ ] 화면 경계, shortcut, search와 스크롤 영역이 깨지지 않는다.
- [ ] target 정치 경로를 확정하면 HoK 상충 경로가 안전하게 잠긴다.
- [ ] HoK root를 확정하면 상충하는 target 정치 진행을 동시에 할 수 없다.
- [ ] `HIDE`에서 HoK root 완료 직후 NCNS 정치 top root와 자체 `allow_branch` 하위 경계 9개의 계통이 모두 사라지고 HoK 구역이 잘리거나 이동하지 않는다.
- [ ] `SHOW`에서 HoK root 완료 뒤 경쟁 정치 계통은 표시되더라도 mutex로 선택할 수 없다.
- [ ] SEA 산업 34개·군부 61개와 경제·군부 shortcut은 HoK 완료 전후 모두 표시·사용되며, HIDE 완료 후 산업 `x=20..37`, 군부 `x=39..65` 범위로 이동한다.
- [ ] 후속 flag 변화, 저장 후 재접속과 구 save에서 고이소·도호카이·황후·불교사회주의 하위 경계가 다시 나타나지 않는다.
- [ ] `jap_imperial_influence_inlay_window`와 가로 스크롤 범위가 target 공통 계통을 정상적으로 포함한다.

### 13.3 행동

- [ ] 민주화 positive path와 선택 불가 negative path를 각각 확인한다.
- [ ] 민주 내전 시작 세력, 수도, states, 육·해군 분할과 생성 부대가 의도와 맞는다.
- [ ] 군국주의자 숙청이 승인된 장군만 이전하며 target의 추가 인물을 뜻밖에 옮기지 않는다.
- [ ] 내전 종료 뒤 focus 진행이 멈추거나 초기화되지 않는다.
- [ ] 쇼와 헌법과 공화정이 서로 배타적이며 지도자·cosmetic·idea가 맞다.
- [ ] 한국 동맹·자유무역의 수락, 거절, 이미 같은 faction인 경우를 확인한다.
- [ ] MAN/MEN/CHI/SOV/TWN/GUM/FSM이 없는 경우 또는 예상과 다른 정권인 경우를 확인한다.
- [ ] 타이완·남양군도·사할린·본토경제의 state 효과가 target 지리와 맞는다.
- [ ] 섬 개발 보상이 실제 쿠릴 열도 state `555`에 적용된다.
- [ ] 신간선이 한국이나 잘못된 province를 통과하지 않는다.

### 13.4 회귀

- [ ] HoK를 선택하지 않은 historical JAP AI가 기존 1.19.2 경로를 유지한다.
- [ ] HoK를 선택하지 않은 플레이어·AI는 SEA 산업 34개와 군부 61개를 target과 동일하게 사용할 수 있다.
- [ ] 중일전쟁, 남방전쟁과 현행 일본 AI plan이 새 분기 때문에 끊기지 않는다.
- [ ] 독립 한국의 1936 OOB와 한국 9도 처리가 유지된다.
- [ ] 1939 bookmark에서 한국 소유권·저항·순응도와 일본 OOB가 유지된다.
- [ ] 새 게임 save → load → 진행 → save → reload가 통과한다.
- [ ] 기존 save 호환을 주장하려면 별도 pre-change save 검증을 수행한다.
- [ ] 멀티플레이 호환성을 주장하려면 같은 mod/DLC/load order의 checksum과 동기화를 확인한다.
- [ ] baseline 대비 새 fatal, parser, invalid focus, missing reference와 event spam이 없다.

## 14. 완료 조건

민주 분기 이식은 다음을 모두 만족할 때만 완료로 판단한다.

1. 1.19.2 바닐라 일본 448개 focus 정의와 ID가 보존되고, HoK를 선택하지 않은 경로에서는 기존처럼 사용할 수 있다. HoK 확정 뒤에는 경쟁 정치 계통에 대한 D-JAP-16 조건부 잠금·숨김만 허용한다.
2. HoK 민주 core 32개와 D-JAP-01에서 포함 확정한 공유경제 focus가 독립 구역에 표시된다.
3. 원작 의도와 달라진 효과가 모두 migration ledger에 기록돼 있다.
4. 중복 ID와 미해결 참조가 없다.
5. 민주 내전과 양 체제 분기를 실제 게임에서 확인했다.
6. 한국 관련 외교·state 효과와 KOR bridge 회귀가 없다.
7. historical JAP AI와 중일전쟁 경로가 기존 control과 동등하다.
8. runtime 로그에 새 관련 오류가 없다.
9. 실제로 수행하지 않은 검사는 `NOT RUN` 또는 `UNPROVEN`으로 남긴다.
10. Git diff에는 승인된 일본 민주 분기와 필수 종속성만 포함된다.

## 15. 롤백 원칙

구현을 되돌릴 때 목표 상태는 현재의 target 직접 상속 상태다.

- HoK shared-focus 정의와 host hook을 제거한다.
- target-derived `japan.txt`가 HoK hook 때문에만 존재했다면, 검증 후 그 override를 제거해 설치된 target을 다시 직접 상속한다.
- 관련 event/idea/character/decision/localisation/GFX는 다른 caller가 없는 것을 확인한 뒤 별도 범위로 처리한다.
- 기존 KOR bridge, 한국 map, OOB, save와 launcher 설정은 건드리지 않는다.
- rollback도 destructive Git 명령으로 수행하지 않는다.

## 16. 구현 시 확정한 결정과 남은 검증

| 번호 | 결정 | 권장 기본값 |
|---|---|---|
| D-JAP-01 | 공유 본토경제 8개 포함 여부 | 포함. HoK 민주 root의 prerequisite 자식으로 귀속 |
| D-JAP-02 | HoK root의 시작 조건 | 1936부터 player에게 표시하고 상충 정치 진입점 선택 전만 가능. 1939 bookmark는 별도 history 회귀 검증 전 지원하지 않음 |
| D-JAP-03 | target 정치 분기와 논리적 배타 방식 | target 정치 진입점 6개와 reciprocal mutex/HIDE guard 적용 |
| D-JAP-04 | AI 선택 | player-only; 원작 일본 AI 파일은 미복구 |
| D-JAP-05 | DLC 지원 범위 | WTT와 NCNS가 모두 활성화된 1.19.2만 최초 지원 후보 |
| D-JAP-06 | 원작 밸런스 그대로 유지 또는 target 조정 | 원작 값을 우선 보존하고 확인된 1.19.2 불일치만 적응 |
| D-JAP-07 | `Minshu_ikki` 음악 복구 | 별도 승인까지 보류 |
| D-JAP-08 | 정확한 화면 좌표 | 절대 `x = -4`와 후속 전체 `+8` 이동은 각각 좌단 잘림과 과도한 공백이 확인된 중간안이며 D-JAP-15가 supersede함 |
| D-JAP-09 | 기존 save 지원 | 주장하지 않음; 새 게임 기준 |
| D-JAP-10 | 군국주의자 숙청 대상 | 원작 8명 explicit allowlist로 확정 |
| D-JAP-11 | 타이완 독립 선택지 지원 | bundle 이식 및 구형 doctrine tech 정리 완료; 실제 생성·자치도는 runtime 미검증 |
| D-JAP-12 | 원작의 확인된 오타·서술 불일치·AI factor 0 처리 | namespace/casing/numeric ID/stale reference만 근거를 기록해 적응; AI는 root에서 차단 |
| D-JAP-13 | 요나이 미쓰마사 처리 | 중복 정의 금지. target role gate 충돌 때문에 최초 구현 보상에서는 보류 |
| D-JAP-14 | 소멸 국가와 영토 소유권 negative path | `MAN`·`KOR`·`SOV` 존재 여부를 확인하고, 북사할린 양도는 `SOV`의 state 655 소유를 focus와 수락 event에서 재검사 |
| D-JAP-15 | HoK root의 후속 배치 기준 | `JAP_the_unthinkable_option`을 참조한 shared→ordinary 상대좌표안은 20:08 런타임에서 `relative_focus_id ... does not exist`로 `DISPROVEN`. root를 절대 `(10,0)`으로 두는 fallback을 적용하고 하위 39개의 상대좌표 사슬은 유지. 전체 `x=6..18`; 20:18 startup과 HIDE 화면 `CONFIRMED` |
| D-JAP-16 | HoK 완료 뒤 경쟁 정치 계통 처리 | 최초 SEA 산업·군부 분류는 오판으로 롤백. 정치 entry 6개의 mutex/HIDE guard를 유지하고 NCNS 정치 하위 자체 `allow_branch` 경계 9개에 같은 HoK 완료/선택 flag 조건을 전파. HoK 완료 후 `HIDE` 화면 `CONFIRMED`; `SHOW`·역방향 잠금·save/load `NOT RUN` |
| D-JAP-17 | HoK 완료 뒤 공통 SEA 산업·군부 배치 | 기능은 보존하고 `HIDE`에서 산업 root에 `x=-83` offset 1개만 적용. 정적 범위 산업 `x=20..37`, 군부 `x=39..65`; 완료 후 공통 계통 유지·재배치 화면 `CONFIRMED` |

D-JAP-08의 첫 런타임에서는 HoK 범위 `x = -8..4`가 좌단에서 잘리는 것이 확인됐다. 이어 HoK와 바닐라 root·절대 UI 요소를 8열 평행 이동해 HoK를 `x = 0..12`로 옮겼지만 사용자 제공 화면에서 바닐라 구성요소 사이의 과도한 공백이 확인됐다. 이 중간안은 D-JAP-15의 절대 `(10,0)` fallback이 대체하며, 바닐라 좌표는 1.19.2 원값으로 복원한다.

### 16.1 D-JAP-15 상대좌표 시도와 절대좌표 fallback

처음에는 `HOK_JAP_strengthen_civilian_government`가 `JAP_the_unthinkable_option`을 `relative_position_id`로 참조하고 상대 `(-2,0)`을 사용하도록 구현했다. 그러나 20:08 HOI4 1.19.2 실행의 `error.log`는 `relative_focus_id: JAP_the_unthinkable_option does not exist. Relative focus must be scripted before this.`를 기록했다. 따라서 이 shared→ordinary 상대참조 조합은 `DISPROVEN`이며 production에서 제거했다.

현재 `HOK_JAP_strengthen_civilian_government`는 `relative_position_id` 없이 절대 `x=10`, `y=0`을 사용한다. 나머지 HoK focus 39개는 기존 직·간접 `relative_position_id` 사슬로 이 root를 따라가므로 계산 범위는 이전과 같은 `x=6..18`, `y=0..9`다. host의 `shared_focus` hook 위치는 기존 WTT root 정의 뒤에 그대로 두지만, 현재 root 위치 계산은 어떤 바닐라 focus에도 의존하지 않는다.

현재 배치 계약은 다음과 같다.

- 바닐라 448개 focus의 좌표를 HoK 배치 때문에 일괄 이동하지 않는다.
- HoK root 하나만 안정적인 절대 `(10,0)`에 두고, 하위 39개의 내부 상대좌표·prerequisite·연결선 구조는 유지한다.
- 하위 상대참조의 누락과 순환 참조가 없어야 한다.
- 위치 배치는 mutually-exclusive, 완료 조건 또는 게임 진행 관계를 추가하지 않는다.
- `allow_branch` 숨김, `obsolete_focus_branches_visibility`의 `HIDE`/`SHOW`, 완료 후 `mark_focus_tree_layout_dirty`와 save/load 뒤에도 root와 하위 분기가 같은 위치에 남아야 한다.
- focus 아이콘·제목·연결선, 분기 선택 UI, continuous-focus 창 및 inlay와 충돌하지 않아야 한다.

target-derived `japan.txt`의 WTT root `x=12`, NCNS root `x=27`, continuous-focus `x=20`과 inlay 좌표 10개는 설치된 1.19.2 target 원값으로 복원하고 정적으로 일치함을 확인했다. 20:08 실행은 상대좌표안의 실패를 재현했고, 20:18 fresh 실행에서는 절대좌표 fallback이 새 focus/위치 오류 없이 1936 single-player까지 로드됐다. 이어 사용자 제공 완료 화면은 `HIDE`에서 HoK와 SEA 공통 계통의 배치를 확인했다. root 진행 중, `SHOW`, 역방향 잠금과 save/load는 후속 검증 대상으로 남는다.

정적 좌표 계산에서는 활성 NCNS focus와 HoK focus의 정확한 좌표 중복이 0이다. 다만 `HOK_JAP_develop_nanyo_gunto` `(15,8)`과 `JAP_the_lecture_group_ascendant` `(15,9)`가 한 칸 수직 인접하므로 아이콘·제목·연결선의 실제 가독성은 런타임 확인 대상으로 남긴다.

### 16.2 D-JAP-16에 적용한 숨김 경계

D-JAP-15 뒤 화면의 큰 잔존 묶음을 SEA 산업·군부 계통으로 분류한 최초 판단은 잘못됐다. 실제 적용 결과 정상 SEA 계통만 사라지고 경쟁 정치 계통이 남아, 화면과 source graph를 다시 대조했다. SEA 산업·군부는 공통 계통으로 복원했으며, 숨김 대상은 NCNS 정치 구간으로 확정했다.

교정 경계는 정치 entry 6개와 NCNS 정치 내부 자체 `allow_branch` 9개다. 보통 자식은 prerequisite 부모의 disallowed 상태를 상속하지만, 자체 `allow_branch`가 있으면 부모 조건을 덮어쓴다. 따라서 9개 경계의 기존 조건 안에 HoK 완료 및 `HOK_JAP_democratic_branch_selected`를 병합했고, 나머지 정치 focus는 prerequisite 전파에 맡겼다. 완료 reward에서 선택 flag를 먼저 설정한 뒤 relayout하는 timing-safe 순서는 유지한다.

사용자 제공 완료 화면에서 `HIDE`의 NCNS 정치 구간이 보이지 않고 SEA 산업·군부 공통 계통이 유지·재배치된 것은 확인했다. 후속 UI 판정에서는 `SHOW`의 mutex 잠금, 반대 정치 root 선완료 시 HoK 역방향 잠금, save/load, 두 shortcut과 `jap_imperial_influence_inlay_window`가 빈 공간이나 유령 이동을 만들지 않는지를 검사한다.

## 17. 현재 판정

- 원작 HoK에 민주주의 전체 분기가 존재한다: `CONFIRMED`
- target 1.19.2에 동일하거나 겹치는 focus ID가 있다: `CONFIRMED`
- target 1.19.2와 직접 충돌하는 원작 민주 분기 focus ID는 현재 확인 기준 최소 8개다: `CONFIRMED`
- target 1.19.2의 state `555`는 파일명과 달리 본문·localisation·소유권 기준으로 쿠릴 열도다: `CONFIRMED`
- 두 번째 일반 일본 focus tree가 기존 트리에 자동 합쳐진다: `UNPROVEN`; target 관례와 맞지 않아 구현 후보로 `REJECTED`
- 별도 shared-focus 정의와 target-derived host의 최소 hook이 연결되고 실제 일본 트리에 표시된다: `CONFIRMED`; 전체 진행 동작은 `UNPROVEN`
- HoK root의 shared→ordinary 상대좌표안은 20:08 HOI4 1.19.2 오류로 `DISPROVEN`; 현재 root는 절대 `(10,0)`이고 하위 39개만 상대좌표 사슬을 유지해 전체 범위는 `x=6..18`이다: 20:18 startup 및 HIDE 완료 화면 `CONFIRMED`
- SEA 산업·군부 95개는 정치 노선과 별개인 공통 계통이며 HoK에서 숨기면 안 된다: target source와 사용자 화면으로 `CONFIRMED`; 최초 D-JAP-16 대상 분류는 `DISPROVEN` 및 롤백
- 정치 root를 숨겨도 자체 `allow_branch`를 가진 하위 경계가 부모 상태를 무시해 최대 135개의 정치 focus를 다시 표시할 수 있다: source graph와 1.19.2 규칙으로 `CONFIRMED`
- D-JAP-16 교정안은 정치 entry 6개와 NCNS 하위 경계 9개에만 HoK guard를 적용한다: HoK 완료 후 HIDE 화면 `CONFIRMED`; SHOW·역방향 잠금·save/load `NOT RUN`
- D-JAP-17은 복원한 SEA 공통 계통을 HIDE에서 HoK 오른쪽으로 이동한다: 정적 범위 산업 `x=20..37`, 군부 `x=39..65`; 완료 후 화면에서 공통 계통 유지·재배치 `CONFIRMED`
- 원작 민주 분기 효과를 1.19.2에 그대로 복사해도 안전하다: `DISPROVEN`
- HoK 민주 분기 통합의 production 소스 구현이 적용됐다: `CONFIRMED`
- 구현의 초기 화면 표시는 사용자 제공 화면으로 확인됐다: `CONFIRMED`; 전체 분기 진행·이벤트·회귀 동작은 `UNPROVEN`
