---
paper: razborov-1997-naturalproofs
title: Natural Proofs
authors:
  - Alexander A. Razborov
  - Steven Rudich
year: 1997
venue: Journal of Computer and System Sciences
field: theory
section: "3"
section_title: Examples of naturalizing arguments
tag: "0210"
kind: section
lang: en
source: https://doi.org/10.1006/jcss.1997.1494
pdf_sha256: 6cf137cf878d01654aeff5dbf031e97a624cd72367b87415ff61080447de7682
pdf_pages: 7-14
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: f100ad71d3c9292c755dc077bc5e342540e3e8dc9465d0db2a1d5f3b3db5632a
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

### 3.1. AC 0 lower bounds for parity: AC 0 -natural {#razborov-1997-naturalproofs-s3-1 .section tag=0211}

One of the rst combinatorial arguments to give people hope and direction in lower bound research was [11] where it was shown that PARITY 62 AC 0 (independently this result, using somewhat di erent machinery, was discovered in [1]). Substantial technical improvements to their bounds were subsequently given by [40, 14]. All these proofs are AC 0 -natural.

The C n used by these arguments simply says that there does not exist a restriction of the variables with the appropriate number of unassigned variables which forces f n to be a constant function. The \appropriate" number of unassigned variables is di erent in [11, 40, 14] and determines the bounds obtained.

All three papers argue explicitly that C ( f ) = 1 implies that f f g 62 AC 0 , in other n n n words, that C is useful against AC 0 . C is a natural property. In fact, we can choose n n C n = C n .

A simple counting argument shows that C n is true of a random function ( C n has the largeness condition).

C is in AC 0 ! ( C has constructivity). Indeed, suppose k is the \appropriate" number n n of unassigned variables. Given the truth table for f n as input, we compute C n ( f n ) as follows. List all n 2 n ? k = 2 O ( n ) restrictions of n ? k variables. For each one there is a k circuit of depth 2 and size 2 O ( n ) which outputs a 1 i that restriction does not leave f a n constant function. Output the AND of all these circuits. The resulting circuit has depth 3 and is polynomial-sized in 2 n .

### 3.2. AC 0 [ q ] lower bounds: NC 2 -natural {#razborov-1997-naturalproofs-s3-2 .section tag=0212}

In this subsection we look at the proofs from [29, 36, 8] of lower bounds on the size of AC 0 [ q ]-circuits, q being a power of a prime. The naturalness of these proofs is especially transparent in the framework of [29]. Namely, we have a GF [2]-linear mapping M from F n to a matrix space, and we simply take C n to be the set of all f n 2 F n for which rank( M ( f n )) is large. After reviewing the argument in Section 3.2.1 below, it will be an exercise for the reader to show that C n ( f n ) = 1 for at least 1/2 fraction of all f n 2 F n . Since computing the rank is in NC 2 , we see that the proof is NC 2 -natural. Smolensky's proof [36] is analyzed below.

We will show in Section 4 that there is no AC 0 -natural proof against AC 0 [2]. Along with the previous subsection, this gives the insight that [29, 36, 8] had to require arguments from a stronger class than those of [11, 40, 14].

### 3.2.1. Smolensky's proof: a non-trivial example of naturalization {#razborov-1997-naturalproofs-s3-2-1 .section tag=0213}

The argument given in Smolensky [36] is a perfect example of a natural circuit lower bound proof, but this is not immediately obvious. We will outline a special case of his argument:

a proof that parity does not have small AC 0 [3] circuits.

First, we recall the notion of polynomial approximation of a Boolean function. Think of the Boolean value TRUE as corresponding to the eld element ? 1 and the Boolean value FALSE as corresponding to the eld element 1. Let f be a Boolean function and p be a polynomial over Z 3 where f and p have an identical set of variable names. Any assignment A to f can be viewed as an assignment to p ; in the case p ( A ) and f ( A ) evaluate to corresponding values we consider them equal on this assignment. Otherwise, we consider them to di er. The better p approximates f , the fewer assignments on which they di er. Since we will only be interested in the values polynomials take on f? 1 ; 1 g (Boolean) assignments, we will consider polynomials to be multi-linear by default (no variable gets raised to a power greater than one).

Proof outline: Smolensky's proof has two main pieces. (1) Any function computed by a \small" AC 0 [3] circuit can be \reasonably" approximated by a \low" degree polynomial over Z 3 . (2) The parity function in n variables can't be \reasonably" approximated by a \low" degree polynomial over Z 3 . The proof of (1) is not important here and is omitted. (2) is proved by contradiction. Suppose there were a \low" degree (degree d ) polynomial p which agrees with the polynomial x 1 x 2 x 3 x n (the parity function) on all but a \small" number of Boolean assignments. Let W be the set of Boolean assignments on which they di er. Let N = 2 n . Let w be the size of the set W . We will assume that n is odd and use l 1 and l 2 to denote polynomials of degree less than n= 2. Every multi-linear polynomial q can be written in the form x 1 x n l 1 + l 2 . This means that, ignoring the inputs in W , every Z -valued function on f? 1 ; 1 g n n W (and there are 3 N ? w of them) can be represented

