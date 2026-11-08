# 현행 지도 기준 주·프로빈스 참조 정렬 구현

작성: 2026-11-08 (Asia/Seoul). **승인한 참조 정렬 수리와 해당 검증 완료.** 이 문서는 [정렬 계획](../HOK_STATE_REFERENCE_ALIGNMENT_PLAN.md)의 후속이며, 최초 읽기 검토와 이번 실행을 구분한다. 모든 콘텐츠·기존 캠페인·장기 진행의 무오류를 뜻하지 않는다.

## 범위와 기준

사용자는 현재 지도를 유지하면서 계획의 참조·지역 목록·관련 설명을 구현하고 검증하도록 승인했다. `history/states/`, `map/`, 시작 산업·인구·자원·승점, 중점 배치·기간·AI, 비용·고정 건물 수량은 보존한다. 기존 ID·완료 이력을 유지하며 기완료 보상 소급 지급은 추가하지 않는다. 별도 표시 감사의 내부 표식 8개, NOR 정권 검사 X-01, 신간선 수치 X-02, 미확정 H-02의 추측성 수리는 포함하지 않는다. H-01은 후술한 실행에서 잔류가 확인된 뒤 두 주에 한정해 수리를 추가했다.

| 기준 | 실제 경로·상태 |
|---|---|
| 작업 소스 | `C:\hoi\hearts_of_korea` |
| Git | `feat/korean-focus-expansion-ai`, HEAD `0d73d49726abbfa435c73f1bf8cc24d4a5af014b`; 선행 분할·국토개발 등 미커밋 작업 보존 |
| 엔진 | `Operation Postern v1.19.4.2.2da5 (270d)`, Steam build `26409260`, 활성 DLC 36개 |
| 설치 원본 | `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV` — 읽기 전용 문법·지리 기준 |
| 역사적 원작 | `C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\2898629778` — 읽기 전용 출처 |
| 활성 소스 | 사용자 `mod/hearts of korea.mod`가 저장소 직접 지정 |
| 원래 순서 | HOK → `Hearts of Korea English Translation Anime Modder's Edition`; DLC 비활성 목록 없음 |
| 번역 사본 | `C:\hoi\Hearts of Korea English Translation Anime Modder's Edition` — D-01~03 활성 영문 설명 수정. Workshop 원본과 구별 |
| 실제 사용자 데이터 | `C:\Users\jaewo\OneDrive\문서\Paradox Interactive\Hearts of Iron IV` |
| 외부 시험·증거 | `C:\hoi\test\hok-state-reference-alignment-20261108-01` (아래 `<TEST>`) |
| 번역 전용 증거 | `C:\hoi\test\hok-english-translation-anime\hok-state-reference-alignment-20261108-01` (아래 `<ENG_TEST>`). 활성 번역의 `AGENTS.md`가 정한 별도 위치 |

기존 사용자 게임은 사용자가 직접 종료했다. 시험 전에 기존 로그를 `<TEST>/baseline-logs`, 네 설정 파일을 `user-config-before`, 저장60개의 해시 목록을 `existing-saves-before.json`에 보존했다. 기존 `autosave_temp.hoi4` 사본은 `user-saves-before`에 보존하고 시험 중 자동 저장을 껐다. 시험에는 고유 descriptor를 사용했으며 최종 설정4파일·원래 모드 순서의 byte 일치 복구를 확인했다. 생산 descriptor·Workshop 정체성은 변경하지 않았다.

## 확정한 대응과 적용 단위

주 ID, 프로빈스 ID, 현지화 키는 서로 다른 식별자다. 숫자 일괄 치환을 사용하지 않았다.

