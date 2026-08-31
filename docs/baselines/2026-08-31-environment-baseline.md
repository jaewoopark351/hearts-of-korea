# Hearts of Korea 환경 기준선 — 2026-08-31

## 목적과 판정 범위

이 문서는 `2026-08-31 15:16:33 +09:00` 전후에 확인한 복구 작업의 환경 기준선이다. 파일·descriptor·Steam 로컬 메타데이터를 읽기 전용으로 대조한 결과와 같은 시점에 생성·검증된 원본 archive 상태를 기록하며, 새 게임 실행이나 수정 후 재현 결과를 대신하지 않는다.

증거 등급은 다음과 같이 사용한다.

- `CONFIRMED`: 로컬 파일, 메타데이터 또는 공식 공개 기록에서 직접 확인
- `STRONGLY_SUPPORTED`: 여러 독립 증거가 일치하지만 필요한 원본 파일 또는 런타임 재현이 없음
- `UNPROVEN`: 가능성은 있으나 추가 기준본이나 실행 증거가 필요
- `DISPROVEN`: 현재 명시된 범위에서 증거와 모순

## 경로 별칭

개인 식별 경로와 계정명은 기록하지 않는다. 이 문서의 모든 경로는 아래 별칭을 사용한다.

| 별칭 | 의미 |
|---|---|
| `<PROJECT>` | 현재 Git 저장소이자 계승판의 권위 있는 작업 복사본 |
| `<HOI4_INSTALL>` | 현재 Steam의 Hearts of Iron IV 설치 폴더 |
| `<HOI4_USER_DATA>` | 실제로 확인한 리디렉션된 Paradox 사용자 데이터 폴더 |
| `<STEAM_WORKSHOP>` | Steam Workshop App ID `394360`의 콘텐츠 루트 |

파생 경로는 `<STEAM_WORKSHOP>/2898629778`처럼 표기한다.

## 기준선 요약

| 항목 | 판정 | 확인 결과 |
|---|---|---|
| Git 작업 복사본 | CONFIRMED | branch `main`, commit `fd168974d29ac0af774ac0b8aa752b01e32f22a0`, 로컬 `origin/main` 대비 ahead/behind `0/0` |
| 목표 바닐라 `V_TARGET` | CONFIRMED | Operation Postern `1.19.2.0.a729 (d245)`, Steam build ID `23969257` |
| 원본 모드 설치본 | CONFIRMED | Workshop ID `2898629778`, content manifest `6685434440007626210` |
| 프로젝트와 원본 모드 파일 | CONFIRMED | 원본 1,049개 파일 중 1,048개 SHA-256 일치, 유일한 차이는 `descriptor.mod` |
| 원본 archive | CONFIRMED | ZIP 생성 및 원본 1,049개 항목과 개별 SHA-256 재검증 완료; missing/extra/mismatch `0/0/0` |
| 원본 공개 릴리스 식별 | STRONGLY_SUPPORTED | 설치 manifest는 공개 `1.0.9(1) '강계'` / HOI4 1.16 릴리스와 시각·크기·내용 범위가 일치 |
| 구형 바닐라 `V_OLD` | STRONGLY_SUPPORTED | 가장 강한 후보는 `1.16.8`, build ID `18550822`; 실제 depot 파일은 미확보 |
| 필수 의존 모드 | CONFIRMED | `Korean Language` 설치본은 존재하지만 현재 launcher 선택에는 활성화되지 않음 |
| active playset | CONFIRMED | `하츠오브 코리아 테스트`, custom order, HoK 1개가 position `0`에서 enabled; launcher DB와 `dlc_load.json`이 일치 |
| 게임 언어 | CONFIRMED | `settings.txt`와 `pdx_settings.json` 모두 `l_korean`; `V_TARGET`에도 공식 Korean localisation과 font가 존재 |
| 의존 모드 VFS 중첩 | CONFIRMED / UNPROVEN | 파일·key 중첩은 확인됐으나 실제 UI/localisation 증상과 `1.19.2` 호환성은 런타임 미검증 |
| launcher가 현재 프로젝트를 로드함 | DISPROVEN | launcher descriptor가 `<PROJECT>`가 아닌 존재하지 않는 과거 공백 경로를 가리킴 |
| `1.19.2` 런타임 호환성 | UNPROVEN | 현재 프로젝트 경로와 지원 playset으로 게임을 실행하지 않음 |