3 in the form pl 1 + l 2 . This representation has degree ( n ? 1) = 2 + d which by a counting argument can't represent as many as 3 N ? w functions. Contradiction.

This proof might seem to be exploiting a very particular fact about how the parity function is expressed as a polynomial; it is not obvious how this same proof would apply to a large fraction of functions. Even worse, the proof refers to a seemingly non-constructive counting argument. However, the proof technique is by its nature applicable to many functions, and counting Boolean functions eventually boils down to counting dimensions of certain linear spaces which already is feasible in our sense.

There is one choice of C n clear from the proof: C n ( f n ) = 1 if f n can't be reasonably approximated by a low degree polynomial over Z 3 (for the appropriate de nitions of reasonable and low). Part (1) of Smolensky's argument proves that C is useful against AC 0 [3].

n Why is C n natural? To see it we have to make a choice of C n .

The simple choice is C n = C n . It is fairly obvious that C n satis es the largeness condition. But what about P=poly -constructivity? It is not at all clear that there is a polynomial-size circuit which can determine if a function (given by its truth-table) can be approximated by a low-degree polynomial over Z 3 . This remains an open problem.

Thus we sink deeper into the proof and try to put

C n ( f n ) = 1 if every polynomial q can be written in the form f n l 1 + l 2 ; (1) where f n is the unique multi-linear polynomial representing f n . Then we have constructivity.

In order to see this, denote by L the vector space of all polynomials of degree less than n= 2, and by T the complementary vector space of all (multi-linear) polynomials without monomials of degree less than n= 2. The whole polynomial space is then represented as the direct sum L T and also, since n is odd, we have dim( L ) = dim( T ) = N= 2. Now, C n ( f n ) = 1 i the linear mapping f n : L ?! T taking l 2 L to the projection of f n l 2 L T onto T is one-to-one (the reader can check his understanding at this point by verifying that the parity function has this property). Thus checking that C n ( f n ) = 1 amounts to checking that a matrix easily computable from f is non-singular which can be done in NC 2 .

n For so chosen C n the largeness condition also looks plausible. But we have no easy proof of it.

We turn around this diculty by trying to extend the de nition of (1) as much as we can (so that we'll have more functions satisfying it) while preserving its spirit (so that constructivity will also be preserved) and keeping the lower bound provided by it. A short examination shows that the de nition

C n ( f n ) = 1 i dim( f n L + L ) N (1 = 2 + ) (2) which for = 1 = 2 is the same as (1), is actually as good as (1) itself for arbitrary xed

> 0. Indeed, (2) implies that at least 3 N (1 = 2+ ) ? w functions on f? 1 ; 1 g n n W can be represented by a degree ( n ? 1) = 2 + d polynomial, and the same counting argument still works.

But if we de ne C n as in (2) with = 1 = 4, we also have largeness! This immediately follows from the fact that for every f n 2 F n either C n ( f n ) = 1 or C n ( x 1 x n f n ) = 1 (cf. the proof of Theorem 5.2 a) below). 1

To show this fact, note that if dim f n L + L 3 N= 4 then C n ( f n ) = 1. Otherwise we have dim ( x 1 x n f n L + L ) =L = dim ( x 1 x n L + f n L ) = f n L

1 C can be further adjusted to be a property of density close to one, as opposed to 1 = 2.

n dim ( x 1 x n L + f n L + L ) = ( f n L + L ) = dim ( T + L ) = ( f n L + L ) N= 4

(the rst equality here comes from the observation that ( f ) 2 = 1 and thus multiplying by n f n de nes an automorphism of L T ). This gives us C n ( x 1 : : : x n f n ) = 1.

So, C is an NC 2 -natural property.

n Smolensky's proof is the most dicult example of naturalization we have encountered in our analysis. On the other hand, it perfectly illustrates the general empirical idea of \adjusting" C n in both directions in order to come up with a natural C n .

### 3.3. Perceptron lower bounds for parity: P -natural {#razborov-1997-naturalproofs-s3-3 .section tag=0214}

In [6], it is shown that a small constant-depth circuit (over f^ ; _ ; :g ) which is allowed a single majority gate can't approximate the parity function. The authors did this by rst showing tight lower bound on the degree of a perceptron required to approximate parity to within a given . Their argument is natural.

