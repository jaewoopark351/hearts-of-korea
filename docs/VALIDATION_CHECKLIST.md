# 수정 후 검증 점검표

이 문서는 수정이 명시적으로 승인되고 적용된 경우에만 사용한다. 게임 실행이나 외부 도구 사용도 별도 승인 범위를 따른다.

중국·만주·일본을 1.19.2 target에 맞추는 후속 작업은 [중국·일본 바닐라 정렬 정책](CHINA_JAPAN_VANILLA_ALIGNMENT_POLICY.md)의 파일 분류, 기능 손실과 행위 검증 조건을 함께 적용한다.

원작 HoK 일본 민주주의 분기 구현은 [HoK 일본 민주주의 전체 분기 1.19.2 통합 설계](HOK_JAPAN_DEMOCRATIC_BRANCH_INTEGRATION_PLAN.md)의 ID migration, target host allowlist, AI·DLC 정책과 focus/event별 검증 계약을 추가로 적용한다. 실제 적용 범위와 아직 실행하지 않은 검사는 [2026-09-09 구현 기록](incidents/2026-09-09-japan-democratic-focus-integration-implementation.md)에 기록한다.

## 1. 변경 범위 확인

- [ ] 수정한 파일 목록과 수정 이유가 있다.
- [ ] 편집 전 Git branch/commit/dirty 상태와 편집 후 상태를 비교했다. Git 저장소가 아니면 그 결과를 기록했다.
- [ ] 승인 범위 밖의 파일은 변경되지 않았다.
- [ ] Steam 게임 원본, Workshop 모드, save/playset/settings를 수동으로 변경하지 않았다.
- [ ] 승인된 게임 실행이 갱신한 로그는 실행 ID로 구분했고, 기존 로그를 승인 없이 삭제·덮어쓰지 않았다.
- [ ] 기존 사용자 변경 사항을 덮거나 되돌리지 않았다.
- [ ] 모드 동작, ID, 밸런스 중 의도적으로 달라진 부분을 명시했다.
- [ ] 임시 파일과 생성 산출물의 위치를 기록했다.

## 2. 정적 검사

- [ ] Clausewitz 문법의 괄호, 따옴표, 키-값 구조를 검사했다.
- [ ] 중복 정의와 존재하지 않는 참조를 검사했다.
- [ ] HoK 일본 root는 `relative_position_id` 없이 절대 `x=10`, `y=0`이고, 하위 39개 HoK 상대좌표 사슬에 누락·순환 참조가 없다.
- [ ] D-JAP-16 적용 시 정치 진입점 6개의 reciprocal mutex/HIDE guard와 NCNS 정치 하위 자체 `allow_branch` 경계 9개의 HoK guard가 정확히 대응한다.
- [ ] HoK 본토경제 8개와 바닐라 SEA 산업 34개·군부 61개를 구분했고, 공통 SEA 계통에는 HoK mutex/HIDE guard가 남지 않았다.
- [ ] 파일 인코딩과 줄바꿈이 엔진 요구사항에 맞는다.
- [ ] localisation `.yml`의 UTF-8 BOM, 기존 locale header, `KEY:0` 형식, 중복·누락·정확한 casing을 검사했다.
- [ ] dual localisation 대상은 English/Korean 대응 파일의 상대경로, key set과 표시 문자열 body가 1:1로 일치한다.
- [ ] `$KEY$` 치환, scripted token, 색상 코드, icon token, `\n`, quote escaping이 보존됐다.
- [ ] 일반 YAML formatter를 사용하지 않았고 BOM·줄바꿈·공백·Unicode를 일괄 정규화하지 않았다.
- [ ] `Korean Language` 의존 계약과 load order를 보존하고, 승인된 경우 실제 게임에서 한국어 표시를 확인했다.
- [ ] repository descriptor와 launcher `.mod`의 dependency, `replace_path`, `remote_file_id`, `path`가 의도대로이며 서로 논리적으로 일관된다.
- [ ] `supported_version`은 목표 기록과 일치하지만 호환성 증거로 취급하지 않았다.
- [ ] 맵 변경이면 [맵 호환성 점검표](MAP_COMPATIBILITY_CHECKLIST.md)의 정적 완료 조건을 모두 확인했다.

