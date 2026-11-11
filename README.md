# Hearts of Korea 디버깅 문서

이 폴더는 Hearts of Korea 모드의 크래시를 재현하고 원인을 좁히며, 특히 맵 데이터를 현재 Hearts of Iron IV 기준에 맞게 이식할 때 사용할 작업 문서다.

문서 자체는 작업 허가가 아니다. 매 작업을 시작하기 전에 요청이 아래 어느 범위인지 확인한다.

- **Review**: 파일을 읽고 상태와 위험만 보고한다.
- **Diagnostic**: 로그와 데이터를 비교해 원인을 진단한다. 프로덕션 동작은 바꾸지 않으며, 사용자가 별도로 허가한 경우에만 가설을 구분하기 위한 최소·한정 instrumentation을 사용한다.
- **Implementation**: 사용자가 승인한 범위만 수정하고 검증한다.

## 문서 목록

- [변경 영향 범위와 누락 방지 절차](docs/HOK_CHANGE_COVERAGE_REVIEW.md): 현지화·표식/변수 표시·주/프로빈스 참조를 검토하거나 변경할 때 먼저 읽는다. 전용 스킬의 호출 조건, 사용처·분기별 처리 대장과 소스/화면/효과/저장 검증을 구분하는 완료 기준을 따른다. 이 지침은 게임 실행이나 코드 수정 권한을 추가하지 않는다.
- [계속개발 내부 표식·변수 현지화 표시 검토](docs/audits/2026-11-08-continuation-localisation-display-review.md): 툴팁에 내부 ID가 보이거나 해당 표시를 수리할 때 먼저 읽는다. 고유 키 8개를 조사한 당시 기록과 [표시 수리 구현·검증 기록](docs/incidents/2026-11-08-localisation-display-implementation.md)을 구분한다. 원문 노출, 수치 조건·효과의 표시 누락, 엔진에서 이미 숨겨진 내부 집계를 별도로 기록한다.
- [현행 지도 기준 주·프로빈스 참조 코드 정렬 계획](docs/HOK_STATE_REFERENCE_ALIGNMENT_PLAN.md): 현재 주·프로빈스를 유지하고 영토 조건·이전·코어·건설 부모·설명을 수리할 때 먼저 읽는다. 최신 9→15주 분할 누락, 기존 결함, 바닐라 공유 불일치와 미확인 후보를 구분한다. 최초 문서화 이후 승인된 수리의 적용 내용·실제 실행·한계는 [정렬 구현 기록](docs/incidents/2026-11-08-state-reference-alignment.md)을 따른다.
- [한국 주 분할과 산업 건설 공간 설계](docs/HOK_KOREAN_STATE_SPLIT_PLAN.md): 한국 여섯 도의 남북 분할과 슬롯 확장을 다룰 때 먼저 읽는다. 9주→15주 구현의 최신 대응표·적용 상태·검증 기록을 연결한다. 기존 ID·프로빈스·시작 공장 총량과 중점 배치를 보존하며, 변경 전 저장 호환을 보장하지 않는 새 게임용 변경이다.
- [강원·포항 반복 자원 탐사 디시전 명세](docs/HOK_KOREAN_REPEATABLE_RESOURCE_PROSPECTING_SPEC.md): 두 디시전을 설계·구현·검증할 때 먼저 읽는다. 기존 자원 탐사 범주에 건설 II·정치력 25·민공 9개·매회 90일·자원 +9·무한 반복을 구현했다. 포항은 「포항제철」 중점 완료도 필요하며, 이 조건·해금 안내·설명문을 검토하거나 수정할 때는 [포항 중점 연계 기록](docs/incidents/2026-11-07-pohang-focus-gate.md)을 먼저 읽는다. 중점 연계 전 실행 결과와 외부 증거·설정 복구는 [최초 구현·검증 기록](docs/incidents/2026-11-06-korean-repeatable-resource-prospecting.md)에서 구분한다.
- [2026-11-06 실행 로그 호환성 수리·검증 기록](docs/incidents/2026-11-06-hok-runtime-compatibility-implementation.md): 해당 오류군을 이어서 수정·검증할 때 먼저 읽는다. 일본 AI·몽골·해군 보상·FIN 교리/장비·일본 인물 등록·음원 수리, 실제 저장·1939 자연 승계·진단 없는 로드 결과와 미검증 범위를 구분한다. [구현 전 검토](docs/incidents/2026-11-06-hok-runtime-log-compatibility-review.md)는 당시의 읽기 전용 판단과 원본 부분 병합 원칙을 보존한 이력이다
- [민주주의 중점 내부 간격 압축 계획·적용 좌표](docs/HOK_KOREAN_DEMOCRATIC_FOCUS_COMPACTION_PLAN.md): 민주 95개 구역 폭 50→38칸(24% 감소), 배치 32개 직접 수정·86개 이동, 게임플레이 보존 29/0. HIDE 정상 완료·같은 프로세스 재로드·별도 합성 선택, 진단 없는 SHOW 정상 완료 뒤 상단 위치 유지와 설정 원복·기존 저장 23개 보존·Steam 플레이 복귀까지 확인했다. 요청 범위의 구현·핵심 검증 완료; [구현 기록](docs/incidents/2026-10-31-korean-democratic-focus-compaction.md)의 한정 화면·기존/추가 경고·성능 등 미측정 범위 참조
- [한미 조약·주한미군 방위비 협상 명세](docs/HOK_KOREAN_US_DEFENSE_COST_SHARING_SPEC.md): 조약·주둔의 미국 선택과 양국 방위비·자치령·사단·후속·표시를 변경할 때 먼저 읽는다. 조약 한국 +5%/미국 −5%, 주둔 협정 최종 +35%/−15%, 자치령은 기존 정신·3사단·KATUSA 허용, AI 주둔 10/0/0을 구현했다. 최신 정적 144 PASS·0 FAIL, run4에서 두 35일 중점의 정상 진행과 미국 AI 수락·한국 +35% UI를 확인했다. 영어·콜론 수정 후 재시작 UI·구저장은 미검증이다.
- [한미 방위비 구현·검증 기록](docs/incidents/2026-11-11-korean-us-defense-sharing.md): 초기 130 PASS, scope 오류를 놓친 수정 전 144 PASS와 수정 뒤 검사를 구분한다. 정상 run4의 AI 협정·helper 재호출·보유 상위 정신의 전쟁 해제·실제 재로드와 최종 저장 필드 대조를 확인했고 설정·파일 복원을 마쳤다. 다른 분기의 강제 준비와 남은 UI·구저장·조건별 검증 범위는 기록에서 분리한다.
- [한미 방위비 사진·아이콘 출처](docs/HOK_KOREAN_US_DEFENSE_ASSET_CREDITS.md) · [통합 자산 manifest](docs/data/HOK_KOREAN_US_DEFENSE_ASSET_MANIFEST.json): HOI4풍 AI 사진 원본 2개·국민정신 원본 4개와 런타임 텍스처 8개, 두 국기 참조·생성/편집 프롬프트·가공·해시·작은 크기 정적 확인을 기록한다. 실제 게임 표시 검증과 구분한다.
- [한국 민간 핵 연구 중점 2개 구현 명세](docs/HOK_KOREAN_CIVIL_NUCLEAR_RESEARCH_SPEC.md): 현재474개. 첫35일·핵 혁신100%·핵 기술 선행 연구 불이익2년 감소1회, 둘째는 감산 없는245일. 후속 변경은 정적 대조만 수행하며 기완료 저장에 새 보상을 자동 소급하지 않음
- [민간 핵 연구 구현·검증 기록](docs/incidents/2026-10-31-korean-civil-nuclear-research.md): 감산 제거 전의 소스506/0·정상240회14/0·건설 대기열17/0·재로드24/0·기보유 통과 각19/0 등은 이력으로 보존. 감산 없는245일의 새 실행·정상 진행은 미검증
- [민간 핵 연구 아이콘 출처](docs/HOK_KOREAN_CIVIL_NUCLEAR_ICON_CREDITS.md): 전용 AI 그림2개·100×88 DDS·내부 광택, 원본·프롬프트·현재1.19.4.1 광택 자산 출처와 해시
- [한국 기능 연동 수리·후속 개발 명세](docs/HOK_KOREAN_FEATURE_INTEGRATION_SPEC.md): 훈장·교리·비전 1950 수리와 수문 조절·MIO 15개 전문화·연구망·해군 습격·세력 템플릿 소스 통합. [구현·검증 기록](docs/incidents/2026-10-31-korean-feature-integration.md)의 실제 검증 범위·제한 참조
- [한국 기능 연동 비교 감사 — 영국·독일 1.19.3 기준](docs/audits/2026-10-30-korean-feature-integration-review.md): 감사 당시 기능 연결 누락 2개 계통·해금 안내 1건, 미완성 흔적 1건과 전용 콘텐츠 차이 4개를 구분한 소스 검토 기록. 이후 구현·실행 검증은 위의 별도 기록 참조
- [비전 1950 긴급 특별 건함계획 명세](docs/HOK_KOREAN_VISION_1950_EMERGENCY_SHIPBUILDING_PLAN.md): 구현·정적 86/0·기록한 조건의 기능 검증 완료. 정치력 150으로 함정·지원함·수리함·수송선 비용 −50% 보정 180일, 적용 중 사용 차단·만료 후 추가 대기 없이 무제한 반복
- [긴급 특별 건함계획 구현·검증 기록](docs/incidents/2026-10-20-korean-emergency-shipbuilding.md): 실제 사용·비용 감소와 복귀·재사용·최종 일반 실행 새 게임 새 정규화 오류 0. 강제 조건 준비·합성 저장 경고·정상 진행 및 미검증 항목은 분리
- [긴급 특별 건함계획 이미지 출처](docs/HOK_KOREAN_EMERGENCY_SHIPBUILDING_ASSET_CREDITS.md): AI 생성 전용 그림 2개·원본 보존·32×32 디시전과 60×68 국민정신·GFX 및 정적 검수
- [한국 재벌과 시민사회 내정 설계와 모드 이식 후보](docs/HOK_KOREAN_CHAEBOL_CIVIL_SOCIETY_RESEARCH_PLAN.md): 선행 원본 조사; 이후 승인한 한국판 구현은 별도 확정 명세·검증 기록을 따름
- [한국 재벌·시민사회 확정 명세](docs/HOK_KOREAN_CHAEBOL_CIVIL_SOCIETY_SPEC.md): 두 세력 UI·13개 중점·조달 사고·검찰 정변과 비용·복구 계약
- [내정 시스템 자산 출처](docs/HOK_KOREAN_CHAEBOL_CIVIL_SOCIETY_ASSET_CREDITS.md): 기존 한국 초상·기업 로고와 공용 UI·사건 그림 재사용
- [내정 시스템 개정·검증 기록](docs/incidents/2026-10-12-korean-civic-revision.md): 진입·주문·배치·표시 개정의 정상 진행·합성 검사·세이브 검증을 구분
- [내정 디시전 아이콘 구현·검증 기록](docs/incidents/2026-10-12-korean-civic-decision-icons.md): 전용 배지·파란 지원/견제 아이콘, 출처·정적 확인·실제 표시와 테스트 정리
- [왕정 중점 완료 조건과 환제국 물자 가지 배치 계획](docs/HOK_KOREAN_ROYAL_PREREQUISITE_LAYOUT_PLAN.md): 기존 18개 코드 적용·정적/로드/초기 SHOW/HIDE 일부 UI 확인·정상 진행 검증 대기; 14개 지정 완료 조건 삭제, 연락망 I·II 형성 전 유지, 물자 가지는 환제국 선행·우측 하단 (184,11)로 이동
- [한국 중점 선행 조건 가독성 개선 계획](docs/HOK_KOREAN_FOCUS_PREREQUISITE_READABILITY_PLAN.md): 여섯 시작 중점 코드 적용·정적 및 초기 UI 확인·정상 진행 검증 대기; 원료는 두 선행 AND 연결, 나머지 다섯은 지정 완료 조건만 삭제. 삼군의 을해군란·F4/F5 후속 조건은 유지
- [한국 신규 디시전과 국민정신 설명 보강 계획](docs/HOK_KOREAN_DECISION_SPIRIT_PROSE_PLAN.md): 설명 124개·한국어/영어 14쌍 적용, 파시즘·공산주의 문체와 좋은 기존 문안 보존; 정적 보존 검사 통과, UI 확인 대기
- [디시전·국민정신 설명 구현 기록](docs/incidents/2026-10-03-korean-decision-spirit-prose.md): 누적 124개와 문체 후속 48개, 효과·조건 대조, 최종 보존 검사와 Rt56 플레이셋으로 인한 화면 검증 대기
- [한국 중점 2차 확장 현황](docs/HOK_KOREAN_SECOND_WAVE_PLAN.md): 현재474개; 기존460개에 내정13개 추가·구 협력1개 제거 후 민간 핵 연구2개 추가. 과거 수량과 실제 검증은 당시 소스·기록별로 구분
- [파시즘 점령행정·삼군 조정·재건예산 명세](docs/HOK_KOREAN_FASCIST_FOLLOWUP_SPEC.md): 신규 12개·국민정신 8개, 영토·평시 조건과 실제 예산 선택
- [한국 중점 보상 재조정 설계·적용 상태](docs/HOK_KOREAN_FOCUS_REBALANCE_PLAN.md): 보상 강화 적용, 게임 검증 진행 중; 보병장비 한정 생산량 +10%는 미적용·대안 응답 대기
- [한국 중점 트리 보존·35일화·확장 설계](docs/HOK_KOREAN_FOCUS_EXPANSION_PLAN.md): 기존 266개 보존, 기간 단축 범위와 단계별 확장 제안
- [한국 중점 좌표·연결선 재배치 설계](docs/HOK_KOREAN_FOCUS_LAYOUT_PLAN.md): x0~194·y0~24 압축 배치 적용; HIDE 초기 상태 전체 분야 화면 검수 완료, 조건별 검증 범위는 문서 참조
- [한국 중점 압축 좌표표](docs/HOK_KOREAN_FOCUS_LAYOUT_COORDINATES.md): AA58→압축 배치 326개 전후 좌표; 절대 7/상대 319, offset 조건 유지·이동량 0
- [한국 중점 압축 작업 기록](docs/incidents/2026-09-21-korean-focus-compact.md): 현재 압축 배치의 실행·화면 검증과 남은 범위
- [한국 중점 첫 재배치 이력](docs/incidents/2026-09-21-korean-focus-layout.md): AA58 넓은 배치의 HIDE·SHOW, 만주 선 수정과 바로가기·최종 실행 관측
- [한국 중점 1차 확장 구현 기록](docs/incidents/2026-09-21-korean-focus-expansion.md): 152개 35일화, 신규 60개와 검증 범위
- [한국 중점 1차 60개 명세](docs/HOK_KOREAN_FOCUS_FIRST_60_SPEC.md): 실제 이름·연결·보상·원본 대응과 현재 압축 기본 절대좌표
- [한국 신규 중점·국민정신 아이콘 개선 계획](docs/HOK_KOREAN_FOCUS_SPIRIT_ICON_PLAN.md): 신규 중점 60개·국민정신 29개 반복 현황, 재사용 자료·조건과 교체 우선순위; 문서화만 완료
- [한국 신규 아이콘 구현·검증 기록](docs/incidents/2026-09-22-korean-focus-icons.md): 위 초기 계획의 후속 구현, 중점 60개·국민정신 29개 이미지 적용 및 실제 검증 범위
- [한국 신규 아이콘 색상 재구성 계획](docs/HOK_KOREAN_FOCUS_ICON_COLOR_PLAN.md): 신규 60개·29개를 정치 계열·정책 용도별로 구분; DDS 82개 배경색 수정, 기존 군종색 7개 유지. [구현·검증 기록](docs/incidents/2026-09-22-korean-focus-icon-colors.md) · [색상 전후 비교](docs/assets/korean-focus-icon-colors/index.html). 정적 검증 통과, 이번 색상 런타임 미실행
- [아이콘 전후 비교](docs/assets/korean-focus-icons/index.html) · [사용 소재·크레딧](docs/HOK_KOREAN_FOCUS_ICON_CREDITS.md) · [대상별 출처·가공·해시](docs/data/HOK_KOREAN_FOCUS_ICON_MANIFEST.json)
- [한국 중점용 바닐라 이식 후보](docs/HOK_KOREAN_FOCUS_DONOR_CATALOG.md): 원본 중점·의존성·한국 연결 지점과 이식 난도
- [크래시 디버깅 런북](docs/CRASH_DEBUGGING_RUNBOOK.md): 재현부터 원인 격리까지의 표준 절차
- [증거 기록 양식](docs/EVIDENCE_RECORD_TEMPLATE.md): 실행별 로그와 가설을 섞지 않고 기록하는 양식
- [맵 호환성 점검표](docs/MAP_COMPATIBILITY_CHECKLIST.md): 맵 데이터 이식 전후의 필수 검사
- [검증 점검표](docs/VALIDATION_CHECKLIST.md): 수정 승인 후 완료 판정 기준
- [2026-08-31 시작 크래시 조사](docs/incidents/2026-08-31-startup-crash.md): 현재 확인된 사실과 남은 가설

