---
paper: backus-1978-vonneumann
title: Can Programming Be Liberated from the von Neumann Style? A Functional Style and Its Algebra of Programs
authors:
  - John Backus
year: 1978
venue: Communications of the ACM (Turing Award lecture)
field: languages
section: "13"
section_title: Formal Systems for Functional Programming (FFP Systems)
tag: "0573"
kind: section
lang: en
source: https://www.cs.cmu.edu/~crary/819-f09/Backus78.pdf
pdf_sha256: 2e412a7986c7fd1bdd060d90d035faa9ecc8a29675f99206c243da90954ca423
pdf_pages: 19-22
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 2d1e903cfb41924987b55e5fd74573249a92b0f40bec1fb4866fb17627b68193
edited: true
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

### 13.1 Introduction {#backus-1978-vonneumann-s13-1 .section tag=0574}

As we have seen, an FP system has a set of functions that depends on its set of primitive functions, its set of functional forms, and its set of definitions. In particular, its set of functional forms is fixed once and for all, and this set determines the power of the system in a major way. For example, if its set of functional forms is empty, then its entire set of functions is just the set of primitive functions. In FFP systems one can create new functional forms. Functional forms are represented by object sequences; the first element of a sequence determines which form it represents, while the remaining elements are the parameters of the form.

The ability to define new functional forms in FFP systems is one consequence of the principal difference between them and FP systems: in FFP systems objects are used to “represent” functions in a systematic way. Otherwise FFP systems mirror FP systems closely. They are similar to, but simpler than, the Reduction (Red) languages of an earlier paper [2].

We shall first give the simple syntax of FFP systems, then discuss their semantics informally, giving examples, and finally give their formal semantics.

### 13.2 Syntax {#backus-1978-vonneumann-s13-2 .section tag=0575}

We describe the set O of objects and the set E of expressions of an FFP system. These depend on the choice of some set A of atoms, which we take as given. We assume that T (true), F (false), φ (the empty sequence), and # (default) belong to A, as well as “numbers” of various kinds, etc.
1) Bottom, ⊥, is an object but not an atom.
2) Every atom is an object.
3) Every object is an expression.
4) If $x_1, ..., x_n$ are objects [expressions], then $<x_1, ..., x_n>$ is an object [resp., expression] called a sequence (of length n) for $n \geq 1$. The object [expression] $x_i$ for $1 \leq i \leq n$, is the ith element of the sequence $<x_1, ..., x_i, ..., x_n>$. ($\phi$ is both a sequence and an atom; its length is 0.)
5) If x and y are expressions, then $(x:y)$ is an expression called an application. x is its operator and y is its operand. Both are elements of the expression.
6) If $x = <x_1, ..., x_n>$ and if one of the elements of x is $\perp$, then $x = \perp$. That is, $<..., \perp, ...> = \perp$.
7) All objects and expressions are formed by finite use of the above rules.

A subexpression of an expression x is either x itself or a subexpression of an element of x. An FFP object is an expression that has no application as a subexpression. Given the same set of atoms, FFP and FP objects are the same.

### 13.3 Informal Remarks About FFP Semantics {#backus-1978-vonneumann-s13-3 .section tag=0576}

13.3.1 The meaning of expressions; the semantic function $\mu$. Every FFP expression e has a meaning, $\mu e$, which is always an object; $\mu e$ is found by repeatedly replacing each innermost application in e by its meaning. If this process is nonterminating, the meaning of e is $\perp$. The meaning of an innermost application $(x:y)$ (since it is innermost, x and y must be objects) is the result of applying the function represented by x to y, just as in FP systems, except that in FFP systems functions are represented by objects, rather than by function expressions, with atoms (instead of function symbols) representing primitive and defined functions, and with sequences representing the FP functions denoted by functional forms.

The association between objects and the functions they represent is given by the representation function, $\rho$, of the FFP system. (Both $\rho$ and $\mu$ belong to the description of the system, not the system itself.) Thus if the atom NULL represents the FP function null, then $\rho NULL =$ null and the meaning of $(NULL:A)$ is $\mu(NULL:A) = (\rho NULL):A =$ null:A = F.

From here on, as above, we use the colon in two senses. When it is between two objects, as in $(NULL:A)$, it identifies an FFP application that denotes only itself; when it comes between a function and an object, as in $(\rho NULL):A$ or null:A, it identifies an FP-like application that denotes the result of applying the function to the object.

The fact that FFP operators are objects makes possible a function, apply, which is meaningless in FP systems:

