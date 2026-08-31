# 크래시 디버깅 런북

## 목적

같은 크래시를 같은 조건에서 재현하고, 한 번에 하나의 변수만 바꾸며, 로그의 오류와 실제 종료 원인을 구분한다.

이 런북은 하츠 오브 코리아 계승·복구 프로젝트의 호환성 조사에 사용한다. 원본 모드의 의도와 콘텐츠를 보존하되, 구버전 바닐라 데이터와 원작자가 실제로 변경한 데이터를 구분하지 않은 채 현재 버전에 덮어쓰지 않는다.

## 1. 프로젝트 전제와 작업 권한

하츠 오브 코리아는 원본 Workshop 항목을 그대로 덮어쓰는 유지보수 포크가 아니라, 원본을 계승·복구해 별도의 새 Workshop 항목으로 배포할 프로젝트다.

- 원본 Workshop ID `2898629778`은 출처·역사·크레딧 확인용이다.
- 원본 `remote_file_id`를 신규 계승판의 업로드 대상으로 재사용하거나 원본 항목을 덮어쓰지 않는다.
- 원 제작자와 기존 기여자의 크레딧을 보존한다.
- 계승·재게시 권한이 있다는 프로젝트 전제 자체를 매 작업마다 다시 문제 삼지 않는다.
- 다만 실제 게시·업데이트·메타데이터 변경은 사용자가 그 행동을 명시적으로 지시했을 때만 수행한다.

시작 전에 현재 작업 단계를 하나로 고정한다.

| 단계 | 허용 범위 |
|---|---|
| Review | 제공된 문서·코드·증거를 읽고 판정한다. 파일 수정, 실행, Git 변경은 하지 않는다. |
| Diagnostic | 로그·파일을 읽고 비교한다. 명시적으로 허가된 최소·한정 instrumentation 외에는 동작을 바꾸지 않는다. |
| Migration Decision | 영구 ID, 맵 토폴로지, 세이브·서브모드 호환성에 대한 매핑안과 영향을 검토한다. production 파일은 아직 수정하지 않는다. |
| Implementation | 승인된 원인과 승인된 매핑에 한해 최소 변경을 적용한다. |
| Validation | 수정 전과 동일한 조건 및 실제 지원 구성에서 정적·런타임 검증을 수행한다. |
| Release | 검증된 빌드를 패키징하고, 별도의 명시적 지시가 있을 때만 새 Workshop 항목에 게시한다. |

한 단계의 승인은 다음 단계를 자동 승인하지 않는다. 특히 일반 Implementation 승인, 영구 province/state/region ID 마이그레이션 승인, Steam Workshop 게시 승인은 서로 별개다.

## 2. 기준 상태와 불변 기준선

재현 전에 아래 정보를 [증거 기록 양식](EVIDENCE_RECORD_TEMPLATE.md)에 남긴다.

- HOI4 버전, 빌드, 체크섬
- 저장소 절대 경로, Git branch/commit/dirty 상태 또는 Git 저장소가 아니라는 결과
- 모드 descriptor의 `supported_version`
- 저장소 `descriptor.mod`와 launcher `.mod`의 `dependencies`, `replace_path`, `remote_file_id`, `path`
- 저장소, 로컬 개발 모드, Workshop 다운로드의 물리 경로와 런처가 실제로 읽는 복사본
- 런처 playset 이름, 활성 모드와 정확한 로드 순서
- 필수 의존 모드 활성 여부와 정확한 버전·물리 경로
- 활성 DLC 목록
- 언어 설정과 `Korean Language` 의존 계약
- 시작 방식과 사용한 실행 옵션
- 테스트 시작 시각
- 이전 로그인지 이번 실행 로그인지 구분할 수 있는 파일 수정 시각
- 실제 HOI4 user-data 디렉터리와 그 경로를 선택한 근거

활성 모드 목록은 추정하지 않는다. 런처 설정과 실제 로드 로그를 함께 확인한다. `supported_version` 문자열은 목표 기록일 뿐 호환성 증거가 아니며, `replace_path`가 있으면 모든 항목과 가려지는 바닐라 범위를 감사한다. 중복 또는 오래된 데이터를 숨기기 위한 광범위한 `replace_path`를 추가하지 않는다.

