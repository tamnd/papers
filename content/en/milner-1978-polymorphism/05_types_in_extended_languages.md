---
paper: milner-1978-polymorphism
title: A Theory of Type Polymorphism in Programming
authors:
  - Robin Milner
year: 1978
venue: Journal of Computer and System Sciences
field: languages
section: "5"
section_title: Types in Extended Languages
tag: 055E
kind: section
lang: en
source: https://doi.org/10.1016/0022-0000(78)90014-4
pdf_sha256: a55f1fb81848085165c55a73c33f28b5d25f3b7bdcfa782c462af7997faad6bc
pdf_pages: 26-28
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: f63e81445e37334346f26e66bb2c81e0af0d3e1448088b47cb36cfddf4ad2c34
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

We now consider some extensions of our language, and how our results may be strengthened to apply to them.

(1) As we said in the introduction, the addition of extra (primitive) type operators such as $\times$ (Cartesian product), $+$ (disjoint sum) and list (list forming), causes no difficulty. Together with $\rightarrow$, these are the primitive type operators in the language ML. For $\times$ one has the standard polymorphic functions pair: $\alpha \rightarrow \beta \rightarrow (\alpha \times \beta)$    (one could add the syntax $(e, e')$ for pair $(e)(e')$),
fst: $\alpha \times \beta \rightarrow \alpha$,
snd: $\alpha \times \beta \rightarrow \beta$.

For $+$, one has inl: $\alpha \rightarrow \alpha + \beta$,
outl: $\alpha + \beta \rightarrow \alpha$,
isl: $\alpha + \beta \rightarrow bool$, inr: $\beta \rightarrow \alpha + \beta$    (left and right injections),
outr: $\alpha + \beta \rightarrow \beta$    (left and right projections),
isr: $\alpha + \beta \rightarrow bool$    (left and right discriminators) with natural interpretations. For list, one has the standard list-processing functions mentioned in Section 2. Notice that all members of a list must have the same type.

With appropriate adjustment to the semantic domains, the Semantic Soundness Theorem extends naturally; the Syntactic Soundness Theorem goes through virtually without change.

(2) Next, we consider assignable variables and assignments. One way (used in ML) of adding these is to allow the assignment expression form "$x := e$" (whose value is the value of $e$), and the expression form "$letref\ x = e\ in\ e'$" to declare an assignable variable, initialized to the value of $e$. The first effect of these additions is a major change in the semantic domains, since now expressions may have side effects. Although we believe that a Semantic Soundness Theorem may be proved, it appears to be a cumbersome task. The reason for the difficulty is illustrated by considering

$$
\lambda x \cdot (y := x)
$$

which is an identity function with a side effect. To say that it has type $\alpha \rightarrow \alpha$, meaning that whenever it is given an argument of type $\mu$ it gives a result of type $\mu$, takes no account of the side effect on $y$. What is required is a more careful definition (in terms of the semantic domains) of what such functional types mean, which takes side effects into account.

By contrast, it is easy enough to give well-typing rules for the two new kinds of expression. We would extend the definition of wt by the following clauses:

(i) (c) If letref $x_{\tau}$ is active in a standard prefix $\bar{p}$, then $\bar{p} \mid x_{\tau}$ is wt. (Thus, all letref-bound occurrences of $x$ must have the same type).

