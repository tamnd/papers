---
paper: ford-1956-maxflow
title: Maximal Flow Through a Network
authors:
  - L. R. Ford Jr.
  - D. R. Fulkerson
year: 1956
venue: Canadian Journal of Mathematics
field: algorithms
section_title: L. R. Ford, Jr. and D. R. Fulkerson
kind: section
lang: en
source: https://www.cs.yale.edu/homes/lans/readings/routing/ford-max_flow-1956.pdf
pdf_sha256: ad378e3c07842a685e94f4cd4c2a18ae2fabe4d39a65338afd896fb069b394a1
pdf_pages: 1-6
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 909c66bc21c54753dc872fe95adfefffbd41c172d18fc67ffbcf23fa8eb10b4f
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Introduction. The problem discussed in this paper was formulated by T. Harris as follows:
"Consider a rail network connecting two cities by way of a number of intermediate cities, where each link of the network has a number assigned to it representing its capacity. Assuming a steady state condition, find a maximal flow from one given city to the other."
While this can be set up as a linear programming problem with as many equations as there are cities in the network, and hence can be solved by the simplex method (1), it turns out that in the cases of most practical interest, where the network is planar in a certain restricted sense, a much simpler and more efficient hand computing procedure can be described.
In §1 we prove the minimal cut theorem, which establishes that an obvious upper bound for flows over an arbitrary network can always be achieved. The proof is non-constructive. However, by specializing the network (§2), we obtain as a consequence of the minimal cut theorem an effective computational scheme. Finally, we observe in §3 the duality between the capacity problem and that of finding the shortest path, via a network, between two given points.

1. The minimal cut theorem. A graph G is a finite, 1-dimensional complex, composed of vertices $a, b, c, \ldots, e$, and arcs $\alpha(ab), \beta(ac), \ldots, \delta(ce)$. An arc $\alpha(ab)$ joins its end vertices $a, b$; it passes through no other vertices of $G$ and intersects other arcs only in vertices. A chain is a set of distinct arcs of $G$ which can be arranged as $\alpha(ab), \beta(bc), \gamma(cd), \ldots, \delta(gh)$, where the vertices $a, b, c, \ldots, h$ are distinct, i.e., a chain does not intersect itself; a chain joins its end vertices $a$ and $h$.
We distinguish two vertices of $G$: $a$, the source, and $b$, the sink.$^1$ A chain flow from $a$ to $b$ is a couple $(C; k)$ composed of a chain $C$ joining $a$ and $b$, and a non-negative number $k$ representing the flow along $C$ from source to sink.
Each arc in $G$ has associated with it a positive number called its capacity. We call the graph $G$, together with the capacities of its individual arcs, a network. A flow in a network is a collection of chain flows which has the property that the sum of the numbers of all chain flows that contain any arc is no greater than the capacity of that arc. If equality holds, we say the arc is saturated by the flow. A chain is saturated with respect to a flow if it contains

Received September 20, 1955.

$^1$The case in which there are many sources and sinks with shipment permitted from any source to any sink is obviously reducible to this.

a saturated arc. The value of a flow is the sum of the numbers of all the chain flows which compose it.

It is clear that the above definition of flow is not broad enough to include everything that one intuitively wishes to think of as a flow, for example, sending trains out a dead end and back or around a circuit, but as far as effective transportation is concerned, the definition given suffices.

A disconnecting set is a collection of arcs which has the property that every chain joining $a$ and $b$ meets the collection. A disconnecting set, no proper subset of which is disconnecting, is a cut. The value of a disconnecting set $D$ (written $v(D)$) is the sum of the capacities of its individual members. Thus a disconnecting set of minimal value is automatically a cut.

