# 2026-10-31 민간 핵 연구 중점 구현·검증 기록

갱신: 2026-11-11 (Asia/Seoul). 상태: **첫 중점의 핵 기술 연구 보너스150% 추가 / 기존 선행 연구 불이익2년 감소1회·핵1.00 유지 / 첫35일·둘째245일 / 새 보상의 런타임 미검증**. 2026-10-31에는 첫 `reduce_focus_completion_cost` 블록을 제거한 뒤 선행 감소만 있는 `add_tech_bonus`를 추가했고, 2026-11-11에는 같은 블록에 연구 보너스를 추가했다. 새 혜택과 감산 없는245일의 HOI4 런타임은 검증하지 않았다. 아래 `ff98`·`1b1c`의240회 진행·건설·재로드·통과 등은 2026-10-31 감산 제거 전 이력으로 보존한다. 기존 저장 감산은 자동 회수하지 않으며 기완료 첫 중점의 새 보상도 자동 소급하지 않는다.

## 기준과 변경 범위

아래 기준선·해시·실행 수치는 2026-10-31 당시 기록이다. 2026-11-11 변경은 별도 후속 절에 기록한다.

- 브랜치/HEAD: `feat/korean-focus-expansion-ai` / `860efe7a3513148dc6964b7e0e3dfafd19addfb7`.
- 대상: **Operation Postern v1.19.4.1.99a5 / Steam build26282552 / 인식 DLC36개**. 최종 정수 방식 실행 체크섬은 `ff98`, 이전 소수 후보는 `7d94`다. 앞선 기능 연동의1.19.3/build25205862 결과를 재사용하지 않는다.
- 새 모듈 전 중점 소스는472개, SHA-256 `440D76ED0395CC84EDD0EE320CE0376E27D5B7D328F0F65D1BA1CB6454ED52E9`다. 해당 바이트는 외부 `validation/baseline-korea-440D.txt`로 고정했다.
- 새 두 정의를 추가해 **474개·절대 기준7개·상대467개·정치 offset7개**가 됐다. 기존 x0~211/y0~24 안의 서울대 아래 `(14,3)→(14,4)` 가지다.
- 2026-10-31 선행 감소 추가 직후 소스 SHA-256은 `3CC9F676203E18F53B7B6A896ADBD9E03796B861D492326E48056EC5E3A122CA`다. 외부 `C:/hoi/test/civil-nuclear-ahead-bonus-20261031/change-record.json`에 당시 `add_tech_bonus`6줄·기여 주석1줄 추가 외 직전 소스 보존을 기록했다. 당시 `ahead_reduction=2 / uses=1 / category=nuclear`, 이름은 첫 중점 현지화 키였고 별도 연구 속도 보너스·자동 기술 지급·기완료 저장 소급은 없었다. 이때 새 런타임 없이 소스 대조만 수행했다.
- 직전 감산 제거 소스 SHA-256은 `F3C4FC60688C6451D396EF494BF9A7AB1FD834CABE139DBFD25301C2EDDD1156`다. 외부 `C:/hoi/test/civil-nuclear-discount-removal-20261031/change-record.json`에 감산4줄 삭제·두 기여 주석 정정 외 바이트 보존을 기록했다. 두 후속 변경에서 사용자가 실행 중이던 게임·프로필·저장은 변경하지 않았다.
- 감산 제거 전 검증 소스 SHA-256은 `ECA5D4FC171962DE94128A9E72D5CEB2BB4E65EF213A1AD31BD4D1345BC0AE7E`다. 당시에는 둘째 `cost=35`의 기본245일에서 필수 첫 완료가 대상 한정5일을 감산했고, 해당 실행 중 생산 스크립트 수정은 없었다.
- 실패 후보 `cost=34.286` 소스 SHA-256은 `FBB156FCB108E043C8961B1AC60A3578DA32D067C9DE7146FDB87F6AE0CAB212`로 별도 보존한다. 기존 연구망 helper는 `185874FC8EEE0A5256E654ECF25EAFD258C487D8E8DA53EAFF5C579B43DCEE87`로 유지한다.
- 진단·저장·화면 증거의 외부 루트는 **`C:/hoi/test/civil-nuclear-20261031/`**다. 이전 기능 연동 자산 검수 자료는 그때의 외부 폴더에 별도 보존했다.

