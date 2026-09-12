# Usage

What the corpus cost in machine time, by stage.

This is read from the ledger, which is one line per ask and lives at `~/.config/papers/ledger.jsonl` on the machine that did the work. The ledger is not in this repository and will not be: it names the hosts that were asked. Nothing below names a host.

257 asks, 248 of them answered and 1 refused before the model read the question. 2,776,185 tokens in, 256,403 out, 1h 54m of waiting over 198 targets, from 2026-09-12 to 2026-09-12.

## Pages read

Counted off the committed English content, one page counted once per paper however many sections were cut from it. `native` is pdftotext on a born digital file with no model anywhere in the path, so those pages were never guessed. `layout` is a layout model reading the page geometry and `ocr` is a vision model reading a page image, and only those two cost anything in the tables below.

| path | papers | pages | what read them |
| --- | --: | --: | --- |
| native | 4 | 8 | pdftotext version 26.09.0 |
| vision | 56 | 125 | gpt-5, olmOCR-2-7B-1025-FP8 |

## Per stage

A target is the thing one ask was about: a page for the extract stage, a section for translate. Asks are higher than targets when a host did not answer and the question went to the next one.

| stage | asks | answered | refused | targets | tokens in | tokens out | time | cost |
| --- | --: | --: | --: | --: | --: | --: | --: | --: |
| extract | 257 | 248 | 1 | 198 | 2,776,185 | 256,403 | 1h 54m | - |
| figures | 0 | 0 | 0 | 0 | 0 | 0 | 0s | - |
| refs | 0 | 0 | 0 | 0 | 0 | 0 | 0s | - |
| glossary | 0 | 0 | 0 | 0 | 0 | 0 | 0s | - |
| translate | 0 | 0 | 0 | 0 | 0 | 0 | 0s | - |

257 of the 257 asks went to a model with no price set, so the money column is a dash for them. Most of this corpus is built on a subscription and on free gateways, where an ask costs a turn rather than a sum of money, and writing zero dollars there would be claiming a measurement nobody made. A price table is a JSON file of dollars per million tokens by model, passed with `papers report usage -prices`.

## Per model

| model | asks | tokens in | tokens out | cost |
| --- | --: | --: | --: | --: |
| not recorded | 9 | 0 | 0 | - |
| gpt-5-6 | 12 | 15,012 | 3,737 | - |
| reader-a | 236 | 2,761,173 | 252,666 | - |

## Per paper

In id order rather than in order of cost, so that two of these reports can be read side by side.

