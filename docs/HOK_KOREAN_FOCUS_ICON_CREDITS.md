# 한국 신규 중점·국민정신 아이콘 출처와 가공 기록

기록일: 2026-09-22. 대상: 신규 중점 60개와 국민정신 정의 29개에 연결한 DDS 89개. 기존 원작 콘텐츠의 그림과 게임 효과는 이 기록의 변경 대상에 포함하지 않는다.

## 채택 자료와 사용 근거

채택한 외부 그림은 [Globvs / Ultimate HOI4 GFX](https://github.com/Globvs/Ultimate-HOI4-GFX)의 PNG 부품·배경 48개다. 완성된 DDS 아이콘을 그대로 가져온 것이 아니라, 공개 팩의 소재를 정책 계열에 맞게 조합했다.

| 항목 | 기록 |
|---|---|
| 고정 원본 커밋 | `3626dc83c8573d6603fa497138090b04b64a15ba` |
| 해당 커밋의 Git 트리 | `324da3225785a8754d5038fb71fe95667b8d81a1` |
| 확인한 사용 근거 | [고정 커밋의 CREDITS.txt](https://github.com/Globvs/Ultimate-HOI4-GFX/blob/3626dc83c8573d6603fa497138090b04b64a15ba/CREDITS.txt) |
| 원문 보존본 | [UPSTREAM_CREDITS.txt](assets/korean-focus-icons/UPSTREAM_CREDITS.txt), 원본 1,029바이트 그대로 복사 |
| 원문 SHA-256 | `cf220dc66463d75163f7690ad77b02b662d0c05ca5d53dc62d33ed504512a7f5` |
| 코드 작업 기준선 | `698b6eb160efbaa04a4d43846330ba002f5e8cc7` |
| 개별 적용 기록 | [아이콘 매니페스트](data/HOK_KOREAN_FOCUS_ICON_MANIFEST.json) |

CREDITS는 다음과 같이 기여자 동의와 자유로운 사용을 명시한다.

> The following people or websites have contributed to Ultimate HOI4 GFX, all with consent, and all free to use:

이 근거는 해당 공개 팩에 수록된 소재에 적용한다. 기여자가 참여한 다른 모드 전체의 그림을 사용할 수 있다는 뜻으로 확대하지 않는다. 별도의 MIT·CC 등 정형 라이선스를 추정해서 붙이지 않았다. 제작자에게 별도 연락하거나 개별 허가를 받은 사실은 없다.

Europe Anew 공개 팩, Kaiserreich, Road to 56의 그림은 이번 구현에 채택하지 않았다. 새로 생성한 AI 이미지는 사용하지 않았다.

## 원 기여자와 계속개발 기여의 구분

원본 소재의 기여 표시는 **Globvs / Ultimate HOI4 GFX contributors**로 기록한다. upstream CREDITS는 파일별 원저자를 연결하지 않으므로, 아래 48개 파일 각각의 개별 원저자는 미상이다. 저장소 소유자·커밋 업로더를 각 그림의 원저자로 단정하지 않는다.

원문 전체를 보존하며, 그 집합 기여자 목록은 다음과 같다. 이 목록이 모든 사람이 채택된 모든 파일을 공동 제작했다는 의미는 아니다.

| 원문 이름·자료원 | upstream이 설명한 기여 범위 |
|---|---|
| Globvs / 저장소 작성자 | 여러 템플릿; 원문에서는 `me`로 표현 |
| HOI4 GFX Modding Database | 중점·국민정신 부품, 장관·국기 템플릿 |
| ThePinkPanzer | 중점·국민정신 부품 |
| Gunnar von Pontius | Photoshop 스마트 오브젝트 |
| Pacifica | 국민정신 아이콘 |
| That Guy Called Curly | 국민정신 부품 |
| Deathlinger | 국민정신 배경과 일부 중점 부품 |
| Edouard_Saladier | 중점 배경·아이콘 |
| scarecroww | 중점 부품용 스마트 오브젝트 |
| joshyflip | 스마트 오브젝트·중점 부품 |
| Indycyclone77 | 중점 아이콘 부품 |
| grestin | 중점 아이콘 부품 |
| AtomicSoviet | The New Order 제공 경위를 명시한 중점 아이콘 부품 |

계속개발 기여자 **kpopmodder**의 이번 작업은 소재 선정, 정책별 조합, 레이어 배치, 투명 여백 정리, 비율을 유지한 크기 조정, 선별한 함선 부품의 명암 보정, 그리고 게임용 DDS 변환이다. 단계 `I`·`II`·`III` 배지, 동계 눈송이, 의료 표식, 검사 확인 표시는 계속개발 작업에서 추가했다. 원본 부품과 배경의 저작을 계속개발 팀의 신규 원화로 표시하지 않는다.

DDS 변환은 BGRA32 형식의 기술적 변환이며, 부품의 원저작과 구분한다. 매니페스트의 각 중점·국민정신 항목은 사용한 원본 경로, 가공 내역, 최종 텍스처 경로, 스프라이트 또는 그림 참조, 최종 DDS SHA-256을 기록한다. 동일한 소재를 공유하는 정책 강화 단계도 해당 항목별로 추적할 수 있다.

## 파일명과 실제 그림의 확인

원본 파일명은 출처 추적을 위해 그대로 기록하지만, 사용 목적은 실제 이미지를 열어 확인한 뒤 정했다.

| 파일 | 실제 확인한 그림과 처리 |
|---|---|
| `Boot.png` | 철모. 동계훈련·상륙연습의 군사 소재로 채택했고, 부츠를 표현한 것으로 설명하지 않는다. |
| `Hammer.png` | 의사봉. 의회 위원회 소재로 채택했고, 공업용 망치로 취급하지 않는다. |
| `Wheat2.png` | 밀 이삭. 농촌교육에 채택. `Wheat.png`는 신발 그림이어서 채택하지 않음. |
| `Briefcase2.png` | 가죽가방. 계속개발 측 의료 표식을 더해 의료지원에 사용. |
| `Paper.png`, `Paper Sign.png` | 서류와 서명하는 그림. `Documents.png`는 가죽가방이어서 행정 서류 소재로 채택하지 않음. |
| `Manchu Snowflake.png` | 금색 만주 상징. 동계용 눈송이로 오인하지 않고 제외. |
| `Hospital.png` | 현대 고층병원. 이번 시대·의료지원 표현에 맞지 않아 제외. |
| `Walkie Talkie.png` | 현대 스마트폰. 무전기 소재로 오인하지 않고 제외. |
| `Cross.png` | 종교용 라틴 십자가. 의료 표식으로 사용하지 않음. |

## 실제 채택한 원본 48개

다음 표에는 최종 89개 텍스처에서 참조한 원본만 싣는다. 검토용으로 내려받았지만 채택하지 않은 파일은 포함하지 않는다. 모든 링크는 위 커밋에 고정한 정확한 원본 파일 URL이며, SHA-256은 가공 전 PNG 바이트의 해시다. 개별 파일의 원저자 상태와 사용 근거는 앞 절에 공통으로 적용된다.

| 원본 경로·직접 링크 | 원본 크기 | 원본 SHA-256 |
|---|---|---|
| [Focus & National Spirits Pieces/Aircraft Fighter.png](https://raw.githubusercontent.com/Globvs/Ultimate-HOI4-GFX/3626dc83c8573d6603fa497138090b04b64a15ba/Focus%20%26%20National%20Spirits%20Pieces/Aircraft%20Fighter.png) | 73×38 | `f072283c024ac7e88317443d6a0144fe19217f1073c115e42d5fce6876efef5d` |
| [Focus & National Spirits Pieces/Anchor.png](https://raw.githubusercontent.com/Globvs/Ultimate-HOI4-GFX/3626dc83c8573d6603fa497138090b04b64a15ba/Focus%20%26%20National%20Spirits%20Pieces/Anchor.png) | 56×70 | `2b805f2d637d8aa26e189699bb4013a5c79398de540dd3a93e922b76acf4a49e` |
| [Focus & National Spirits Pieces/Artillery.png](https://raw.githubusercontent.com/Globvs/Ultimate-HOI4-GFX/3626dc83c8573d6603fa497138090b04b64a15ba/Focus%20%26%20National%20Spirits%20Pieces/Artillery.png) | 65×54 | `7e870d4c21869521217f74ce6721f7167c131a388d9600b41fefe056b2777af6` |
| [Focus & National Spirits Pieces/Battleship.png](https://raw.githubusercontent.com/Globvs/Ultimate-HOI4-GFX/3626dc83c8573d6603fa497138090b04b64a15ba/Focus%20%26%20National%20Spirits%20Pieces/Battleship.png) | 45×55 | `e8fce17b146e946967f7c33e05cbf06da0a501ba4e6892c5b82a1856093b15f7` |
| [Focus & National Spirits Pieces/Binoculars.png](https://raw.githubusercontent.com/Globvs/Ultimate-HOI4-GFX/3626dc83c8573d6603fa497138090b04b64a15ba/Focus%20%26%20National%20Spirits%20Pieces/Binoculars.png) | 57×46 | `3d4c629e4422bb00430cb056f67918da6ecdaa88016f88c64b2dc89f5560b836` |
| [Focus & National Spirits Pieces/Blueprints.png](https://raw.githubusercontent.com/Globvs/Ultimate-HOI4-GFX/3626dc83c8573d6603fa497138090b04b64a15ba/Focus%20%26%20National%20Spirits%20Pieces/Blueprints.png) | 45×36 | `1d75e423748392240bd246dc9681b2787c8f0c19c6200bf4a412a14809def3e4` |
| [Focus & National Spirits Pieces/Book Open.png](https://raw.githubusercontent.com/Globvs/Ultimate-HOI4-GFX/3626dc83c8573d6603fa497138090b04b64a15ba/Focus%20%26%20National%20Spirits%20Pieces/Book%20Open.png) | 73×55 | `b8f601a26d8e0ad7f8eecdccca2c447a59921e15aa05bb0078142b803ed25e9d` |
| [Focus & National Spirits Pieces/Boot.png](https://raw.githubusercontent.com/Globvs/Ultimate-HOI4-GFX/3626dc83c8573d6603fa497138090b04b64a15ba/Focus%20%26%20National%20Spirits%20Pieces/Boot.png) | 60×55 | `7bc25680260b633c63c569d8e6eef17808b78a1e3900db66b38bcc0f9bf5fd2b` |
| [Focus & National Spirits Pieces/Briefcase2.png](https://raw.githubusercontent.com/Globvs/Ultimate-HOI4-GFX/3626dc83c8573d6603fa497138090b04b64a15ba/Focus%20%26%20National%20Spirits%20Pieces/Briefcase2.png) | 57×54 | `0ed20621f1f1c11098c1101cb47edf2d06bfde0b97bae275239043ed495b3628` |
| [Focus & National Spirits Pieces/Bullets.png](https://raw.githubusercontent.com/Globvs/Ultimate-HOI4-GFX/3626dc83c8573d6603fa497138090b04b64a15ba/Focus%20%26%20National%20Spirits%20Pieces/Bullets.png) | 37×38 | `b10eabf21e4090bef7283c3290a0c2bcd50ce8506522bd1a50f4eac158d084a7` |
| [Focus & National Spirits Pieces/Cannon Twins.png](https://raw.githubusercontent.com/Globvs/Ultimate-HOI4-GFX/3626dc83c8573d6603fa497138090b04b64a15ba/Focus%20%26%20National%20Spirits%20Pieces/Cannon%20Twins.png) | 69×65 | `0ec66d5ef7949f99a5603d3c52c2608ec3195494fe82f1538c63b41aeaec006d` |
| [Focus & National Spirits Pieces/Carrier.png](https://raw.githubusercontent.com/Globvs/Ultimate-HOI4-GFX/3626dc83c8573d6603fa497138090b04b64a15ba/Focus%20%26%20National%20Spirits%20Pieces/Carrier.png) | 78×40 | `c04e18029a861c0e466ca5ba7416a39e2a17594455d05165f4a96b153ef86d73` |
| [Focus & National Spirits Pieces/Circular Arrows.png](https://raw.githubusercontent.com/Globvs/Ultimate-HOI4-GFX/3626dc83c8573d6603fa497138090b04b64a15ba/Focus%20%26%20National%20Spirits%20Pieces/Circular%20Arrows.png) | 58×59 | `49d17868495b84cabeef78c85a2111adf8d325a5b76a0cb72973f51f9150f4c4` |
| [Focus & National Spirits Pieces/Cog Wheel.png](https://raw.githubusercontent.com/Globvs/Ultimate-HOI4-GFX/3626dc83c8573d6603fa497138090b04b64a15ba/Focus%20%26%20National%20Spirits%20Pieces/Cog%20Wheel.png) | 42×41 | `8765480f16fbfd54babe02163ad5db3a68e0472e18789c1880ee40c6b12a3ada` |
| [Focus & National Spirits Pieces/Coins.png](https://raw.githubusercontent.com/Globvs/Ultimate-HOI4-GFX/3626dc83c8573d6603fa497138090b04b64a15ba/Focus%20%26%20National%20Spirits%20Pieces/Coins.png) | 43×22 | `545398fd3cf250a89a03d4a92e7f1bcebe3b28c7b3196894243af19d5a728407` |
| [Focus & National Spirits Pieces/Crate.png](https://raw.githubusercontent.com/Globvs/Ultimate-HOI4-GFX/3626dc83c8573d6603fa497138090b04b64a15ba/Focus%20%26%20National%20Spirits%20Pieces/Crate.png) | 75×75 | `4efdb13ea21e1fc35019c1efdb2b7594739f47d8c4d7a8ce43060a2c2860dd17` |
| [Focus & National Spirits Pieces/Electricity.png](https://raw.githubusercontent.com/Globvs/Ultimate-HOI4-GFX/3626dc83c8573d6603fa497138090b04b64a15ba/Focus%20%26%20National%20Spirits%20Pieces/Electricity.png) | 27×42 | `9dd1d2abf5e050db4a9d0e5a84ba435a140067e8f2ba6fc73fa9caaab4393a1c` |
| [Focus & National Spirits Pieces/Factories2.png](https://raw.githubusercontent.com/Globvs/Ultimate-HOI4-GFX/3626dc83c8573d6603fa497138090b04b64a15ba/Focus%20%26%20National%20Spirits%20Pieces/Factories2.png) | 49×37 | `10898f9e4600558cd329d8bcb601cb453d89d8b46d90d079ce328294a96a31a7` |
| [Focus & National Spirits Pieces/Global Trade.png](https://raw.githubusercontent.com/Globvs/Ultimate-HOI4-GFX/3626dc83c8573d6603fa497138090b04b64a15ba/Focus%20%26%20National%20Spirits%20Pieces/Global%20Trade.png) | 51×44 | `e9f22863d098bd2f23536c4e9c08988e399ee84796d25b5f717e3cc33f7e7821` |
| [Focus & National Spirits Pieces/Hammer.png](https://raw.githubusercontent.com/Globvs/Ultimate-HOI4-GFX/3626dc83c8573d6603fa497138090b04b64a15ba/Focus%20%26%20National%20Spirits%20Pieces/Hammer.png) | 69×49 | `c413553c81cd9060a3692259203d777477ea6154493ba764938a7d15b08a35dc` |
| [Focus & National Spirits Pieces/Hand Out.png](https://raw.githubusercontent.com/Globvs/Ultimate-HOI4-GFX/3626dc83c8573d6603fa497138090b04b64a15ba/Focus%20%26%20National%20Spirits%20Pieces/Hand%20Out.png) | 46×30 | `869586ae9629904ee98467edebb5e35bbb41b18ad1b22da2f22d182196e9b563` |
| [Focus & National Spirits Pieces/Hands Shaking.png](https://raw.githubusercontent.com/Globvs/Ultimate-HOI4-GFX/3626dc83c8573d6603fa497138090b04b64a15ba/Focus%20%26%20National%20Spirits%20Pieces/Hands%20Shaking.png) | 47×39 | `33da602c5a3ff1ee05077afdb7d12f13b7a94a0cbc296bb97330f0becd5cbb25` |
| [Focus & National Spirits Pieces/Island.png](https://raw.githubusercontent.com/Globvs/Ultimate-HOI4-GFX/3626dc83c8573d6603fa497138090b04b64a15ba/Focus%20%26%20National%20Spirits%20Pieces/Island.png) | 49×53 | `5e31219e2d53949988cf4c1b7de2f3a81991c04dd99dabf48aabd10ff27c5de1` |
| [Focus & National Spirits Pieces/Lantern.png](https://raw.githubusercontent.com/Globvs/Ultimate-HOI4-GFX/3626dc83c8573d6603fa497138090b04b64a15ba/Focus%20%26%20National%20Spirits%20Pieces/Lantern.png) | 29×73 | `f0cebd4c0df7045fcc222abe571fb2e0ee192c4eaf028d9321779b68d47f7a02` |
| [Focus & National Spirits Pieces/Magnifying Glass.png](https://raw.githubusercontent.com/Globvs/Ultimate-HOI4-GFX/3626dc83c8573d6603fa497138090b04b64a15ba/Focus%20%26%20National%20Spirits%20Pieces/Magnifying%20Glass.png) | 39×34 | `bea177a67a7890adbdb4c79ad689e2d4e271a8db3216f77295e6c46aec7f8674` |
| [Focus & National Spirits Pieces/Map with Sextant.png](https://raw.githubusercontent.com/Globvs/Ultimate-HOI4-GFX/3626dc83c8573d6603fa497138090b04b64a15ba/Focus%20%26%20National%20Spirits%20Pieces/Map%20with%20Sextant.png) | 60×50 | `4f89b8b062e3c3b7e4cd4d4dfe9affc860949cbb0b855a0347e622307e8d67a7` |
| [Focus & National Spirits Pieces/Paper Sign.png](https://raw.githubusercontent.com/Globvs/Ultimate-HOI4-GFX/3626dc83c8573d6603fa497138090b04b64a15ba/Focus%20%26%20National%20Spirits%20Pieces/Paper%20Sign.png) | 68×35 | `e623b233c2ba688421edd3048ce4940073014ed6b423039b77c9e35c6006a8b0` |
| [Focus & National Spirits Pieces/Paper.png](https://raw.githubusercontent.com/Globvs/Ultimate-HOI4-GFX/3626dc83c8573d6603fa497138090b04b64a15ba/Focus%20%26%20National%20Spirits%20Pieces/Paper.png) | 47×51 | `f702a6971726ba0608f75cb71a90fc8f0ac0cc0474a2cd5ca172330dbf3c803c` |
| [Focus & National Spirits Pieces/Parliament.png](https://raw.githubusercontent.com/Globvs/Ultimate-HOI4-GFX/3626dc83c8573d6603fa497138090b04b64a15ba/Focus%20%26%20National%20Spirits%20Pieces/Parliament.png) | 88×33 | `c6e3b610167c239d3c39809156fd08a8799834f53020f7ac797d3d346a6d9993` |
| [Focus & National Spirits Pieces/Power Plant.png](https://raw.githubusercontent.com/Globvs/Ultimate-HOI4-GFX/3626dc83c8573d6603fa497138090b04b64a15ba/Focus%20%26%20National%20Spirits%20Pieces/Power%20Plant.png) | 57×51 | `b3b6ea27284b3ff043f4c7e5739ee928bbf179df1a2dbb324e7c27b0cb93218f` |
| [Focus & National Spirits Pieces/Radar Tower.png](https://raw.githubusercontent.com/Globvs/Ultimate-HOI4-GFX/3626dc83c8573d6603fa497138090b04b64a15ba/Focus%20%26%20National%20Spirits%20Pieces/Radar%20Tower.png) | 58×56 | `15390b984da3cab8ed2bf0e48ac40aa0ad38c6228ad05cdfd51d427a0ee43f05` |
| [Focus & National Spirits Pieces/Scales.png](https://raw.githubusercontent.com/Globvs/Ultimate-HOI4-GFX/3626dc83c8573d6603fa497138090b04b64a15ba/Focus%20%26%20National%20Spirits%20Pieces/Scales.png) | 58×69 | `c0ac5a1a677c551cc40fcbf7f3a1cde31b000368793aafc070117c1ed24a27b4` |
| [Focus & National Spirits Pieces/Shield.png](https://raw.githubusercontent.com/Globvs/Ultimate-HOI4-GFX/3626dc83c8573d6603fa497138090b04b64a15ba/Focus%20%26%20National%20Spirits%20Pieces/Shield.png) | 53×57 | `a8afd464c5401e8489cdd632362a5c2b576385cb5fef22cfdb310d590ac94e02` |
| [Focus & National Spirits Pieces/Ship Small.png](https://raw.githubusercontent.com/Globvs/Ultimate-HOI4-GFX/3626dc83c8573d6603fa497138090b04b64a15ba/Focus%20%26%20National%20Spirits%20Pieces/Ship%20Small.png) | 88×31 | `8ab3b27c12ed50e58c729f16bf5990be4112f40ed462e081c6c22b5b09f90b21` |
| [Focus & National Spirits Pieces/Ship Submarine.png](https://raw.githubusercontent.com/Globvs/Ultimate-HOI4-GFX/3626dc83c8573d6603fa497138090b04b64a15ba/Focus%20%26%20National%20Spirits%20Pieces/Ship%20Submarine.png) | 82×24 | `0b76b7fd1de37cacbd2d5b6472348e2ca1f7fd39a8f5470ef68561e41b4e1c44` |
| [Focus & National Spirits Pieces/Towers Electric.png](https://raw.githubusercontent.com/Globvs/Ultimate-HOI4-GFX/3626dc83c8573d6603fa497138090b04b64a15ba/Focus%20%26%20National%20Spirits%20Pieces/Towers%20Electric.png) | 56×52 | `eeaec87403da21e150be1bb77de6b93f36d5243df2d972ea3ad014fe007985c5` |
| [Focus & National Spirits Pieces/Truck.png](https://raw.githubusercontent.com/Globvs/Ultimate-HOI4-GFX/3626dc83c8573d6603fa497138090b04b64a15ba/Focus%20%26%20National%20Spirits%20Pieces/Truck.png) | 76×66 | `69a26a0dccc4dddc8cdbaaa253f6381a0b43d085ca29e09c8bd549a22f7388c4` |
| [Focus & National Spirits Pieces/Vial.png](https://raw.githubusercontent.com/Globvs/Ultimate-HOI4-GFX/3626dc83c8573d6603fa497138090b04b64a15ba/Focus%20%26%20National%20Spirits%20Pieces/Vial.png) | 36×47 | `eaeaf724c4d23e8b9ed98527d27ac9156138a51dc2c1f3cd1ada3d7b4edc239a` |
| [Focus & National Spirits Pieces/Volunteer.png](https://raw.githubusercontent.com/Globvs/Ultimate-HOI4-GFX/3626dc83c8573d6603fa497138090b04b64a15ba/Focus%20%26%20National%20Spirits%20Pieces/Volunteer.png) | 65×51 | `32f3ac929ec16814609b4703f478d4cbc6ee3ee09b16952951a6d4851a228852` |
| [Focus & National Spirits Pieces/Wheat2.png](https://raw.githubusercontent.com/Globvs/Ultimate-HOI4-GFX/3626dc83c8573d6603fa497138090b04b64a15ba/Focus%20%26%20National%20Spirits%20Pieces/Wheat2.png) | 19×52 | `14ba5dd63e9721ed74c55e0857fb2c2fbca82112da641127a97f7c3ae0e90d9f` |
| [Focus & National Spirits Pieces/Worker.png](https://raw.githubusercontent.com/Globvs/Ultimate-HOI4-GFX/3626dc83c8573d6603fa497138090b04b64a15ba/Focus%20%26%20National%20Spirits%20Pieces/Worker.png) | 30×46 | `ce24044539a35f6355c012450c02910e5957281391ff85ca9d88f017ea0d87ff` |
| [Focus & National Spirits Pieces/Wrench.png](https://raw.githubusercontent.com/Globvs/Ultimate-HOI4-GFX/3626dc83c8573d6603fa497138090b04b64a15ba/Focus%20%26%20National%20Spirits%20Pieces/Wrench.png) | 59×53 | `8bb9e9f9322f567f6ac8a8d50b2aa186845d56c3ffc638a16f8e6ff29a10d09f` |
| [Focus & National Spirits Pieces/Wrenches Crossed.png](https://raw.githubusercontent.com/Globvs/Ultimate-HOI4-GFX/3626dc83c8573d6603fa497138090b04b64a15ba/Focus%20%26%20National%20Spirits%20Pieces/Wrenches%20Crossed.png) | 59×53 | `73e8577b06e02cb2c30d2d675f9b310e8532bc31c4889837ccb77292dfa1b94a` |
| [Focus Backgrounds/Circle with Ribbon2.png](https://raw.githubusercontent.com/Globvs/Ultimate-HOI4-GFX/3626dc83c8573d6603fa497138090b04b64a15ba/Focus%20Backgrounds/Circle%20with%20Ribbon2.png) | 100×88 | `5bcf53259a04276b1586f6c83f7a35a14ba9d22742ea75fb4802911978db2f95` |
| [National Spirit Backgrounds/Airforce.png](https://raw.githubusercontent.com/Globvs/Ultimate-HOI4-GFX/3626dc83c8573d6603fa497138090b04b64a15ba/National%20Spirit%20Backgrounds/Airforce.png) | 60×68 | `33dc1dedbeacaee4e0f97c86b9a135d8b3248c4d7c4532372b561d7e77b03a48` |
| [National Spirit Backgrounds/Circle.png](https://raw.githubusercontent.com/Globvs/Ultimate-HOI4-GFX/3626dc83c8573d6603fa497138090b04b64a15ba/National%20Spirit%20Backgrounds/Circle.png) | 64×64 | `11004efa4f5cafa05524bd1293d6fc464b42c0e33f0dd740a67de4c52bf17804` |
| [National Spirit Backgrounds/Naval.png](https://raw.githubusercontent.com/Globvs/Ultimate-HOI4-GFX/3626dc83c8573d6603fa497138090b04b64a15ba/National%20Spirit%20Backgrounds/Naval.png) | 60×68 | `3289d46407bab14e69cc0ae7bce1124f21d0d15117ff9745c839a6066fe52ab3` |
| [National Spirit Backgrounds/Shield Blue.png](https://raw.githubusercontent.com/Globvs/Ultimate-HOI4-GFX/3626dc83c8573d6603fa497138090b04b64a15ba/National%20Spirit%20Backgrounds/Shield%20Blue.png) | 60×68 | `a9b1fb64ab7c75395f3ba86fa8ea049a48f585eb1d4ce6ae30b58312822e4785` |

## 검증 범위

이 문서는 원본 사용 근거, 출처, 소재 선정 및 가공 내역의 기록이다. 원본 48개와 보존 CREDITS의 SHA-256을 로컬 보존본과 대조했다. 게임 UI에서의 표시·잠금·진행·완료 상태 검증이나 런타임 호환성 검증을 이 출처 문서만으로 주장하지 않는다. 최종 출력별 관계와 해시는 [아이콘 매니페스트](data/HOK_KOREAN_FOCUS_ICON_MANIFEST.json)를 따른다.

## 배경 색상 가공 추가 — 2026-09-22

사용자가 선택한 기존 `System.Drawing` 합성 방식을 사용하여 신규 60개·29개 안에서 정치 가지·정책 분야별 배경색을 적용했다. 계속개발 기여자 `kpopmodder`의 추가 가공은 배경색 분류, 배경 픽셀의 마스크 선정, 원본 밝기에 따른 색조 변환, 기존 중심 소재·장식·단계 표식과의 재합성 및 DDS 출력이다. AI 이미지 생성이나 새 도구 설치는 사용하지 않았다.

중점 60개·국민정신 22개의 DDS를 수정했고, 이미 남색·은색 배경을 사용하는 해군 국민정신 4개와 공군 국민정신 3개는 바이트 그대로 유지했다. 산업 회색·교육 은색·육군 올리브·해군 남색·공군 은청색·민주 청색의 정확한 기준 RGB는 [색상 기록 8절](HOK_KOREAN_FOCUS_ICON_COLOR_PLAN.md#8-배경색-구현--2026-09-22)을 따른다. 기준색은 음영 계산용 견본이며 단색 채우기가 아니다.

원본 48개·고정 커밋·원본 해시·보존 CREDITS·원 기여자 표시는 그대로 유지한다. 추가된 PNG는 기존 원본의 배경색 가공본이며 별도 외부 원화 10개를 새로 채택한 것이 아니다. 원본 소재의 저작을 계속개발 기여로 바꾸거나 공개 팩의 사용 근거를 다른 모드 전체로 확대하지 않는다.

파생 배경 PNG 10개와 마스크 PNG 10개는 [배경 기록 폴더](assets/korean-focus-icon-colors/backgrounds)에 있다. 매니페스트의 항목별 `color_background`에 원본·파생 배경·마스크 경로와 해시를, `pre_color_sha256`에 기존 DDS 해시를, `sha256`에 현재 DDS 해시를 기록한다. `color_revision`에는 팔레트와 변환식·마스크 조건·배정 예외를 기록했다. [색상 전후 비교](assets/korean-focus-icon-colors/index.html)와 [작업·검증 기록](incidents/2026-09-22-korean-focus-icon-colors.md)은 이전 아이콘 구현의 갤러리·런타임 증거와 구분한다. 이번 색상의 런타임은 미실행이다.
