---
paper: mccarthy-1960-lisp
title: Recursive Functions of Symbolic Expressions and Their Computation by Machine, Part I
authors:
  - John McCarthy
year: 1960
venue: Communications of the ACM
field: languages
section: "3"
section_title: Recursive Functions of Symbolic Expressions
tag: "0250"
kind: section
lang: en
source: http://www-formal.stanford.edu/jmc/recursive.pdf
pdf_sha256: 3d981849e59505eff3f14397a177b409f5d978d43d114bdd67c956e74320fc92
pdf_pages: 8-22
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: dfa0ae70bdfe9b4e20e0166957fdcd30094fdbb8151a9f7d0e892f28b648007a
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

We shall first define a class of symbolic expressions in terms of ordered pairs and lists. Then we shall define five elementary functions and predicates, and build from them by composition, conditional expressions, and recursive definitions an extensive class of functions of which we shall give a number of examples. We shall then show how these functions themselves can be expressed as symbolic expressions, and we shall define a universal function apply that allows us to compute from the expression for a given function its value for given arguments. Finally, we shall define some functions with functions as arguments and give some useful examples.

a. *A Class of Symbolic Expressions.* We shall now define the S-expressions (S stands for symbolic). They are formed by using the special characters

.
)
(
and an infinite set of distinguishable atomic symbols. For atomic symbols, we shall use strings of capital Latin letters and digits with single imbedded blanks.$^3$ Examples of atomic symbols are

$$
A \\
ABA \\
APPLE PIE NUMBER 3
$$

There is a twofold reason for departing from the usual mathematical practice of using single letters for atomic symbols. First, computer programs frequently require hundreds of distinguishable symbols that must be formed from the 47 characters that are printable by the IBM 704 computer. Second, it is convenient to allow English words and phrases to stand for atomic entities for mnemonic reasons. The symbols are atomic in the sense that any substructure they may have as sequences of characters is ignored. We assume only that different symbols can be distinguished. S-expressions are then defined as follows:

1. Atomic symbols are S-expressions.
2. If $e_1$ and $e_2$ are S-expressions, so is $(e_1 \cdot e_2)$.
Examples of S-expressions are

$$
AB \\
(A \cdot B) \\
((AB \cdot C) \cdot D)
$$

An S-expression is then simply an ordered pair, the terms of which may be atomic symbols or simpler S-expressions. We can can represent a list of arbitrary length in terms of S-expressions as follows. The list

$$
(m_1, m_2, \cdots, m_n)
$$

is represented by the S-expression

$$
(m_1 \cdot (m_2 \cdot (\cdots (m_n \cdot NIL) \cdots)))
$$

Here $NIL$ is an atomic symbol used to terminate lists. Since many of the symbolic expressions with which we deal are conveniently expressed as lists, we shall introduce a list notation to abbreviate certain S-expressions. We have

\footnotetext{3}{1995 remark: Imbedded blanks could be allowed within symbols, because lists were then written with commas between elements.}

1. $(m)$ stands for $(m \cdot NIL)$.
2. $(m_1, \cdots, m_n)$ stands for $(m_1 \cdot (\cdots (m_n \cdot NIL) \cdots))$.
3. $(m_1, \cdots, m_n \cdot x)$ stands for $(m_1 \cdot (\cdots (m_n \cdot x) \cdots))$.

Subexpressions can be similarly abbreviated. Some examples of these abbreviations are

$$
((AB, C), D) \text{ for } ((AB \cdot (C \cdot NIL)) \cdot (D \cdot NIL))
$$

$$
((A, B), C, D \cdot E) \text{ for } ((A \cdot (B \cdot NIL)) \cdot (C \cdot (D \cdot E)))
$$

Since we regard the expressions with commas as abbreviations for those not involving commas, we shall refer to them all as S-expressions.

b. *Functions of S-expressions and the Expressions That Represent Them.*
We now define a class of functions of S-expressions. The expressions representing these functions are written in a conventional functional notation. However, in order to clearly distinguish the expressions representing functions from S-expressions, we shall use sequences of lower-case letters for function names and variables ranging over the set of S-expressions. We also use brackets and semicolons, instead of parentheses and commas, for denoting the application of functions to their arguments. Thus we write

$$
car[x]
$$

$$
car[cons[(A \cdot B); x]]
$$

In these M-expressions (meta-expressions) any S-expression that occur stand for themselves.

c. *The Elementary S-functions and Predicates.* We introduce the following functions and predicates:
1. atom. atom[x] has the value of T or F according to whether x is an atomic symbol. Thus atom [X] = T
atom [(X \cdot A)] = F

2. eq. eq [x;y] is defined if and only if both x and y are atomic. eq [x; y] = T if x and y are the same symbol, and eq [x; y] = F otherwise. Thus eq [X; X] = T
eq [X; A] = F
eq [X; (X · A)] is undefined.

3. car. car[x] is defined if and only if x is not atomic. car [(e₁ · e₂)] = e₁. Thus car [X] is undefined.

car [(X · A)] = X
car [((X · A) · Y)] = (X · A)

4. cdr. cdr [x] is also defined when x is not atomic. We have cdr [(e₁ · e₂)] = e₂. Thus cdr [X] is undefined.

cdr [(X · A)] = A cdr [((X · A) · Y)] = Y

5. cons. cons [x; y] is defined for any x and y. We have cons [e₁; e₂] = (e₁ · e₂). Thus cons [X; A] = (X A)
cons [(X · A); Y] = ((X · A)Y) car, cdr, and cons are easily seen to satisfy the relations car [cons [x; y]] = x
cdr [cons [x; y]] = y
cons [car [x]; cdr [x]] = x, provided that x is not atomic.

The names “car” and “cons” will come to have mnemonic significance only when we discuss the representation of the system in the computer. Compositions of car and cdr give the subexpressions of a given expression in a given position. Compositions of cons form expressions of a given structure out of parts. The class of functions which can be formed in this way is quite limited and not very interesting.

d. *Recursive S-functions.* We get a much larger class of functions (in fact, all computable functions) when we allow ourselves to form new functions of S-expressions by conditional expressions and recursive definition. We now give some examples of functions that are definable in this way.

1. ff[x]. The value of ff[x] is the first atomic symbol of the S-expression x with the parentheses ignored. Thus

$$
\mathrm{ff}[(A \cdot B) \cdot C)] = A
$$

