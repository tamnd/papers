---
paper: razborov-1997-naturalproofs
title: Natural Proofs
authors:
  - Alexander A. Razborov
  - Steven Rudich
year: 1997
venue: Journal of Computer and System Sciences
field: theory
section: "4"
section_title: Inherent limitations of natural proofs
tag: 021A
kind: section
lang: en
source: https://doi.org/10.1006/jcss.1997.1494
pdf_sha256: 6cf137cf878d01654aeff5dbf031e97a624cd72367b87415ff61080447de7682
pdf_pages: 15-19
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 8dea356839fbe805c3e7efa60faed3d4e7d157f41a63c71d50ec53243b2aad43
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

In this section, we argue that natural proofs for lower bounds are almost self-defeating . The idea is that a natural proof that some function f is not in P=poly has an associated algorithm. But just as the proof must distinguish f from a pseudo-random function in P=poly (one being hard the other not), the associated algorithm must be able to tell the di erence between the two. Thus, the algorithm can be used to break a pseudo-random generator. This is self-defeating in the sense that a natural proof that hardness exists would have as an automatic by-product an algorithm to solve a \hard" problem.

For a pseudo-random generator G : f 0 ; 1 g k ?! f 0 ; 1 g 2 k de ne its hardness H ( G ) as k k the minimal S for which there exists a circuit C of size S such that j P [ C ( G ( x )) = 1] ? P [ C ( y ) = 1] j 1 k S

(cf. [9]). Here, as usual, x is taken at random from f 0 ; 1 g k , and y is taken at random from f 0 ; 1 g 2 k .