## Git 기준선

이 문서 생성 직전 읽기 전용 확인 결과:

- branch: `main`
- HEAD: `fd168974d29ac0af774ac0b8aa752b01e32f22a0`
- upstream comparison: `origin/main...HEAD = 0/0`
- working tree: dirty
- 이미 존재하던 변경:
  - `M <PROJECT>/.gitignore`
  - `M <PROJECT>/docs/CRASH_DEBUGGING_RUNBOOK.md`
  - `M <PROJECT>/docs/incidents/2026-08-31-startup-crash.md`
- 이 문서 추가 후 예상되는 새 항목:
  - `?? <PROJECT>/docs/baselines/2026-08-31-environment-baseline.md`

`.gitignore` 변경에는 `/.local-artifacts/` 제외 규칙이 포함된다. 검증 archive는 그 하위에 있어 Git status에 나타나지 않는다. 기존 변경은 본 문서 작업에서 수정하거나 되돌리지 않았다. commit, push, branch 변경도 수행하지 않았다.

## 목표 바닐라 `V_TARGET`

`<HOI4_INSTALL>/launcher-settings.json`과 Steam 로컬 App State에서 다음을 직접 확인했다.

- 제품: Hearts of Iron IV, Steam App ID `394360`
- 표시 버전: `Operation Postern v1.19.2.0.a729 (d245)`
- raw version: `1.19.2.0`
- Steam build ID: `23969257`
- 콘텐츠 depot `394361`의 현재 설치 manifest: `5160844398159557201`
- Windows depot `394362`의 현재 설치 manifest: `2731534386967510061`

이 값들은 설치된 목표 기준본을 `CONFIRMED`로 만든다. 다만 이번 작업에서는 HOI4를 실행하지 않았으므로, launcher가 실제로 이 설치본과 `<PROJECT>`를 함께 로드했다는 런타임 사실은 아직 확인되지 않았다.

Steam App State의 설치 언어는 `english`로 기록되어 있지만, 실제 HOI4 사용자 설정인 `<HOI4_USER_DATA>/settings.txt`와 `<HOI4_USER_DATA>/pdx_settings.json`은 모두 게임 localisation을 `l_korean`으로 지정한다. 두 값은 서로 다른 설정 층이므로 모순으로 취급하지 않는다. `V_TARGET` 자체에도 공식 Korean localisation과 font 파일이 존재한다.

`<HOI4_USER_DATA>/dlc_load.json`의 `disabled_dlcs`는 빈 배열이지만, 이것만으로 보유 DLC 전체의 실제 활성 상태를 확정하지 않는다.

## 원본 모드 `HOK_ORIGINAL`

### Steam 관리 설치본

`<STEAM_WORKSHOP>/2898629778`에서 확인한 값:

- Workshop ID / `remote_file_id`: `2898629778`
- descriptor 내부 version: `1.0.0`
- descriptor 선언 호환 버전: `1.16.*`
- 선언 dependency: `Korean Language`
- Steam content manifest: `6685434440007626210`
- Steam 기록 크기: `224,994,293` bytes
- Steam `timeupdated`: `1748899130`

공식 Workshop 페이지는 공개 릴리스를 `Ver. 1.0.9(1) '강계'`, `HOI4 1.16 호환`, `한글패치 필요`로 표시하고, 2025-06-02 업데이트 및 224.994 MB 크기를 기록한다. 개발자 패치노트도 `1.0.9(1) '강계'`가 HOI4 1.16 대응 업데이트라고 명시한다.

