---
paper: shamir-1992-ippspace
title: IP = PSPACE
authors:
  - Adi Shamir
year: 1992
venue: Journal of the ACM
field: theory
section: "4"
section_title: '*Interactive Proofs for PSPACE Languages*'
tag: "0535"
kind: section
lang: en
source: http://crypto.cs.mcgill.ca/~crepeau/COMP647/2007/
pdf_sha256: 64e55264e8386142cd8821ddccb435579ecd13a50658047d488011145d5a405f
pdf_pages: 4-7
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: f4f0e55be4628e924b62f05d1022427a43e172f03a5e263e0e3a2c410ab3ee60
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Since deciding the truth of (simple) QBFs is known to be PSPACE complete (see Garey and Johnson [5]), it suffices to demonstrate the existence of interactive proofs for this problem. Given the arithmetic form $A$ of a simple QBF $B$, we want to prove that $A \neq 0 \pmod{p}$ for some polynomially long prime $p$. This prime can be chosen by the prover $P$ and sent to the verifier $V$ (along with a written proof of primality) as the first step of the interactive proof, since even an infinitely powerful cheating prover cannot find such a prime if $A = 0$. Alternatively, we can ask $V$ to choose a random prime $p$, and use the fact that for most $p$, $A \neq 0 \pmod{p}$ iff $B$ is true. This makes it possible to prove both membership and non-membership by the same protocol, but has imperfect completeness (even an honest prover may be unable to prove a correct statement if the verifier chooses a prime divisor of $A$).

Given a closed arithmetic expression $A$, we define its *functional form* $A'$ by eliminating the leftmost $\Sigma_{z_i \in \{0,1\}}$ or $\Pi_{z_i \in \{0,1\}}$ symbol, and considering $A'$ as a polynomial function $q(z_i)$ of one free variable $z_i$. The *randomized form* of $A$ is $A'(z_i = r)$ in which $z_i$ is set to a random number $r$ modulo $p$ supplied by the verifier. This randomized form can again be evaluated to a constant, but its number of $\Sigma$ and $\Pi$ symbols is reduced by 1. Note that the simplicity of $A$ is preserved by these transformations.

*Example.* Consider the true QBF:

$$
B = \forall x_1 [\bar{x}_1 \lor \exists x_2 \forall x_3 (x_1 \land x_2) \lor x_3],
$$

and assume that $p$ is large enough so that the following calculations are not affected by modular reductions. The arithmetic form of $B$ is

$$
A = \prod_{z_1 \in \{0,1\}} \left[ (1 - z_1) + \sum_{z_2 \in \{0,1\}} \prod_{z_3 \in \{0,1\}} (z_1 \cdot z_2 + z_3) \right],
$$

whose value is 2. The functional form of $A$ is:

$$
A' = \left[ (1 - z_1) + \sum_{z_2 \in \{0,1\}} \prod_{z_3 \in \{0,1\}} (z_1 \cdot z_2 + z_3) \right].
$$

By evaluating all the summations and products, the infinitely powerful prover can express $A'$ as the polynomial

$$
q(z_1) = z_1^2 + 1.
$$

The randomized form of $A'$ with $z_1 = 3$ can be expressed as

$$
A'(z_1 = 3) = \left[ (1 - 3) + \sum_{z_2 \in \{0,1\}} \prod_{z_3 \in \{0,1\}} (3z_2 + z_3) \right],
$$

whose value 10 can be deduced from $q(3) = 3^2 + 1 = 10$.

The polynomial $q(z_i)$ that represents $A'$ can have an exponentially high degree. Consider, for example, the QBF

$$
B = \forall x_1 \forall x_2 \cdots \forall x_n (x_1 \lor x_2 \lor \cdots \lor x_n),
$$

whose arithmetization is

$$
A = \prod_{z_1 \in \{0,1\}} \prod_{z_2 \in \{0,1\}} \cdots \prod_{z_n \in \{0,1\}} (z_1 + z_2 + \cdots + z_n).
$$

The polynomial $q(z_1)$ of its functional form $A'$ is the product of $2^{n-1}$ terms of the form $(z_1 + c)$ for $0 \leq c \leq n$, which is a dense polynomial of degree $2^{n-1}$. Such polynomials cannot be handled by the polynomial time verifier during the interactive proof. However, for simple QBFs we can prove:

THEOREM 5. *If B is simple, then the degree of the polynomial $q(z_i)$ that describes the functional form of A grows at most linearly with the size of B.*

PROOF. Let $x_i$ be the leftmost quantified variable in $B$. The degree of $z_i$ created by any quantifier-free subexpression of $B$ is bounded by the size of the subexpression. Summations over arbitrarily many other variables can change the coefficients but not the degree of the polynomial, and each product can at most double the degree. The result follows from the fact that in simple $B$ such a doubling can occur at most once. $\Box$

Remark. By adding sufficiently many dummy variables to the quantifier-free subexpressions of $B$, this degree can be reduced to 3, and thus $q(z_i)$ can be represented by just four numbers in $\mathbb{Z}_p$. Consider for example $B = \forall x_i B'$ where $x_i$ occurs $k$ times in $B'$. This expression can be replaced by