사용자가 승인한 서울대학교 확장 → 핵분열 연쇄반응 실험 → 민간 원자로 투자를 구현했다. 2026-11-11 후속 변경까지 반영한 첫 중점은 기본35일과 핵 분야 `add_breakthrough_progress value=1.00`, 핵 기술 연구 보너스150%·선행 연구 불이익2년 감소1회를 제공한다. 둘째는 감산 없는 기본245일, 핵 연구·GDR 조건 아래 민간 원자로 **건설 기술만** 지급한다. 첫 보상에 일반 핵 기술을 섞거나 둘째에서 프로젝트·시설·과학자·무료 건물을 지급하지 않는다. 기술 기보유 bypass, 조건 무효 시 취소 설정을 넣었으며 기존 무궁화75%와 연구망 보상을 유지한다. [현재 구현 명세](../HOK_KOREAN_CIVIL_NUCLEAR_RESEARCH_SPEC.md)를 따른다.

게임플레이 소스는 `common/national_focus/korea.txt`, 문구는 새 `HOK_KOR_civil_nuclear_research_l_*.yml` 쌍, 그림은 새 내부 DDS·GFX다. [그림 출처](../HOK_KOREAN_CIVIL_NUCLEAR_ICON_CREDITS.md)와 [매니페스트](../data/HOK_KOREAN_CIVIL_NUCLEAR_ICON_MANIFEST.json)는 AI 생성 원본·전문 프롬프트·기계적100×88 변환·원본 광택의 재사용을 구분한다. 원본 설치·Workshop·기존 기술·프로젝트·중점 기간 전역 define은 수정하지 않았다. 커밋·푸시·게시 작업도 수행하지 않았다.

## 2026-11-11 후속 — 150% 연구 보너스

사용자는 설명 검토 후 구현을 승인했다. 시작 소스는 `feat/korean-focus-expansion-ai` / HEAD `1c2e5423c08677228fa89c0181535bc30fc5764d`, 작업 트리는 변경 없음이었다. 첫 중점의 기존 `add_tech_bonus` 블록에 `bonus=1.5`와 `#20261111_kpopmodder` 기여 주석을 추가했다. 기존 `ahead_reduction=2 / uses=1 / category=nuclear` 및 이름을 유지해 동일한1회 보상에 연구 혜택을 더한다. 2년은 보상 유효기간이 아닌 선행 불이익 감소량이며, 선행 불이익이 없어도150% 연구 혜택을 받도록 하는 의도다.

설치본 메타데이터는 `Operation Postern v1.19.4.2.2da5 (0bdb)`다. 같은 설치본의 `common/national_focus/toa_shared_military_branch.txt:1568–1574`는 `nuclear` 기술의 `ahead_reduction=2`와 `bonus=1`을 같은 블록에 두며, `localisation/korean/effects_l_korean.yml:92`는 선행 감소와 연구 혜택의 함께 표시를 정의한다. 이는 소스 문맥의 근거이고 이번 보상의 실제 실행 증거가 아니다.

런처 descriptor `hearts of korea.mod`의 실제 선택 경로는 `C:/hoi/hearts_of_korea`다. 활성 순서는 저장소 → `C:/hoi/Hearts of Korea English Translation Anime Modder's Edition`, 언어는 `settings.txt`의 `l_korean`이다. 활성 번역은 해당 중점의 이름/설명을 덮어쓰지만 `common/national_focus/korea.txt`나 `EFFECT_ADD_TECH_BONUS`를 덮어쓰지 않는 것을 소스 검색으로 확인했다. 이 설정·파일 확인은 새 런타임 관측이 아니다.

후속 증거 위치는 `C:/hoi/test/fission-research-bonus-20261111/`다. `korea.before.txt`는 변경 전 소스 증거 사본이고 `change-record.json`은 전후 해시와 두 줄 외 보존을 기록한다. 작업 원본은 저장소 `common/national_focus/korea.txt`다. 변경 전 SHA-256은 `fcab533936d55625692b6a58422c6556713a45e0dbdb344b0004262d0e9eb85b`, 변경 후는 `f2a26c497ce1d7bad49410f7e6c66d88ba1a72c942477f18ea36aab1658f5c26`이다. 생산파일은 기여 주석과 `bonus=1.5` **2줄 추가·삭제0** 외 바이트 동일을 확인했으며 `git diff --check`는 종료코드0이었다. 새 표시 경로 없이 기존 효과의 숫자만 추가한 범위에 맞춰 소스 보존·원본 동일 문맥 대조까지 수행했다.

2026-10-31의 `civil-nuclear-20261031/`, `civil-nuclear-discount-removal-20261031/`, `civil-nuclear-ahead-bonus-20261031/`는 당시 증거 원본 위치로 계속 유지하며 새 결과로 대체하지 않는다.