따라서 설치된 manifest가 공개된 마지막 `1.0.9(1)` 배포본이라는 판단은 `STRONGLY_SUPPORTED`이다. descriptor의 `version=1.0.0`은 공개 버전 표기와 맞지 않는 내부 메타데이터로 보이지만, 그 필드만으로 별도 배포본이라고 판단하지 않는다.

### 프로젝트 파일과의 일치

`<STEAM_WORKSHOP>/2898629778`의 전체 1,049개 파일을 `<PROJECT>`의 동일 상대 경로와 SHA-256으로 다시 대조했다.

- 상대 경로 누락: 0
- 프로젝트의 추가 런타임 파일: 0
- SHA-256 일치: 1,048
- SHA-256 불일치: `descriptor.mod` 1개

`descriptor.mod`의 차이는 다음과 같다.

| 필드 | `HOK_ORIGINAL` | `<PROJECT>` |
|---|---|---|
| name | 원본 제목 | `[1.19 호환]` 문구가 붙은 계승 작업 제목 |
| supported_version | `1.16.*` | `1.19.*` |
| remote_file_id | `2898629778` | 없음 |

즉, descriptor를 제외한 현재 프로젝트의 모드 콘텐츠는 설치된 원본과 byte-for-byte 동일하다. 이는 복구 시작점의 출처를 확정하지만 `supported_version` 변경이 실제 호환성을 증명하지는 않는다.

### 검증 archive

Steam 관리 폴더를 그대로 불변 기준본으로 보지 않기 위해 다음 snapshot을 별도로 생성했다.

- 경로: `<PROJECT>/.local-artifacts/baselines/HOK_ORIGINAL_2898629778_manifest-6685434440007626210/HOK_ORIGINAL_2898629778_manifest-6685434440007626210.zip`
- ZIP 크기: `70,486,687` bytes
- ZIP SHA-256: `4683E8E2D8BBAAD8AEFA5C1E335DFB6346FEE269300E0FDDE34AEA7F012118F9`
- 원본 입력: 1,049 files / `224,994,293` bytes
- ZIP 항목 대조: missing `0`, extra `0`, SHA-256 mismatch `0`

따라서 이 ZIP과 기록된 ZIP hash는 현재 `HOK_ORIGINAL` snapshot을 재식별할 수 있는 검증 기준이다. 다만 각 1,049개 파일의 상대 경로·크기·SHA-256을 담은 독립적인 per-file manifest 파일은 아직 생성하지 않았다. “archive 및 내용 검증 완료”와 “별도 per-file manifest 미생성”을 혼동하지 않는다.

## 구형 바닐라 `V_OLD`

공식 HoK 업데이트 시점과 로컬 Steam rollback branch 메타데이터를 함께 보면 가장 강한 후보는 HOI4 `1.16.8`이다.

| 항목 | 값 |
|---|---|
| 후보 버전 | `1.16.8` |
| branch build ID | `18550822` |
| 콘텐츠 depot | `394361` |
| 콘텐츠 manifest | `2512503158411563220` |
| Windows depot | `394362` |
| Windows manifest | `4372532302181969559` |

판정 근거:

1. HoK의 마지막 공개 업데이트는 2025-06-02이며 HOI4 1.16 대응을 명시한다.
2. 로컬 Steam appinfo에는 `1.16.8` rollback branch와 build/depot manifest가 존재한다.
3. `1.16.9`는 HoK 업데이트 뒤의 빌드이므로, 업데이트 당시 최신 1.16 계열이라는 시간 조건에는 `1.16.8`이 가장 잘 맞는다.

그러나 정확한 `1.16.8` depot 파일은 로컬에 없다. 별도 디렉터리, 전체 파일 목록, SHA-256 manifest, 실행 체크섬도 확보되지 않았다. 따라서:

- `1.16.8`을 `V_OLD`로 쓰는 선택은 현재 `STRONGLY_SUPPORTED`
- 실제 3-way 파일 비교 입력으로서의 `V_OLD`는 `UNPROVEN / NOT ACQUIRED`
- `INTENDED_DELTA = HOK_ORIGINAL - V_OLD`는 아직 production 맵에 적용할 수 없음

