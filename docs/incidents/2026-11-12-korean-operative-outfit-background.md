# 2026-11-12 한국 첩보원 초상화 배경·복장 수정

같은 날 [처음 구현한 한국 신규 첩보원 초상화](2026-11-12-korean-operative-portraits.md) 8장을 사용자의 후속 요청에 따라 편집했다. 남녀 각각 4명의 기존 얼굴을 입력으로 사용하고, 드라마 《도깨비》의 저승사자 복장을 검은 중절모·정장·코트, 흰 셔츠와 검은 넥타이로 해석했다. 각 인물의 나이·표정·안경·콧수염을 유지하는 방향으로 AI 이미지 편집을 수행했다.

## 작업 기준과 경로

- 작업 소스는 `C:/hoi/hearts_of_korea/`, 브랜치는 `feat/korean-focus-expansion-ai`, 시작 HEAD는 `f1282d701bc47e47c119ca31faa6082e9e6ed1e6`이다. 기존 미커밋 초상화 구현과 문서를 보존했다.
- 이번 외부 작업·증거 기준 경로는 `C:/hoi/test/hok-operative-outfit-background-20261112-01/`이다. 아래 외부 상대 경로는 이 디렉터리를 기준으로 한다.
- 최초 제작 원본은 `C:/hoi/test/hok-operative-portraits-20261112-01/art/generated/portrait_HOK_KOR_operative_{female,male}_NN.png`다. 이번 편집의 입력 참조이며 이전 결과의 출처는 최초 구현 기록을 따른다.
- 편집 도구의 원본은 `C:/Users/jaewo/.codex/generated_images/01a1cf1e-a773-7480-b988-8c8652f01d70/`에 보존되어 있다. 선택한 새 PNG 사본은 이번 외부 경로의 `art/generated/`에 있다.
- 게임 자산 경로는 `gfx/leaders/operatives/HOK_KOR/portrait_HOK_KOR_operative_{female,male}_01`~`04.dds`다. 이전 DDS와 문서의 사본·해시는 `baseline.json`과 `source-before/`에 보존했다.

개별 도구 원본 → 보존 PNG → 변환 DDS → 저장소 DDS 대응과 SHA-256, 입력 참조와 정확한 프롬프트는 [자산 manifest](../data/HOK_KOREAN_OPERATIVE_PORTRAIT_ASSET_MANIFEST.json), `art/imagegen-records-batch1.json`, `art/imagegen-records-batch2.json`, `validation/staged-asset-revision-records.json`에 기록했다. 도구는 `image_gen.imagegen`이며 모델명은 도구에 노출되지 않았다.

## 배경 원인과 적용 방식

`CONFIRMED`. 후보 행에 쓰이는 바닐라 `gfx/interface/naval_leader_selection_entry_bg.dds`에는 흰 초상화 칸이 들어 있다. 해당 그림의 `x=57–118, y=6–90` 영역 5,270픽셀은 `(255,255,255,255)`다. 최초 HOK 초상화 배경은 실제 투명 픽셀이므로 이 흰 칸이 드러났다. 설치본의 아시아 첩보원 DDS 18장에는 완전 투명 픽셀이 없고, 어두운 따뜻한 회색 배경이 그림 자체에 포함되어 있다.

이번 8장은 중간~어두운 회색 그라데이션을 캔버스 전체에 포함했다. 최종 DDS는 모든 픽셀의 알파가 255다. 근거는 `inspection/background-cause-conclusion.json`, `inspection/dds-background-alpha-analysis.json`, `inspection/native-comparison.png`다.

선택한 1086×1448 PNG의 전체 캔버스를 bicubic 방식으로 156×210에 맞췄다. 모자 윗부분과 챙을 보존하도록 전체 그림을 사용했다. 형식은 기존과 같은 uncompressed BGRA32, 파일당 131,168바이트, mipmap 헤더 값 0이다. 변환 helper와 이전 helper의 대응은 `art/helper-provenance.json`, 변환별 기록은 `art/final-dds/conversion-manifest.json`을 따른다.

## 확인 기록

8개 원본 편집 결과와 `art/final-dds/native-contact-sheet.png`를 직접 검토했다. 여성 03·남성 04의 안경, 남성 02의 콧수염, 각자의 얼굴 특징과 연령 표현을 확인했다. 검은 모자·옷과 회색 배경이 구분되며 모자 전체가 작은 그림 안에 들어온다. 독립 검토는 `validation/independent-native-visual-review.json`에 기록했다.

## 이번 수정 그림의 실행 확인

설치본 `Operation Postern v1.19.4.2.2da5`, Korean Language → 로컬 본체, 활성 DLC 36개와 La Resistance 조건에서 게임 프로세스를 새로 시작했다. PID는 `26248`, 메뉴 체크섬은 `04d2`다. 실제 구성과 실행 정보는 `runtime/main-test-preparation.json`, `runtime/main-process.json`, `runtime/main-session-final/`에 있다. 이번 실행의 관측은 `runtime/ui-observation.json`을 따른다.

