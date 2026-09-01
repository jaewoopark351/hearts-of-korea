# 2026-09-01 HoK dual localisation migration

## 범위와 현재 판정

- 작업 모드: **Implementation / static validation complete / runtime validation pending**
- 대상: Hearts of Korea, HOI4 `1.19.2.0.a729`, 게임 언어 `l_korean`
- 확인된 실행 구성: **HoK 단독 활성화**
- production localisation 수정: **수행함 — 기존 English 채널을 보존하고 Korean 채널을 추가함**
- 정책 결정: **APPROVED — 사용자가 `_l_english`를 남겨 두고 복사해 `l_korean`으로 작성하도록 승인함**
- post-migration 게임 실행: **NOT RUN — 현재 실행 중이던 프로세스는 새 파일 생성 이전에 시작됨**
- `Korean Language` dependency 제거·축소: **수행하지 않음 — 별도 migration 대상**

이 사건은 state ID와 맵 크래시 사건에서 분리한다. 이번 작업은 한국어가 raw localisation key로 표시되는 문제만 대상으로 하며, province·state·전략 지역·보급망 또는 게임플레이 정의를 변경하지 않는다.

관련 문서:

- [시작 크래시 사건](2026-08-31-startup-crash.md)
- [중국·일본 정렬 구현 기록](2026-09-01-china-japan-vanilla-alignment-implementation.md)
- [환경 기준선](../baselines/2026-08-31-environment-baseline.md)
- [크래시 디버깅 런북](../CRASH_DEBUGGING_RUNBOOK.md)

## 재현 증거와 원인

### CONFIRMED

1. 현재 게임 언어는 `l_korean`이다.
2. 재현 당시 활성 모드는 HoK 하나뿐이었다.
3. 한국 중점 화면에서 `KOR_future_of_the_republic`, `KOR_democracy_advance_forward` 등 raw key가 표시됐다.
4. 해당 key와 한국어 표시 문자열은 HoK의 기존 `localisation/english/*_l_english.yml` 파일에 존재하지만, 재현 당시 `l_korean` 채널에는 대응 파일이 없었다.
5. 따라서 이번 HoK 단독 재현에서 한국어가 보이지 않은 직접 원인은 **게임의 활성 언어 채널 `l_korean`과 HoK localisation 등록 채널 `l_english`의 불일치**다.

사전 수정 실행 증거는 다음 불변 bundle에 보존했다.

- 경로: `.local-artifacts/incidents/2026-09-01-localisation/D-LOC-RAW-214500-LIVE/`
- bundle manifest SHA-256: `da871fa9eca7d35528a6484b3f7a33860ef8c83e82db9cca7643d38e9e241736`

이 판정은 localisation 표시 문제에 한정한다. 기존 맵 크래시의 원인이나 `Korean Language` 전체 호환성을 이 증거로 판단하지 않는다.

## 수정 전 기준선

- 현재 source localisation은 **18개**다.
- 과거 조사 문서의 19개 수치는 당시 snapshot 기준이다. 중국·일본 바닐라 정렬 작업에서 republican Japan localisation이 별도 승인 아래 제거되어 현재는 18개다.
- 18개 모두 `localisation/english/` 또는 그 아래 `replace/`에 있었다.
- 파일명 suffix는 `_l_english.yml`, language header는 `l_english:`였다.
- 기존 파일은 UTF-8 BOM을 사용한다.
- 설치된 `Korean Language` 후보는 `supported_version = 1.17.*`인 legacy dependency다. 이번 HoK 단독 표시 수정에 이를 활성화하거나 그 파일을 복사하지 않았다.

## 승인된 dual localisation 정책

이번 migration의 채널 계약은 다음과 같다.

| 채널 | 역할 | 상태 |
| --- | --- | --- |
| `localisation/english/**/*_l_english.yml` | 기존 legacy English 채널과 과거 dependency 계약 보존 | 유지 |
| `localisation/korean/**/*_l_korean.yml` | HOI4 `1.19.2`의 native Korean 언어 선택에서 HoK 문자열 제공 | 신규 추가 |

기존 key 이름과 한국어 표시 문자열을 유지한다. Korean 채널은 English 채널과 같은 상대 디렉터리 구조를 가지며, `replace/` 파일도 동일하게 대응시킨다. 이 작업은 `Korean Language` dependency를 descriptor에서 제거하거나 그 dependency의 UI·font override를 승인한 것이 아니다.

## 구현 내용

1. 기존 English localisation 18개를 삭제·이동·rename하지 않고 보존했다.
2. `localisation/korean/` 아래에 대응 Korean localisation 18개를 추가했다.
3. 각 Korean 파일명 suffix를 `_l_korean.yml`로 변경했다.
4. 각 Korean 파일의 language header를 `l_korean:`으로 변경했다.
5. `localisation/english/replace/`에 대응하는 파일은 `localisation/korean/replace/`에 배치했다.
6. Korean 파일도 UTF-8 BOM을 유지했다.
7. key와 게임에 표시되는 문자열은 English 채널과 Korean 채널 사이에서 1:1로 보존했다.
8. `korea_equipment_l_english.yml`의 기존 `l_english:` header 뒤 후행 공백을 제거하고, 대응 Korean 파일도 공백 없는 정확한 `l_korean:` header로 작성했다.

