# papers

A hundred computer science papers as tagged Markdown, in English, Vietnamese, Chinese and Japanese, with the mathematics, the figures, the code and the bibliographies kept intact.

This repository is the corpus. The toolchain that builds it is [tamnd/papers-reader](https://github.com/tamnd/papers-reader), and the model plumbing under that is [tamnd/llm](https://github.com/tamnd/llm).

There is no PDF here and there never will be. See [Licensing](#licensing).

## Status

Everything is at `listed`. The manifest holds the hundred, nothing has been resolved, fetched or extracted yet, and `reports/coverage.md` will say so in numbers as soon as there is anything to count.

## Layout

```
manifests/
  papers.yaml            the hundred, and everything added after
  collections.yaml       named reading lists over them
  sources.yaml           where each PDF was found, and under what licence
  glossary.yaml          the controlled vocabulary, English to vi, zh and ja
  figures.yaml           every figure: page, bounding box, caption, hash
  refs/<id>.yaml         the parsed bibliography of one paper
  pages/<id>.yaml        which page of the file is which page of the paper
content/en/<id>/
  00_front.md            title, authors, venue, abstract
  01_<slug>.md           one file per top level section
  NN_references.md       the bibliography, rendered
content/vi/<id>/         the same tree, translated
content/zh/<id>/
content/ja/<id>/
figures/<id>/f01.png     cropped diagrams, committed, size capped
tags/                    permanent identifiers, append only
reports/                 coverage, audit, usage, citation graph
```

`pdf/`, `images/` and `work/` are gitignored and hold the source PDFs, the page rasters and the queues. None of them belong in a public repository.

## Paper ids

An id is `<surname>-<year>-<keyword>`, lowercase ASCII with hyphens, and it never changes.

```
turing-1936-computable      shannon-1948-communication
hoare-1962-quicksort        codd-1970-relational
lamport-1978-clocks         vaswani-2017-attention
```

The keyword is the word a person would use in conversation, not a word taken mechanically off the title, because the point of the id is that somebody can type it from memory. If a keyword turns out to be a poor choice it stays, and the better name goes in `aka`. Renaming an id would break every tag line, every figure path, every citation edge and every translation's record of what it was made from, and nothing here can follow such a rename.

## Tags

Every section, numbered statement, numbered equation, figure, table and listing carries a four hex digit tag. Tags are append only, never reused and never edited.

```markdown
### 3.2 Multi-Head Attention {#vaswani-2017-attention-s3-2 .section tag=0A3F}
```

`tags/tags` is the register, one line per anchored item. A tag is what lets the four languages point at the same paragraph, and what the citation graph joins on when one paper in the corpus cites another.

The one exception to the attribute block is the section a whole file is. Its heading lives in the front matter rather than in the body, so its tag lives there too, as a `tag` field. `tags/runs` records the range of tags each assignment handed out, because tags climb in reading order within one run and deliberately do not climb across runs: a section added to a paper next year takes a tag from the top of the register and sits between two much lower ones.

## Provenance

Every content file opens with YAML front matter recording where the text came from: the source PDF hash, the pages, the extraction path, and for a translation the English file it was made from together with the SHA-256 of that file as it stood at the time.

That last field is the one that earns its keep. It lets a single pass over the corpus list every translated file whose English has since changed, so a stale file is detectably stale instead of quietly wrong.

The extraction path is one of three and they are not interchangeable. `native` means `pdftotext -layout` on a born digital PDF with no model anywhere in the path, so the text was never guessed. `layout` means a layout model read the page geometry. `ocr` means a vision model read a page image.

## Licensing

The papers themselves belong to their authors and publishers. This repository holds a transcription and a translation of each one, and what it is allowed to hold depends on the licence of the source, recorded per paper in `manifests/sources.yaml`.

| access | what is published |
| --- | --- |
| `public-domain` | full text and figures |
| `open` | full text and figures |
| `permissive` | full text and figures, with attribution |
| `restricted` | the bibliographic record and a short abstract, no body text, no figures |
| `unknown` | nothing |

A paper with no access class publishes nothing, so the default of not having looked is the default of not publishing. Figures are cropped diagrams under a size cap, never whole pages.

Our own contributions, meaning the manifests, the tags, the structure, the translations and the reports, are released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). See [LICENCE](LICENCE).

If you hold rights in one of these papers and want an entry changed or removed, open an issue and it will be removed first and discussed after.

## Machine written

The transcriptions and the translations are produced by language models and checked by an audit, not by a human translator. Sections that came through a small model or a free gateway are marked as provisional in their front matter, and the reading app shows that on the page. A corpus that is mostly machine translated and does not say so is dishonest, so this one says so everywhere it can.

## Adding a paper

The hundred stay a hundred. Anything added later is a peer of them in the corpus and gets no number.

```sh
papers add --arxiv 2203.15556
papers add --doi 10.1145/3299869.3314036
papers suggest --min-citations 3
```

`papers suggest` lists works cited by three or more papers already in the corpus and not yet in it, which is a canon derived from the canon rather than from anybody's memory.