apply:<x,y> = (x:y).

The result of apply:<x,y>, namely (x:y), is meaningless in FP systems on two levels. First, (x:y) is not itself an object; it illustrates another difference between FP and FFP systems: some FFP functions, like apply, map objects into expressions, not directly into objects as FP functions do. However, the meaning of apply:<x,y> is an object (see below). Second, (x:y) could not be even an intermediate result in an FP system; it is meaningless in FP systems since x is an object, not a function and FP systems do not associate functions with objects. Now if APPLY represents apply, then the meaning of (APPLY:<NULL,A>) is

$$
\begin{align*}
\mu(APPLY:<NULL,A>) \\
&= \mu((\rho APPLY):<NULL,A>) \\
&= \mu(apply:<NULL,A>) \\
&= \mu(NULL:A) = \mu((\rho NULL):A) \\
&= \mu(null:A) = \mu F = F.
\end{align*}
$$

The last step follows from the fact that every object is its own meaning. Since the meaning function $\mu$ eventually evaluates all applications, one can think of apply:<NULL,A> as yielding F even though the actual result is (NULL:A).

13.3.2 How objects represent functions; the representation function $\rho$. As we have seen, some atoms (primitive atoms) will represent the primitive functions of the system. Other atoms can represent defined functions just as symbols can in FP systems. If an atom is neither primitive nor defined, it represents $\perp$, the function which is $\perp$ everywhere.

Sequences also represent functions and are analogous to the functional forms of FP. The function represented by a sequence is given (recursively) by the following rule.

Metacomposition rule

$$(\rho<x_1, ..., x_n>):y = (\rho x_1):<<x_1, ..., x_n>, y>,$$

where the $x_i$'s and y are objects. Here $\rho x_1$ determines what functional form $<x_1, ..., x_n>$ represents, and $x_2, ..., x_n$ are the parameters of the form (in FFP, $x_1$ itself can also serve as a parameter). Thus, for example, let Def $\rho CONST \equiv 2 \circ 1$; then $<CONST,x>$ in FFP represents the FP functional form $\bar{x}$, since, by the metacomposition rule, if $y \neq \perp$,

$$(\rho<CONST,x>):y = (\rho CONST):<<CONST,x>,y> \\
= 2 \circ 1:<<CONST,x>,y> = x.$$

Here we can see that the first, controlling, operator of a sequence or form, CONST in this case, always has as its operand, after metacomposition, a pair whose first element is the sequence itself and whose second element is the original operand of the sequence, y in this case. The controlling operator can then rearrange and reapply the elements of the sequence and original operand in a great variety of ways. The significant point about metacomposition is that it permits the definition of new functional forms, in effect, merely by defining new functions. It also permits one to write recursive functions without a definition.

Store and push, pop, purge

Like fetch, store takes an object n as its parameter; it is written $\downarrow n$ ("store n"). When applied to a pair $<x,y>$, where y is a sequence, $\downarrow n$ removes the first cell named n from y, if any, then creates a new cell named n with contents x and appends it to y. Before defining $\downarrow n$ (store n) we shall specify four auxiliary functional forms. (These can be used in combination with fetch n and store n to obtain multiple, named, LIFO stacks within a storage sequence.) Two of these auxiliary forms are specified by recursive functional equations; each takes an object n as its parameter.

(cellname n) $\equiv$ atom $\rightarrow \bar{F}$;

$$
\text{eq} \circ [\text{length}, \bar{3}] \rightarrow \text{eq} \circ [[\overline{CELL}, \bar{n}], [1, 2]] ; \bar{F}
$$

(push n) $\equiv$ pair $\rightarrow$ apndl$[[\overline{CELL}, \bar{n}, 1], 2]; \bot$
(pop n) $\equiv$ null $\rightarrow \bar{\phi}$;

$$
(\text{cellname } n) \circ 1 \rightarrow \text{tl}; \text{apndl} \circ [1, (\text{pop } n) \circ \text{tl}]
$$

(purge n) $\equiv$ null $\rightarrow \bar{\phi}$; (cellname n) $\circ 1 \rightarrow$ (purge n) $\circ \text{tl}$;

$$
\text{apndl} \circ [1, (\text{purge } n) \circ \text{tl}]
$$

$\downarrow n \equiv$ pair $\rightarrow$ (push n)$[1, (\text{pop } n) \circ 2]$; $\bot$

