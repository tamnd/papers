---
paper: silver-2016-alphago
title: Mastering the game of Go with deep neural networks and tree search
authors:
  - David Silver
  - Aja Huang
  - Chris J. Maddison
  - Arthur Guez
  - Laurent Sifre
  - George van den Driessche
  - Julian Schrittwieser
  - Ioannis Antonoglou
  - Veda Panneershelvam
  - Marc Lanctot
year: 2016
venue: Nature
field: ai-ml
section_title: Front Matter
tag: 01A4
kind: front
lang: en
source: https://storage.googleapis.com/deepmind-media/alphago/AlphaGoNaturePaper.pdf
pdf_sha256: 9c9184385a3d37b4f4e9d9715270986c43172747b1d08f29093128c1ef878b60
pdf_pages: 1-3
extraction: vision
extraction_model: gpt-5
content_sha256: 52f6dc20585ccc9fea30d7103718d2270d69b381f5d7f965e5a1a62eb0d11372
prompt_sha256: e1b070d511afab62a45db64b491e759e38eaa12f6c7943b773a942f4f2f70935
---

doi:10.1038/nature16961

**The game of Go has long been viewed as the most challenging of classic games for artificial intelligence owing to its enormous search space and the difficulty of evaluating board positions and moves. Here we introduce a new approach to computer Go that uses ‘value networks’ to evaluate board positions and ‘policy networks’ to select moves. These deep neural networks are trained by a novel combination of supervised learning from human expert games, and reinforcement learning from games of self-play. Without any lookahead search, the neural networks play at the level of state-of-the-art Monte Carlo tree search programs that simulate thousands of random games of self-play. We also introduce a new search algorithm that combines Monte Carlo simulation with value and policy networks. Using this search algorithm, our program AlphaGo achieved a 99.8% winning rate against other Go programs, and defeated the human European Go champion by 5 games to 0. This is the first time that a computer program has defeated a human professional player in the full-sized game of Go, a feat previously thought to be at least a decade away.**