## 고정 안전 원칙

1. `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`의 게임 원본과 Workshop 모드는 읽기 전용 기준 자료로 취급한다.
2. 로그, 크래시 덤프, 세이브, 런처 사용자 데이터는 증거다. 사용자의 별도 승인 없이 수정·이동·삭제하지 않는다.
3. 목표 버전의 바닐라 파일을 기준으로 삼고, 구버전 파일 전체를 복사해 덮지 않는다.
4. 모드의 의도, 이벤트·포커스 ID, 밸런스, 명칭은 호환성 수정에 필요한 경우가 아니면 변경하지 않는다.
5. 맵 ID 변경은 세이브·스크립트·서브모드와의 호환성을 깨뜨릴 수 있다. 명시적인 마이그레이션 승인 전에는 실행하지 않는다.
6. 숫자는 문맥 없이 일괄 치환하지 않는다. 같은 숫자가 state, province, 이벤트 값 등 서로 다른 의미로 사용될 수 있다.
7. 수정이 승인되더라도 먼저 대상과 영향 범위를 기록하고, 작은 단위로 적용한 뒤 같은 조건에서 검증한다.
8. 게임 실행, Nudger 사용, 테스트, 커밋·푸시·배포는 각각 사용자의 명시적인 요청 범위 안에서만 한다.
9. 저장소 `descriptor.mod`와 launcher `.mod`의 `dependencies`, `replace_path`, `remote_file_id`, `path`를 감사하고, 런처가 실제로 읽은 물리적 모드 복사본을 확인한다.
10. `supported_version` 변경이나 메인 메뉴 진입만으로 호환성이 증명됐다고 판단하지 않는다.
11. localisation은 일반 YAML이 아니다. UTF-8 BOM, locale header, 키·토큰과 `Korean Language` 의존 계약을 보존하고 일반 YAML formatter를 사용하지 않는다.

