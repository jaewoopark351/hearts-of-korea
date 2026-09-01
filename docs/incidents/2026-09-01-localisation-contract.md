# 2026-09-01 HoK localisation 언어 계약 조사

## 범위와 현재 판정

- 작업 모드: **Documentation / Diagnostic review**
- 대상: Hearts of Korea, HOI4 `1.19.2.0.a729 (d245)`, 설치된 `Korean Language` 후보
- production localisation 수정: **수행하지 않음**
- 게임 실행: **수행하지 않음**
- 정책 결정: **PENDING**

이 사건은 시작 크래시의 맵 데이터 사건과 분리한다. 현재 증거는 localisation 구조와 의존 계약의 검증 필요성을 보여 주지만, `l_english`를 `l_korean`으로 일괄 변경해야 한다는 결론이나 시작 크래시의 직접 원인을 증명하지 않는다.

관련 문서:

- [시작 크래시 사건](2026-08-31-startup-crash.md)
- [환경 기준선](../baselines/2026-08-31-environment-baseline.md)
- [크래시 디버깅 런북](../CRASH_DEBUGGING_RUNBOOK.md)

## CONFIRMED

1. 현재 HoK localisation `.yml`은 19개다.
2. 19개 모두 `localisation/english/` 아래에 있고 파일명이 `*_l_english.yml`이다.
3. 19개 모두 UTF-8 BOM을 가지며 첫 language header는 trim 기준 `l_english:`다. `korea_equipment_l_english.yml` 한 파일의 header 끝에는 공백 1개가 있다.
4. 19개 모두 Hangul 문자열을 포함한다.
5. 현재 HOI4 사용자 설정은 `settings.txt`와 `pdx_settings.json` 모두 `l_korean`이다.
6. 목표 Vanilla `1.19.2`에는 `localisation/korean/` 아래 `l_korean` `.yml` 206개와 Korean font 자산이 있다.
7. 설치된 `Korean Language` 후보는 version `25.11.23`, declared `supported_version = 1.17.*`이며 localisation 194개, gfx 102개, interface 3개를 포함한다.
8. `Korean Language`와 HoK는 102개 localisation key가 겹친다. 이 중 13개는 `STATE_1017`–`STATE_1027`, `VICTORY_POINTS_13376`, `VICTORY_POINTS_13378`처럼 map ID 형태의 표시 key다.
9. `Korean Language`에는 `map/`과 `history/` 파일이 없다.

## STRONGLY_SUPPORTED

- HoK의 Korean 문자열이 `l_english` namespace에 놓인 구조와 필수 dependency 선언은 legacy `Korean Language` 로드 계약을 전제로 했을 가능성과 일치한다.
- dependency가 target과 270개 동일 상대 경로(localisation 189, gfx 78, interface 3)를 가지므로 `1.19.2`에서 UI·font·localisation 회귀 위험이 있다.

이 두 판단은 실제 loader 순서와 화면 표시를 아직 관찰하지 않았으므로 `CONFIRMED`로 올리지 않는다.

## UNPROVEN

- `l_korean` 실행에서 HoK의 `l_english` 파일이 실제로 로드·fallback·override되는 방식
- HoK 단독 구성과 dependency 포함 구성에서 19개 파일의 key가 실제 화면에 표시되는지
- 겹치는 102개 key의 최종 승자와 의도한 문자열 보존 여부
- `interface/chatfonts.gfx` override가 `1.19.2` UI와 font를 깨뜨리는지
- dependency의 `supported_version = 1.17.*` 선언이 실제 `1.19.2` 비호환을 의미하는지
- 목표 Vanilla의 native Korean만으로 기존 HoK 계약을 대체할 수 있는지
- 공식 Korean localisation이 처음 도입된 정확한 HOI4 버전

## 시작 크래시와의 관계

설치된 dependency가 map/state 데이터의 직접 공급원이라는 가설은 정적 파일 범위에서 `DISPROVEN`이다. dependency에는 `map/`과 `history/` 파일이 0개다. 반면 dependency 미활성이 UI·font·localisation 또는 다른 비맵 경로에서 시작 과정에 기여했는지는 `UNPROVEN`이며 A/B/C/D 실행으로만 분리한다.

따라서 이 사건의 파일을 바꾸어 province `13410–13413`, state ID `1017–1027`, 중복 membership 또는 WER `c0000409`를 고쳤다고 주장하지 않는다.

## 정책 선택지 — 미승인

### Legacy dependency 유지

- 기존 `l_english` 경로·header·key와 `Korean Language` dependency를 유지한다.
- 실제 지원 구성 `C`에서 load order, Korean 문자열, state 이름, font와 UI를 검증한다.
- dependency의 target-version override 위험을 감수하므로 `1.19.2` runtime PASS가 필요하다.

### Native `l_korean` 이관

- dependency 제거 또는 축소를 포함하는 별도 migration으로 취급한다.
- key를 안정적으로 보존하고 파일명·header·디렉터리·BOM을 함께 설계한다.
- target native key와 중복되는 항목의 precedence를 검토하고 HoK 단독 `D`에서 전 화면을 검증한다.

### Dual 제공

- 동일 key의 중복 등록과 언어별 divergence 위험이 있으므로 파일 복제로 자동 생성하지 않는다.
- 지원 언어·fallback 정책, 생성 원본과 동기화 방식을 먼저 승인한다.
- 양쪽 언어 구성과 dependency 유무를 별도 테스트한다.

## 안전 게이트

1. 맵 크래시 수정과 localisation migration을 같은 patch로 섞지 않는다.
2. 정책 승인 전에는 19개 파일을 일괄 rename·이동·header 치환·복제하지 않는다.
3. generic YAML formatter를 사용하지 않고 UTF-8 BOM, `KEY:0 "Text"`, `$KEY$`, 색·아이콘 token과 escape를 보존한다.
4. 정적 key·BOM·header 검사 뒤 `B`(dependency only), `C`(HoK + dependency), `D`(HoK only)를 필요한 정책에 맞춰 clean start로 실행한다.
5. 실제 화면에서 Korean 문자열, state·victory-point 이름, font, UI clipping과 missing key를 확인한다.
6. 선택한 정책과 무관하게 기존 localisation key의 변경은 별도 호환성 검토를 받는다.

## 현재 결론

Paradox localisation 언어 계약은 아직 손대지 않은 것이 맞다. 이는 누락이 아니라 의도적인 안전 정지다. 현재 최우선인 맵 시작 크래시의 원인 분류를 유지하면서, 언어 계약은 runtime 증거와 정책 승인 뒤 별도 migration으로 처리한다.
