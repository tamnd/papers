# Usage

What the corpus cost in machine time, by stage.

This is read from the ledger, which is one line per ask and lives at `~/.config/papers/ledger.jsonl` on the machine that did the work. The ledger is not in this repository and will not be: it names the hosts that were asked. Nothing below names a host.

1,449 asks, 1,297 of them answered and 7 refused before the model read the question. 13,494,811 tokens in, 1,178,788 out, 34h 41m of waiting over 734 targets, from 2026-09-12 to 2026-09-18.

## Pages read

Counted off the committed English content, one page counted once per paper however many sections were cut from it. `native` is pdftotext on a born digital file with no model anywhere in the path, so those pages were never guessed. `layout` is a layout model reading the page geometry and `ocr` is a vision model reading a page image, and only those two cost anything in the tables below.

| path | papers | pages | what read them |
| --- | --: | --: | --- |
| native | 3 | 8 | pdftotext version 24.02.0, pdftotext version 26.09.0 |
| vision | 95 | 408 | gpt-5, gpt-6-astra, olmOCR-2-7B-1025-FP8 |

## Per stage

A target is the thing one ask was about: a page for the extract stage, a section for translate. Asks are higher than targets when a host did not answer and the question went to the next one.

| stage | asks | answered | refused | targets | tokens in | tokens out | time | cost |
| --- | --: | --: | --: | --: | --: | --: | --: | --: |
| extract | 847 | 769 | 4 | 455 | 9,326,157 | 920,309 | 14h 39m | $0.00 |
| figures | 0 | 0 | 0 | 0 | 0 | 0 | 0s | - |
| refs | 0 | 0 | 0 | 0 | 0 | 0 | 0s | - |
| glossary | 17 | 14 | 0 | 14 | 15,789 | 2,036 | 34m 18s | $0.00 |
| translate | 395 | 326 | 3 | 79 | 1,866,842 | 211,305 | 18h 12m | - |
| roundtrip | 190 | 188 | 0 | 186 | 2,286,023 | 45,138 | 1h 15m | - |

41 of the 1,449 asks went to a model with no price set, so the money column is a dash for them. A price is dollars per million tokens by model, and the table is `manifests/prices.json`. A model that is missing from it is a model nobody has looked the rate up for, which is not the same thing as a model that costs nothing, so it gets a dash rather than a zero.

## Per model

| model | asks | tokens in | tokens out | cost |
| --- | --: | --: | --: | --: |
| not recorded | 152 | 0 | 0 | $0.00 |
| gpt-5-6 | 381 | 980,586 | 232,862 | $0.00 |
| gpt-5-6-mini | 41 | 139,688 | 36,470 | - |
| gpt-6-astra | 218 | 3,795,402 | 114,273 | $0.00 |
| reader-a | 657 | 8,579,135 | 795,183 | $0.00 |

What the rates are:

- gpt-5-6: reached through a ChatGPT subscription, which is billed by the month and not by the token
- gpt-6-astra: reached through a Codex subscription, which is billed by the month and not by the token
- reader-a: an olmOCR build served from a GPU in this house, so a page costs electricity and no tokens

## Per paper

In id order rather than in order of cost, so that two of these reports can be read side by side.