현재 `<HOI4_INSTALL>`을 rollback하거나 덮어쓰지 않았다.

## `Korean Language` 의존성 범위와 충돌

`<STEAM_WORKSHOP>/2743487021`에서 확인한 값:

- Workshop ID / `remote_file_id`: `2743487021`
- version: `25.11.23`
- declared `supported_version`: `1.17.*`
- Steam content manifest: `919612200712679333`
- 총 파일: 301
- 파일 범위:
  - `localisation/`: 194
  - `gfx/`: 102
  - `interface/`: 3
  - `descriptor.mod`, `Thumbnail.png`: 각 1
- `map/` 또는 `history/` 파일: 0

### 직접 맵 원인과 VFS 중첩의 분리

현재 프로젝트와 동일한 상대 경로는 `descriptor.mod`, `Thumbnail.png` 두 개뿐이다. 또한 의존 모드에는 `map/` 또는 `history/` 파일이 없다. 따라서 설치된 의존 모드가 province/state geometry, membership 또는 ID 정의를 직접 덮거나 추가한다는 가설은 이 파일 범위에서는 `DISPROVEN`이다. 이는 `Korean Language`가 기존 `D-PRE` 맵 크래시의 직접 map-data 원인이라는 주장도 지지하지 않는다.

반면 `V_TARGET` 및 HoK와의 VFS/localisation 중첩은 별도로 확인됐다.

| 비교 대상 | CONFIRMED 결과 |
|---|---|
| `Korean Language` ↔ `V_TARGET` 동일 상대 경로 | 총 267개: localisation 186, gfx 78, interface 3 |
| `Korean Language` ↔ HoK 동일 상대 경로 | `descriptor.mod`, `Thumbnail.png` 2개 |
| `Korean Language` ↔ HoK 동일 localisation key | 102개 |
| 위 102개 중 map-ID 형태의 표시 문자열 key | 13개: `STATE_1017`–`STATE_1027`, `VP_13376`, `VP_13378` |

위 13개는 localisation key이지 province/state 정의나 membership 자체가 아니다. 따라서 “ID 이름 문자열 중첩”과 “맵 ID 데이터 충돌”을 같은 것으로 판정하지 않는다.

추가 위험:

- 의존 모드의 state-name localisation 파일은 `STATE_1046`까지만 포함한다. 목표 바닐라의 더 높은 state ID 표시를 완전하게 다룬다고 볼 수 없다.
- `interface/chatfonts.gfx`도 목표 바닐라와 같은 VFS 상대 경로를 가진다. 구형 UI/font 정의가 목표 파일을 override할 가능성이 있다.
- 위 구조적 중첩으로 UI/font/localisation 회귀 위험은 `STRONGLY_SUPPORTED`지만, 실제 누락 문자열·글꼴·UI 파손 여부는 아직 `UNPROVEN`이다.

반면 다음은 별개다.

- HoK descriptor와 공식 Workshop 페이지는 `Korean Language`를 필수로 선언한다: `CONFIRMED`
- 현재 launcher DB와 `dlc_load.json`에는 HoK만 있고 `Korean Language`는 없다: `CONFIRMED`
- 의존 모드가 `1.19.2`에서 UI, 글꼴, localisation을 정상 로드하는지: `UNPROVEN`
- `1.17.*` 선언만으로 `1.19.2` 비호환을 확정할 수 있는지: `UNPROVEN`
- 목표 바닐라의 공식 Korean localisation/font만으로 HoK의 기존 언어 계약을 안전하게 대체할 수 있는지: `UNPROVEN`

## launcher와 현재 선택 상태

`<HOI4_USER_DATA>/mod/hearts of korea.mod`는 `<PROJECT>`가 아니라 현재 존재하지 않는 과거 공백 경로 문자열을 `path`로 가진다. 해당 대상이 존재하지 않는 것과 현재 프로젝트 경로가 다른 것은 직접 확인했다.

Paradox `launcher-v2.sqlite`에서 확인한 active playset:

- 이름: `하츠오브 코리아 테스트`
- load order: custom
- enabled mods: HoK 1개
- HoK position: `0`

`<HOI4_USER_DATA>/dlc_load.json`의 현재 값:

- `enabled_mods`: `mod/hearts of korea.mod` 하나
- `Korean Language`: 미포함
- `disabled_dlcs`: 빈 배열

`launcher-v2.sqlite`의 active playset과 `dlc_load.json`은 HoK 한 개가 활성화된다는 점에서 일치한다. 따라서 playset 이름과 저장된 custom order는 `CONFIRMED`다. 하지만 활성 HoK descriptor의 `path`가 stale 상태이므로, 실제 물리적 로드 성공이나 `<PROJECT>` 로드는 여전히 확인되지 않았다.

`<STEAM_WORKSHOP>/3757430319`도 비활성 잔존 Workshop 항목으로 확인됐다. 현재 active playset이나 `dlc_load.json`에는 없으므로 현재 활성 원인으로 분류하지 않는다. 다만 다음 A/B/C/D 재현에서는 launcher DB, playset 및 실제 로드 목록 모두에서 비활성인지 기록해 이전 모드 조합의 잔존 영향을 격리한다.

## 수행하지 않은 작업

이 기준선 문서 작성 중 다음 작업은 수행하지 않았다.

- `<PROJECT>/map/`, `history/states/` 또는 다른 production 모드 파일 수정
- `<PROJECT>/descriptor.mod` 수정
- `<HOI4_USER_DATA>`의 launcher descriptor, playset, 설정 또는 로그 수정
- `<HOI4_INSTALL>` 또는 `<STEAM_WORKSHOP>` 수정
- HOI4 또는 launcher 실행
- 새 로그·WER 생성
- province/state/strategic-region 영구 ID 마이그레이션
- 구형 맵 폴더 복사 또는 숫자 전역 치환
- Git commit, push, branch 변경 또는 외부 게시

원본 archive 생성과 `.gitignore`의 `/.local-artifacts/` 제외 규칙 추가는 이 기준선에 기록된 진단 산출물 작업이다. 생산 맵, launcher, 게임 실행 상태와 영구 ID는 바뀌지 않았다.

## 다음 승인 게이트

다음 단계는 서로 다른 권한과 호환성 결정을 요구한다.

1. **정확한 `V_OLD` 확보 승인**
   - `1.16.8`의 위 두 depot manifest를 현재 설치와 분리된 위치에 다운로드한다.
   - 다운로드·외부 경로 쓰기·저장 공간 사용이 발생하므로 별도 승인이 필요하다.
   - 파일 목록과 SHA-256 manifest를 만든 뒤에야 3-way 비교를 production 판단에 사용할 수 있다.

2. **원본 증거 manifest 완성**
   - 검증 ZIP과 ZIP SHA-256은 확보됐다.
   - 별도의 1,049개 per-file 경로·크기·SHA-256 manifest를 만들어 archive 검증을 재현 가능하게 고정한다.
   - archive를 프로젝트 밖에 이중 보존하려면 해당 외부 쓰기 위치에 대한 별도 승인을 받는다.

3. **launcher 외부 설정 변경 승인**
   - launcher descriptor가 `<PROJECT>`를 가리키도록 별도 local-mod 등록을 만들거나 기존 항목을 안전하게 교정한다.
   - 선언된 의존 계약을 유지할지, 목표 바닐라의 공식 Korean localisation으로 의도적으로 이관할지 별도 결정한다.
   - 계약을 유지하는 동안 실제 지원 구성에는 `Korean Language`의 경로와 로드 순서를 명시한다.
   - 비활성 잔존 Workshop 항목 `3757430319`이 테스트 playset에 들어오지 않도록 격리한다.

4. **영구 ID 마이그레이션 결정**
   - 3-way 비교와 fresh scan 결과로 province/state별 의미 매핑표를 제시한다.
   - save·submod 호환성 영향을 포함해 개별 old ID → new ID를 승인받는다.
   - 연속 오프셋이나 전역 숫자 치환은 승인 대상으로 제시하지 않는다.