| 대상 | 처리 판정 | 확인·한계 |
|---|---|---|
| 첫 연구 보상 | **변경** — `bonus=1.5` 추가 | 새 실제 UI·연구 적용·소모는 미검증 |
| 핵1.00·선행2년·사용1회·핵 기술 범위·이름 | **의도적 유지** — 기존 혜택과 범위를 보존 | 두 줄 외 소스 바이트 동일 확인 |
| 선행·기간·AI·배치·그림·둘째·기존 연구망과 무궁화 | **의도적 유지** — 이번 보상 추가 외 변경 없음 | 생산파일 두 줄 외 보존 확인. 과거 정상 진행 결과와 구분 |
| 두 본체 현지화·활성 번역 문구 | **의도적 유지** — 이름 재사용, 숫자는 엔진 효과 표시 | 현지화 수정 없음. 번역의 자동 효과 문구·중점 소스 덮어쓰기 없음 확인. 새 표시 미검증 |
| 기완료 저장·기존 보너스·새 저장 왕복 | **미확인** — 소급/변환 코드 없음 | 실제 지급·소모·직렬화·재로드 미검증 |

게임 실행·강제 효과 진단·기존 저장 수정·커밋·푸시·업로드는 이 후속 변경에 포함하지 않았다. 아래 과거240회 진행과 저장 검증을 새150% 보너스 검증으로 재사용하지 않는다.

## 감산 제거 전 검증 이력 — 소스·자산 확인

`validation/source-review-cost34_286-01.json`은 당시 후보의 **503 PASS / 0 FAIL**이다. 고정된472개 기준선과 비교해 기존 본문 바이트·ID·순서·조건·배치·보상·AI 보존과 새 두 정의를 확인했으나 실제240일 완료는 입증하지 못했다. 새 정수 비용·감산 전략의 소스 확인으로 재사용하지 않는다.

최종 `validation/source-review-integer35-minus5-01.json`은 **506 PASS / 0 FAIL**이다. 동일한 기존472개 보존과 함께 정수35·첫 완료 감산5·핵 보상 유지의 최종 소스를 확인했다. 소스 검사와 아래 실제 진행 증거를 구분한다.

자산 검수 **28 PASS / 0 FAIL**은 별도다. 두100×88 알파 DDS, 프로젝트 내부 일반·광택 sprite와 마스크·오버레이 경로, 정확한 대소문자, 원본 sprite 비덮어쓰기와 선택 원본의 사본을 확인했다. `ba03` 후보의 실제 초기 HIDE 화면에서 새 가지와 인접 명판·아이콘·연결을 확인했지만 SHOW·정치 분기 변경·완료 광택·모든 클릭 영역까지 검증했다고 주장하지 않는다. 화면은 `runtime-ui/clean-new-branch-initial-hide.jpg`다.

## 기간 후보와 실제240일 표시

원본 `FOCUS_POINT_DAYS=7`은 비용1당7일을 정의한다. 다음 두 소수 비용은 전체 재시작해도 실제 UI에서239일이었다.

| 비용 | 관측 | 화면 |
|---|---|---|
| `34.285714` | 239일 | `candidate-cost-34_285714-shows-239-days.jpg` |
| `34.2857142857142857` | 239일 | `candidate-long-literal-still-239-days.jpg` |
| `34.286` | **UI240일, 실제240/240에도 활성** | `cost-34_286-shows-240-days.jpg`, `second-240-of-240-still-active-Nov24-18.jpg` |
| 정수35 + 첫 완료5일 감산 | **UI240일, 최종240번째 일일 진행에 완료** | `integer35-minus5-after-normal-first-shows240.jpg`, `integer35-minus5-normal-completion-Nov30-14.jpg` |

화면은 외부 `runtime-ui/`에 있다. 올바른 중점ID·240일·기술·DLC·보상 문구를 확인했지만1936.11.24.18 저장은 `progress=240`, 둘째 `current` 유지·`paused=no`였다. 저장 SHA-256은 `B3393F487BD9CF99A4D3D7E6735172A8A33522334B528AD55B6AF03CD8177722`, 원문 판독은 `validation/second-progress240-still-active-Nov24-18-focus.json`이다. **UI240일은 실제240일 완료를 보장하지 않았으며 이 후보는 최종 방식이 아니다.** 내부 숫자 표현·정확한 최종 완료 날짜를 이 관측만으로 추정하지 않는다.

