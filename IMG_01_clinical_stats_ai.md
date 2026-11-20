# 이미지 제작 명세서 · `01_clinical_stats_ai`

| 항목 | 값 |
|---|---|
| 페이지 | 01 · 신약은 어떤 숫자로 허가받는가 — 임상시험의 통계와 AI |
| 분야 | 통계학(주) · 인공지능(보조) |
| 주 앵커 | B 연구실 앵커 (재판정 · 고리 던지기 · 다트 · 봉인된 시험지) |
| 그림체 | 16비트 RPG풍 픽셀아트, 굵은 어두운 외곽선(`#1d1a22` 계열), 명암 2~3단계 |
| 장면 조명 | 낮의 연구실 — 큰 창의 자연광, 흰 벽, 연보라·민트·분홍 소품, 밝은 중간 톤. 밤·어둠·네온 금지 |
| 시즌 | 기본 (시즌 의상 없음) |
| 글자 | 그림 안에 글자·숫자·로고를 넣지 않는다. 칠판·기록지는 줄무늬나 빈 자리로 둔다 |
| 공통 금지 | 무기·담배·술·피, 실존 인물·기업 로고, 저작권 캐릭터, 결과 전 승패를 암시하는 표정 |

## 1. 그림 목록

| 키 | 판 | 자리 | 상태 | 우선 |
|---|---|---|---|---|
| `cover_01` | L (1920×1080) | 페이지 맨 위 글 표지 | **새로 그릴 것** | P1 |
| `bg_01` | F (1920×720) | 히어로 뒤 넓은 배경 | 새로 그릴 것 (없으면 절차적 픽셀아트로 대체 중) | P1 |
| `sc_01_outro` | E (1200×800) | 아웃트로 장면 | **새로 그릴 것** | P2 |
| `thumb_01` | I (600×400) | 목차 카드 썸네일 | `cover_01`을 3:2로 자름 | P2 |
| `og_01` | K (1200×630) | 공유 미리보기 | `cover_01`에서 자름 | P3 |
| `doc_think` `doc_front` `doc_board` `doc_magic` | A | 표지·해설·판정·아웃트로 | **재사용** (캐릭터 팩 1.4) | — |
| `asst_smile` `asst_report` `asst_firm` `asst_spark` | B | 숫자 발표·기본 | **재사용** | — |
| `fly_clip` `fly_point` `fly_magnify` `fly_coffee` `fly_arms` | C | 의심·대결·아웃트로 | **재사용** | — |
| `robo_coin` `robo_calc` `robo_meh` | D | 확신·지표 계산·판정 보류 | **재사용** | — |
| 행동으로 보기 6종 | — | 저울·고리·다트·지도·띠·봉인 상자 | **코드** (Canvas 2D) | — |

재사용 키는 `packs/character/character_pack/webp/96`에서 `--pick`으로 뽑아 base64로 넣었다(18장, 85.6 KB). 새로 그릴 그림은 세 장뿐이다.

## 2. 대결 결과와 표정 짝

이 페이지의 대결 결과는 **C(조건부)**다. 캐릭터 팩 5-8 표의 조건부 줄을 쓴다.

| 자리 | 박사 | 조수 | 초파리 | 주판봇 |
|---|---|---|---|---|
| 결과 보기 전 | `doc_think` | `asst_firm` | `fly_point` | `robo_coin` |
| 결과 뒤 (C) | `doc_think` | `asst_report` | `fly_coffee` | `robo_calc` |
| 아웃트로 | `doc_magic` | `asst_report` | `fly_coffee` | `robo_meh` |

결과를 보기 전 표정에 승패가 드러나지 않는다. 판정 보류이므로 아웃트로에서 어느 쪽도 승자 자리에 두지 않는다.

## 3. 새로 그릴 그림의 프롬프트

### 3-1. `cover_01` — 글 표지 (L판, 1920×1080, 16:9)

안전 영역: 왼쪽 아래 구석 28%는 제목 글자가 얹히므로 단순하게 비운다. 네 캐릭터는 가운데에서 오른쪽에 배치하고, 얼굴은 가장자리에서 60px 안쪽에 둔다.

구도: 낮의 연구실 측정실. 가운데에 **고리 던지기 놀이판**이 놓여 있고, 바닥에 박힌 나무 말뚝 하나를 빛나는 고리 여러 개가 둘러싸거나 비껴 나가 있다. 박사가 말뚝을 가리키고, 조수는 기록지를 들고 고리를 세고, 초파리 연구원은 돋보기로 비껴 난 고리를 들여다보고, 주판봇은 주판을 든 채 고리 더미 쪽을 본다.

```
16-bit RPG pixel art, bold dark outlines, 2-3 tone shading, 16:9 wide composition, 1920x1080.
A sunlit measuring room beside a bright white laboratory, large window light from the upper right,
lavender and mint props. On the floor sits a ring toss game: one wooden peg driven into a low wooden
base, with many thin glowing rings around it, some encircling the peg and some lying off to the side.
Four characters stand to the right of centre.
A chibi scientist with thin teal rectangular glasses, spiky black hair with one white streak, a small
ponytail at the back, white lab coat over black vest and tie, pointing at the wooden peg.
A girl researcher with long pink hair in two round buns and a navy streak, blue eyes, white lab coat
over lavender hoodie, jeans, holding a blank clipboard and counting the rings.
An anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold
stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings,
crouching and inspecting a stray ring through a magnifying glass.
A boxy beige retro CRT-monitor robot with a dark green screen face, mint pixel eyes and mouth, a short
antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a
wooden abacus and looking toward the pile of rings.
Height order, strictly: scientist tallest, girl researcher slightly shorter, robot shorter still,
fruit fly smallest.
Leave the lower-left quarter of the image visually simple and uncluttered.
No text, no letters, no numbers, no logos anywhere in the image. No weapons, no alcohol, no blood.
Bright daytime palette, no night scene, no neon.
```