## 증거 등급

- **확인됨(Confirmed)**: 파일·로그·반복 재현으로 직접 확인한 사실
- **강하게 뒷받침됨(Strongly supported)**: 여러 증거가 같은 원인을 가리키지만 수정 후 재현 검증이 남은 판단
- **미확인(Unproven)**: 가능성은 있으나 직접 증거 또는 분리 시험이 부족한 가설
- **반증됨(Disproven)**: 현재 재현 조건에서 성립하지 않는 가설

결론에는 반드시 이 등급을 붙인다. 엔진 크래시 주소만으로 내부 원인을 단정하지 않는다.

## 민감하거나 임시인 자료

다음 자료는 필요할 때 원래 위치에서 읽고, 기본적으로 프로젝트에 복사하거나 커밋하지 않는다.

- `error.log`, `game.log`, `system.log`, `setup.log`, `exceptions.log`
- Windows Error Reporting 보고서와 덤프
- 플레이어 세이브 및 런처 설정
- 사용자 이름이나 로컬 절대 경로가 포함된 진단 자료

사건 문서에는 원본 파일 자체가 아니라 감사에 필요한 경로 별칭, 파일명, 줄 번호, 수정 시각과 짧은 발췌만 기록한다. 개인 식별 경로는 `<HOI4_USER_DATA>` 같은 별칭으로 비식별화한다. 원본 로그 보존이 필요하면 사용자가 승인한 별도 진단 위치에 실행 ID별로 복사하고, 커밋하지 않는다.