당시 구현은 둘째 정수 비용35(기본245일)와 첫 완료의 대상 한정 `reduce_focus_completion_cost cost=5`를 조합했다. 효과의5는5일이며 중점 선언의 비용5주와 다르다. 첫 핵1.00 보상을 유지하고 둘째의 실효 기간만240회 일일 진행으로 만들었다. 원본 효과 문서는 `documentation/effects_documentation.md:5709–5722`다. 후속 요청으로 이 감산만 현재 소스에서 제거했고245일을 수용했다.

감산 제거 전에는 첫 완료 전 잠긴 둘째가 기본245일, 첫 완료 후 실제 시작 가능한 시점에는240일로 표시됐다.

## 소수 후보 당시 첫 중점 정상 완료·원시 혁신 보상

외부 준비 모듈은 기존 서울대 부모만 완료하여 기존 연구 슬롯을 제공했다. 새 두 중점이나 핵 연구 기술·시설·과학자·혁신을 강제 지급하지 않았다. 첫 중점은 실제 UI로 선택하여 정상 진행했다. 수동 시작 보고는1936.1.1.12, 활성 저장은1.1.17이며 이 저장에 진행도1이 기록돼 있다.

일회 일일 관측기가 완료를 처음 본 시각은1936.2.4.02다. 실제 완료 팝업 확인과 완료 저장은3.29.9로 지연됐다. 따라서 이 시각을 정확한 완료 순간으로 합치거나 비축0에서35일이 정확히 경과했다고 주장하지 않는다.

| 저장 | SHA-256 | 관측 |
|---|---|---|
| `saves/first-active-before-reward-Jan1-17.hoi4` | `57ECFCBB694B83886D08589CF8CD98A3DB0DAB1BFED495B7F3FF1DB27073B4B5` | 첫 중점 활성, 핵 원시값0 |
| `saves/first-completed-before-atomic-Mar29-09.hoi4` | `2D91B4534E67188078673A8F9BB072BE643376D5E46112801AFE2BFFB4D30BAC` | 첫 완료1회, 둘째 미완료, 핵 원시값10000 |

`countries/KOR/program_status/breakthrough`에서 핵은 **0→10000**, 육군·해군·항공은 각각0으로 같았다. `validation/first-normal-reward-assessment.json`의 **9 PASS / 0 FAIL**은 이 제어된 `value=1.00` 보상의 실제 저장 차이와 완료 상태를 확인한다. 기반 raw-diff JSON의 SHA-256은 `100CC8BAC91B3AC09E7633855051C1E1840C2AEAE189547CDE8C642860EED4D9`다. 보편적인 원시단위 환산이나 관측기의 점수 역치 로그를 정확한 수치 증거로 쓰지 않는다.

독립 `validation/research-state-immutable-baseline.json`의 **37 PASS / 0 FAIL**은 첫 보상 전·후·둘째 시작 저장을 사용해 원래 과학자 소유·역할·수준, KOR 시설 program 목록, 프로젝트 등록·완료 상태와 단계별 지정 기술 상태를 고정했다. 둘째 시작을 위해 나중에 준비한 핵 연구 기술까지 처음부터 동일했다고 주장하지 않는다. 이는 둘째 완료 전의 기준선이며 모든 실제 프로빈스 건물의 보존이나 최종 건설 결과 증거가 아니다.

## 둘째 비축0 제어 시작과 소수 후보 실패

첫 완료 뒤 유휴 저장에는 비축10이 있었다. 원본 저장을 보존한 채 승인된 **합성 사본**에서 관측된 `countries/KOR/focus/progress` 한 값만10→0으로 바꿨다. `validation/synthetic-zero-bank-Mar29-09-manifest.json`은 해당 숫자 이외의 접두·접미 바이트 동일을 확인한 **8/0** 기록이다. 날짜·완료 기록·기술·혁신·시설·과학자·다른 세계 상태를 이 단계에서 바꾸지 않았다. 합성 비축0을 자연 상태라고 부르지 않는다.

그 사본을 실제 로드한 뒤 준비 결정으로 `atomic_research`를 취득시켰다. 이는 정상 연구 완료가 아닌 시험 조건 준비다. 그 후 실제 둘째 UI를 선택했다. `saves/second-start-zero-bank-Mar29-09.hoi4`, SHA-256 `480AF033049055B0C63CC2582798AD3BFA786D34E1F1D068D51E00A70AE99E16`에는 둘째가 활성·비일시정지 상태로 기록돼 있다. 활성 중점의 progress 필드 생략을 단독으로0이라고 추정하지 않으며 사전에 준비·로드한 제어 기준선과 실제 시작 기록을 함께 사용한다.