Theorem 1. (Minimal cut theorem). *The maximal flow value obtainable in a network $N$ is the minimum of $v(D)$ taken over all disconnecting sets $D$.* {#ford-1956-maxflow-thm-1 .statement tag=031D}

*Proof.* There are only finitely many chains joining $a$ and $b$, say $n$ of them. If we associate with each one a coordinate in $n$-space, then a flow can be represented by a point whose $j$th coordinate is the number attached to the chain flow along the $j$th chain. With this representation, the class of all flows is a closed, convex polytope in $n$-space, and the value of a flow is a linear functional on this polytope. Hence, there is a maximal flow, and the set of all maximal flows is convex.

Now let $S$ be the class of all arcs which are saturated in every maximal flow.

Lemma 1. *$S$ is a disconnecting set.* {#ford-1956-maxflow-lem-1 .statement tag=031E}

Suppose not. Then there exists a chain $\alpha_1, \alpha_2, \ldots, \alpha_m$ joining $a$ and $b$ with $\alpha_i \notin S$ for each $i$. Hence, corresponding to each $\alpha_i$, there is a maximal flow $f_i$ in which $\alpha_i$ is unsaturated. But the average of these flows,

$$
f = \frac{1}{m} \sum f_i,
$$

is maximal and $\alpha_i$ is unsaturated by $f$ for each $i$. Thus the value of $f$ may be increased by imposing a larger chain flow on $\alpha_1, \alpha_2, \ldots, \alpha_m$, contradicting maximality.

Notice that the orientation assigned to an arc of $S$ by a positive chain flow of a maximal flow is the same for all such chain flows. For suppose first that $(C_1, k_1), (C_2, k_2)$ are two chain flows occurring in a maximal flow $f, k_1 \geq k_2 > 0$, where

$$
C_1 = \alpha_1(a a_1), \alpha_2(a_1 a_2), \ldots, \alpha_j(a_{j-1}, a_j), \ldots, \alpha_r(a_{r-1}, b)
$$

$$
C_2 = \beta_1(a b_1), \beta_2(b_1 b_2), \ldots, \beta_k(b_{k-1}, b_k), \ldots, \beta_s(b_{s-1}, b),
$$

and $\alpha_j(a_{j-1}, a_j) = \beta_k(b_{k-1}, b_k) \in S, a_{j-1} = b_k, a_j = b_{k-1}$. Then

$$
C'_1 = \alpha_1, \alpha_2, \ldots, \alpha_{j-1}, \beta_{k+1}, \ldots, \beta_s
$$

$$
C'_2 = \beta_1, \beta_2, \ldots, \beta_{k-1}, \alpha_{j+1}, \ldots, \alpha_r
$$

contain chains $C_1''$, $C_2''$ joining $a$ and $b$, and another maximal flow can be obtained from $f$ as follows. Reduce the $C_1$ and $C_2$ components of $f$ each by $k_2$, and increase each of the $C_1''$ and $C_2''$ components by $k_2$. This unsaturates the arc $\alpha_j$, contradicting its definition as an element of $S$. On the other hand, if $(C_1, k_1), (C_2, k_2)$ were members of distinct maximal flows $f_1, f_2$, consideration of $f = \frac{1}{2}(f_1 + f_2)$ brings us back to the former case. Hence, the arcs of $S$ have a definite orientation assigned to them by maximal flows. We refer to that vertex of an arc $\alpha \in S$ which occurs first in a positive chain flow of a maximal flow as the left vertex of $\alpha$.

Now define a left arc of $S$ as follows: an arc $\alpha$ of $S$ is a left arc if and only if there is a maximal flow $f$ and a chain $\alpha_1, \alpha_2, \ldots, \alpha_k$ (possibly null) joining $a$ and the left vertex of $\alpha$ with no $\alpha_i$ saturated by $f$. Let $L$ be the set of left arcs of $S$.

Lemma 2. $L$ is a disconnecting set. {#ford-1956-maxflow-lem-2 .statement tag=031F}

Given an arbitrary chain $\alpha_1(a\ a_1), \alpha_2(a_1a_2), \ldots, \alpha_m(a_{m-1}\ b)$ joining $a$ and $b$, it must intersect $S$ by Lemma 1. Let $\alpha_t(a_{t-1}, a_t)$ be the first $\alpha_i \in S$. Then for each $\alpha_i, i < t$, there is a maximal flow $f_i$ in which $\alpha_i$ is unsaturated. The average of these flows provides a maximal flow $f$ in which $\alpha_1, \alpha_2, \ldots, \alpha_{t-1}$ are unsaturated. It remains to show that this chain joins $a$ to the left vertex of $\alpha_t$, i.e., $a_{t-1}$ is the left vertex of $\alpha_t$. Suppose not. Then the maximal flow $f$ contains a chain flow

$$
[\beta_1(ab_1), \beta_2(b_1, b_2), \ldots, \beta_r(b_{r-1}, b); k],\ k > 0,\ \beta_s = \alpha_t,\ b_{s-1} = a_t,\ b_s = a_{t-1}.
$$

Let the amount of unsaturation in $f$ of $\alpha_i \ (i = 1, \ldots, t - 1)$, be $k_i > 0$. Now alter $f$ as follows: decrease the flow along the chain $\beta_1, \beta_2, \ldots, \beta_r$ by $\min[k, k_i] > 0$ and increase the flow along the chain contained in

$$
\alpha_1, \alpha_2, \ldots, \alpha_{t-1}, \beta_{s+1}, \ldots, \beta_r
$$

by this amount. The result is a maximal flow in which $\alpha_t$ is unsaturated, a contradiction. Hence $\alpha_t \in L$.

Lemma 3. No positive chain flow of a maximal flow can contain more than one arc of $L$. {#ford-1956-maxflow-lem-3 .statement tag=0320}

Assume the contrary, that is, there is a maximal flow $f_1$ containing a chain flow

$$
[\beta_1(ab_1), \beta_2(b_1b_2), \ldots, \beta_r(b_{r-1}, b); k],\ k > 0,
$$

with arcs $\beta_i, \beta_j \in L, \beta_i$ occurring before $\beta_j$, say, in the chain. Let $f_2$ be that maximal flow for which there is an unsaturated chain

$$
\alpha_1(aa_1),\ \alpha_2(a_1, a_2), \ldots, \alpha_s(a_{s-1}, b_{j-1})
$$

from $a$ to the left vertex of $\beta_j$. Consider $f = \frac{1}{2}(f_1 + f_2)$. This maximal flow contains the chain flow $[\beta_1, \beta_2, \ldots, \beta_r; k']$ with $k' \geq \frac{1}{2}k$, and each $\alpha_i (i = 1, \ldots, s)$ is unsaturated by $k_i > 0$ in $f$. Again alter $f$: decrease the flow along

$\beta_1, \beta_2, \ldots, \beta_r$ by min $[k', k_i] > 0$ and increase the flow along the chain contained in $\alpha_1, \alpha_2, \ldots, \alpha_s, \beta_j, \ldots, \beta_r$ by the same amount, obtaining a maximal flow in which $\beta_i$ is unsaturated, a contradiction.

Now to prove the theorem it suffices only to remark that the value of every flow is no greater than $v(D)$ where $D$ is any disconnecting set; and on the other hand we see from Lemma 3 and the definition of $S$ that in adding the capacities of arcs of $L$ we have counted each chain flow of a maximal flow just once. Since by Lemma 2 $L$ is a disconnecting set, we have the reverse inequality. Thus $L$ is a minimal cut and the value of a maximal flow is $v(L)$.

We shall refer to the value of a maximal flow through a network $N$ as the capacity of $N$ ($\operatorname{cap}(N)$). Then note the following corollary of the minimal cut theorem.

Corollary. *Let $A$ be a collection of arcs of a network $N$ which meets each cut of $N$ in just one arc. If $N'$ is a network obtained from $N$ by adding $k$ to the capacity of each arc of $A$, then $\operatorname{cap}(N') = \operatorname{cap}(N) + k$.*

It is worth pointing out that the minimal cut theorem is not true for networks with several sources and corresponding sinks, where shipment is restricted to be from a source to its sink. For example, in the network (Fig. 1) with shipment from $a_i$ to $b_i$ and capacities as indicated, the value of a minimal disconnecting set (i.e., a set of arcs meeting all chains joining sources and corresponding sinks) is 4, but the value of a maximal flow is 3.

Figure.

Fig. 1

2. **A computing procedure for source-sink planar networks.** We say that a network $N$ is *planar* with respect to its source and sink, or briefly, $N$ is *ab*-planar, provided the graph $G$ of $N$, together with arc $ab$, is a planar

2It was conjectured by G. Dantzig, before a proof of the minimal cut theorem was obtained, that the computing procedure described in this section would lead to a maximal flow for planar networks.

graph $(2; 3)$. (For convenience, we suppose there is no arc in $G$ joining $a$ and $b$.) The importance of $ab$-planar networks lies in the following theorem.

**Theorem 2.** *If $N$ is ab-planar, there exists a chain joining $a$ and $b$ which meets each cut of $N$ precisely once.* {#ford-1956-maxflow-thm-2 .statement tag=0321}

*Proof.* We may assume, without loss of generality, that the arc $ab$ is part of the boundary of the outside region, and that $G$ lies in a vertical strip with $a$ located on the left bounding line of the strip, $b$ on the right. Let $T$ be the chain joining $a$ and $b$ which is top-most in $N$. $T$ has the desired property, as we now show. Suppose not. Then there is a cut $D$, at least two arcs of which are in $T$. Let these be $\alpha_1$ and $\alpha_2$, with $\alpha_1$ occurring before $\alpha_2$ in following $T$ from $a$ to $b$. Since $D$ is a cut, there is a chain $C_1$ joining $a$ and $b$ which meets $D$ in $\alpha_1$ only. Similarly there is a chain $C_2$ meeting $D$ in $\alpha_2$ only. Let $C_2'$ be that part of $C_2$ joining $a$ to an end point of $\alpha_2$. It follows from the definition of $T$ that $C_1$ and $C_2'$ must intersect. But now, starting at $a$, follow $C_2'$ to its last intersection with $C_1$, then $C_1$ to $b$. We thus have a chain from $a$ to $b$ not meeting $D$, contradicting the fact that $D$ is a cut.

Symmetrically, of course, the bottom-most chain of $N$ has the same property.

Notice that this theorem is not valid for networks which are not $ab$-planar. A simple example showing this is provided by the "gas, water, electricity" graph (Fig. 2), in which every chain joining $a$ and $b$ meets some cut in three arcs.

Figure.

Fig. 2

Theorem 2 and the corollary to Theorem 1 provide an easy computational procedure for determining a maximal flow in a network of the kind here considered. Simply locate a chain having the property of Theorem 2; this can be done at a glance by finding the two regions separated by arc $ab$, and taking the rest of the boundary of either region (throwing out portions of the boundary where it has looped back and intersected itself, so as to get a chain). Impose as large a chain flow $(T; k)$ as possible on this chain, thereby saturating one or more of its arcs. By the corollary, subtracting $k$ from each capacity in $T$ reduces the capacity of $N$ by $k$. Delete the saturated arcs, and proceed as before. Eventually, the graph disconnects, and a maximal flow has been constructed. {#ford-1956-maxflow-thm-2-2 .statement tag=0322}

3. A minimal path problem. For source-sink planar networks, there is an interesting duality between the problem of finding a chain of minimal capacity-sum joining source and sink and the network capacity problem, which lies in the fact that chains of $N$ joining source and sink correspond to cuts (relative to two particular vertices) of the dual$^3$ of $N$ and vice versa. More precisely, suppose one has a network $N$, planar relative to two vertices $a$ and $b$, and wishes to find a chain joining $a$ and $b$ such that the sum of the numbers assigned to the arcs of the chain is minimal. An easy way to solve this problem is as follows. Add the arc $ab$, and construct the dual of the resulting graph $G$. Let $a'$ and $b'$ be the vertices of the dual which lie in the regions of $G$ separated by $ab$. Assign each number of the original network to the corresponding arc in the dual. Then solve the capacity problem relative to $a'$ and $b'$ for the dual network by the procedure of §2. A minimal cut thus constructed corresponds to a minimal chain in the original network.

$^3$The dual of a planar graph $G$ is formed by taking a vertex inside each region of $G$ and connecting vertices which lie in adjacent regions by arcs. See (2; 3).
