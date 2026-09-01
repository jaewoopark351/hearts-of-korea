# 2026-09-01 fresh 맵 격리 사건

## 문서 판정

> 이 문서의 `NOT APPROVED` 표기는 fresh 진단 당시의 역사적 상태다. 이후 사용자가 target-native production 구현과 persistent ID 마이그레이션을 명시적으로 승인했고 정적 구현이 적용됐다. 후속 상태는 [2026-09-01 target-native 맵 구현 기록](2026-09-01-target-native-map-implementation.md)을 따른다.

- 작업 모드: **Diagnostic documentation**
- 대상: HOI4 `1.19.2.0.a729`, Hearts of Korea 시작 crash
- production source 수정: **수행하지 않음**
- 실행된 controls: `A-FRESH`, `D-FRESH`, `D-NOMAP`
- 아직 실행하지 않은 control: `D-MAPONLY`
- 실제 지원 구성 `C`: **NOT RUN**
- root-cause family: **STRONGLY_SUPPORTED — HoK map/state bundle**
- 정확한 proximate engine failure: **UNPROVEN**
- production map implementation: **NOT APPROVED**
- persistent province/state ID migration: **NOT APPROVED**

이 문서는 [2026-08-31 시작 크래시 조사](2026-08-31-startup-crash.md)의 후속 사건이다. 이전 사건의 stale launcher 경로 문제를 해소한 뒤 현재 저장소를 실제로 로드해 fresh control을 수집했다.

맵 재구성 후보와 승인 게이트는 [Hearts of Korea 1.19.2 맵 재구성 설계](../HOK_MAP_RECONSTRUCTION_PLAN.md)에 분리해 기록한다.

## 1. 환경과 물리 경로

경로 별칭:

- `<PROJECT>`: `C:\hoi\hearts_of_korea`
- `<D_NOMAP>`: `C:\hoi\hearts_of_korea_d_nomap`
- `<D_MAPONLY>`: `C:\hoi\hearts_of_korea_d_maponly`
- `<HOI4_INSTALL>`: `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`
- `<HOI4_USER_DATA>`: `C:\Users\<USER>\OneDrive\문서\Paradox Interactive\Hearts of Iron IV`

기준 정보:

- Git branch: `main`
- Git HEAD: `91e1a7b62d046ba209fc6e35c0e405c65e07355a`
- 게임: Operation Postern `1.19.2.0.a729`
- 바닐라 checksum: `d245`
- 실행에서 확인된 active DLC: 36개
- 시스템 언어: Korean
- HoK descriptor의 선언된 dependency: `Korean Language`
- 아래 fresh `D`와 `D-NOMAP` 실행에는 `Korean Language`가 활성화되지 않음

## 2. Launcher 경로 정합성

사용자의 명시적 승인 뒤 launcher descriptor가 현재 저장소를 가리키도록 수정됐다.

- 이전 path: `C:/hoi/hearts of korea`
- 수정 path: `C:/hoi/hearts_of_korea`
- 이전 descriptor SHA-256: `633C768D976054AE144DEAE0A39CD7390A28E204443634FAFD215D0BC5125B83`
- 수정 descriptor SHA-256: `A4975CDD6D2261AB1F62596A8F9F3A193A8F93F4BC89FBA737987FDEC41C76C5`
- 이전 파일 보존 위치: `<PROJECT>/.local-artifacts/incidents/2026-09-01-fresh-debug/hearts of korea.mod.before`

`D-FRESH` bundle에는 실제 실행에 사용된 launcher descriptor가 포함돼 있다. 따라서 `D-PRE`와 달리 이번 실행은 현재 `<PROJECT>`를 로드했다는 물리 경로 증거를 가진다.

## 3. 실행 행렬

| 실행 ID | 활성 구성 | 실행 방식 | 결과 |
|---|---|---|---|
| `D-FRESH-2026-09-01` | HoK only | `hoi4.exe --debug` | 시작 crash |
| `A-FRESH-2026-09-01` | vanilla only | `hoi4.exe --debug` | startup 완료, exit 0 |
| `D-NOMAP-FRESH-2026-09-01` | HoK without `map/` and `history/states/` | launcher, `--debug` 아님 | startup/session change 완료, 새 crash 없음 |
| `D-MAPONLY` | HoK `map/` + `history/states/` only | 미실행 | `NOT RUN` |
| `C` | HoK + `Korean Language` | 미실행 | `NOT RUN` |

한 실행의 로그와 다른 실행의 crash/WER을 섞지 않는다. 각 결과는 아래 bundle에 한정한다.

## 4. `D-FRESH-2026-09-01`

### 구성

- process start: `2026-09-01 14:35:02.823 KST`
- launch arguments: `--debug`
- active mods: HoK 1개
- active DLC: 36개
- 실제 launcher path: `<PROJECT>`
- loaded provinces: 13,410개

### 관찰된 실패 경계

`game.log`:

1. defines 4,469개 로드
2. province 13,410개 로드
3. Resetting game
4. 첫 history 구간 `-1.1.1.1 → 2.1.1.1` 실행
5. 두 번째 history 구간 완료 전에 crash

