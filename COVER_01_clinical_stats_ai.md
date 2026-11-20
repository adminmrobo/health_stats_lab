# 글 표지 지시문 · `cover_01`

| 항목 | 값 |
|---|---|
| 페이지 | 01 · 신약은 어떤 숫자로 허가받는가 |
| 키 | `cover_01` |
| 판 | L (1920×1080 이상, 16:9) |
| 빌드 후 | 1600×900 + 960×540 |
| 주제 은유 | **고리 던지기** — 말뚝(참값)은 고정, 고리(신뢰구간)가 움직인다 |
| 등장 | 네 캐릭터 모두 (박사 · 조수 하루 · 초파리 연구원 · 주판봇) |
| 시즌 | 기본 |
| 안전 영역 | 왼쪽 아래 28%는 제목이 얹히므로 단순하게 비운다. 얼굴은 가장자리에서 60px 안쪽 |

## Genspark 등에 붙여 넣기

### 한국어 지시

첨부한 캐릭터 기본 그림 네 장과 **같은 캐릭터, 같은 그림체**로 16:9 가로 표지 한 장을 만들어 주세요.

- 그림체는 16비트 RPG풍 픽셀아트입니다. 굵은 어두운 외곽선, 명암 2~3단계, 작은 반사광.
- 장소는 낮의 연구실 옆 측정실입니다. 오른쪽 위 큰 창으로 자연광이 들어오고, 흰 벽에 연보라·민트 소품이 놓여 있습니다. 밤·어둠·네온 분위기는 쓰지 마세요.
- 바닥 가운데에 **고리 던지기 놀이판**을 놓아 주세요. 낮은 나무 받침에 말뚝 하나가 박혀 있고, 얇게 빛나는 고리 여러 개가 말뚝을 둘러싸거나 옆으로 비껴 나가 있습니다.
- 네 캐릭터는 가운데에서 오른쪽에 모여 섭니다. 박사가 말뚝을 가리키고, 조수는 빈 기록지를 들고 고리를 세고, 초파리 연구원은 비껴 난 고리를 돋보기로 들여다보고, 주판봇은 나무 주판을 든 채 고리 더미 쪽을 봅니다.
- 키 순서를 꼭 지켜 주세요: **박사 > 조수 > 주판봇 > 초파리**.
- **그림 안에 글자·숫자·로고를 넣지 마세요.** 제목은 나중에 HTML로 얹습니다. 칠판이나 기록지는 빈 자리나 줄무늬로 둡니다.
- 왼쪽 아래 4분의 1은 비교적 단순하게 비워 주세요. 그 자리에 제목이 들어갑니다.
- 무기·담배·술·피, 실존 인물이나 기업 로고는 넣지 마세요.

### 영어 프롬프트

```
16-bit RPG pixel art, bold dark outlines, 2-3 tone shading, small specular highlights,
16:9 wide composition, 1920x1080, bright daytime palette.

Scene: a sunlit measuring room beside a bright white laboratory. Large window light from the upper
right, white walls, lavender and mint props, a long workbench in the background with a brass balance
scale and graduated cylinders.

Centre of the floor: a ring toss game. One wooden peg driven into a low wooden base, surrounded by many
thin glowing rings — some encircling the peg, several lying off to one side, missing it.

Four characters gathered centre-right:
- A chibi scientist with thin teal rectangular glasses, spiky black hair with one white streak, a small
  ponytail at the back, white lab coat over black vest and tie, pointing at the wooden peg.
- A girl researcher with long pink hair in two round buns and a navy streak, blue eyes, white lab coat
  over a lavender hoodie, jeans, holding a blank clipboard and counting the rings.
- An anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold
  stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings,
  crouching to inspect a stray ring through a magnifying glass.
- A boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, a short
  antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a
  wooden abacus, looking toward the pile of rings.

Height order, strictly: scientist tallest, girl researcher slightly shorter, robot shorter still,
fruit fly smallest.

Keep the lower-left quarter visually simple and uncluttered.
No text, no letters, no numbers, no logos anywhere. No weapons, no alcohol, no blood.
No night scene, no neon lighting.
```

## 대체 글 (alt)

> 연구실 측정실 바닥의 고리 던지기 놀이판 앞에 모여 선 네 사람. 나무 말뚝 하나를 빛나는 고리 여러 개가 둘러싸고, 일부는 옆으로 비껴 나가 있다.

## 받은 뒤 점검 (18-15-1)

- [ ] 비율이 16:9이고 가로가 1600px 이상인가
- [ ] 그림 안에 글자·숫자·로고가 없는가
- [ ] 네 캐릭터의 고정 외형이 지켜졌는가 (박사 안경·흰 브릿지, 조수 두 번·남색 브릿지, 초파리 파란 헬멧·금줄, 주판봇 상자형 CRT·주판알 안테나)
- [ ] 키 순서가 박사 > 조수 > 주판봇 > 초파리인가
- [ ] 주판봇이 흰 둥근 머리·노란 눈·공중 부유로 그려지지 않았는가 (회사 캐릭터와 섞이면 다시 요청)
- [ ] 왼쪽 아래 구석이 제목을 얹을 만큼 단순한가
- [ ] 밤·네온 분위기가 아닌가
- [ ] 결과를 암시하는 표정(한쪽이 이긴 듯한 표정)이 없는가 — 이 페이지의 대결은 판정 보류다

## 반영

```
build_character_pack.py --ingest ./받은표지 --plates cover_01=L --out received_01
```

생성된 WebP를 `<!-- lab-cover -->` 표시 사이의 대체 표지 자리와 교체하고, 본문은 바꾸지 않는다. `thumb_01`(600×400)과 `og_01`(1200×630)은 같은 그림을 잘라 `assets/img/`에 둔다.