| 확인 경로 | 실제 관측과 화면 증거 |
|---|---|
| 기존 정상 채용 저장 재로드 | `KOR_1936_05_12_02_temp.hoi4`의 1936-05-12 02:00 상태를 불러왔다. Hyeja Hong 여성 04와 Sungjin Yun 남성 02가 새 검은 복장·모자·회색 배경으로 표시됐다. 명단 카드와 원형 지도 아이콘을 확인했다. `runtime/screenshots/main-reloaded-pair-gray-background-and-costume.png` |
| 모집 후보 화면 | 같은 프로세스에서 이전 진단 후보가 담긴 `KOR_1936_01_02_16_temp.hoi4`를 불러왔다. 일반 UI로 기관을 창설하고 모집 대기 후 1936-03-21 15:00에 후보 목록을 스크롤했다. 흰 칸 노출이 해소되고 회색 배경과 검은 복장·모자가 표시됐다. `runtime/screenshots/main-candidates-01.png`~`06-foreign-controls-and-normal.png` |
| 새 일반 모집 후보 | 기존 진단 이름과 함께 새로 나온 `Hyeja Gang` 후보가 여성 01 그림을 표시했다. `runtime/screenshots/main-candidates-06-foreign-controls-and-normal.png` |

후보 화면에서 남녀 8종 모두 현재 자산에 대응함을 대조했다. 남성 01은 작은 화면에서 눈 주변이 안경처럼 보여 정량 대조를 추가했다. 01M·03M·04M·12M의 얼굴 영역은 모두 현재 남성 01이 최소 오차였고 RGB RMSE는 11.80~12.14, 두 번째 후보는 42.69~42.78이었다. 시각적으로 구분된 다른 7종도 같은 축소·캡처 조건에서 실제 자산이 최소 오차였다. 비교 기록은 `inspection/ui-crops/candidate-pixel-comparison.json`이다. 저장소 DDS 8개를 독립 디코딩한 픽셀도 승인된 native PNG와 모두 같았다. `inspection/dds-native-pixel-check/pixel-comparison.json`

이전 진단 overlay는 이번에 활성화하지 않았다. 이 저장의 후보 표시는 현재 그림의 렌더링 확인이며, 최초 구현 때 강제 생성한 태그별 결과와 구분한다. 이번에는 별도 저장을 시도하지 않았다. 기존 저장 두 개는 작업 전후 SHA-256이 같고 저장 목록도 87개로 동일하다. 최초 구현의 일반 저장 이름 변경 실패는 당시 기록을 따른다.

이번 애니 조합의 실행 확인은 수행하지 않았다. 같은 DDS 경로를 공급하는 연결과 본체 그림을 공유하는 구조는 정적으로 보존 확인했다. 자연스러운 정치 경로·외국 현지 모집 결정·장기 진행·멀티플레이는 이번 그림 편집의 실행 확인 범위에서 미검증이다.

## 종료와 설정 복원

`runtime/main-session-final/assessment.json`에서 실제 활성 모드 두 개·DLC 36개·메뉴 체크섬 `04d2`를 확인했다. 초상화·GFX·texture·sprite·shader·DDS 관련 오류는 0개다. 전체 오류는 76행·고유 74개이며, 이전 본체 첫 세션 대비 추가 64종은 이전 진단 저장을 불러올 때 기록된 `Invalid fleet type` 32행과 `Invalid fleet reference type` 32행이다. 전자 32행은 `save games/KOR_1936_01_02_16_temp.hoi4:0`을 가리키며 게임 날짜는 1936-01-02 16:00이다. 함대 경고의 원인 귀속은 미확정이다. 마지막 오류 게임 날짜는 1936-03-21 15:00이며 로그 사본 20개·903,461바이트를 보존했다.

게임을 일반 UI로 종료하고 Steam의 플레이 버튼 복귀를 확인했다. `runtime/pre-restoration/restoration.json`에서 HOI4·dowser·Paradox Launcher 잔류 프로세스가 없고 설정 네 개 모두 이번 작업 기준선과 바이트·SHA-256이 일치함을 확인했다. `settings.txt`는 이번 작업 전후 `DE97534FED2150477EE0B9144888B0794FC70379FE0A780C1E1C523F5B4F3088`로 동일하다. `dlc_load.json`은 원래 RT56 조합의 `A035CE0F00E763F597E523D2F7298B1FE1DF4B643A3907BAB7F24506A27F79C9`로 복원했다. 이전 작업의 설정 기록과 이번 복원 결과를 구분한다.

후보 목록·GFX 연결·고정 인물·과학자 자산·descriptor 등 보존 대상 14개는 작업 전과 해시가 같다. 자산 8개와 출처 사본·DDS 규격·알파 검사는 `validation/final-integration.json`, `validation/final-static-review.json`에 기록했다.

최종 그림 대응 검토는 `validation/independent-runtime-portrait-mapping-review.json`, 전달 전 검사는 `validation/final-delivery-review.json`을 따른다. 화면 캡처 11개의 원본 JPEG는 `runtime/screenshots-original-jpeg/`에 바이트 보존하고, 문서가 가리키는 `runtime/screenshots/*.png`는 실제 PNG로 저장했다. 원본 디코딩 픽셀과 PNG 디코딩 픽셀의 해시가 11개 모두 같으며 이전·현재 파일명과 인코딩 해시 대응은 `runtime/screenshot-format-normalization.json`에 기록했다.

저장소에 앞서 존재하던 `docs/assets/korean-fascist-mobilization-validation-20260923/` 검증 PNG 4개는 정리 대기 상태다. 이번 이미지 원본·helper·시험 화면·로그는 위 외부 작업 경로에 보존했다.
