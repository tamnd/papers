---
paper: cortes-1995-svm
title: Support-Vector Networks
authors:
  - Corinna Cortes
  - Vladimir Vapnik
year: 1995
venue: Machine Learning
field: ai-ml
section: "6"
section_title: Experimental Analysis
tag: "0848"
kind: section
lang: en
source: https://doi.org/10.1023/a:1022627411411
pdf_sha256: 561361e49eb22df6f5e14f8c19d681c6b596891f07057fc43703394383233002
pdf_pages: 14-18
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 914eb477ca72a4197177b6a819159e4261a3a23b106f942d56d12f56c458ac1e
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

To demonstrate the support-vector network method we conduct two types of experiments. We construct artificial sets of patterns in the plane and experiment with 2nd degree polynomial decision surfaces, and we conduct experiments with the real-life problem of digit recognition.

### 6.1. Experiments in the Plane {#cortes-1995-svm-s6-1 .section tag=0849}

Using dot-products of the form

$$
K(\mathbf{u}, \mathbf{v}) = (\mathbf{u} \cdot \mathbf{v} + 1)^d
$$

with $d = 2$ we construct decision rules for different sets of patterns in the plane. Results of these experiments can be visualized and provide nice illustrations of the power of the algorithm. Examples are shown in Fig. 5. The 2 classes are represented by black and white

Figure.

