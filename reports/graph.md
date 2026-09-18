# The citation graph

Which papers of this corpus cite which others of it.

An edge is a bibliography entry of one paper here that was resolved to another paper here. Almost every reference in the corpus points somewhere else, which is what a hundred papers spread over eighty years looks like, so the edge count is small next to the reference count and that is the right shape rather than a shortfall.

102 papers, 19 with a bibliography read, 26 edges between them out of 678 references.

83 papers have no bibliography read yet. A paper with none cites nothing here, which is not the same as citing nothing.

## Edges

| cites | cited |
| --- | --- |
| brown-2020-gpt3 | devlin-2018-bert |
| brown-2020-gpt3 | vaswani-2017-attention |
| corbett-2012-spanner | ghemawat-2003-gfs |
| corbett-2012-spanner | lamport-1998-paxos |
| dean-2004-mapreduce | ghemawat-2003-gfs |
| devlin-2018-bert | vaswani-2017-attention |
| devlin-2018-bert | wu-2016-gnmt |
| dewitt-1990-gamma | astrahan-1976-systemr |
| dewitt-1990-gamma | selinger-1979-accesspath |
| goodfellow-2014-gan | krizhevsky-2012-imagenet |
| goodfellow-2014-gan | lecun-1998-lenet |
| he-2016-resnet | hochreiter-1997-lstm |
| he-2016-resnet | krizhevsky-2012-imagenet |
| jouppi-2017-tpu | krizhevsky-2012-imagenet |
| jouppi-2017-tpu | silver-2016-alphago |
| jouppi-2017-tpu | wu-2016-gnmt |
| metcalfe-1976-ethernet | cerf-1974-tcpip |
| saltzer-1984-endtoend | diffie-1976-newdirections |
| sutskever-2014-seq2seq | hochreiter-1997-lstm |
| sutskever-2014-seq2seq | krizhevsky-2012-imagenet |
| sutskever-2014-seq2seq | lecun-1998-lenet |
| sutskever-2014-seq2seq | rumelhart-1986-backprop |
| vaswani-2017-attention | he-2016-resnet |
| vaswani-2017-attention | hochreiter-1997-lstm |
| vaswani-2017-attention | sutskever-2014-seq2seq |
| vaswani-2017-attention | wu-2016-gnmt |

## Most cited

The papers of the corpus that other papers of the corpus cite, most cited first.

| paper | field | year | cited by |
| --- | --- | --: | --- |
| krizhevsky-2012-imagenet | ai-ml | 2012 | goodfellow-2014-gan, he-2016-resnet, jouppi-2017-tpu, sutskever-2014-seq2seq |
| hochreiter-1997-lstm | ai-ml | 1997 | he-2016-resnet, sutskever-2014-seq2seq, vaswani-2017-attention |
| wu-2016-gnmt | ai-ml | 2016 | devlin-2018-bert, jouppi-2017-tpu, vaswani-2017-attention |
| ghemawat-2003-gfs | systems | 2003 | corbett-2012-spanner, dean-2004-mapreduce |
| lecun-1998-lenet | ai-ml | 1998 | goodfellow-2014-gan, sutskever-2014-seq2seq |
| vaswani-2017-attention | ai-ml | 2017 | brown-2020-gpt3, devlin-2018-bert |
| astrahan-1976-systemr | databases | 1976 | dewitt-1990-gamma |
| cerf-1974-tcpip | networks | 1974 | metcalfe-1976-ethernet |
| devlin-2018-bert | ai-ml | 2018 | brown-2020-gpt3 |
| diffie-1976-newdirections | security | 1976 | saltzer-1984-endtoend |
| he-2016-resnet | ai-ml | 2016 | vaswani-2017-attention |
| lamport-1998-paxos | systems | 1998 | corbett-2012-spanner |
| rumelhart-1986-backprop | ai-ml | 1986 | sutskever-2014-seq2seq |
| selinger-1979-accesspath | databases | 1979 | dewitt-1990-gamma |
| silver-2016-alphago | ai-ml | 2016 | jouppi-2017-tpu |
| sutskever-2014-seq2seq | ai-ml | 2014 | vaswani-2017-attention |

## Cited from outside

Papers this corpus does not hold that 2 or more papers in it cite. This is the reading list, and audit rule R07 reports the strongest of these as a finding.

| title as printed | cited by |
| --- | --- |
| deep neural networks for acoustic modeling in speech recognition | goodfellow-2014-gan, sutskever-2014-seq2seq |
| edinburgh’s phrase-based machine translation systems for wmt-14 | brown-2020-gpt3, sutskever-2014-seq2seq |
| exploring the limits of language modeling | brown-2020-gpt3, vaswani-2017-attention |
| extracting and composing robust features with denoising autoencoders | devlin-2018-bert, goodfellow-2014-gan |
| generating sequences with recurrent neural networks | sutskever-2014-seq2seq, vaswani-2017-attention |
| glove: global vectors for word representation | brown-2020-gpt3, devlin-2018-bert |
| going deeper with convolutions | he-2016-resnet, jouppi-2017-tpu |
| gradient flow in recurrent nets: the difficulty of learning long-term dependencies, 2001 | sutskever-2014-seq2seq, vaswani-2017-attention |
| imagenet large scale visual recognition challenge | he-2016-resnet, jouppi-2017-tpu |
| improving neural networks by preventing co-adaptation of feature detectors | goodfellow-2014-gan, he-2016-resnet |
| learned in translation: contextualized word vectors | brown-2020-gpt3, devlin-2018-bert |
| learning long-term dependencies with gradient descent is difficult | he-2016-resnet, sutskever-2014-seq2seq |
| learning multiple layers of features from tiny images | goodfellow-2014-gan, he-2016-resnet |
| learning phrase representations using rnn encoder-decoder for statistical machine translation | sutskever-2014-seq2seq, vaswani-2017-attention |
| maxout networks | goodfellow-2014-gan, he-2016-resnet |
| neural machine translation by jointly learning to align and translate | sutskever-2014-seq2seq, vaswani-2017-attention |
| notes on database operating systems | dewitt-1990-gamma, saltzer-1984-endtoend |
| outrageously large neural networks: the sparsely-gated mixture-of-experts layer | brown-2020-gpt3, vaswani-2017-attention |
| private communication | jouppi-1990-victimcache, jouppi-2017-tpu |
| semi-supervised sequence learning | brown-2020-gpt3, devlin-2018-bert |
| the fifth pascal recognizing textual entailment challenge | brown-2020-gpt3, devlin-2018-bert |
| the winograd schema challenge | brown-2020-gpt3, devlin-2018-bert |
| triviaqa: a large scale distantly supervised challenge dataset for reading comprehension | brown-2020-gpt3, devlin-2018-bert |
| universal language model fine-tuning for text classification | brown-2020-gpt3, devlin-2018-bert |

## Connected to nothing

The 6 papers whose bibliography has been read and that neither cite nor are cited by anything else here. A paper stays in this list until the corpus grows around it.

- bosshart-2014-p4
- jouppi-1990-victimcache
- mccarthy-1960-lisp
- nakamoto-2008-bitcoin
- rabin-1959-automata
- razborov-1997-naturalproofs
