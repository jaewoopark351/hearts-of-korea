# 긴급 특별 건함계획 이미지 제작·출처

작성: 2026-10-20. 범위는 비전 1950의 신규 반복 디시전과 기간제 국민정신 이미지 2개다. 기존 원작 이미지, 비전 1950 중점 이미지, 다른 정책 그림은 변경하지 않았다.

## 제작과 출처

두 그림 모두 **내장 `image_gen.imagegen`으로 새로 생성한 AI 래스터 이미지**다. 서로 다른 구도를 위해 각각 별도의 호출로 생성했으며, 참조 이미지·외부 작가 그림·공개 소재 팩·바닐라 픽셀을 사용하지 않았다. 실제 모델 식별자는 도구 응답에 노출되지 않아 기록하지 않는다. 오픈소스 다운로드나 원작자의 신작으로 표시하지 않는다.

계속개발 기여는 kpopmodder의 정책별 프롬프트 지정, 결과 선정, UI 크기 변환·DDS 내보내기, 프로젝트 소유 스프라이트 연결과 정적 검수다. 원작 Hearts of Korea의 다른 그림과 그 출처·기여자 기록은 그대로 보존한다. 생성물에 임의의 MIT·CC 라이선스나 외부 작가 이름을 붙이지 않는다.

최종 채택 원본 PNG는 [프로젝트 내부 원본 폴더](assets/korean-emergency-shipbuilding)에 보관한다. 두 호출의 전체 프롬프트, 생성 도구·날짜·참조 이미지 없음·모델 비공개 상태는 [생성 기록](assets/korean-emergency-shipbuilding/generation-record.json)에 있다. 내용 ID, 원본·결과 해시, 가공 수치와 스프라이트는 [전용 매니페스트](data/HOK_KOREAN_EMERGENCY_SHIPBUILDING_ICON_MANIFEST.json)에 기록한다.

| 대상 | 콘텐츠 ID | 구도·규격 | 게임용 파일 |
|---|---|---|---|
| 디시전 「긴급 특별 건함계획 시행」 | `HOK_KOR_enact_emergency_special_shipbuilding` | 군함 옆모습과 망치, 단순 금속 원판, **32×32** | [전용 DDS](../gfx/interface/decisions/HOK_KOR/emergency_shipbuilding/emergency_special_shipbuilding.dds) |
| 국민정신 「긴급 특별 건함계획」 | `HOK_KOR_emergency_special_shipbuilding` | 조선소 크레인·갈고리 아래 건조 중인 선체, **60×68** | [전용 DDS](../gfx/interface/ideas/HOK_KOR/emergency_special_shipbuilding.dds) |

공통 해군 정책으로 해군색 기준 `#283b52`(RGB 40,59,82)의 남색·슬레이트 계열과 은색 금속 소재를 생성 프롬프트에 지정했다. 배경의 실제 픽셀은 생성된 명암을 유지하며, 모든 픽셀이 기준색과 같다고 주장하지 않는다. 망치 손잡이와 크레인 기계의 소량 갈색·청동색은 보조 소재다. 정부 이념에 따라 바꾸지 않으며 I·II·III 단계 표시는 없다.

## 변환과 연결

생성 원본은 수정하지 않고 그대로 보존했다. 알파가 8을 초과하는 픽셀의 경계를 찾아 투명 바깥 여백을 정리하고, 가로세로 비율을 유지해 목표 캔버스 안에 배치했다. 디시전은 최소 1픽셀, 국민정신은 최소 2픽셀의 투명 여백을 확보했다. 리샘플링은 System.Drawing의 HighQualityBicubic·SourceCopy를 사용했고, 원본 도형의 알파를 유지했다. 전체 색조 필터, 바탕색 일괄 변경, 외부 프레임 합성은 하지 않았다.