이후 생산 중점을 실제 진행시켰으나 위240/240 활성 잔류가 나타났다. 기술은 결국 원본 획득 시각1936.11.25.01에 지급되어 목표보다 한 차례 늦은 일일 진행이었다. 완료 효과를 강제로 실행하지 않았다. 이 저장·관측을 최종 정수 전략의 성공으로 재사용하지 않는다.

이전 후보의 Nov26.20 저장은 KOR focus 본문이 비어 서울대·첫 중점까지 완료ID가 사라졌다. `validation/candidate-34_286-completed-reward-assessment.json`은 **13 PASS / 1 FAIL**이며 실패는 완료 기록 보존이다. 이전 실행에 소스/디버그 편집이 섞였을 가능성은 있으나 원인은 **UNPROVEN**이다. 실패를 통과로 바꾸거나 최종 고정 소스의 실행 결과로 귀속하지 않는다.

## 최종 ff98의 정상240회 진행·기술 지급

최종 소스로 전체 재시작한 뒤 이전 `7d94`의 첫 활성 Jan1.17 저장을 `ff98`에서 불러왔다. 입력 저장의 체크섬 차이를 숨기지 않는다. 첫 중점을 새 소스 아래 정상 완료해 핵 원시값10000 유지와 대상 감산5 직렬화를 확인했다. 첫 완료 저장 Apr4.19의 유휴 비축10만0으로 만든 별도 승인 합성 사본을 실제 로드했다. `validation/integer35-minus5-zero-bank-Apr4-19-manifest.json`은 다른 바이트와 감산5의 보존을 기록한다. 핵 연구 기술은 둘째 시작 전에 시험 준비했고 민간 기술이나 중점 완료는 강제 지급하지 않았다.

| 단계 | 실제 저장·판정 | 확인 범위 |
|---|---|---|
| 첫 정상 완료 | `saves/integer35-minus5-first-completed-Apr4-19.hoi4`, `integer35-minus5-first-discount-ff98-assessment.json` **18/0** | 핵 보상·둘째 감산5, 첫 완료 기록 |
| 둘째 실제 UI 선택 | `saves/integer35-minus5-second-start-Apr4-19.hoi4`, `integer35-minus5-second-start-ff98-assessment.json` **18/0** | Apr4.19 활성, 시험 준비한 핵 연구, 민간 기술 미보유 |
| 239회 진행 | `saves/integer35-minus5-progress239-Nov29-09.hoi4`, `integer35-minus5-progress239-ff98-assessment.json` **20/0** | 원시 진행239, 둘째 활성, 민간 기술 미보유 |
| 정상 완료 | `saves/integer35-minus5-completed-Nov30-14.hoi4`, `integer35-minus5-completed-ff98-assessment.json` **18/0** | 실제 완료 팝업, 완료ID1회, 기술 수준1, 원래 연구 상태 보존 |

판정 파일은 외부 `validation/` 아래에 있다. 첫 완료 저장 SHA-256은 `CC659E1724C4CB61C02F2153613E7FEFDD0389A668CD17ACD4AE241650B72B78`, 둘째 시작은 `37FCEFA0049F90FAEC522F9E870DFFF6D479D5ABAFCB89C1722151BE4B84C4AD`, 완료 저장은 `E962056B3BF64FBD69B748167F5DF10F628C14ABF969724240C98E17310F41D0`이다.

민간 기술의 원본 획득 시각은 **1936.11.30.01**이다. Nov29.09의 진행239와 교차한 `validation/integer35-minus5-normal240-final-evidence.json`은 **14 PASS / 0 FAIL**이다. 다음날01시부터의240번째 일일 진행과 일치하며 Apr4.19부터 경과한 실제 시간은 **5742시간=239일6시간**이다. 이를5760시간의 정확한 경과로 표현하지 않는다. 첫 중점의 정확35×24시간도 아직 입증하지 않았다.

완료 저장은 서울대·첫·둘째 완료ID를 각각1회 보존했다. 핵 원시값10000과 나머지 세 분야0, 기존 과학자4명의 소유·역할·수준, 등록 프로젝트49개의 원문, 시설 program0을 확인했다. 프로젝트 착수·완료나 새 과학자·시설 program 보상은 없었다. 이는 열거한 연구 상태의 보존이며8개월간 전체 국가·세계가 바이트 동일하다는 주장이 아니다. 각 단계 판정은 겹치므로18/18/20/18/14를 독립 검증 수로 합산하지 않는다.

## 실제 민간 원자로 건설 사용

