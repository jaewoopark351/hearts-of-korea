# 재벌·시민사회 체계 자산 출처와 재사용 기록

기록일: 2026-10-11. 추가 갱신: 2026-10-12 디시전 배지·파란 지원/견제 아이콘(아래 후속 절). 대상은 한국 신규 내정 중점 13개, 정국의 영향력 패널, 연결 국민정신·결정·사건의 이미지 참조다. 2026-10-11 최초 작업은 기존 DDS 재사용과 스프라이트·UI 연결이며, 새 그림 생성, 새 합성, 이미지 크기 변경, 색상 수정, 파일 형식 변환을 하지 않았다. 게임에서 적용한 scale·타일 배치와 이미지 파일 자체의 가공은 구분한다.

## 기여와 사용 근거

하츠 오브 코리아에서 이어받은 한국 인물 초상, 기업 로고, 기존 한국 중점 및 사건 그림은 기존 원작과 원기여자의 크레딧을 유지한다. 이번 조사에서 파일별 작가·최초 원본·별도 허가를 확인하지 못한 항목에는 새 작가 이름이나 라이선스를 붙이지 않는다. 한국 기업명은 로고에 표현된 대상을 가리키며, 해당 회사에서 이번 재사용을 승인했다는 뜻이 아니다.

계속개발 정책 아이콘의 원본 소재는 기존 [중점·국민정신 크레딧](HOK_KOREAN_FOCUS_ICON_CREDITS.md)과 [아이콘 매니페스트](data/HOK_KOREAN_FOCUS_ICON_MANIFEST.json)를 따른다. 원본 출처는 [Globvs / Ultimate HOI4 GFX](https://github.com/Globvs/Ultimate-HOI4-GFX), 고정 커밋 `3626dc83c8573d6603fa497138090b04b64a15ba`이다. [그 커밋의 CREDITS.txt](https://github.com/Globvs/Ultimate-HOI4-GFX/blob/3626dc83c8573d6603fa497138090b04b64a15ba/CREDITS.txt)와 [보존 원문](assets/korean-focus-icons/UPSTREAM_CREDITS.txt)의 기록된 사용 근거는 해당 공개 팩 소재에만 적용한다. 보존 원문 SHA-256은 `cf220dc66463d75163f7690ad77b02b662d0c05ca5d53dc62d33ed504512a7f5`이다.

이 소재의 원 기여 표시는 **Globvs / Ultimate HOI4 GFX contributors**다. 파일별 작가는 원문에 연결되어 있지 않아 미상이며, 저장소 소유자나 업로더를 각 그림의 작가로 추정하지 않는다. 기존 정책 아이콘의 소재 선정·합성·DDS 변환·배경 색상 가공은 이전 계속개발 기록의 kpopmodder 기여다. 2026-10-11의 kpopmodder 기여는 재사용 자산 선정, 새 스프라이트·패널 배치·스크립트 연결과 이 출처 기록이다. 이전 가공을 이번 신규 원화 제작으로 표시하지 않는다.

아래 바닐라 공용 UI·사건 그림과 기존 광택 오버레이는 **Paradox Interactive / Hearts of Iron IV 원작 게임 자산**으로 기록한다. 개별 작가는 확인하지 않았다. 이것은 출처와 원작 귀속의 기록이며 새 이용 허가·라이선스 부여가 아니다. 공개 PNG 팩의 CREDITS 사용 근거와 별개이며, 플레이어의 게임 이용·배포 조건 및 후속 모드의 배포 조건을 대신하거나 새로 확정하지 않는다. 이 작업에서 별도 허가를 받았다는 주장은 없다.

## 바닐라 DDS 바이트 복사 6개

읽기 전용 설치 원본: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV`. 설치 메타데이터 기록은 `1.19.3.0.c01a (5632)`이며 [연구 계획](HOK_KOREAN_CHAEBOL_CIVIL_SOCIETY_RESEARCH_PLAN.md)의 설치본 기록과 같다. 실행 플레이셋의 모드 체크섬이나 활성 DLC 검증 결과를 뜻하지 않는다. 표의 원본 경로는 이 설치 폴더 기준 상대 경로이고, 최종 경로는 프로젝트 루트 기준 상대 경로다. 모든 행의 원본·복사본 SHA-256 및 전체 바이트가 일치한다.

| 원본 상대 경로 | 프로젝트 최종 경로 | 실제 DDS 크기 | 원본 = 복사본 SHA-256 |
| --- | --- | --- | --- |
| `gfx/interface/tiles/tiled_window_thin_border2.dds` | `gfx/interface/HOK_KOR/civic/tiled_window_thin_border2.dds` | 190×190 | `4e91de69fd47b0ec93eb1bf9fe5b2d5b563b999829a151f2aafe62edd71d627e` |
| `gfx/interface/tiles/tiled_window_small.dds` | `gfx/interface/HOK_KOR/civic/tiled_window_small.dds` | 95×95 | `75a8ba04928042bcd820789c1053008ab9664659fe208854242bbcb7dbcc50a1` |
| `gfx/interface/pol_leader_frame.dds` | `gfx/interface/HOK_KOR/civic/pol_leader_frame.dds` | 172×258 | `bb4d9292da380ce7570499d77fe2dec3ea3ecb4049d7e4e90b5af77bc7640ef2` |
| `gfx/interface/button_94x31.dds` | `gfx/interface/HOK_KOR/civic/button_94x31.dds` | 94×31 | `dc84a070a068c35b1192b084635d97aaa4a828eef96f22a375552aa7005fceb9` |
| `gfx/event_pictures/report_event_fighters.dds` | `gfx/event_pictures/HOK_KOR/civic/report_event_fighters.dds` | 209×176 | `6b1e66cdfaa3728043198932eca66b4ec291c427ce259e17ee6c7b22e830925f` |
| `gfx/event_pictures/report_event_generic_parliament.dds` | `gfx/event_pictures/HOK_KOR/civic/report_event_generic_parliament.dds` | 210×176 | `3463efe78172032a555cfa534eca2f40f95beae4c46c13bad7c066017b49f233` |

새 프로젝트 스프라이트는 `interface/HOK_KOR_civic_influence.gfx`의 `GFX_HOK_KOR_civic_panel_background`, `GFX_HOK_KOR_civic_card_background`, `GFX_HOK_KOR_civic_leader_frame`, `GFX_HOK_KOR_civic_action_button`와 `interface/HOK_KOR_civic_events.gfx`의 `GFX_HOK_KOR_civic_event_fighters`, `GFX_HOK_KOR_civic_event_parliament`다. 타일의 선언 size 192×192·96×96은 바닐라 설정을 따른 논리 크기이며, 위 표의 실제 DDS 크기 190×190·95×95와 구분한다. 원본 게임 파일과 Workshop 다운로드는 변경하지 않았다.

## 현재 지도자 초상

기존 `interface/characters_HoK.gfx` 스프라이트 11개를 그대로 참조한다. 아래 DDS는 모두 기존 프로젝트 파일이며 실제 크기는 156×210이다. inlay 조건은 각 character의 `has_country_leader = { character = ... ruling_only = yes }`로 현직 여부를 확인한다. 이름은 실제 현직 지도자를 표시하는 `ROOT.GetLeader`를 사용한다.

| 현직 character | 기존 스프라이트 | 기존 프로젝트 DDS | 현재 SHA-256 |
| --- | --- | --- | --- |
| `KOR_syngman_rhee` | `GFX_Portrait_KOR_Syngman_Rhee` | `gfx/leaders/KOR/Portrait_KOR_Prince_Rhee.dds` | `3209325c12bb1e3b6e5a4226088c5d5fd085e5917a760c7a6a799a98d994c6b5` |
| `KOR_Gu_Kim` | `GFX_Portrait_KOR_Gu_Kim` | `gfx/leaders/KOR/Portrait_KOR_Gu_Kim.dds` | `8a19b37ecf6bef487e089e8a49e19563b40ace99af671b3df27ad4a210d8fe0f` |
| `KOR_Boseon_Yoon` | `GFX_Portrait_KOR_Boseon_Yoon` | `gfx/leaders/KOR/Portrait_KOR_Boseon_Yoon.dds` | `8300b5c9fa4bd2d039e369928981022ce2c8716da6aa029435293c466cd1323b` |
| `KOR_Gang_Lee` | `GFX_Portrait_KOR_Gang_Lee` | `gfx/leaders/KOR/Portrait_KOR_Gang_Lee.dds` | `d5b2974c6f442f27c175379d30b7d12829b0e336e3d696348a5e202c8b4f3c6e` |
| `KOR_provisional_peoples_committee` | `GFX_Portrait_KOR_provisional_peoples_committee` | `gfx/leaders/KOR/Portrait_KOR_provisional_peoples_committee.dds` | `f55b9d2a86afacb737006ecca2fbf040c85e22b124a6c6cda7335a6ce40b96bc` |
| `KOR_Woonhyung_Yeo` | `GFX_Portrait_KOR_Woonhyung_Yeo` | `gfx/leaders/KOR/Portrait_KOR_Woon_Hyung_Yeo.dds` | `2b4f7a6785e3a8d79ddf2236974007d0c460fe50c91e188447aaafd711a66a72` |
| `KOR_Heonyoung_Park` | `GFX_Portrait_KOR_Heonyoung_Park` | `gfx/leaders/KOR/Portrait_KOR_Heon_Young_Park.dds` | `2e16fd178afe63d0b3ad05088e7daa2470f27b76773d4241d520a1b590a41a7b` |
| `KOR_Beomseok_Lee` | `GFX_Portrait_KOR_Beomseok_Lee` | `gfx/leaders/KOR/Portrait_KOR_Beomseok_Lee.dds` | `2d0f9854265ab5121db7a84011c05a256c5203c87b4e9bda4e01935b2b453b92` |
| `KOR_Yeonsu_Gye` | `GFX_Portrait_KOR_Yeonsu_Gye` | `gfx/leaders/KOR/Portrait_KOR_Yeonsu_Gye.dds` | `4a60dedf5ad1df5d892aad76b00c3779dac8298d8511268fa6abf2f3f673c243` |
| `KOR_Eun_Lee` | `GFX_Portrait_KOR_Eun_Lee` | `gfx/leaders/KOR/Portrait_KOR_Eun_Lee.dds` | `5d44d316e2ff4b4eca435dca5d0dbc8894c78b01ae752a828ea90f42fc33a3e8` |
| `KOR_Changho_Ahn` | `GFX_Portrait_KOR_Changho_Ahn` | `gfx/leaders/KOR/Portrait_KOR_Changho_Ahn.dds` | `7eb956c4c8b1b5b49c3b44d5cac3a6d1fa89a745190caa1db046775ef98b54a9` |

character ID 방식 밖의 기존 이름형 지도자 2명은 같은 기존 한국 초상 DDS에 새 프로젝트 스프라이트 별칭을 연결했다. 두 별칭은 지도자가 없는 경우의 고정 초상이 아니다. 나머지 미매핑 지도자는 기존 빈 DDS를 사용하고 실제 지도자 이름과 미매핑 안내를 표시한다. 아래 세 파일도 156×210이며 가공하지 않았다.

| 조건 | 새 스프라이트 별칭 | 기존 프로젝트 DDS | 현재 SHA-256 |
| --- | --- | --- | --- |
| 기존 이름형 지도자: Deoksugung Pyeonguihoe | `GFX_HOK_KOR_civic_leader_council` | `gfx/leaders/KOR/Portrait_KOR_Urihwangsilsaranghoe.dds` | `ed49517c5b0f2f356d55a3db27f284b6924ef158d407e1fc8fa70d6024fb23cb` |
| 기존 이름형 지도자: Gim Teuleo | `GFX_HOK_KOR_civic_leader_gim_teuleo` | `gfx/leaders/KOR/Portrait_KOR_Teul_Eo_Kim.dds` | `fef1d9eb886304865c72094219a8a4caefecf34ef0550a1d57328025ba3f411b` |
| 매핑되지 않은 실제 현직 지도자 | `GFX_HOK_KOR_civic_leader_unmapped` | `gfx/leaders/KOR/empty.dds` | `daa416037874073cd3d733a31ba364e2340b82ae5a4c50dde1811af970e5b218` |

## 재벌·시민사회 카드 그림

두 카드는 기존 정책 중점의 100×88 DDS와 기존 `interface/HOK_KOR_focus_icons.gfx` 스프라이트를 재사용한다. 카드 배치를 위해 DDS를 다시 그리거나 변환하지 않았다. 이전 정책별 배경 가공과 소재 합성의 상세 내역은 앞의 기존 매니페스트를 따른다. 표의 원본 소재 경로는 고정 Ultimate HOI4 GFX 커밋 기준이다.

| 카드 | 기존 스프라이트 | 프로젝트 DDS | 크기 | 현재 SHA-256 | 기록된 원본 소재 경로 |
| --- | --- | --- | --- | --- | --- |
| 재벌 | `GFX_HOK_KOR_focus_industrial_power_allocation` | `gfx/interface/goals/HOK_KOR/industrial_power_allocation.dds` | 100×88 | `203b015c15fbda591b0734a0d27bdb82c6812fb0ecddd2eac6278a5955a8802b` | `Focus Backgrounds/Circle with Ribbon2.png`<br>`Focus & National Spirits Pieces/Power Plant.png`<br>`Focus & National Spirits Pieces/Towers Electric.png`<br>`Focus & National Spirits Pieces/Electricity.png` |
| 시민사회 | `GFX_HOK_KOR_focus_parliamentary_committee` | `gfx/interface/goals/HOK_KOR/parliamentary_committee.dds` | 100×88 | `2e774310d255f16ffe2e5af68e7f00606cf017b4ca2dae8b59f89059bf5e957e` | `Focus Backgrounds/Circle with Ribbon2.png`<br>`Focus & National Spirits Pieces/Parliament.png`<br>`Focus & National Spirits Pieces/Hammer.png` |

`Hammer.png`는 기존 실제 그림 확인 기록의 의사봉이며, 공업용 망치로 설명하지 않는다.

## 한국 기업 중점 로고

선경·삼성전자·금성의 원래 `interface/ideas_HoK.gfx` 기업 그림을 신규 중점 스프라이트 별칭에 직접 연결했다. 모두 원래 64×64 DDS를 그대로 사용하며 100×88 캔버스로 확대·재가공하지 않았다. 일본 기업 그림을 대체하기 위한 신규 한국 로고 제작도 하지 않았다.

| 기업 | 새 일반 스프라이트 | 원래 프로젝트 DDS | 실제 크기 | 현재 SHA-256 |
| --- | --- | --- | --- | --- |
| 선경 | `GFX_HOK_KOR_focus_civic_sunkyong_investment` | `gfx/interface/ideas/idea_kor_sunkyong.dds` | 64×64 | `78dba446556242587ed22f84f47d8b43c2d61cf6a930b85f85620ad0710ab15a` |
| 삼성전자 | `GFX_HOK_KOR_focus_civic_samsung_electronics` | `gfx/interface/ideas/idea_kor_samsung.dds` | 64×64 | `813457200a3efa952c5b269310ee49a15092ee5ef11b0bf8bd0552746c9c7a1a` |
| 금성 | `GFX_HOK_KOR_focus_civic_goldstar_mass_production` | `gfx/interface/ideas/idea_kor_goldstar.dds` | 64×64 | `2b6fcb567ba8652c5fb8b8f374ed0eaac1b16d6b16a97d978c27d2a267d8cd47` |

## 신규 중점의 전체 이미지 연결

정의 파일은 `interface/HOK_KOR_civic_focus.gfx`이다. 각 일반 스프라이트와 같은 이름의 `_shine` 스프라이트가 동일 DDS를 참조한다. 아래 13개 일반 스프라이트가 26개 정의의 기본 그림을 모두 설명한다. 회사 로고 3개와 기존 원작 `focus_kor_begin_rearmament.dds`를 제외한 9개는 기존 계속개발 정책 아이콘 매니페스트와 현재 SHA-256이 일치한다.

| 새 일반 스프라이트 | 기존 프로젝트 DDS | 실제 크기 | 현재 SHA-256 | 기존 출처 항목 |
| --- | --- | --- | --- | --- |
| `GFX_HOK_KOR_focus_civic_industrial_compact` | `gfx/interface/goals/HOK_KOR/integrated_production_planning.dds` | 100×88 | `ee1a60d7ed29492e34e34df405682727b0f1d916400fa2f21972ae5734780bc8` | `HOK_KOR_integrated_production_planning` |
| `GFX_HOK_KOR_focus_civic_chaebol_cooperation` | `gfx/interface/goals/HOK_KOR/regional_industry_fund.dds` | 100×88 | `66dd1e6d90404b3caa71660a17aa463272d0d9cb48bcd598d3d6ad63065e8b7c` | `HOK_KOR_regional_industry_fund` |
| `GFX_HOK_KOR_focus_civic_nationalization` | `gfx/interface/goals/HOK_KOR/industrial_power_allocation.dds` | 100×88 | `203b015c15fbda591b0734a0d27bdb82c6812fb0ecddd2eac6278a5955a8802b` | `HOK_KOR_industrial_power_allocation` |
| `GFX_HOK_KOR_focus_civic_break_monopolies` | `gfx/interface/goals/HOK_KOR/public_accounts_committee.dds` | 100×88 | `4807461d8da15c8771a97dfc9356fc33596ce3bf7a69cd1eafc2d23629eac0b2` | `HOK_KOR_public_accounts_committee` |
| `GFX_HOK_KOR_focus_civic_sunkyong_investment` | `gfx/interface/ideas/idea_kor_sunkyong.dds` | 64×64 | `78dba446556242587ed22f84f47d8b43c2d61cf6a930b85f85620ad0710ab15a` | 기존 HoK 기업 로고 |
| `GFX_HOK_KOR_focus_civic_samsung_electronics` | `gfx/interface/ideas/idea_kor_samsung.dds` | 64×64 | `813457200a3efa952c5b269310ee49a15092ee5ef11b0bf8bd0552746c9c7a1a` | 기존 HoK 기업 로고 |
| `GFX_HOK_KOR_focus_civic_goldstar_mass_production` | `gfx/interface/ideas/idea_kor_goldstar.dds` | 64×64 | `2b6fcb567ba8652c5fb8b8f374ed0eaac1b16d6b16a97d978c27d2a267d8cd47` | 기존 HoK 기업 로고 |
| `GFX_HOK_KOR_focus_civic_labor_compact` | `gfx/interface/goals/HOK_KOR/skilled_workforce.dds` | 100×88 | `42751af6998c03f900a26e7104ff183e2c8a09d40a6e328ac7f5f6b8df3b64fc` | `HOK_KOR_skilled_workforce` |
| `GFX_HOK_KOR_focus_civic_mass_conscription` | `gfx/interface/goals/focus_kor_begin_rearmament.dds` | 100×88 | `44e173e45680cab9ed599cfb0051de028576f1bb4b9c2c1626311f2ba94f765a` | 기존 HoK 원작 중점 그림 |
| `GFX_HOK_KOR_focus_civic_public_accountability` | `gfx/interface/goals/HOK_KOR/parliamentary_committee.dds` | 100×88 | `2e774310d255f16ffe2e5af68e7f00606cf017b4ca2dae8b59f89059bf5e957e` | `HOK_KOR_parliamentary_committee` |
| `GFX_HOK_KOR_focus_civic_social_settlement` | `gfx/interface/goals/HOK_KOR/production_quality_assurance.dds` | 100×88 | `0b374793f6ebe5e1f58dc741a7e7cc31b699d92050d50121bef20545188057d7` | `HOK_KOR_production_quality_assurance` |
| `GFX_HOK_KOR_focus_civic_public_procurement` | `gfx/interface/goals/HOK_KOR/production_review.dds` | 100×88 | `9e7648a26ca474f67363d887e8c7057e5015b1f8a26f3a696d7895ef31cd23fe` | `HOK_KOR_production_review` |
| `GFX_HOK_KOR_focus_civic_procurement_inspections` | `gfx/interface/goals/HOK_KOR/ordnance_inspection.dds` | 100×88 | `bd9a04ee4082f3ac15eda12aaaabbf611473cabaf2eff02787b1c79254d8b6e6` | `HOK_KOR_ordnance_inspection` |

## 광택과 마스크

26개 중점 스프라이트 정의에서 일반 그림·`animationmaskfile`은 위에 매핑한 프로젝트 DDS다. `animationtexturefile`은 모두 기존 프로젝트 파일 `gfx/interface/goals/HOK_KOR/shine_overlay.dds`이며 87×88, SHA-256 `bb416649358c73d34aacd46bad61bc44211fac8111627b56e25f385ad98f4448`이다. 원본은 Paradox Interactive / HOI4 설치본의 `gfx/interface/goals/shine_overlay.dds`이며 이번에 다시 복사하거나 변환하지 않았다. 현 설치 원본과 기존 프로젝트 오버레이의 전체 바이트도 일치한다. 기존 기록은 [공산주의 내정 아이콘 크레딧](HOK_KOREAN_COMMUNIST_GOVERNANCE_ICON_CREDITS.md)과 [군수조달 아이콘 크레딧](HOK_KOREAN_FASCIST_PROCUREMENT_ICON_CREDITS.md)에 있다.

UI의 `effectFile` 참조 `gfx/FX/buttonstate.lua`와 `gfx/FX/buttonstate_nodowneffect.lua`는 기존 게임의 렌더링 효과 코드 경로다. DDS·마스크·오버레이 이미지 참조와 구분하며, 이번에 이미지로 복사하거나 새 셰이더로 제작하지 않았다.

## 국민정신·결정·사건의 추가 재사용 그림

아래 국민정신 13개 스프라이트는 `interface/HOK_KOR_spirit_icons.gfx`의 기존 정의다. 실제 크기는 모두 60×68이며 기존 [정책 아이콘 매니페스트](data/HOK_KOREAN_FOCUS_ICON_MANIFEST.json)의 해당 texture 항목에 원본 소재와 이전 가공이 기록되어 있다. 새 정신 ID가 기존 그림을 참조해도 기존 그림의 제작 시점·원저작이 바뀌지 않는다.

| 기존 스프라이트 | 프로젝트 DDS | 현재 SHA-256 |
| --- | --- | --- |
| `GFX_idea_HOK_KOR_icon_mass_production_1` | `gfx/interface/ideas/HOK_KOR/mass_production_1.dds` | `0451796ca5e538317fa337c70606262144112b5061b36b4a1ef75dcf7663311c` |
| `GFX_idea_HOK_KOR_icon_mass_production_2` | `gfx/interface/ideas/HOK_KOR/mass_production_2.dds` | `18597a2e94741a611092f9f8277a204b9544c94de03c21037832b65ed0d40b08` |
| `GFX_idea_HOK_KOR_icon_workforce_1` | `gfx/interface/ideas/HOK_KOR/workforce_1.dds` | `20ba8c432954cdd3a285631eb6b3a09c67a1c6f6111b97683f7d6d01b8e8f7e3` |
| `GFX_idea_HOK_KOR_icon_workforce_2` | `gfx/interface/ideas/HOK_KOR/workforce_2.dds` | `ed046114a046127308af6ff3b4865aed92cffd8a3d97698ed9d85adb3450cf31` |
| `GFX_idea_HOK_KOR_icon_accountable_administration_idea` | `gfx/interface/ideas/HOK_KOR/accountable_administration_idea.dds` | `cbd411e49643c33d592dfcdac874ee3cc1831871789f6681e8390705fc181a76` |
| `GFX_idea_HOK_KOR_icon_procurement_spirit_2` | `gfx/interface/ideas/HOK_KOR/procurement_spirit_2.dds` | `33ab9497ac08506503cde8c873dca296d3970e1f8228d368d519706bc23264f3` |
| `GFX_idea_HOK_KOR_icon_quality_control` | `gfx/interface/ideas/HOK_KOR/quality_control.dds` | `64e4734b246bca9fdeb30ba96a86372a4929a5be10e4bc03bfc43adf22ff8505` |
| `GFX_idea_HOK_KOR_icon_staff_spirit_2` | `gfx/interface/ideas/HOK_KOR/staff_spirit_2.dds` | `0ce22835abe89c846b81ab89373b48e2ec288ae0f0ef1fcc49b1aef4868fe0a4` |
| `GFX_idea_HOK_KOR_icon_license_participant_idea` | `gfx/interface/ideas/HOK_KOR/license_participant_idea.dds` | `8e6654a5d1af954a466cbe5da951118fee6a06ca2003f444f221cfbbd3669059` |
| `GFX_idea_HOK_KOR_icon_procurement_spirit_1` | `gfx/interface/ideas/HOK_KOR/procurement_spirit_1.dds` | `953673a4c1e0cab68acafdc1da685a8884987fe2eaae8e88e220afab0efcb5c0` |
| `GFX_idea_HOK_KOR_icon_air_maintenance_spirit` | `gfx/interface/ideas/HOK_KOR/air_maintenance_spirit.dds` | `528e2c3f82ea8cc133ea867bb43cbe0850409095f0296588c33a1329f174af71` |
| `GFX_idea_HOK_KOR_icon_public_accounts_idea` | `gfx/interface/ideas/HOK_KOR/public_accounts_idea.dds` | `006dc72fef874722bd2ab821414c73e34efd49be386f5f8b691a18b69d3b90f4` |
| `GFX_idea_HOK_KOR_icon_formation_spirit_2` | `gfx/interface/ideas/HOK_KOR/formation_spirit_2.dds` | `0ccdcf32ce0d3598e496bb70fe3cc3ddbb227d695796781d9ba3b4e85b7baf9b` |

2026-10-11의 결정·범주 연결은 기존 공산주의 내정 및 군수조달 자산을 재사용했다.2026-10-12 후속에서는 시민 카테고리와 지원·견제4개만 아래 전용 그림으로 교체했으며, 표의 공용 자산과 다른 소비자를 유지한다. 해당 모듈의 [공산주의 내정 크레딧](HOK_KOREAN_COMMUNIST_GOVERNANCE_ICON_CREDITS.md), [군수조달 크레딧](HOK_KOREAN_FASCIST_PROCUREMENT_ICON_CREDITS.md)와 각 전용 매니페스트의 원작 귀속·기존 합성 기록을 유지한다.

| 기존 스프라이트 | 프로젝트 DDS | 실제 크기 | 현재 SHA-256 | 기존 정의 |
| --- | --- | --- | --- | --- |
| `GFX_HOK_KOR_decision_yeo_labor_compact` | `gfx/interface/decisions/HOK_KOR/communist_governance/yeo_labor_compact.dds` | 32×32 | `57dacaa69f260a889e9a751ec65302303ac22700fe01b1ddc5579e1f3fdfb58a` | `interface/HOK_KOR_communist_governance_icons.gfx` |
| `GFX_HOK_KOR_decision_nrsc_material_contracts` | `gfx/interface/decisions/HOK_KOR/fascist_procurement/nrsc_material_contracts.dds` | 32×32 | `b1884485d74f096f029931c9e33bdd65a5af90cca7ea5aacf3cf156fd9e78754` | `interface/HOK_KOR_fascist_procurement_icons.gfx` |
| `GFX_HOK_KOR_decision_category_communist_governance` | `gfx/interface/decisions/HOK_KOR/communist_governance/category.dds` | 51×40 | `03dc0fea9d56a8aa1e930b41f4f7eb6387bd5f695053f27a89d0deb3d036375b` | `interface/HOK_KOR_communist_governance_icons.gfx` |
| `GFX_HOK_KOR_decision_category_fascist_procurement` | `gfx/interface/decisions/HOK_KOR/fascist_procurement/category.dds` | 51×40 | `ba072735a97396ce1772cd9fa84419c2609a4be4ad7ebced84689349143f5799` | `interface/HOK_KOR_fascist_procurement_icons.gfx` |

전투기·의회 사건 그림은 위 바닐라 복사 6개 표의 마지막 두 행이다. 로켓 사고 그림은 기존 `interface/eventpictures_HoK.gfx`의 `GFX_report_event_K002`를 재사용하며 실제 경로 `gfx/event_pictures/report_event_K002.dds`, 크기 210×176, 현재 SHA-256 `887415f7754e25c8220a9f841f8ea9addc934be9acf5724113d549e31b718b23`이다. 이 기존 원작 사건 그림의 개별 작가·최초 출처는 이번 조사에서 새로 확인하지 않았으며 기존 크레딧을 보존한다.

## 확인 범위

이 문서는 현재 소스의 스프라이트→텍스처 연결, 실제 DDS 헤더 크기, SHA-256과 바이트 복사 출처를 기록한다. 표의 이미지 파일은 모두 프로젝트 내부에 실제 존재하는 경로다. 광택의 마스크·오버레이도 같은 기준으로 추적했다. 일본 기업 로고·천황 초상·꽃 초상은 이 패널과 신규 중점에 채택하지 않았다.

이번 문서화 단계에서는 이 문서만 새로 작성했다. 이 출처 확인으로 게임의 잠김·진행·완료 광택, 패널 렌더링·클릭 영역, 지도자 전환, 정상 진행, 저장·불러오기 또는 DLC 동작을 검증했다고 주장하지 않는다. 실제 UI 관찰과 시스템 검증 결과는 별도 구현·검증 기록을 따른다.

## 2026-10-12 디시전 배지·파란 지원/견제 아이콘

사용자 구현 승인에 따라 카테고리 배지1개와 지원·견제 네 행을 전용 작은 이미지로 연결했다. 최초 문서화와 달리 이번에는 소재 재구성·배경 가공·DDS 내보내기 및 실제 화면 확인을 수행했다. 원래 중점·공용 빨간 DDS/GFX는 변경하지 않았다.

| 적용 대상 | 전용 스프라이트 | 프로젝트 DDS | 크기 | SHA-256 |
|---|---|---|---|---|
| 재벌과 시민사회 카테고리 | `GFX_HOK_KOR_decision_category_civic_balance` | `gfx/interface/decisions/HOK_KOR/civic/category.dds` |51×40|`bafbbc102e4da51ab05ca9b15910dea930dc1461994bef4eb373a5a6381cd937`|
| 재벌 지원·견제 / 시민사회 지원·견제 | `GFX_HOK_KOR_decision_civic_influence_blue` | `gfx/interface/decisions/HOK_KOR/civic/influence_blue.dds` |32×32|`c305d3c1c4a747e060f8aca551678cebf6a5986fd91467fb34161b0fcb7f19ab`|

원본은 위와 같은 Globvs / Ultimate HOI4 GFX 고정 revision과 CREDITS의 채택 파일 허용 범위를 따른다. 기존 `Circle with Ribbon2`·`Blueprints`·`Cog Wheel`·`Circular Arrows`를 카테고리에, `Circle`·`Scales`를 행에 사용했다. 채택 원본과 CREDITS를 `docs/assets/korean-civic-decision-icons/sources/`에 바이트 보존했다. 개별 작가 미상·원작 귀속을 유지하며 kpopmodder 기여는 선정·작은 크기 재구성·배경색 가공·내보내기·연결로 구분한다. 새 AI 생성이나 다운로드는 없다.

파란 원판은 분리된 배경에 민주 팔레트RGB(53,91,126)를 적용했다. 금속 테두리·저울·알파에 전체 색조 필터를 씌우지 않았다. 카테고리는 기존 산업RGB(100,100,95) 배경과 금색 장식을 유지한다. 정확한 소재 해시·배경 마스크·배치·DDS 형식·결정 ID는 [전용 매니페스트](data/HOK_KOREAN_CIVIC_DECISION_ICON_MANIFEST.json)에 기록한다.

원래 빨간 저울 재구성은 기존 DDS와 바이트까지 같았고, 파란 최종본의1024개 알파 바이트도 기존과 동일하다.51×40/32×32의 BGRA32 단일 프레임과 소스 보존을 확인했다. 전체 재시작575f에서 배지·불가 표시·접기/펼치기를, 외부 수동 fixture2430에서 가능·지원 실행 후 표시를 확인했다. 일반 진행·모든 배율/DLC 검증으로 확대하지 않는다. 실제 관측과 테스트 정리는 [아이콘 구현 기록](incidents/2026-10-12-korean-civic-decision-icons.md)을 따른다.
