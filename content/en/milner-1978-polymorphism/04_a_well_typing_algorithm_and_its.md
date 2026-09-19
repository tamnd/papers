---
paper: milner-1978-polymorphism
title: A Theory of Type Polymorphism in Programming
authors:
  - Robin Milner
year: 1978
venue: Journal of Computer and System Sciences
field: languages
section: "4"
section_title: A Well-Typing Algorithm and Its Correctness
tag: 054F
kind: section
lang: en
source: https://doi.org/10.1016/0022-0000(78)90014-4
pdf_sha256: a55f1fb81848085165c55a73c33f28b5d25f3b7bdcfa782c462af7997faad6bc
pdf_pages: 19-25
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 08ede47223eb3e0286a5030522d1c008f87a1ec7580dbbaae8c80f962c3073fe
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

### 4.1. The Algorithm $\mathcal{W}$ {#milner-1978-polymorphism-s4-1 .section tag=0550}

In this section we tackle the question of finding a well typing for a prefixed expression. We present an algorithm $\mathcal{W}$ for this. We would like to prove that $\mathcal{W}$ is both syntactically sound and (in some sense) complete. By syntactic soundness, we mean that whenever $\mathcal{W}$ succeeds it produces a wt; by completeness, we mean that whenever a wt exists, $\mathcal{W}$ succeeds in finding one which is (in some sense) at least as general.

Although $\mathcal{W}$ is probably complete, it is difficult to find a simple proof. So we concentrate on soundness, and then comment on implementation of $\mathcal{W}$ and on extending it to deal with richer languages. Since a type-checking algorithm which simulates $\mathcal{W}$ has been working successfully for nearly 2 years in the context of the LCF metalanguage ML [2], we have evidence for its usefulness and even—to some extent—for its completeness.

$\mathcal{W}$ is based on the unification algorithm of Robinson [14]. Indeed, the only feature of well typing which does not fall directly within the framework of unification is the condition that $\tau$ should be a generic instance of $\sigma$ whenever $x_{\tau}$ is bound by let $x_{\sigma}$. The completeness (in some sense) of $\mathcal{W}$ should follow from the second part of the following proposition concerning unification, but we need only the first half for our proof that $\mathcal{W}$ is sound.

