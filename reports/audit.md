# Audit

98 rules: 82 passed, 11 failed, 5 not run

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

**S11** (soft, 4 found) every page of a paper published in full is in one of its files.

- `content/en/dewitt-1990-gamma` 1 page of the 38 page PDF is in no file: 38
- `content/en/graefe-1994-volcano` 1 page of the 16 page PDF is in no file: 16
- `content/en/hoare-1969-axiomatic` 1 page of the 6 page PDF is in no file: 6
- `content/en/sutherland-1963-sketchpad` 3 pages of the 149 page PDF are in no file: 8, 30, 146

## T Structure

**T01** (hard, pass) every content file parses: front matter, then body.

**T02** (hard, pass) every front matter field is known and typed.

**T03** (hard, pass) content_sha256 matches the body as it stands.

**T04** (hard, pass) section numbers within a paper are contiguous from 0.

**T05** (hard, pass) the heading tree is well formed: no level skipped.

**T06** (hard, pass) every paper has a 00_front.md with an abstract.

**T07** (hard, pass) every paper with a reference section has it as the last file.

**T08** (soft, 23 found) no section body is under 200 characters.

- `content/en/barham-2003-xen/07_acknowledgments.md` the body is 183 characters, which is a split that landed in the wrong place
- `content/en/brooks-1987-nosilverbullet/06_acknowledgments.md` the body is 191 characters, which is a split that landed in the wrong place
- `content/en/castro-1999-pbft/10_acknowledgments.md` the body is 193 characters, which is a split that landed in the wrong place
- `content/en/freund-1997-adaboost/07_acknowledgments.md` the body is 138 characters, which is a split that landed in the wrong place
- `content/en/graefe-1994-volcano/08_acknowledgments.md` the body is 107 characters, which is a split that landed in the wrong place
- `content/en/karp-1972-reducibility/06_node_cover.md` the body is 155 characters, which is a split that landed in the wrong place
- `content/en/karp-1972-reducibility/08_feedback_node_set.md` the body is 137 characters, which is a split that landed in the wrong place
- `content/en/karp-1972-reducibility/09_feedback_arc_set.md` the body is 137 characters, which is a split that landed in the wrong place
- `content/en/karp-1972-reducibility/10_directed_hamilton_circuit.md` the body is 88 characters, which is a split that landed in the wrong place
- `content/en/karp-1972-reducibility/11_undirected_hamilton_circuit.md` the body is 77 characters, which is a split that landed in the wrong place
- `content/en/karp-1972-reducibility/12_satisfiability_with_at_most_3_literals.md` the body is 189 characters, which is a split that landed in the wrong place
- `content/en/karp-1972-reducibility/13_chromatic_number.md` the body is 137 characters, which is a split that landed in the wrong place
- `content/en/karp-1972-reducibility/14_clique_cover.md` the body is 88 characters, which is a split that landed in the wrong place
- `content/en/karp-1972-reducibility/16_hitting_set.md` the body is 126 characters, which is a split that landed in the wrong place
- `content/en/karp-1972-reducibility/17_steiner_tree.md` the body is 150 characters, which is a split that landed in the wrong place
- `content/en/karp-1972-reducibility/18_3_dimensional_matching.md` the body is 156 characters, which is a split that landed in the wrong place
- `content/en/karp-1972-reducibility/19_knapsack.md` the body is 92 characters, which is a split that landed in the wrong place
- `content/en/karp-1972-reducibility/21_partition.md` the body is 160 characters, which is a split that landed in the wrong place
- `content/en/royce-1970-lifecycle/02_analysis.md` the body is 6 characters, which is a split that landed in the wrong place
- `content/en/savitch-1970-tape/02_acknowledgments.md` the body is 78 characters, which is a split that landed in the wrong place
- `content/en/stoica-2001-chord/09_acknowledgments.md` the body is 164 characters, which is a split that landed in the wrong place
- `content/en/verma-2015-borg/06_acknowledgments.md` the body is 99 characters, which is a split that landed in the wrong place
- `content/en/wu-2016-gnmt/10_acknowledgments.md` the body is 131 characters, which is a split that landed in the wrong place

**T09** (soft, 12 found) no section body is over 40,000 characters.