| 항목 | 현재 대상·범위 | 적용 내용·보존 사항 |
|---|---|---|
| R-02 쓰시마 | state1085 / province10011 / 기존 표시 키 `STATE_KR_1027` | 아덴 state992 이전과 미정의 키 참조만 교정. 기존 조건·비용·일회성 유지 |
| R-03 일본 보호령·낙일 | 282, 528–536, 1018–1020 (13주) | 직접 점령·JAP 종속국 대안, KJP 코어·이전 목록을 같은 범위로 정렬. 별도 쓰시마는 제외 |
| R-04 중국 인정 | 기존 목록 +1032–1046 (15주) | CHI 국가 합병은 유지, KCH 코어 범위만 보완. 간도·안둥·헤이허의 제거된 영토를 복원하지 않음 |
| R-05 KCH 수도 | 난징 province11913의 state1035 | 상하이613에서 난징1035로 참조 정렬. 현행 CHI 수도·원래 주석·생성 경로 근거 |
| R-06 해주 항구 요새 | province13438 / state1083 / coastal=true | 옛 HOK 해주13400의 현행 대응을 사용. 비해안13419에서 옮기며 해안요새3·다른6항구 유지 |
| R-07 일본 한반도 요새 | province4052→527, province1003→1083 | 1003만 부모·소유/통제 검사 분리. 평양527의 다른 지급은 그대로 유지 |
| R-08 몽골 보급 | 7799→330; 7843→818; 7717·7676→820; 12557→819; 12612·12541→817; 12609→621 | 8개 각1, 순서·기존 철도11명령 유지 |
| R-09A 인도차이나 | 671,670,741,286 +1017,1066–1069 (9주) | 착수 통제·controller·일반 이전·내전 이전을 같은 지역으로 정렬 |
| R-09B 필리핀 | 623,327,625,624,627,626 +628,1025–1027 (10주) | 기존628 누락과 신규 분할3주를 구분. NOR 검사는 보존 |
| R-09C 인도네시아 | 672,334,335,673,667,668,669 +1022,1047–1058,738 (21주) | 자카르타7381의 현행 주1058 포함. INS 소유/지역 태그 코어를 구분하며 INS 코어를 일괄 추가하지 않음 |
| R-09D 말레이시아 | 336,333 +1021,1023,1024,1059–1065 (12주) | 싱가포르·페낭 포함. 외교 사건 H-01의 자동 이전 여부는 별도 검사 |
| R-09E 호주 | 522,520,519,521,285,517,518 +674,870–873,1074,1075 (14주) | 본토 범위를 복구. 해외령523을 포함하지 않으며 해외령 자동 포함 없음 |
| R-09F 뉴질랜드 | 723,284 +1079–1081 (5주) | 본토 범위를 복구. 사모아 제외 |
| R-10 외교 인도차이나 | 같은9주, VIN 코어는 기존670·741 +1067–1069 | 중점 FRA 조건과 수락 사건 이전을 정렬. 이미 VIN 코어인1017·1066은 중복 부여하지 않고 다른 코어 보존 |
| H-01 해협식민지 외교 | 싱가포르1021·페낭1065 | 실제 수락 효과의 puppet만으로는 두 주가 ENG에 잔류했다. 수락 때 각각 ENG 소유·완전통제·MAL 코어인 경우에만 MAL로 이전. 적 점령지는 건너뛰며 나중에 자동 이전하지 않음. 기존 gate·720일 정신·AI·코어·다른 영토 유지 |
| V-01 중국 요새 | 6969→610; 11822·12043·3900·1052→609; 1137·6904·9776→1039 | 기존5프로빈스의 `any <5` 풀을 OR로 유지하고 건설 부모만 분리. 6969 지급에는 실제610의 ROOT 완전통제 검사 적용. 고정3단계·명령 순서 유지 |
| V-02 섬 요새 | 기존15개 태평양 섬의 실제 해안 프로빈스 | 중국 본토5프로빈스 조회를 `all_provinces/limit_to_coastal`로 교정. `<5` 조건·해안2단계 유지 |
| V-03 인도차이나 우회 | 기존8주 +1017 | 실제9주 reward generator와 우회 지역 일치 |
| D-01 해군 연구 | 우선 state1086 경상남도 | paired 저장소 현지화·활성 영어에서 `$HOK_KOR_STATE_1086$` 사용. 보상 로직 그대로 |
| D-02 실업·시민교육 | 조건525·1082·1088·1031·1087; 수혜525·1082·1031 | 경기·전라남북·충청남북 조건과 경기·전북·충남 각각 슬롯2/민간공장2 지급을 명시. 연구25%1회 유지. 실제 영문 화면의 잘림을 확인해 정보 보존한 짧은 문구로 조정 |
| D-03 지역 투자 | 평남·충남·경남 수혜, 해당 도 남북 조건 | 활성 영어3설명만 현재 한국어·실제 취소 조건에 동기화. 150정치력·90일·각1건물 유지 |
| D-04 영문 주 이름 | 한국15주 중 고유 이름 키12개 | 실제 영어 조건·보상에서 한국어 글꼴 미지원으로 `????`를 확인. 활성 번역에 source12키와 순서가 같은 `HOK_KOR_state_split_l_english.yml` 추가. 기존525·1029·1084 영문키는 유지 |

정확한 원래/추가/최종 주 순서는 `<TEST>/decisions/region-alignment-manifest.json`에 유지한다. HOK 소스 백업은 `<TEST>`의 `decisions/source-before`, `focuses/source-before`, `compat/source-before`, `source-before/repository`에 있으며 각각 실제 작업 전 사본이다. 번역 소스 백업은 `<ENG_TEST>/source-before`, `focus-description`, `state-name-display`에 둔다. 상세 해시 manifest는 각 하위 디렉터리에 유지한다. 지도·주24파일의 작업 전 해시는 `<TEST>/map-and-state-before.json`이다.

