# Usage

What the corpus cost in machine time, by stage.

This is read from the ledger, which is one line per ask and lives at `~/.config/papers/ledger.jsonl` on the machine that did the work. The ledger is not in this repository and will not be: it names the hosts that were asked. Nothing below names a host.

52 asks, 50 of them answered. 564,131 tokens in, 31,553 out, 35m 43s of waiting over 27 targets, from 2026-09-12 to 2026-09-12.

## Pages read

Counted off the committed English content, one page counted once per paper however many sections were cut from it. `native` is pdftotext on a born digital file with no model anywhere in the path, so those pages were never guessed. `layout` is a layout model reading the page geometry and `ocr` is a vision model reading a page image, and only those two cost anything in the tables below.

| path | papers | pages | what read them |
| --- | --: | --: | --- |
| native | 4 | 8 | pdftotext version 26.09.0 |
| vision | 3 | 25 | olmOCR-2-7B-1025-FP8 |

## Per stage

A target is the thing one ask was about: a page for the extract stage, a section for translate. Asks are higher than targets when a host did not answer and the question went to the next one.

| stage | asks | answered | refused | targets | tokens in | tokens out | time | cost |
| --- | --: | --: | --: | --: | --: | --: | --: | --: |
| extract | 52 | 50 | 0 | 27 | 564,131 | 31,553 | 35m 43s | - |
| figures | 0 | 0 | 0 | 0 | 0 | 0 | 0s | - |
| refs | 0 | 0 | 0 | 0 | 0 | 0 | 0s | - |
| glossary | 0 | 0 | 0 | 0 | 0 | 0 | 0s | - |
| translate | 0 | 0 | 0 | 0 | 0 | 0 | 0s | - |

52 of the 52 asks went to a model with no price set, so the money column is a dash for them. Most of this corpus is built on a subscription and on free gateways, where an ask costs a turn rather than a sum of money, and writing zero dollars there would be claiming a measurement nobody made. A price table is a JSON file of dollars per million tokens by model, passed with `papers report usage -prices`.

## Per model

| model | asks | tokens in | tokens out | cost |
| --- | --: | --: | --: | --: |
| not recorded | 2 | 0 | 0 | - |
| gpt-5-6 | 6 | 7,506 | 719 | - |
| reader-a | 44 | 556,625 | 30,834 | - |

## Per paper

In id order rather than in order of cost, so that two of these reports can be read side by side.

| paper | stage | targets | tokens in | tokens out | time |
| --- | --- | --: | --: | --: | --: |
| codd-1970-relational | extract | 3 | 34,073 | 4,183 | 59.4s |
| nakamoto-2008-bitcoin | extract | 9 | 219,924 | 10,067 | 14m 42s |
| vaswani-2017-attention | extract | 15 | 310,134 | 17,303 | 20m 1s |

## What did not answer

| stage | why | asks |
| --- | --- | --: |
| extract | unreachable | 2 |