주 작업자가 완료 후 실제 건설 메뉴에서 민간 원자로 해금을 확인하고 강원에 일반 클릭으로 **대기열1개**를 추가했다. 화면은 `runtime-ui/final-commercial-reactor-build-unlocked.jpg`와 `final-commercial-reactor-queued-Gangwon.jpg`다. 기술 지급을 실제 건설에 사용할 수 있음을 확인했으며 무료 건물·완성된 원자로·프로젝트 완료를 지급한 것은 아니다. 저장 비교 자체와 별도로 실제 UI 관측을 기록한다.

`validation/integer35-minus5-commercial-queue-assessment.json`은 **17 PASS / 0 FAIL**이다. 완료 저장과 같은 Nov30.14의 `saves/integer35-minus5-commercial-queue1-Nov30-14.hoi4`를 비교해 강원1029의 민간 원자로 대기열1개(`amount=1`)와 완성 수준0을 확인했다. 대기열 저장 SHA-256은 `CC3DE55E98CD046ED60FDDE70948EF1429B51938738D8A5037CFAD0FA77DF06E`다. 초기 진행 필드 생략을 원문에 존재하는 `progress=0`으로 쓰지 않으며, 기술·완료ID·열거한 연구 상태는 같은 시각에 보존됐다.

## 임시 진단 없는 두 모드 전체 재시작 — 메인 메뉴

주 작업자가 생산 모드만으로 전체 재시작하여 메인 메뉴 도달을 확인했다. `dlc_load.json` 순서는 **Korean Language(`ugc_2743487021`) → 저장소(`hearts of korea`)**, 비활성 DLC 목록은 비었으며 실제 로그는 DLC36개·모드2개다. 새 모듈의 임시 `HOK_CNUC` 실행 흔적은 없었다. 한국 새 게임 로드와 저장 재로드는 이 메인 메뉴 판정에 포함하지 않는다.

외부 `clean-two-mods-1b10/`에 로그20개·실제 로드 설정·두 launcher·각 파일 해시를 보존했다. 최초 UI 판독은 마지막c를0으로 읽었으며, 주 작업자의 확대 재확인 결과 **UI와 system.log 모두 `1b1c`**다. 폴더명1b10은 기존 보관 식별자로만 유지하며 체크섬 충돌로 취급하지 않는다. `validation/clean-two-mods-1b10-log-assessment.json`은 **9 PASS / 0 FAIL**이다. 같은1.19.4.1의 `control-current-1.19.4.1`과 비교해 error.log **45행→45행, 정규화 추가0·제거0**, text.log도 추가0·제거0이었다. 최초 시각과 기존 한국 중점의 이동한 줄 주소만 정규화하고 날짜·내용·중복 횟수·그 외 줄 주소는 유지했다. 기존 오류가 사라졌다는 판정이나 전체 모드 무오류 주장은 아니다. 실행 중 로그를 순서대로 복사했으므로 원자적 파일시스템 스냅샷도 아니다.

## 두 모드 실제 재로드·같은 시각 재저장

위 전체 재시작 `1b1c`에서 실제 UI로 대기열 추가 후의 자기 저장을 로드하고 시간 진행 없이 Nov30.14에 재저장했다. `validation/clean-two-mods-roundtrip-assessment.json`은 **24 PASS / 0 FAIL**이다. `saves/clean-two-mods-reloaded-resaved-Nov30-14.hoi4`의 SHA-256은 `FAC6ABC2A572BE1F7D68D05E90E58F24F74E896556824884050240E274CD3E41`이다.

서울대·첫·둘째 완료ID와 순서, 감산5, 핵 연구·민간 기술 수준과 획득일, 강원 대기열1개 원문 및 미완성 수준0, 혁신 잔액·49개 프로젝트·과학자4명·시설 program0을 보존했다. 당시 구현 저장의 열거한 상태 왕복이며 임의의 이전 버전 저장·전체 세계 동일성·완성된 원자로 기능까지 검증하지 않는다. 초기 시험의 비축0·핵 연구 준비를 자연 획득으로 바꾸는 증거도 아니다.

## 기술 기보유 자동 통과 — 별도 합성 입력 두 사례

진단 없는 두 모드 실행에서 다음 합성 입력을 각각 실제 UI로 로드·시간 진행했다. 두 입력은 모두 서울대와 첫 완료·핵 연구·민간 기술을 보유하며, 기술 획득을 정상 연구/프로젝트 완료로 표현하지 않는다. 주 작업자는 각 중점 통과 팝업과 기술 보유 사유를 관측했다.