Some de nitions from [6]. A real polynomial p strongly represents a Boolean function 2 f just in case sgn( p ( x )) = f ( x ) for all input vectors x ; such a polynomial is also called a perceptron to compute f . Let p weakly represent f just in case p is not the constant zero function on f? 1 ; 1 g n , and sgn( p ( x )) = f ( x ) for all x where p ( x ) is nonzero. The weak degree , d w ( f ), is de ned as the least k for which there exists a non-zero degree k polynomial which weakly represents f .

A natural C n stated in the paper is that f n can't be well approximated by the sign of a low degree polynomial. It is explicitly shown that any f n with property C n can't be approximated by a small, constant-depth circuit with one majority gate, i.e., C n has usefulness. To see that C n is natural one must exhibit a proper subset C n .

Let C n ( f n ) = 1 if d w ( f n ) is greater than the appropriate threshold. [6] explicitly showed that C n ( f n ) = 1 implies that a polynomial must have appropriately high degree to approximate f n with its sign, i.e., C n ( f n ) = 1 implies that C n ( f n ) = 1. d w is computable in polynomial-time using linear programming. This shows that C n has constructivity. Since the linear programming seems essential it is doubtful that anything substantially more constructive than C n could be found in the above argument, e.g., an NC -natural property for example.

2 In this section we, similarly to 3.2.1, represent Boolean functions as mappings from f? 1 ; 1 g n to f? 1 ; 1 g , and fg stands for the point-wise product, which is the same as f g in the f 0 ; 1 g -notation

To argue that C n has the largeness property, we can show the following improvement of an ( n= log n ) lower bound from [6]:

Theorem 3.1. f 2 F P [ d ( f ) n= 20] > 1 ? 2 ? 2 ( n ) {#razborov-1997-naturalproofs-thm-3-1 .statement tag=0215}

For a uniformly chosen n n , w n .

Proof. We use the following well-known facts:

Proposition 3.2. Let a 1 ; : : : ; a N 2 R . Then there exist a 0 ; : : : ; a 0 2 Z such that j a 0 j {#razborov-1997-naturalproofs-prop-3-2 .statement tag=0216}

1 N i exp( O ( N log N )) (1 i N ) , and for every x 2 f? 1 ; 1 g N , i X N ! X N ! sgn a x = sgn a 0 x :

i i i i i =1 i =1 Proposition 3.3. Every integer polynomial p ( x 1 ; : : : ; x n ) of degree d which is not an identically zero on f? 1 ; 1 g n , di ers from zero on at least 2 n ? d points from f? 1 ; 1 g n .

The proof of Proposition 3.2 can be found e.g. in [21]; Proposition 3.3 is folklore. Let f n 2 F n . If f n is weakly represented by a polynomial p of degree at most n= 20, we rstly apply Proposition ! 3.2 to the vector of coecients of p . The length N of this vector is P n= 20 n 2 n ( H (1 = 20)+ o (1)) , where H ( ) is the entropy function. We nd that i =0 i p can be replaced by a polynomial p 0 with integer coecients whose bit size is at most O ( N 2 log N ) 2 n (2 H (1 = 20)+ o (1)) .

f n can be uniquely retrieved from the pair ( p 0 ; f 0 ), where f 0 is the list of values of f n n n on zeros of p 0 (arranged, say, in the lexicographic order). From Proposition 3.3 we know that the bit size of f 0 is at most 2 n ? 2 19 = 20 n , thus the bit size of the pair ( p 0 ; f 0 ) is at n H n most 2 n ? 2 19 = 20 n + 2 n (2 (1 = 20)+ o (1)) . Since 2 H (1 = 20) < 19 , the proof is completed by the

20 standard counting argument.

### 3.4. Lower bounds on formula size: AC 0 -natural {#razborov-1997-naturalproofs-s3-4 .section tag=0217}

Andreev [5] gives a promising lower bound for the formula size of an explicit function. His bound was subsequently improved in [23, 24]. Finally, Hastad [15] gave a nearly optimal lower bound (almost n 3 ) of the formula size for Andreev's function.

Andreev's function is a Boolean function A 2 n on 2 n bits: a 1 ; a 2 ; : : : ; a n ; b 1 ; b 2 ; : : : ; b n . The a 's are partitioned into log n groups of size n= log n each. Let h j be the parity of the bits in the j th group. The bits h 1 ; h 2 ; : : : ; h log n index a number i from 1 to n . The value of the function A 2 n is the bit b i .

All these proofs work by using a shrinkage factor T which was successively improved in the last three papers until T = ~ ( n 2 ). ( ~ is the \soft Omega" notation which is like but ignores multiplicative factors of (log n ) k for constant k .)

The meaning of T is that when a formula is hit by a random restriction it is almost certain to shrink by a factor of T . Thus, to prove a formula lower bound, just show that a formula must have size s after being hit by a random restriction. It follows that the original formula had size around sn 2 .

The natural property C 2 n is that there is a restriction of b 's such that any of its extensions leaving at least one unrestricted variable in each group of a 's induces a formula of size

( n= log n ). This property is useful since a random restriction leaving (log n ) 2 unrestricted variables leaves at least one such variable in each group: for some xing of b 's, a random restriction to the a 's will shrink the formula to ( n= log n ). Obviously, A 2 n has C 2 n (simply restrict b 's so that they will encode the most complex function in log n variables) which implies that it must have formula complexity at least ~ ( n 3 ).

We can choose C 2 n = C 2 n . The fact that C 2 n has largeness is easy to prove. Constructivity is also easy if we observe that there are only 2 O ( n ) formulas of size less than n= log n .

### 3.5. Lower bounds against depth-2 threshold circuits: {#razborov-1997-naturalproofs-s3-5 .section tag=0218}

TC 0 -natural

Hajnal et al. [13] show that the MOD-2 inner-product function requires depth-2 threshold circuits of exponential size. Any Boolean function can be viewed as a Boolean matrix by dividing the inputs into two equal sets with the left half indexing the rows and the right half indexing the columns. Seen in this way the inner-product function is a Hadamard matrix. Their proof shows that any matrix with low discrepancy can't be computed by small depth-2 threshold circuits. Choose C n to be true of all functions whose matrices have low discrepancy. Their main lemma shows that any Hadamard matrix has low discrepancy. The same argument shows that any matrix which is almost Hadamard in the sense that the dot product of any two rows or any two columns is small also has the low discrepancy property. Thus, the C n suggested by their proof is to check that the function viewed as a matrix is almost Hadamard, for the appropriate de nition of almost. It is possible to de ne \almost" so as to guarantee that C n has largeness and preserves usefulness. Constructivity: For each of the 2 O ( n ) dot products, feed the binary AND's into a threshold gate; feed the outputs of the threshold gates into a large fan-in AND. This is in TC 0 .

### 3.6. Lower bounds against switching-and-recti er networks: {#razborov-1997-naturalproofs-s3-6 .section tag=0219}

AC 0 -natural

It was shown in [30] that any switching-and-recti er network (in particular, any nondeterministic branching program) for a large variety of symmetric functions must have size

( n ( n )), where ( n ) is a function which slowly grows to in nity. A similar result was proven in [18] for -branching programs.

The proofs are based upon a purely combinatorial characterization of the network size in terms of particular instances of the MINIMUM COVER problem. Let C n be the set of those functions f n for which the size ( f n ) of the minimal solution to the corresponding instance is ( n ( n )).

The key lemma in these proofs says that if f n outputs a 1 on any input with s ( n ) ones, and outputs a 0 on any input with s ( n ) ? d ( n ) ones, then ( f n ) ( n ( n )) ( s ( n ) and d ( n ) are functions which slowly grow to in nity; s ( n ) d ( n )).

Denote this property by A n . It obviously violates the largeness condition. We circumvent this by letting C n be the set of those functions for which any restriction assigning n= 2 variables to zero can be extended to another restriction 0 by assigning to zero ( n= 2 ? log log n ) additional variables in such a way that the induced function has A log log n .

To see C n C n , recall from [30, 18] that every covering set i; ( A ) has its associated variable x i such that restricting this variable to 0 kills i; ( A ). Now, for any collection of o ( n ( n )) covering sets we simply assign n= 2 most frequently represented x i 's to 0, and this leaves us with a collection in which every variable corresponds to at most o ( ( n )) sets. Hence, for every extension 0 of this restriction, the size of the resulting collection will be o (log log n ( n )). Thus, by the above lemma, this collection (and hence the original one) does not cover all the points from the universe ( ( n ) and (log log n ) di er by at most 1).

C is in AC 0 (cf. Section 3.1).

n To see the largeness condition, note that for every we can choose n 3 = 2 extensions 0 ; : : : ; 0 3 = 2 so that the sets of variables unassigned by every two di erent 0 ; 0 from this 1 n i j list have at most one variable in common. The event \ f n restricted by 0 has A log log n " i depends only on those inputs that have either s ( n ) or s ( n ) ? d ( n ) ones, and, moreover, all these ones correspond to variables not assigned by 0 . Since d ( n ) > 1 and s ( n ) ? d ( n ) > 1, i our assumption on 0 ; : : : ; 0 3 = 2 implies that these sets of inputs are pairwise disjoint (when

1 n i ranges over f 1 ; : : : ; n 3 = 2 g ). Hence, the events \ f restricted by 0 has A " are n i log log n independent, and we can apply the standard counting argument.