| paper | stage | targets | tokens in | tokens out | time |
| --- | --- | --: | --: | --: | --: |
| aho-1975-corasick | extract | 3 | 35,820 | 3,245 | 51.2s |
| astrahan-1976-systemr | extract | 3 | 26,076 | 1,372 | 22.2s |
| backus-1978-vonneumann | extract | 3 | 35,820 | 2,975 | 48.9s |
| bayer-1972-btree | extract | 3 | 24,108 | 690 | 12.5s |
| birrell-1984-rpc | extract | 3 | 58,036 | 3,039 | 52.0s |
| bloom-1970-filter | extract | 3 | 35,820 | 3,734 | 56.2s |
| brin-1998-pagerank | extract | 3 | 31,178 | 2,420 | 47.6s |
| brooks-1987-nosilverbullet | extract | 6 | 40,019 | 1,664 | 6m 54s |
| cerf-1974-tcpip | extract | 3 | 36,981 | 2,415 | 37.6s |
| chiu-1989-aimd | extract | 3 | 10,086 | 107 | 3.5s |
| codd-1970-relational | extract | 3 | 34,073 | 4,183 | 59.4s |
| cook-1971-np | extract | 3 | 35,820 | 3,216 | 48.7s |
| cooley-1965-fft | extract | 3 | 26,397 | 2,495 | 35.3s |
| cortes-1995-svm | extract | 3 | 35,820 | 1,950 | 31.2s |
| cytron-1991-ssa | extract | 3 | 71,058 | 3,239 | 1m 10s |
| dean-2004-mapreduce | extract | 3 | 35,820 | 1,955 | 35.4s |
| dennard-1974-scaling | extract | 3 | 73,480 | 7,756 | 1m 55s |
| denning-1968-workingset | extract | 3 | 35,820 | 3,172 | 54.6s |
| deutsch-1984-smalltalk | extract | 3 | 35,820 | 3,865 | 1m 4s |
| diffie-1976-newdirections | extract | 3 | 35,491 | 3,400 | 50.3s |
| dijkstra-1959-shortestpath | extract | 3 | 36,981 | 1,589 | 26.8s |
| dijkstra-1968-the | extract | 3 | 35,820 | 864 | 18.2s |
| floyd-1962-shortestpath | extract | 3 | 35,820 | 4,404 | 1m 3s |
| ford-1956-maxflow | extract | 3 | 22,476 | 2,768 | 38.2s |
| goldwasser-1984-probabilistic | extract | 3 | 35,820 | 1,890 | 33.4s |
| goldwasser-1985-zk | extract | 3 | 35,820 | 3,085 | 50.5s |
| graefe-1994-volcano | extract | 3 | 36,359 | 3,277 | 46.2s |
| hamming-1950-codes | extract | 3 | 18,786 | 1,508 | 23.3s |
| hoare-1962-quicksort | extract | 3 | 36,981 | 3,703 | 55.7s |
| hoare-1969-axiomatic | extract | 3 | 32,931 | 4,687 | 1m 9s |
| jouppi-1990-victimcache | extract | 3 | 35,820 | 4,052 | 58.8s |
| karp-1972-reducibility | extract | 3 | 22,911 | 779 | 14.7s |
| knuth-1977-kmp | extract | 3 | 26,718 | 71,586 | 15m 50s |
| lamport-1978-clocks | extract | 3 | 35,820 | 3,210 | 1m 2s |
| mccabe-1976-complexity | extract | 3 | 3,753 | 2,883 | 15m 13s |
| metcalfe-1976-ethernet | extract | 3 | 35,820 | 2,689 | 41.0s |
| milner-1978-polymorphism | extract | 3 | 28,669 | 1,628 | 31.1s |
| mohan-1992-aries | extract | 3 | 35,820 | 3,091 | 43.9s |
| nagle-1984-congestion | extract | 3 | 35,820 | 1,623 | 27.1s |
| nakamoto-2008-bitcoin | extract | 9 | 443,976 | 17,886 | 17m 26s |
| needham-1978-authentication | extract | 3 | 35,820 | 3,294 | 48.8s |
| parnas-1972-modules | extract | 3 | 35,820 | 2,642 | 40.8s |
| patterson-1981-risc | extract | 3 | 36,266 | 2,843 | 43.3s |
| phong-1975-illumination | extract | 3 | 35,820 | 2,453 | 39.0s |
| rabin-1959-automata | extract | 3 | 36,809 | 3,938 | 56.0s |
| royce-1970-lifecycle | extract | 3 | 29,286 | 149 | 7.3s |
| rumelhart-1986-backprop | extract | 3 | 36,528 | 3,777 | 59.3s |
| saltzer-1975-protection | extract | 3 | 35,820 | 1,988 | 31.4s |
| saltzer-1984-endtoend | extract | 3 | 35,820 | 2,222 | 42.6s |
| savitch-1970-tape | extract | 3 | 25,236 | 1,954 | 29.1s |
| shneiderman-1983-directmanipulation | extract | 3 | 35,820 | 2,746 | 54.4s |
| sussman-1975-scheme | extract | 3 | 35,820 | 1,341 | 27.8s |
| tarjan-1972-dfs | extract | 3 | 26,718 | 2,654 | 37.6s |
| tomasulo-1967-algorithm | extract | 3 | 35,820 | 2,242 | 33.6s |
| turing-1936-computable | extract | 3 | 24,510 | 1,567 | 25.0s |
| turing-1950-intelligence | extract | 3 | 35,820 | 1,786 | 28.5s |
| vaswani-2017-attention | extract | 15 | 310,134 | 17,303 | 20m 1s |
| wegman-1991-sccp | extract | 3 | 70,704 | 3,117 | 56.4s |
| yeh-1991-branchprediction | extract | 3 | 71,150 | 4,293 | 1m 14s |

## What did not answer

| stage | why | asks |
| --- | --- | --: |
| extract | unreachable | 8 |
| extract | unauthorized | 1 |
