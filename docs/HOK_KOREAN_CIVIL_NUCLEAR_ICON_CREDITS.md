# 민간 핵 연구 중점 아이콘 출처와 제작 기록

작성: 2026-10-31. 범위는 신규 민간 핵 중점 두 개의 전용 그림과 해당 그림의 일반·완료 광택 sprite다. 기존 그림·중점 효과·현지화·배치·AI는 이 자산 작업에서 수정하지 않았다. 새 그림은 아래처럼 AI 생성물로 기록하며 바닐라 원화나 공개 팩의 원화로 표시하지 않는다.

현재 설치본은 **Operation Postern v1.19.4.1.99a5 / Steam build 26282552**다. `system.log:139`의 버전과 `appmanifest_394360.acf`의 buildid를 읽었다. 앞선 기능 연동의 1.19.3/build25205862를 이번 자산의 원본 버전으로 재사용하지 않았다.

## 새 그림과 계속개발 기여

두 중심 그림·배경·금속 테두리는 내장 **image_gen.imagegen**으로 새로 생성했다. 실제 모델 이름은 도구 결과에 공개되지 않았으므로 특정 모델명을 추정하지 않는다. 외부 참조 이미지를 생성 입력으로 제공하지 않았고 CLI·API 키 경로를 사용하지 않았다. 초기에는 현재 설치본의 핵·연구·산업 후보 24개를 실제 크기로 살펴봤지만, 합의한 소재·분야색 조합을 충족하지 않아 최종 그림에 채택하지 않았다.

계속개발 기여자 `kpopmodder`의 작업은 프롬프트 작성·선정, 알파 여백 정리·기계적 축소·형식 변환, 내부 GFX 연결과 검수다. 새로 사람이 그린 원화나 Paradox Interactive·Ultimate HOI4 GFX의 원화로 표시하지 않는다. 프롬프트 전문·도구·선정 원본 경로는 [생성 기록](assets/civil-nuclear-research/generation-prompts.json)에 있으며 [매니페스트](data/HOK_KOREAN_CIVIL_NUCLEAR_ICON_MANIFEST.json)에 파일 해시와 변환 값이 있다.

| 중점 | 중심 소재·분야색 | 프로젝트 sprite | 런타임 DDS |
|---|---|---|---|
| `HOK_KOR_fission_chain_reaction_experiments` | 원자 궤도와 실험 장치, 밝은 회색·은색 연구 배지 | `GFX_HOK_KOR_focus_fission_chain_reaction_experiments` | `gfx/interface/goals/HOK_KOR/civil_nuclear_research/fission_chain_reaction_experiments.dds` |
| `HOK_KOR_civilian_nuclear_investment` | 냉각탑·돔형 원자로·발전시설, 중립 회색·동색 산업 배지 | `GFX_HOK_KOR_focus_civilian_nuclear_investment` | `gfx/interface/goals/HOK_KOR/civil_nuclear_research/civilian_nuclear_investment.dds` |

두 파일 모두 **100×88, 알파 포함 비압축 BGRA32 DDS, mip 1개**다. 별개의 정책 두 개이므로 I/II 단계 표식·문자·국기·무기 이미지를 넣지 않았다. 생성 PNG의 알파가 0보다 큰 모든 픽셀을 포함하는 경계를 구하고, 투명 외곽만 정리한 뒤 96×84 이내에 비율을 유지하여 맞췄다. System.Drawing의 HighQualityBicubic·SourceCopy를 사용했으며 색조 변경·덧그림은 하지 않았다. 두 원본 PNG는 각각 1337×1176으로 [generated 폴더](assets/civil-nuclear-research/generated)에 그대로 보존했다.

| 출력 | 최종 SHA-256 | 선정 원본 PNG SHA-256 |
|---|---|---|
| 핵분열 연쇄반응 실험 | `bcf3761f057a465b613d366000b9b9679e31fd53326a26839fe3672d9535ae45` | `2d0412933f4ae0a048d878bf597570ee89a9888269f0a7711ef86a83e6a3f7a7` |
| 민간 원자로 투자 | `74431437fa43fee63da63e580b93aecdc8d0c2c7e4bc2c0dbf1f1a6892beb4f0` | `3eb4141798b9f08e9ad7963afe63f55c9872a0dc8845a60a0ad80bf165cf0824` |

## 원본 완료 광택 효과

원본 그림 재사용은 광택 오버레이 하나로 한정한다. 출처는 설치본 `gfx/interface/goals/shine_overlay.dds`, 원 저작은 **Paradox Interactive / Hearts of Iron IV**다. 같은 게임용 모드 안에서 선택한 바닐라 효과 자산을 재사용한 것이며 공개 팩·오픈소스 허가나 저작권 이전을 주장하지 않는다. 원본 설치 파일은 읽기 전용으로 유지했다.

이 파일을 `docs/assets/civil-nuclear-research/sources/shine_overlay.dds`와 `gfx/interface/goals/HOK_KOR/civil_nuclear_research/shine_overlay.dds`에 바이트 그대로 복사했다. 세 파일의 SHA-256은 모두 `bb416649358c73d34aacd46bad61bc44211fac8111627b56e25f385ad98f4448`이며 형식·크기·알파·프레임을 바꾸지 않았다. 세부 헤더는 매니페스트에 기록했다.

`interface/HOK_KOR_civil_nuclear_research.gfx`는 일반 sprite 2개와 같은 이름에 `_shine`을 붙인 sprite 2개만 등록한다. 완료 효과는 설치본 `interface/goals_shine.gfx:4–34`의 두 방향 scrolling 구조를 따른다. 각 새 DDS 자체가 내부 알파 마스크이고 오버레이도 위 내부 사본을 사용한다. 표준 `gfx/FX/buttonstate.lua` 효과 참조를 유지하며 바닐라·의존 모드의 전역 sprite는 덮어쓰지 않는다.

## 확인 범위

[실제 크기 미리보기](assets/civil-nuclear-research/actual-size-preview.png)에서 100×88 원자·실험 장치와 냉각탑·원자로가 구별되고 은색·동색 테두리 및 투명 여백이 유지됨을 직접 확인했다. 원본 PNG의 작업 공간 사본과 생성 도구 원본의 바이트 일치, DDS 헤더·알파·투명 테두리, 내부 경로의 정확한 대소문자, 일반·광택 이름 유일성과 원본 sprite 비덮어쓰기를 확인했다. 외부 `C:/hoi/test/feature-integration-20261031/civil-nuclear-assets/source-asset-checks.json`은 **28 PASS / 0 FAIL**이다.

이 자산 검수는 전체 재시작 후 실제 그림·광택 표시, 잠김·선택 가능·진행·완료 상태, 중점 명판·연결선·클릭 영역을 입증하지 않는다. 런타임은 주 작업자가 별도로 검증하고 실제 결과를 신규 중점 명세에 기록한다.
