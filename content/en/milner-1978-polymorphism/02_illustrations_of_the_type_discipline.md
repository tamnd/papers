---
paper: milner-1978-polymorphism
title: A Theory of Type Polymorphism in Programming
authors:
  - Robin Milner
year: 1978
venue: Journal of Computer and System Sciences
field: languages
section: "2"
section_title: ILLUSTRATIONS OF THE TYPE DISCIPLINE
tag: "0541"
kind: section
lang: en
source: https://doi.org/10.1016/0022-0000(78)90014-4
pdf_sha256: a55f1fb81848085165c55a73c33f28b5d25f3b7bdcfa782c462af7997faad6bc
pdf_pages: 4-10
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 2d14536da9d98145b6a56bc5a07a8cd9a94511e01544fe820adf35ad93f36845
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

We illustrate our notion of polymorphism by means of some simple examples. They are written in a fragment of ML which we hope is self-explanatory; this fragment is indeed no more than Landins ISWIM [7], and we refer the reader to Burge's book [1] in which he uses this style of programming almost exactly. We use no imperative constructs here (assignments or jumps). The constructs

$$
let\ x = e\ in\ e', \\
let\ f(x_1, ..., x_n) = e\ in\ e'
$$

are used to give $x$ the value of $e$, and to give $f$ the value of the abstraction $\lambda(x_1, ..., x_n) \cdot e$, throughout $e'$. For recursive functions *letrec* is used in place of *let*, and when the part *in e'* is omitted we have a declaration.

The fully determined types (i.e., the monotypes) of ML are built from a set of basic types (*int*, *bool*, etc.) by the binary infix operators $\times$ (Cartesian product), $+$ (disjoint sum) and $\rightarrow$ (function type), and the unary postfixed operator *list*. Polymorphic types (polytypes) are obtained by admitting *type variables*, which here are represented by $\alpha, \beta, \gamma \cdots$. We represent arbitrary types by $\rho, \sigma, \tau$. For this section we leave the meaning of types to the reader's intuition; it is made precise in the next section.