대체 글: “연구실 측정실 바닥의 고리 던지기 놀이판 앞에 선 네 사람. 말뚝 하나를 고리 여러 개가 둘러싸고 일부는 비껴 나가 있다.”

### 3-2. `bg_01` — 히어로 배경 (F판, 1920×720, 8:3)

왼쪽 45%에 제목이 얹히므로 복잡한 것은 오른쪽에 둔다. 인물은 없거나 아주 작게.

```
16-bit RPG pixel art, bold dark outlines, 8:3 ultra-wide background, 1920x720, no characters.
A bright white laboratory measuring room in daytime. Left 45% is mostly empty wall and floor with soft
window light. Right side holds a long workbench with a brass balance scale, three graduated cylinders
with purple, green and blue liquid, a tape measure, and a blank grid board covered with small scattered
dots. A tall window in the upper right casts clean daylight.
Muted mid-tone palette with lavender, mint and soft blue accents. No text, no numbers, no logos.
```

대체 글: “낮의 연구실 측정실 배경. 오른쪽에 저울, 눈금 실린더 세 개, 점이 흩어진 모눈판이 있다.”

### 3-3. `sc_01_outro` — 아웃트로 장면 (E판, 1200×800, 3:2)

판정 보류로 끝난 자리. 승자를 앞에 두지 않고 넷이 같은 칠판을 본다. 중요한 것은 위쪽 62% 안에 둔다.

```
16-bit RPG pixel art, bold dark outlines, 3:2 composition, 1200x800.
Inside the same bright daytime laboratory. Four characters stand in a loose half circle facing a large
blank board that shows only two simple horizontal bars of different length, drawn as plain shapes with
no text or numbers. The chibi scientist stands at the centre with faint purple sparks in both hands,
calm and pleased. The girl researcher stands beside him holding a blank clipboard, speaking. The fruit
fly researcher sits on the bench edge holding a small coffee cup, relaxed. The boxy CRT robot stands on
the other side with its arms lowered and a flat neutral screen expression.
Neither rival is placed in front of the other; both are the same distance from the board.
Keep all faces within the upper 62% of the frame. Bright daytime light, lavender and mint accents.
No text, no letters, no numbers, no logos.
```

대체 글: “연구실에서 네 사람이 막대 두 개만 그려진 칠판을 함께 보고 있다. 어느 쪽도 승자 자리에 서 있지 않다.”

## 4. 반영 방법

1. 받은 그림을 `cover_01.png`, `bg_01.png`, `sc_01_outro.png`로 저장한다.
2. `build_character_pack.py --ingest ./받은그림 --plates cover_01=L,bg_01=F,sc_01_outro=E --out received_01`로 판에 맞게 처리한다.
3. 표지는 `<!-- lab-cover -->` 표시 사이에만 넣고 본문은 바꾸지 않는다. 다른 두 장은 해당 `data-img` 자리의 대체 상자를 `<img>`로 교체한다.
4. WebP로 변환해 내장하고, 한 편 합계 600 KB 이하를 지킨다(현재 캐릭터 그림 85.6 KB 사용 중).
5. 썸네일과 공유 미리보기는 `cover_01`을 잘라 `assets/img/`에 따로 둔다.

## 5. 매니페스트

```json
{
  "page": "01_clinical_stats_ai",
  "domain": ["stats", "ai"],
  "anchorType": "B",
  "duelResult": "C",
  "style": "16bit-rpg-pixel-art",
  "season": "base",
  "images": [
    {"key": "cover_01",    "plate": "L", "size": "1920x1080", "status": "to-draw", "priority": "P1"},
    {"key": "bg_01",       "plate": "F", "size": "1920x720",  "status": "to-draw", "priority": "P1", "fallback": "procedural-pixel-canvas"},
    {"key": "sc_01_outro", "plate": "E", "size": "1200x800",  "status": "to-draw", "priority": "P2", "fallback": "css-placeholder"},
    {"key": "thumb_01",    "plate": "I", "size": "600x400",   "status": "crop-from", "from": "cover_01", "priority": "P2"},
    {"key": "og_01",       "plate": "K", "size": "1200x630",  "status": "crop-from", "from": "cover_01", "priority": "P3"}
  ],
  "reused": ["doc_think","doc_front","doc_board","doc_magic","asst_smile","asst_report","asst_firm","asst_spark","fly_clip","fly_point","fly_magnify","fly_coffee","fly_arms","robo_coin","robo_calc","robo_meh"],
  "code": ["저울(재판정)","고리 던지기","다트 과녁","서열 지도","무리별 점유율 띠","봉인 상자"],
  "characterPack": {"repo": "adminmrobo/fruitfly-lab-expressions", "commit": "86d04ac", "size": 96, "bytes": 87654}
}
```
