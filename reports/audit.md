# Audit

55 rules: 48 passed, 0 failed, 7 not run

## S Sources and licensing

**S01** (hard, pass) no content file exists for a paper whose access is unknown or missing.

**S02** (hard, pass) a restricted paper has only 00_front.md, and no figures.

**S03** (hard, pass) no PDF is tracked by git, whatever the licence says.

**S04** (hard, pass) every paper in papers.yaml has an entry in sources.yaml.

**S05** (hard, pass) every fetched PDF hashes to what sources.yaml records.

**S06** (hard, pass) every open and permissive paper names a licence, not just a URL.

**S07** (hard, pass) a restricted paper quotes under 250 words.

**S08** (hard, pass) no content is longer than the PDF it claims to come from could hold.

**S09** (hard, pass) the pages that were read carry as much text as a paper's pages do.

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

## M Mathematics

**M01** (hard, pass) every math span is closed.

**M02** (hard, not run) the number sets are written with \mathbb, consistently.

**M03** (hard, pass) no character is stranded out of its TeX.

**M04** (hard, not run) every math span parses under KaTeX.

**M05** (hard, pass) no illegible marker is left in the corpus.

**M06** (soft, not run) displays per page are within 3 sigma of the paper's mean.

**M07** (hard, not run) no bracket from the prose closes inside the mathematics.

**M08** (hard, pass) no matrix is left flattened into a pair of scripts.

**M09** (soft, not run) no base carries two superscripts or two subscripts.

**M10** (hard, not run) no relation sign has lost the stroke that negates it.

**M11** (hard, pass) the mathematics is written between dollars, never \( or \[.

**M12** (soft, not run) an inline formula is written tight against its dollars.

**M13** (hard, pass) no $ inside a fenced code block opened a span.

## F Figures

**F01** (hard, pass) every figure a file references exists on disk.

**F02** (hard, pass) no figure is under 100 by 100 pixels.

**F03** (hard, pass) no figure is over 512 KB.

**F04** (hard, pass) nothing under figures/ is untracked.

**F05** (hard, pass) no paper has two figures with the same bytes.

**F06** (hard, pass) no figure covers more than 0.75 of the page it came from.

**F07** (hard, pass) every committed figure has an entry in manifests/figures.yaml with a caption.

**F08** (hard, pass) no restricted paper has a figure.

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

**G06** (hard, pass) tags climb in reading order within a run.