## 3. 비교 검사

- [ ] 목표 바닐라를 기준으로 변경 전·후 차이를 확인했다.
- [ ] 변경 의도와 무관한 전역 데이터 차이가 없다.
- [ ] 삭제한 stale override가 목표 버전 바닐라를 실제로 상속하며, 내용이 같은 불필요한 바닐라 복사본이 모드에 남지 않았다.
- [ ] target-derived 파일의 target 대비 차이가 승인된 KOR bridge와 명시적으로 승인된 HoK 일본 민주 host/delta allowlist에만 한정된다.
- [ ] 일본 host의 WTT/NCNS root, imperial-influence inlay와 continuous-focus 절대좌표가 정확한 target 원값과 일치하고, HoK shared hook은 한 번만 존재한다.
- [ ] D-JAP-16/17을 구현했다면 target 대비 host delta는 정치 entry 6개, NCNS 정치 하위 자체 `allow_branch` 경계 9개, timing-safe HoK 선택 flag와 HoK-HIDE용 SEA 산업 위치 offset 1개에 한정된다.
- [ ] ID 마이그레이션 표의 모든 항목이 문맥별로 반영됐다.
- [ ] 이전 ID가 잘못 남은 곳과 새 ID가 잘못 유입된 곳을 모두 검색했다.
- [ ] 필수 의존 모드와의 충돌을 검사했다.
- [ ] 런처가 저장소/로컬 개발/Workshop 중 의도한 물리적 복사본을 로드했음을 확인했다.

## 4. 실행 검사

사용자가 실행을 승인한 경우에만 진행한다.

- [ ] 바닐라 기준 실행 결과를 기록했다.
- [ ] 필수 의존 모드만의 결과를 기록했다.
- [ ] Hearts of Korea 단독 결과를 기록해 모드 자체 문제와 의존 모드 VFS 문제를 분리했다.
- [ ] Hearts of Korea와 필수 의존 모드 조합을 같은 조건에서 실행했다.
- [ ] exact playset, load order, DLC, language와 실행 ID를 기록했다.
- [ ] 런처 진입, 데이터 초기화, 메인 메뉴, 관련 bookmark의 새 게임, 한국 국가 선택까지 승인된 범위를 통과했다.
- [ ] 변경 지역의 줌, state 선택, 보급·철도·해군 경로 표시를 확인했다.
- [ ] WTT·NCNS 활성 상태에서 `HIDE`와 `SHOW` 각각 1936 시작, HoK root 진행 중, 완료 후 dirty relayout과 save/load 뒤에도 절대 root와 하위 상대좌표 분기가 같은 위치에 남는다.
- [ ] HoK root의 절대 위치 `(10,0)`과 전체 범위 `x=6..18`, `y=0..9`가 화면 경계, focus 아이콘·제목·연결선, branch UI, inlay와 충돌하지 않는다.
- [ ] `error.log`에 `HOK_JAP_strengthen_civilian_government`의 `relative_focus_id` 또는 `Relative focus must be scripted before this` 오류가 다시 나타나지 않는다.
- [ ] `HIDE`에서 HoK root 완료 직후 NCNS 정치 301개 구간이 자체 `allow_branch` 경계를 통해 재등장하지 않는다.
- [ ] `SHOW`에서는 경쟁 정치 계통이 보여도 HoK와 동시에 진입할 수 없다.
- [ ] SEA 산업 34개·군부 61개는 HoK 완료 전후 계속 표시·사용되며, `HIDE` 완료 후 각각 `x=20..37`, `x=39..65` 범위로 이동한다.
- [ ] 경제·군부 shortcut과 `jap_imperial_influence_inlay_window`가 빈 위치로 이동시키거나 불필요한 가로 폭을 만들지 않는다.
- [ ] 일시정지를 해제한 짧은 진행 중 즉시 크래시, 멈춤, event spam 또는 심각한 오류 증가가 없다.
- [ ] 원래 실패의 positive 재현 경로와 중요한 blocked/negative 경로를 확인했다.
- [ ] persistent ID, flag, variable, history 또는 map 변경이면 승인된 save/load 검사를 수행했다.
- [ ] AI 로직 변경이면 승인된 runtime 행동을 검사했다.
- [ ] 멀티플레이 호환성을 주장하는 경우에만 동일 구성의 checksum과 동기화를 검사했다.
- [ ] 종료 직후 로그와 WER을 해당 실행 ID로 기록했다.