### 2.1 맵 또는 바이너리 파일 수정 전 필수 기준선

`provinces.bmp`, `heightmap.bmp`, `terrain.bmp`처럼 일반 텍스트 diff로 복구하기 어려운 파일을 수정하기 전에 다음을 확보한다.

1. 원본 Hearts of Korea 배포본의 읽기 전용 archive
2. 원본 archive 전체의 파일 목록과 SHA-256 manifest
3. 실제 작업용 별도 복사본
4. 정확한 마지막 지원 바닐라 기준본
5. 현재 목표 바닐라 기준본
6. 필수 의존 모드 기준본
7. Git 저장소의 baseline commit 또는 그와 동등한 불변 snapshot

현재 작업 폴더가 Git 저장소가 아니면 그 사실만 기록하고 넘어가지 않는다. 위 기준선이 없으면 맵 Implementation은 `BLOCKED`다. Git 초기화, commit 또는 저장소 구조 변경은 사용자의 별도 승인 없이 수행하지 않는다.

### 2.2 연결 문서 확인

다음 상대 링크가 실제 프로젝트 트리에서 유효한지 확인한다.

- `EVIDENCE_RECORD_TEMPLATE.md`
- `MAP_COMPATIBILITY_CHECKLIST.md`

파일이 없거나 경로가 다르면 누락으로 보고한다. 별도 생성 지시가 없으면 링크를 맞추기 위해 파일을 임의 생성하지 않는다.

## 3. 재현 행렬과 실행 ID

게임 실행이 승인된 경우에만 아래 순서로 시험한다. 각 행은 별도 실행이며, 한 행의 로그를 보존한 뒤 다음으로 넘어간다.

| 기본 실행 ID | 구성 | 목적 |
|---|---|---|
| A | 바닐라만 | 설치와 현재 게임 빌드의 기준 확인 |
| B | 필수 의존 모드만 | 의존 모드 단독 상태 확인 |
| C | Hearts of Korea + 필수 의존 모드 | 지원되는 실제 구성 재현 |
| D | Hearts of Korea만 | 의존성 결손과 모드 자체 오류 분리 |
| E | 다른 서브모드 추가 | 추가 모드가 원인인 경우에만 제한적으로 확인 |

수정 전·후 비교에는 기본 ID 뒤에 접미사를 붙인다.

- `D-PRE`: 수정 전 Hearts of Korea 단독 재현
- `D-POST`: 같은 조건의 수정 후 재현
- `C-PRE`: 수정 전 실제 지원 구성 재현
- `C-POST`: 같은 조건의 수정 후 실제 지원 구성 검증

`A/B 테스트`라는 표현을 수정 전·후 비교의 뜻으로 사용하지 않는다. A와 B는 이미 재현 행렬의 고정된 control ID다.

지원 구성이 C라면 C의 결과를 최종 판단 기준으로 삼는다. D에서 크래시가 사라졌다는 사실만으로 지원 구성이 복구됐다고 판정하지 않는다. 각 결과는 `PASS`, `FAIL`, `NOT RUN`, `BLOCKED` 중 하나로 기록한다.

새 실행은 기존 로그를 덮어쓸 수 있다. 실행과 파일 복사가 승인된 경우에만 현재 로그를 `<승인된 진단 위치>/<사건 ID>/<실행 ID>/` 같은 별도 위치에 보존한 뒤 재현한다. 원본 로그, 덤프, 세이브와 개인 launcher 데이터는 커밋하지 않는다. 보존 위치 승인이 없다면 로그를 이동하거나 회전하지 말고 수정 시각과 현재 상태만 기록한다.

## 4. 실행별 증거 수집

한 번의 실행이 끝난 직후 아래를 같은 실행 묶음으로 기록한다.