| paper | stage | targets | tokens in | tokens out | time |
| --- | --- | --: | --: | --: | --: |
| aho-1975-corasick | extract | 3 | 35,820 | 3,245 | 51.2s |
| amdahl-1967-law | translate | 3 | 17,130 | 1,290 | 12m 39s |
| astrahan-1976-systemr | extract | 3 | 26,076 | 1,372 | 22.2s |
| astrahan-1976-systemr | translate | 1 | 3,014 | 329 | 1m 0s |
| backus-1978-vonneumann | extract | 3 | 35,820 | 2,975 | 48.9s |
| barham-2003-xen | extract | 3 | 38,034 | 3,911 | 1m 27s |
| barham-2003-xen | translate | 1 | 3,247 | 474 | 3m 26s |
| bayer-1972-btree | extract | 3 | 24,108 | 690 | 12.5s |
| birrell-1984-rpc | extract | 3 | 58,036 | 3,039 | 52.0s |
| birrell-1984-rpc | translate | 1 | 3,096 | 407 | 2m 27s |
| bloom-1970-filter | extract | 3 | 35,820 | 3,734 | 56.2s |
| boncz-2005-x100 | extract | 3 | 76,428 | 5,506 | 13m 14s |
| boncz-2005-x100 | translate | 1 | 17,876 | 344 | 16.7s |
| bosshart-2014-p4 | extract | 8 | 146,097 | 10,935 | 16m 0s |
| bosshart-2014-p4 | translate | 3 | 86,677 | 13,809 | 27m 57s |
| brin-1998-pagerank | extract | 3 | 31,178 | 2,420 | 47.6s |
| brin-1998-pagerank | translate | 1 | 18,015 | 460 | 22.3s |
| brooks-1987-nosilverbullet | extract | 6 | 40,019 | 1,664 | 6m 54s |
| brown-2020-gpt3 | extract | 75 | 1,459,382 | 199,584 | 2h 10m |
| castro-1999-pbft | extract | 3 | 56,214 | 4,204 | 10m 40s |
| cerf-1974-tcpip | extract | 3 | 36,981 | 2,415 | 37.6s |
| chang-2006-bigtable | extract | 3 | 38,034 | 2,610 | 5m 49s |
| chang-2006-bigtable | translate | 1 | 2,932 | 292 | 4m 16s |
| chiu-1989-aimd | extract | 3 | 48,120 | 2,466 | 5m 28s |
| chiu-1989-aimd | translate | 1 | 9,690 | 1,295 | 26m 47s |
| codd-1970-relational | extract | 5 | 247,145 | 27,022 | 12m 9s |
| content/ja/goodfellow-2014-gan/00_front.md | roundtrip | 2 | 2,138 | 350 | 3m 36s |
| content/ja/goodfellow-2014-gan/01_introduction.md | roundtrip | 2 | 2,965 | 851 | 1m 43s |
| content/ja/goodfellow-2014-gan/02_related_work.md | roundtrip | 2 | 3,298 | 1,084 | 1m 32s |
| content/ja/goodfellow-2014-gan/03_adversarial_nets.md | roundtrip | 2 | 3,598 | 938 | 9m 4s |
| content/ja/goodfellow-2014-gan/04_theoretical_results.md | roundtrip | 2 | 6,077 | 2,080 | 4m 21s |
| content/ja/goodfellow-2014-gan/05_experiments.md | roundtrip | 2 | 4,332 | 1,300 | 1m 22s |
| content/ja/goodfellow-2014-gan/06_advantages_and_disadvantages.md | roundtrip | 2 | 2,224 | 396 | 1m 10s |
| content/ja/goodfellow-2014-gan/07_conclusions_and_future_work.md | roundtrip | 2 | 2,111 | 342 | 1m 4s |
| content/ja/goodfellow-2014-gan/08_acknowledgments.md | roundtrip | 2 | 1,759 | 178 | 56.9s |
| content/vi/aho-1975-corasick/00_front.md | roundtrip | 2 | 32,706 | 215 | 17.3s |
| content/vi/amdahl-1967-law/00_front.md | roundtrip | 2 | 32,861 | 317 | 18.6s |
| content/vi/astrahan-1976-systemr/00_front.md | roundtrip | 2 | 32,880 | 325 | 19.7s |
| content/vi/backus-1978-vonneumann/00_front.md | roundtrip | 2 | 32,998 | 336 | 19.7s |
| content/vi/barham-2003-xen/00_front.md | roundtrip | 2 | 33,045 | 457 | 23.0s |
| content/vi/bayer-1972-btree/00_front.md | roundtrip | 2 | 33,020 | 388 | 22.7s |
| content/vi/birrell-1984-rpc/00_front.md | roundtrip | 2 | 32,813 | 454 | 26.3s |
| content/vi/bloom-1970-filter/00_front.md | roundtrip | 2 | 32,789 | 307 | 19.3s |
| content/vi/brin-1998-pagerank/00_front.md | roundtrip | 2 | 32,897 | 437 | 22.4s |
| content/vi/cerf-1974-tcpip/00_front.md | roundtrip | 2 | 32,152 | 200 | 15.8s |
| content/vi/codd-1970-relational/00_front.md | roundtrip | 2 | 32,950 | 392 | 21.5s |
| content/vi/cook-1971-np/00_front.md | roundtrip | 2 | 32,413 | 180 | 14.5s |
| content/vi/cooley-1965-fft/00_front.md | roundtrip | 2 | 32,822 | 309 | 20.5s |
| content/vi/corbett-2012-spanner/00_front.md | roundtrip | 2 | 32,638 | 268 | 18.2s |
| content/vi/corbett-2012-spanner/07_future_work.md | roundtrip | 2 | 33,143 | 499 | 24.9s |
| content/vi/corbett-2012-spanner/08_conclusions.md | roundtrip | 2 | 32,629 | 319 | 19.3s |
| content/vi/cytron-1991-ssa/00_front.md | roundtrip | 2 | 32,704 | 291 | 19.6s |
| content/vi/dageville-2016-snowflake/00_front.md | roundtrip | 2 | 33,255 | 421 | 22.6s |
| content/vi/dean-2004-mapreduce/00_front.md | roundtrip | 2 | 32,724 | 286 | 18.0s |
| content/vi/decandia-2007-dynamo/00_front.md | roundtrip | 2 | 32,908 | 391 | 21.5s |
| content/vi/dennard-1974-scaling/00_front.md | roundtrip | 2 | 33,165 | 414 | 21.6s |
| content/vi/denning-1968-workingset/00_front.md | roundtrip | 2 | 32,901 | 337 | 21.7s |
| content/vi/deutsch-1984-smalltalk/00_front.md | roundtrip | 2 | 32,550 | 289 | 18.0s |
| content/vi/dewitt-1990-gamma/00_front.md | roundtrip | 2 | 32,912 | 325 | 20.9s |
| content/vi/dijkstra-1959-shortestpath/00_front.md | roundtrip | 2 | 32,775 | 296 | 18.6s |
| content/vi/dijkstra-1968-the/00_front.md | roundtrip | 2 | 32,250 | 207 | 15.9s |
| content/vi/floyd-1962-shortestpath/00_front.md | roundtrip | 2 | 33,133 | 417 | 22.9s |
| content/vi/ford-1956-maxflow/00_front.md | roundtrip | 2 | 32,031 | 88 | 15.5s |
| content/vi/gal-2009-tracejit/00_front.md | roundtrip | 2 | 33,241 | 494 | 24.4s |
| content/vi/ghemawat-2003-gfs/00_front.md | roundtrip | 2 | 32,979 | 325 | 21.9s |
| content/vi/goldwasser-1985-zk/00_front.md | roundtrip | 2 | 32,285 | 92 | 12.8s |
| content/vi/goodfellow-2014-gan/00_front.md | roundtrip | 2 | 35,152 | 859 | 1m 30s |
| content/vi/goodfellow-2014-gan/01_introduction.md | roundtrip | 2 | 3,285 | 701 | 1m 12s |
| content/vi/goodfellow-2014-gan/02_related_work.md | roundtrip | 2 | 3,701 | 1,091 | 1m 24s |
| content/vi/goodfellow-2014-gan/03_adversarial_nets.md | roundtrip | 2 | 4,390 | 1,061 | 1m 20s |
| content/vi/goodfellow-2014-gan/04_theoretical_results.md | roundtrip | 2 | 6,531 | 1,987 | 1m 59s |
| content/vi/goodfellow-2014-gan/05_experiments.md | roundtrip | 2 | 4,927 | 1,457 | 1m 23s |
| content/vi/goodfellow-2014-gan/06_advantages_and_disadvantages.md | roundtrip | 2 | 2,389 | 381 | 1m 6s |
| content/vi/goodfellow-2014-gan/07_conclusions_and_future_work.md | roundtrip | 2 | 2,296 | 402 | 1m 7s |
| content/vi/goodfellow-2014-gan/08_acknowledgments.md | roundtrip | 2 | 1,828 | 174 | 1m 2s |
| content/vi/graefe-1994-volcano/00_front.md | roundtrip | 2 | 33,015 | 491 | 24.9s |
| content/vi/hamming-1950-codes/00_front.md | roundtrip | 2 | 32,637 | 303 | 23.4s |
| content/vi/hoare-1962-quicksort/00_front.md | roundtrip | 2 | 32,707 | 276 | 17.5s |
| content/vi/hoare-1969-axiomatic/00_front.md | roundtrip | 2 | 32,541 | 207 | 15.9s |
| content/vi/jacobson-1988-congestion/00_front.md | roundtrip | 2 | 32,544 | 275 | 17.9s |
| content/vi/jouppi-1990-victimcache/00_front.md | roundtrip | 2 | 32,823 | 301 | 18.2s |
| content/vi/jouppi-2017-tpu/00_front.md | roundtrip | 2 | 34,336 | 816 | 34.2s |
| content/vi/jouppi-2017-tpu/08_discussion.md | roundtrip | 2 | 36,435 | 1,501 | 54.2s |
| content/vi/karp-1972-reducibility/00_front.md | roundtrip | 2 | 32,992 | 421 | 22.6s |
| content/vi/knuth-1977-kmp/00_front.md | roundtrip | 2 | 32,877 | 324 | 20.3s |
| content/vi/lamport-1978-clocks/00_front.md | roundtrip | 2 | 32,364 | 165 | 14.2s |
| content/vi/lamport-1998-paxos/00_front.md | roundtrip | 2 | 32,956 | 410 | 22.9s |
| content/vi/lattner-2004-llvm/00_front.md | roundtrip | 2 | 32,900 | 363 | 21.0s |
| content/vi/mccarthy-1960-lisp/00_front.md | roundtrip | 2 | 32,946 | 392 | 20.5s |
| content/vi/mckeown-2008-openflow/00_front.md | roundtrip | 2 | 32,976 | 373 | 24.0s |
| content/vi/metcalfe-1976-ethernet/00_front.md | roundtrip | 2 | 32,664 | 240 | 17.1s |
| content/vi/mohan-1992-aries/00_front.md | roundtrip | 2 | 32,984 | 332 | 21.2s |
| content/vi/nagle-1984-congestion/00_front.md | roundtrip | 2 | 32,058 | 74 | 13.1s |
| content/vi/ongaro-2014-raft/00_front.md | roundtrip | 2 | 32,429 | 202 | 15.2s |
| content/vi/patterson-1981-risc/00_front.md | roundtrip | 2 | 32,751 | 313 | 22.0s |
| content/vi/rabin-1959-automata/00_front.md | roundtrip | 2 | 32,230 | 157 | 14.0s |
| content/vi/razborov-1997-naturalproofs/00_front.md | roundtrip | 2 | 33,009 | 364 | 21.3s |
| content/vi/ritchie-1974-unix/00_front.md | roundtrip | 2 | 33,016 | 397 | 22.7s |
| content/vi/saltzer-1984-endtoend/00_front.md | roundtrip | 2 | 32,500 | 189 | 16.0s |
| content/vi/savitch-1970-tape/00_front.md | roundtrip | 2 | 32,529 | 321 | 20.8s |
| content/vi/selinger-1979-accesspath/00_front.md | roundtrip | 2 | 32,399 | 234 | 17.8s |
| content/vi/shannon-1948-communication/00_front.md | roundtrip | 2 | 32,287 | 172 | 14.4s |
| content/vi/stoica-2001-chord/00_front.md | roundtrip | 2 | 32,589 | 298 | 18.6s |
| content/vi/stonebraker-2005-cstore/00_front.md | roundtrip | 2 | 32,655 | 412 | 22.3s |
| content/vi/sussman-1975-scheme/00_front.md | roundtrip | 2 | 32,823 | 333 | 19.5s |
| content/vi/tarjan-1972-dfs/00_front.md | roundtrip | 2 | 32,207 | 160 | 13.8s |
| content/vi/tomasulo-1967-algorithm/00_front.md | roundtrip | 2 | 32,369 | 220 | 15.4s |
| content/vi/turing-1936-computable/00_front.md | roundtrip | 2 | 32,730 | 305 | 18.7s |
| content/vi/verma-2015-borg/00_front.md | roundtrip | 2 | 32,467 | 260 | 17.6s |
| content/vi/yeh-1991-branchprediction/00_front.md | roundtrip | 2 | 32,724 | 385 | 21.1s |
| content/zh/goodfellow-2014-gan/00_front.md | roundtrip | 2 | 2,092 | 344 | 1m 3s |
| content/zh/goodfellow-2014-gan/01_introduction.md | roundtrip | 2 | 2,860 | 1,041 | 1m 17s |
| content/zh/goodfellow-2014-gan/02_related_work.md | roundtrip | 2 | 3,167 | 840 | 1m 5s |
| content/zh/goodfellow-2014-gan/03_adversarial_nets.md | roundtrip | 2 | 3,764 | 1,054 | 1m 20s |
| content/zh/goodfellow-2014-gan/04_theoretical_results.md | roundtrip | 2 | 5,916 | 1,915 | 4m 21s |
| content/zh/goodfellow-2014-gan/05_experiments.md | roundtrip | 2 | 4,182 | 1,246 | 1m 18s |
| content/zh/goodfellow-2014-gan/06_advantages_and_disadvantages.md | roundtrip | 2 | 2,185 | 413 | 1m 7s |
| content/zh/goodfellow-2014-gan/07_conclusions_and_future_work.md | roundtrip | 2 | 2,081 | 361 | 1m 16s |
| content/zh/goodfellow-2014-gan/08_acknowledgments.md | roundtrip | 2 | 1,737 | 230 | 3m 16s |
| cook-1971-np | extract | 3 | 35,820 | 3,216 | 48.7s |
| cook-1971-np | translate | 2 | 5,161 | 299 | 10m 24s |
| cooley-1965-fft | extract | 3 | 26,397 | 2,495 | 35.3s |
| corbett-2012-spanner | extract | 14 | 213,984 | 21,708 | 5m 23s |
| corbett-2012-spanner | translate | 3 | 138,904 | 11,395 | 48m 10s |
| cortes-1995-svm | extract | 3 | 35,820 | 1,950 | 31.2s |
| cortes-1995-svm | translate | 1 | 18,400 | 628 | 24.3s |
| cytron-1991-ssa | extract | 3 | 71,058 | 3,239 | 1m 10s |
| dageville-2016-snowflake | extract | 3 | 38,034 | 3,514 | 22m 19s |
| dean-2004-mapreduce | extract | 13 | 492,588 | 40,013 | 58m 47s |
| dean-2004-mapreduce | translate | 2 | 0 | 0 | 3m 47s |
| decandia-2007-dynamo | extract | 3 | 38,034 | 3,367 | 1m 11s |
| dennard-1974-scaling | extract | 3 | 73,480 | 7,756 | 1m 55s |
| dennard-1974-scaling | translate | 1 | 3,667 | 418 | 1m 5s |
| denning-1968-workingset | extract | 3 | 35,820 | 3,172 | 54.6s |
| deutsch-1984-smalltalk | extract | 3 | 35,820 | 3,865 | 1m 4s |
| deutsch-1984-smalltalk | translate | 1 | 2,900 | 297 | 1m 18s |
| devlin-2018-bert | extract | 16 | 858,700 | 82,769 | 1h 10m |
| devlin-2018-bert | translate | 3 | 101,449 | 27,281 | 3h 51m |
| dewitt-1990-gamma | extract | 3 | 27,390 | 1,273 | 4m 58s |
| diffie-1976-newdirections | extract | 3 | 35,491 | 3,400 | 50.3s |
| diffie-1976-newdirections | translate | 1 | 2,606 | 142 | 5m 29s |
| dijkstra-1959-shortestpath | extract | 3 | 36,981 | 1,589 | 26.8s |
| dijkstra-1968-the | extract | 3 | 35,820 | 864 | 18.2s |
| engelbart-1968-augmenting | extract | 3 | 39,195 | 1,383 | 3m 37s |
| floyd-1962-shortestpath | extract | 4 | 137,748 | 17,378 | 5m 43s |
| floyd-1962-shortestpath | translate | 3 | 34,746 | 2,265 | 18m 5s |
| ford-1956-maxflow | extract | 3 | 22,476 | 2,768 | 38.2s |
| freund-1997-adaboost | extract | 3 | 81,994 | 8,122 | 15m 9s |
| gal-2009-tracejit | extract | 3 | 174,504 | 11,252 | 20m 14s |
| gal-2009-tracejit | translate | 1 | 6,415 | 1,024 | 1m 39s |
| ghemawat-2003-gfs | extract | 3 | 38,034 | 3,002 | 1m 13s |
| glossary | glossary | 14 | 15,789 | 2,036 | 34m 18s |
| goldwasser-1984-probabilistic | extract | 3 | 35,820 | 1,890 | 33.4s |
| goldwasser-1985-zk | extract | 3 | 35,820 | 3,085 | 50.5s |
| goodfellow-2014-gan | extract | 9 | 354,619 | 20,749 | 13m 35s |
| goodfellow-2014-gan | translate | 9 | 553,258 | 67,490 | 5h 49m |
| graefe-1994-volcano | extract | 3 | 36,359 | 3,277 | 46.2s |
| hamming-1950-codes | extract | 3 | 18,786 | 1,508 | 23.3s |
| hamming-1950-codes | translate | 1 | 0 | 0 | 1m 0s |
| he-2016-resnet | extract | 12 | 255,693 | 44,452 | 37m 54s |
| he-2016-resnet | translate | 7 | 203,739 | 37,028 | 2h 16m |
| hoare-1962-quicksort | extract | 3 | 36,981 | 3,703 | 55.7s |
| hoare-1969-axiomatic | extract | 4 | 122,603 | 16,034 | 4m 15s |
| jacobson-1988-congestion | extract | 3 | 39,195 | 1,759 | 3m 37s |
| jouppi-1990-victimcache | extract | 3 | 35,820 | 4,052 | 58.8s |
| jouppi-2017-tpu | extract | 17 | 439,428 | 51,028 | 39m 50s |
| jouppi-2017-tpu | translate | 1 | 49,798 | 6,707 | 4m 55s |
| karp-1972-reducibility | extract | 3 | 22,911 | 779 | 14.7s |
| knuth-1977-kmp | extract | 3 | 26,718 | 71,586 | 15m 50s |
| knuth-1977-kmp | translate | 1 | 0 | 0 | 2m 16s |
| krizhevsky-2012-imagenet | extract | 3 | 38,034 | 2,652 | 5m 30s |
| lamport-1978-clocks | extract | 3 | 35,820 | 3,210 | 1m 2s |
| lamport-1998-paxos | translate | 1 | 3,194 | 419 | 3m 16s |
| lattner-2004-llvm | extract | 3 | 38,034 | 3,461 | 1m 17s |
| lattner-2004-llvm | translate | 1 | 0 | 0 | 22.8s |
| lecun-1998-lenet | extract | 3 | 89,493 | 5,580 | 23m 6s |
| lecun-1998-lenet | translate | 1 | 18,221 | 531 | 21.8s |
| mccabe-1976-complexity | extract | 3 | 3,753 | 2,883 | 15m 13s |
| mccarthy-1960-lisp | translate | 1 | 18,068 | 464 | 21.1s |
| mckeown-2008-openflow | extract | 3 | 38,034 | 3,341 | 6m 12s |
| metcalfe-1976-ethernet | extract | 3 | 35,820 | 2,689 | 41.0s |
| milner-1978-polymorphism | extract | 3 | 28,669 | 1,628 | 31.1s |
| milner-1978-polymorphism | translate | 1 | 9,648 | 1,412 | 13m 9s |
| mohan-1992-aries | extract | 3 | 35,820 | 3,091 | 43.9s |
| nagle-1984-congestion | extract | 3 | 35,820 | 1,623 | 27.1s |
| nakamoto-2008-bitcoin | extract | 9 | 443,976 | 17,886 | 17m 26s |
| nakamoto-2008-bitcoin | translate | 1 | 204,627 | 8,873 | 39m 14s |
| needham-1978-authentication | extract | 3 | 35,820 | 3,294 | 48.8s |
| ongaro-2014-raft | extract | 3 | 38,034 | 3,059 | 1m 13s |
| parnas-1972-modules | extract | 3 | 35,820 | 2,642 | 40.8s |
| patterson-1981-risc | extract | 3 | 36,266 | 2,843 | 43.3s |
| phong-1975-illumination | extract | 3 | 35,820 | 2,453 | 39.0s |
| rabin-1959-automata | extract | 3 | 36,809 | 3,938 | 56.0s |
| rabin-1959-automata | translate | 3 | 24,955 | 452 | 12m 31s |
| razborov-1997-naturalproofs | extract | 2 | 2,104 | 634 | 13m 38s |
| ritchie-1974-unix | extract | 3 | 87,072 | 6,197 | 1m 40s |
| rivest-1978-rsa | extract | 3 | 39,195 | 1,802 | 23m 25s |
| royce-1970-lifecycle | extract | 3 | 98,820 | 1,417 | 21m 22s |
| rumelhart-1986-backprop | extract | 3 | 36,528 | 3,777 | 59.3s |
| saltzer-1975-protection | extract | 3 | 35,820 | 1,988 | 31.4s |
| saltzer-1984-endtoend | extract | 3 | 35,820 | 2,222 | 42.6s |
| savitch-1970-tape | extract | 3 | 25,236 | 1,954 | 29.1s |
| savitch-1970-tape | translate | 1 | 2,543 | 106 | 2m 45s |
| selinger-1979-accesspath | extract | 3 | 89,106 | 6,244 | 17m 11s |
| shannon-1948-communication | extract | 3 | 38,034 | 2,384 | 46.2s |
| shannon-1948-communication | translate | 1 | 17,651 | 197 | 11.5s |
| shneiderman-1983-directmanipulation | extract | 3 | 35,820 | 2,746 | 54.4s |
| shneiderman-1983-directmanipulation | translate | 3 | 8,740 | 771 | 7m 32s |
| silver-2016-alphago | extract | 3 | 87,382 | 9,838 | 1h 5m |
| steiner-1988-kerberos | extract | 3 | 38,034 | 2,270 | 4m 28s |
| stoica-2001-chord | extract | 3 | 56,214 | 4,995 | 1h 2m |
| stonebraker-2005-cstore | extract | 3 | 27,390 | 3,542 | 1m 44s |
| sussman-1975-scheme | extract | 3 | 35,820 | 1,341 | 27.8s |
| sussman-1975-scheme | translate | 3 | 26,800 | 1,252 | 11m 10s |
| sutherland-1963-sketchpad | extract | 3 | 39,195 | 623 | 2m 18s |
| sutskever-2014-seq2seq | extract | 9 | 201,108 | 14,822 | 3m 45s |
| sutskever-2014-seq2seq | translate | 6 | 116,098 | 12,114 | 54m 7s |
| tarjan-1972-dfs | extract | 3 | 26,718 | 2,654 | 37.6s |
| tomasulo-1967-algorithm | extract | 3 | 35,820 | 2,242 | 33.6s |
| turing-1936-computable | extract | 3 | 24,510 | 1,567 | 25.0s |
| turing-1936-computable | translate | 2 | 20,863 | 531 | 3m 24s |
| turing-1950-intelligence | extract | 3 | 35,820 | 1,786 | 28.5s |
| vaswani-2017-attention | extract | 15 | 457,248 | 35,203 | 25m 2s |
| vaswani-2017-attention | translate | 3 | 112,714 | 10,509 | 28m 16s |
| verma-2015-borg | extract | 3 | 74,394 | 4,589 | 4m 45s |
| wegman-1991-sccp | extract | 3 | 70,704 | 3,117 | 56.4s |
| wegman-1991-sccp | translate | 1 | 0 | 0 | 20m 16s |
| yeh-1991-branchprediction | extract | 3 | 71,150 | 4,293 | 1m 14s |

## What did not answer

| stage | why | asks |
| --- | --- | --: |
| extract | unreachable | 49 |
| extract | broken | 25 |
| extract | unauthorized | 3 |
| extract | quota | 1 |
| glossary | broken | 3 |
| translate | broken | 53 |
| translate | unreachable | 13 |
| translate | quota | 3 |
| roundtrip | broken | 2 |
