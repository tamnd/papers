# Audit

14 rules: 11 passed, 0 failed, 3 not run

## S Sources and licensing

**S01** (hard, pass) no content file exists for a paper whose access is unknown or missing.

**S02** (hard, pass) a restricted paper has only 00_front.md, and no figures.

**S03** (hard, pass) no PDF is tracked by git, whatever the licence says.

**S04** (hard, pass) every paper in papers.yaml has an entry in sources.yaml.

**S06** (hard, pass) every open and permissive paper names a licence, not just a URL.

## R References

**R01** (hard, pass) every [[id]] in a body names a paper in papers.yaml.

**R02** (hard, pass) every in-text [n] has an entry n in that paper's bibliography.

**R03** (hard, pass) every reference keeps the text the paper printed.

**R04** (soft, pass) every resolves_to passes the verified matcher again.

**R05** (hard, pass) no resolves_to points at the citing paper itself.

**R08** (hard, pass) a reference section renders the printed text and not only the parsed fields.

## G Tags

**G01** (hard, not run) every tag in tags/tags is four hex characters, and every line is tag,anchor.

**G02** (hard, not run) no tag appears twice.

**G03** (hard, not run) no anchor appears twice.