번역 전용 지침을 늦게 확인해 초기에 `<TEST>/source-before/active-translation`과 `<TEST>/final-runtime-source/active-translation`에 둔 백업/스냅샷6개는 각각 `<ENG_TEST>/source-before`, `<ENG_TEST>/final-runtime-source`로 바로잡았다. 이는 초기 시험 자료의 보관 위치 위반 시정이며 생산 파일 이동이 아니다. 이동 전 두 절대 경로가 이번 task의 지정 디렉터리 안에 있는지 확인하고, 이동 후6개 SHA256 동일성을 검사했다. 과거 위치·현재 위치·역할·검증은 두 시험 루트의 `translation-evidence-location.json`/`evidence-location-manifest.json` 및 갱신한 localisation/source manifest로 추적한다. 번역의 새 UI 스크린샷과 검증 보고도 `<ENG_TEST>`에만 둔다.

최종 생산 전용 실행에 대응하는 소스 증거 사본은 저장소13파일을 `<TEST>/final-runtime-source/repository/`, 활성 영어 번역4파일을 `<ENG_TEST>/final-runtime-source/`에 보존했다. 통합 `<TEST>/final-runtime-source/manifest.json`은 총17파일의 원본·사본 경로, 역할, 바이트 수·SHA256을 기록한다. 번역4파일에는 새12키 주 이름 파일과 최종306자 교육 설명을 포함한다. 작업 전 백업과 구별되는 실행 시점 스냅샷이며 배포 패키지가 아니다.

지역 범위가 늘면 이전받는 국가의 기존 공장·인력과 저항·코어 적용이 달라질 수 있다. 이는 건물 보상 복제와 다르며 밸런스가 완전히 동일하다는 뜻이 아니다. V-01은 실제 부모 주의 소유자가 다를 때 제3국 땅에 건설하지 않도록 통제 경계가 분리된다. 기존의 잘못된 교차 주 조회와 모든 상태에서 동작이 같다고 주장하지 않는다.

R-09의 기존 착수 조건은 `controls_state`이며 소유·완전통제 조건으로 강화하지 않았다. `general01`의 여섯 합성 단일 프로빈스 상실 상태는 모두 `owned=1, fully=0, available=1`이었다. 주 controller 전체 상실과 새 주 하나만 미통제인 경우는 차단됐지만, 일부 프로빈스 상실은 기존 조건상 허용될 수 있다. 이것은 이번 정렬에서 새로 추가한 예외가 아니다.

다음은 추가 대상 주의 **1936년 undated history 원시 인구·기존 건물**이다. 실제 가용 인력·야전 인력, 동원법·코어·점령·산업 효율, 이후 on_startup 지급을 계산한 수치가 아니다. 상세46주·소스 경로·해시·행 근거는 `<TEST>/decisions/territory-impact.json`에 둔다.

| 추가 범위 | 주 수 | 원시 인구 | 민간/군수/조선소 |
|---|---:|---:|---:|
| R-03 일본 본토 | 3 | 6,930,521 | 3 / 1 / 1 |
| R-09A 인도차이나 | 5 | 7,865,000 | 1 / 0 / 0 |
| R-09B 필리핀 | 4 | 6,845,116 | 0 / 1 / 0 |
| R-09C 인도네시아 | 14 | 44,322,795 | 4 / 3 / 1 |
| R-09D 말레이시아 | 10 | 4,454,845 | 2 / 1 / 1 |
| R-09E 호주 | 7 | 442,000 | 0 / 0 / 0 |
| R-09F 뉴질랜드 | 3 | 691,297 | 2 / 1 / 0 |

고유46주 합계는 원시 인구71,551,574·민간12/군수7/조선소3이다. R-10은 R-09A와 동일한5주이므로 중복 합산하지 않는다. R-04는 기존 CHI 국가 합병 자체를 유지해 합병 영토 증분은0이지만 새15주의 KCH 코어 적용으로 인력·점령 효과가 달라질 수 있다.

## 바닐라 공유 정의의 등록 확인

R-01(코민테른 접경1028→1090), R-11(소련 내전527↔408→1090↔408)은 loader 계약을 먼저 검증한다. 설치 파일을 수정하거나 전체 데이터베이스 `replace_path`를 추가하지 않는다.

