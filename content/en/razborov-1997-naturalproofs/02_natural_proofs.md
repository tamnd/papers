---
paper: razborov-1997-naturalproofs
title: Natural Proofs
authors:
  - Alexander A. Razborov
  - Steven Rudich
year: 1997
venue: Journal of Computer and System Sciences
field: theory
section: "2"
section_title: Natural proofs
tag: 020D
kind: section
lang: en
source: https://doi.org/10.1006/jcss.1997.1494
pdf_sha256: 6cf137cf878d01654aeff5dbf031e97a624cd72367b87415ff61080447de7682
pdf_pages: 3-7
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: db6b30bcce013dbf6553ef009f9b6e815e3f1d72f8295f072b41e40105ae0b05
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

### 2.1. Natural combinatorial properties {#razborov-1997-naturalproofs-s2-1 .section tag=020E}

We start by de ning what we mean by a \natural combinatorial property"; natural proofs will be those that use a natural combinatorial property.

Formally, by a combinatorial property of Boolean functions we will mean a set of Boolean functions f C n F n j n 2 ! g . Thus, a Boolean function f n will possess property C n if and only if f n 2 C n . (Alternatively, we will sometimes nd it convenient to use function notation: C n ( f n ) = 1 if f n 2 C n , and C n ( f n ) = 0 if f n 62 C n .) The combinatorial property C n is natural if it contains a subset C n with the following two conditions:

Constructivity: The predicate f n 2 C n is in P . Thus, C n is computable in time which

? is polynomial in the truth table of f n ;

Largeness: j C j 2 ? O ( n ) j F j .

n n A combinatorial property C n is useful against P=poly if it satis es:

Usefulness: The circuit size of any sequence of functions f 1 ; f 2 ; : : : ; f n ; : : : , where f n 2 C n , is super-polynomial, i.e., for any constant k , for suciently large n , the circuit size of f is greater than n k .

n A proof that some function does not have polynomial-sized circuits is natural against P=poly if the proof contains, more or less explicitly, the de nition of a natural combinatorial property C n which is useful against P=poly .

Note that the de nition of a natural proof, unlike that of a natural combinatorial property, is not precise. This is because while the notion of a property being explicitly de ned in a journal paper is perfectly clear to the working mathematician, it is a bit slippery to formalize. This lack of precision will not a ect the precision of our general statements about natural proofs (see Section 4) because they will appear only in the form \there exists (no) natural proof : : : ", and should be understood as equivalent to \there exists (no) natural combinatorial property C n : : : "

The de nitions of natural property and natural proof can be explained much less formally. First, a proof that some explicit function f g n g does not have polynomial-sized circuits must plainly identify some combinatorial property C n of g n that is used in the proof. That is, the proof will show that all functions f n that have this property, including g n itself, are hard to compute. In other words, C n is useful . If f g n g 2 NP , then the proof concludes P 6 = NP . Our main contention, backed by evidence in the next section, is that current proof techniques would strongly tend to make this C n large and constructive as de ned above. (Or at least these two conditions would hold for some sub-property C n of C n .)

In order to understand the de nition of large more intuitively, let N = 2 n . Largeness requires that j C n j 1 for some xed k > 0, i.e., f has a non-negligible chance of having j F n j N k n property C n .

Constructivity is a more subtle notion to understand and justify. We take as our basic benchmark of \constructive" that f 2 C be decidable in time 2 O ( n ) , i.e., polynomial n n as a function of 2 n . Now, this is exponential in the number n of variables in f , and n this makes our concept somewhat mysterious, especially since we are going to employ it for studying computations which are polynomial in n ! The best justi cation we have is empirical: the vast majority of properties of Boolean functions or n -vertex graphs (etc.) that one encounters in combinatorics are at worst exponential-time decidable, and, as a matter of fact, known lower bounds proofs operate only with such properties. It also should be noted that even with this loose notion of constructivity we manage to prove in Section 4 strong negative results on the non-existence of natural proofs.

More speci cally, consider a commonly-envisioned proof strategy for proving P 6 = NP :

Formulate some mathematical notion of \discrepancy" or \scatter" or \variation" of the values of a Boolean function, or of an associated polytope or other structure. (In our terms, this notion would be formalized as a combinatorial property C n that is true of any function with suciently high discrepancy.)

Show by an inductive argument that polynomial-sized circuits can only compute functions of \low" discrepancy. (In our terms, this would mean showing that C n is \useful", because any function with property C n can't be computed by a polynomialsized circuit.)

Then show that SAT, or some other function in NP , has \high" discrepancy. (In our terms, this means showing that SAT has property C n .)

Our main theorem in Section 4 gives evidence that no proof strategy along these lines can ever succeed . We show that any large and constructive C n that is useful against P=poly provides a statistical test that can be used to break any polynomial-time pseudo-random number generator. Speci cally, it would violate the fairly widely believed conjecture that there exist pseudo-random generators of hardness 2 n , for some > 0 (e.g., the standard n 1 = 3 generator based on the discrete logarithm function [9] is believed to be 2 -hard).