`error.log`의 earliest map family:

- state ID `1017–1027` conflict 11건
- target state가 참조하는 province `13410–13413` malformed
- land province의 state 누락·중복
- province의 strategic region 누락·중복
- target 동남아시아·중국 등 province와 HoK 한국 province의 ID 의미 충돌

### Crash bundle

- Paradox crash directory: `hoi4_20260901_143524`
- local crash time: `2026-09-01 14:35:24 KST`
- exception: `C0000005 EXCEPTION_ACCESS_VIOLATION`
- exception address: `0x00007FF62DFDC7F6`
- `IsMapInGoodState: no`
- launch arguments: `--debug`
- HasMods: true

이 crash는 이전 `D-PRE`의 `BEX64 / c0000409 / +0x253C715`과 서명이 다르다. 동일한 root-cause family일 수 있지만 같은 proximate engine failure라고 단정하지 않는다.

### 증거 위치

- `<PROJECT>/.local-artifacts/incidents/2026-09-01-fresh-debug/D-FRESH-2026-09-01/`
- `<PROJECT>/.local-artifacts/incidents/2026-09-01-fresh-debug/D-FRESH-2026-09-01-CRASH/`

## 5. `A-FRESH-2026-09-01`

### 구성

- process start: `2026-09-01 14:46:55.445 KST`
- launch: `hoi4.exe --debug`
- active mods: 0
- active DLC: 36개
- loaded provinces: 13,414개

### 결과

- 두 history 구간 완료
- startup 완료: `2026-09-01 14:47:23 KST`
- 60초 이상 생존
- `CloseMainWindow` 정상 처리
- exit code: `0`
- 새 Paradox crash bundle, WER, local CrashDump, Application Error 없음

판정: 같은 HOI4 설치본과 DLC 집합의 vanilla startup control은 `PASS`다. 게임 설치 자체가 `D-FRESH`와 같은 경계에서 crash한다는 가설은 현재 범위에서 반증된다.

### 증거 위치

- `<PROJECT>/.local-artifacts/incidents/2026-09-01-fresh-debug/A-FRESH-2026-09-01-PRE/`
- `<PROJECT>/.local-artifacts/incidents/2026-09-01-fresh-debug/A-FRESH-2026-09-01/`

## 6. `D-NOMAP-FRESH-2026-09-01`

### 진단 복사본 정의

`D-NOMAP`은 현재 HoK에서 다음만 제외한 진단 복사본이다.

- `map/` 전체
- `history/states/` 전체

나머지 HoK runtime content는 유지한다.

- `common/`
- `events/`
- `gfx/`
- `history/countries/`
- `history/general/`
- `history/units/`
- `interface/`, `localisation/`, `music/`, `portraits/`, `sound/`

retained files는 main project 대응 파일과 SHA-256이 일치한다.

- retained files: 996개
- retained bytes: 150,279,776
- manifest: `<PROJECT>/.local-artifacts/diagnostic-variants/manifests/2026-09-01-D-NOMAP.tsv`
- manifest SHA-256: `51BE51511BAB27F0965475C34741E16D64D3A5921CF206C83CE9CD2ACAB50EF9`

### 실행 결과

- active mod: `하츠 오브 코리아 Hearts of Korea hearts_of_korea_d_nomap` 1개
- active DLC: 36개
- loaded provinces: 13,414개
- 두 history 구간 완료
- startup time 기록: `2026-09-01 15:13:06 KST`
- session change 기록: `2026-09-01 15:13:08 KST`
- capture 시점에 `hoi4.exe` process 없음
- 새 Paradox crash bundle, WER, local CrashDump, Application Error 없음

제한:

- launcher 사용자 실행으로 정확한 process exit code를 수집하지 못했다.
- `memory.log`와 `system_debug.log`가 비어 있어 `--debug` 없이 실행된 것으로 보인다.
- 따라서 `D-FRESH --debug`와 완전히 같은 harness의 `PASS`로 표현하지 않는다.

그럼에도 원래 history crash 경계를 넘었고 map 오류가 사라졌으므로, HoK map/state bundle이 `D-FRESH` crash에 필요한 기여 요인이라는 판정은 `STRONGLY_SUPPORTED`다.

### 한국이 사라진 이유

사용자 관찰대로 `D-NOMAP`에서는 HoK 한국 영토가 사라진다. 이는 진단 복사본의 예상 동작이다.

- HoK `history/countries/KOR - Korea.txt`는 `capital = 1017`을 사용한다.
- HoK state를 제외하면 target state `1017`은 한국이 아니다.
- target 한국 state `525`, `527`, `1028–1031`은 1936년에 JAP owner, KOR core다.
- HoK가 KOR owner와 custom state 분할을 제공하지 않으므로 KOR은 한국 영토를 가지지 않는다.

`D-NOMAP`에 맵을 다시 넣어 정상 모드로 바꾸지 않는다. 이 복사본은 map/state가 없는 control로 유지한다.

### 증거 위치