- 사건 ID와 실행 ID
- 런처 playset과 정확한 활성 모드 순서
- 사용한 실행 옵션과 `-debug` 여부
- 사용자가 실제로 누른 버튼과 재현 절차
- 실행 시작·종료 시각과 크래시까지의 경과 시간
- 마지막으로 보인 화면, 로딩 문구 또는 진행률
- 종료 형태: 정상 종료 / 멈춤 / 바탕 화면 종료 / 런처 오류
- `error.log`의 최초 관련 오류와 마지막 관련 오류
- `game.log`의 마지막 진행 단계
- `setup.log`, `system.log`, `exceptions.log`의 관련 항목
- launcher 로그에서 확인한 실제 물리 로드 경로
- Windows Error Reporting의 이벤트 유형, 예외 코드, 예외 오프셋, 보고서 ID
- 직전 실행과 달라진 변수 하나
- 기준 실행 또는 control 실행과 비교해 새로 생기거나 사라진 관련 오류
- 입력 파일 해시와 사용한 검색·검사 명령
- 검사 결과 전체 목록 또는 그 보존 위치

로그의 모든 오류가 크래시 원인은 아니다. 경고 수보다 **재현 시각에 가깝고 반복되며 대상 데이터와 연결되는 오류**를 우선한다. 로그 위치나 재현 산출물이 없는 항목은 구현 작업 목록이 아니라 `UNVALIDATED INVENTORY`로 분리한다.

## 5. 원인 분류와 증거 등급

오류를 다음 범주로 나눠 서로 섞지 않는다.

1. **하드 크래시 후보**: 같은 조건에서 같은 WER 서명으로 반복되는 데이터 불일치, assert, 메모리 손상 계열
2. **초기화 차단 오류**: 파서 오류, 필수 데이터 누락, 잘못된 맵 관계, unsafe `replace_path`, dependency/load-order 오류
3. **콘텐츠 기능 오류**: 잘못된 focus/event/decision/character/MIO 참조
4. **비치명 경고**: 아이콘, 음원 샘플레이트, descriptor 경고 등
5. **다른 모드에서 유입된 오류**: 현재 최소 재현 구성에는 없는 항목

각 후보에는 다음 등급을 붙인다.

- `CONFIRMED`: 소스, 로그 또는 재현으로 직접 확인됨
- `STRONGLY_SUPPORTED`: 여러 증거가 일치하지만 수정 후 런타임 증명이 아직 없음
- `UNPROVEN`: 추가 증거가 필요한 가설 또는 보존되지 않은 예비 inventory
- `DISPROVEN`: 관찰된 증거와 모순됨

결론의 적용 범위도 실행 ID로 제한한다. `D-PRE`에서 반증된 가설을 모든 playset과 모든 모드 조합에서 영구 반증됐다고 확대하지 않는다.

## 6. 원인 격리 규칙

- 한 번에 하나의 변수만 바꾼다.
- 로그 묶음 사이에 실행 조건을 섞지 않는다.
- 파일 이름이 같다는 이유만으로 바닐라와 모드 파일의 의미가 같다고 가정하지 않는다.
- 같은 오류가 반복되어도 그 오류 이후 게임이 계속 초기화되면 직접 원인인지 별도로 확인한다.
- WER의 `c0000409` 같은 예외 코드는 결과의 형태이지, 손상시킨 데이터 파일의 이름을 직접 알려주는 증거는 아니다.
- 로그에서 사라진 오류는 해당 실행 구성에서는 반증 근거가 되지만, 다른 모드 조합에서도 영구 해결됐다는 뜻은 아니다.
- 검색 결과 수치를 보고할 때는 distinct ID 수, 전체 match 수, 첫 소속을 제외한 초과 membership 수를 구분한다.
- 입력 파일, 검색 명령, 필터 조건과 전체 결과가 보존되지 않은 수치는 구현 근거로 사용하지 않는다.

## 7. 맵 크래시가 의심될 때

[맵 호환성 점검표](MAP_COMPATIBILITY_CHECKLIST.md)를 사용한다. 특히 다음을 먼저 검사한다.

- `definition.csv`에 없는 province ID를 state/strategic region/railway/supply 파일이 참조하는지
- 같은 province가 둘 이상의 state에 포함되는지
- state ID와 province ID가 현재 바닐라 또는 의존 모드와 충돌하는지
- `provinces.bmp`의 RGB와 `definition.csv`가 일대일로 대응하는지
- 바다·호수·육지 유형, coastal 플래그, adjacency가 일관적인지
- 구버전의 전역 맵 파일이 현재 바닐라 데이터를 통째로 가리는지