What we are saying, subject to the truth of the hard pseudo-random generator conjecture, is this: Any proof that some function f f n g does not have small circuits must either seize on some very specialized property of f n , i.e. one shared by only a negligible fraction of functions, or must de ne a very complicated property C n , one outside the bounds of most mathematical experience. In our terms, the proof must be unnatural by violating either \largeness" or \constructivity." In Section 5 we give some solid theoretical evidence for largeness, by showing that any C n based on a formal complexity measure must be large. We do not have any similar formal evidence for constructivity, but from experience it is plausible to say that we do not yet understand the mathematics of C n outside exponential time (as a function of n ) well enough to use them e ectively in a combinatorial style proof.

We make this point in Section 3, where we argue that all known lower bound proofs against non-monotone circuits are natural by our de nition.

The best example of a purportedly unnatural argument is a traditional counting argument. The combinatorial property C n would just be something asserting that f f n g is not in P=poly (e.g., C ( f ) = 1 exactly when the complexity of f is greater than n log n ). The n n n proof that C n is large does not give us the least hint as to how to prove the existence of a large constructive subset C n C n . Moreover, a consequence of Theorem 4.1 is that if our pseudo-random generator assumption is true then such C n cannot exist at all! Thus, a counting argument is presumably not a natural argument. This poses no problem for us since counting arguments (closely associated with diagonalization arguments) have yet not proved any lower bounds for explicit functions (except when counting is used for limited purposes, as in [36, 5]. These examples perfectly t our general framework { see Sections 3.2.1, 3.4.) The question of whether (unlimited) counting or diagonalization arguments are suciently powerful to resolve barrier problems in complexity theory predates the combinatorial style lower bounds of the 1980s. Our results have nothing to say { one way or the other { concerning the future promise of diagonalization and counting arguments.

Another exception to our scheme is the list of strong lower bounds proofs against monotone circuit models [2, 3, 4, 17, 26, 27, 28, 37]. Here the issue is not constructivity { the properties used in these proofs are all feasible { but that there appears to be no good formal analogue of the largeness condition. In particular, no one has formulated a workable de nition of a \random monotone function."

All the lower bound proofs surveyed in this paper explicitly state a natural property, and so are natural proofs. In some cases this property is explicit in the original paper, while in others we need to do some work to bring out a natural property C n that yields the same lower bound. We call this latter process naturalizing the original proof. This can be subtle (see e.g. Section 3.2.1 below). Given C n , one must exhibit C n and prove that it has both the constructivity and largeness conditions. The key to doing this seems to lie in carefully analyzing the lower bound proof that used C n . In the case where a researcher intends to build a lower bound proof around some property C n , evaluating C n for naturalness might be non-trivial. Nonetheless, in light of our framework, such an evaluation could be worthwhile: if it is natural, C n is not a useful property for solving P = ? NP and similar questions. Just as a researcher might rule out an approach to lower bounds because it relativizes, he/she might rule out an approach to circuit lower bounds because it \naturalizes".

### 2.2. Properties which are ? -natural against with density n {#razborov-1997-naturalproofs-s2-2 .section tag=020F}

It is easy and useful to extend the de nition of natural proof to a more general, parameterized version. Understanding this more general de nition is important to understanding the results as presented in this paper.

Let ? and be complexity classes. Call a combinatorial property C n ?- natural with density n if it contains C n C n with the following two conditions:

Constructivity: The predicate f n 2 C n is computable in ? (recall, C n is a set of truth-

? tables with 2 n bits);

Largeness: j C n j n j F n j .

A combinatorial property C n is useful against if it satis es:

Usefulness: For any sequence of functions f n , where the event f n 2 C n happens in nitely often, f f n g 62 .

A lower bound proof that some explicit function is not in is called ?- natural against with density n if it states a ?-natural property C n which is useful against with density n .

The \default" settings of our parameters will be ? = P , = P=poly , and = 2 ? O ( n ) , n as in the initial de nition. Our main result implies the negative statement that, under our pseudo-randomness assumption, no proof with these parameters can show that SAT does not have polynomial-sized circuits. In fact, as we survey the known lower bound arguments they all remain natural even when the parameters are more restrictively adjusted. We are unaware of a lower bound proof for which we cannot exhibit a C n which is P -natural with density close to one. For most known arguments, ? can be restricted to NC 2 or lower. Our full negative result (strengthened by an observation of Razborov [33]) is that, under our pseudo-randomness assumption, no property with ?=quasi-polynomial-sized circuits,

= P=poly , and = 2 ? O ( n ) can exist. Thus, our negative result rules out proofs with n much more inclusive parameters than currently known circuit lower bounds.