- `loader01`: 외부 fixture에서 익명 constant collection 문법 오류가 발생했다. 관련 결과는 수리 성공 증거로 사용하지 않는다. 유효한 scripted effect 검사에서는 뒤 선언의 단순 교체가 되지 않았다.
- `loader02`: 설치 원본의 explicit `name`이 있는 collection 문법으로 fixture를 수정해 재시작했다. partial `state_groups` 변경으로 목록41·1090포함·1028제외와 다른 두 지역 목록 보존을 확인해 R-01을 적용했다. scripted effect의 직접 호출과 먼저 정의된 caller 모두 두 body를 실행했다.
- `compat_forward01`: 누적 effect의 순서 추적은 두 호출 모두 `trace=12, calls=2`였다. 1090→408 실제 국경분쟁을 만든 뒤 prefix에서 분쟁을 종료하고, 기존 소련 함수가 한 번 실행돼 실제 내전이 시작되는 것을 확인했다. 이 실행의 consumer collection과 허브 판정에는 별도 fixture 오류가 있어 그 결과를 제외한다.
- `compat_reverse02`: 잘못된 진단 collection 선언 순서와 비교 문법을 고쳐 완전 재시작했다. 실제 consumer41개·1090포함/통제·1028제외, 역방향408→1090 정리와 실제 내전 시작, 몽골 실제 startup flag·영토/합병 및 허브8개 각1단계를 확인했다.

최종 호환 파일은 `common/script_constants/zzzz_HOK_KOR_state_reference_constants.txt`(41개 중1028→1090만 교정)와 `common/scripted_effects/00_HOK_KOR_state_reference_effects.txt`(**진단 로그를 제외한29행** 정리 prefix)이다. SOV의 기존597행 본문은 설치 원본에서 그대로 한 번 실행되며 복사하지 않았다. prefix 본문은 원래 두 방향 검사·정리의 네527 참조만1090으로 바꾼 것이다. 검증된 early-first 순서를 파일명으로 유지한다. 초기 전체 함수 복사 후보는 `<TEST>/compat`의 미사용 진단 자료이며 생산 파일이 아니다. 세부 순서·해시 비교는 `compat/R11-promotion-review.json`에 보존했다.

## 실제 검증 기록

다음은 승인한 수리 범위에서 완료한 실제 검증이다. 정적 검사, 강제 효과 시험, 실제 UI, 새 시험 저장 왕복을 구분하며 정상 장기 진행·기존 캠페인 호환을 대신하지 않는다.