The above functional forms work as follows. For $x \neq \bot$, (cellname n):x is T if x is a cell named n, otherwise it is F. (pop n):y removes the first cell named n from a sequence y; (purge n):y removes all cells named n from y. (push n):$<x,y>$ puts a cell named n with contents x at the head of sequence y; $\downarrow n:<x,y>$ is (push n):$<x, (\text{pop } n):y>$.

(Thus (push n):$<x,y>$ = y' pushes x onto the top of a "stack" named n in y'; x can be read by $\uparrow n:y' = x$ and can be removed by (pop n):y'; thus $\uparrow n \circ (\text{pop } n):y'$ is the element below x in the stack n, provided there is more than one cell named n in y'.)

13.3.5 Definitions in FFP systems. The semantics of an FFP system depends on a fixed set of definitions D (a sequence of cells), just as an FP system depends on its informally given set of definitions. Thus the semantic function $\mu$ depends on D; altering D gives a new $\mu'$ that reflects the altered definitions. We have represented D as an object because in AST systems (Section 14) we shall want to transform D by applying functions to it and to fetch data from it—in addition to using it as the source of function definitions in FFP semantics.

If $<CELL,n,c>$ is the first cell named n in the sequence D (and n is an atom) then it has the same effect as the FP definition Def $n \equiv \rho c$, that is, the meaning of $(n:x)$ will be the same as that of $\rho c:x$. Thus for example, if $<CELL,CONST,<COMP,2,1>>$ is the first cell in D named CONST, then it has the same effect as Def $CONST \equiv 2 \circ 1$, and the FFP system with that D would find

$$
\mu(CONST:<<x,y>,z>) = y
$$

and consequently

$$
\mu(<CONST,A>:B) = A.
$$

In general, in an FFP system with definitions D, the meaning of an application of the form (atom:x) is dependent on D; if $\uparrow atom:D \neq \#$ (that is, atom is defined in D) then its meaning is $\mu(c:x)$, where $c = \uparrow atom:D$, the contents of the first cell in D named atom. If $\uparrow atom:D = \#$, then atom is not defined in D and either atom is primitive, i.e. the system knows how to compute $\rho atom:x$, and $\mu(atom:x) = \mu(\rho atom:x)$, otherwise $\mu(atom:x) = \bot$.

### 13.4 Formal Semantics for FFP Systems {#backus-1978-vonneumann-s13-4 .section tag=0577}

We assume that a set A of atoms, a set D of definitions, a set P $\subset$ A of primitive atoms and the primitive functions they represent have all been chosen. We assume that $\rho a$ is the primitive function represented by a if a belongs to P, and that $\rho a = \bot$ if a belongs to Q, the set of atoms in A-P that are not defined in D. Although $\rho$ is defined for all expressions (see 13.3.3), the formal semantics uses its definition only on P and Q. The functions that $\rho$ assigns to other expressions x are implicitly determined and applied in the following semantic rules for evaluating $\mu(x:y)$. The above choices of A and D, and of P and the associated primitive functions determine the objects, expressions, and the semantic function $\mu_D$ for an FFP system. (We regard D as fixed and write $\mu$ for $\mu_D$.) We assume D is a sequence and that $\uparrow y:D$ can be computed (by the function $\uparrow y$ as given in Section 13.3.4) for any atom y. With these assumptions we define $\mu$ as the least fixed point of the functional $\tau$, where the function $\tau \mu$ is defined as follows for any function $\mu$ (for all expressions x, $x_i$, y, $y_i$, z, and w):

$$
(\tau \mu)x \equiv x \in A \rightarrow x;
$$

$$
x = <x_1, ..., x_n> \rightarrow <\mu x_1, ..., \mu x_n>;
$$

$$
x = (y:z) \rightarrow
$$

$$
(y \in A \& (\uparrow y:D) = \# \rightarrow \mu((\rho y)(\mu z));
$$

$$
y \in A \& (\uparrow y:D) = w \rightarrow \mu(w:z);
$$

$$
y = <y_1, ..., y_n> \rightarrow \mu(y_1:<y,z>);\mu(\mu y:z)); \bot
$$

The above description of $\mu$ expands the operator of an application by definitions and by metacomposition before evaluating the operand. It is assumed that predicates like "x $\in$ A" in the above definition of $\tau \mu$ are $\bot$-preserving (e.g., "$\bot \in A$" has the value $\bot$) and that the conditional expression itself is also $\bot$-preserving. Thus $(\tau \mu)\bot \equiv \bot$ and $(\tau \mu)(\bot:z) \equiv \bot$. This concludes the semantics of FFP systems.