5. **게임 실행 및 재현 승인**
   - 증거 보존 뒤 `A` 바닐라, `B` Korean Language만, `C` HoK + Korean Language, `D` HoK만을 동일 조건으로 실행한다.
   - 각 실행에서 active playset, 실제 로드 목록, `l_korean` 설정 및 잔존 Workshop `3757430319`의 비활성을 기록한다.
   - `B`와 `C`에서는 localisation key, state 이름, `chatfonts.gfx`, UI/font 표시도 검증한다.
   - production 수정 후에는 `D-POST`와 실제 지원 구성 `C-POST`를 별도로 검증한다.

6. **production 맵 구현 승인**
   - `V_OLD`, `HOK_ORIGINAL`, `V_TARGET` 3-way 결과와 승인된 ID 정책이 준비된 뒤, 검토된 `INTENDED_DELTA`만 최소 병합한다.

## 증거 출처

로컬 읽기 전용 출처:

- `<PROJECT>/.git`
- `<PROJECT>/descriptor.mod`
- `<PROJECT>/.local-artifacts/baselines/HOK_ORIGINAL_2898629778_manifest-6685434440007626210/HOK_ORIGINAL_2898629778_manifest-6685434440007626210.zip`
- `<HOI4_INSTALL>/launcher-settings.json`
- `<HOI4_INSTALL>`의 Korean localisation/font inventory
- Steam App ID `394360`의 로컬 App State 및 appinfo branch 메타데이터
- Paradox launcher `launcher-v2.sqlite`의 active playset 및 mod position 기록
- `<HOI4_USER_DATA>/mod/hearts of korea.mod`
- `<HOI4_USER_DATA>/dlc_load.json`
- `<HOI4_USER_DATA>/settings.txt`
- `<HOI4_USER_DATA>/pdx_settings.json`
- `<STEAM_WORKSHOP>/../appworkshop_394360.acf`
- `<STEAM_WORKSHOP>/2898629778/descriptor.mod`
- `<STEAM_WORKSHOP>/2743487021/descriptor.mod`
- `<STEAM_WORKSHOP>/3757430319`의 비활성 잔존 항목 inventory
- 위 두 Workshop 설치본의 전체 파일 inventory와 프로젝트 대조

공식 공개 출처:

- [Hearts of Korea Steam Workshop 항목](https://steamcommunity.com/sharedfiles/filedetails/?id=2898629778)
- [개발자 게시 HoK 1.0.9(1) '강계' 패치노트](https://steamcommunity.com/workshop/filedetails/discussion/2898629778/601906153570468116/)

## 현재 결론

현재 작업 복사본은 descriptor를 제외하면 설치된 원본 HoK manifest의 콘텐츠와 정확히 일치하고, 검증된 원본 ZIP snapshot도 확보됐다. 목표 설치본은 HOI4 `1.19.2.0.a729 (d245)`로 확정됐다. active playset은 `하츠오브 코리아 테스트`이며 launcher DB와 `dlc_load.json` 모두 HoK 한 개만 활성화된 상태를 가리킨다. 그러나 HoK descriptor가 stale 경로를 사용하므로 현재 프로젝트의 실제 로드는 확인되지 않았고, 선언된 필수 `Korean Language`도 활성화되지 않았다.

`Korean Language`에는 직접 map/history 데이터가 없어 맵 크래시의 직접 원인으로 보이지 않지만, 목표 바닐라와 267개 상대 경로가 겹치고 HoK와 102개 localisation key가 겹쳐 UI/font/localisation 호환성 사건으로는 별도 검증이 필요하다. `V_OLD = 1.16.8`은 가장 강한 후보지만 실제 파일이 없으므로 3-way 맵 이식은 아직 production 적용 단계가 아니다. 다음 안전한 구현 경계는 정확한 `V_OLD`와 per-file manifest 확보, launcher 지원 구성 및 언어 의존 계약 확정, 그리고 개별 ID 마이그레이션 승인이다.