복제 과정에서 현재 엔진이 문자열 경계를 잘못 해석할 수 있는 unescaped inner quote 5쌍을 네 줄에서 escape했다. 이 변경은 따옴표를 화면에서 없애거나 문구를 바꾸지 않고 `\"`로 명시해 같은 문자열을 안전하게 등록하기 위한 것이다.

- `korea_event_l_english.yml`: 4행, 80행
- `korea_focus_l_english.yml`: 255행
- `korea_ideas_l_english.yml`: 8행
- 각 대응 `_l_korean.yml` 파일에도 같은 escape를 적용함

## 정적 검증

현재 정적 결과:

- English 파일: 18
- Korean 대응 파일: 18
- English key: 1,856
- Korean key: 1,856
- 양 채널 key set 차이: 0
- 각 채널 내부 duplicate key: 0
- Korean 파일명 suffix 오류: 0
- Korean language header 오류: 0
- Korean UTF-8 BOM 누락: 0
- `replace/` 상대 경로 불일치: 0
- English/Korean localisation body 불일치: 0
- target 1.19.2 native Korean key와 겹치는 key: 79, 모두 `replace/`의 의도된 override
- `replace/` 밖의 target native Korean key 충돌: 0
- `tests/test_localisation_contract.py`: 5 tests, `PASS`
- Korean tree manifest: `.local-artifacts/audits/2026-09-01-dual-localisation/SHA256SUMS.tsv`
- manifest SHA-256: `A550070DA2CF76681C7F0DFD267CDD6B9B5AE19DD5A34F687F9FAA027AD2BF4C`
- manifest verification: 18 files, 260,876 bytes, mismatch 0

추가된 계약 테스트는 다음을 검사한다.

- English 18개와 Korean 18개의 상대 경로 대응
- UTF-8 BOM과 정확한 language header
- header를 제외한 body의 byte-level 동등성
- unescaped inner quote 부재
- 채널별 duplicate key 부재

따라서 파일 복제와 채널 등록 구조는 정적으로 일치한다. 정적 일치는 실제 loader 등록, 화면 렌더링 또는 모든 문자열의 UI 적합성을 증명하지 않는다.

## 런타임 검증 상태

post-migration 런타임은 아직 실행하지 않았다. 새 Korean 파일을 만든 시점에 열려 있던 HOI4 프로세스는 수정 전 파일 집합으로 시작되었으므로 그 화면이나 로그를 post-migration 증거로 사용하지 않는다. console/hot reload도 최종 판정으로 사용하지 않는다.

다음 clean-start 검증이 필요하다.

1. HOI4 프로세스를 완전히 종료한다.
2. 게임 언어 `l_korean`, HoK 단독 구성으로 다시 시작한다.
3. 대한민국으로 새 게임을 시작하고 중점 화면을 연다.
4. 기존에 보였던 `KOR_*` raw key가 한국어 중점명으로 바뀌었는지 확인한다.
5. 국가명·정당·인물·중점·이벤트·결정·아이디어·장비·state 이름에서 대표 key를 확인한다.
6. font 누락, 네모 문자, 잘림, `$KEY$`·아이콘 token 노출과 새 localisation 오류를 확인한다.
7. post-migration 로그와 화면 증거를 별도 사건 bundle로 보존한다.

이 검증이 통과하기 전 상태는 다음과 같다.

- locale channel mismatch 원인: `CONFIRMED`
- dual 파일 구조와 key 대응: `CONFIRMED` by static validation
- 실제 한국어 화면 복구: `UNPROVEN / NOT YET RUN`
- `Korean Language` 포함 구성 호환성: `UNPROVEN / NOT RUN`

## 남은 위험과 별도 결정

- English와 Korean 두 사본은 이후 한쪽만 수정하면 divergence할 수 있다. localisation 변경 시 양 채널 key·표시 문자열 동기화 검사를 유지해야 한다.
- 설치된 `Korean Language`는 `1.17.*` legacy 구성이므로 이를 포함하는 지원 playset은 HoK 단독과 별도로 검사해야 한다.
- dependency 제거, descriptor dependency 변경, native font/UI 전환은 이번 승인 범위가 아니다.
- 동일 key를 dependency와 HoK가 함께 제공할 때의 최종 승자와 load order는 `C` 구성 runtime 증거가 필요하다.
- 모든 화면과 장문 event description의 clipping·escape 렌더링은 정적 key 비교만으로 확인할 수 없다.

## 현재 결론

사용자 승인에 따라 기존 `_l_english` 18개를 유지하면서 동일한 Korean 채널 18개를 추가했다. HoK 단독 `l_korean` 실행에서 raw 중점 key가 보인 직접 원인은 locale channel mismatch로 확인됐고, 정적 파일·key·BOM·header 대응은 통과했다. 다만 새 파일이 로드되는 완전 재시작을 아직 수행하지 않았으므로 실제 한국어 표시 복구를 runtime `PASS`로 선언하지 않는다.