**Example 1.** Mapping a function over a list. {#milner-1978-polymorphism-ex-1 .statement tag=0542}

$$
letrec\ map(f, m) = if\ null(m)\ then\ nil \\
else\ cons(f(hd(m)), map(f, tl(m))).
$$

Intuitively, the function map so declared takes a function from things of one sort to things of another sort, and a list of things of the first sort, and produces a list of things of the second sort. So we say that map has type

$$
((\alpha \rightarrow \beta) \times \alpha\ list) \rightarrow \beta\ list,
$$

where $\alpha, \beta$ are type variables.

How is this type determined from the bare declaration of map? First, the *generic* types (we discuss "generic" later) of the identifiers occurring free in the declaration are given by null: $\alpha\ list \rightarrow bool$,
nil: $\alpha\ list$,
hd: $\alpha\ list \rightarrow \alpha$,
tl: $\alpha\ list \rightarrow \alpha\ list$,
cons: $(\alpha \times \alpha\ list) \rightarrow \alpha\ list$, that is, they are polymorphic, because their types contain one or more type variables, and our rule is: To every occurrence of such an identifier is assigned a type which is a substitution instance (substituting types for type variables) of its generic type.

Now each of these identifiers occurs just once in the declaration, so if we denote by $\sigma_{id}$ the type assigned to an identifier id we must have for some types $\tau_1, ..., \tau_5$,

$$
\begin{align*}
\sigma_{null} &= \tau_1\ list \rightarrow bool, \\
\sigma_{nil} &= \tau_2\ list, \\
\sigma_{hd} &= \tau_3\ list \rightarrow \tau_3, \\
\sigma_{tl} &= \tau_4\ list \rightarrow \tau_4\ list, \\
\sigma_{cons} &= (\tau_5 \times \tau_5\ list) \rightarrow \tau_5\ list.
\end{align*}
$$

The other identifiers (map, f, m) each occur more than once, and our rules demand that each occurrence is assigned the same type. The rules also demand that the following equations are satisfied for some types $\rho_1, \rho_2, ...$,

$$
\begin{align*}
\sigma_{map} &= \sigma_f \times \sigma_m \rightarrow \rho_1, \\
\sigma_{null} &= \sigma_m \rightarrow bool, \\
\sigma_{hd} &= \sigma_m \rightarrow \rho_2, \\
\sigma_{tl} &= \sigma_m \rightarrow \rho_3, \\
\sigma_f &= \rho_2 \rightarrow \rho_4, \\
\sigma_{map} &= \sigma_f \times \rho_3 \rightarrow \rho_5, \\
\sigma_{cons} &= \rho_4 \times \rho_5 \rightarrow \rho_6, \\
\rho_1 &= \sigma_{nil} = \rho_6.
\end{align*}
$$

The first of these conditions relates the type of a function to those of its formal parameters; each of the other conditions arises from some subterm which is a function application, except the last, which is because a conditional expression has the same type as its two arms, and because the definiens and definiendum of a declaration have the same type.

Now these equations may be solved for the variables $\rho_i, \tau_i$, and $\sigma_{id}$; Morris [10] discusses the solution of such equations. Indeed, the situation is entirely appropriate for the use of the Unification Algorithm of Robinson [14]; our well-typing algorithm is based upon this algorithm, and (since in this case nothing more than unification is needed) we may conclude from Robinson's work that the most general type of map is obtained, i.e., any other type $\sigma_{map}$ which satisfies the equations must be a substitution instance of the type obtained. In fact, the solution of the above equations is

$$
\sigma_{map} = (\gamma \rightarrow \delta) \times \gamma\ list \rightarrow \delta\ list,
$$

where $\gamma, \delta$ are any distinct type variables. So this is the generic type of map, that is, to any occurrence of map within the scope of this declaration must be assigned some substitution instance of this type.

These instances need not be the same. Suppose that tok is a basic type (a token being a sequence of characters) and that we have available the identifiers (with their types) and
tokl: tok list      (a variable),
length: tok \rightarrow int,
sqroot: int \rightarrow real,    two obvious functions.

Then in the expression map(sqroot, map(length, tokl)) the two occurrence of map will have types

$$
\begin{align*}
((tok \rightarrow int) \times tok\ list) &\rightarrow int\ list, \\
((int \rightarrow real) \times int\ list) &\rightarrow real\ list.
\end{align*}
$$

Similarly, if null, for example, had occurred twice in the definition of map, its types could have been different instances of

$$
\alpha \text{ list } \rightarrow \text{ bool}
$$

but our rules demand that different occurrences of a formal parameter ($f$, for example), or of an identifier (map) being recursively defined, shall have the same type.

In passing, note that the occurrences of map mentioned above can be regarded as uses of two separately declared (and monomorphic!) map functions, which differ only in that different types are explicitly provided for their arguments and results. As Gries and Gehani remark, the compiler could be given the task of generating these distinct declarations—or more accurately (since the programmer need not see the replication or even be aware of it), the task of generating different code for the body of the map function for use at distinct types. This would indeed be necessary in the above example if, for efficiency, token lists were implemented differently from integer lists (and the primitive polymorphic functions hd, tl etc., were correspondingly different). We are concerned with a conceptual framework in which these map functions may all be regarded semantically as the same object; then the implementor is left with the freedom to implement as few or many variants as he wishes.

It is clear from our example that the rules of typing need to be carefully framed. We leave this task until the next section, but here we look at one more example to illustrate what happens when *let* or *letrec* is used locally.

**Example 2.** Tagging. Suppose we want a function tagpair, such that tagpair ($a$) is a function under which {#milner-1978-polymorphism-ex-2 .statement tag=0543}

$$
(b, c) \mapsto ((a, b), (a, c)).
$$

Of course, we can easily write

$$
\text{let tagpair}(a) = \lambda(b, c) \cdot ((a, b), (a, c)).
$$

Now we can explain, without setting up equations, how our well-typing algorithm tackles this declaration. It first assigns "unknown" types (i.e., type variables) $\alpha, \beta,$ and $\gamma$ to $a, b,$ and $c$. Then $((a, b), (a, c))$ acquires type $(\alpha \times \beta) \times (\alpha \times \gamma)$, and the $\lambda$-expression acquires $\beta \times \gamma \rightarrow (\alpha \times \beta) \times (\alpha \times \gamma)$; finally tagpair acquires

$$
\alpha \rightarrow (\beta \times \gamma \rightarrow (\alpha \times \beta) \times (\alpha \times \gamma))
$$

$(*)$

(no type equations have placed any constraint upon the types of $a, b,$ and $c$).

But consider another way of defining tagpair, using the (infixed) function

$$
\#: (\alpha \rightarrow \beta) \times (\gamma \rightarrow \delta) \rightarrow ((\alpha \times \gamma) \rightarrow (\beta \times \delta))
$$

such that $(f \# g)(a, c) = (f(a), g(c))$, and the pairing function

$$
\text{pair: } \alpha \rightarrow (\beta \rightarrow \alpha \times \beta)
$$

such that pair(a)(b) = (a, b). We could write

$$
let\ tagpair = \lambda a \cdot (let\ tag = pair(a)\ in\ tag\ \#\ tag)
$$

We might then expect the well-typing algorithm to proceed as follows. First, $\alpha$ is assigned to $a$. Then, using the generic type of pair, pair(a) acquires $\delta \to \alpha \times \delta$. This is then used as the local generic type of tag, and the two occurrences of tag in tag $\#$ tag are assigned $\beta \to \alpha_1 \times \beta, \gamma \to \alpha_2 \times \gamma$, respectively. The occurrence of $\#$ is assigned an instance of its generic type (again using new type variables) and the type equation for function application will cause the type

$$
\beta \times \gamma \to (\alpha_1 \times \beta) \times (\alpha_2 \times \gamma)
$$

to be assigned to tag $\#$ tag, and to the body of the $\lambda$-expression, so that tagpair acquires the type

$$
\alpha \to (\beta \times \gamma \to (\alpha_1 \times \beta) \times (\alpha_2 \times \gamma)).
$$

Now comparing (*) with (**), something has gone wrong; the second type is too general. The problem is that tag and its generic type depend upon the $\lambda$-bound variable $a$ and its type $\alpha$, and we do not allow different bound occurrences of a $\lambda$-bound variable to have different type. Indeed, as far as type is concerned, we should get the same as if tagpair were defined in yet a third way, by

$$
let\ tagpair = \lambda a \cdot (pair(a)\ \#\ pair(a))
$$

and the reader may be able to obtain (by setting up some equations as in Example 1) the expected type (*) in this case.

The solution is fortunately straightforward. We decree that in instantiating the type of a variable bound by let or by letrec. only those type variables which do not occur in the types of enclosing $\lambda$-bindings (or formal parameter bindings) may be instantiated. We call such instantiable variables (in a generic type) generic type variables.

Now in the second definition of tagpair, the locally defined tag acquired a generic type $\delta \to \alpha \times \delta$, in which $\delta$ is generic but $\alpha$ is not. Thus $\alpha$ should not have been instantiated in assigning types to the occurrences of tag, and then (**) would have been identical with (*). This example may appear a little contrived; indeed, our experience has been that almost always either all or none of the type variables of a generic type are generic. But there seem to be no simple syntactic constraints which would eliminate the exceptions, nor does it seem desirable to do so.

From the examples it becomes clear that the rules for typing variables bound, respectively, by let (or letrec) and by $\lambda$ are going to be different. Thus, although our semantics for the two expressions

$$
let\ x = e\ in\ e'; \qquad (\lambda x \cdot e')e
$$

may be (and are) equivalent, it may be possible to assign types correctly to the former but not to the latter. An example is the pair

$$
let\ I = \lambda x \cdot x\ in\ I(I); \qquad (\lambda I \cdot I(I))(\lambda x \cdot x).
$$

A (partial) intuition for this is that a $\lambda$-abstraction may often occur without an argument; the second expression above contains a special (and rather unnecessary) use of abstraction, in that an explicit argument—$(\lambda x \cdot x)$—is present. Since the *let* construct (when translated) involves this restricted use of an abstraction, it is not unnatural that its rule for type assignment is less constrained. A compiler could, of course, treat all explicit occurrences of $(\lambda x \cdot e')e$ in the less constrained manner.

The treatment of types in the interaction between $\lambda$-bindings (i.e., formal parameter bindings) and *let* bindings is really the core of our approach. It gives a consistent treatment of the nonglobal declaration of a procedure which may contain, as a free variable, a formal parameter of an enclosing procedure. This appears to be one of the more crucial difficulties with polymorphism, and therefore we feel justified in presenting our analysis in terms of a simple language (Exp) which excludes as much as possible that is irrelevant to the difficulty.

The reader may still feel that our rules are arbitrarily chosen and only partly supported by intuition. We certainly do not claim that the rules are the only possible ones, but the results given later demonstrate that they are semantically justified. In fact, we show that a program which admits a correct type assignment cannot fail at run-time due to a type error—or more precisely, that type constraints encoded in its semantics are always satisfied. It follows from this that compile-time type checking (i.e., the attempt to discover a correct type assignment) obviates the need to carry types at run-time, with an obvious gain in the efficiency of implementation.

This is of course a principal aim in compile-time type checking; another is the early detection of programming errors (many of which result in ill-typed programs). Our achievement is to extend type checking to embrace polymorphism. Moreover the type-checking algorithm in its final form (Algorithm $J$ in Section 3) is remarkably simple, even though the proof of the Syntactic Soundness Theorem, which states that—if it succeeds—it produces a correct type assignment, is rather tedious.

We would like to give an independent characterization of the class of programs which can be well typed in our system, but we have no idea how to do this. However, we can give some pointers. At the suggestion of a referee we looked at Burge [1, Chapt. 3] concerning general functions for processing data structures. All of the functions there (with the exception of Section 3.11 which we did not examine) acquired the expected types from the ML type checker after they had been modified in two respects. First, Burge leaves implicit the coercion functions between a disjoint sum type and its summand types; we needed to make these explicit (this point was mentioned in our Introduction). Second, we used the ML abstract type construct (see Section 5 for an example) to formulate the recursive type definitions used by Burge. In this construct, the isomorphism between a defined abstract type and its representation is made explicit and must be used explicitly. To see the need for this requirement consider the case of an $\alpha$-stream, which is defined to be a function which yields a pair consisting of an $\alpha$ and an $\alpha$-stream. The type equation

$$
\alpha\text{-stream} = -- \rightarrow (\alpha \times \alpha\text{-stream})
$$

cannot be solved by unification (unless we allow infinite type expressions). But by treating the equation as an isomorphism, and using two functions to convert back and forth between an abstract type and its representation, this difficulty is removed. We claim that this solution is in keeping with the notion of abstract type (see [8], for example).

On the negative side, there are certainly useful expressions which we cannot well type, though we are not clear how burdensome it is to do without them. An obvious example is Curry's $Y$ combinator.

$$
Y = \lambda f \cdot (\lambda x \cdot f(x(x)))(\lambda x \cdot f(x(x)))
$$

since self-application is ill typed for us. But *letrec* avoids the need for $Y$. More practically, consider

$$
let F(f) = \lambda(a, b) \cdot (f(a), f(b))
$$

which—it may be argued—should accept as argument a function which is polymorphic enough to operate upon $a$ and $b$ of different type. For example,

$$
F(\text{reverse})(x, y)
$$

produces a pair of reversed lists of different type if $x$ and $y$ are lists of different type. Our system rejects such a use of $F$ (since it requires $a$ and $b$ to have the same type), but admits

$$
let \text{reversepair} = \lambda(x, y) \cdot (\text{reverse}(x), \text{reverse}(y))
$$

or any other specialization of the function argument of $F$.

We feel that this example illustrates the main limitation of our system, but that we may have kept as much flexibility as is possible without the use of explicit type parameters. When these are introduced, the problem arises of the type of types; Reynolds [12] has made some progress in solving this problem, but we were anxious to see how much could be done while avoiding it.