- `content/en/astrahan-1976-systemr/02_the_relational_data_system.md` the body is 47980 characters, which is a section that was never split
- `content/en/gal-2009-tracejit/03_trace_trees.md` the body is 62599 characters, which is a section that was never split
- `content/en/goldwasser-1985-zk/01_shafi_goldwasser_silvio_micali_and.md` the body is 51031 characters, which is a section that was never split
- `content/en/knuth-1977-kmp/00_front.md` the body is 78346 characters, which is a section that was never split
- `content/en/rabin-1959-automata/01_introduction.md` the body is 75468 characters, which is a section that was never split
- `content/en/saltzer-1975-protection/03_2_functional_levels_of_information.md` the body is 60172 characters, which is a section that was never split
- `content/en/saltzer-1975-protection/04_descriptor_based_protection_systems.md` the body is 81107 characters, which is a section that was never split
- `content/en/savitch-1970-tape/01_introduction.md` the body is 42188 characters, which is a section that was never split
- `content/en/silver-2016-alphago/02_method.md` the body is 40757 characters, which is a section that was never split
- `content/en/sussman-1975-scheme/00_front.md` the body is 45380 characters, which is a section that was never split
- `content/en/sutherland-1963-sketchpad/05_introduction.md` the body is 153702 characters, which is a section that was never split
- `content/en/turing-1936-computable/03_examples_of_computing_machines.md` the body is 59565 characters, which is a section that was never split

**T10** (hard, pass) no page furniture is left in the body: running heads, bare folios.

**T11** (hard, pass) no raw HTML markup is left in a body.

**T12** (hard, pass) no Markdown link is left in a body.

**T13** (soft, 3 found) no word is left split at the hyphen the page broke it with.

- `content/en/dennard-1974-scaling/00_front.md:6` "orschungs- und" is one word the page broke across two lines
- `content/en/dennard-1974-scaling/00_front.md:9` "orschungs- und" is one word the page broke across two lines
- `content/en/mohan-1992-aries/15_references.md:116` "multiac- tion" is one word the page broke across two lines

**T14** (hard, pass) no section file has an empty body.

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

**M12** (soft, 2 found) an inline formula is written tight against its dollars.

- `content/en/backus-1978-vonneumann/12_functional_programming_systems_fp.md:198` the formula opens with a space inside the dollars: /+:<4,5,6> = +:<4, +:<5,/+:<6>>>>
- `content/en/mccabe-1976-complexity/03_working_experience_with_the_complexity.md:32` the formula closes with a space inside the dollars: 990) LM=0 LU=NCHARS*NWORDS+LM LV=NWORDS+LU LW=NWORDS+LV LX=N...

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

**C08** (soft, 12 found) no run of lines reads as program text outside a fence.

- `content/en/astrahan-1976-systemr/02_the_relational_data_system.md:171` 6 lines here read as program text and are not in a fence
- `content/en/astrahan-1976-systemr/07_appendix_ii_sequel_syntax.md:47` 94 lines here read as program text and are not in a fence
- `content/en/brooks-1987-nosilverbullet/07_references.md:1` 13 lines here read as program text and are not in a fence
- `content/en/cytron-1991-ssa/03_static_single_assignment_form.md:140` 10 lines here read as program text and are not in a fence
- `content/en/cytron-1991-ssa/03_static_single_assignment_form.md:151` 10 lines here read as program text and are not in a fence
- `content/en/cytron-1991-ssa/07_translating_from_ssa_form.md:11` 27 lines here read as program text and are not in a fence
- `content/en/cytron-1991-ssa/07_translating_from_ssa_form.md:124` 6 lines here read as program text and are not in a fence
- `content/en/lecun-1998-lenet/09_graph_transformer_networks_and.md:38` 40 lines here read as program text and are not in a fence
- `content/en/razborov-1997-naturalproofs/05_one_property_of_formal_complexity.md:87` 3 lines here read as program text and are not in a fence
- `content/en/sussman-1975-scheme/00_front.md:562` 4 lines here read as program text and are not in a fence
- `content/en/turing-1936-computable/03_examples_of_computing_machines.md:317` 66 lines here read as program text and are not in a fence
- `content/en/wegman-1991-sccp/05_observations_on_the_constant.md:86` 9 lines here read as program text and are not in a fence