| 입력 | 실제 저장·판정 | 결과 |
|---|---|---|
| 둘째 활성 + 민간 기술1 | `saves/clean-midactive-bypassed-May2-17.hoi4`, `clean-midactive-bypass-assessment.json` **19/0** | 둘째 완료ID1회·활성 해제, 기술 수준/획득일 보존 |
| 둘째 미선택 + 민간 기술1 | `saves/clean-preowned-bypassed-May11-16.hoi4`, `clean-preowned-bypass-assessment.json` **19/0** | 둘째 완료ID1회·활성 없음, 기술 수준/획득일 보존 |

판정 파일은 외부 `validation/` 아래다. 실제 후속 저장의 SHA-256은 순서대로 `D77846CB96663D4CBDF8EAA8BCFD4D5C6812E5D37B6A017907225647A8D3AFCA`, `D794B51404F2A0791FA72D3420DC28B84D1C1691EF8AE7F3D483E57271E81B20`이다. 혁신 잔액·프로젝트·원래 과학자·시설 program을 열거해 보존을 확인했다. 원시 focus 본문에는 별도 bypass boolean·완료 시각이 없어 UI 관측과 함께 판정한다. 값의 보존만으로 멱등적인 기술 지급의 보이지 않는 실행 횟수까지 단정하지 않는다.

이는 **기술을 이미 보유한 저장의 엔진 재평가**이며 연속 실행 중 기술 지급의 같은 틱 작동을 뜻하지 않는다. 별도 실제 실행에서 Nov29.09 기술 지급 후17시까지 중점 활성 상태가 남은 관측도 보존한다. 정확한 재평가 틱·선행 미완료·DLC 미보유와의 우선순위는 이 두 사례로 확정하지 않는다.

## 시험 저장 로드 후 최종 로그의 추가 오류

`clean-two-mods-final-before-dlcoff/`의 종료 전 로그는 메인 메뉴 기준선 이후 **45→74행, 정규화 추가29행·제거0행**이다. text.log는 추가0·제거0이었다. 비교 원문과 추가22개 메시지 블록은 `validation/clean-two-mods-final-before-dlcoff-log-assessment.json`에 보존했다. 따라서 최종 프로세스 전체를 새 오류0으로 표현하지 않는다.

가장 이른 추가 오류는16:42:15에 불러온 시험 저장의 `HOK_CNUC_duration.2/3/4` 참조가 제거된 진단 정의를 찾지 못한 기록이다. 이어 진단 decision 참조·이름 없는 decision 파싱/중복, `Failed to rename` errno2, 합성 기보유 입력의 `Unexpected token: hours`가 있다. 이름 없는 파싱·파일 이름 변경·hours 오류의 정확한 원인을 주변 메시지만으로 단정하지 않는다. 명명된 두 신규 생산 중점 오류는 없으나 이는 전체 저장 파싱 무오류의 증거가 아니다. 위24/0·각19/0은 실제 UI와 열거한 상태의 보존·통과를 확인한 좁은 판정이며 이 추가 오류를 없애지 않는다.

후속 원문 추적은 `hours` 필드가 **기술 삽입이나 진단 제거 전에 이미 있었음**을 확인했다. 수정하지 않은 첫 완료 저장 `CC659E…B72B78`의3951402행과 비축0 사본에 MON의 state819 국경 전투 `removed_unit = { unit = { id=2563 type=51 } hours=2147483643 }`가 있고, `SEA_border_incidents_events.6/.5/.7` 콜백 문맥이다. 합성 기보유 입력의3951411행은 기술 기록 두 개의9행 삽입만큼 위치가 이동한 같은 필드다. 진단이 활성화됐던 기존 비축0 로드의 `integer35-minus5-normal240-completed/logs/error.log:49`에도 해당 오류가 있다. 따라서 기술 삽입이 새 필드를 만들었거나 제거한 진단 이벤트 때문에 생긴 오류로 분류하지 않는다. 선행 외국 국경 전투 상태를 상속한 것은 확인됐지만 최초 작성 경위와 loader가 거부하는 내부 원인은 **UNPROVEN**이다. 이는 위 duration 이벤트 미등록 오류와 별개다.

## GDR 제외 새 한국 게임·조건 표시

별도 전체 재시작 `-debug -exclude_dlc=Gotterdammerung -start_tag=KOR`에서 진단 없는 새1936.1.1.12 한국을 로드했다. 최종 `1b1c` 초기 HIDE 화면의 두 새 아이콘·이름표·인접 연결선이 정상적으로 보였다. 둘째 tooltip은 잠긴 기본245일과 핵 연구 미완료·GDR 조건의 빨간X를 표시했다. 화면은 `runtime-ui/clean-fresh-KOR-initial-HIDE-branch.jpg`와 `clean-fresh-KOR-GDR-excluded-tooltip.jpg`다.

