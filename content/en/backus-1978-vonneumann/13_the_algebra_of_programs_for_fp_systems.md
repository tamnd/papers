---
paper: backus-1978-vonneumann
title: Can Programming Be Liberated from the von Neumann Style? A Functional Style and Its Algebra of Programs
authors:
  - John Backus
year: 1978
venue: Communications of the ACM (Turing Award lecture)
field: languages
section: "12"
section_title: The Algebra of Programs for FP Systems
tag: 056C
kind: section
lang: en
source: https://www.cs.cmu.edu/~crary/819-f09/Backus78.pdf
pdf_sha256: 2e412a7986c7fd1bdd060d90d035faa9ecc8a29675f99206c243da90954ca423
pdf_pages: 12-19
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: b27df568a60a2ab8421d4df997e0b53759fe2d1eb80b436e3a9cfeae9c6ec0cb
edited: true
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

### 12.1 Introduction {#backus-1978-vonneumann-s12-1 .section tag=056D}

The algebra of the programs described below is the work of an amateur in algebra, and I want to show that it is a game amateurs can profitably play and enjoy, a game that does not require a deep understanding of logic and mathematics. In spite of its simplicity, it can help one to understand and prove things about programs in a systematic, rather mechanical way.

So far, proving a program correct requires knowledge of some moderately heavy topics in mathematics and logic: properties of complete partially ordered sets, continuous functions, least fixed points of functionals, the first-order predicate calculus, predicate transformers, weakest preconditions, to mention a few topics in a few approaches to proving programs correct. These topics have been very useful for professionals who make it their business to devise proof techniques; they have published a lot of beautiful work on this subject, starting with the work of McCarthy and Floyd, and, more recently, that of Burstall, Dijkstra, Manna and his associates, Milner, Morris, Reynolds, and many others. Much of this work is based on the foundations laid down by Dana Scott (denotational semantics) and C. A. R. Hoare (axiomatic semantics). But its theoretical level places it beyond the scope of most amateurs who work outside of this specialized field.

If the average programmer is to prove his programs correct, he will need much simpler techniques than those the professionals have so far put forward. The algebra of programs below may be one starting point for such a proof discipline and, coupled with current work on algebraic manipulation, it may also help provide a basis for automating some of that discipline.

One advantage of this algebra over other proof techniques is that the programmer can use his programming language as the language for deriving proofs, rather than having to state proofs in a separate logical system that merely talks about his programs.

At the heart of the algebra of programs are laws and theorems that state that one function expression is the same as another. Thus the law $[f,g] \circ h \equiv [f \circ h, g \circ h]$ says that the construction of $f$ and $g$ (composed with $h$) is the same function as the construction of ($f$ composed with $h$) and ($g$ composed with $h$) no matter what the functions $f$, $g$, and $h$ are. Such laws are easy to understand, easy to justify, and easy and powerful to use. However, we also wish to use such laws to solve equations in which an “unknown” function appears on both sides of the equation. The problem is that if $f$ satisfies some such equation, it will often happen that some extension $f'$ of $f$ will also satisfy the same equation. Thus, to give a unique meaning to solutions of such equations, we shall require a foundation for the algebra of programs (which uses Scott’s notion of least fixed points of continuous functionals) to assure us that solutions obtained by algebraic manipulation are indeed least, and hence unique, solutions.

Our goal is to develop a foundation for the algebra of programs that disposes of the theoretical issues, so that a programmer can use simple algebraic laws and one or two theorems from the foundations to solve problems and create proofs in the same mechanical style we use to solve high-school algebra problems, and so that he can do so without knowing anything about least fixed points or predicate transformers.

One particular foundational problem arises: given equations of the form

$$
f \equiv p_0 \rightarrow q_0; ... ; p_i \rightarrow q_i; E_i(f),
$$

where the $p_i$’s and $q_i$’s are functions not involving $f$ and $E_i(f)$ is a function expression involving $f$, the laws of the algebra will often permit the formal “extension” of this equation by one more “clause” by deriving

$$
E_i(f) \equiv p_{i+1} \rightarrow q_{i+1}; E_{i+1}(f)
$$

which, by replacing $E_i(f)$ in (1) by the right side of (2), yields

$$
f \equiv p_0 \rightarrow q_0; ... ; p_{i+1} \rightarrow q_{i+1}; E_{i+1}(f).
$$

This formal extension may go on without limit. One question the foundations must then answer is: when can the least $f$ satisfying (1) be represented by the infinite expansion

$$
f \equiv p_0 \rightarrow q_0; ... ; p_n \rightarrow q_n; ...
$$

in which the final clause involving $f$ has been dropped, so that we now have a solution whose right side is free of f’s? Such solutions are helpful in two ways: first, they give proofs of “termination” in the sense that (4) means that f:x is defined if and only if there is an n such that, for every i less than n, p_i:x = F and p_n:x = T and q_n:x is defined. Second, (4) gives a case-by-case description of f that can often clarify its behavior.

The foundations for the algebra given in a subsequent section are a modest start toward the goal stated above. For a limited class of equations its “linear expansion theorem” gives a useful answer as to when one can go from indefinitely extendable equations like (1) to infinite expansions like (4). For a larger class of equations, a more general “expansion theorem” gives a less helpful answer to similar questions. Hopefully, more powerful theorems covering additional classes of equations can be found. But for the present, one need only know the conclusions of these two simple foundational theorems in order to follow the theorems and examples appearing in this section.

The results of the foundations subsection are summarized in a separate, earlier subsection titled “expansion theorems,” without reference to fixed point concepts. The foundations subsection itself is placed later where it can be skipped by readers who do not want to go into that subject.

### 12.2 Some Laws of the Algebra of Programs {#backus-1978-vonneumann-s12-2 .section tag=056E}

