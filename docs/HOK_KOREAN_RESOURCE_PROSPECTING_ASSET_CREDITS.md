# 강원·포항 자원 탐사 디시전 이미지 출처

작성: **2026-11-06 (Asia/Seoul)**. 대상은 「강원도 탄광 확장」·「포항 제철소 확장」의 디시전 행 이미지 2개다. **원본 소형 DDS의 바이트 보존 복사와 프로젝트 소유 GFX 연결을 준비했으며, 이 이미지 작업에서는 게임을 실행하지 않았다.** 비용·기간·자원 보상·AI·현지화는 이미지 작업의 변경 대상이 아니다.

이 이미지를 교체하거나 재사용 출처를 확인할 때는 [개발 자료 보관 안내](HOK_DEVELOPMENT_ARTIFACT_ARCHIVE.md), [현재 이미지 제작 방침](HOK_KOREAN_FOCUS_SPIRIT_ICON_PLAN.md), [소형 디시전 아이콘 크기 기록](incidents/2026-09-22-korean-decision-icon-size.md)을 먼저 읽는다. 정책 동작을 변경할 때는 별도의 [반복 자원 탐사 명세](HOK_KOREAN_REPEATABLE_RESOURCE_PROSPECTING_SPEC.md)를 따른다.

## 출처·저작자·사용 범위

원저작자는 **Paradox Interactive**다. 읽기 전용 설치 원본 `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`의 공용 소형 자원 이미지 2개를 선택했다. 출처 버전은 상위 구현 작업에서 확인한 **Operation Postern v1.19.4.2.2da5 / Steam build 26409260**이다. 이 이미지 작업이 버전이나 게임 실행을 새로 확인한 것은 아니다.

