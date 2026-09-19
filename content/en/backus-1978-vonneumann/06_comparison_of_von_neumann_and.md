---
paper: backus-1978-vonneumann
title: Can Programming Be Liberated from the von Neumann Style? A Functional Style and Its Algebra of Programs
authors:
  - John Backus
year: 1978
venue: Communications of the ACM (Turing Award lecture)
field: languages
section: "5"
section_title: Comparison of von Neumann and Functional Programs
tag: "0561"
kind: section
lang: en
source: https://www.cs.cmu.edu/~crary/819-f09/Backus78.pdf
pdf_sha256: 2e412a7986c7fd1bdd060d90d035faa9ecc8a29675f99206c243da90954ca423
pdf_pages: 4-5
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 10d815e75480061a272c135b6f4a1f36c49d2929f08bef42e4774a6118d70245
edited: true
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

To get a more detailed picture of some of the defects of von Neumann languages, let us compare a conventional program for inner product with a functional one written in a simple language to be detailed further on.

### 5.1 A von Neumann Program for Inner Product {#backus-1978-vonneumann-s5-1 .section tag=0562}

```text
c = 0
for i := 1 step 1 until n do
    c := c + a[i]×b[i]
```

Several properties of this program are worth noting:
a) Its statements operate on an invisible “state” according to complex rules.
b) It is not hierarchical. Except for the right side of the assignment statement, it does not construct complex entities from simpler ones. (Larger programs, however, often do.)
c) It is dynamic and repetitive. One must mentally execute it to understand it.
d) It computes word-at-a-time by repetition (of the assignment) and by modification (of variable i).
e) Part of the data, n, is in the program; thus it lacks generality and works only for vectors of length n.
f) It names its arguments; it can only be used for vectors a and b. To become general, it requires a procedure declaration. These involve complex issues (e.g., call-by-name versus call-by-value).
g) Its “housekeeping” operations are represented by symbols in scattered places (in the for statement and the subscripts in the assignment). This makes it impossible to consolidate housekeeping operations, the most common of all, into single, powerful, widely useful operators. Thus in programming those operations one must always start again at square one, writing “for i := ...” and “for j := ...” followed by assignment statements sprinkled with i’s and j’s.

### 5.2 A Functional Program for Inner Product {#backus-1978-vonneumann-s5-2 .section tag=0563}

Def Innerproduct
    ≡ (Insert +)∘(ApplyToAll ×)∘Transpose

Or, in abbreviated form:

Def IP ≡ (/+)∘(α×)∘Trans.

Composition (∘), Insert (/), and ApplyToAll (α) are functional forms that combine existing functions to form new ones. Thus f∘g is the function obtained by applying first g and then f, and αf is the function obtained by applying f to every member of the argument. If we write f:x for the result of applying f to the object x, then we can explain each step in evaluating Innerproduct applied to the pair of vectors <<1, 2, 3>, <6, 5, 4>> as follows:

```text
IP:<<1,2,3>, <6,5,4>> =
Definition of IP      ⇒ (/+)∘(α×)∘Trans: <<1,2,3>, <6,5,4>>
Effect of composition, ∘   ⇒ (/+):((α×):(Trans:
                                    <<1,2,3>, <6,5,4>>))
```

Applying Transpose      $\Rightarrow (/+):((\alpha\times): <<1,6>, <2,5>, <3,4>>)$
Effect of ApplyToAll, $\alpha$    $\Rightarrow (/+): <\times: <1,6>, \times: <2,5>, \times: <3,4>>$
Applying $\times$    $\Rightarrow (/+): <6,10,12>$
Effect of Insert, /    $\Rightarrow +: <6, +: <10,12>>$
Applying +    $\Rightarrow +: <6,22>$
Applying + again    $\Rightarrow 28$

Let us compare the properties of this program with those of the von Neumann program.

a) It operates only on its arguments. There are no hidden states or complex transition rules. There are only two kinds of rules, one for applying a function to its argument, the other for obtaining the function denoted by a functional form such as composition, $f \circ g$, or ApplyToAll, $\alpha f$, when one knows the functions $f$ and $g$, the parameters of the forms.

b) It is hierarchical, being built from three simpler functions ($+,\times,\mathrm{Trans}$) and three functional forms $f \circ g$, $\alpha f$, and $/f$.

c) It is static and nonrepetitive, in the sense that its structure is helpful in understanding it without mentally executing it. For example, if one understands the action of the forms $f \circ g$ and $\alpha f$, and of the functions $\times$ and Trans, then one understands the action of $\alpha \times$ and of $(\alpha \times) \circ \mathrm{Trans}$, and so on.

d) It operates on whole conceptual units, not words; it has three steps; no step is repeated.

e) It incorporates no data; it is completely general; it works for any pair of conformable vectors.

f) It does not name its arguments; it can be applied to any pair of vectors without any procedure declaration or complex substitution rules.

g) It employs housekeeping forms and functions that are generally useful in many other programs; in fact, only + and $\times$ are not concerned with housekeeping. These forms and functions can combine with others to create higher level housekeeping operators.

Section 14 sketches a kind of system designed to make the above functional style of programming available in a history-sensitive system with a simple framework, but much work remains to be done before the above applicative style can become the basis for elegant and practical programming languages. For the present, the above comparison exhibits a number of serious flaws in von Neumann programming languages and can serve as a starting point in an effort to account for their present fat and flabby condition.