- `<PROJECT>/.local-artifacts/incidents/2026-09-01-fresh-debug/D-NOMAP-FRESH-2026-09-01/`

## 7. `D-MAPONLY` 준비 상태

`D-MAPONLY`는 다음만 포함한 진단 복사본이다.

- `map/`
- `history/states/`
- `descriptor.mod`

manifest:

- retained files: 51개
- retained bytes: 71,719,029
- `<PROJECT>/.local-artifacts/diagnostic-variants/manifests/2026-09-01-D-MAPONLY.tsv`
- SHA-256: `C1E120314A8C88CBE935C76F94F8D0D9BD6CB1189DFC7F43F9784E7BFFE39BB7`

현재 상태는 `READY / NOT RUN`이다. 실행하면 HoK map/state bundle이 다른 HoK content 없이도 crash 경계를 만드는지 확인할 수 있다. 단, 실행 전에 live 로그가 덮어써지므로 이전 run bundle이 검증됐는지 확인하고 다른 모드를 모두 비활성화해야 한다.

## 8. 통합 증거 archive

`A-FRESH`와 `D-FRESH` 증거는 다음 archive로 통합 보존했다.

- archive: `<PROJECT>/.local-artifacts/archives/2026-09-01-A-D-startup-evidence.zip`
- SHA-256: `9504B75F143DBA15399A7AB588FD2B7DFAD06F0380BA88994DAFE37557D7DEC1`
- manifest: `<PROJECT>/.local-artifacts/archives/2026-09-01-A-D-startup-evidence.manifest.tsv`
- manifest entries: 48개
- verification: `PASS`

## 9. 원인 분류

### CONFIRMED

1. 현재 저장소 HoK only `D-FRESH`가 1.19.2 history 초기화 중 crash했다.
2. `D-FRESH`가 로드한 province는 13,410개이며 target보다 4개 적다.
3. `D-FRESH`에는 state `1017–1027` conflict와 province `13410–13413` malformed가 있다.
4. crash metadata가 `IsMapInGoodState: no`를 기록했다.
5. vanilla `A-FRESH`는 province 13,414개를 로드하고 startup과 정상 종료를 완료했다.
6. `D-NOMAP`은 province 13,414개, 두 history 구간, startup과 session change까지 도달했다.
7. `D-NOMAP`에는 원래 map family 오류가 없다.
8. `D-NOMAP`에 비맵 오류가 남았지만 이번 startup 경계를 막지 않았다.

### STRONGLY_SUPPORTED

1. HoK의 구형 global map과 state bundle이 target 1.19.2 데이터와 부분 합성되며 `D-FRESH` startup crash에 기여한다.
2. 안전한 복구에는 target-first province/state 재구성과 persistent ID migration이 필요하다.
3. 누락된 `13410–13413` 네 definition 행만 추가하는 방식은 전체 원인을 해결하지 못한다.

### UNPROVEN

1. `D-FRESH`의 exact dereference를 일으킨 단일 엔진 invariant 또는 데이터 행
2. map/state bundle만으로 crash가 충분한지 — `D-MAPONLY` 미실행
3. 수정 뒤 `D-POST`와 실제 지원 구성 `C-POST`의 결과
4. `Korean Language`의 1.19.2 runtime UI/font/localisation 호환성
5. `V_OLD`가 없는 상태에서 HoK 전역 bitmap 차이 중 원작자가 의도한 정확한 delta
6. 기존 save와 submod를 위한 persistent ID 호환성

### 현재 범위에서 반증

- 게임 설치 자체가 같은 startup 경계에서 항상 crash한다는 가설
- 다른 Workshop 모드가 반드시 있어야 crash한다는 가설
- `Korean Language`가 map/history 파일을 직접 제공해 이 map geometry 충돌을 만든다는 가설

## 10. 다음 게이트

진단 선택지:

1. `D-MAPONLY`를 단독으로 한 번 실행하고 즉시 로그·crash를 보존한다.
2. `D-NOMAP --debug`를 동일 harness로 재실행해 exit code를 수집한다.

맵 구현 전 결정:

1. 정확한 `V_OLD`를 확보할지, target-native reconstruction을 명시적으로 선택할지
2. HoK province 34개의 개별 old ID → new ID 매핑
3. 한국 9개와 주변 4개 state의 의미 매핑
4. save/submod 호환성 정책
5. production map implementation 승인

실제 지원 구성:

1. `Korean Language` 경로·버전·load order 확정
2. 수정 후 `D-POST` 증거 보존
3. 실제 지원 구성 `C-POST` 증거 보존

## 11. 변경 영향

이 사건 과정에서 launcher descriptor와 별도 diagnostic 복사본은 사용자의 명시적 승인으로 변경·생성됐다. 원본 game installation, Workshop-managed HoK, production `<PROJECT>/map/`, `<PROJECT>/history/states/`와 gameplay script는 수정하지 않았다.

이번 문서 갱신에서는 Markdown 문서만 변경했다. HOI4를 실행하거나 launcher/playset/log를 추가 변경하지 않았고, Git commit·push·Workshop 업로드도 수행하지 않았다.