| 단계 | 현재 실제 결과 |
|---|---|
| 결정·사건·KCH 독립 소스 검사 | 초기121→최종163 PASS / 0 FAIL(H-01·진단 사본 확인 포함); ordered multi-map·지역4경로·비지리 값 보존. 합성 gate 집합 검사는 엔진 동작 증거와 구분 |
| 몽골·호환 소스 검사 | 초기11→최종13 PASS / 0 FAIL; 허브8·철도11·SOV 정리4참조 외 순서 보존, 최종 prefix29행에 진단/전체 함수 복사 없음 |
| 중점3파일 소스·정적 검사 | 대상8블록·실제 부모·수량·조건 확인. 초기1107→현행1108 PASS / 0 FAIL(terrain cap 정의 검사1개 추가); 1024개 합성 수준 벡터를 포함하며 게임 함수 수가 아님 |
| 지도·현지화·구조 검사 | 초기79→80→현행81 PASS / 0 FAIL; 지도·주24파일 해시와 경로 집합 동일, locale BOM·키·짝 내용·유일 변경 값, 실제1082 전북 수혜, 활성 영어의1086 영문 이름, 호환2파일 구조 확인 |
| 번역 주 이름 정적 검사 | 38 PASS / 0 FAIL; source12키·순서·nam/buk 대응, UTF-8 BOM·영문 헤더, 기존 연구키 및525·1029·1084 영문키 보존. 근거 `<ENG_TEST>/state-name-display/source-validation.json` |
| diff 공백 검사 | 이번 HOK 대상과 활성 영어 번역의 diff 공백 검사 모두 통과 |
| 일반 결정·음성 조건 | `general01`: PASS122/FAIL0; 일반 해방6·누락 주43·주 전체 controller 상실6·쓰시마·일본·KCH15코어·VIN 수락 사본. KCH 수도 단일 seed 검사는 수도 이력 우선순위의 독립 증명이 아님 |
| 해협식민지 원인 관측 | 수정 전 수락 payload를 ENG scope에서 복제 실행. 즉시와 실제1936.1.2.17(약23시간 뒤)에1021·1065가 ENG 소유로 잔류. `hours=1` 후속은 같은 게임 시각에 실행돼 1시간 경과 증거로 쓰지 않음. 최종 H-01 경계 결과는 아래 별도 행 |
| 중점·허브 초기 진단 | 첫 fixture의 잘못된 `level =` 비교와 불필요한0건물 제거 경고를 발견해 수정. 첫 결과는 통과 증거에서 제외. 허브0/1 경계는 `compat_reverse02`, 요새0/3 및 지형 상한·보정된5/7/8은 `final_suite04`에서 확인 |
| 최종 중점 강제 효과·조건 | `final_suite04`, 진단v4:1936.1.1.14에197 PASS / 0 FAIL, `DONE PASSED`. 기대197개·관측197개·고유197개이며 누락·추가0. 세부 분류는 아래 표 |
| 실제 내전·국경분쟁 | 소련 양방향 prefix 정리 후 기존 본문 내전 시작 확인. `final_suite04` 해방6종은 native 결정 활성화·실제 내전 분기 전제·동적 민주 수령국의 지역 전체 소유/완전통제·KOR 종속을 확인. PASS25 / FAIL0,1936.1.1.18에 `DONE native_civil6 failures=0` |
| 최종 H-01 경계 | `final_suite04`, 수락 효과 사본: PASS10회 / FAIL0. ENG 정상 소유·통제, 타국 소유, ENG의 타국 점령, 이미 MAL 소유, ENG 소유 지역 중 적 점령을 검사.1936.1.2.24 즉시 및1936.1.3.23 후속에서 적 점령1021은 ENG 소유/GER 통제 보존, 비점령1065는 MAL 소유/통제로 이전. `DONE H01_boundaries failures=0` |
| 한국어 UI | `focus_h01_03`: 실제 교육 중점 설명·조건5주/지급3주, 해군 중점 효과의 경상남도 우선 문구 확인. 스크린샷은 해당 run의 `screenshots/` |
| 최종 영어 UI | `production_final06`: 진단 모드 없이 HOK→활성 영어 번역만 완전 재시작. D-02의 조건5주·수혜3주 이름이 정상 영문으로 표시돼 `????`가 해소됐고,306자 설명의 마지막 연구25%1회까지 잘림 없이 확인. D-01 효과의 `Gyeongsangnam` 우선 문구도 확인. 증거는 아래 별도 문단 |
| 새 저장·재로드 | `compat_reverse02`에서 새로 만든 시험 저장을 `production_final06`의 생산 전용 영어 playset에서 실제 로드·재저장. 같은 정지 날짜1936.1.29.23에서 비교9 PASS / 0 FAIL. 전후 저장·해시와 실제 후속 파일명은 아래 기록 |
| 기존 저장 | 기존60개 저장 목록은 RT56 등 다른 playset의 저장을 포함해 그대로 보존. 대표 기존 HOK 캠페인 호환의 독립 검증으로 사용하지 않음 |
| 최종 보존·복구·종료 | 기존 저장60/60 SHA256 동일, 설정4파일 exact byte 복구, 소스17/17 최종 스냅샷과 동일. 새 게임 생성 저장은 이번 `temp_temp`1개. HOI4 UI 정상 종료·CIM0, 시험 소유 Notepad19개만 종료 후0·Notepad++ 보존, native Steam 녹색 Play 화면 확인 |

`loader01`의 추가 오류는 외부 진단 fixture 경로에 귀속되며 생산 코드의 실패로 세지 않는다. 기존 baseline은 비활성 Workshop descriptor 경고6행이었다. 이후 실행 로그와 별도로 비교한다.

몽골의 초기 +2h 연결 조회11개는 FALSE였다. 그러나 같은 실행의1936.1.29.23 텍스트 저장에서 허브8개 각1,32개 경로 노드의 rail graph를 확인했다.31/32개 의도한 level2 edge는 지리·차수로 직접 확인됐고, 나머지7676↔7717은 알려진38개 연결 대조로 보정한 인덱스 해석이 지지한다(`STRONGLY_SUPPORTED`). 철도망 전체가 생성되지 않았다는 해석은 반증됐다. 초기 조회 실패의 시점/trigger 원인은 미확정이며 기존 철도11개 명령은 수정하지 않았다. 근거는 `compat/saved-mongolia-review.json`, `saved-rail-constraint-review.json`, `saved-rail-index-order-review.json`이다.

`focus_h01_03`에서 중점 판정95 PASS/38 FAIL이 나왔다. 4개는 진단의 다중조건 `NOT` 묶음, 34개는 실제 terrain cap을 무시한5/7/8단계 기대였다. 실제 source의 조건·수량은 바꾸지 않고 진단만 고쳤다. v3 사본은 `focuses/probe-terrain-not-v3/`에 보존했다. 최종v4는 `NOT={AND={원래 gate}}`, 별도 쓰시마1085에 존재하는 독립 JAP·누락 주 통제의 전제 검사, native terrain cap 관측과 시험 전용 cap 증가 idea를 사용한다. H-01 초기 소유권 전용 guard가 적 점령을 해제하는 것을 old/new 대조에서 확인해 최종 완전통제 guard를 추가했다. 이 중간 결과와 최종 통과 결과를 구분한다.

