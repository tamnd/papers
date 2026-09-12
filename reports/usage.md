# Usage

What the corpus cost in machine time, by stage.

This is read from the ledger, which is one line per ask and lives at `~/.config/papers/ledger.jsonl` on the machine that did the work. The ledger is not in this repository and will not be: it names the hosts that were asked. Nothing below names a host.

Nothing has been asked of a model yet, so there is nothing to count. A paper that came through the native extraction path never puts a question to a model, by design, and a corpus built entirely that way has an empty ledger and an honest zero here.

## Pages read

Counted off the committed English content, one page counted once per paper however many sections were cut from it. `native` is pdftotext on a born digital file with no model anywhere in the path, so those pages were never guessed. `layout` is a layout model reading the page geometry and `ocr` is a vision model reading a page image, and only those two cost anything in the tables below.

| path | papers | pages | what read them |
| --- | --: | --: | --- |
| native | 6 | 32 | pdftotext version 26.09.0 |

## Per stage

A target is the thing one ask was about: a page for the extract stage, a section for translate. Asks are higher than targets when a host did not answer and the question went to the next one.

| stage | asks | answered | refused | targets | tokens in | tokens out | time | cost |
| --- | --: | --: | --: | --: | --: | --: | --: | --: |
| extract | 0 | 0 | 0 | 0 | 0 | 0 | 0s | - |
| figures | 0 | 0 | 0 | 0 | 0 | 0 | 0s | - |
| refs | 0 | 0 | 0 | 0 | 0 | 0 | 0s | - |
| glossary | 0 | 0 | 0 | 0 | 0 | 0 | 0s | - |
| translate | 0 | 0 | 0 | 0 | 0 | 0 | 0s | - |