게임용 결과는 단일 레벨·알파 포함 **비압축 BGRA32 DDS**다. DDS를 다시 읽어 내보내기 직전 RGBA 버퍼와 모든 픽셀이 같은지 확인했다. 테스트용 내보내기 스크립트·PNG 미리보기·변환 기록은 저장소 외부 `C:/hoi/test/vision1950-20261020-01/art/`에 둔다.

[전용 GFX](../interface/HOK_KOR_emergency_shipbuilding_icons.gfx)는 모드 루트 기준 상대경로로 다음 이름을 연결한다.

- 디시전: `GFX_HOK_KOR_decision_emergency_special_shipbuilding`. 디시전의 `icon`에는 전체 이름을 사용한다.
- 국민정신: `GFX_idea_HOK_KOR_emergency_special_shipbuilding`. 국민정신의 `picture`는 `HOK_KOR_emergency_special_shipbuilding`이다.

원본 SHA-256:

- 디시전 PNG: `7a8c56023ee44ab988f59e62d23063bea2a3507a58fff2efa09f7d6bb69f6e14`
- 국민정신 PNG: `b81195035ff28bec9daeee3f7c573465412ec13cbfac4a5f7ba4c56b51038b7e`

게임용 SHA-256:

- 디시전 DDS: `383cfe8e1552eca4eb6621535e3b3da89984a414f3e00ad2f63c5f2fed1fe350`
- 국민정신 DDS: `f7a33fd43eeeadceeff2ed8f32d6b6b1dae97b8482fd1c9e7a0d97da724a1b9b`

## 검수 범위

**정적 검수 PASS:** DDS 크기·헤더·채널·단일 레벨·파일 길이·알파·해시, 게임용 파일의 픽셀 재읽기 일치, 내부 상대경로와 GFX 연결을 확인했다. 실제 크기 및 6배 최근접 확대에서 선체·망치와 크레인·갈고리·선체가 구분되고 금속 테두리가 어두운 UI 바탕과 분리된다. 소형 디시전 전용 그림을 사용해 큰 국민정신 이미지를 행에 직접 연결하지 않는다.

설치 바닐라 `interface/countrydecisionview.gui`의 일반 결정 아이콘 중심 (30,19), 제목 시작 x63을 확인했다. 32×32 캔버스는 행 내 x14~46/y3~35에 놓이며 제목까지 17픽셀이 남는다. 이는 정적 좌표 계산이며 실제 게임 화면 관측과 구분한다.

**실제 UI 관측:** 본 구현의 진단 보조 실행에서 최종 DDS가 표시되는 것을 확인했다. 비전 1950을 완료한 상태에서 디시전의 이름·전용 군함/망치 그림이 같은 행 안에 정상 표시됐고, 정치력 149 상태 및 시행 후 사용 불가 상태에서도 그림이 유지됐다. 정치 화면에는 크레인·선체 국민정신 그림이 나타났으며, 마우스 툴팁이 「긴급 특별 건함계획」 이름·함종별 생산 비용 효과·제거 예정일을 표시했다. 관측 환경은 설정 해상도 1280×720, GUI 배율 1.0, DPI가 반영된 원본 캡처 2564×1504, Man the Guns 활성·DLC 36개·모드 2개다.

증거는 저장소 외부 `C:/hoi/test/vision1950-20261020-01/runtime-ui/`의 `05-unlocked-blocked-at-149.png`, `06-first-use-pp350.png`, `07-spirit-effects-expiry-june30.png`다. 개별 원본 해시는 전용 매니페스트에 기록한다. 이는 표시한 디시전 행·정치 화면·툴팁의 관측이며 전체 중점의 정상 진행, 모든 배율·DLC 조합·UI 상태의 통과를 뜻하지 않는다. 실제 180일 만료와 반복 사용 등 정책 동작은 본 구현의 별도 검증 기록을 따른다. 정적 미리보기와 실제 게임 캡처를 구분한다. 커밋·푸시·게시를 수행하지 않았다.
