# HOK 로그 검토 스킬 위치와 이동 기록

기록일: 2026-11-06. 사용자의 프로젝트 내부 배치 요청에 따라 문서만 이동·수정했다.

## 현재 기준 위치

스킬의 기준 원본은 [프로젝트 SKILL.md](../.agents/skills/hok-log-review/SKILL.md)다. HOK 실행 로그를 검토하거나 오류 원인을 판정하기 전에 [AGENTS.md](../AGENTS.md)에 명시된 조건에 따라 읽는다.

프로젝트 스킬은 `.agents/skills/`에 두라는 [OpenAI 공식 문서](https://learn.chatgpt.com/docs/build-skills)의 위치 안내를 따랐다. 이 기록의 확인 범위는 실제 파일과 문서 연결이며, 실행 중인 Codex의 스킬 목록 갱신·자동 선택을 시험한 결과는 아니다.

## 이전 위치와 현재 위치

| 구분 | 절대 경로 | 역할과 처리 |
|---|---|---|
| 초기 작성 위치 | `C:/Users/jaewo/.codex/skills/hok-log-review/SKILL.md` | 같은 날 먼저 작성한 개인 범위의 원본. 아래 프로젝트 경로로 이동했으며 이 위치의 파일은 남기지 않았다 |
| 현재 위치 | `C:/hoi/hearts_of_korea/.agents/skills/hok-log-review/SKILL.md` | 이후 유지할 프로젝트 기준 원본. 스킬 이름 `hok-log-review`와 파일명 `SKILL.md`를 유지했다 |

기존 파일을 이동한 뒤 저장소 루트 안내와 프로젝트 문서 링크를 상대 경로로 수정했다. 로그 출처·원인 구분, 읽기 전용 기본 범위, 과거 사례의 한계에 관한 본문은 유지했다. `AGENTS.md`의 필독 링크도 현재 프로젝트 위치를 가리킨다. 이전 개인 위치는 위 이력으로만 남긴다.

## 프로젝트 이동 직후의 문서 확인과 증거 자료

- 현재 파일이 존재하고 이전 위치의 파일은 없음을 확인했다.
- `AGENTS.md`에서 스킬과 이 기록으로 연결되는 상대 경로, 스킬에서 저장소 루트와 기존 구현 기록으로 연결되는 상대 경로를 확인했다.
- 이동 직후에는 기존 `.gitignore`의 `/.agents/` 규칙 때문에 스킬이 `git status`의 신규 파일 목록에서 제외됐다. 당시 `git check-ignore -v`로 해당 규칙을 확인했으며, 문서 전용 요청에 따라 ignore 규칙이나 Git 인덱스는 변경하지 않았다. 이후의 제외 해제는 아래 후속 변경과 구분한다.
- 별도 manifest·검증 보고서·백업·진단 파일은 생성하지 않았다. 기존 런타임 검증 자료의 위치와 원본/사본 역할은 [2026-11-06 구현·검증 기록](incidents/2026-11-06-hok-runtime-compatibility-implementation.md)에 유지된다. 이번 문서 이동으로 그 증거 자료를 옮기거나 과거 검증 결과를 갱신하지 않았다.
- 이번 작업에서는 게임·스킬 검증 스크립트·시험을 실행하지 않았다. 게임 코드·설정 변경과 커밋·푸시·배포도 수행하지 않았다.

## 후속 변경: 스킬 문서의 Git 제외 해제

2026-11-06 같은 날 사용자가 스킬 문서를 GitHub에 올릴 수 있도록 `.gitignore` 제외 해제를 요청했다. 이에 `.agents/skills/`와 하위 디렉터리를 탐색할 수 있게 하고, 그 아래의 `SKILL.md`·`skill.md` 파일들을 ignore 예외로 지정했다. 다른 agent 파일과 기존 로컬 설정·비밀파일·로그·임시파일의 제외 규칙은 유지했다.

실제 스킬에 대해 `git check-ignore`의 제외 여부를 확인하고, `git status --short --untracked-files=all`에서 `.agents/skills/hok-log-review/SKILL.md`가 신규 파일로 표시되는 것을 확인했다. 아직 스테이징·커밋·푸시는 하지 않았으며 GitHub 업로드 완료를 의미하지 않는다. 이번 후속 변경은 `.gitignore`와 이 기록에 한정했다.
