# 2026-11-01 유일한의 재정 전문가 특성 교체

상태: **소스 수정·정적 대조 완료 / 새 게임·고용 UI·기존 저장 반영 미검증**.

사용자가 원본 HOI4의 소비재 공장 감소 특성으로 유일한을 금융 전문가로 바꿀 수 있는지 물은 뒤 수정을 요청했다. 기존 경제학자 효과에 추가하지 않고 원본 `financial_expert`로 교체하는 범위다. 호환성 오류 수정이 아니라 요청된 고문 효과 변경이다.

## 기준과 변경

- 작업 저장소: `C:/hoi/hearts_of_korea`, 브랜치 `feat/korean-focus-expansion-ai`, HEAD `f79cebfbb92518f478d8258bd406b52d3a1ae6d6`. 시작 시 작업 트리는 깨끗했다.
- [유일한 정의](../../common/characters/KOR.txt:638)의 특성 하나를 `KOR_economist`에서 `financial_expert`로 교체하고 해당 줄 바로 위에 기여 주석을 추가했다.
- 이전 효과: [모드 경제학자 특성](../../common/country_leader/00_hok_traits.txt:158)의 `production_factory_max_efficiency_factor = 0.05`, **생산 효율 상한 +5%**.
- 변경 효과: 설치본 `common/country_leader/00_traits.txt:8522`의 `financial_expert`, `consumer_goods_factor = -0.15`, **소비재 공장 변동치 −15%**. 소비재 비율을 직접 15%p 차감한다고 설명하지 않는다.
- 원본 특성을 참조하며 전역 특성 정의를 복사하거나 수정하지 않는다. 기존 `KOR_economist` 정의도 보존했다. 두 특성의 `ai_will_do.factor`는 모두 2다.
- `KOR_Ilhan_Yu`, `idea_token = ilhan_yu`, 이름·초상·정치 고문 슬롯·한국 제한·별도 비용을 지정하지 않는 기존 방식은 그대로다. 팔도 개발 위원회 완료 해금 조건과 중점의 고문 안내, 시작 캐릭터 모집도 변경하지 않았다.

## 근거와 정적 확인

설치본 `common/characters/ARG.txt:1889–1899`는 같은 `political_advisor` 역할에서 `financial_expert`를 사용하는 사례다. 저장소와 Korean Language 의존성에서 해당 원본 특성을 덮어쓰는 별도 정의는 찾지 못했다. 원본 및 Korean Language의 표시 명칭은 **재정 전문가**다.

설치본 실행 파일 SHA-256은 `CF781ED178CD801643B233B7E3FCD1C0EFD19BD01AECD24BF07A35F69F10476F`로 앞선 [1.19.4.1.99a5 검증 기록](2026-10-31-korean-democratic-focus-compaction.md)의 설치본과 같다. 이번 변경으로 게임을 새로 실행하거나 새 체크섬을 관측하지는 않았다. 저장소 descriptor의 `1.19.*`·Korean Language 의존 선언·후속 Workshop ID는 유지했다.

변경 전후 원문을 대조하여 유일한의 특성 참조와 기여 주석 외의 바이트가 보존됐는지 확인했다. 다른 캐릭터·해금 조건·전역 특성·중점·현지화는 수정하지 않았다. UTF-8 상태와 기존 줄바꿈을 보존했고 `git diff --check`를 통과했다. 이는 소스·참조 검토이며 엔진 고용 효과 검증은 아니다.

- `common/characters/KOR.txt` 변경 전 SHA-256: `b42fc7ba449df32fa05aa8d4f6aab7a05d29a9e2c0a3d5c2bbedeae7f4dd7ef7`.
- 변경 후 SHA-256: `ec8eeec8ba2a3055be8f01466353a0575330c87660ce90e0663a461838d8c2d8`.
- 변경 전 소스와 변경 기록은 저장소 밖 `C:/hoi/test/ilhan-financial-expert-20261101/`에 보존했다.

## 실행 범위와 남은 확인

점검 시 HOI4 프로세스는 없었고, 실제 활성 모드 목록은 별도 `C:/hoi/hearts_of_korea_Road_to_56` 사본과 Road to 56을 가리켰다. 이번 요청은 현재 작업 저장소의 수정이며 그 별도 사본으로 전파하지 않았다. 실제 프로필·모드 선택·설정·저장·설치본·Workshop은 변경하지 않았다.

새 게임에서의 특성 표시·해금 전 고용 차단·정상 고용 후 소비재 효과, 이미 고용한 이전 저장의 반영과 다른 모드·DLC·멀티플레이는 미검증이다. 기존 민주주의 배치 검증을 이 특성 변경의 실행 검증으로 재사용하지 않는다. 커밋·푸시는 수행하지 않았다.