Theorem 4.1. There (1) is no lower bound proof which is P=poly -natural against P=poly , {#razborov-1997-naturalproofs-thm-4-1 .statement tag=021B}

H G k o G f ; g k ?! f ; g 2 k unless ( k ) 2 for every pseudo-random generator k : 0 1 0 1 in P=poly .

In particular, if 2 n -hard functions exist then there is no P=poly -natural proof (against P=poly ). Proof. For the sake of contradiction, suppose that such a lower bound proof exists and C n is associated P=poly -natural combinatorial property. Let C n C n satisfy the constructivity and largeness conditions. W.l.o.g. we may assume from the very beginning that C n = C n .

We use a slightly modi ed construction from [12]. Let G : f 0 ; 1 g k ?! f 0 ; 1 g 2 k be a k polynomial time computable pseudo-random generator, and > 0 be an arbitrary constant. Set n = d k e . We use G : f 0 ; 1 g k ?! f 0 ; 1 g 2 k for constructing a pseudo-random function generator f : f 0 ; 1 g k ?! F in the same way as in [12]. Namely, let G ; G : f 0 ; 1 g k ?!

n 0 1 f 0 ; 1 g k be the rst and the last k bits of G , respectively. For a string y 2 f 0 ; 1 g n we de ne G : f 0 ; 1 g k ?! f 0 ; 1 g k by G G G G , and for x 2 f 0 ; 1 g k let f ( x )( y ) be y y y n y n ? 1 y 1 the rst bit of G y ( x ).

Note that f ( x )( y ) is computable by poly-size circuits, hence (from the de nition of a proof natural against P=poly ) the function f ( x ) 2 F n is not in C n for any xed x 2 f 0 ; 1 g k and any suciently large k . In other words, C has empty intersection with n n 2 f g k o f ( x ) x 0 ; 1 , and this disjointness implies that C n provides a statistical test for f ( x ), with ?

j P [ C ( f ) = 1] ? P [ C ( f ( x )) = 1] j 2 O ( n ) : (3) n n n Note that this test is computable by circuits of size 2 O ( n ) .

Constructing from this a statistical test for strings in our case is even simpler than in [12]. Namely, we arrange all internal nodes of the binary tree T of height n :

v 1 ;v 2 ;:::;v (2 n ? 1) in such a way that if v i is a son of v j then i < j . Let T i be the union of subtrees of T made by f v 1 ; : : : ; v i g along with all leaves. For a leaf y of T let v i ( y ) be the root of the subtree in T i containing y . Let G i;y G y n G y n ? h ( i;y )+1 , where h ( i; y ) is the distance between v i ( y ) and y . Finally, de ne the random collection f i;n by letting f i;n ( y ) be the rst bit of G x , where x are taken from f 0 ; 1 g k uniformly and independently for all roots v i;y v i ( y ) v of trees from T i .

Since f 0 ;n is f n , and f 2 n ? 1 ;n is f ( x ), we have from (3) that for some i , j P [ C ( f ) = 1] ? P [ C ( f ) = 1] j 2 ? O ( n ) :

n i;n n i +1 ;n Fix x for all roots v of subtrees in T other than v so that the bias 2 ? O ( n ) is preserved.

v i +1 i +1 Then we have a statistical test for strings distinguishing between G x v i +1 and ( x v 0 ; x v 00 ), where v 0 ; v 00 are the two sons of v . Thus H ( G ) 2 O ( n ) 2 O ( k ) . As was arbitrary, i +1 k the result follows.

The assumption that 2 n -hard functions exist is quite plausible. For example, despite many advances in computational number theory, multiplication seems to provide a basis for a family of such functions (known factoring algorithms are suciently exponential).

Based upon lower bounds for the parity function, Nisan [22] constructed a very strong generator secure against AC 0 -attack. In fact, an easy analysis of his generator in terms of its own complexity gives the following:

Theorem 4.2. For any integer d , there exists a family G n;s F n , where s is a seed of size polynomial in n such that G 2 AC 0 [2] and G looks random for 2 O ( n ) -size depth- d n;s n;s circuits, i.e., for any polynomial-size ( in 2 n ) depth d circuit family C : F ?! f 0 ; 1 g , n n j P [ C ( f ) = 1] ? P [ C ( G ) = 1] j < 2 ? ! ( n ) : (4) n n n n; s Here s is a random seed of the appropriate size. {#razborov-1997-naturalproofs-thm-4-2 .statement tag=021C}

Theorem 4.3. There is no lower bound proof which is AC 0 -natural against AC 0 [2] . {#razborov-1997-naturalproofs-thm-4-3 .statement tag=021D}

Proof. Assume, on the contrary, that such a proof exists, and that C n has the same meaning as in the proof of Theorem 4.1. Let d be the depth of a size 2 O ( n ) circuit to compute C . Let G be the generator which is pseudo-random against depth- d 2 O ( n ) n n;s sized circuits from Theorem 4.2. From the de nition of a proof natural against AC 0 [2], for suciently large n , C n ( G n;s ) = 0. Now, (4) immediately contradicts the largeness condition.

In fact, it is clear from the above proofs that whenever a complexity class contains pseudo-random function generators that are suciently secure against ?-attack, then there is no ?-natural proof against . E.g., it is easy to see that Theorems 4.1, 4.3 are still valid for the larger class of ?-natural proofs, where ? consists of languages computable by quasi-polynomial-sized circuits. This observation is of little importance for the examples of natural proofs given in this paper. However, it is useful in the context of proofs feasible in the logical sense [33], where quasi-polynomial limitations on the complexity arise more often. Formally, we de ne P=qpoly ~ as the class of non-uniform, quasi-polynomial size log n O (1) circuits, i.e., size n .

Theorem 4.4. There is no lower bound proof which is P=qpoly ~ -natural against P=poly {#razborov-1997-naturalproofs-thm-4-4 .statement tag=021E}

H ( G ) 2 k o (1) G : f 0 ; 1 g k ?! f 0 ; 1 g 2 k unless k for every pseudo-random generator k in P=poly .

### 4.1. Natural proofs are not applicable to the discrete logarithm problem {#razborov-1997-naturalproofs-s4-1 .section tag=021F}

It is possible (though we are unaware of any such examples) that a lower bound proof for restricted models might be natural, but cannot be applied to any explicit function. In other words, the proof might simply argue that many functions are complex without providing us with any explicit examples of such functions. Given our hardness assumption, no natural proof can prove lower bounds against P=poly whether or not the proof makes explicit what the hard function is. Avi Wigderson has pointed out that if we restrict ourselves to certain explicit functions, we can prove unconditional results in the style of Theorem 4.1. A good example of such a function is the discrete logarithm. The key point is that the discrete logarithm is known to be hard on average if and only if it is hard in the worst case. In this section, we show that there is no natural proof that the discrete logarithm requires exponential-sized circuits.

Recall from [9] that for a prime p and a generator g for Z p , the predicate B p;g ( x ) on Z p is de ned to be 1 if log g x ( p ? 1) = 2 and 0 otherwise. B p;g ( x ) was shown in [9] to be a hard bit of the discrete logarithm problem. We consider B p;g ( x ) as a Boolean function in d log p e variables (extended by, say, zeros on those inputs x which do not represent an integer in the range [1 ; p ? 1]). Our principal goal in this section is to show that no P=poly -natural proof against \suciently large" Boolean circuits can be applied to B p;g ( x ).

To explain the meaning of \suciently large", we need a couple of technical de nitions. For an integer-valued function t ( n ), let SIZE ( t ( n )) be the complexity class consisting of all functions f f n g which have circuit size O ( t ( n )). Let t ? 1 ( n ) max f x j t ( x ) n g :

We say that t ( n ) is half-exponential if it is non-decreasing and t ? 1 ( n C ) o (log t ( n )) (5) for every C > 0. The meaning of this de nition is that, roughly speaking, the second iteration of t ( n ) should grow faster than the exponent. For example, t ( n ) = 2 n is halfexponential, whereas t ( n ) = 2 (log n ) C is not.

Theorem 4.5. Let t ( n ) be an arbitrary half-exponential function. Then there is no combinatorial property C n useful against S SIZE ( t ( n )) and satisfying P=poly -constructivity and largeness conditions such that n 2 ! C n contains in nitely many functions of the form B p;g ( x ) . {#razborov-1997-naturalproofs-thm-4-5 .statement tag=0220}

Proof. Assume the contrary, and let f B g be an in nite sequence contained in S C p ;g n 2 ! n such that d log p 1 e < d log p 2 e < : : : Let k d log p e . Applying the usefulness condition to the sequence f n obtained from f B p ;g g by letting f n 0 for those n which are not of the form d log p e , we will nd in f B p ;g g an in nite subsequence where all functions have the circuit size at least t ( k ). W.l.o.g. we may assume that this is the case for our original sequence.

Let G : f 0 ; 1 g 2 k ?! f 0 ; 1 g 4 k be the standard pseudo-random generator from [9] based upon f B p ;g g . It is easy to check that the proof of [9, Theorem 3] actually extends to showing that the circuit size of f B p ;g g is polynomial in H ( G ) + k . Thus, we have t ( k ) ( H ( G ) + k ) O (1) : (6)

Now we convert G into the pseudo-random function generator f : f 0 ; 1 g 2 k ?! F n as in the proof of Theorem 4.1, where n will be speci ed a little bit later. There exists a fixed constant $C > 0$ such that for almost all $\nu$, $f_\nu(x)(y)$ is computable by circuits of size $(k_\nu + n_\nu)^C$. Let $n_\nu = t^{-1}(k_\nu^{C+1}) + 1$.

(5) implies that $t(k_\nu) > k_\nu^{C+1}$ for almost all $\nu$, since otherwise we would have $k_\nu \leq t^{-1}\left(k_\nu^{C+1}\right) \leq \log t(k_\nu) \leq (C+1)\log k_\nu$. Hence $n_\nu \leq k_\nu$. Now we have that for almost all $\nu$ every function in the image of the generator $f_\nu$ has circuit size at most $(k_\nu + n_\nu)^C \leq (2k_\nu)^C \leq k_\nu^{C+1} \leq t(n_\nu)$. Applying the usefulness condition again, we find that for almost all $\nu$, the image of the generator $f_\nu$ has the empty intersection with $C_n$. Arguing as in the proof of Theorem 4.1, we get from this

$$
H(G_\nu) \leq 2^{O(n_\nu)}.
$$

Finally note that $C_n \neq \emptyset$ for almost all $n$ (from largeness) and, thus,

$$
t(n) \leq 2^n
$$

(again, for almost all $n$.)

The required contradiction is now obtained simply by combining the inequalities (5) (with $n := k_\nu, C := C + 1$), (6), (7), (8):

$$
n_\nu = t^{-1}(k_\nu^{C+1}) + 1 \leq o(\log t(k_\nu)) \leq o (\log H(G_\nu) + \log k_\nu) \leq o(n_\nu) + o(\log k_\nu) \leq o(n_\nu).
$$

■

Corollary 4.6. *There is no combinatorial property* $C_n$ *useful against* $\bigcap_{\epsilon > 0} SIZE\left(2^{n^\epsilon}\right)$ *and satisfying P/poly-constructivity and largeness conditions such that* $\bigcup_{n \in \omega} C_n$ *contains infinitely many functions of the form* $B_{p,g}(x)$. {#razborov-1997-naturalproofs-cor-4-6 .statement tag=0221}

Proof. $\bigcap_{\epsilon > 0} SIZE\left(2^{n^\epsilon}\right) \supseteq SIZE\left(2^{2^{\sqrt{\log n}}}\right)$, and $t(n) = 2^{2^{\sqrt{\log n}}}$ is half-exponential. ■

It is easy to see that the above proof is actually valid for an *arbitrary* collection $\{f_{p,g}\}$ of functions poly-time nonuniformly Turing reducible to the corresponding discrete logarithm problem in place of $\{B_{p,g}\}$.