We have

$$
\mathrm{ff}[x] = [atom[x] \rightarrow x; T \rightarrow \mathrm{ff}[car[x]]]
$$

We now trace in detail the steps in the evaluation of ff [((A . B) . C)]:
ff [((A . B) . C)]

$$
= [atom[((A \cdot B) \cdot C)] \rightarrow ((A \cdot B) \cdot C); T \rightarrow \mathrm{ff}[car[((A \cdot B)C\cdot))]]
$$

$$
= [F \rightarrow ((A \cdot B) \cdot C); T \rightarrow \mathrm{ff}[car[((A \cdot B) \cdot C))]]
$$

$$
= [T \rightarrow \mathrm{ff}[car[((A \cdot B) \cdot C))]]
$$

$$
= \mathrm{ff}[car[((A \cdot B) \cdot C))]
$$

$$
= \mathrm{ff}[(A \cdot B)]
$$

$$
= [atom[(A \cdot B)] \rightarrow (A \cdot B); T \rightarrow \mathrm{ff}[car[(A \cdot B))]]
$$

$$
= [F \rightarrow (A \cdot B); T \rightarrow \mathrm{ff}[car[(A \cdot B))]]
$$

$$
= [T \rightarrow \mathrm{ff}[car[(A \cdot B))]]
$$

$$
= \mathrm{ff}[car[(A \cdot B))]
$$

$$
= \mathrm{ff}[A]
$$

$$
= \ [atom[A] \rightarrow A; T \rightarrow \mathbf{ff}[car[A]]]
$$

$$
= \ [T \rightarrow A; T \rightarrow \mathbf{ff}[car[A]]]
$$

$$
= \ A
$$

2. subst $[x; y; z]$. This function gives the result of substituting the S-expression $x$ for all occurrences of the atomic symbol $y$ in the S-expression $z$. It is defined by

$$
\text{subst } [x; y; z] = [\text{atom } [z] \rightarrow [\text{eq } [z; y] \rightarrow x; \text{T} \rightarrow z]; \\
\text{T} \rightarrow \text{cons } [\text{subst } [x; y; \text{car } [z]]; \text{subst } [x; y; \text{cdr } [z]]]]
$$

As an example, we have

$$
\text{subst}[(X \cdot A); B; ((A \cdot B) \cdot C)] = ((A \cdot (X \cdot A))) \cdot C)
$$

