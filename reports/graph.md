# The citation graph

Which papers of this corpus cite which others of it.

An edge is a bibliography entry of one paper here that was resolved to another paper here. Almost every reference in the corpus points somewhere else, which is what a hundred papers spread over eighty years looks like, so the edge count is small next to the reference count and that is the right shape rather than a shortfall.

101 papers, 9 with a bibliography read, 15 edges between them out of 296 references.

92 papers have no bibliography read yet. A paper with none cites nothing here, which is not the same as citing nothing.

## Edges

| cites | cited |
| --- | --- |
| corbett-2012-spanner | ghemawat-2003-gfs |
| corbett-2012-spanner | lamport-1998-paxos |
| dean-2004-mapreduce | ghemawat-2003-gfs |
| devlin-2018-bert | vaswani-2017-attention |
| goodfellow-2014-gan | krizhevsky-2012-imagenet |
| goodfellow-2014-gan | lecun-1998-lenet |
| he-2016-resnet | hochreiter-1997-lstm |
| he-2016-resnet | krizhevsky-2012-imagenet |
| sutskever-2014-seq2seq | hochreiter-1997-lstm |
| sutskever-2014-seq2seq | krizhevsky-2012-imagenet |
| sutskever-2014-seq2seq | lecun-1998-lenet |
| sutskever-2014-seq2seq | rumelhart-1986-backprop |
| vaswani-2017-attention | he-2016-resnet |
| vaswani-2017-attention | hochreiter-1997-lstm |
| vaswani-2017-attention | sutskever-2014-seq2seq |

## Most cited

The papers of the corpus that other papers of the corpus cite, most cited first.

| paper | field | year | cited by |
| --- | --- | --: | --- |
| hochreiter-1997-lstm | ai-ml | 1997 | he-2016-resnet, sutskever-2014-seq2seq, vaswani-2017-attention |
| krizhevsky-2012-imagenet | ai-ml | 2012 | goodfellow-2014-gan, he-2016-resnet, sutskever-2014-seq2seq |
| ghemawat-2003-gfs | systems | 2003 | corbett-2012-spanner, dean-2004-mapreduce |
| lecun-1998-lenet | ai-ml | 1998 | goodfellow-2014-gan, sutskever-2014-seq2seq |
| he-2016-resnet | ai-ml | 2016 | vaswani-2017-attention |
| lamport-1998-paxos | systems | 1998 | corbett-2012-spanner |
| rumelhart-1986-backprop | ai-ml | 1986 | sutskever-2014-seq2seq |
| sutskever-2014-seq2seq | ai-ml | 2014 | vaswani-2017-attention |
| vaswani-2017-attention | ai-ml | 2017 | devlin-2018-bert |

## Cited from outside

Papers this corpus does not hold that 2 or more papers in it cite. This is the reading list, and audit rule R07 reports the strongest of these as a finding.

| title as printed | cited by |
| --- | --- |
| deep neural networks for acoustic modeling in speech recognition | goodfellow-2014-gan, sutskever-2014-seq2seq |
| extracting and composing robust features with denoising autoencoders | devlin-2018-bert, goodfellow-2014-gan |
| generating sequences with recurrent neural networks | sutskever-2014-seq2seq, vaswani-2017-attention |
| gradient flow in recurrent nets: the difficulty of learning long-term dependencies, 2001 | sutskever-2014-seq2seq, vaswani-2017-attention |
| improving neural networks by preventing co-adaptation of feature detectors | goodfellow-2014-gan, he-2016-resnet |
| learning long-term dependencies with gradient descent is difficult | he-2016-resnet, sutskever-2014-seq2seq |
| learning multiple layers of features from tiny images | goodfellow-2014-gan, he-2016-resnet |
| learning phrase representations using rnn encoder-decoder for statistical machine translation | sutskever-2014-seq2seq, vaswani-2017-attention |
| maxout networks | goodfellow-2014-gan, he-2016-resnet |
| neural machine translation by jointly learning to align and translate | sutskever-2014-seq2seq, vaswani-2017-attention |

## Connected to nothing

The 2 papers whose bibliography has been read and that neither cite nor are cited by anything else here. A paper stays in this list until the corpus grows around it.

- bosshart-2014-p4
- nakamoto-2008-bitcoin