$$
\forall x_i^1 \exists x_i^2 \cdots \exists x_i^k (x_i^1 = x_i^2 = \cdots = x_i^k) \land B'' ,
$$

where $B''$ is obtained from $B'$ by using a different $x'_i$ variable in each occurrence of $x_i$ in $B'$. If $B$ is simple and the multiple equality is arithmetized as $z_1^1 \cdot z_1^2 \cdots z_1^k + (1 - z_1^1)(1 - z_1^2) \cdots (1 - z_1^k)$, the degree of each functional form is at most 3.

The interactive protocol for proving that $A \neq 0 \pmod{p}$ is very simple. The prover $P$ sends the claimed value $a$ of $A \pmod{p}$ to the verifier $V$, and justifies this claim by considering successively smaller subexpressions of $A$. At any intermediate stage of the protocol, the current expression $A$ is split into $A_1 + A_2$ or $A_1 \cdot A_2$ where $A_1$ is a polynomial with fully instantiated variables (whose value $a_1$ can be computed by $V$ himself), and $A_2$ starts with the leftmost $\Sigma$ or $\Pi$ symbol of $A$. $P$ and $V$ then repeatedly execute the following simplification steps:

(1) If $A_2$ is empty, $V$ stops and accepts the claim iff $a = a_1$.
(2) If $A_1$ is nonempty, $V$ replaces $A$ by $A_2$, and replaces $a$ by $a - a_1 \pmod{p}$ or $a / a_1 \pmod{p}$ (depending on the operator that connects $A_1$ and $A_2$). If $V$ tries to divide $a$ by $a_1 = 0 \pmod{p}$, he stops and accepts the claim iff $a = 0 \pmod{p}$.
(3) Otherwise, $P$ sends the polynomial descriptions $q(z_i)$ of $A'$ to $V$. $V$ checks that $a = q(0) + q(1) \pmod{p}$ or $a = q(0) \cdot q(1) \pmod{p}$ (depending on the first symbol of $A_2$), sends a random $r \in \mathbb{Z}_p$ to $P$, replaces $A$ by $A'(z_i = r) \pmod{p}$, and replaces $a$ by $q(r) \pmod{p}$.

Example. Consider once more the expression $A$ of the previous example, whose claimed value is $a = 2$. When $P$ sends its polynomial $q(z_1) = z_1^2 + 1$ to $V, V$ checks that $q(0) \cdot q(1) = 1 \cdot 2 = a$, sends $z_1 = 3$ to $P$, replaces $A$ by $A'(z_1 = 3)$, and replaces $a$ by $q(3) = 10$. The new $A$ starts with a nonempty $A_1$, whose value $a_1 = (1 - 3) = -2$ can be computed by $V$. $A$ and $a$ are now adjusted to

$$
A = \sum_{z_2 \in \{0,1\}} \prod_{z_3 \in \{0,1\}} (3z_2 + z_3),
$$

$$
a = 10 - (-2) = 12.
$$

The functional form of this $A$ is

$$
A' = \prod_{z_3 \in \{0,1\}} (3z_2 + z_3),
$$

whose polynomial representation is $q(z_2) = 9z_2^2 + 3z_2$. When $V$ gets this polynomial from $P$, he checks that $q(0) + q(1) = 0 + 12 = 12 = a$, and picks $z_2 = 2$ as his random choice. $A$ and $a$ are again adjusted to

$$
A = \prod_{z_3 \in \{0,1\}} (6 + z_3),
$$

$$
a = q(2) = 9 \cdot 4 + 3 \cdot 2 = 42.
$$

$P$ now sends $q(z_3) = z_3 + 6$ as the polynomial representation of $A'$, and $V$ checks that $q(0) \cdot q(1) = 6 \cdot 7 = 42 = a$. Finally, $V$ chooses $z_3 = 5$, and verifies by himself that the value of

$$
A'(z_3 = 5) = (6 + 5) = 11
$$

is the same as $a = q(5) = 5 + 6 = 11$.

THEOREM 6

(1) When B is true and P is honest, V always accepts the proof.
(2) When B is false, V accepts the proof with negligible probability.

PROOF

(1) An honest P can always justify his claimed values and polynomials.
(2) The proof of this part is similar to the one used by Lund et al. [10] in their permanent proving protocol. A cheating prover who supplied an incorrect value of a must provide an incorrect polynomial q(z_t) to support his claim, since a is checked against q(0) + q(1) (mod p) or q(0) · q(1) (mod p). By the interpolation theorem, such an incorrect polynomial of degree t can agree with the correct polynomial on at most t of the p points in $\mathbb{Z}_p$. When the value of t is a polynomial and the value of p is exponential in the size of B, there is only a negligible probability that the incorrect q yields a correct value when evaluated at a random point r chosen by V. As a result, a cheating P is forced to provide incorrect values for successively smaller subexpressions, until he is exposed with overwhelming probability when V evaluates the final subexpression by himself. □

Remark. A single application of this protocol suffices to make the probability of cheating exponentially small, and there is no need to iterate it as in other interactive proofs. However, the protocol seems to be inherently sequential, and it is a major open problem whether it can be executed with a small (e.g., logarithmic) number of rounds. Note that the existence of a constant round protocol for IP would collapse the polynomial hierarchy to its second level, as shown by Boppana et al. [3].