Proposition 5 (Robinson). *There is an algorithm $\mathcal{U}$, taking a pair of expressions (over some alphabet of variables) and yielding a substitution, such that for any pair of expressions $\sigma$ and $\tau$* {#milner-1978-polymorphism-prop-5 .statement tag=0551}

(A) *If $\mathcal{U}(\sigma, \tau)$ succeeds, yielding $U$, then $U$ unifies $\sigma$ and $\tau$ (i.e., $U\sigma = U\tau$).*

(B) *If $R$ unifies $\sigma$ and $\tau$, then $\mathcal{U}(\sigma, \tau)$ succeeds yielding a $U$ such that for some substitution $S$, $R = SU$.*

Moreover, $U$ involves only variables in $\sigma$ and $\tau$.

To find a well typing of a complete program $f$, we would expect to supply also a typed prefix $\bar{p}$, containing only *let* bindings, giving the types of values bound to predefined identifiers. We would then expect $\mathcal{W}$ to yield $\vec{f}$ such that $\bar{p} \mid \vec{f}$ is a wt.

To state (and prove) $\mathcal{W}$ recursively however, prefixes containing all types of binding occur, and $\mathcal{W}$ in general needs to modify the nongeneric type variables in the prefix to meet constraints imposed on the program. We therefore make $\mathcal{W}$ return also a substitution $T$, indicating the necessary transformation.

To be precise, we show that if $\mathcal{W}(\bar{p}, f)$ succeeds and returns $(T, \vec{f})$, then $(T\bar{p})|\vec{f}$ is a wt.

We first state $\mathcal{W}$. At certain points $\mathcal{W}$ requires type variables which have not previously occurred; such new type variables are denoted by $\beta$ or $\beta_i$. $\mathcal{W}(\bar{p}, f)$ is defined by induction on the structure of $f$; the algorithm is expressed in a purely applicative programming style, in contrast with the more efficient algorithm $\mathcal{J}$ presented later, which is expressed more in the style of imperative programming.

Algorithm $\mathcal{W}$

$$
\mathcal{W}(\bar{p}, f) = (T, \vec{f}), \text{ where}
$$

(i) If $f$ is $x$, then:
    if $\lambda x_\sigma$ or $fix\ x_\sigma$ is active in $\bar{p}$ then
        $T = I, \vec{f} = x_\sigma$;
    if let $x_\sigma$ is active in $\bar{p}$ then
        $T = I, \vec{f} = x_\tau$
    where $\tau = [\beta_i/\alpha_i]\sigma$, $\alpha_i$ are the generic variables of $\sigma$,
    and $\beta_i$ are new variables.

(ii) If $f$ is $(de)$, then:
    let $(R, \vec{d}_\rho) = \mathcal{W}(\bar{p}, d)$, and $(S, \vec{e}_\sigma) = \mathcal{W}(R\bar{p}, e)$;
    let $U = \mathcal{U}(S\rho, \sigma \to \beta)$, $\beta$ new;
    then $T = USR$, and $\vec{f} = U(((S\vec{d})\vec{e})_\beta)$.

(iii) If $f$ is $(if\ d\ then\ e\ else\ e')$, then:
    let $(R, \vec{d}_\rho) = \mathcal{W}(\bar{p}, d)$ and $U_0 = \mathcal{U}(\rho, i_0)$;
    let $(S, \vec{e}_\sigma) = \mathcal{W}(U_0R\bar{p}, e)$, and $(S', \vec{e}'_\sigma) = \mathcal{W}(SU_0R\bar{p}, e')$;
    let $U = \mathcal{U}(S'\sigma, \sigma')$;
    then $T = US'SU_0R$, and
        $\vec{f} = U((if\ S'SU_0\vec{d}\ then\ S'\vec{e}\ else\ \vec{e}')_\sigma)$.

(iv) If $f$ is $(\lambda x \cdot d)$, then:
    let $(R, \vec{d}) = \mathcal{W}(\bar{p} \cdot \lambda x_\beta , d)$, where $\beta$ is new;
    then $T = R$, and $\vec{f} = (\lambda x_{R\beta} \cdot \vec{d}_\rho)_{R\beta \to \rho}$.

(v) If $f$ is $(fix\ x \cdot d)$, then:
    let $(R, \vec{d}_\rho) = \mathcal{W}(\bar{p} \cdot fix\ x_\beta , d)$, $\beta$ new;
    let $U = \mathcal{U}(R\beta, \rho)$;
    then $T = UR$, and $\vec{f} = (fix\ x_{UR\beta} \cdot Ud)_{UR\beta}$.

(vi) If $f$ is $(let\ x = d\ in\ e)$, then:
    let $(R, \vec{d}_\rho) = \mathcal{W}(\bar{p}, d)$;
    let $(S, \vec{e}_\sigma) = \mathcal{W}(R\bar{p} \cdot let\ x_\rho , e)$;
    then $T = SR$, and $\vec{f} = (let\ x_{S\rho} = S\vec{d}\ in\ \vec{e})_\sigma$.

### 4.2. *The Soundness of $\mathcal{W}$* {#milner-1978-polymorphism-s4-2 .section tag=0552}

To show that $\mathcal{W}$ is sound it is convenient to have a few simple definitions.
If $A$ is a type, a typed prefix, or a typed pe then

$$
\operatorname{Vars}(A) \overset{\mathrm{def}}{=} \{ \alpha \mid \alpha \in A, \alpha \text{ a type variable} \}.
$$

If $A$ is a typed prefix or a typed pe then

$$
\operatorname{Gen}(A) \overset{\mathrm{def}}{=} \{ \alpha \mid \alpha \in A, \alpha \text{ a generic type variable} \}.
$$

$$
\operatorname{Spec}(A) \overset{\mathrm{def}}{=} \operatorname{Vars}(A) - \operatorname{Gen}(A).
$$

If $S$ is a substitution, then

$$
\operatorname{Inv}(S) \overset{\mathrm{def}}{=} \{ \alpha \mid S \text{ involves } \alpha \}
$$

$$
= \{ \alpha \mid \exists \beta \cdot S\beta \neq \beta \text{ and } \alpha \in \{ \beta \} \cup \operatorname{Vars}(S\beta) \}.
$$

We need the following simple properties, whose proof we omit:

**Proposition 6.** (A) $\operatorname{Inv}(RS) \subseteq \operatorname{Inv}(R) \cup \operatorname{Inv}(S)$ {#milner-1978-polymorphism-prop-6 .statement tag=0553}
(B) $\operatorname{Vars}(S\tau) \subseteq \operatorname{Vars}(\tau) \cup \operatorname{Inv}(S)$.

**Theorem 2** (Syntactic Soundness). *Let $\bar{p}$ be a standard prefix, and $p \mid f$ a (closed) pe. Then, if $\mathcal{W}(\bar{p}, f) = (T, \bar{f}_\tau)$,* {#milner-1978-polymorphism-thm-2 .statement tag=0554}

(A) $T\bar{p} \mid \bar{f}$ is wt,
(B) $\operatorname{Inv}(T) \subseteq \operatorname{Spec}(\bar{p}) \cup New$,
and
(C) $\operatorname{Vars}(\tau) \subseteq \operatorname{Spec}(\bar{p}) \cup New$,

*where New is the set of new type variables used by $\mathcal{W}$.*

*Proof.* By induction on the structure of $f$, using the recursive definition of wt. We omit the cases of conditional and fix expressions, since nothing new arises there, and we treat the easier of the other cases first

(i) $f$ is $x$. Then $T = I$, so (B) is immediate. If $\lambda x_\sigma$ or $fix\ x_\sigma$ is active in $\bar{p}$ then $\bar{f} = x_\sigma$ and (A), (C) are immediate.

*If let $x_\sigma$ is active, then $\bar{f} = x_\tau$, where $\tau = [\beta_i/\alpha_i]\sigma, \{ \alpha_i \}$ generic in $\sigma$, $New = \{ \beta_i \}$. Then $T\bar{p} \mid \bar{f} = \bar{p} \mid x_\tau$ is standard and (A), (C) follow easily.*

(iv) $f$ is $(\lambda x \cdot d)$. Let $(R, \bar{d}_\rho) = \mathcal{W}(\bar{p} \cdot \lambda x_\beta , d)$, using new variables $New_1$, say.

By induction, $R(\bar{p} \cdot \lambda x_\beta) | \vec{d}_\rho$ is wt, so for (A) $f = R\bar{p} | (\lambda x_{R\beta} \cdot \vec{d})_{R\beta \to \rho}$ is wt (defn of wt).
Also by induction,

$$
\begin{align*}
\operatorname{Inv}(R)\{ & \subseteq \operatorname{Spec}(\bar{p} \cdot \lambda x_\beta) \cup \operatorname{New}_1 \\
\operatorname{Vars}(\rho)\{ & = \operatorname{Spec}(\bar{p}) \cup \{\beta\} \cup \operatorname{New}_1 \\
& = \operatorname{Spec}(\bar{p}) \cup \operatorname{New} \quad \text{(since New} = \operatorname{New}_1 \cup \{\beta\})
\end{align*}
$$

and (B) follows since $T = R$. For (C)

$$
\operatorname{Vars}(R\beta \to \rho) \subseteq \operatorname{Inv}(R) \cup \{\beta\} \cup \operatorname{Vars}(\rho) \quad \text{by Proposition 6,}
$$

$$
\subseteq \operatorname{Spec}(\bar{p}) \cup New
$$

as required.

(vi) $f$ is (let $x = d$ in $e$). Then let $(R, \vec{d}_\rho) = \mathcal{W}(\bar{p}, d)$, using new variables $New_1$, say. Then by induction

$$
R\bar{p} | \vec{d} \text{ is wt} \tag{1}
$$
{#milner-1978-polymorphism-eq-1 .equation tag=0555}

$$
\operatorname{Inv}(R)\{ \subseteq \operatorname{Spec}(\bar{p}) \cup \operatorname{New}_1 \tag{2}
$$
{#milner-1978-polymorphism-eq-2 .equation tag=0556}

Now from (2)

$$
\operatorname{Spec}(R\bar{p}) \subseteq \operatorname{Inv}(R) \cup \operatorname{Spec}(\bar{p})
$$

$$
\subseteq \operatorname{Spec}(\bar{p}) \cup \operatorname{New}_1 \tag{3}
$$
{#milner-1978-polymorphism-eq-3 .equation tag=0557}

and from (1) by standardness

$$
\operatorname{Gen}(R\bar{p} | \vec{d}) \cap \operatorname{Spec}(R\bar{p}) = \varnothing. \tag{4}
$$
{#milner-1978-polymorphism-eq-4 .equation tag=0558}

We also have that $\operatorname{Gen}(R\bar{p}) = \operatorname{Gen}(\bar{p})$, which is disjoint from $\operatorname{Vars}(\rho)$ by (2), hence $R\bar{p} \cdot let x_\rho$ is a standard prefix.

So let $S, \bar{e}_\sigma = \mathcal{W}(R\bar{p} \cdot let x_\rho, e)$ using new variables $New_2$. Then by induction

$$
S(R\bar{p} \cdot let x_\rho) | \bar{e} \text{ is wt} \tag{5}
$$
{#milner-1978-polymorphism-eq-5 .equation tag=0559}

$$
\operatorname{Inv}(S)\{ \subseteq \operatorname{Spec}(R\bar{p} \cdot let x_\rho) \cup \operatorname{New}_2 \tag{6}
$$
{#milner-1978-polymorphism-eq-6 .equation tag=055A}

But $\operatorname{Spec}(R\bar{p} \cdot let x_\rho) = \operatorname{Spec}(R\bar{p})$, so putting (6) and (4) together yields (since $New_2$ are new variables)

$$
\operatorname{Inv}(S) \cap \operatorname{Gen}(R\bar{p} | \vec{d}) = \varnothing
$$

and it follows by Proposition 4 that $S(R\bar{p} | \vec{d})$ is wt, and using (5) we have by definition of wt that

$$
SR\bar{p} | (let x_{S_\rho} = Sd \text{ in } \bar{e})_\sigma
$$

is wt; but this is just $T\bar{p} \mid \vec{f}$, so we have proved (A). For (B), we have

$$
\begin{align*}
\operatorname{Inv}(T) &\subseteq \operatorname{Inv}(S) \cup \operatorname{Inv}(R), \text{ by Proposition 6}, \\
&\subseteq \operatorname{Spec}(\bar{p}) \cup New_1 \cup New_2, \text{ using (6), (3), and (2)}
\end{align*}
$$

and for (C), by similar reasoning,

$$
\operatorname{Vars}(\sigma) \subseteq \operatorname{Spec}(\bar{p}) \cup New_1 \cup New_2.
$$

This is all we need, since $New = New_1 \cup New_2$ in this case.

(ii) $f$ is ($de$). Let $(R, \vec{d}_o) = \mathcal{W}(\bar{p}, d)$, using new variables $New_1$, and $(S, \bar{e}_o) = \mathcal{W}(R\bar{p}, e)$, using new variables $New_2$; then by similar reasoning to case (vi) we find that

$$
\begin{align*}
SR\bar{p} \mid S(\vec{d}_o) &\quad \text{is wt} \tag{7} \\
SR\bar{p} \mid \bar{e}_o &\quad \text{is wt} \tag{8} \\
\operatorname{Inv}(SR)\} \subseteq \operatorname{Spec}(\bar{p}) \cup New_1 \cup New_2. \tag{9}
\end{align*}
$$
{#milner-1978-polymorphism-eq-7 .equation tag=055B}

Now if $U = \mathcal{U}(S\rho, \sigma \to \beta)$, where $\beta$ is new, we have by Proposition 5 that

$$
\begin{align*}
US\rho &= U\sigma \to U\beta, \tag{10} \\
\operatorname{Inv}(U) &\subseteq \operatorname{Vars}(S\rho) \cup \operatorname{Vars}(\sigma) \cup \{\beta\}. \tag{11}
\end{align*}
$$
{#milner-1978-polymorphism-eq-10 .equation tag=055C}

It follows that $U$ involves no generic variables of the wt's (7) and (8), and that

$$
USR\bar{p} \mid U(((S\vec{d})\bar{e})_\beta)
$$

is wt; but this is just $T\bar{p} \mid \vec{f}$, so we have proved (A). For (B), we have first that

$$
New = New_1 \cup New_2 \cup \{\beta\},
$$

so

$$
\begin{align*}
\operatorname{Inv}(T) &\subseteq \operatorname{Inv}(U) \cup \operatorname{Inv}(SR), \quad \text{by Proposition 6}, \\
&\subseteq \operatorname{Spec}(\bar{p}) \cup New, \quad \text{from (9) and (11)},
\end{align*}
$$

and for (C),

$$
\begin{align*}
\operatorname{Vars}(\tau) &= \operatorname{Vars}(U\beta) \\
&\subseteq \operatorname{Inv}(U) \cup \{\beta\}, \quad \text{by Proposition 6}, \\
&\subseteq \operatorname{Spec}(\bar{p}) \cup New, \quad \text{again from (9) and (11)}.
\end{align*}
$$

### 4.3. *Implementation of $\mathcal{W}$; a Simplified Algorithm $\mathcal{J}$* {#milner-1978-polymorphism-s4-3 .section tag=055D}

As it stands, $\mathcal{W}$ is hardly an efficient algorithm; substitutions are applied too often. It was formulated to aid the proof of soundness. We now present a simpler algorithm $\mathcal{J}$ which simulates $\mathcal{W}$ in a precise sense.

$\mathcal{I}$ differs from $\mathcal{W}$ in two ways. First, we adopt an idea familiar in the literature on resolution-based theorem-proving systems, in which substitutions are *composed*, but only *applied* when it is essential to do so. Second, we take advantage of the fact that what is often needed in practice from a well-typing algorithm is not the whole type assignment $f$, but only the type assigned to $f$ itself.

In fact $\mathcal{I}$ builds only one substitution, called $E$, which is idempotent—that is, $EE = E$—which is to say that if $\beta \in E\alpha$, then $E\beta = \beta$. This substitution is held in a program variable (called $E$) global to $\mathcal{I}$, and $\mathcal{I}$ works by transforming $E$. In place of the unification function $\mathcal{U}$, $\mathcal{I}$ calls a unification procedure UNIFY which delivers no result but side-effects the variable $E$. We assume that $\mathcal{U}$ and UNIFY are related as follows: of $E$ and $E'$ are the values of $E$ before and after the command

$$
\text{UNIFY}(\sigma, \tau)
$$

and if

$$
\mathcal{U}(E\sigma, E\tau) = U
$$

then

$$
E' = UE.
$$

Thus, applying UNIFY to types $\sigma$ and $\tau$ in the presence of $E$ corresponds to applying $\mathcal{U}$ to types $E\sigma$ and $E\tau$; $\sigma$ and $\tau$ may be thought of as *implicit* types standing for the *explicit* types which would be gained by applying the "explicating" substitution $E$ (the idempotency of $E$ means that further explication is unnecessary). The effect of UNIFY (if successful) is to generate the new explicating substitution $E'$. $\mathcal{I}$ will similarly handle an implicit typed prefix $\bar{p}$, which can be explicated when necessary by applying $E$. We assume that $\mathcal{I}$ has local variables $\rho, \sigma,$ and $\sigma'$, whose values are implicit types, and generates its result in a fourth variable $\tau$.

Assuming an initial idempotent $E$, $\mathcal{I}$ is given a typed prefix $\bar{p}$ and an expression $f$ such that $E\bar{p}$ is standard and $p \mid f$ is a pe (i.e., all free identifiers in $f$ are bound in $p$). Here is the algorithm:

*Algorithm* $\mathcal{I}$

$$
\mathcal{I}(\bar{p}, f) = \tau, \text{ where}
$$

(i) If $f$ is $x$, then:

If $\lambda x_\sigma$ or *fix* $x_\sigma$ is active in $\bar{p}$, $\tau := \sigma$.
If *let* $x_\sigma$ is active in $\bar{p}$, $\tau := [\beta_i/\alpha_i]E\sigma$, where
$\alpha_i$ are the generic type variables of *let* $x_{E\sigma}$ in $E\bar{p}$,
and $\beta_i$ are new variables.

(ii) If $f$ is (*de*) then:

$$
\rho := \mathcal{I}(\bar{p}, d); \quad \sigma := \mathcal{I}(\bar{p}, e);
$$

UNIFY ($\rho, \sigma \rightarrow \beta$); ($\beta$ new)

$$
\tau := \beta
$$

(iii) If $f$ is (*if d then e else e'*, then:

$$
\rho := \mathcal{J}(\bar{p}, d); \text{UNIFY } (\rho, \iota_0);
$$

$$
\sigma := \mathcal{J}(\bar{p}, e); \sigma' := \mathcal{J}(\bar{p}, e');
$$

$$
\text{UNIFY}(\sigma, \sigma'); \tau := \sigma
$$

(iv) If $f$ is $(\lambda x \cdot d)$, then:

$$
\rho := \mathcal{J}(\bar{p} \cdot \lambda x_\beta , d); (\beta \text{ new})
$$

$$
\tau := \beta \rightarrow \rho
$$

(v) If $f$ is (*fix x \cdot d*), then:

$$
\rho := \mathcal{J}(\bar{p} \cdot fix x_\beta , d); (\beta \text{ new})
$$

$$
\text{UNIFY}(\beta, \rho); \tau := \beta
$$

(vi) If $f$ is (*let x = d in e*) then:

$$
\rho := \mathcal{J}(\bar{p}, d); \sigma := \mathcal{J}(\bar{p} \cdot \text{let } x_\rho , e);
$$

$$
\tau := \sigma.
$$

What is the simulation relation between $\mathcal{J}$ and $\mathcal{W}$? It is simply expressed by the following proposition, whose proof we omit, since it is an easy structural induction involving few of the subtleties which we encountered in the soundness theorem.

PROPOSITION 7. *Let p | f be a pe, E be idempotent, and Ep̄ be standard. Then $\mathcal{J}(\bar{p}, f)$ succeeds (producing $\tau'$ and a new value $E'$ for $E$) iff $\mathcal{W}(Ep̄, f)$ succeeds (producing T and $f_{\tau'}$), and moreover if both succeed*

(A) $E' = TE,$
(B) $E'\tau' = \tau.$

Thus the type produced by $\mathcal{J}$, when explicated, is exactly that ascribed to $f$ by $\mathcal{W}$.
In practice, $E$ may be efficiently represented by a table INST of variable-type pairs, representing those variables which have hitherto been instantiated. The effect of UNIFY is merely to add some entries to INST, representing instantiation of previously uninstantiated variables. The substitution $E$ represented by INST is given recursively as follows

$$
E(i) = i \quad \text{(basic types)},
$$

$$
E(\alpha) = E(\rho) \quad \text{if } (\alpha, \rho) \in \text{INST for some } \rho,
$$

$$
= \alpha \quad \text{otherwise},
$$

$$
E(\sigma \rightarrow \tau) = E\sigma \rightarrow E\tau.
$$

In fact, in the extended version of $\mathcal{J}$ implemented for ML, which is written in LISP, INST itself is represented by a property (in the LISP sense) INSTANCE of type variables. Each type variable $\alpha$ has $\rho$ as its INSTANCE property value, if $(\alpha, \rho) \in \text{INST}$ for some $\rho$; otherwise the property value is NIL.