3. equal $[x; y]$. This is a predicate that has the value $T$ if $x$ and $y$ are the same S-expression, and has the value F otherwise. We have

$$
\text{equal } [x; y] = [\text{atom } [x] \land \text{atom } [y] \land \text{eq } [x; y]]
$$

$$
\lor [\neg \text{atom } [x] \land \neg \text{atom } [y] \land \text{equal } [\text{car } [x]; \text{car } [y]] \\
\land \text{equal } [\text{cdr } [x]; \text{cdr } [y]]]
$$

It is convenient to see how the elementary functions look in the abbreviated list notation. The reader will easily verify that

(i) $car[(m_1, m_2, \cdots, m_n)] = m_1$
(ii) $cdr[(m_s, m_2, \cdots, m_n)] = (m_2, \cdots, m_n)$
(iii) $cdr[(m)] = NIL$
(iv) $cons[m_1; (m_2, \cdots, m_n)] = (m_1, m_2, \cdots, m_n)$
(v) $cons[m; NIL] = (m)$

We define

$$
null[x] = atom[x] \land eq[x; NIL]
$$

This predicate is useful in dealing with lists.

Compositions of car and cdr arise so frequently that many expressions can be written more concisely if we abbreviate

$$
cadr[x] \text{ for } car[cdr[x]],
caddr[x] \text{ for } car[cdr[cdr[x]]], \text{ etc.}
$$

Another useful abbreviation is to write list $[e_1; e_2; \cdots; e_n]$
for $cons[e_1; cons[e_2; \cdots; cons[e_n; NIL] \cdots]]$.

This function gives the list, $(e_1, \cdots, e_n)$, as a function of its elements.

The following functions are useful when S-expressions are regarded as lists.

1. append [x;y].

append [x; y] = [null[x] \rightarrow y; T \rightarrow cons [car [x]; append [cdr [x]; y]]]

An example is append [(A, B); (C, D, E)] = (A, B, C, D, E)

2. among [x;y]. This predicate is true if the S-expression $x$ occurs among the elements of the list $y$. We have

$$
among[x; y] = \neg null[y] \land [equal[x; car[y]] \lor among[x; cdr[y]]]
$$

3. pair [x;y]. This function gives the list of pairs of corresponding elements of the lists $x$ and $y$. We have

$$
pair[x; y] = [null[x] \land null[y] \rightarrow NIL; \neg atom[x] \land \neg atom[y] \rightarrow cons[list[car[x]; car[y]]; pair[cdr[x]; cdr[y]]]]
$$

An example is

$$
pair[(A, B, C); (X, (Y, Z), U)] = ((A, X), (B, (Y, Z)), (C, U)).
$$

4. assoc [x;y]. If y is a list of the form ((u₁, v₁), ..., (uₙ, vₙ)) and x is one of the u’s, then assoc [x; y] is the corresponding v. We have

$$
assoc[x; y] = eq[caar[y]; x] \rightarrow cadar[y]; T \rightarrow assoc[x; cdr[y]]
$$

An example is

$$
assoc[X; ((W, (A, B)), (X, (C, D)), (Y, (E, F)))) = (C, D).
$$

5. sublis[x; y]. Here x is assumed to have the form of a list of pairs ((u₁, v₁), ..., (uₙ, vₙ)), where the u’s are atomic, and y may be any S-expression. The value of sublis[x; y] is the result of substituting each v for the corresponding u in y. In order to define sublis, we first define an auxiliary function. We have

$$
sub2[x; z] = [null[x] \rightarrow z; eq[caar[x]; z] \rightarrow cadar[x]; T \rightarrow sub2[cdr[x]; z]]
$$

and

