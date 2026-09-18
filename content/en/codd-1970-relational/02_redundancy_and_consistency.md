---
paper: codd-1970-relational
title: A Relational Model of Data for Large Shared Data Banks
authors:
  - E. F. Codd
year: 1970
venue: Communications of the ACM
field: databases
section: "2"
section_title: Redundancy and Consistency
tag: "0303"
kind: section
lang: en
source: https://www.seas.upenn.edu/~zives/03f/cis550/codd.pdf
pdf_sha256: fa2579f427a4da68466ef159a3ae0c3c1fe4eafec60f73c9f2f40378a65d8ef9
pdf_pages: 7-11
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 6570432322ba609e03e5a7b402c94aa508a1a4aee6e5f6ba701bc36871a88125
prompt_sha256: 6deed113e702745ea82772457035bb281a0a0db9eb7baaa76a842f19ad073ba5
---

### 2.1. OPERATIONS ON RELATIONS {#codd-1970-relational-s2-1 .section tag=0304}

Since relations are sets, all of the usual set operations are applicable to them. Nevertheless, the result may not be a relation; for example, the union of a binary relation and a ternary relation is not a relation.

The operations discussed below are specifically for relations. These operations are introduced because of their key role in deriving relations from other relations. Their principal application is in noninferential information systems—systems which do not provide logical inference services—although their applicability is not necessarily destroyed when such services are added.

Most users would not be directly concerned with these operations. Information systems designers and people concerned with data bank control should, however, be thoroughly familiar with them.

2.1.1. Permutation. A binary relation has an array representation with two columns. Interchanging these columns yields the converse relation. More generally, if a permutation is applied to the columns of an $n$-ary relation, the resulting relation is said to be a permutation of the given relation. There are, for example, $4! = 24$ permutations of the relation supply in Figure 1, if we include the identity permutation which leaves the ordering of columns unchanged.

Since the user's relational model consists of a collection of relationships (domain-unordered relations), permutation is not relevant to such a model considered in isolation. It is, however, relevant to the consideration of stored representations of the model. In a system which provides symmetric exploitation of relations, the set of queries answerable by a stored relation is identical to the set answerable by any permutation of that relation. Although it is logically unnecessary to store both a relation and some permutation of it, performance considerations could make it advisable.

2.1.2. Projection. Suppose now we select certain columns of a relation (striking out the others) and then remove from the resulting array any duplication in the rows. The final array represents a relation which is said to be a projection of the given relation.

A selection operator $\pi$ is used to obtain any desired permutation, projection, or combination of the two operations. Thus, if $L$ is a list of $k$ indices\footnote{When dealing with relationships, we use domain names (role-qualified whenever necessary) instead of domain positions.} $L = i_1, i_2, \cdots, i_k$ and $R$ is an $n$-ary relation ($n \geq k$), then $\pi_L(R)$ is the $k$-ary relation whose $j$th column is column $i_j$ of $R$ ($j = 1, 2, \cdots, k$) except that duplication in resulting rows is removed. Consider the relation supply of Figure 1. A permuted projection of this relation is exhibited in Figure 4. Note that, in this particular case, the projection has fewer $n$-tuples than the relation from which it is derived.

2.1.3. Join. Suppose we are given two binary relations, which have some domain in common. Under what circumstances can we combine these relations to form a ternary relation which preserves all of the information in the given relations?

The example in Figure 5 shows two relations $R, S$, which are joinable without loss of information, while Figure 6 shows a join of $R$ with $S$. A binary relation $R$ is joinable with a binary relation $S$ if there exists a ternary relation $U$ such that $\pi_{12}(U) = R$ and $\pi_{23}(U) = S$. Any such ternary relation is called a join of $R$ with $S$. If $R, S$ are binary relations such that $\pi_2(R) = \pi_1(S)$, then $R$ is joinable with $S$. One join that always exists in such a case is the natural join of $R$ with $S$ defined by

$$
R*S = \{ (a, b, c): R(a, b) \land S(b, c) \}
$$

where $R(a, b)$ has the value true if $(a, b)$ is a member of $R$ and similarly for $S(b, c)$. It is immediate that