In the algebra of programs for an FP system variables range over the set of functions of the system. The “operations” of the algebra are the functional forms of the system. Thus, for example, [f,g]o h is an expression of the algebra for the FP system described above, in which f, g, and h are variables denoting arbitrary functions of that system. And

[f,g]o h ≡ [f o h, g o h] is a law of the algebra which says that, whatever functions one chooses for f, g, and h, the function on the left is the same as that on the right. Thus this algebraic law is merely a restatement of the following proposition about any FP system that includes the functional forms [f,g] and f o g:

PROPOSITION: For all functions f, g, and h and all objects x, ([f,g]o h):x ≡ [f o h, g o h]:x.
PROOF:
([f,g]o h):x = [f,g]: (h:x)
    by definition of composition
    = <f:(h:x), g:(h:x)>
        by definition of construction
    = <(f o h):x, (g o h):x>
        by definition of composition
    = [f o h, g o h]:x
        by definition of construction □

Some laws have a domain smaller than the domain of all objects. Thus 1°[f,g] ≡ f does not hold for objects x such that g:x = ⊥. We write defined°g →→ 1° [f,g] ≡ f to indicate that the law (or theorem) on the right holds within the domain of objects x for which defined°g:x = T. Where

Def defined ≡ $\bar{T}$ i.e. defined:x ≡ x=⊥ → ⊥; T. In general we shall write a *qualified functional equation*:

p →→ f ≡ g to mean that, for any object x, whenever p:x = T, then f:x = g:x.

Ordinary algebra concerns itself with two operations, addition and multiplication; it needs few laws. The algebra of programs is concerned with more operations (functional forms) and therefore needs more laws.

Each of the following laws requires a corresponding proposition to validate it. The interested reader will find most proofs of such propositions easy (two are given below). We first define the usual ordering on functions and equivalence in terms of this ordering:

DEFINITION f≤g iff for all objects x, either f:x = ⊥, or f:x = g:x.
DEFINITION f ≡ g iff f≤g and g≤f.

It is easy to verify that ≤ is a partial ordering, that f≤g means g is an extension of f, and that f≡g iff f:x = g:x for all objects x. We now give a list of algebraic laws organized by the two principal functional forms involved.

I  Composition and construction

```text
I.1   [f_1, ..., f_n]°g ≡ [f_1°g, ..., f_n°g]
I.2   αf°[g_1, ..., g_n] ≡ [f°g_1, ..., f°g_n]
I.3   /f°[g_1, ..., g_n]
      ≡ f°[g_1, /f°[g_2, ..., g_n]]   when n≥2
      ≡ f°[g_1, f°[g_2, ..., f°[g_{n-1}, g_n]...]]
/f°[g] ≡ g
I.4   f°[x,g] ≡ (bu f x)°g
I.5   1° [f_1, ..., f_n] ≤f_1
      s°[f_1, ..., f_s, ..., f_n] ≤f_s for any selector s, s≤n
      defined°f_i (for all i≠s, 1≤i≤n) →→
      s°[f_1, ..., f_n] ≡ f_s

I.5.1   [f_1°1, ..., f_n°n]°[g_1, ..., g_n] ≡ [f_1°g_1, ..., f_n°g_n]
I.6   tl°[f_1] ≤ φ and
      tl°[f_1, ..., f_n] ≤ [f_2, ..., f_n]   for n≥2
      defined°f_1 →→ tl°[f_1] ≡ φ
      and tl°[f_1, ..., f_n] ≡ [f_2, ..., f_n] for n≥2
```
I.7   distl°[f, [g_1, ..., g_n]] ≡ [[f,g_1], ..., [f,g_n]]
      defined°f →→ distl°[f,φ] ≡φ
      The analogous law holds for distr.
I.8   apndl°[f, [g_1, ..., g_n]] ≡ [f,g_1, ..., g_n]
      null°g →→ apndl°[f,g] ≡ [f]
And so on for apndr, reverse, rotl, etc.
I.9   [... , 1, ...] ≡ 1
I.10  apndl° [f°g, αf°h] ≡ αf°apndl°[g,h]
I.11  pair & not°null°1 →→
      apndl°[[1°1,2], distr°[tl°1,2]] ≡ distr

Where $f \& g \equiv \mathrm{and}^{\circ}[f,g];$
pair $\equiv \mathrm{atom} \rightarrow \bar{F}; \mathrm{eq}^{\circ}[\mathrm{length},\bar{2}]$

II Composition and condition (right associated parentheses omitted) (Law II.2 is noted in Manna et al. [16], p. 493.)
II.1 $(p \rightarrow f; g)^{\circ}h \equiv p^{\circ}h \rightarrow f^{\circ}h; g^{\circ}h$
II.2 $h^{\circ}(p \rightarrow f; g) \equiv p \rightarrow h^{\circ}f; h^{\circ}g$
II.3 $\mathrm{or}^{\circ}[q,\mathrm{not}^{\circ}q] \rightarrow \rightarrow \mathrm{and}^{\circ}[p,q] \rightarrow f;$
    $\mathrm{and}^{\circ}[p,\mathrm{not}^{\circ}q] \rightarrow g; h \equiv p \rightarrow (q \rightarrow f; g); h$
II.3.1 $p \rightarrow (p \rightarrow f; g); h \equiv p \rightarrow f; h$
III Composition and miscellaneous
III.1 $\bar{x}^{\circ}f \leq \bar{x}$
    defined$f \rightarrow \rightarrow \bar{x}^{\circ}f \equiv \bar{x}$
III.1.1 $\bar{1}^{\circ}f \equiv f^{\circ}\bar{1} \equiv \bar{1}$
III.2 $f^{\circ}\mathrm{id} \equiv \mathrm{id}^{\circ}f \equiv f$
III.3 pair $\rightarrow \rightarrow 1^{\circ}\mathrm{distr} \equiv [1 \circ 1,2]$ also:
    pair $\rightarrow \rightarrow 1^{\circ}\mathrm{tl} \equiv 2$ etc.
