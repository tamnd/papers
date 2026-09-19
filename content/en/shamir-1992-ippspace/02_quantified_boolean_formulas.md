---
paper: shamir-1992-ippspace
title: IP = PSPACE
authors:
  - Adi Shamir
year: 1992
venue: Journal of the ACM
field: theory
section: "2"
section_title: '*Quantified Boolean Formulas*'
tag: 052F
kind: section
lang: en
source: http://crypto.cs.mcgill.ca/~crepeau/COMP647/2007/
pdf_sha256: 64e55264e8386142cd8821ddccb435579ecd13a50658047d488011145d5a405f
pdf_pages: 2-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 943e36fcbafa593059cea4c49ff1bf06563c71efa4c6113a492cdce4b62656c1
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The class of quantified Boolean formulas (QBF) is defined as the closure of the set of Boolean variables $x_i$ and their negations $\bar{x}_i$ under the operations $\land$ (and), $\lor$ (or), $\forall x_i$ (universal quantification), and $\exists x_i$ (existential quantification). These operations can be mixed in any order, and in particular we do not require that all the quantifiers appear in a leftmost prefix. For the sake of convenience, we add the boolean equality operation, denote vectors of boolean variables by $X_i$, and extend the operations $=, \forall, \exists$ from single variables $x_i$ to vectors of variables $X_i$ in the obvious way.

A QBF in which all the variables are quantified is called *closed*, and can be evaluated to either $T$ (true) or $F$ (false). An *open* QBF with $k > 0$ free variables can be interpreted as a boolean function from $\{T, F\}^k$ to $\{T, F\}$.

The interactive proofs presented in this paper can only handle QBFs of a special type:

*Definition.* A closed QBF is called *simple* if in the given syntactic representation every occurrence of each variable is separated from its point of quantification by at most one universal quantifier (and arbitrarily many other symbols).

*Example.* $\forall x_1 \forall x_2 \exists x_3 [((x_1 \lor x_2) \land \forall x_4 (x_2 \land x_3 \land x_4))]$ is simple, since:
(1) $x_1$ is used once, and only $\forall x_2$ separates its point of quantification from its point of use,
(2) $x_2$ is used twice; its first use is not separated from its point of quantification by any universal quantifiers, whereas its second use is separated only by $\forall x_4$,
(3) $x_3$ is used once, and separated only by $\forall x_4$,
(4) $x_4$ is used once, and not separated by any universal quantifiers.

*Example.* $\forall x_1 \forall x_2 [(x_1 \land x_2) \land \forall x_3 (\bar{x}_1 \land x_3)]$ is not simple, since the second occurrence of $x_1$ (which is negated) is separated from its point of quantification by both $\forall x_2$ and $\forall x_3$.

The notion of simple QBFs seems to be quite restrictive. However, we can prove:

**Theorem 1.** *Every QBF of size n can be transformed into an equivalent simple QBF whose size is polynomial in n.* {#shamir-1992-ippspace-thm-1 .statement tag=0530}

**Proof.** To turn a given QBF into a simple QBF, we completely rename all the Boolean variables after each universal quantifier, by introducing new existentially quantified Boolean variables $x_i^j$ to denote the $j$th name of the $i$th variable, and equating each $x_i^j$ with its previous name $x_i^{j-1}$. Consider, for example, the QBF

$$
\exists x_1 \forall x_2 \exists x_3 \forall x_4 \exists x_5 \cdots Q(x_1, x_2, \ldots).
$$

in which $Q$ is quantifier free. The transformed QBF is:

$$
\exists x_1^0 \forall x_2^0 \exists x_1^1 (x_1^1 = x_1^0) \land \exists x_3^0 \forall x_4^0 \exists x_1^2 \exists x_2^1 \exists x_3^1 \\
(x_1^2 = x_1^1) \land (x_2^1 = x_2^0) \land (x_3^1 = x_3^0) \land \exists x_5^0 \cdots Q(x_1^{j_1}, x_2^{j_2}, \ldots)
$$

where $x_{i'}^{j'}$ is the last name given to the initial boolean variable $x_i^0$. This QBF is simple by definition, and contains a quadratic number of variables (compared to the original QBF). □