$$
\pi_{12}(R*S) = R
$$

and

$$
\pi_{23}(R*S) = S.
$$

Note that the join shown in Figure 6 is the natural join of $R$ with $S$ from Figure 5. Another join is shown in Figure 7.

| $\Pi_{31}(supply)$ | (project | supplier) |
| --- | --- | --- |
| 5 | 1 |  |
| 5 | 2 |  |
| 1 | 4 |  |
| 7 | 2 |  |

Fig. 4. A permuted projection of the relation in Figure 1 {#codd-1970-relational-fig-4 .figure tag=0305}

| R | (supplier | part) | S | (part | project) |
| --- | --- | --- | --- | --- | --- |
| 1 | 1 |  | 1 | 1 |  |
| 2 | 1 |  | 1 | 2 |  |
| 2 | 2 |  | 2 | 1 |  |

Fig. 5. Two joinable relations {#codd-1970-relational-fig-5 .figure tag=0306}

| R*S | (supplier | part | project) |
| --- | --- | --- | --- |
| 1 | 1 | 1 | 1 |
| 1 | 1 | 2 |  |
| 2 | 1 | 1 |  |
| 2 | 1 | 2 |  |
| 2 | 2 | 1 |  |

Fig. 6. The natural join of R with S (from Figure 5) {#codd-1970-relational-fig-6 .figure tag=0307}

| U | (supplier | part | project) |
| --- | --- | --- | --- |
| 1 | 1 | 2 |  |
| 2 | 1 | 1 |  |
| 2 | 2 | 1 |  |

Fig. 7. Another join of R with S (from Figure 5) {#codd-1970-relational-fig-7 .figure tag=0308}

Inspection of these relations reveals an element (element 1) of the domain part (the domain on which the join is to be made) with the property that it possesses more than one relative under $R$ and also under $S$. It is this element which gives rise to the plurality of joins. Such an element in the joining domain is called a point of ambiguity with respect to the joining of $R$ with $S$.

If either $\pi_{21}(R)$ or $S$ is a function,\footnote{A function is a binary relation, which is one-one or many-one, but not one-many.} no point of ambiguity can occur in joining $R$ with $S$. In such a case, the natural join of $R$ with $S$ is the only join of $R$ with $S$. Note that the reiterated qualification "of $R$ with $S$" is necessary, because $S$ might be joinable with $R$ (as well as $R$ with $S$), and this join would be an entirely separate consideration. In Figure 5, none of the relations $R, \pi_{21}(R), S, \pi_{21}(S)$ is a function.

Ambiguity in the joining of $R$ with $S$ can sometimes be resolved by means of other relations. Suppose we are given, or can derive from sources independent of $R$ and $S$, a relation $T$ on the domains project and supplier with the following properties:

(1) $\pi_1(T) = \pi_2(S)$,
(2) $\pi_2(T) = \pi_1(R)$,
(3) $T(j, s) \rightarrow \exists p (R(S, p) \land S(p, j))$,
(4) $R(s, p) \rightarrow \exists j (S(p, j) \land T(j, s))$,
(5) $S(p, j) \rightarrow \exists s (T(j, s) \land R(s, p))$, then we may form a three-way join of $R, S, T$; that is, a ternary relation such that

$$
\pi_{12}(U) = R, \quad \pi_{23}(U) = S, \quad \pi_{31}(U) = T.
$$

Such a join will be called a cyclic 3-join to distinguish it from a linear 3-join which would be a quaternary relation $V$ such that

$$
\pi_{12}(V) = R, \quad \pi_{23}(V) = S, \quad \pi_{34}(V) = T.
$$

While it is possible for more than one cyclic 3-join to exist (see Figures 8, 9, for an example), the circumstances under which this can occur entail much more severe constraints than those for a plurality of 2-joins. To be specific, the relations $R, S, T$ must possess points of ambiguity with respect to joining $R$ with $S$ (say point $x$), $S$ with $T$ (say $y$), and $T$ with $R$ (say $z$), and, furthermore, $y$ must be a relative of $x$ under $S$, $z$ a relative of $y$ under $T$, and $x$ a relative of $z$ under $R$. Note that in Figure 8 the points $x = a; \quad y = d; \quad z = 2$ have this property.

The natural linear 3-join of three binary relations $R, S, T$ is given by

$$
R*S*T = \{ (a, b, c, d): R(a, b) \land S(b, c) \land T(c, d) \}
$$

where parentheses are not needed on the left-hand side because the natural 2-join (*) is associative. To obtain the cyclic counterpart, we introduce the operator $\gamma$ which produces a relation of degree $n - 1$ from a relation of degree $n$ by tying its ends together. Thus, if $R$ is an $n$-ary relation ($n \geq 2$), the tie of $R$ is defined by the equation

$$
\gamma(R) = \{ (a_1, a_2, \cdots, a_{n-1}): R(a_1, a_2, \cdots, a_{n-1}, a_n) \land a_1 = a_n \}.
$$

We may now represent the natural cyclic 3-join of $R, S, T$ by the expression

$$
\gamma(R*S*T).
$$

Extension of the notions of linear and cyclic 3-join and their natural counterparts to the joining of $n$ binary relations (where $n \geq 3$) is obvious. A few words may be appropriate, however, regarding the joining of relations which are not necessarily binary. Consider the case of two relations $R$ (degree $r$), $S$ (degree $s$) which are to be joined on $p$ of their domains ($p < r, \quad p < s$). For simplicity, suppose these $p$ domains are the last $p$ of the $r$ domains of $R$, and the first $p$ of the $s$ domains of $S$. If this were not so, we could always apply appropriate permutations to make it so. Now, take the Cartesian product of the first $r-p$ domains of $R$, and call this new domain $A$. Take the Cartesian product of the last $p$ domains of $R$, and call this $B$. Take the Cartesian product of the last $s-p$ domains of $S$ and call this $C$.

We can treat $R$ as if it were a binary relation on the domains $A, B$. Similarly, we can treat $S$ as if it were a binary relation on the domains $B, C$. The notions of linear and cyclic 3-join are now directly applicable. A similar approach can be taken with the linear and cyclic $n$-joins of $n$ relations of assorted degrees.

2.1.4. Composition. The reader is probably familiar with the notion of composition applied to functions. We shall discuss a generalization of that concept and apply it first to binary relations. Our definitions of composition and composability are based very directly on the definitions of join and joinability given above.

Suppose we are given two relations $R, S$. $T$ is a composition of $R$ with $S$ if there exists a join $U$ of $R$ with $S$ such that $T = \pi_{13}(U)$. Thus, two relations are composable if and only if they are joinable. However, the existence of more than one join of $R$ with $S$ does not imply the existence of more than one composition of $R$ with $S$.

Corresponding to the natural join of $R$ with $S$ is the natural composition⁹ of $R$ with $S$ defined by

$$
R \cdot S = \pi_{13}(R*S).
$$

Taking the relations $R, S$ from Figure 5, their natural composition is exhibited in Figure 10 and another composition is exhibited in Figure 11 (derived from the join exhibited in Figure 7).

$$
\begin{array}{cc}
R \cdot S & (project\ supplier) \\
1 & 1 \\
1 & 2 \\
2 & 1 \\
2 & 2
\end{array}
$$

Fig. 10. The natural composition of R with S (from Figure 5) {#codd-1970-relational-fig-10 .figure tag=0309}

$$
\begin{array}{cc}
T & (project\ supplier) \\
1 & 2 \\
2 & 1
\end{array}
$$

Fig. 11. Another composition of R with S (from Figure 5) {#codd-1970-relational-fig-11 .figure tag=030A}

When two or more joins exist, the number of distinct compositions may be as few as one or as many as the number of distinct joins. Figure 12 shows an example of two relations which have several joins but only one composition. Note that the ambiguity of point c is lost in composing $R$ with $S$, because of unambiguous associations made via the points $a, b, d, e$.

$$
\begin{array}{ccc}
R & (supplier\ part) & S & (part\ project) \\
1 & a & a & g \\
1 & b & b & f \\
1 & c & c & f \\
2 & c & c & g \\
2 & d & d & g \\
2 & e & e & f
\end{array}
$$

Fig. 12. Many joins, only one composition {#codd-1970-relational-fig-12 .figure tag=030B}

Extension of composition to pairs of relations which are not necessarily binary (and which may be of different degrees) follows the same pattern as extension of pairwise joining to such relations.

A lack of understanding of relational composition has led several systems designers into what may be called the connection trap. This trap may be described in terms of the following example. Suppose each supplier description is linked by pointers to the descriptions of each part supplied by that supplier, and each part description is similarly linked to the descriptions of each project which uses that part. A conclusion is now drawn which is, in general, erroneous: namely that, if all possible paths are followed from a given supplier via the parts he supplies to the projects using those parts, one will obtain a valid set of all projects supplied by that supplier. Such a conclusion is correct only in the very special case that the target relation between projects and suppliers is, in fact, the natural composition of the other two relations—and we must normally add the phrase “for all time,” because this is usually implied in claims concerning path-following techniques.

⁹ Other writers tend to ignore compositions other than the natural one, and accordingly refer to this particular composition as the composition—see, for example, Kelley’s “General Topology.”

2.1.5. Restriction. A subset of a relation is a relation. One way in which a relation $S$ may act on a relation $R$ to generate a subset of $R$ is through the operation restriction of $R$ by $S$. This operation is a generalization of the restriction of a function to a subset of its domain, and is defined as follows.

Let $L, M$ be equal-length lists of indices such that $L = i_1, i_2, \ldots, i_k, M = j_1, j_2, \ldots, j_k$ where $k \leq$ degree of $R$ and $k \leq$ degree of $S$. Then the $L, M$ restriction of $R$ by $S$ denoted $R_{L|M}S$ is the maximal subset $R'$ of $R$ such that

$$
\pi_L(R') = \pi_M(S).
$$

The operation is defined only if equality is applicable between elements of $\pi_{i_h}(R)$ on the one hand and $\pi_{j_h}(S)$ on the other for all $h = 1, 2, \ldots, k$.

The three relations $R, S, R'$ of Figure 13 satisfy the equation $R' = R_{(2,3)|(1,2)}S$.

$$
\begin{array}{ccc}
R & (s\ p\ j) & S & (p\ j) & R' & (s\ p\ j) \\
1 & a\ A & a\ A & 1 & a\ A \\
2 & a\ A & c\ B & 2 & a\ A \\
2 & a\ B & b\ B & 2 & b\ B \\
2 & b\ A & & \\
2 & b\ B & &
\end{array}
$$

Fig. 13. Example of restriction {#codd-1970-relational-fig-13 .figure tag=030C}

We are now in a position to consider various applications of these operations on relations.

### 2.2. Redundancy {#codd-1970-relational-s2-2 .section tag=030D}

Redundancy in the named set of relations must be distinguished from redundancy in the stored set of representations. We are primarily concerned here with the former. To begin with, we need a precise notion of derivability for relations.

Suppose $\theta$ is a collection of operations on relations and each operation has the property that from its operands it yields a unique relation (thus natural join is eligible, but join is not). A relation $R$ is $\theta$-derivable from a set $S$ of relations if there exists a sequence of operations from the collection $\theta$ which, for all time, yields $R$ from members of $S$. The phrase “for all time” is present, because we are dealing with time-varying relations, and our interest is in derivability which holds over a significant period of time. For the named set of relationships in noninferential systems, it appears that an adequate collection $\theta_1$ contains the following operations: projection, natural join, tie, and restriction. Permutation is irrelevant and natural composition need not be included, because it is obtainable by taking a natural join and then a projection. For the stored set of representations, an adequate collection $\theta_2$ of operations would include permutation and additional operations concerned with subsetting and merging relations, and ordering and connecting their elements.

2.2.1. Strong Redundancy. A set of relations is strongly redundant if it contains at least one relation that possesses a projection which is derivable from other projections of relations in the set. The following two examples are intended to explain why strong redundancy is defined this way, and to demonstrate its practical use. In the first example the collection of relations consists of just the following relation:

employee (serial #, name, manager#, managername) with serial# as the primary key and manager# as a foreign key. Let us denote the active domain by $\Delta_t$, and suppose that

$$
\Delta_t(manager\#) \subset \Delta_t(serial\#)
$$

and

$$
\Delta_t(managername) \subset \Delta_t(name)
$$

for all time t. In this case the redundancy is obvious: the domain managername is unnecessary. To see that it is a strong redundancy as defined above, we observe that

$$
\pi_{34}(employee) = \pi_{12}(employee)_1|\pi_3(employee).
$$

In the second example the collection of relations includes a relation S describing suppliers with primary key s#, a relation D describing departments with primary key d#, a relation J describing projects with primary key j#, and the following relations:

$$
P(s\#, d\#, \cdots), \qquad Q(s\#, j\#, \cdots), \qquad R(d\#, j\#, \cdots),
$$

where in each case $\cdots$ denotes domains other than s#, d#, j#. Let us suppose the following condition C is known to hold independent of time: supplier s supplies department d (relation P) if and only if supplier s supplies some project j (relation Q) to which d is assigned (relation R). Then, we can write the equation

$$
\pi_{12}(P) = \pi_{12}(Q) \cdot \pi_{21}(R)
$$

and thereby exhibit a strong redundancy.

An important reason for the existence of strong redundancies in the named set of relationships is user convenience. A particular case of this is the retention of semi-obsolete relationships in the named set so that old programs that refer to them by name can continue to run correctly. Knowledge of the existence of strong redundancies in the named set enables a system or data base administrator greater freedom in the selection of stored representations to cope more efficiently with current traffic. If the strong redundancies in the named set are directly reflected in strong redundancies in the stored set (or if other strong redundancies are introduced into the stored set), then, generally speaking, extra storage space and update time are consumed with a potential drop in query time for some queries and in load on the central processing units.

2.2.2. Weak Redundancy. A second type of redundancy may exist. In contrast to strong redundancy it is not characterized by an equation. A collection of relations is weakly redundant if it contains a relation that has a projection which is not derivable from other members but is at all times a projection of some join of other projections of relations in the collection.

We can exhibit a weak redundancy by taking the second example (cited above) for a strong redundancy, and assuming now that condition C does not hold at all times.

The relations $\pi_{12}(P), \pi_{12}(Q), \pi_{12}(R)$ are complex$^{10}$ relations with the possibility of points of ambiguity occurring from time to time in the potential joining of any two. Under these circumstances, none of them is derivable from the other two. However, constraints do exist between them, since each is a projection of some cyclic join of the three of them. One of the weak redundancies can be characterized by the statement: for all time, $\pi_{12}(P)$ is *some* composition of $\pi_{12}(Q)$ with $\pi_{21}(R)$. The composition in question might be the natural one at some instant and a nonnatural one at another instant.

Generally speaking, weak redundancies are inherent in the logical needs of the community of users. They are not removable by the system or data base administrator. If they appear at all, they appear in both the named set and the stored set of representations.

### 2.3. Consistency {#codd-1970-relational-s2-3 .section tag=030E}

Whenever the named set of relations is redundant in either sense, we shall associate with that set a collection of statements which define all of the redundancies which hold independent of time between the member relations. If the information system lacks—and it most probably will—detailed semantic information about each named relation, it cannot deduce the redundancies applicable to the named set. It might, over a period of time, make attempts to induce the redundancies, but such attempts would be fallible.

Given a collection C of time-varying relations, an associated set Z of constraint statements and an instantaneous value V for C, we shall call the state (C, Z, V) consistent or inconsistent according as V does or does not satisfy Z. For example, given stored relations R, S, T together with the constraint statement "$\pi_{12}(T)$ is a composition of $\pi_{12}(R)$ with $\pi_{12}(S)$", we may check from time to time that the values stored for R, S, T satisfy this constraint. An algorithm for making this check would examine the first two columns of each of R, S, T (in whatever way they are represented in the system) and determine whether

(1) $\pi_1(T) = \pi_1(R)$,
(2) $\pi_2(T) = \pi_2(S)$,
(3) for every element pair $(a, c)$ in the relation $\pi_{12}(T)$ there is an element b such that $(a, b)$ is in $\pi_{12}(R)$ and $(b, c)$ is in $\pi_{12}(S)$.

There are practical problems (which we shall not discuss here) in taking an instantaneous snapshot of a collection of relations, some of which may be very large and highly variable.

It is important to note that consistency as defined above is a property of the instantaneous state of a data bank, and is independent of how that state came about. Thus, in particular, there is no distinction made on the basis of whether a user generated an inconsistency due to an act of omission or an act of commission. Examination of a simple

10 A binary relation is complex if neither it nor its converse is a function.

example will show the reasonableness of this (possibly unconventional) approach to consistency.

Suppose the named set $C$ includes the relations $S, J, D, P, Q, R$ of the example in Section 2.2 and that $P, Q, R$ possess either the strong or weak redundancies described therein (in the particular case now under consideration, it does not matter which kind of redundancy occurs). Further, suppose that at some time $t$ the data bank state is consistent and contains no project $j$ such that supplier 2 supplies project $j$ and $j$ is assigned to department 5. Accordingly, there is no element $(2, 5)$ in $\pi_{12}(P)$. Now, a user introduces the element $(2, 5)$ into $\pi_{12}(P)$ by inserting some appropriate element into $P$. The data bank state is now inconsistent. The inconsistency could have arisen from an act of omission, if the input $(2, 5)$ is correct, and there does exist a project $j$ such that supplier 2 supplies $j$ and $j$ is assigned to department 5. In this case, it is very likely that the user intends in the near future to insert elements into $Q$ and $R$ which will have the effect of introducing $(2, j)$ into $\pi_{12}(Q)$ and $(5, j)$ in $\pi_{12}(R)$. On the other hand, the input $(2, 5)$ might have been faulty. It could be the case that the user intended to insert some other element into $P$—an element whose insertion would transform a consistent state into a consistent state. The point is that the system will normally have no way of resolving this question without interrogating its environment (perhaps the user who created the inconsistency).

There are, of course, several possible ways in which a system can detect inconsistencies and respond to them. In one approach the system checks for possible inconsistency whenever an insertion, deletion, or key update occurs. Naturally, such checking will slow these operations down. If an inconsistency has been generated, details are logged internally, and if it is not remedied within some reasonable time interval, either the user or someone responsible for the security and integrity of the data is notified. Another approach is to conduct consistency checking as a batch operation once a day or less frequently. Inputs causing the inconsistencies which remain in the data bank state at checking time can be tracked down if the system maintains a journal of all state-changing transactions. This latter approach would certainly be superior if few non-transitory inconsistencies occurred.

### 2.4. SUMMARY {#codd-1970-relational-s2-4 .section tag=030F}

In Section 1 a relational model of data is proposed as a basis for protecting users of formatted data systems from the potentially disruptive changes in data representation caused by growth in the data bank and changes in traffic. A normal form for the time-varying collection of relationships is introduced.

In Section 2 operations on relations and two types of redundancy are defined and applied to the problem of maintaining the data in a consistent state. This is bound to become a serious practical problem as more and more different types of data are integrated together into common data banks.

Many questions are raised and left unanswered. For example, only a few of the more important properties of the data sublanguage in Section 1.4 are mentioned. Neither the purely linguistic details of such a language nor the implementation problems are discussed. Nevertheless, the material presented should be adequate for experienced systems programmers to visualize several approaches. It is also hoped that this paper can contribute to greater precision in work on formatted data systems.

Acknowledgment. It was C. T. Davies of IBM Poughkeepsie who convinced the author of the need for data independence in future information systems. The author wishes to thank him and also F. P. Palermo, C. P. Wang, E. B. Altman, and M. E. Senko of the IBM San Jose Research Laboratory for helpful discussions.

RECEIVED SEPTEMBER, 1969; REVISED FEBRUARY, 1970