네 줄을 추가하는 식의 국소 처방은 전체 참조 관계가 검증되기 전에는 해결로 판정하지 않는다.

### 7.1 필수 3-way 비교

구버전 맵 모드를 현재 바닐라에 이식할 때는 다음 세 기준본을 비교한다.

- `V_OLD`: 원본 모드가 마지막으로 지원한 정확한 Vanilla 1.16.x 빌드
- `HOK_ORIGINAL`: 원본 Hearts of Korea `1.0.9(1)` 배포본
- `V_TARGET`: 현재 목표 Vanilla 빌드

개념상 원작자가 의도한 변경분은 다음과 같다.

```text
INTENDED_DELTA = HOK_ORIGINAL - V_OLD
SUCCESSOR_CANDIDATE = V_TARGET + reviewed(INTENDED_DELTA)
```

이는 자동 binary diff를 그대로 적용하라는 뜻이 아니다. 각 차이가 원작자의 의도인지, 구형 바닐라 잔재인지, 현재 엔진에서 더 이상 유효하지 않은 구조인지 의미 단위로 판정하라는 뜻이다.

다음 방식은 금지한다.

```text
HOK_ORIGINAL과 V_TARGET의 모든 차이
= 원작자가 의도한 변경
```

정확한 `V_OLD`를 확보하지 못하면 해당 차이의 의미는 `UNPROVEN`으로 남긴다. 이 상태에서는 파일 단위 자동 병합, 일괄 번호 이동, bitmap 자동 덮어쓰기를 승인하지 않는다.

각 기준본에 대해 다음을 보존한다.

- 정확한 버전·빌드·체크섬
- 획득 경로와 물리 경로
- 파일 목록
- SHA-256 manifest
- `definition.csv`, `provinces.bmp`, states, strategic regions, railways, supply, adjacency 등 영향 파일의 비교 산출물

### 7.2 영구 ID 매핑

충돌이 없는 연속 ID 범위는 **임시 충돌 회피용 ID 예약 구간 후보**일 뿐, 마이그레이션 공식이 아니다.

실제 변경은 다음 열을 가진 개별 매핑표로 승인한다.

| 필드 | 내용 |
|---|---|
| Entity type | province / state / strategic region 등 |
| Entity identity | 지역 이름, RGB, 기존 membership 또는 지리적 의미 |
| Old ID | 원본 모드 ID |
| Proposed new ID | 후보 신규 ID |
| Collision reason | 현재 바닐라·의존 모드와의 충돌 근거 |
| References | 파일명과 문맥별 참조 위치 |
| Save/submod impact | 세이브·서브모드·스크립트 영향 |
| Evidence grade | CONFIRMED / STRONGLY_SUPPORTED / UNPROVEN |
| Approval status | 미승인 / 승인 / 적용 / 검증 |

`+38`, `+65` 같은 오프셋을 전역 숫자 치환 규칙으로 사용하지 않는다. 같은 숫자가 province, state, 날짜, 수량 또는 다른 스크립트 값으로 등장할 수 있다.

## 8. 단계별 게이트

### 8.1 Diagnostic continuation

다음은 구현이 아니라 추가 진단이다.

- 실제 지원 playset, DLC, 언어 설정과 물리 로드 경로 확정
- 현재 로그·WER·검사 결과의 사건별 증거 bundle 보존
- 원본 archive와 SHA-256 manifest 확보
- `V_OLD`, `HOK_ORIGINAL`, `V_TARGET`의 3-way 비교
- 전체 ID·RGB·membership·참조 inventory 재산출
- 예비 수치의 검색 명령과 전체 결과 목록 보존
- 연결 문서의 존재와 상대 경로 확인

### 8.2 Migration Decision

- 개별 old ID → new ID 의미 매핑표 검토
- 원본 지도 의도와 현재 바닐라 변경의 충돌 해결 원칙 승인
- 기존 세이브와 서브모드 호환성 정책 결정
- 신규 Workshop 계승판의 장기 ID 안정성 검토

### 8.3 Implementation

- 승인된 매핑과 의미 단위 변경만 production 파일에 적용
- 숫자 전역 치환 금지
- 무관한 포맷 정리·밸런스 변경·콘텐츠 재설계 금지
- 변경 단위별 되돌리기 가능한 diff 유지

