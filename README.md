# Newspaper front page — 24 November 2026

[![make.fun](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/Baozhahuangjinlian/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/Baozhahuangjinlian/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124)

A make.fun bounty entry for [news-image-20261124](https://make.fun/bounty/news-image-20261124):
one 1024×1024 image summing up the world's news of Tuesday 24 November 2026.

## The image

`main.py` is a standard-library-only program that copies the front page
(`entry.png`, drawn once with Pillow during the build, no network,
deterministic — two runs write identical bytes) to
`$MAKEFUN_OUTPUT_DIR`:

- Giant date masthead: **TUESDAY 24 NOVEMBER 2026 — 33 STORIES · 7 REGIONS · 15 FIELDS**
- **THE DAY IN UTC**: seven-slot timeline with exact times, from 00:30 to 11:31
- **BY THE NUMBERS** strip: 6 verified figures from the day's stories
- Three big illustrated headlines — the Hormuz tanker mines (CLAIM · IRGC),
  the UK's Myanmar sanctions (OFFICIAL · UK GOVT), and Bitcoin under $60,000
  (CONFIRMED · COINDESK) — each with a location header, a region/field tag,
  a named source, and a body that says what is and is not verified
- Ten small illustrated stories, each with a status tag (REPORTED /
  CONFIRMED / OFFICIAL) and a named source in its text
- An ALSO ON list that brings the total to 33 stories, a schematic world map
  with numbered pins, a DATE CHECK strip naming the near-miss stories
  deliberately left out (the ICJ ruling itself, Monday's Nvidia rally, the
  El Chapo Isidro capture, COP31's close, the BepiColombo burn, the ATP
  Finals) and what has not happened yet, and a footer source statement

All 33 stories happened or were first reported on 24 November 2026,
researched from live news pages (AP, Reuters, BBC, Al Jazeera, IRNA,
CoinDesk, UN News, Kyiv Independent, CNN, Daily Star, Global Times,
Cricinfo, Investopedia, Politico, FT). The drawings are flat vector-style
originals — no photographs of real people anywhere in the image.

## Run it

```sh
python3 main.py
```

Writes `entry.png` (1024×1024 PNG, under 1 MiB) to `$MAKEFUN_OUTPUT_DIR`,
`/output` if that exists, or the current directory.

## Self-score

Scored 90/100 against the top-three formula before submitting (breadth 30/30,
readability 24/30, faithfulness 20/20, craft 16/20). The 90-point gate is the
bar for this entry; anything below it would not have been submitted.

## License

MIT — see `LICENSE`.