**C09** (soft, 32 found) no run of lines is lined up with spaces Markdown will collapse.

- `content/en/astrahan-1976-systemr/02_the_relational_data_system.md:238` 2 lines here are lined up with spaces that Markdown will collapse, so the columns are lost
- `content/en/astrahan-1976-systemr/02_the_relational_data_system.md:243` 2 lines here are lined up with spaces that Markdown will collapse, so the columns are lost
- `content/en/astrahan-1976-systemr/02_the_relational_data_system.md:246` 2 lines here are lined up with spaces that Markdown will collapse, so the columns are lost
- `content/en/astrahan-1976-systemr/02_the_relational_data_system.md:272` 5 lines here are lined up with spaces that Markdown will collapse, so the columns are lost
- `content/en/backus-1978-vonneumann/06_comparison_of_von_neumann_and.md:32` 2 lines here are lined up with spaces that Markdown will collapse, so the columns are lost
- `content/en/backus-1978-vonneumann/13_the_algebra_of_programs_for_fp_systems.md:79` 4 lines here are lined up with spaces that Markdown will collapse, so the columns are lost
- `content/en/backus-1978-vonneumann/13_the_algebra_of_programs_for_fp_systems.md:85` 2 lines here are lined up with spaces that Markdown will collapse, so the columns are lost
- `content/en/backus-1978-vonneumann/13_the_algebra_of_programs_for_fp_systems.md:91` 3 lines here are lined up with spaces that Markdown will collapse, so the columns are lost
- `content/en/backus-1978-vonneumann/13_the_algebra_of_programs_for_fp_systems.md:404` 2 lines here are lined up with spaces that Markdown will collapse, so the columns are lost
- `content/en/cytron-1991-ssa/07_translating_from_ssa_form.md:125` 5 lines here are lined up with spaces that Markdown will collapse, so the columns are lost
- `content/en/gal-2009-tracejit/02_overview_example_tracing_run.md:45` 17 lines here are lined up with spaces that Markdown will collapse, so the columns are lost
- `content/en/gal-2009-tracejit/02_overview_example_tracing_run.md:64` 3 lines here are lined up with spaces that Markdown will collapse, so the columns are lost
- `content/en/patterson-1981-risc/08_references.md:46` 8 lines here are lined up with spaces that Markdown will collapse, so the columns are lost
- `content/en/shannon-1948-communication/03_the_discrete_source_of_information.md:58` 4 lines here are lined up with spaces that Markdown will collapse, so the columns are lost
- `content/en/sussman-1975-scheme/00_front.md:349` 15 lines here are lined up with spaces that Markdown will collapse, so the columns are lost
- `content/en/sussman-1975-scheme/00_front.md:381` 3 lines here are lined up with spaces that Markdown will collapse, so the columns are lost
- `content/en/sussman-1975-scheme/00_front.md:385` 4 lines here are lined up with spaces that Markdown will collapse, so the columns are lost
- `content/en/sussman-1975-scheme/00_front.md:390` 4 lines here are lined up with spaces that Markdown will collapse, so the columns are lost
- `content/en/sussman-1975-scheme/00_front.md:395` 4 lines here are lined up with spaces that Markdown will collapse, so the columns are lost
- `content/en/sutherland-1963-sketchpad/03_acknowledgments.md:13` 16 lines here are lined up with spaces that Markdown will collapse, so the columns are lost
- `content/en/tomasulo-1967-algorithm/01_introduction.md:25` 3 lines here are lined up with spaces that Markdown will collapse, so the columns are lost
- `content/en/tomasulo-1967-algorithm/01_introduction.md:86` 7 lines here are lined up with spaces that Markdown will collapse, so the columns are lost
- `content/en/tomasulo-1967-algorithm/02_bb_tag_1_1010_a1.md:3` 2 lines here are lined up with spaces that Markdown will collapse, so the columns are lost
- `content/en/tomasulo-1967-algorithm/02_bb_tag_1_1010_a1.md:34` 5 lines here are lined up with spaces that Markdown will collapse, so the columns are lost
- `content/en/tomasulo-1967-algorithm/02_bb_tag_1_1010_a1.md:44` 2 lines here are lined up with spaces that Markdown will collapse, so the columns are lost
- `content/en/turing-1936-computable/03_examples_of_computing_machines.md:62` 3 lines here are lined up with spaces that Markdown will collapse, so the columns are lost
- `content/en/turing-1936-computable/03_examples_of_computing_machines.md:70` 2 lines here are lined up with spaces that Markdown will collapse, so the columns are lost
- `content/en/turing-1936-computable/03_examples_of_computing_machines.md:76` 2 lines here are lined up with spaces that Markdown will collapse, so the columns are lost
- `content/en/turing-1936-computable/03_examples_of_computing_machines.md:82` 8 lines here are lined up with spaces that Markdown will collapse, so the columns are lost
- `content/en/turing-1936-computable/03_examples_of_computing_machines.md:328` 2 lines here are lined up with spaces that Markdown will collapse, so the columns are lost
- `content/en/turing-1936-computable/03_examples_of_computing_machines.md:337` 2 lines here are lined up with spaces that Markdown will collapse, so the columns are lost
- `content/en/turing-1936-computable/03_examples_of_computing_machines.md:392` 4 lines here are lined up with spaces that Markdown will collapse, so the columns are lost

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