### 8.4 Validation

- 원래 실패를 재현한 `D-PRE`와 동일 조건의 `D-POST` 비교
- 실제 지원 구성의 `C-POST` 검증
- 정적 맵 무결성 검사
- 새 게임 진입, 맵 표시, 국가 선택, unpause
- 영향 지역의 state, ownership, cores, victory points, supply, railway, adjacency, buildings, positions 확인
- 승인된 경우 save/load 검증
- 새 WER, fatal, assert와 관련 로그 증가 여부 비교

## 9. 완료 판정

수정이 승인되고 적용된 뒤에도 아래 조건을 모두 만족해야 해당 원인을 해결했다고 판정한다.

- 승인된 지원 구성 `C-POST`에서 시작 크래시가 재현되지 않는다.
- 원래 실패 구성의 `D-POST`가 `D-PRE`와 비교되어 원인 격리 결과가 보존된다.
- 기존과 동일한 WER 서명이 다시 생성되지 않는다.
- 새 fatal/assert/맵 무결성 오류가 없다.
- 새 게임 진입, 맵 표시, 국가 선택 등 승인된 스모크 테스트를 통과한다.
- 수정한 데이터에 대한 정적 무결성 검사가 통과한다.
- 기준/control보다 새 관련 오류가 없고, 영향받는 ID·scope·localisation·dependency·load order를 검토했다.
- diff에 무관한 정리, 대량 포맷, 인코딩 또는 줄바꿈 변환이 없다.
- 관련 bookmark별 positive path와 중요한 blocked/negative path를 확인했다.
- 영구 ID·map 변경이면 승인된 save/load 검사를, AI 변경이면 runtime 행동 검사를 수행했다.
- 멀티플레이 호환성을 주장하는 경우에만 동일 모드/DLC/load order의 checksum 및 동기화를 확인했다.
- `supported_version`과 공개 제목의 호환성 표기가 실제 검증 결과와 일치한다.
- 남은 경고와 미확인 위험을 별도로 보고한다.

메인 메뉴 진입, malformed 로그 네 줄 제거, `supported_version` 변경 또는 크래시 한 건 소멸만으로 완료 판정하지 않는다.

## 10. 안전 정지 조건

아래 조건 중 하나라도 해당하면 production 파일을 수정하거나 추측으로 방향을 정하지 않는다. 가능한 읽기 전용 inventory와 증거를 정리한 뒤, 빠진 결정 또는 자료를 사용자에게 보고한다.

- 정확한 목표 HOI4 버전이 해결 방법을 바꾸는데 버전을 확정할 수 없다.
- 런처가 조사 중인 저장소가 아닌 다른 물리적 모드 복사본을 로드한다.
- 확인되지 않은 dependency 또는 load order가 실패에 직접 영향을 준다.
- 서로 다른 root-cause 가설이 같은 정도로 증거와 맞고 분리 시험이 필요하다.
- persistent province/state/region ID의 재번호가 필요하지만 개별 매핑표와 승인이 없다.
- `replace_path` 마이그레이션이 넓은 바닐라 데이터를 unload할 수 있다.
- 필요한 bitmap/binary 원본, 형식 또는 안전한 재생성 방법을 알 수 없다.
- 정확한 마지막 지원 바닐라 기준본이 없어 원작 변경과 구형 바닐라 잔재를 구분할 수 없다.
- save 또는 submod 호환성에 명시적인 마이그레이션 결정이 필요하다.
- 불변 원본 archive와 baseline snapshot이 없다.
- 구체적인 제3자 라이선스·권리 충돌 증거가 발견된다.
- 원본 Workshop ID 또는 `remote_file_id`를 신규 계승판의 업로드 대상으로 사용하려 한다.
- 사용자가 설명한 계승·재게시 권한과 모순되는 구체적 자료가 발견된다.
- 원 제작자의 사망 또는 계승 경위를 공개 설명에 어떤 문구로 적을지 별도 결정이 필요하다.

이미 확인된 계승 프로젝트라는 이유만으로 매번 안전 정지하지 않는다. 안전 정지는 조사 포기가 아니며, 수정하지 않은 상태에서 영향 범위, 빠진 증거와 다음 한 단계의 진단 방법을 제시한다.