시작 system.log는 여전히 **DLC36개와 GDR을 열거**하지만 실제 `has_dlc` UI 조건은 거짓이었다. DLC35개 실행이나 GDR 소유권 미보유 환경으로 바꾸어 설명하지 않는다. 이때 첫 선행·핵 연구도 미완료여서 GDR 하나만의 시작 차단 증거는 아니다. 핵 연구1 준비 저장을 로드하려 했으나 누락 GDR·제거된 진단 모드로 로드 자체가 차단됐다. `clean-GDR-excluded-prepared-save-blocked.jpg`에 남겼으며 조건 단독 검증을 통과로 세지 않는다. GDR 제외 상태의 첫 보상 실행도 관측하지 않았다.

불러온 시험 저장이 없는 이 새 게임의 로그는 외부 `clean-fresh-KOR-exclude-GDR/`와 `validation/clean-fresh-KOR-exclude-GDR-log-assessment.json`에 별도로 보존했다. 현재 버전 기준선 대비 **45→51행, 정규화 추가6·제거0**, text.log 추가0·제거0이다. 추가 행은 GER land cruiser 애니메이션4개·KOR mesh1개·JAP 장비 GFX1개다. 새 핵 모듈·진단 참조·불러온 저장 파싱 오류는 없지만 전체 새 오류0은 아니며, 이6행의 근본 원인은 이번 중점 작업에서 조사하지 않았다.

## 실행 종료·원래 프로필 복구

주 작업자가 게임 종료를 확인하고 원래 프로필을 복구했다. `validation/final-profile-restore-assessment.json`에서 `settings.txt` SHA-256 `DE97534FED2150477EE0B9144888B0794FC70379FE0A780C1E1C523F5B4F3088`, `dlc_load.json` `BD386BA1B9D96B673BDC9ABF276816C00F58AF6A4E844A95DB7332F0C8D4B183`가 작업 전 사본과 정확히 일치했다. 기존 저장3개도 각각 원래 해시를 유지했다.

원래 플레이세트 순서는 `mod/hearts of korea.mod` → `mod/Hearts of Korea English Translation Anime Modder's Edition.mod`, 비활성 DLC 목록은 비어 있다. 검증용 Korean Language → 저장소 구성과 원래 구성을 혼동하지 않는다. 임시 `HOK_CNUC_runtime_test.mod`는 SHA-256 `1522A2B2241C123EE76860400A7B6EAA935DFC5D332A6C15C14A3B8EE7E65206` 확인·외부 사본 보존 후 제거했다. 시험 저장·외부 로그·화면 증거는 유지했고 커밋·푸시·게시를 수행하지 않았다.

## 남은 검증과 기록 규칙

1. 연속 실행 중 다른 경로로 기술 취득 시 정확한 bypass·취소 평가 시점, 선행 미완료·DLC 조건과의 우선순위. 기보유 합성 입력 두 사례는 위에서 확인했다.
2. GDR 제외 새 게임의 빨간 조건 표시는 확인했지만 DLC 하나만의 시작 차단은 준비 저장 로드 제한으로 미검증이다. 실제 라이선스 미보유 환경과 GDR 제외 상태의 첫 효과 실행도 별도다.
3. 현재 완료/queue 저장의 실제 재로드24/0·새 한국 초기 HIDE·프로필 복구는 확인했다. 시험 저장 파싱 오류와 임의 이전 저장 일반 호환·장기 지속성은 이 결과와 분리한다.
4. 기존 무궁화75%·연구 혜택·뉴스·일회 과학자 성장, 새 가지와 양쪽 진행 순서 및175% 총 지급량의 경계.
5. SHOW/HIDE·정치 경로·잠김/진행/완료 광택·클릭 영역, 첫 정확35×24시간과 이전 저장 일반 호환·AI 장기 진행·멀티플레이.

감산 제거 전 소스506/0·자산28/0·과거 첫 보상9/0·연구 기준선37/0·단계 판정은 각기 다른 증거다. 이를 합쳐 전체 런타임 통과 수로 표시하거나 감산 없는245일 실행의 검증으로 재사용하지 않는다. 실제 UI·정상 진행, 합성 준비, 강제 효과, 저장 재로드와 장기 호환의 증거를 구분하며 구현 완료를 위 남은 사례의 검증 완료로 확대하지 않는다.