두 파일은 같은 게임인 HOI4용 HOK 모드에서 사용하는 원본 게임 자산이다. [Paradox의 공식 게시물에 인용된 Modding Policy 7항](https://store.steampowered.com/oldnews/?appgroupname=stellaris&appids=281990&enddate=1777618800&feed=steam_community_announcements&l=greek)은 Paradox 소유 콘텐츠를 쓰는 모드가 대응 게임·DLC 설치자에게만 사용되도록 할 것을 요구한다. 게시물이 연결한 [원 정책](https://forum.paradoxplaza.com/forum/threads/updated-14-06-18-rules-for-user-made-mods-and-edits-of-pds-games.708039/)의 본문은 도구 접근 제한으로 직접 읽지 못했으며, 여기서는 공식 게시물의 해당 인용과 이 두 HOI4 자산의 동일 게임용 사용 범위를 기록한다. 기존 자원 탐사 범주의 DLC 조건은 변경하지 않는다.

게임 자산의 저작권과 사용 조건은 Paradox에 남는다. 별도 오픈소스·MIT·CC 라이선스나 타 게임·독립 이미지 팩으로의 사용 권한을 주장하지 않는다. 새 그림·AI 생성물·원작 HOK 제작자의 신작으로 표시하지 않는다. 계속개발 기여는 **kpopmodder의 대상 선정, 내부 보존 복사, 전용 스프라이트 연결, 출처 기록과 정적 검수**다.

## 원본과 프로젝트 사본

아래 원본 경로는 위 설치 원본에 상대적이며, 게임용 파일과 GFX의 경로는 모드 루트에 상대적이다. 원본을 수정하지 않고 전체 DDS를 그대로 복사했다.

| 대상·콘텐츠 ID | 원본 | 게임용 파일 | 규격·바이트 |
|---|---|---|---|
| 강원도 탄광 확장 `HOK_KOR_expand_gangwon_coal_mines` | `gfx/interface/decisions/decision_coal.dds` | [gangwon_coal.dds](../gfx/interface/decisions/HOK_KOR/resource_prospecting/gangwon_coal.dds) | **33×32**, 4,352바이트 |
| 포항 제철소 확장 `HOK_KOR_expand_pohang_steelworks` | `gfx/interface/decisions/decision_steel.dds` | [pohang_steel.dds](../gfx/interface/decisions/HOK_KOR/resource_prospecting/pohang_steel.dds) | **34×30**, 4,208바이트 |

두 파일은 알파를 포함한 **비압축 BGRA32 DDS**다. 색상·소재·비율·알파·프레임·헤더를 보존했으며 리사이즈·재색칠·재압축·단계 표시는 하지 않았다. 석탄 파일의 mipmap-count 헤더는 1, 강철은 0이며 두 파일 모두 실제 파일 길이가 헤더와 한 장의 32비트 이미지 크기에 일치한다. 이를 동일한 헤더 값으로 정규화하지 않았다.

원본과 게임용 사본 각각의 SHA-256은 다음과 같이 동일하다.

- 석탄: `352a18868c7aa8297427cf05f88eb58df21e067bb85b6b87fe84715636d3b0ea`
- 강철: `688461188713c346cfb7ecf366c64b714c7586ecd7ced64cd5851f9e28602a8a`

[전용 GFX](../interface/HOK_KOR_resource_prospecting_icons.gfx)는 아래 프로젝트 소유 스프라이트를 내부 DDS에 연결한다. 원본 `GFX_decision_coal`·`GFX_decision_steel` 정의를 덮어쓰지 않는다.

- `GFX_HOK_KOR_decision_expand_gangwon_coal_mines`
- `GFX_HOK_KOR_decision_expand_pohang_steelworks`

원본 GFX 대응은 설치 원본 `interface/decisions.gfx:2831`의 석탄과 `:768`의 강철이다. 이 원본 정의와 두 디시전의 실제 `icon` 연결은 구분하며, 게임 코드 쪽 연결은 상위 구현 작업에서 수행한다.

## 32×32 기준과 원본 크기 보존

프로젝트의 새 디시전 행 이미지 기준은 32×32다. 이번 두 파일은 원본 자원 디시전이 사용하는 **이미 소형으로 제작된 자원 그림**이므로, 현재 설치 GUI의 행 경계를 확인한 뒤 원본 규격을 보존했다. 큰 중점·국민정신 그림을 행에 직접 넣거나 전체 GUI 행을 확대하지 않았다.

확인한 파일은 설치 원본 `interface/countrydecisionview.gui`다. 일반 행은 398~437행의 높이 41·아이콘 중심 (30,19)·제목 x63, 기간제 행은 584~637행의 높이 40·아이콘 중심 (32,20)·제목 x62를 사용한다. 해당 아이콘 블록에는 별도 크기 축소 설정이 없다.

| 이미지 | 일반 행의 이론상 이미지 경계 | 일반 행 제목까지 여백 | 기간제 행의 이론상 이미지 경계 | 기간제 행 제목까지 여백 |
|---|---|---:|---|---:|
| 석탄 33×32 | x13.5~46.5 / y3~35 | 16.5px | x15.5~48.5 / y4~36 | 13.5px |
| 강철 34×30 | x13~47 / y4~34 | 16px | x15~49 / y5~35 | 13px |

이는 중심·캔버스 크기를 이용한 **정적 좌표 계산**이며 실제 렌더링의 픽셀 반올림이나 게임 화면 관측을 대신하지 않는다. 알파가 0을 초과하는 실제 그림의 원본 경계는 석탄 (6,1)~(28,31), 강철 (1,6)~(33,28)로 캔버스 안에 있다. 원본의 투명 여백과 작고 서로 다른 자원 소재를 유지한다.

## 수행한 확인과 외부 자료

- 원본·사본 바이트 및 SHA-256 일치, DDS 헤더·크기·파일 길이·BGRA32·알파 범위를 확인했다.
- 새 스프라이트 이름은 도입 전 프로젝트와 설치 원본 interface에서 검색했으며 충돌이 발견되지 않았다. 내부 경로·대소문자와 실제 사본 존재를 확인했다.
- 실제 크기와 8배 최근접 확대 미리보기를 직접 관찰했다. 석탄과 강철이 구별되며 어두운 배경에서 외곽선과 명암이 유지된다. 일반·기간제 행 좌표를 사용한 별도 배치 그림에서 제목 시작선과 이미지 사이 공간을 확인했다.
- 미리보기는 Python 표준 라이브러리로 비압축 BGRA32를 읽어 PNG로 만든 외부 검토 자료다. 런타임 DDS에는 변환을 적용하지 않았다. 새 패키지나 도구를 설치하지 않았다.

외부 증거·미리보기 위치는 `C:\hoi\test\hok-resource-prospecting-20261106-01\assets\`다. `prepare_resource_icons.py`, `asset-copy-verification.json`, `gangwon_coal-native.png`, `pohang_steel-native.png`, `native-icons-8x.png`, `native-ui-layout.png`가 있다. 배치 그림은 위에서부터 석탄 일반/기간제·강철 일반/기간제이며, 파란 세로선은 제목 시작 위치다. 배경·경계선은 설명용이며 **게임 스크린샷이 아니다**. 최초 Python 3.14·3.12에서 Pillow 가져오기는 실패했고 파일 복사 전에 종료됐다. 이후 외부 helper를 표준 라이브러리 방식으로 바꿔 사본·미리보기를 만들었다.

관련 파일·해시·sprite·원본 경로와 정적 배치 정보는 [전용 매니페스트](data/HOK_KOREAN_RESOURCE_PROSPECTING_ASSET_MANIFEST.json)에 기록한다. 저장소에는 런타임 DDS·GFX와 유지할 출처 문서·매니페스트만 추가한다.

**실제 UI 상태:** 이미지 하위 작업 자체는 정적 검토였다. 이후 상위 구현의 `ui-main-02`·`ui-main-03` 실행에서 2564×1504 창의 자원 탐사 목록에 두 아이콘과 제목이 정상 표시되는 것을 관측했다. 실제 클릭 전 사용 가능 행, 클릭 후 90일 진행 행, 완료 후 재사용 행을 구분해 확인했다. 증거는 외부 작업 루트의 `runs/ui-main-02/ui/`와 `runs/ui-main-03/ui/`에 있고 [구현·검증 기록](incidents/2026-11-06-korean-repeatable-resource-prospecting.md)에 범위를 남긴다. 다른 배율·해상도까지 검증한 것으로 확대하지 않는다.