III.4 $\alpha(f^{\circ}g) \equiv \alpha f^{\circ} \alpha g$
III.5 $\mathrm{null}^{\circ}g \rightarrow \rightarrow \alpha f^{\circ}g \equiv \bar{\phi}$

IV Condition and construction

IV.1 $[f_1, ..., (p \rightarrow g; h), ..., f_n]$
    $\equiv p \rightarrow [f_1, ..., g, ..., f_n]; [f_1, ..., h, ..., f_n]$
IV.1.1 $[f_1, ..., (p_1 \rightarrow g_1; ... ; p_n \rightarrow g_n; h), ..., f_m]$
    $\equiv p_1 \rightarrow [f_1, ..., g_1, ..., f_m];$
    ... ; $p_n \rightarrow [f_1, ..., g_n, ..., f_m]; [f_1, ..., h, ..., f_m]$

This concludes the present list of algebraic laws; it is by no means exhaustive, there are many others.

Proof of two laws
We give the proofs of validating propositions for laws I.10 and I.11, which are slightly more involved than most of the others.

PROPOSITION 1 apndl $\circ [f^{\circ}g, \alpha f^{\circ}h] \equiv \alpha f^{\circ} \mathrm{apndl} \circ [g,h]$
Proof. We show that, for every object $x$, both of the above functions yield the same result.
Case 1. $h:x$ is neither a sequence nor $\phi$.
Then both sides yield $\bot$ when applied to $x$.
Case 2. $h:x = \phi$. Then
apndl$[f^{\circ}g, \alpha f^{\circ}h]$: $x$
    = apndl: $<f^{\circ}g:x, \phi> = <f:(g:x)>$
$\alpha f^{\circ} \mathrm{apndl} \circ [g,h]$: $x$
    = $\alpha f^{\circ} \mathrm{apndl}: <g:x, \phi> = \alpha f:<g:x>$
    = $<f:(g:x)>$
Case 3. $h:x = <y_1, ..., y_n>$. Then
apndl$[f^{\circ}g, \alpha f^{\circ}h]$: $x$
    = apndl: $<f^{\circ}g:x, \alpha f: <y_1, ..., y_n>>$
    = $<f:(g:x), f:y_1, ..., f:y_n>$
$\alpha f^{\circ} \mathrm{apndl} \circ [g,h]$: $x$
    = $\alpha f^{\circ} \mathrm{apndl}: <g:x, <y_1, ..., y_n>>$
    = $\alpha f:<g:x, y_1, ..., y_n>$

PROPOSITION 2

Pair & not\circ null\circ 1 \rightarrow \rightarrow
    apndl\circ[[1^2, 2], distr\circ[t1\circ 1, 2]] \equiv distr
where $f \& g$ is the function: and\circ[f, g], and $f^2 \equiv f\circ f$.
Proof. We show that both sides produce the same result when applied to any pair $<x,y>$, where $x \neq \phi$, as per the stated qualification.
Case 1. $x$ is an atom or $\bot$. Then distr: $<x,y> = \bot$, since $x \neq \phi$. The left side also yields $\bot$ when applied to $<x,y>$, since tl\circ 1:<x,y> = $\bot$ and all functions are $\bot$-preserving.
Case 2. $x = <x_1, ..., x_n>$. Then
    apndl\circ[[1^2, 2], distr\circ[t1\circ 1, 2]]:<x, y>
        = apndl: <<1:x, y>, distr: <tl:x, y>>
        = apndl: <<x_1,y>, \phi> = <<x_1,y>>> \text{ if tl:x = } \phi
        = apndl: <<x_1,y>, <<x_2,y>, ..., <x_n,y>>> \text{ if tl:x } \neq \phi
        = <<x_1,y>, ..., <x_n,y>>
        = distr: <x,y>

12.3 Example: Equivalence of Two Matrix Multiplication Programs
We have seen earlier the matrix multiplication program:

Def MM $\equiv \alpha \alpha \mathrm{IP} \circ \alpha \mathrm{distl} \circ \mathrm{distr} \circ [1, \mathrm{trans} \circ 2]$.

We shall now show that its initial segment, MM', where

Def MM' $\equiv \alpha \alpha \mathrm{IP} \circ \alpha \mathrm{distl} \circ \mathrm{distr}$, can be defined recursively. (MM' "multiplies" a pair of matrices after the second matrix has been transposed. Note that MM', unlike MM, gives $\bot$ for all arguments that are not pairs.) That is, we shall show that MM' satisfies the following equation which recursively defines the same function (on pairs):

$f \equiv \mathrm{null}^{\circ}1 \rightarrow \bar{\phi}; \mathrm{apndl}^{\circ}[\alpha \mathrm{IP}^{\circ} \mathrm{distl}^{\circ}[1 \circ 1, 2], f^{\circ}[tl \circ 1, 2]]$.

Our proof will take the form of showing that the following function, R,