`final_suite04`는 생산 코드·진단v4·H-01 완전통제 guard를 포함해 완전 재시작했다. 아래 수는 강제 효과·합성 조건 검사의 실행 수이며 중점 수나 정상 UI 진행 횟수가 아니다. 소스·진단 해시는 `final-runtime-source/manifest.json`, `focuses/probe/native-assertions.json`, `decisions/probe/runtime-fixture-manifest.json`에, 실행 로그·프로세스 기록은 `runs/final_suite04/`에 대응시킨다. 이 강제 검사와 별도 `production_final06`의 실제 UI 관측·저장 왕복9개 비교·설정 복구를 구분한다.

| 중점 검사 묶음 | PASS / FAIL | 확인한 범위 |
|---|---:|---|
| R-06 | 8 / 0 | 해주13438 포함7항구 각 해안요새3, 옛 비해안13419는0 |
| R-03 | 9 / 0 | 독립 JAP 존재, 본토13주, 신규3주 각각 누락 시 차단·통제 전제, JAP 종속국 대안 |
| R-10 | 12 / 0 | FRA9주 경로, 신규5주 각각 누락·분기 전제, VIN 종속국 대안 |
| V-03 | 3 / 0 |9주 우회,1017 누락 전제와 우회 차단 |
| native 수준·상한 보정 | 13 / 0 | 기본 지형 상한, 시험 idea 적용, 실제5/7/8 수준, 시험 idea 제거 |
| R-07 | 4 / 0 |527/1083의 각 요새3, 외국1083의1003 지급 차단, 평양 지급 유지 |
| V-01 | 90 / 0 |2개 중점의 실제 효과·혼합 수준·pool 전제,610/609 외국 통제,1039 ROOT/MEN/제3국 경로 |
| V-02 | 58 / 0 |684의 해안11프로빈스, 기본0/5/한곳4 혼합, 보정 후 한곳4/나머지5 경로와 전제 |
| 합계 | 197 / 0 | 기대·관측·고유 label 일치, 누락·추가0 |

지형 상한은 설치 원본 `common/terrain/00_terrain.txt`에서 forest·mountain의 육상요새4, plains의 육상요새5, 해안요새6을 확인했다. 실제 mountain1137에서 요청0·3·5는 각각0·3·4로 관측됐다. 0은 `<1` 참,3은 `>2`/`<4` 참 및 `<3`/`>3` 거짓이므로 이번 건물 쿼리의 비교는 strict이며0도 관측 가능했다. 이후 외부 시험용 JAP idea에 native CZE/FRA와 같은 종류의 `bunker_max_level_terrain_limit`·`coastal_bunker_max_level_terrain_limit`를 각10 부여하고, bunker1137·coastal3900의 실제5·7·8을 모두 확인한 뒤 혼합 수준을 검사했다. idea는 각 묶음 뒤 제거·부재를 확인했으며 생산 파일에는 없다. 기본 V-02에서는4+2와5+2가 모두 실제 상한6에 도달했고, 시험 idea 아래에서는 각각6·7이 됐다. native 정의·프로빈스 terrain·상한 해시는 `focuses/probe/native-assertions.json`에 기록한다.

V-01의 원인 해석도 실행 결과에 맞춰 제한한다. 수정 전5프로빈스 pool 블록을 별도로 복제한 대조는 같은 all-owned·상한 보정 조건에서 두 중점 모두 all-low/6969-only-low/609-only-low 때6969·11822의3단계 증가를 관측했고, 모두5인 경우에는 증가하지 않았다(16개 관측). 따라서 **6969를609 아래 둔 기존 pool의 부모 불일치가 이 엔진에서 반드시 조회·건설 실패를 일으켰다는 주장은 반증됐다.** 별도1039 보상의 옛611 부모는 이 old-block 대조 대상이 아니다. 이번 V-01은 현재 부모 정렬과 실제610의 ROOT 완전통제 경계를 명시한 변경이며, 소유자가 다를 때도 옛 코드와 동작이 같다는 뜻은 아니다. 대조는 원래 블록의 실행 관측이며 바닐라 단독·정상 진행 전체를 입증하지 않는다.

