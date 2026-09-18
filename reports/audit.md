# Audit

96 rules: 88 passed, 3 failed, 5 not run

## S Sources and licensing

**S01** (hard, not run) no content file exists for a paper whose access is unknown or missing.

**S02** (hard, not run) a restricted paper has only 00_front.md, and no figures.

**S03** (hard, pass) no PDF and no EPUB is tracked by git, whatever the licence says.

**S04** (hard, pass) every paper in papers.yaml has an entry in sources.yaml.

**S05** (hard, pass) every fetched PDF hashes to what sources.yaml records.

**S06** (hard, pass) every open and permissive paper names a licence, not just a URL.

**S07** (hard, not run) a restricted paper quotes under 250 words.

**S08** (hard, pass) no content is longer than the PDF it claims to come from could hold.

**S09** (hard, pass) the pages that were read carry as much text as a paper's pages do.

**S10** (hard, not run) the quotation published from a restricted paper is from that paper.

## T Structure

**T01** (hard, pass) every content file parses: front matter, then body.

**T02** (hard, pass) every front matter field is known and typed.

**T03** (hard, pass) content_sha256 matches the body as it stands.

**T04** (hard, pass) section numbers within a paper are contiguous from 0.

**T05** (hard, pass) the heading tree is well formed: no level skipped.

**T06** (hard, pass) every paper has a 00_front.md with an abstract.

**T07** (hard, pass) every paper with a reference section has it as the last file.

**T08** (soft, pass) no section body is under 200 characters.

**T09** (soft, pass) no section body is over 40,000 characters.

**T10** (hard, pass) no page furniture is left in the body: running heads, bare folios.

**T11** (hard, pass) no raw HTML markup is left in a body.

**T12** (hard, pass) no Markdown link is left in a body.

**T13** (soft, pass) no word is left split at the hyphen the page broke it with.

## M Mathematics

**M01** (hard, pass) every math span is closed.

**M02** (hard, pass) the number sets are written with \mathbb, consistently.

**M03** (hard, pass) no character is stranded out of its TeX.

**M04** (hard, pass) every math span parses under KaTeX.

**M05** (hard, pass) no illegible marker is left in the corpus.

**M06** (soft, pass) displays per page are within 3 sigma of the paper's mean.

**M07** (hard, pass) no bracket from the prose closes inside the mathematics.

**M08** (hard, pass) no matrix is left flattened into a pair of scripts.

**M09** (soft, pass) no base carries two superscripts or two subscripts.

**M10** (hard, pass) no relation sign has lost the stroke that negates it.