**F09** (soft, 27 found) every figure the paper numbers in its prose is present.

- `manifests/figures.yaml` bloom-1970-filter mentions Figure 1 in its prose and has no such figure
- `manifests/figures.yaml` aho-1975-corasick mentions Figure 3 in its prose and has no such figure
- `manifests/figures.yaml` knuth-1977-kmp mentions Figure 1 in its prose and has no such figure
- `manifests/figures.yaml` brin-1998-pagerank mentions Figure 1 in its prose and has no such figure
- `manifests/figures.yaml` cytron-1991-ssa mentions Figure 4 in its prose and has no such figure
- `manifests/figures.yaml` cytron-1991-ssa mentions Figure 12 in its prose and has no such figure
- `manifests/figures.yaml` gal-2009-tracejit mentions Figure 6 in its prose and has no such figure
- `manifests/figures.yaml` denning-1968-workingset mentions Figure 6 in its prose and has no such figure
- `manifests/figures.yaml` denning-1968-workingset mentions Figure 7 in its prose and has no such figure
- `manifests/figures.yaml` ghemawat-2003-gfs mentions Figure 1 in its prose and has no such figure
- `manifests/figures.yaml` cerf-1974-tcpip mentions Figure 3 in its prose and has no such figure
- `manifests/figures.yaml` dennard-1974-scaling mentions Figure 7 in its prose and has no such figure
- `manifests/figures.yaml` patterson-1981-risc mentions Figure 6 in its prose and has no such figure
- `manifests/figures.yaml` krizhevsky-2012-imagenet mentions Figure 3 in its prose and has no such figure
- `manifests/figures.yaml` sutherland-1963-sketchpad mentions Figure 1.5A in its prose and has no such figure
- `manifests/figures.yaml` sutherland-1963-sketchpad mentions Figure 1.5D in its prose and has no such figure
- `manifests/figures.yaml` sutherland-1963-sketchpad mentions Figure 1.5F in its prose and has no such figure
- `manifests/figures.yaml` sutherland-1963-sketchpad mentions Figure 1.5G in its prose and has no such figure
- `manifests/figures.yaml` sutherland-1963-sketchpad mentions Figure 1.5H in its prose and has no such figure
- `manifests/figures.yaml` sutherland-1963-sketchpad mentions Figure 7.1A in its prose and has no such figure
- `manifests/figures.yaml` sutherland-1963-sketchpad mentions Figure 7.1B in its prose and has no such figure
- `manifests/figures.yaml` sutherland-1963-sketchpad mentions Figure 7.1C in its prose and has no such figure
- `manifests/figures.yaml` sutherland-1963-sketchpad mentions Figure 7.1D in its prose and has no such figure
- `manifests/figures.yaml` sutherland-1963-sketchpad mentions Figure 9.4B in its prose and has no such figure
- `manifests/figures.yaml` engelbart-1968-augmenting mentions Figure 7 in its prose and has no such figure
- `manifests/figures.yaml` engelbart-1968-augmenting mentions Figure 8 in its prose and has no such figure
- `manifests/figures.yaml` shneiderman-1983-directmanipulation mentions Figure 2 in its prose and has no such figure

## R References