해방 내전25회 검사는6종 각각의 착수 가능·실제 내전 분기 전제·동적 수령국 전체 지역 결과18회와 호주/뉴질랜드 제외 해외령7회다. 동적 태그의 원래 국가·민주주의·KOR 종속·소유 및 완전통제를 함께 요구했다. H-01의10회는 전제 검사 반복을 포함하며 고유10개 시나리오가 아니다. 수락 효과는 실제 option의 순서를 유지한 사본에서 이름·AI 확률만 제외했으므로, native 외교 사건 전달·사용자 선택 경로와 구별한다. 두 해협 주는 각각1프로빈스여서 부분 점령 시험은 주 내부 분할이 아니라1021만 적 점령/1065는 ENG 통제인 지역 단위 혼합이다. 원래 수락 사본과 최종 수리 사본의 직전 소유·통제·전쟁·종주국 관측이 일치했고, 최종 guard는 적 점령1021을 보존하면서1065만 이전했다.

내전 검사 도중1936.1.1.18에 D04–D09 각각 `valid capital state`/`capital_scope: invalid event target` 경고가1쌍씩, 총6쌍12행 발생했다. 호출 위치는 설치 원본 `common/on_actions/12_wuw_on_actions.txt:3095`의 `on_annex` 내 `FROM = { capital_scope = ... }`이며 HOK·활성 번역·외부 fixture가 이 파일을 덮어쓰지 않는 것을 확인했다(`CONFIRMED` 출처). 강제 seed·연속 native 활성화의 영향인지, 기존 size1 내전 경로의 일시 상태인지, 새 지역 참조와 관련되는지는 `UNPROVEN`이다. 바닐라 단독 또는 정상 UI 경로의 대조 재현 없이 HOK 고유 결함이나 진단만의 무해한 경고로 단정하지 않았다. 이 경고를 숨기려고 생산 on_action·수도·내전 동작을 수정하지 않았다. focus 진단의 잘못된 비교·없는 건물 제거·시험 idea modifier 관련 경고는 최종 실행에서 없었다.

생산 전용 `production_final06`은 활성 HOK+영어 번역2개, DLC36개, 엔진 `v1.19.4.2.2da5 (add6)`이며 마지막 정지 날짜는1936.1.29.23이다. 이번 주 참조·영문 주 이름 수리의 새 관련 실패, unknown effect/trigger, invalid state/province, 외부 fixture 실행은 발견하지 못했다. 다만 전체 로그가 비어 있지는 않다. `error.log`1–6행은 기존 비활성 Workshop descriptor 경고,8행은 작업 전과 SHA256이 같은 HOK `map/buildings.txt:66858` 경고이며 이전 실행에도 있었다. map 경고의 정확한 원인은 미확정이다.9–13행은 로그·continue 파일·저장 rename `errno2`5행으로, 실제 생성된 저장과 검증 결과를 아래에 구분했다. I/O 원인은 `UNPROVEN`이다. 기존 함장13키의 중복26행과 이전 기록에도 있던 ConflictRisk, `graphics.log`의 `Too small river`, 기존 저장3개의 형식 경고는 별도 잔여로 남는다. 임시1086 중복2행은 전용 주 이름 파일로 정리한 최종 실행에서 사라졌다. 이 구분은 기존 경고를 무해하다고 판정하거나 HOK 전체와 무관함을 입증한 것이 아니다.

영어 UI의 초기 `production_reload05`에서는 분할 주의 고유12키가 번역 모드에 없어 일부 조건·보상이 `????`로 표시됐고, 긴 D-02 설명은 마지막 연구 보너스가 잘렸다. 활성 번역에 source12키를 같은 순서로 추가하고, D-02는 계기 읽기·시민권 교육 문장을 남긴306자 설명으로 줄였다. Gyeonggi와 전라·충청 남북의 소유/완전통제 조건, Gyeonggi·Jeollabuk·Chungcheongnam만의 부지 조건과 각 슬롯2/민간공장2, 전자공학25%1회는 유지했다.327자 중간 초안도 `<ENG_TEST>/focus-description/source-before-327/`에 보존했고, 최종 값·SHA256·BOM/CRLF·다른 문장 byte 보존 검사는 `focus-description/compact-education-final-report.json`에 기록했다.

`production_final06`에서는 `settings.txt`와 `pdx_settings.txt`를 모두 영어로 맞춘 뒤 생산 전용 playset을 완전 재시작해 관측했다. D-02의 Gyeonggi·Jeollabuk·Jeollanam·Chungcheongnam·Chungcheongbuk 조건과 Gyeonggi·Jeollabuk·Chungcheongnam 보상 이름,306자 설명 전체, D-01의 `Gyeongsangnam` 우선 문구를 실제 화면에서 확인했다. 증거는 `<ENG_TEST>/screenshots/after-english-civic-state-names.jpg`, `after-english-civic-description.jpg`, `after-english-naval-priority.jpg`다. 나머지 주 이름의 정적 대응까지 확인한 것을 모든 주의 개별 UI 관측이나 정상 장기 진행의 증거로 확대하지 않는다.