$$
sublis[x; y] = [atom[y] \rightarrow sub2[x; y]; T \rightarrow cons[sublis[x; car[y]]; sublis[x; cdr[y]]]
$$

We have sublis[((X, (A, B)), (Y, (B, C))); (A, X · Y)] = (A, (A, B), B, C) e. Representation of S-Functions by S-Expressions. S-functions have been described by M-expressions. We now give a rule for translating M-expressions into S-expressions, in order to be able to use S-functions for making certain computations with S-functions and for answering certain questions about S-functions.

The translation is determined by the following rules in rich we denote the translation of an M-expression $\mathcal{E}$ by $\mathcal{E}^*$.

1. If $\mathcal{E}$ is an S-expression $\mathcal{E}^*$ is (QUOTE, $\mathcal{E}$).
2. Variables and function names that were represented by strings of lower-case letters are translated to the corresponding strings of the corresponding uppercase letters. Thus car* is CAR, and subst* is SUBST.
3. A form $f[e_1; \cdots; e_n]$ is translated to ($f^*, e_1^* \cdots, e_n^*$). Thus cons [car [x]; cdr [x]]* is (CONS, (CAR, X), (CDR, X)).
4. $\{[p_1 \rightarrow e_1; \cdots; p_n \rightarrow e_n]\}^*$ is (COND, $(p_1^*, e_1^*), \cdots, (p_n^* \cdot e_n^*)$).

5. $\{\lambda[[x_1;\cdots;x_n];\mathcal{E}]\}^*$ is (LAMBDA, $(x_1^*,\cdots,x_n^*),\mathcal{E}^*$).
6. $\{label[a;\mathcal{E}]\}^*$ is (LABEL, $a^*,\mathcal{E}^*$).

With these conventions the substitution function whose M-expression is label [subst; $\lambda [[x; y; z]; [atom [z] \rightarrow [eq [y; z] \rightarrow x; T \rightarrow z]; T \rightarrow cons [subst [x; y; car [z]]]; subst [x; y; cdr [z]]]]]]$ has the S-expression

$$(LABEL, SUBST, (LAMBDA, (X, Y, Z), (COND ((ATOM, Z), (COND, (EQ, Y, Z), X), ((QUOTE, T), Z))), ((QUOTE, T), (CONS, (SUBST, X, Y, (CAR Z)), (SUBST, X, Y, (CDR, Z))))))$$

This notation is writable and somewhat readable. It can be made easier to read and write at the cost of making its structure less regular. If more characters were available on the computer, it could be improved considerably.$^4$ f. *The Universal S-Function apply*. There is an S-function *apply* with the property that if $f$ is an S-expression for an S-function $f'$ and *args* is a list of arguments of the form $(arg_1,\cdots,arg_n)$, where $arg_1,\cdots,arg_n$ are arbitrary S-expressions, then *apply*[f; args] and $f'[arg_1;\cdots;arg_n]$ are defined for the same values of $arg_1,\cdots,arg_n$, and are equal when defined. For example,

$$\lambda[[x; y]; cons[car[x]; y]][(A, B); (C, D)]$$

$= apply[(LAMBDA, (X, Y), (CONS, (CAR, X), Y)); ((A, B), (C, D))] = (A, C, D)$

The S-function *apply* is defined by

$$apply[f; args] = eval[cons[f; appq[args]]; NIL],$$

where

$$appq[m] = [null[m] \rightarrow NIL; T \rightarrow cons[list[QUOTE; car[m]]; appq[cdr[m]]]]$$

and