**R01** (hard, pass) every [[id]] in a body names a paper in papers.yaml.

**R02** (hard, pass) every in-text [n] has an entry n in that paper's bibliography.

**R03** (hard, pass) every reference keeps the text the paper printed.

**R04** (soft, pass) every resolves_to passes the verified matcher again.

**R05** (hard, pass) no resolves_to points at the citing paper itself.

**R06** (soft, pass) the citation graph has no cycle among papers more than two years apart.

**R07** (soft, 6 found) a paper three or more corpus papers cite is in the corpus.

- `manifests/papers.yaml` "Improving neural networks by preventing co-adaptation of feature detectors" is cited by goodfellow-2014-gan, he-2016-resnet, krizhevsky-2012-imagenet and is not in the corpus
- `manifests/papers.yaml` "Edinburgh’s phrase-based machine translation systems for wmt-14" is cited by brown-2020-gpt3, sutskever-2014-seq2seq, wu-2016-gnmt and is not in the corpus
- `manifests/papers.yaml` "Handwritten digit recognition with a back-propagation network" is cited by cortes-1995-svm, krizhevsky-2012-imagenet, lecun-1998-lenet and is not in the corpus
- `manifests/papers.yaml` "Learning long-term dependencies with gradient descent is difficult" is cited by he-2016-resnet, hochreiter-1997-lstm, lecun-1998-lenet, sutskever-2014-seq2seq and is not in the corpus
- `manifests/papers.yaml` "Learning multiple layers of features from tiny images" is cited by goodfellow-2014-gan, he-2016-resnet, krizhevsky-2012-imagenet and is not in the corpus
- `manifests/papers.yaml` "Notes on Database Operating Systems" is cited by dewitt-1990-gamma, mohan-1992-aries, saltzer-1984-endtoend and is not in the corpus

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

**L20** (soft, 131 found) every translation answers the English as it now stands.