## 5. 크래시 회귀 판정

- [ ] 이전과 동일한 이벤트 유형, 예외 코드, 예외 오프셋의 WER이 재발하지 않았다.
- [ ] 이전 핵심 오류가 현재 실행 로그에서 사라졌거나 더 이상 종료와 연결되지 않음을 확인했다.
- [ ] 새 fatal, assert, malformed map 오류가 없다.
- [ ] 다른 오류가 먼저 드러났다면 별도 사건으로 분리했다.
- [ ] 최소 두 번 이상 같은 지원 구성에서 결과가 일관적이다.

## 6. 콘텐츠 회귀 표본 검사

- [ ] 주요 focus/event/decision이 로드된다.
- [ ] 주요 character와 country leader 참조가 유효하다.
- [ ] MIO, technology, doctrine 참조 오류를 확인했다.
- [ ] division name group과 OOB가 유효하다.
- [ ] 주요 state의 owner/core/claim, victory point, resource가 유지된다.
- [ ] HoK 한국 경계·명칭·핵심 콘텐츠가 유지된다.
- [ ] 중국·만주는 target control과 일치하며, 일본은 명시적으로 승인된 HoK 민주 delta를 제외하고 target control과 일치한다.
- [ ] `SND`를 포함한 중국 국가의 map/UI 색상과 owner·core가 target과 일치한다.
- [ ] 현행 일본 focus·AI plan·decision·character·MIO·OOB가 유효하고, 승인된 HoK 민주 분기와 공존하며, historical AI에서 중국전쟁 경로가 실제로 진행된다.
- [ ] HoK 미선택 1936 플레이어·AI는 SEA 산업 34개와 군부 61개를 target과 동일하게 이용하며, HoK 선택 뒤에도 기능은 유지되고 위치만 D-JAP-17에 따라 바뀐다.
- [ ] 1939 bookmark에서는 history상 완료된 경쟁 정치 root와의 배타성 및 기존 일본 history·OOB가 유지된다.
- [ ] 독립 한국 때문에 필요한 1936·지원 대상 1939 일본 OOB 위치, KOR caller와 명시적으로 승인된 HoK 일본 민주 분기·필수 종속성만 allowlist에 남았다.
- [ ] 한국 추가 state `1082–1084`가 target의 한국 전체·남부·북부 판정, 저항, decision와 WTT Japan 효과에 문맥별로 반영됐다.

## 7. 최종 보고

완료 보고에는 다음을 포함한다.

- 기준 버전과 정확한 테스트 구성
- 확인된 원인과 증거 등급
- 변경한 파일과 동작 영향
- 수행한 검사와 수행하지 않은 검사
- 크래시 재현 여부 및 WER 비교
- 남은 경고, 미확인 위험, 호환성 영향
- Git 상태와 커밋·푸시·배포 여부

## 8. 완료 정의

- [ ] 정확한 target HOI4 버전과 test playset을 기록했다.
- [ ] 원래 실패를 정밀하게 설명하고 가능한 경우 pre-patch로 재현했다.
- [ ] root cause가 확인됐거나 남은 불확실성이 명확히 제한돼 있다.
- [ ] patch가 입증된 원인에 필요한 최소 범위다.
- [ ] 기존 동작이 보존됐고, 의도적인 차이는 모두 기록했다.
- [ ] 동일 재현 조건에서 실패가 사라졌다.
- [ ] baseline/control 대비 새 관련 오류가 없다.
- [ ] 영향받은 ID, scope, localisation, dependency와 load order를 검토했다.
- [ ] diff에 무관한 cleanup, mass formatting, encoding 또는 line-ending 변환이 없다.
- [ ] 실행하지 못한 검사는 `NOT RUN` 또는 `BLOCKED`로 명시했다.

일부 테스트가 승인되지 않았거나 불가능했다면 “검증 완료”라고 표현하지 않고, 확인된 범위까지만 보고한다.
