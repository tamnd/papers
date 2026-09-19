---
paper: milner-1978-polymorphism
title: A Theory of Type Polymorphism in Programming
authors:
  - Robin Milner
year: 1978
venue: Journal of Computer and System Sciences
field: languages
section: "1"
section_title: INTRODUCTION
tag: "0540"
kind: section
lang: en
source: https://doi.org/10.1016/0022-0000(78)90014-4
pdf_sha256: a55f1fb81848085165c55a73c33f28b5d25f3b7bdcfa782c462af7997faad6bc
pdf_pages: 2-4
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 02612fbc98993310ed55b492578566cc4faae25784801a2b740ca8bb152ac9c5
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The aim of this work is largely a practical one. A widely employed style of programming, particularly in structure-processing languages which impose no discipline of types (LISP is a perfect example), entails defining procedures which work well on objects of a wide variety (e.g., on lists of atoms, integers, or lists). Such flexibility is almost essential in this style of programming; unfortunately one often pays a price for it in the time taken to find rather inscrutable bugs—anyone who mistakenly applies CDR to an atom in LISP, and finds himself absurdly adding a property list to an integer, will know the symptoms. On the other hand a type discipline such as that of ALGOL 68 [22] which precludes the flexibility mentioned above, also precludes the programming style which we are talking about. ALGOL 60 was more flexible—in that it required procedure parameters to be specified only as "procedure" (rather than say "integer to real procedure")—but the flexibility was not uniform, and not sufficient.

An early discussion of such flexibility can be found in Strachey [19], who was probably the first to call it polymorphism. In fact he qualified it as "parametric" polymorphism, in contrast to what he called "adhoc" polymorphism. An example of the latter is the use of "+*" to denote both integer and real addition (in fact it may be further extended to denote complex addition, vector addition, etc.); this use of an identifier at several distinct types is often now called "overloading," and we are not concerned with it in this paper.

In this paper then, we present and justify one method of gaining type flexibility, but also retaining a discipline which ensures robust programs. We have evidence that this work is not just a theoretical exercise; the polymorphic type discipline which we discuss here has been incorporated in the LCF metalanguage ML [2, 3], and has been in use for nearly 2 years. The compile-time type checker for this language has proved to be a valuable filter which traps a significant proportion of programming errors.

The main body of the present paper is concerned with a technical account—both semantic and syntactic—of our discipline of types in the context of a simple illustrative language, but at this point it is helpful to characterize the approach informally. We outline its predominant features.

First, everything concerning types is done at compile time; once the type checker (part of the compiler) has accepted a program or program phrase, code may be generated which assumes that no objects carry their types at run-time. This is widely accepted as yielding efficient object code, though it does impose constraints on the use of types compared with, for example, the approach in EL1 [21].

Second, many nontrivial programs can avoid mentioning types entirely, since they be inferred from context. (In ML however, as in other languages, the user may—indeed often should—define his own types together with operations over these types. Recent languages which allow the user to define his own types in this manner are CLU [8], ALPHARD [23] and Euclid [6]). Although it can be argued convincingly that to demand type specification for declared variables, including the formal parameters of procedures, leads to more intelligible problems, it is also convenient—particularly in on-line programming—to be able to leave out these specifications. In any case, the type checker which we present is quite simple and could not be made much simpler even if the types of variables were always specified in declarations.

Third, polymorphism plays a leading role. For example, a procedure is assigned a polymorphic type (which we abbreviate to polytype) in general; only when the types of its arguments and result can be uniquely determined from the context is it monomorphic (i.e., assigned a monotype). Gries and Gehani [4], among others, have made a convincing case for controlled polymorphic programming (in contrast with the typeless programming in LISP or in SNOBOL); for them however, and also for Tennent [20], the presence of type variables or identifiers is needed to specify polymorphic types. For us, the polymorphism present in a program is a natural outgrowth of the primitive polymorphic operators which appear to exist in every programming language; such operators are assignment, function application, pairing and tupling, and list-processing operators. It is principally the type constraints on these operators, and in the declaration and use of variables, which determine for us the types of a program phrase and its subphrases.

We do not discuss in this paper—except briefly at the end—either coercions or the "overloading" of identifiers. Our view is that these concepts, and also run-time type manipulation, are somewhat orthogonal to a compile-time polymorphic type discipline, and may (to some extent) be incorporated without invalidating it.

In Section 2 we illustrate our type discipline by examples in a fragment of ML. This fragment should be self-explanatory, but an outline of ML is given in [3] and a full description appears in [2]. These illustrations should serve to make the point that we are able to handle useful languages. The remainder of the paper justifies the discipline using a very simple applicative language, Exp. The justification factors into two parts.

In Section 3 we define the notion of well typing (correct type assignment) and prove the Semantic Soundness Theorem, which says that a well-typed program is semantically free of type violation. If we were to give an operational definition of the language, this would imply that, for example, an integer is never added to a truth value or applied to an argument, and consequently need not carry its type around for run-time checking. In Section 4 we present a well-type algorithm $\mathcal{W}$ and prove the Syntactic Soundness Theorem, which states that $\mathcal{W}$, if it succeeds, produces a well typing of a program. We also give a more efficient algorithm $\mathcal{J}$, which simulates $\mathcal{W}$.

The types in Exp are just the hierarchy of purely functional types over a set of basic types. That is, the polymorphism in Exp is the natural outgrowth of a single primitive polymorphic operator, function application, together with variable binding. To add other primitive polymorphic operators, such as pairing and list-processing operators (as in ML), together with types built from basic ones $\times$ (Cartesian Product), list (list-forming), and $+$ (disjoint sum) in addition to (function type), presents no extra difficulty in the two soundness theorems. Indeed, adding an assignment operator is also easy as far as the Syntactic Soundness Theorem is concerned, but the Semantic Soundness Theorem is harder to extend in this case, due to the extra semantic complication of a memory or store which holds the current values of assignable variables. We discuss this further in Section 5.

Our work is a step towards solving the problem expressed by Morris [10] in his thesis as follows: "to design a language and a type system in which a programmer may define functions whose parameters may have different types for different calls of the function." We recommend Chapter 4 of this thesis as a lucid introduction to the problem. Although Morris does not discuss the semantics of types formally, or give a polymorphic type system, he describes how a valid type assignment may be found for a term of the $\lambda$-calculus by solving a set of simultaneous linear equations; we take this idea further in the next section.

After doing this work we became aware of Hindley's [5] method for deriving the "principal type scheme" (which is what we call a polymorphic type) for a term in combinatory logic. Hindley appears to have been the first to notice that the Unification Algorithm of Robinson [14] is appropriate to this problem. Our work can be regarded as an extension of Hindley's method to programming languages with local declarations, and as a semantic justification of the method.

In summary, we present a polymorphic type discipline which is syntactically well understood and justified for a currently used programming language with imperative features, and is also semantically explained for a nontrivial, though nonimperative, sublanguage.