- `content/ja/amdahl-1967-law/00_front.md` this answers content/en/amdahl-1967-law/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/ja/backus-1978-vonneumann/00_front.md` this answers content/en/backus-1978-vonneumann/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/ja/birrell-1984-rpc/00_front.md` this answers content/en/birrell-1984-rpc/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/ja/bloom-1970-filter/00_front.md` this answers content/en/bloom-1970-filter/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/ja/cooley-1965-fft/00_front.md` this answers content/en/cooley-1965-fft/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/ja/cytron-1991-ssa/00_front.md` this answers content/en/cytron-1991-ssa/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/ja/denning-1968-workingset/00_front.md` this answers content/en/denning-1968-workingset/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/ja/dijkstra-1959-shortestpath/00_front.md` this answers content/en/dijkstra-1959-shortestpath/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/ja/dijkstra-1968-the/00_front.md` this answers content/en/dijkstra-1968-the/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/ja/floyd-1962-shortestpath/00_front.md` this answers content/en/floyd-1962-shortestpath/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/ja/ford-1956-maxflow/00_front.md` this answers content/en/ford-1956-maxflow/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/ja/goldwasser-1985-zk/00_front.md` this answers content/en/goldwasser-1985-zk/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/ja/goodfellow-2014-gan/00_front.md` this answers content/en/goodfellow-2014-gan/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/ja/goodfellow-2014-gan/05_experiments.md` this answers content/en/goodfellow-2014-gan/05_experiments.md as it was and that file has been written again since, so it needs translating again
- `content/ja/hoare-1962-quicksort/00_front.md` this answers content/en/hoare-1962-quicksort/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/ja/karp-1972-reducibility/00_front.md` this answers content/en/karp-1972-reducibility/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/ja/knuth-1977-kmp/00_front.md` this answers content/en/knuth-1977-kmp/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/ja/lamport-1998-paxos/00_front.md` this answers content/en/lamport-1998-paxos/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/ja/mccarthy-1960-lisp/00_front.md` this answers content/en/mccarthy-1960-lisp/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/ja/razborov-1997-naturalproofs/00_front.md` this answers content/en/razborov-1997-naturalproofs/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/ja/shneiderman-1983-directmanipulation/00_front.md` this answers content/en/shneiderman-1983-directmanipulation/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/ja/sussman-1975-scheme/00_front.md` this answers content/en/sussman-1975-scheme/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/ja/tarjan-1972-dfs/00_front.md` this answers content/en/tarjan-1972-dfs/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/ja/turing-1936-computable/00_front.md` this answers content/en/turing-1936-computable/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/ja/wegman-1991-sccp/00_front.md` this answers content/en/wegman-1991-sccp/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/backus-1978-vonneumann/00_front.md` this answers content/en/backus-1978-vonneumann/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/barham-2003-xen/00_front.md` this answers content/en/barham-2003-xen/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/bayer-1972-btree/00_front.md` this answers content/en/bayer-1972-btree/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/birrell-1984-rpc/00_front.md` this answers content/en/birrell-1984-rpc/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/bloom-1970-filter/00_front.md` this answers content/en/bloom-1970-filter/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/bosshart-2014-p4/00_front.md` this answers content/en/bosshart-2014-p4/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/bosshart-2014-p4/04_p4_language_by_example.md` this answers content/en/bosshart-2014-p4/04_p4_language_by_example.md as it was and that file has been written again since, so it needs translating again
- `content/vi/brin-1998-pagerank/00_front.md` this answers content/en/brin-1998-pagerank/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/brooks-1987-nosilverbullet/00_front.md` this answers content/en/brooks-1987-nosilverbullet/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/castro-1999-pbft/00_front.md` this answers content/en/castro-1999-pbft/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/cerf-1974-tcpip/00_front.md` this answers content/en/cerf-1974-tcpip/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/chiu-1989-aimd/00_front.md` this answers content/en/chiu-1989-aimd/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/cook-1971-np/00_front.md` this answers content/en/cook-1971-np/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/cooley-1965-fft/00_front.md` this answers content/en/cooley-1965-fft/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/cortes-1995-svm/00_front.md` this answers content/en/cortes-1995-svm/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/cytron-1991-ssa/00_front.md` this answers content/en/cytron-1991-ssa/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/dageville-2016-snowflake/00_front.md` this answers content/en/dageville-2016-snowflake/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/decandia-2007-dynamo/00_front.md` this answers content/en/decandia-2007-dynamo/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/dennard-1974-scaling/00_front.md` this answers content/en/dennard-1974-scaling/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/denning-1968-workingset/00_front.md` this answers content/en/denning-1968-workingset/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/dewitt-1990-gamma/00_front.md` this answers content/en/dewitt-1990-gamma/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/dewitt-1990-gamma/01_introduction.md` this answers content/en/dewitt-1990-gamma/01_introduction.md as it was and that file has been written again since, so it needs translating again
- `content/vi/dewitt-1990-gamma/02_hardware_architecture_of_gamma.md` this answers content/en/dewitt-1990-gamma/02_hardware_architecture_of_gamma.md as it was and that file has been written again since, so it needs translating again
- `content/vi/dewitt-1990-gamma/03_software_architecture_of_gamma.md` this answers content/en/dewitt-1990-gamma/03_software_architecture_of_gamma.md as it was and that file has been written again since, so it needs translating again
- `content/vi/dewitt-1990-gamma/04_query_processing_algorithms.md` this answers content/en/dewitt-1990-gamma/04_query_processing_algorithms.md as it was and that file has been written again since, so it needs translating again
- `content/vi/dewitt-1990-gamma/05_transaction_and_failure_management.md` this answers content/en/dewitt-1990-gamma/05_transaction_and_failure_management.md as it was and that file has been written again since, so it needs translating again
- `content/vi/dewitt-1990-gamma/06_performance_studies.md` this answers content/en/dewitt-1990-gamma/06_performance_studies.md as it was and that file has been written again since, so it needs translating again
- `content/vi/dewitt-1990-gamma/07_conclusions_and_future_research.md` this answers content/en/dewitt-1990-gamma/07_conclusions_and_future_research.md as it was and that file has been written again since, so it needs translating again
- `content/vi/dewitt-1990-gamma/09_references.md` this answers content/en/dewitt-1990-gamma/09_references.md as it was and that file has been written again since, so it needs translating again
- `content/vi/diffie-1976-newdirections/00_front.md` this answers content/en/diffie-1976-newdirections/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/dijkstra-1959-shortestpath/00_front.md` this answers content/en/dijkstra-1959-shortestpath/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/dijkstra-1968-the/00_front.md` this answers content/en/dijkstra-1968-the/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/engelbart-1968-augmenting/00_front.md` this answers content/en/engelbart-1968-augmenting/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/floyd-1962-shortestpath/00_front.md` this answers content/en/floyd-1962-shortestpath/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/ford-1956-maxflow/00_front.md` this answers content/en/ford-1956-maxflow/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/freund-1997-adaboost/00_front.md` this answers content/en/freund-1997-adaboost/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/gal-2009-tracejit/00_front.md` this answers content/en/gal-2009-tracejit/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/ghemawat-2003-gfs/00_front.md` this answers content/en/ghemawat-2003-gfs/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/goldwasser-1985-zk/00_front.md` this answers content/en/goldwasser-1985-zk/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/goodfellow-2014-gan/05_experiments.md` this answers content/en/goodfellow-2014-gan/05_experiments.md as it was and that file has been written again since, so it needs translating again
- `content/vi/graefe-1994-volcano/00_front.md` this answers content/en/graefe-1994-volcano/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/hamming-1950-codes/00_front.md` this answers content/en/hamming-1950-codes/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/hoare-1962-quicksort/00_front.md` this answers content/en/hoare-1962-quicksort/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/jacobson-1988-congestion/00_front.md` this answers content/en/jacobson-1988-congestion/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/jouppi-1990-victimcache/00_front.md` this answers content/en/jouppi-1990-victimcache/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/jouppi-2017-tpu/00_front.md` this answers content/en/jouppi-2017-tpu/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/karp-1972-reducibility/00_front.md` this answers content/en/karp-1972-reducibility/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/knuth-1977-kmp/00_front.md` this answers content/en/knuth-1977-kmp/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/lamport-1998-paxos/00_front.md` this answers content/en/lamport-1998-paxos/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/lattner-2004-llvm/00_front.md` this answers content/en/lattner-2004-llvm/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/lecun-1998-lenet/00_front.md` this answers content/en/lecun-1998-lenet/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/mccabe-1976-complexity/00_front.md` this answers content/en/mccabe-1976-complexity/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/mccarthy-1960-lisp/00_front.md` this answers content/en/mccarthy-1960-lisp/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/mckeown-2008-openflow/00_front.md` this answers content/en/mckeown-2008-openflow/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/metcalfe-1976-ethernet/00_front.md` this answers content/en/metcalfe-1976-ethernet/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/metcalfe-1976-ethernet/01_background.md` this answers content/en/metcalfe-1976-ethernet/01_background.md as it was and that file has been written again since, so it needs translating again
- `content/vi/metcalfe-1976-ethernet/02_system_summary.md` this answers content/en/metcalfe-1976-ethernet/02_system_summary.md as it was and that file has been written again since, so it needs translating again
- `content/vi/metcalfe-1976-ethernet/03_design_principles.md` this answers content/en/metcalfe-1976-ethernet/03_design_principles.md as it was and that file has been written again since, so it needs translating again
- `content/vi/metcalfe-1976-ethernet/04_implementation.md` this answers content/en/metcalfe-1976-ethernet/04_implementation.md as it was and that file has been written again since, so it needs translating again
- `content/vi/metcalfe-1976-ethernet/05_growth.md` this answers content/en/metcalfe-1976-ethernet/05_growth.md as it was and that file has been written again since, so it needs translating again
- `content/vi/metcalfe-1976-ethernet/06_performance.md` this answers content/en/metcalfe-1976-ethernet/06_performance.md as it was and that file has been written again since, so it needs translating again
- `content/vi/metcalfe-1976-ethernet/07_protocol.md` this answers content/en/metcalfe-1976-ethernet/07_protocol.md as it was and that file has been written again since, so it needs translating again
- `content/vi/metcalfe-1976-ethernet/08_conclusion.md` this answers content/en/metcalfe-1976-ethernet/08_conclusion.md as it was and that file has been written again since, so it needs translating again
- `content/vi/milner-1978-polymorphism/00_front.md` this answers content/en/milner-1978-polymorphism/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/mohan-1992-aries/00_front.md` this answers content/en/mohan-1992-aries/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/nagle-1984-congestion/00_front.md` this answers content/en/nagle-1984-congestion/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/ongaro-2014-raft/00_front.md` this answers content/en/ongaro-2014-raft/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/razborov-1997-naturalproofs/00_front.md` this answers content/en/razborov-1997-naturalproofs/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/royce-1970-lifecycle/00_front.md` this answers content/en/royce-1970-lifecycle/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/rumelhart-1986-backprop/00_front.md` this answers content/en/rumelhart-1986-backprop/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/saltzer-1975-protection/00_front.md` this answers content/en/saltzer-1975-protection/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/shannon-1948-communication/00_front.md` this answers content/en/shannon-1948-communication/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/shneiderman-1983-directmanipulation/00_front.md` this answers content/en/shneiderman-1983-directmanipulation/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/stoica-2001-chord/00_front.md` this answers content/en/stoica-2001-chord/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/sussman-1975-scheme/00_front.md` this answers content/en/sussman-1975-scheme/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/sutherland-1963-sketchpad/00_front.md` this answers content/en/sutherland-1963-sketchpad/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/tarjan-1972-dfs/00_front.md` this answers content/en/tarjan-1972-dfs/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/turing-1936-computable/00_front.md` this answers content/en/turing-1936-computable/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/turing-1950-intelligence/00_front.md` this answers content/en/turing-1950-intelligence/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/verma-2015-borg/00_front.md` this answers content/en/verma-2015-borg/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/wegman-1991-sccp/00_front.md` this answers content/en/wegman-1991-sccp/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/vi/yeh-1991-branchprediction/00_front.md` this answers content/en/yeh-1991-branchprediction/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/zh/amdahl-1967-law/00_front.md` this answers content/en/amdahl-1967-law/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/zh/backus-1978-vonneumann/00_front.md` this answers content/en/backus-1978-vonneumann/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/zh/birrell-1984-rpc/00_front.md` this answers content/en/birrell-1984-rpc/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/zh/bloom-1970-filter/00_front.md` this answers content/en/bloom-1970-filter/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/zh/cooley-1965-fft/00_front.md` this answers content/en/cooley-1965-fft/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/zh/denning-1968-workingset/00_front.md` this answers content/en/denning-1968-workingset/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/zh/dijkstra-1959-shortestpath/00_front.md` this answers content/en/dijkstra-1959-shortestpath/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/zh/dijkstra-1968-the/00_front.md` this answers content/en/dijkstra-1968-the/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/zh/floyd-1962-shortestpath/00_front.md` this answers content/en/floyd-1962-shortestpath/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/zh/ford-1956-maxflow/00_front.md` this answers content/en/ford-1956-maxflow/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/zh/goldwasser-1985-zk/00_front.md` this answers content/en/goldwasser-1985-zk/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/zh/goodfellow-2014-gan/00_front.md` this answers content/en/goodfellow-2014-gan/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/zh/goodfellow-2014-gan/05_experiments.md` this answers content/en/goodfellow-2014-gan/05_experiments.md as it was and that file has been written again since, so it needs translating again
- `content/zh/hamming-1950-codes/00_front.md` this answers content/en/hamming-1950-codes/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/zh/hoare-1962-quicksort/00_front.md` this answers content/en/hoare-1962-quicksort/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/zh/karp-1972-reducibility/00_front.md` this answers content/en/karp-1972-reducibility/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/zh/lamport-1998-paxos/00_front.md` this answers content/en/lamport-1998-paxos/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/zh/mccarthy-1960-lisp/00_front.md` this answers content/en/mccarthy-1960-lisp/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/zh/razborov-1997-naturalproofs/00_front.md` this answers content/en/razborov-1997-naturalproofs/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/zh/shneiderman-1983-directmanipulation/00_front.md` this answers content/en/shneiderman-1983-directmanipulation/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/zh/sussman-1975-scheme/00_front.md` this answers content/en/sussman-1975-scheme/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/zh/tarjan-1972-dfs/00_front.md` this answers content/en/tarjan-1972-dfs/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/zh/turing-1936-computable/00_front.md` this answers content/en/turing-1936-computable/00_front.md as it was and that file has been written again since, so it needs translating again
- `content/zh/wegman-1991-sccp/00_front.md` this answers content/en/wegman-1991-sccp/00_front.md as it was and that file has been written again since, so it needs translating again

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