**M11** (hard, pass) the mathematics is written between dollars, never \( or \[.

**M12** (soft, pass) an inline formula is written tight against its dollars.

**M13** (hard, pass) no $ inside a fenced code block opened a span.

**M14** (hard, pass) a paper with mathematics in its prose has mathematics in its markup.

## C Code

**C01** (hard, pass) every fence is closed.

**C02** (hard, pass) every fence carries a language tag from the known list.

**C03** (hard, pass) no fence is nested inside another.

**C04** (hard, pass) no fence opens inside a math span.

**C05** (soft, pass) no listing runs past 120 lines.

**C06** (hard, pass) a numbered listing carries an attribute block with a .code class.

**C07** (hard, pass) the fenced regions of a translation are its English ones, byte for byte.

**C08** (soft, 1 found) no run of lines reads as program text outside a fence.

- `content/en/razborov-1997-naturalproofs/05_one_property_of_formal_complexity.md:73` 3 lines here read as program text and are not in a fence

**C09** (soft, pass) no run of lines is lined up with spaces Markdown will collapse.

**C10** (hard, pass) no run of backticks has a sentence after it on the same line.

## F Figures

**F01** (hard, pass) every figure a file references exists on disk.

**F02** (hard, pass) no figure is under 100 by 100 pixels.

**F03** (hard, pass) no figure is over 512 KB.

**F04** (hard, pass) nothing under figures/ is untracked.

**F05** (hard, pass) no paper has two figures with the same bytes.

**F06** (hard, pass) no figure covers more than 0.75 of the page it came from.

**F07** (hard, pass) every committed figure has an entry in manifests/figures.yaml with a caption.

**F08** (hard, not run) no restricted paper has a figure.

**F09** (soft, pass) every figure the paper numbers in its prose is present.

## R References

**R01** (hard, pass) every [[id]] in a body names a paper in papers.yaml.

**R02** (hard, pass) every in-text [n] has an entry n in that paper's bibliography.

**R03** (hard, pass) every reference keeps the text the paper printed.

**R04** (soft, pass) every resolves_to passes the verified matcher again.

**R05** (hard, pass) no resolves_to points at the citing paper itself.

**R06** (soft, pass) the citation graph has no cycle among papers more than two years apart.

**R07** (soft, pass) a paper three or more corpus papers cite is in the corpus.

**R08** (hard, pass) a reference section renders the printed text and not only the parsed fields.

## G Tags

**G01** (hard, pass) every tag in tags/tags is four hex characters, and every line is tag,anchor.

**G02** (hard, pass) no tag appears twice.

**G03** (hard, pass) no anchor appears twice.

**G04** (hard, pass) every tag in a body is in tags/tags against that anchor.

**G05** (hard, pass) every anchored item in a body carries a tag.

## L Translation

**L01** (hard, pass) the mathematics of a translation is the mathematics of its English.

**L02** (hard, pass) the attribute blocks of a translation are its English ones.

**L03** (hard, pass) the heading tree of a translation is its English one.

**L04** (hard, pass) every translated file is a file of the English paper, with the same number and kind.

**L05** (hard, pass) every translation records the English file and the hash it was made from.

**L06** (soft, pass) a glossary term used in the English is rendered the glossary's way in the translation.

**L07** (hard, pass) no paragraph came back in English.

**L08** (soft, pass) no translation was written by a small model.

**L09** (hard, pass) two files under one glossary version were translated against the same renderings.

**L10** (hard, pass) no English glossary term is left standing in a translation with its rendering nowhere in the file.

**L11** (hard, pass) no sentence came back in English.

**L12** (hard, pass) the words set inside the mathematics are translated too.

**L13** (hard, pass) no word of a translation is written in a script that language does not use.

**L14** (hard, pass) a bibliography stands as printed in every language.

**L15** (soft, pass) no translation was written on a free gateway.

**L16** (hard, pass) the citations of a translation are its English ones.

**L17** (hard, pass) no translation is a provider's error message or an apology.

**L18** (hard, pass) the listings of a translation are its English ones, byte for byte.

**L19** (soft, pass) the section title of a translation was translated too.

**L20** (soft, 14 found) every translation answers the English as it now stands.

- `content/ja/amdahl-1967-law/00_front.md` this answers content/en/amdahl-1967-law/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/ja/dijkstra-1968-the/00_front.md` this answers content/en/dijkstra-1968-the/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/ja/floyd-1962-shortestpath/00_front.md` this answers content/en/floyd-1962-shortestpath/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/ja/goodfellow-2014-gan/00_front.md` this answers content/en/goodfellow-2014-gan/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/ja/mccarthy-1960-lisp/00_front.md` this answers content/en/mccarthy-1960-lisp/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/ja/razborov-1997-naturalproofs/00_front.md` this answers content/en/razborov-1997-naturalproofs/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/lecun-1998-lenet/00_front.md` this answers content/en/lecun-1998-lenet/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/razborov-1997-naturalproofs/00_front.md` this answers content/en/razborov-1997-naturalproofs/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/zh/amdahl-1967-law/00_front.md` this answers content/en/amdahl-1967-law/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/zh/dijkstra-1968-the/00_front.md` this answers content/en/dijkstra-1968-the/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/zh/floyd-1962-shortestpath/00_front.md` this answers content/en/floyd-1962-shortestpath/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/zh/goodfellow-2014-gan/00_front.md` this answers content/en/goodfellow-2014-gan/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/zh/mccarthy-1960-lisp/00_front.md` this answers content/en/mccarthy-1960-lisp/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/zh/razborov-1997-naturalproofs/00_front.md` this answers content/en/razborov-1997-naturalproofs/00_front.md as it was and that file has been written again since, so it needs translating again

**L21** (soft, 7 found) no translation is left carrying a materially different verdict.

- `content/ja/goodfellow-2014-gan/02_related_work.md` the back translation of this came away believing something the English does not say, so it needs translating again
- `content/ja/goodfellow-2014-gan/03_adversarial_nets.md` the back translation of this came away believing something the English does not say, so it needs translating again
- `content/ja/goodfellow-2014-gan/04_theoretical_results.md` the back translation of this came away believing something the English does not say, so it needs translating again
- `content/ja/goodfellow-2014-gan/05_experiments.md` the back translation of this came away believing something the English does not say, so it needs translating again
- `content/zh/goodfellow-2014-gan/01_introduction.md` the back translation of this came away believing something the English does not say, so it needs translating again
- `content/zh/goodfellow-2014-gan/04_theoretical_results.md` the back translation of this came away believing something the English does not say, so it needs translating again
- `content/zh/goodfellow-2014-gan/08_acknowledgments.md` the back translation of this came away believing something the English does not say, so it needs translating again

## P Publication

**P01** (hard, pass) every block of every page renders, and its HTML is on the allowlist.

**P02** (hard, pass) every link a page carries has something at the other end.

**P03** (hard, pass) every figure a page shows is in the build.

**P04** (soft, pass) a language under the glossary coverage floor is emitted as a draft.

**P05** (hard, pass) the emitted JSON validates against schema/site.schema.json.

**P06** (hard, pass) every search result leads to a block that is in the build.