Figure 5. Examples of the dot-product (39) with $d = 2$. Support patterns are indicated with double circles, errors with a cross. {#cortes-1995-svm-fig-5 .figure tag=084A}

SUPPORT-VECTOR NETWORKS bullets. In the figure we indicate support patterns with a double circle, and errors with a cross. The solutions are optimal in the sense that no 2nd degree polynomials exist that make less errors. Notice that the numbers of support patterns relative to the number of training patterns are small.

Figure 6. Examples of patterns with labels from the US Postal Service digit database. {#cortes-1995-svm-fig-6 .figure tag=084B}

### 6.2. Experiments with Digit Recognition {#cortes-1995-svm-s6-2 .section tag=084C}

Our experiments for constructing support-vector networks make use of two different databases for bit-mapped digit recognition, a small and a large database. The small one is a US Postal Service database that contains 7,300 training patterns and 2,000 test patterns. The resolution of the database is $16 \times 16$ pixels, and some typical examples are shown in Fig. 6. On this database we report experimental research with polynomials of various degree.

The large database consists of 60,000 training and 10,000 test patterns, and is a 50-50 mixture of the NIST$^7$ training and test sets. The resolution of these patterns is $28 \times 28$ yielding an input dimensionality of 784. On this database we have only constructed a 4th degree polynomial classifier. The performance of this classifier is compared to other types of learning machines that took part in a benchmark study (Bottou, 1994).

In all our experiments ten separators, one for each class, are constructed. Each hypersurface makes use of the same dot product and pre-processing of the data. Classification of an unknown patterns is done according to the maximum output of these ten classifiers.

6.2.1. Experiments with US Postal Service Database. The US Postal Service Database has been recorded from actual mail pieces and results from this database have been reported by several researchers. In Table 1 we list the performance of various classifiers collected

Table 1. Performance of various classifiers collected from publications and own experiments. For references see text. {#cortes-1995-svm-tab-1 .table tag=084D}

| Classifier | Raw error, % |
| --- | --- |
| Human performance | 2.5 |
| Decision tree, CART | 17 |
| Decision tree, C4.5 | 16 |
| Best 2 layer neural network | 6.6 |
| Special architecture 5 layer network | 5.1 |

Table 2. Results obtained for dot products of polynomials of various degree. The number of "support vectors" is a mean value per classifier. {#cortes-1995-svm-tab-2 .table tag=084E}

| Degree of polynomial | Raw error, % | Support vectors | Dimensionality of feature space |
| --- | --- | --- | --- |
| 1 | 12.0 | 200 | 256 |
| 2 | 4.7 | 127 | ~33000 |
| 3 | 4.4 | 148 | ~$1 \times 10^6$ |
| 4 | 4.3 | 165 | ~$1 \times 10^9$ |
| 5 | 4.3 | 175 | ~$1 \times 10^{12}$ |
| 6 | 4.2 | 185 | ~$1 \times 10^{14}$ |
| 7 | 4.3 | 190 | ~$1 \times 10^{16}$ |

from publications and own experiments. The result of human performance was reported by J. Bromley & E. Sackinger (Bromley & Sackinger, 1991). The result with CART was carried out by Daryl Pregibon and Michael D. Riley at Bell Labs., Murray Hill, NJ. The results of C4.5 and the best 2-layer neural network (with optimal number of hidden units) were obtained specially for this paper by Corinna Cortes and Bernard Schoelkopf respectively. The result with a special purpose neural network architecture with 5 layers, LeNet1, was obtained by Y. LeCun et al. (1990).

On the experiments with the US Postal Service Database we used pre-processing (centering, de-slanting and smoothing) to incorporate knowledge about the invariances of the problem at hand. The effect of smoothing of this database as a pre-processing for support-vector networks was investigated in (Boser, Guyon & Vapnik, 1992). For our experiments we chose the smoothing kernel as a Gaussian with standard deviation $\sigma = 0.75$ in agreement with (Boser, Guyon & Vapnik, 1992).

In the experiments with this database we constructed polynomial indicator functions based on dot-products of the form (39). The input dimensionality was 256, and the order of the polynomial ranged from 1 to 7. Table 2 describes the results of the experiments. The training data are not linearly separable.

Notice that the number of support vectors increases very slowly. The 7 degree polynomial has only 30% more support vectors than the 3rd degree polynomial—and even less than the first degree polynomial. The dimensionality of the feature space for a 7 degree polynomial is however $10^{10}$ times larger than the dimensionality of the feature space for a 3rd degree polynomial classifier. Note that performance almost does not change with increasing dimensionality of the space—indicating no over-fitting problems.

The relatively high number of support vectors for the linear separator is due to non-separability: the number 200 includes both support vectors and training vectors with a non-zero $\xi$-value. If $\xi > 1$ the training vector is misclassified; the number of mis-classifications on the training set averages to 34 per classifier for the linear case. For a 2nd degree classifier the total number of mis-classifications on the training set is down to 4. These 4 patterns are shown in Fig. 7.

It is remarkable that in all our experiments the bound for generalization ability (5) holds when we consider the number of obtained support vectors instead of the expectation value of this number. In all cases the upper bound on the error probability for the single classifier does not exceed 3% (on the test data the actual error does not exceed 1.5% for the single classifier).

SUPPORT-VECTOR NETWORKS

Figure.

Figure 7. Labeled examples of errors on the training set for the 2nd degree polynomial support-vector classifier. {#cortes-1995-svm-fig-7 .figure tag=084F}

The training time for construction of polynomial classifiers does not depend on the degree of the polynomial—only the number of support vectors. Even in the worst case it is faster than the best performing neural network, constructed specially for the task, LeNet1 (LeCun, et al., 1990). The performance of this neural network is 5.1% raw error. Polynomials with degree 2 or higher outperform LeNet1.

6.2.2. Experiments with the NIST Database. The NIST database was used for benchmark studies conducted over just 2 weeks. The limited time frame enabled only the construction of 1 type of classifier, for which we chose a 4th degree polynomial with no pre-processing. Our choice was based on our experience with the US Postal database.

Table 3 lists the number of support vectors for each of the 10 classifiers and gives the performance of the classifier on the training and test sets. Notice that even polynomials of degree 4 (that have more than $10^8$ free parameters) commit errors on this training set. The average frequency of training errors is $0.02\% \sim 12$ per class. The 14 misclassified test patterns for classifier 1 are shown in Fig. 8. Notice again how the upper bound (5) holds for the obtained number of support vectors.

The combined performance of the ten classifiers on the test set is 1.1% error. This result should be compared to that of other participating classifiers in the benchmark study. These other classifiers include a linear classifier, a $k = 3$-nearest neighbor classifier with 60,000 prototypes, and two neural networks specially constructed for digit recognition (LeNet1 and LeNet4). The authors only contributed with results for support-vector networks. The results of the benchmark are given in Fig. 9.

We conclude this section by citing the paper (Bottou, et al., 1994) describing results of the benchmark:

For quite a long time LeNet1 was considered state of the art.... Through a series of experiments in architecture, combined with an analysis of the characteristics of recognition error, LeNet4 was crafted....
The support-vector network has excellent accuracy, which is most remarkable, because unlike the other high performance classifiers, it does not include knowledge

Table 3. Results obtained for a 4th degree polynomial classifier on the NIST database. The size of the training set is 60,000, and the size of the test set is 10,000 patterns. {#cortes-1995-svm-tab-3 .table tag=0850}

|  | Cl. 0 | Cl. 1 | Cl. 2 | Cl. 3 | Cl. 4 | Cl. 5 | Cl. 6 | Cl. 7 | Cl. 8 | Cl. 9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Supp. patt. | 1379 | 989 | 1958 | 1900 | 1224 | 2024 | 1527 | 2064 | 2332 | 2765 |
| Error train | 7 | 16 | 8 | 11 | 2 | 4 | 8 | 16 | 4 | 1 |
| Error test | 19 | 14 | 35 | 35 | 36 | 49 | 32 | 43 | 48 | 63 |

Figure 8. The 14 misclassified test patterns with labels for classifier 1. Patterns with label “1” are false negative. Patterns with other labels are false positive. {#cortes-1995-svm-fig-8 .figure tag=0851}

Figure 9. Results from the benchmark study. {#cortes-1995-svm-fig-9 .figure tag=0852}

about the geometry of the problem. In fact the classifier would do as well if the image pixels were encrypted e.g. by a fixed, random permutation.

The last remark suggests that further improvement of the performance of the support-vector network can be expected from the construction of functions for the dot-product $K(\mathbf{u}, \mathbf{v})$ that reflect a priori information about the problem at hand.
