# 긴급 원료 순환체계 아이콘 출처·제작 기록

작성: 2026-10-02. [원료 순환체계 명세](HOK_KOREAN_MATERIAL_CYCLE_REWARD_SPEC.md)의 신규 임시 국민정신·디시전·범주 전용 이미지 3개를 기록한다. 기존 원료 순환체계 I·II 아이콘은 수정하지 않았다.

## 출처와 재사용 근거

선정 소재는 [Ultimate HOI4 GFX](https://github.com/Globvs/Ultimate-HOI4-GFX/tree/3626dc83c8573d6603fa497138090b04b64a15ba)의 고정 커밋 `3626dc83c8573d6603fa497138090b04b64a15ba`에서 가져왔다. 해당 커밋의 [CREDITS](https://github.com/Globvs/Ultimate-HOI4-GFX/blob/3626dc83c8573d6603fa497138090b04b64a15ba/CREDITS.txt)는 기여자의 동의와 자유로운 사용을 명시한다. 이를 이번에 선택한 팩의 Circle·Circular Arrows·Steel·Factories2에 대한 재사용 근거로 기록하며, 다른 모드 전체나 별도 이미지에 대한 허가로 확대하지 않는다.

원저작은 Globvs와 Ultimate HOI4 GFX의 기여자들에게 있다. 원본 CREDITS의 HOI4 GFX Modding Database, ThePinkPanzer, Gunnar von Pontius, Pacifica, That Guy Called Curly, Deathlinger, Edouard_Saladier, scarecroww, joshyflip, Indycyclone77, grestin, AtomicSoviet 및 The New Order 귀속 정보를 그대로 보존했다. 원본은 개별 소재와 작가를 일대일로 연결하지 않으므로 특정 파일의 작가를 추정하지 않는다.

| 원본 소재 | 선정 원본 보존 경로 | SHA-256 |
|---|---|---|
| National Spirit Backgrounds/Circle.png | `docs/assets/korean-material-cycle-icons/sources/Circle.png` | `11004efa4f5cafa05524bd1293d6fc464b42c0e33f0dd740a67de4c52bf17804` |
| Focus & National Spirits Pieces/Circular Arrows.png | 같은 폴더의 `Circular Arrows.png` | `49d17868495b84cabeef78c85a2111adf8d325a5b76a0cb72973f51f9150f4c4` |
| Focus & National Spirits Pieces/Steel.png | 같은 폴더의 `Steel.png` | `1b118fdadfd2d4b0f1bb3b16735913c5cacb428a0ae4dde490f747160236294a` |
| Focus & National Spirits Pieces/Factories2.png | 같은 폴더의 `Factories2.png` | `10898f9e4600558cd329d8bcb601cb453d89d8b46d90d079ce328294a96a31a7` |
| CREDITS.txt | 같은 폴더의 `CREDITS.txt` | `cf220dc66463d75163f7690ad77b02b662d0c05ca5d53dc62d33ed504512a7f5` |

원본 URL·치수·해시와 최종 조합은 [이미지 매니페스트](data/HOK_KOREAN_MATERIAL_CYCLE_ICON_MANIFEST.json)를 따른다. 선택한 소스만 프로젝트에 보존하고 베이스게임·워크숍 원본은 수정하지 않았다.

2026-10-03 커밋 준비 과정에서 `.gitattributes`에 원본 `CREDITS.txt`와 해시를 기록한 GFX 파일만 `-text`로 지정했다. PC의 `core.autocrlf` 설정이 달라도 두 파일의 원본 바이트와 매니페스트 해시를 유지한다. 원본 CREDITS 6행의 끝 공백도 그대로 보존하며, 공백 검사는 이 원본 파일을 제외한 커밋 대상에 적용했다.

## 후속 제작과 최종 연결

kpopmodder의 후속 기여는 소재 선택·산업색 배경 처리·전용 크기 재구성·시계 표식 직접 작성·DDS 출력·GFX 연결이다. AI 생성 이미지는 사용하지 않았다. 시계는 원·눈금·바늘 도형으로 직접 작성했으며, 별도 참조 이미지 없이 만든 원본을 `docs/assets/korean-material-cycle-icons/sources/clock-original.png`에 보존했다(`c3e1c0f0392a062d5de4c155a779449526fe405421adf09b394157c46e8fdfc9`).

산업 공통 분야 RGB(100,100,95)의 중립 회색 배경을 사용했다. 배경만 조정하고 금속 테두리·주제·알파는 보존했다. 임시 국민정신은 순환 화살표·금속·제련시설에 시계 표식을 붙이고 I·II·III 단계 표기를 만들지 않았다. 결정과 범주는 큰 정신 이미지를 그대로 연결하지 않고 각각 별도 소형 이미지로 재구성했다.

| 대상 | 크기 | 최종 프로젝트 경로 | SHA-256 |
|---|---|---|---|
| 임시 국민정신 | 60×68 | `gfx/interface/ideas/HOK_KOR/material_cycle/cmn_emergency_material_cycle_boost.dds` | `386b9f24720bcdd04eb8176a1aa3458f42f6d5aa691e89cb5dbaf5e97b0d6d2f` |
| 디시전 행 | 32×32 | `gfx/interface/decisions/HOK_KOR/material_cycle/cmn_emergency_material_cycle.dds` | `8de32fbdd83fe1d5137906dac2ad9070aa56dcf1ce7975ead397d27c61867ac7` |
| 범주 헤더 | 51×40 | `gfx/interface/decisions/HOK_KOR/material_cycle/cmn_material_cycle_projects.dds` | `5ca46c1b4b2247487eda7d41aa6580bfbead10f642911014c912182775754dc3` |

DDS는 BGRA32 비압축·기본 프레임 1개·명시적 알파로 출력했다. `interface/HOK_KOR_material_cycle_icons.gfx`에서 프로젝트 소유 스프라이트 3개와 모드 상대경로로 연결하며, 정확한 스프라이트명·picture·조합 위치·해시는 매니페스트에 기록한다.

## 확인 범위

이미지 작업의 정적 확인은 37 PASS / 0 FAIL이다. DDS 헤더·치수·알파·내부 경로·대소문자·해시·스프라이트 충돌·선정 원본·기존 I·II 보존을 확인했다. 별도 콘텐츠 검토의 238 PASS / 0 FAIL과 겹치는 항목이 있으므로 독립적인 275개 검사로 합산하지 않는다.

실제 크기 연락시트를 기존 원료 순환체계 II와 나란히 확인했다. 소형 행·헤더의 주제와 여백, 시계 표식 및 산업색을 직접 검수했으며, 이 결과는 게임 내 아이콘 위치·행 간격·활성·비활성 표시의 검증을 대신하지 않는다. 연락시트와 제작 스크립트·상세 검사 보고서는 `C:\hoi\test\material-cycle-20261002\art\`에 보존했다. 실제 게임 UI 검사 상태는 [구현 기록](incidents/2026-10-02-korean-material-cycle.md)을 따른다.