## 저장 정책과 검증 한계

지도·영구 ID·완료 이력과 기존 국토개발의 신·구 저장 분기를 유지한다. 완료 보상·코어를 자동 재지급하거나 일회 결정을 다시 여는 마이그레이션은 없다. KCH 수도 이력은 새 생성/초기화 경로의 참조이며 기존 저장의 수도를 강제 변경하지 않는다. 9주 지도 저장 마이그레이션, 모든 DLC 조합·장기 AI·멀티플레이는 이 변경의 검증 범위를 자동 확장하지 않는다.

새 시험 저장 왕복은 `<TEST>/compat/roundtrip-save-review.json`에 기록했다. 최초 `compat_reverse02` 저장과 `production_final06` 재저장은 엔진 `Operation Postern v1.19.4.2.2da5`와 정지 날짜1936.1.29.23이 같고, 진단 모드를 제거한 playset의 차이로 checksum은 `f223`→`add6`이다. MON 소유11주의 산업·자원·인구·슬롯·소유, 허브8개, 저장된 rail graph3194노드 전체, world flag 값·날짜,1090/408의 소유·국경분쟁 필드, game rule이 같아 해당 비교9개가 통과했다. 이 관측 범위에서는 로드·재저장 때 보상이 다시 지급되지 않았다. 활성 내전 관계 전체, 관련 없는 저장 필드, 기존 사용자 캠페인이나 장기 진행의 검증은 아니다.

native 저장 UI에서는 백업·검증한 이번 시험 소유 저장을 선택해 Overwrite했다. 엔진이 rename `errno2` 경고와 함께 실제 후속 파일 `KOR_1936_01_29_23_temp_temp.hoi4`를 생성했으므로, 처음 이름에 정상 덮어쓰기됐다고 기록하지 않는다. 전후 외부 사본은 각각 `<TEST>/runs/compat_reverse02/saves/KOR_1936_01_29_23_temp.hoi4`와 `<TEST>/runs/production_final06/saves/KOR_1936_01_29_23_temp_temp.hoi4`에 보존했다. 후속 파일 SHA256은 `013fe6c8cc1ee459f90c984217c5d8e157f440a98c03b794828e2337d0600521`이며9개 비교는 실제 생성된 후속 파일을 사용했다. 이 저장 경고를 숨기기 위한 생산 코드나 기존 저장 수정은 하지 않았다.

세션 종료 검사는 `<TEST>/final-session-review.json`에 보존했다. `dlc_load.json`, `gameplaysettings.txt`, `pdx_settings.txt`, `settings.txt`4개가 원래 바이트와 같고, 기존 저장60개와 최종 생산/번역 소스17개가 각각 작업 전 목록·최종 스냅샷의 SHA256과 일치했다. HOI4는 native UI로 정상 종료한 뒤 CIM0을 확인했다. 이번 시험의 Notepad19개는 PID·시작 시각·명령행과 오류창을 확인한 뒤 해당 프로세스만 종료했고, 최종 Notepad0·기존 Notepad++ 보존을 기록했다. native Steam의 녹색 Play 버튼은 `<TEST>/root/screenshots/steam-play-after-tests.jpg`에 보존했다. 임의의 모든 창·프로세스·외부 자료를 정리했다는 뜻은 아니다.

번역 지침에 따른 일회 도구 정리는 이번 작업 소유인 `<TEST>/root/patch_localisation.py`, `english_recipient.py`, `correct_recipient_wording.py`3개에 한정했다. SHA256과 역할을 기록한 뒤 삭제했으며 근거는 `<ENG_TEST>/one-off-helper-cleanup.json`이다. 교육 설명 수정의 별도 일회 helper도 해당 전용 경로에서 제거한 것을 보고서에 기록했다. 나머지 재현 fixture·백업·로그·스크린샷은 보존한다.

기존 시험 PNG4개·815,391바이트(`docs/assets/korean-fascist-mobilization-validation-20260923/`)는 미정리로 남겨두었다. 이번 작업은 해당 정리를 승인하거나 수행하지 않는다. 신규 시험 자료는 `<TEST>`·번역 전용 `<ENG_TEST>` 및 게임이 생성하는 실제 사용자 데이터에만 둔다. 커밋·푸시·Workshop 업로드는 수행하지 않는다.