(vii) $\bar{p} | (x_\rho := \bar{e}_\sigma)_\tau$ is wt iff $\bar{p} | \bar{e}$ is wt, and letref $x_\rho$ is active in $\bar{p}$, and $\rho = \sigma = \tau$.
(viii) $\bar{p} | (letref\ x_\rho = \bar{e}_\rho\ in\ \bar{e}'_\sigma)_\tau$ is wt iff $\bar{p} | \bar{e}$ and $\bar{p} \cdot letref\ x_\rho | \bar{e}'$ are wt, and $\sigma = \tau$.

It is a routine matter to extend the algorithm $\mathcal{W}$ and the Syntactic Soundness Theorem to handle these clauses. But returning again to semantic considerations, there is a problem concerned with nonlocal assignments within $\lambda$-abstractions (procedures). Consider

$$
let\ g = (letref\ y = nil\ in\ \lambda z \cdot y := cons(z, y))
$$

which sets up $y$ as a hidden (own) variable for the function $g$. With our rules, $g$ obtains generic type $\alpha \to \alpha\ list$. Remembering that the value of an assignment is the value assigned, each call of $g$ augments the hidden $y$, returning the augmented list as value. Now since $\alpha$ is generic, the expressions

$$
g(2), \qquad g(true)
$$

are both admissible within the scope of $g$, with types *int list* and *bool list*, respectively. But if they are evaluated in this order, the value of the second expression is a list whose two members are *true* and 2; it is *not* a list of Boolean values!

There are at least two possible solutions to this dilemma. One is to decree that in such a situation $\alpha$ is not a generic type variable. Another, which we adopt in ML, is to forbid nonlocal assignments to *polymorphic* assignable variables within $\lambda$-abstractions (procedures). Polymorphic assignable variables are still useful, for example, in programming iterations (*while* statements) which themselves can be given simple wt rules.

I believe that the second solution, even slightly relaxed, admits a Semantic Soundness Theorem. The details, however, are unattractive, and I have been discouraged (particularly after a useful discussion with John Reynolds) from attempting to complete the proof. What is rather needed is a language design which pays more respect to side effects; one approach might be to modify PASCAL by requiring that all variables assigned in a procedure be listed as output parameters of the procedure. But how to combine this with the rather useful properties of *own* variables is, as far as I know, an open problem in language design, and a good solution would be a valuable step forward. For a recent promising attempt to control side effects see Reynolds [13].

(3) To complete the list of nontrivial extensions which we have included in ML, consider the declaration (possibly recursive) of a new type operator in terms of old ones. Such a declaration may have nonglobal scope. If it is also accompanied by the declaration of a set of functions over the new type operator, and the explicit definition of the type operator is only available in defining the set of functions (not within the whole scope of the new type operator), one has a version of what is currently called *abstract* type. In ML, we would define the class of binary trees whose tips are labeled by objects of arbitrary type as follows, using the type variable $\alpha$ to stand for the type of tip labels:

$$
absrectype\ \alpha\ bitree = \alpha + (\alpha\ bitree \times \alpha\ bitree) \\
with\ sons(t) = \cdots \\
and\ maketree(t, t') = \cdots \\
and\ tiptree(a) = \cdots
$$

in which only the omitted defining expressions are given access to the representation of bitrees. The defined functions are polymorphic, with generic types

$$
\alpha \text{ bitree} \rightarrow (\alpha \text{ bitree})^2,\quad (\alpha \text{ bitree})^2 \rightarrow \alpha \text{ bitree},\quad \alpha \rightarrow \alpha \text{ bitree}.
$$

For full details of this construct, see [2]; we owe the construct partly to Lockwood Morris and to discussion with Jerry Schwarz. In this case the wt rules are also rather easy; we have not checked syntactic and semantic soundness, but suspect that there should be no great difficulty.

(4) Two features which contribute a kind of polymorphism have been completely ignored so far. The first is *coercions*. The expression $x := 42$, where $x$ is a *real* assignable variable, is ill typed for us. However, there is no barrier to having the type checker report such instances of ill typing and allowing the compiler to receive the report and insert a coercion to rectify it.

The second feature is to allow certain procedures—either standard or user defined—to possess more than one type. We may wish “+” to possess $int^2 \rightarrow int$ and $real^2 \rightarrow real$, without of course possessing $\alpha^2 \rightarrow \alpha$ (which is the least general polytype having the two given types as instances). While we have not investigated the question, there appears to be a good possibility of superposing this feature upon our discipline.