Def R $\equiv \mathrm{null}^{\circ}1 \rightarrow \bar{\phi};$
    apndl\circ[\alpha \mathrm{IP}^{\circ} \mathrm{distl}^{\circ}[1 \circ 1, 2], \mathrm{MM}'^{\circ}[tl \circ 1, 2]] is, for all pairs $<x,y>$, the same function as MM'. R "multiplies" two matrices, when the first has more than zero rows, by computing the first row of the "product" (with $\alpha \mathrm{IP}^{\circ} \mathrm{distl}^{\circ}[1 \circ 1, 2]$) and adjoining it to the "product" of the tail of the first matrix and the second matrix. Thus the theorem we want is pair $\rightarrow \rightarrow \mathrm{MM}' \equiv \mathrm{R}$, from which the following is immediate:

MM $\equiv \mathrm{MM}' \circ [1, \mathrm{trans} \circ 2] \equiv \mathrm{R} \circ [1, \mathrm{trans} \circ 2]$;

where

Def pair $\equiv \mathrm{atom} \rightarrow \bar{F}; \mathrm{eq}^{\circ}[\mathrm{length}, \bar{2}]$.

THEOREM: pair $\rightarrow \rightarrow \mathrm{MM}' \equiv \mathrm{R}$ where

Def MM' ≡ ααIP ∘ αdistl ∘ distr
Def R ≡ null∘1 → φ;
    apndl∘[αIP∘distl∘[1^2, 2], MM'∘[tl∘1, 2]]

Proof.
Case 1. pair & null∘1 →→ MM' ≡ R.
pair & null∘1 →→ R ≡ φ̄ by def of R
pair & null∘1 →→ MM' ≡ φ̄
    since distr: <φ,x> = φ by def of distr
and αf:φ = φ by def of Apply to all.
And so: ααIP ∘ αdistl ∘ distr: <φ,x> = φ.
Thus pair & null∘1 →→ MM' ≡ R.
Case 2. pair & not∘null∘1 →→ MM' ≡ R.
pair & not∘null∘1 →→ R ≡ R',
    by def of R and R', where
Def R' ≡ apndl∘[αIP∘distl∘[1^2, 2], MM'∘[tl∘1, 2]].
We note that
R' ≡ apndl∘[f∘g, αf∘h]
where
f ≡ αIP∘distl
g ≡ [1^2, 2]
h ≡ distr∘[tl∘1, 2]
αf ≡ α(αIP∘distl) ≡ ααIP∘αdistl (by III.4).
Thus, by I.10,
R' ≡ αf∘apndl∘[g,h].
Now apndl∘[g,h] ≡ apndl∘[[1^2, 2], distr∘[tl∘1, 2]],
thus, by I.11,
pair & not∘null∘1 →→ apndl∘[g,h] ≡ distr.
And so we have, by (1), (2), (3) and (4),
pair & not∘null∘1 →→ R ≡ R'
    ≡ αf∘distr ≡ ααIP∘αdistl∘distr ≡ MM'.
Case 1 and Case 2 together prove the theorem. □

12.4 Expansion Theorems

In the following subsections we shall be “solving” some simple equations (where by a “solution” we shall mean the “least” function which satisfies an equation). To do so we shall need the following notions and results drawn from the later subsection on foundations of the algebra, where their proofs appear.

### 12.4.1 Expansion. Suppose we have an equation of the form {#backus-1978-vonneumann-s12-4-1 .section tag=056F}

$$
f \equiv \mathrm{E}(f)
$$

(E1)
where E(f) is an expression involving f. Suppose further that there is an infinite sequence of functions f_i for i = 0, 1, 2, ..., each having the following form:

$$
f_0 \equiv \bot \\
f_{i+1} \equiv p_0 \rightarrow q_0; ... ; p_i \rightarrow q_i; \bot
$$

(E2) where the p_i's and q_i's are particular functions, so that E has the property:

$$
\mathrm{E}(f_i) \equiv f_{i+1} \text{ for } i = 0, 1, 2, ...
$$

(E3)

Then we say that E is *expansive* and has the f_i's as *approximating functions*.

If E is expansive and has approximating functions as in (E2), and if f is the solution of (E1), then f can be written as the infinite expansion

$$
f \equiv p_0 \rightarrow q_0; ... ; p_n \rightarrow q_n; ...
$$

(E4)
meaning that, for any x, f:x ≠ ⊥ iff there is an n ≥ 0 such that (a) p_i:x = F for all i < n, and (b) p_n:x = T, and (c) q_n:x ≠ ⊥. When f:x ≠ ⊥, then f:x = q_n:x for this n. (The foregoing is a consequence of the “expansion theorem”.)
12.4.2 Linear expansion. A more helpful tool for solving some equations applies when, for any function h,

$$
\mathrm{E}(h) \equiv p_0 \rightarrow q_0; \mathrm{E}_1(h)
$$

(LE1)
and there exist p_i and q_i such that

$$
\mathrm{E}_1(p_i \rightarrow q_i; h) \equiv p_{i+1} \rightarrow q_{i+1}; \mathrm{E}_1(h)
$$

for i = 0, 1, 2, ... (LE2)
and

$$
\mathrm{E}_1(\bot) \equiv \bot.
$$

(LE3)
Under the above conditions E is said to be *linearly expansive*. If so, and f is the solution of

$$
f \equiv \mathrm{E}(f)
$$

(LE4)
then E is expansive and f can again be written as the infinite expansion

$$
f \equiv p_0 \rightarrow q_0; ... ; p_n \rightarrow q_n; ...
$$

(LE5)
using the p_i's and q_i's generated by (LE1) and (LE2).

Although the p_i's and q_i's of (E4) or (LE5) are not unique for a given function, it may be possible to find additional constraints which would make them so, in which case the expansion (LE5) would comprise a canonical form for a function. Even without uniqueness these expansions often permit one to prove the equivalence of two different function expressions, and they often clarify a function’s behavior.

12.5 A Recursion Theorem

Using three of the above laws and linear expansion, one can prove the following theorem of moderate generality that gives a clarifying expansion for many recursively defined functions.

Recursion theorem: Let f be a solution of

$$
f \equiv p \rightarrow g; Q(f)
$$

(1)
where

$$
Q(k) \equiv h \circ [i, k \circ j] \text{ for any function } k
$$

(2)
and p, g, h, i, j are any given functions, then f ≡ p → g; p°j → Q(g); ... ; p°j^n → Q^n(g); ...      (3)
(where Q^n(g) is h°[i, Q^{n-1}(g)°j], and j^n is j°j^{n-1} for n ≥ 2) and
Q^n(g) ≡ /h ° [i, i°j, ..., i°j^{n-1}, g°j^n].      (4)

Proof. We verify that p → g, Q(f) is linearly expansive. Let p_n, q_n and k be any functions. Then

$$
\begin{align*}
Q(p_n \rightarrow q_n; k) \\
&\equiv h°[i, (p_n \rightarrow q_n; k)°j] \quad \text{by (2)} \\
&\equiv h°[i, (p_n°j \rightarrow q_n°j; k°j)] \quad \text{by II.1} \\
&\equiv h°(p_n°j \rightarrow [i, q_n°j]; [i, k°j]) \quad \text{by IV.1} \\
&\equiv p_n°j \rightarrow h°[i, q_n°j]; h°[i, k°j] \quad \text{by II.2} \\
&\equiv p_n°j \rightarrow Q(q_n); Q(k) \quad \text{by (2)}
\end{align*}
\tag{5}
$$
{#backus-1978-vonneumann-eq-5 .equation tag=0570}

Thus if p_0 ≡ p and q_0 ≡ g, then (5) gives p_1 ≡ p°j and q_1 = Q(g) and in general gives the following functions satisfying (LE2) p_n ≡ p°j^n   and   q_n ≡ Q^n(g).      (6)

Finally,

$$
\begin{align*}
Q(\bar{I}) &\equiv h°[i, \bar{I}°j] \\
&\equiv h°[i, \bar{I}] \quad \text{by III.1.1} \\
&\equiv h°\bot \quad \text{by I.9} \\
&\equiv \bar{I} \quad \text{by III.1.1.}
\end{align*}
\tag{7}
$$
{#backus-1978-vonneumann-eq-7 .equation tag=0571}

Thus (5) and (6) verify (LE2) and (7) verifies (LE3), with E_1 ≡ Q. If we let E(f) ≡ p → g; Q(f), then we have (LE1); thus E is linearly expansive. Since f is a solution of f ≡ E(f), conclusion (3) follows from (6) and (LE5). Now

$$
\begin{align*}
Q^n(g) &\equiv h°[i, Q^{n-1}(g)°j] \\
&\equiv h°[i, h°[i°j, ..., h°[i°j^{n-1}, g°j^n] ... ]] \\
&\equiv /h°[i, i°j, ..., i°j^{n-1}, g°j^n] \quad \text{by I.1, repeatedly}
\end{align*}
\tag{8}
$$
{#backus-1978-vonneumann-eq-8 .equation tag=0572}

Result (8) is the second conclusion (4). □

12.5.1 Example: correctness proof of a recursive factorial function. Let f be a solution of f ≡ eq0 → \bar{I}; ×°[id, f°s] where

Def s ≡ −°[id, \bar{I}]   (subtract 1).

Then f satisfies the hypothesis of the recursion theorem with p ≡ eq0, g ≡ \bar{I}, h ≡ ×, i ≡ id, and j ≡ s. Therefore f ≡ eq0 → \bar{I}; ... ; eq0°s^n → Q^n(\bar{I}); ...

and

Q^n(\bar{I}) ≡ /× ° [id, id°s, ..., id°s^{n-1}, \bar{I}°s^n].

Now id°s^k ≡ s^k by III.2 and eq0°s^n →→ \bar{I}°s^n ≡ \bar{I} by III.1, since eq0°s^n:x implies defined°s^n:x; and also eq0°s^n:x ≡ eq0: (x − n) ≡ x=n. Thus if eq0°s^n: x = T, then x = n and

Q^n(\bar{I}): n = n × (n − 1) × ... × (n − (n − 1)) × (\bar{I}: (n − n)) = n!.

Using these results for \bar{I}°s^n, eq0°s^n, and Q^n(\bar{I}) in the previous expansion for f, we obtain f:x ≡ x=0 → l; ... ; x=n → n × (n − 1) × ... × 1 × 1; ...

Thus we have proved that f terminates on precisely the set of nonnegative integers and that it is the factorial function thereon.

12.6 An Iteration Theorem

This is really a corollary of the recursion theorem. It gives a simple expansion for many iterative programs.

Iteration theorem: Let f be the solution (i.e., the least solution) of f ≡ p → g; h°f°k then f ≡ p → g; p°k → h°g°k; ... ; p°k^n → h^n°g°k^n; ...

Proof. Let h' ≡ h°2, i' ≡ id, f' ≡ k, then f ≡ p → g; h'°[i', f°j'] since h°2°[id, f°k] ≡ h°f°k   by I.5 (id is defined except for ⊥, and the equation holds for ⊥). Thus the recursion theorem gives f ≡ p → g; ... ; p°k^n → Q^n(g); ...

where

Q^n(g) ≡ h°2°[id, Q^{n-1}(g)°k]
≡ h°Q^{n-1}(g)°k ≡ h^n°g°k^n
by I.5 □

12.6.1 Example: Correctness proof for an iterative factorial function. Let f be the solution of f ≡ eq0°1 → 2; f°[s°1, ×] where Def s ≡ −°[id, \bar{I}] (substract 1). We want to prove that f:<x,1> = x! iff x is a nonnegative integer. Let p ≡ eq0°1, g ≡ 2, h ≡ id, k ≡ [s°1, ×]. Then f ≡ p → g; h°f°k and so f ≡ p → g; ... ; p°k^n → g°k^n; ...

```text
by the iteration theorem, since h^n ≡ id. We want to show that pair →→ k^n ≡ [a_n, b_n] holds for every n ≥ 1, where a_n ≡ s^n°1      (3)
b_n ≡ /× ° [s^{n-1}°1, ..., s°1, 1, 2]      (4)
```

Now (2) holds for n = 1 by definition of k. We assume it holds for some n ≥ 1 and prove it then holds for n + 1. Now pair →→ k^{n+1} ≡ k°k^n ≡ [s°1, ×]°[a_n, b_n]      (5) since (2) holds for n. And so pair $\longrightarrow k^{n+1} \equiv [s^o a_n, \times^o[a_n, b_n]]$ by I.1 and I.5 (6)

To pass from (5) to (6) we must check that whenever $a_n$ or $b_n$ yield $\perp$ in (5), so will the right side of (6). Now

$$
s^o a_n \equiv s^{n+1} \circ 1 \equiv a_{n+1}
$$

$$
\times^o[a_n, b_n] \equiv / \times \circ [s^n \circ 1, s^{n-1} \circ 1, ..., s \circ 1, 1, 2]
$$

$$
\equiv b_{n+1} \text{ by I.3.}
$$

Combining (6), (7), and (8) gives pair $\longrightarrow k^{n+1} \equiv [a_{n+1}, b_{n+1}].$

Thus (2) holds for $n = 1$ and holds for $n + 1$ whenever it holds for $n$, therefore, by induction, it holds for every $n \geq 1$. Now (2) gives, for pairs:

defined$k^n \longrightarrow p \circ k^n \equiv eq0 \circ 1 \circ [a_n, b_n]$

$$
\equiv eq0 \circ a_n \equiv eq0 \circ s^n \circ 1
$$

defined$k^n \longrightarrow g \circ k^n$

$$
\equiv 2 \circ [a_n, b_n] \equiv / \times \circ [s^{n-1} \circ 1, ..., s \circ 1, 1, 2]
$$

(both use I.5). Now (1) tells us that $f:<x, l>$ is defined iff there is an $n$ such that $p \circ k^i:<x, l> = F$ for all $i < n$, and $p \circ k^n:<x, l> = T$, that is, by (10), $eq0 \circ s^n : x = T$, i.e., $x = n$; and $g \circ k^n:<x, l>$ is defined, in which case, by (11),

$$
f:<x, l> = / \times:<1, 2, ..., x-1, x, l> = n!,
$$

which is what we set out to prove.

12.6.2 Example: proof of equivalence of two iterative programs. In this example we want to prove that two iteratively defined programs, $f$ and $g$, are the same function. Let $f$ be the solution of

$$
f \equiv p \circ 1 \rightarrow 2; h \circ f \circ [k \circ 1, 2].
$$

Let $g$ be the solution of

$$
g \equiv p \circ 1 \rightarrow 2; g \circ [k \circ 1, h \circ 2].
$$

Then, by the iteration theorem:

$$
f \equiv p_0 \rightarrow q_0; ... ; p_n \rightarrow q_n; ...
$$

$$
g \equiv p'_0 \rightarrow q'_0; ... ; p'_n \rightarrow q'_n; ...
$$

where (letting $r^0 \equiv id$ for any $r$), for $n = 0, 1, ...$

$$
p_n \equiv p \circ 1 \circ [k \circ 1, 2]^n \equiv p \circ 1 \circ [k^n \circ 1, 2] \quad \text{by I.5.1} \tag{5}
$$
{#backus-1978-vonneumann-eq-5-2 .equation tag=0936}

$$
q_n \equiv h^n \circ 2 \circ [k \circ 1, 2]^n \equiv h^n \circ 2 \circ [k^n \circ 1, 2] \quad \text{by I.5.1} \tag{6}
$$
{#backus-1978-vonneumann-eq-6 .equation tag=0937}

$$
p'_n \equiv p \circ 1 \circ [k \circ 1, h \circ 2]^n \equiv p \circ 1 \circ [k^n \circ 1, h^n \circ 2] \quad \text{by I.5.1} \tag{7}
$$
{#backus-1978-vonneumann-eq-7-2 .equation tag=0938}

$$
q'_n \equiv 2 \circ [k \circ 1, h \circ 2]^n \equiv 2 \circ [k^n \circ 1, h^n \circ 2] \quad \text{by I.5.1.} \tag{8}
$$
{#backus-1978-vonneumann-eq-8-2 .equation tag=0939}

Now, from the above, using I.5, defined$2 \longrightarrow p_n \equiv p \circ k^n \circ 1$
defined$h^n \circ 2 \longrightarrow p'_n \equiv p \circ k^n \circ 1$
defined$k^n \circ 1 \longrightarrow q_n \equiv q'_n \equiv h^n \circ 2$

Thus defined$h^n \circ 2 \longrightarrow$ defined$2 \equiv \bar{T}$
defined$h^n \circ 2,\longrightarrow p_n \equiv p'_n$ and

$$
f \equiv p_0 \rightarrow q_0; ... ; p_n \rightarrow h^n \circ 2; ...
$$

$$
g \equiv p'_0 \rightarrow q'_0; ... ; p'_n \rightarrow h^n \circ 2; ...
$$

since $p_n$ and $p'_n$ provide the qualification needed for $q_n \equiv q'_n \equiv h^n \circ 2$.

Now suppose there is an $x$ such that $f:x \not\equiv g:x$. Then there is an $n$ such that $p_i : x = p'_i : x = F$ for $i < n$, and $p_n : x \not\equiv p'_n : x$. From (12) and (13) this can only happen when $h^n \circ 2 : x = \perp$. But since $h$ is $\perp$-preserving, $h^m \circ 2 : x = \perp$ for all $m \geq n$. Hence $f : x = g : x = \perp$ by (14) and (15). This contradicts the assumption that there is an $x$ for which $f : x \not\equiv g : x$. Hence $f \equiv g$.

This example (by J. H. Morris, Jr.) is treated more elegantly in [16] on p. 498. However, some may find that the above treatment is more constructive, leads one more mechanically to the key questions, and provides more insight into the behavior of the two functions.

12.7 Nonlinear Equations

The preceding examples have concerned "linear" equations (in which the "unknown" function does not have an argument involving itself). The question of the existence of simple expansions that "solve" "quadratic" and higher order equations remains open.

The earlier examples concerned solutions of $f \equiv E(f)$, where $E$ is linearly expansive. The following example involves an $E(f)$ that is quadratic and expansive (but not linearly expansive).

12.7.1 Example: proof of idempotency ([16] p. 497).
Let $f$ be the solution of

$$
f \equiv E(f) \equiv p \rightarrow id; f^2 \circ h.
$$

We wish to prove that $f \equiv f^2$. We verify that $E$ is expansive (Section 12.4.1) with the following approximating functions:

$$
f_0 \equiv \bar{1}
$$

$$
f_n \equiv p \rightarrow id; ... ; p \circ h^{n-1} \rightarrow h^{n-1}; \bar{1} \quad \text{for } n > 0
$$

First we note that $p \longrightarrow f_n \equiv id$ and so

$$
p \circ h^i \longrightarrow f_n \circ h^i \equiv h^i.
$$

Now $E(f_0) \equiv p \rightarrow id; \bar{1}^2 \circ h \equiv f_1$, and

$$
E(f_n)
$$

$$
\equiv p \rightarrow id; f_n \circ (p \rightarrow id; ... ; p \circ h^{n-1} \rightarrow h^{n-1}; \bar{1}) \circ h
$$

$$
\equiv p \rightarrow id; f_n \circ (p \circ h \rightarrow h; ... ; p \circ h^n \rightarrow h^n; \bar{1} \circ h)
$$

$$
\equiv p \rightarrow id; p \circ h \rightarrow f_n \circ h; ... ; p \circ h^n \rightarrow f_n \circ h^n; f_n \circ \bar{1}
$$

$$
\equiv p \rightarrow id; p \circ h \rightarrow h; ... ; p \circ h^n \rightarrow h^n; \bar{1} \quad \text{by (3)}
$$

$$
\equiv f_{n+1}.
$$

Thus $E$ is expansive by (4) and (5); so by (2) and Section 12.4.1 (E4)

$$
f \equiv p \rightarrow id; ... ; p \circ h^n \rightarrow h^n; ...
$$

But (6), by the iteration theorem, gives

$$
f \equiv p \rightarrow id; f \circ h.
$$

Now, if $p : x = T$, then $f : x = x = f^2 : x$, by (1). If $p : x = F$, then

$$
f : x = f^2 \circ h : x \quad \text{by (1)}
$$

= f:(f \circ h:x) = f:(f:x) \quad \text{by (7)}
= f^2:x.

If p:x is neither T nor F, then f:x = \bot = f^2:x. Thus f \equiv f^2.

12.8 Foundations for the Algebra of Programs

Our purpose in this section is to establish the validity of the results stated in Section 12.4. Subsequent sections do not depend on this one, hence it can be skipped by readers who wish to do so. We use the standard concepts and results from [16], but the notation used for objects and functions, etc., will be that of this paper.

We take as the domain (and range) for all functions the set O of objects (which includes \bot) of a given FP system. We take F to be the set of functions, and F to be the set of functional forms of that FP system. We write E(f) for any function expression involving functional forms, primitive and defined functions, and the function symbol f; and we regard E as a functional that maps a function f into the corresponding function E(f). We assume that all f \in F are \bot-preserving and that all functional forms in F correspond to continuous functionals in every variable (e.g., [f, g] is continuous in both f and g). (All primitive functions of the FP system given earlier are \bot-preserving, and all its functional forms are continuous.)

Definitions. Let E(f) be a function expression. Let f_0 \equiv \bot
f_{i+1} \equiv p_0 \rightarrow q_0; ... ; p_i \rightarrow q_i; \bot \quad \text{for } i = 0, 1, ...

where p_i, q_i \in F. Let E have the property that

E(f_i) \equiv f_{i+1} \quad \text{for } i = 0, 1, ...

Then E is said to be *expansive* with the *approximating functions* f_i. We write f \equiv p_0 \rightarrow q_0; ... ; p_n \rightarrow q_n; ...

to mean that $f \equiv \lim_i \{ f_i \}$, where the f_i have the form above. We call the right side an *infinite expansion* of f. We take f:x to be defined iff there is an n \geq 0 such that (a) p_i:x = F for all i < n, and (b) p_n:x = T, and (c) q_n:x is defined, in which case f:x = q_n:x.

Expansion theorem: Let E(f) be expansive with approximating functions as above. Let f be the least function satisfying f \equiv E(f).

Then f \equiv p_0 \rightarrow q_0; ... ; p_n \rightarrow q_n; ...

Proof. Since E is the composition of continuous functionals (from F) involving only monotonic functions (\bot-preserving functions from F) as constant terms, E is continuous ([16] p. 493). Therefore its least fixed point f is $\lim_i \{ E^i(\bot) \} \equiv \lim_i \{ f_i \}$ ([16] p. 494), which by definition is the above infinite expansion for f.

Definition. Let E(f) be a function expression satisfying the following:

E(h) \equiv p_0 \rightarrow q_0; E_1(h) \quad \text{for all } h \in F \tag{LE1} where p_i \in F and q_i \in F exist such that

E_1(p_i \rightarrow q_i; h) \equiv p_{i+1} \rightarrow q_{i+1}; E_1(h) \quad \text{for all } h \in F \text{ and } i = 0, 1, ... \tag{LE2} and

E_1(\bot) \equiv \bot. \tag{LE3}

Then E is said to be *linearly expansive* with respect to these p_i's and q_i's.

Linear Expansion Theorem: Let E be linearly expansive with respect to p_i and q_i, i = 0, 1, ... . Then E is expansive with approximating functions f_0 \equiv \bot \tag{1}
f_{i+1} \equiv p_0 \rightarrow q_0; ... ; p_i \rightarrow q_i; \bot. \tag{2}

Proof. We want to show that E(f_i) = f_{i+1} for any i \geq 0. Now

E(f_0) \equiv p_0 \rightarrow q_0; E_1(\bot) \equiv p_0 \rightarrow q_0; \bot \equiv f_1 \tag{3}
\quad \text{by (LE1) (LE3) (1).}

Let i > 0 be fixed and let f_i \equiv p_0 \rightarrow q_0; w_1 \tag{4a}
w_1 \equiv p_1 \rightarrow q_1; w_2 \tag{4b}
etc.
w_{i-1} \equiv p_{i-1} \rightarrow q_{i-1}; \bot. \tag{4-}

Then, for this i > 0

E(f_i) \equiv p_0 \rightarrow q_0; E_1(f_i) \quad \text{by (LE1)}
E_1(f_i) \equiv p_1 \rightarrow q_1; E_1(w_1) \quad \text{by (LE2) and (4a)}
E_1(w_1) \equiv p_2 \rightarrow q_2; E_1(w_2) \quad \text{by (LE2) and (4b)} etc.

E_1(w_{i-1}) \equiv p_i \rightarrow q_i; E_1(\bot) \quad \text{by (LE2) and (4-)}
\equiv p_i \rightarrow q_i; \bot \quad \text{by (LE3)}

Combining the above gives

E(f_i) \equiv f_{i+1} \quad \text{for arbitrary } i > 0, \text{ by (2).} \tag{5}

By (3), (5) also holds for i = 0; thus it holds for all i \geq 0. Therefore E is expansive and has the required approximating functions. □

Corollary. If E is linearly expansive with respect to p_i and q_i, i = 0, 1, ... , and f is the least function satisfying f \equiv E(f) \tag{LE4} then f \equiv p_0 \rightarrow q_0; ... ; p_n \rightarrow q_n; ... . \tag{LE5}

12.9 The Algebra of Programs for the Lambda Calculus and for Combinators

Because Church's lambda calculus [5] and the system of combinators developed by Schönfinkel and Curry [6] are the primary mathematical systems for representing the notion of application of functions, and because they are more powerful than FP systems, it is natural to enquire what an algebra of programs based on those systems would look like.

The lambda calculus and combinator equivalents of FP composition, $f \circ g$, are

$$
\lambda fgx.(f(gx)) \equiv B
$$

where B is a simple combinator defined by Curry. There is no direct equivalent for the FP object <x,y> in the Church or Curry systems proper; however, following Landin [14] and Burge [4], one can use the primitive functions prefix, head, tail, null, and atomic to introduce the notion of list structures that correspond to FP sequences. Then, using FP notation for lists, the lambda calculus equivalent for construction is $\lambda fgx.<fx,gx>$. A combinatory equivalent is an expression involving prefix, the null list, and two or more basic combinators. It is so complex that I shall not attempt to give it.

If one uses the lambda calculus or combinatorial expressions for the functional forms $f \circ g$ and $[f,g]$ to express the law I.1 in the FP algebra, $[f,g] \circ h \equiv [f \circ h, g \circ h]$, the result is an expression so complex that the sense of the law is obscured. The only way to make that sense clear in either system is to name the two functionals: composition $\equiv B$, and construction $\equiv A$, so that $Bfg \equiv f \circ g$, and $Afh \equiv [f,g]$. Then I.1 becomes

$$
B(Afh)h \equiv A(Bfh)(Bgh),
$$

which is still not as perspicuous as the FP law.

The point of the above is that if one wishes to state clear laws like those of the FP algebra in either Church’s or Curry’s system, one finds it necessary to select certain functionals (e.g., composition and construction) as the basic operations of the algebra and to either give them short names or, preferably, represent them by some special notation as in FP. If one does this and provides primitives, objects, lists, etc., the result is an FP-like system in which the usual lambda expressions or combinators do not appear. Even then these Church or Curry versions of FP systems, being less restricted, have some problems that FP systems do not have:

a) The Church and Curry versions accommodate functions of many types and can define functions that do not exist in FP systems. Thus, $Bf$ is a function that has no counterpart in FP systems. This added power carries with it problems of type compatibility. For example, in $f \circ g$, is the range of $g$ included in the domain of $f$? In FP systems all functions have the same domain and range.

b) The semantics of Church’s lambda calculus depends on substitution rules that are simply stated but whose implications are very difficult to fully comprehend. The true complexity of these rules is not widely recognized but is evidenced by the succession of able logicians who have published “proofs” of the Church-Rosser theorem that failed to account for one or another of these complexities. (The Church-Rosser theorem, or Scott’s proof of the existence of a model [22], is required to show that the lambda calculus has a consistent semantics.) The definition of pure Lisp contained a related error for a considerable period (the “funarg” problem). Analogous problems attach to Curry’s system as well.

In contrast, the formal (FFP) version of FP systems (described in the next section) has no variables and only an elementary substitution rule (a function for its name), and it can be shown to have a consistent semantics by a relatively simple fixed-point argument along the lines developed by Dana Scott and by Manna et al [16]. For such a proof see McJones [18].

12.10 Remarks

The algebra of programs outlined above needs much work to provide expansions for larger classes of equations and to extend its laws and theorems beyond the elementary ones given here. It would be interesting to explore the algebra for an FP-like system whose sequence constructor is not $\perp$-preserving (law I.5 is strengthened, but IV.1 is lost). Other interesting problems are: (a) Find rules that make expansions unique, giving canonical forms for functions; (b) find algorithms for expanding and analyzing the behavior of functions for various classes of arguments; and (c) explore ways of using the laws and theorems of the algebra as the basic rules either of a formal, preexecution “lazy evaluation” scheme [9, 10], or of one which operates during execution. Such schemes would, for example, make use of the law $l \circ [f,g] \leq f$ to avoid evaluating $g:x$.