$$eval[e; a] = [$$

__________________________
$^4$1995: More characters were made available on SAIL and later on the Lisp machines. Alas, the world went back to inferior character sets again—though not as far back as when this paper was written in early 1959.

atom [e] → assoc [e; a];

atom [car [e]] → [
eq [car [e]; QUOTE] → cadr [e];
eq [car [e]; ATOM] → atom [eval [cadr [e]; a]];
eq [car [e]; EQ] → [eval [cadr [e]; a] = eval [caddr [e]; a]];
eq [car [e]; COND] → evcon [cdr [e]; a];
eq [car [e]; CAR] → car [eval [cadr [e]; a]];
eq [car [e]; CDR] → cdr [eval [cadr [e]; a]];
eq [car [e]; CONS] → cons [eval [cadr [e]; a]; eval [caddr [e]; a]]; T → eval [cons [assoc [car [e]; a]; evlis [cdr [e]; a]]];
eq [caar [e]; LABEL] → eval [cons [caddar [e]; cdr [e]]];
cons [list [cadar [e]; car [e]; a]];
eq [caar [e]; LAMBDA] → eval [caddar [e];
append [pair [cadar [e]; evlis [cdr [e]; a]]]

and

$$
evcon[c; a] = [eval[caar[c]; a] \rightarrow eval[cadar[c]; a]; T \rightarrow evcon[cdr[c]; a]]
$$

and

$$
evlis[m; a] = [null[m] \rightarrow NIL; T \rightarrow cons[eval[car[m]; a]; evlis[cdr[m]; a]]]
$$

We now explain a number of points about these definitions.⁵

1. apply itself forms an expression representing the value of the function applied to the arguments, and puts the work of evaluating this expression onto a function eval. It uses appq to put quotes around each of the arguments, so that eval will regard them as standing for themselves.

2. eval[e; a] has two arguments, an expression e to be evaluated, and a list of pairs a. The first item of each pair is an atomic symbol, and the second is the expression for which the symbol stands.

3. If the expression to be evaluated is atomic, eval evaluates whatever is paired with it first on the list a.

4. If e is not atomic but car[e] is atomic, then the expression has one of the forms (QUOTE, e) or (ATOM, e) or (EQ, e₁, e₂) or (COND, (p₁, e₁), ⋯, (pₙ, eₙ)), or (CAR, e) or (CDR, e) or (CONS, e₁, e₂) or (f, e₁, ⋯, eₙ) where f is an atomic symbol.

In the case (QUOTE, e) the expression e, itself, is taken. In the case of (ATOM, e) or (CAR, e) or (CDR, e) the expression e is evaluated and the appropriate function taken. In the case of (EQ, e₁, e₂) or (CONS, e₁, e₂) two expressions have to be evaluated. In the case of (COND, (p₁, e₁), ⋯ (pₙ, eₙ)) the p’s have to be evaluated in order until a true p is found, and then the corresponding e must be evaluated. This is accomplished by evcon. Finally, in the case of (f, e₁, ⋯, eₙ) we evaluate the expression that results from replacing f in this expression by whatever it is paired with in the list a.

5. The evaluation of ((LABEL, f, E), e₁, ⋯, eₙ) is accomplished by evaluating (E, e₁, ⋯, eₙ) with the pairing (f, (LABEL, f, E)) put on the front of the previous list a of pairs.

6. Finally, the evaluation of ((LAMBDA, (x₁, ⋯, xₙ), E), e₁, ⋯ eₙ) is accomplished by evaluating E with the list of pairs ((x₁, e₁), ⋯, ((xₙ, eₙ)) put on the front of the previous list a.

The list a could be eliminated, and LAMBDA and LABEL expressions evaluated by substituting the arguments for the variables in the expressions E. Unfortunately, difficulties involving collisions of bound variables arise, but they are avoided by using the list a.

⁵1995: This version isn’t quite right. A comparison of this and other versions of eval including what was actually implemented (and debugged) is given in “The Influence of the Designer on the Design” by Herbert Stoyan and included in Artificial Intelligence and Mathematical Theory of Computation: Papers in Honor of John McCarthy, Vladimir Lifschitz (ed.), Academic Press, 1991

Calculating the values of functions by using apply is an activity better suited to electronic computers than to people. As an illustration, however, we now give some of the steps for calculating
apply [(LABEL, FF, (LAMBDA, (X), (COND, (ATOM, X), X), ((QUOTE, T),(FF, (CAR, X))))));((A·B))] = A
The first argument is the S-expression that represents the function ff defined in section 3d. We shall abbreviate it by using the letter $\phi$. We have apply [$\phi$; ( (A·B) )]
    = eval [((LABEL, FF, $\psi$), (QUOTE, (A·B)))); NIL] where $\psi$ is the part of $\phi$ beginning (LAMBDA

= eval[((LAMBDA, (X), $\omega$), (QUOTE, (A·B))));((FF, $\phi$))]
    where $\omega$ is the part of $\psi$ beginning (COND

= eval [(COND, ($\pi_1, \epsilon_1$), ($\pi_2, \epsilon_2$)); ((X, (QUOTE, (A·B)) ) ), (FF, $\phi$) )]
Denoting ((X, (QUOTE, (A·B))), (FF, $\phi$)) by $a$, we obtain

= evcon [(($\pi_1, \epsilon_1$), ($\pi_2, \epsilon_2$)); $a$]

This involves eval [$\pi_1$; $a$]

= eval [( ATOM, X); $a$]

= atom [eval [X; $a$]]

= atom [eval [assoc [X; ((X, (QUOTE, (A·B))), (FF,$\phi$))];$a$]]

= atom [eval [(QUOTE, (A·B)); $a$]]

= atom [(A·B)],

= F

Our main calculation continues with apply [$\phi; ((A\cdot B))$]

$$
= \mathrm{evcon}\ [((\pi_2, \epsilon_2, )); a],
$$

which involves eval $[\pi_2; a] = \mathrm{eval}\ [(\mathrm{QUOTE}, \mathrm{T}); a] = \mathrm{T}$

Our main calculation again continues with apply [$\phi; ((A\cdot B))$]

$$
= \mathrm{eval}\ [\epsilon_2; a]
$$

$$
= \mathrm{eval}\ [(\mathrm{FF}, (\mathrm{CAR}, X)); a]
$$

$$
= \mathrm{eval}\ [\mathrm{Cons}\ [\phi; \mathrm{evlis}\ [((\mathrm{CAR}, X)); a]]]; a]
$$

Evaluating evlis [((CAR, X)); a] involves

$$
\mathrm{eval}\ [(\mathrm{CAR}, X); a]
$$

$$
= \mathrm{car}\ [\mathrm{eval}\ [X; a]]
$$

$$
= \mathrm{car}\ [(A\cdot B)], \text{ where we took steps from the earlier computation of atom } [\mathrm{eval}\ [X; a]] = A,
$$

and so evlis [((CAR, X)); a] then becomes

$$
\mathrm{list}\ [\mathrm{list}\ [\mathrm{QUOTE}; A]] = ((\mathrm{QUOTE}, A)),
$$

and our main quantity becomes

$$
= \mathrm{eval}\ [(\phi, (\mathrm{QUOTE}, A)); a]
$$

The subsequent steps are made as in the beginning of the calculation. The LABEL and LAMBDA cause new pairs to be added to $a$, which gives a new list of pairs $a_1$. The $\pi_1$ term of the conditional eval [(\mathrm{ATOM}, X); $a_1$] has the value T because X is paired with (QUOTE, A) first in $a_1$, rather than with (QUOTE, (A·B)) as in $a$.
Therefore we end up with eval [X; $a_1$] from the *evcon*, and this is just A. g. *Functions with Functions as Arguments.* There are a number of useful functions some of whose arguments are functions. They are especially useful in defining other functions. One such function is *maplist[x; f]* with an S-expression argument $x$ and an argument $f$ that is a function from S-expressions to S-expressions. We define

$$
maplist[x; f] = [null[x] \rightarrow NIL; T \rightarrow cons[f[x]; maplist[cdr[x]; f]]]
$$

The usefulness of *maplist* is illustrated by formulas for the partial derivative with respect to $x$ of expressions involving sums and products of $x$ and other variables. The S-expressions that we shall differentiate are formed as follows.

1. An atomic symbol is an allowed expression.
2. If $e_1, e_2, \cdots, e_n$ are allowed expressions, (PLUS, $e_1, \cdots, e_n$) and (TIMES, $e_1, \cdots, e_n$) are also, and represent the sum and product, respectively, of $e_1, \cdots, e_n$.

This is, essentially, the Polish notation for functions, except that the inclusion of parentheses and commas allows functions of variable numbers of arguments. An example of an allowed expression is (TIMES, X, (PLUS, X, A), Y), the conventional algebraic notation for which is X(X + A)Y.

Our differentiation formula, which gives the derivative of $y$ with respect to $x$, is

$$
diff[y; x] = [atom[y] \rightarrow [eq[y; x] \rightarrow ONE; T \rightarrow ZERO]; eq[car[Y]; PLUS] \rightarrow cons[PLUS; maplist[cdr[y]; \lambda[[z]; diff[car[z]; x]]]]; eq[car[y]; TIMES] \rightarrow cons[PLUS; maplist[cdr[y]; \lambda[[z]; cons[TIMES; maplist[cdr[y]; \lambda[[w]; \neg eq[z; w]] \rightarrow car[w]; T \rightarrow diff[car[[w]; x]]]]]]]]
$$

The derivative of the expression (TIMES, X, (PLUS, X, A), Y), as computed by this formula, is
(PLUS, (TIMES, ONE, (PLUS, X, A), Y), (TIMES, X, (PLUS, ONE, ZERO), Y), (TIMES, X, (PLUS, X, A), ZERO))

Besides *maplist*, another useful function with functional arguments is *search*, which is defined as

$$
search[x; p; f; u] = [null[x] \rightarrow u; p[x] \rightarrow f[x]; T \rightarrow search[cdr[x]; p; f; u]]
$$

The function search is used to search a list for an element that has the property p, and if such an element is found, f of that element is taken. If there is no such element, the function u of no arguments is computed.
