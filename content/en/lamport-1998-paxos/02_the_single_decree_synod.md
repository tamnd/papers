---
paper: lamport-1998-paxos
title: The Part-Time Parliament
authors:
  - Leslie Lamport
year: 1998
venue: ACM TOCS
field: systems
section: "2"
section_title: The Single-Decree Synod
tag: 023E
kind: section
lang: en
source: https://lamport.azurewebsites.net/pubs/lamport-paxos.pdf
pdf_sha256: cd9544e9615bcd417a2c10063671cecca0b28ad4bc5db3f64467a83ecc7028d3
pdf_pages: 5-16
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 07e14f985f0eb4ab9a452c8901e1f5eb32422918b1b6a05be53fc75a98e7630a
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The Paxon Parliament evolved from an earlier ceremonial Synod of priests that was convened every 19 years to choose a single, symbolic decree. For centuries, the Synod had chosen the decree by a conventional procedure that required all priests to be present. But as commerce flourished, priests began wandering in and out of the Chamber while the Synod was in progress. Finally, the old protocol failed, and a Synod ended with no decree chosen. To prevent a repetition of this theological disaster, Paxon religious leaders asked mathematicians to formulate a protocol for choosing the Synod’s decree. The protocol’s requirements and assumptions were essentially the same as those of the later Parliament except that instead of containing a sequence of decrees, a ledger would have at most one decree. The resulting Synod protocol is described here; the Parliamentary protocol is described in Section 3.

Mathematicians derived the Synod protocol in a series of steps. First, they proved results showing that a protocol satisfying certain constraints would guarantee consistency and allow progress. A preliminary protocol was then derived directly from these constraints. A restricted version of the preliminary protocol provided the basic protocol that guaranteed consistency, but not progress. The complete Synod protocol, satisfying the consistency and progress requirements, was obtained by restricting the basic protocol. 4

The mathematical results are described in Section 2.1, and the protocols are described informally in Sections 2.2–2.4. A more formal description and correctness proof of the basic protocol appears in the appendix.

4 The complete history of the Synod protocol’s discovery is not known. Like modern computer scientists, Paxon mathematicians would describe elegant, logical derivations that bore no resemblance to how the algorithms were actually derived. However, it is known that the mathematical results (Theorems 1 and 2 of Section 2.1) really did precede the protocol. They were discovered when mathematicians, in response to the request for a protocol, were attempting to prove that a satisfactory protocol was impossible.

### 2.1 Mathematical Results {#lamport-1998-paxos-s2-1 .section tag=023F}

The Synod’s decree was chosen through a series of numbered ballots, where a ballot was a referendum on a single decree. In each ballot, a priest had the choice only of voting for the decree or not voting. 5 Associated with a ballot was a set of priests called a quorum. A ballot succeeded iff (if and only if) every priest in the quorum voted for the decree. Formally, a ballot B consisted of the following four components. (Unless otherwise qualified, set is taken to mean finite set. 6 )

B dec A decree (the one being voted on). B qrm A nonempty set of priests (the ballot’s quorum). B A set of priests (the ones who cast votes for the decree). 7 vot B bal A ballot number. A ballot B was said to be successful iff B qrm ⊆ B vot , so a successful ballot was one in which every quorum member voted.

Ballot numbers were chosen from an unbounded ordered set of numbers. If B bal > B bal , then ballot B was said to be later than ballot B. However, this indicated nothing about the order in which ballots were conducted; a later ballot could actually have taken place before an earlier one.

Paxon mathematicians defined three conditions on a set B of ballots, and then showed that consistency was guaranteed and progress was possible if the set of ballots that had taken place satisfied those conditions. The first two conditions were simple; they can be stated informally as follows.

B1(B) Each ballot in B has a unique ballot number. B2(B) The quorums of any two ballots in B have at least one priest in common.

The third condition was more complicated. One Paxon manuscript contained the following, rather confusing, statement of it.

B3(B) For every ballot B in B, if any priest in B’s quorum voted in an earlier ballot in B, then the decree of B equals the decree of the latest of those earlier ballots.

Interpretation of this cryptic text was aided by the manuscript pictured in Figure 1, which illustrates condition B3(B) with a set B of five ballots for a Synod consisting of the five priests A, B, Γ, ∆, and E. This set B contains five ballots, where for each ballot, the set of voters is the subset of the priests in the quorum whose names are enclosed in boxes. For example, ballot number 14 has decree α, a quorum containing three priests, and a set of two voters. Condition B3(B) has the form “for every B in B: . . . ”, where “. . .” is a condition on ballot B. The conditions for the five ballots B of Figure 1 are as follows.

5 Like some modern nations, Paxos had not fully grasped the nature of Athenian democracy. 6 Although Paxon mathematicians were remarkably advanced for their time, they obviously had no knowledge of set theory. I have taken the liberty of translating the Paxon’s more primitive notation into the language of modern set theory. 7 Only priests in the quorum actually voted, but Paxon mathematicians found it easier to convince people that the protocol was correct if, in their proof, they allowed any priest to vote in any ballot.

| # | decree | quorum and voters |
| --- | --- | --- |
| 2 | $\alpha$ | A B $\Gamma$ $\Delta$ |
| 5 | $\beta$ | A B $\Gamma$ E |
| 14 | $\alpha$ | B $\Delta$ E |
| 27 | $\beta$ | A $\Gamma$ $\Delta$ |
| 29 | $\beta$ | B $\Gamma$ $\Delta$ |

Fig. 1. Paxon manuscript showing a set $\mathcal{B}$, consisting of five ballots, that satisfies conditions $B1(\mathcal{B})–B3(\mathcal{B})$. (Explanatory column headings have been added.) {#lamport-1998-paxos-fig-1 .figure tag=022B}

2. Ballot number 2 is the earliest ballot, so the condition on that ballot is trivially true.
5. None of ballot 5’s four quorum members voted in an earlier ballot, so the condition on ballot 5 is also trivially true.
14. The only member of ballot 14’s quorum to vote in an earlier ballot is $\Delta$, who voted in ballot number 2, so the condition requires that ballot 14’s decree must equal ballot 2’s decree.
27. (This is a successful ballot.) The members of ballot 27’s quorum are A, $\Gamma$, and $\Delta$. Priest A did not vote in an earlier ballot, the only earlier ballot $\Gamma$ voted in was ballot 5, and the only earlier ballot $\Delta$ voted in was ballot 2. The latest of these two earlier ballots is ballot 5, so the condition requires that ballot 27’s decree must equal ballot 5’s decree.
29. The members of ballot 29’s quorum are B, $\Gamma$, and $\Delta$. The only earlier ballot that B voted in was number 14, priest $\Gamma$ voted in ballots 5 and 27, and $\Delta$ voted in ballots 2 and 27. The latest of these four earlier ballots is number 27, so the condition requires that ballot 29’s decree must equal ballot 27’s decree.

To state $B1(\mathcal{B})–B3(\mathcal{B})$ formally requires some more notation. A *vote* $v$ was defined to be a quantity consisting of three components: a priest $v_{pst}$, a ballot number $v_{bal}$, and a decree $v_{dec}$. It represents a vote cast by priest $v_{pst}$ for decree $v_{dec}$ in ballot number $v_{bal}$. The Paxons also defined *null* votes to be votes $v$ with $v_{bal} = -\infty$ and $v_{dec} = \mathrm{BLANK}$, where $-\infty < b < \infty$ for any ballot number $b$, and BLANK is not a decree. For any priest $p$, they defined $null_p$ to be the unique null vote $v$ with $v_{pst} = p$.

Paxon mathematicians defined a total ordering on the set of all votes, but part of the manuscript containing the definition has been lost. The remaining fragment indicates that, for any votes $v$ and $v'$, if $v_{bal} < v'_{bal}$ then $v < v'$. It is not known how the relative order of $v$ and $v'$ was defined if $v_{bal} = v'_{bal}$.

For any set $\mathcal{B}$ of ballots, the set $Votes(\mathcal{B})$ of votes in $\mathcal{B}$ was defined to consist of all votes $v$ such that $v_{pst} \in B_{vot}$, $v_{bal} = B_{bal}$, and $v_{dec} = B_{dec}$ for some $B \in \mathcal{B}$. If $p$ is a priest and $b$ is either a ballot number or $\pm \infty$, then $MaxVote(b, p, \mathcal{B})$ was defined to be the largest vote $v$ in $Votes(\mathcal{B})$ cast by $p$ with $v_{bal} < b$, or to be $null_p$ if there was no such vote. Since $null_p$ is smaller than any real vote cast by $p$, this means that $MaxVote(b, p, \mathcal{B})$ is the largest vote in the set

$$
\{ v \in Votes(\mathcal{B}) : (v_{pst} = p) \land (v_{bal} < b) \} \cup \{ null_p \}
$$

For any nonempty set $Q$ of priests, $MaxVote(b, Q, \mathcal{B})$ was defined to equal the maximum of all votes $MaxVote(b, p, \mathcal{B})$ with $p$ in $Q$.

Conditions $B1(\mathcal{B})–B3(\mathcal{B})$ are stated formally as follows.$^8$

$$
\begin{align*}
B1(\mathcal{B}) &\triangleq \forall B, B' \in \mathcal{B} : (B \neq B') \Rightarrow (B_{bal} \neq B'_{bal}) \\
B2(\mathcal{B}) &\triangleq \forall B, B' \in \mathcal{B} : B_{qrm} \cap B'_{qrm} \neq \emptyset \\
B3(\mathcal{B}) &\triangleq \forall B \in \mathcal{B} : (MaxVote(B_{bal}, B_{qrm}, \mathcal{B})_{bal} \neq -\infty) \Rightarrow \\
&\phantom{\forall B \in \mathcal{B} :} (B_{dec} = MaxVote(B_{bal}, B_{qrm}, \mathcal{B})_{dec})
\end{align*}
$$

Although the definition of $MaxVote$ depends upon the ordering of votes, $B1(\mathcal{B})$ implies that $MaxVote(b, Q, \mathcal{B})_{dec}$ is independent of how votes with equal ballot numbers were ordered.

To show that these conditions imply consistency, the Paxons first showed that $B1(\mathcal{B})–B3(\mathcal{B})$ imply that, if a ballot $B$ in $\mathcal{B}$ is successful, then any later ballot in $\mathcal{B}$ is for the same decree as $B$.

Lemma *If* $B1(\mathcal{B}), B2(\mathcal{B}),$ and $B3(\mathcal{B})$ *hold*, then*

$$
((B_{qrm} \subseteq B_{vot}) \land (B'_{bal} > B_{bal})) \Rightarrow (B'_{dec} = B_{dec})
$$

*for any* $B, B'$ *in* $\mathcal{B}$.

**Proof of Lemma**
For any ballot $B$ in $\mathcal{B}$, let $\Psi(B, \mathcal{B})$ be the set of ballots in $\mathcal{B}$ later than $B$ for a decree different from $B$'s:

$$
\Psi(B, \mathcal{B}) \triangleq \{ B' \in \mathcal{B} : (B'_{bal} > B_{bal}) \land (B'_{dec} \neq B_{dec}) \}
$$

To prove the lemma, it suffices to show that if $B_{qrm} \subseteq B_{vot}$ then $\Psi(B, \mathcal{B})$ is empty. The Paxons gave a proof by contradiction. They assumed the existence of a $B$ with $B_{qrm} \subseteq B_{vot}$ and $\Psi(B, \mathcal{B}) \neq \emptyset$, and obtained a contradiction as follows.$^9$

1. Choose $C \in \Psi(B, \mathcal{B})$ such that $C_{bal} = \min\{ B'_{bal} : B' \in \Psi(B, \mathcal{B}) \}$.
   **Proof:** $C$ exists because $\Psi(B, \mathcal{B})$ is nonempty and finite.
2. $C_{bal} > B_{bal}$
   **Proof:** By 1 and the definition of $\Psi(B, \mathcal{B})$.
3. $B_{vot} \cap C_{qrm} \neq \emptyset$
   **Proof:** By $B2(\mathcal{B})$ and the hypothesis that $B_{qrm} \subseteq B_{vot}$.

\footnotetext{8}{I use the Paxon mathematical symbol $\triangleq$, which meant *equals by definition*.}
\footnotetext{9}{Paxon mathematicians always provided careful, structured proofs of important theorems. They were not as sophisticated as modern mathematicians, who can omit many details and write paragraph-style proofs without ever making a mistake.}

4. $MaxVote(C_{bal}, C_{qrm}, \mathcal{B})_{bal} \geq B_{bal}$

Proof: By 2, 3 and the definition of $MaxVote(C_{bal}, C_{qrm}, \mathcal{B})$.
5. $MaxVote(C_{bal}, C_{qrm}, \mathcal{B}) \in Votes(\mathcal{B})$
Proof: By 4 (which implies that $MaxVote(C_{bal}, C_{qrm}, \mathcal{B})$ is not a null vote) and the definition of $MaxVote(C_{bal}, C_{qrm}, \mathcal{B})$.
6. $MaxVote(C_{bal}, C_{qrm}, \mathcal{B})_{dec} = C_{dec}$
Proof: By 5 and $B3(\mathcal{B})$.
7. $MaxVote(C_{bal}, C_{qrm}, \mathcal{B})_{dec} \neq B_{dec}$
Proof: By 6, 1, and the definition of $\Psi(B, \mathcal{B})$.
8. $MaxVote(C_{bal}, C_{qrm}, \mathcal{B})_{bal} > B_{bal}$
Proof: By 4, since 7 and $B1(\mathcal{B})$ imply that $MaxVote(C_{bal}, C_{qrm}, \mathcal{B})_{bal} \neq B_{bal}$.
9. $MaxVote(C_{bal}, C_{qrm}, \mathcal{B}) \in Votes(\Psi(B, \mathcal{B}))$
Proof: By 7, 8, and the definition of $\Psi(B, \mathcal{B})$.
10. $MaxVote(C_{bal}, C_{qrm}, \mathcal{B})_{bal} < C_{bal}$
Proof: By definition of $MaxVote(C_{bal}, C_{qrm}, \mathcal{B})$.
11. Contradiction
Proof: By 9, 10, and 1.

End Proof of Lemma

With this lemma, it was easy to show that, if $B1–B3$ hold, then any two successful ballots are for the same decree.

Theorem 1. *If $B1(\mathcal{B}), B2(\mathcal{B}),$ and $B3(\mathcal{B})$ hold, then* {#lamport-1998-paxos-thm-1 .statement tag=022C}

$$
((B_{qrm} \subseteq B_{vot}) \land (B'_{qrm} \subseteq B'_{vot})) \Rightarrow (B'_{dec} = B_{dec})
$$

*for any $B, B'$ in $\mathcal{B}$.*

Proof of Theorem
If $B'_{bal} = B_{bal}$, then $B1(\mathcal{B})$ implies $B' = B$. If $B'_{bal} \neq B_{bal}$, then the theorem follows immediately from the lemma.
End Proof of Theorem

The Paxons then proved a theorem asserting that if there are enough priests in the Chamber, then it is possible to conduct a successful ballot while preserving $B1–B3$. Although this does not guarantee progress, it at least shows that a balloting protocol based on $B1–B3$ will not deadlock.

Theorem 2. *Let b be a ballot number and Q a set of priests such that $b > B_{bal}$ and $Q \cap B_{qrm} \neq \emptyset$ for all $B \in \mathcal{B}$. If $B1(\mathcal{B}), B2(\mathcal{B}),$ and $B3(\mathcal{B})$ hold, then there is a ballot $B'$ with $B'_{bal} = b$ and $B'_{qrm} = B'_{vot} = Q$ such that $B1(\mathcal{B} \cup \{B'\}), B2(\mathcal{B} \cup \{B'\}),$ and $B3(\mathcal{B} \cup \{B'\})$ hold.* {#lamport-1998-paxos-thm-2 .statement tag=022D}

Proof of Theorem
Condition $B1(\mathcal{B} \cup \{B'\})$ follows from $B1(\mathcal{B})$, the choice of $B'_{bal}$, and the assumption about $b$. Condition $B2(\mathcal{B} \cup \{B'\})$ follows from $B2(\mathcal{B})$, the choice of $B'_{qrm}$, and the assumption about $Q$. If $MaxVote(b, Q, \mathcal{B})_{bal} = -\infty$ then let $B'_{dec}$ be any decree, else let it equal $MaxVote(b, Q, \mathcal{B})_{dec}$. Condition $B3(\mathcal{B} \cup \{B'\})$ then follows from $B3(\mathcal{B})$.
End Proof of Theorem

### 2.2 The Preliminary Protocol {#lamport-1998-paxos-s2-2 .section tag=0244}

The Paxons derived the preliminary protocol from the requirement that conditions $B1(\mathcal{B}) - B3(\mathcal{B})$ remain true, where $\mathcal{B}$ was the set of all ballots that had been or were being conducted. The definition of the protocol specified how the set $\mathcal{B}$ changed, but the set was never explicitly calculated. The Paxons referred to $\mathcal{B}$ as a quantity observed only by the gods, since it might never be known to any mortal.

Each ballot was initiated by a priest, who chose its number, decree, and quorum. Each priest in the quorum then decided whether or not to vote in the ballot. The rules determining how the initiator chose a ballot’s number, decree, and quorum, and how a priest decided whether or not to vote in a ballot were derived directly from the need to maintain $B1(\mathcal{B}) - B3(\mathcal{B})$.

To maintain $B1$, each ballot had to receive a unique number. By remembering (with notes in his ledger) what ballots he had previously initiated, a priest could easily avoid initiating two different ballots with the same number. To keep different priests from initiating ballots with the same number, the set of possible ballot numbers was partitioned among the priests. While it is not known how this was done, an obvious method would have been to let a ballot number be a pair consisting of an integer and a priest, using a lexicographical ordering, where

$$
(13, \Gamma\rho\alpha\ddot{i}) < (13, \Lambda\nu\sigma\epsilon\ddot{i}) < (15, \Gamma\rho\alpha\ddot{i})
$$

since $\Gamma$ came before $\Lambda$ in the Paxon alphabet. In any case, it is known that every priest had an unbounded set of ballot numbers reserved for his use.

To maintain $B2$, a ballot’s quorum was chosen to contain a $\mu\alpha\delta\zeta\partial\omega\rho\iota\tau\ddot{\iota}\sigma\epsilon\tau$ of priests. Initially, $\mu\alpha\delta\zeta\partial\omega\rho\iota\tau\ddot{\iota}\sigma\epsilon\tau$ just meant a simple majority. Later, it was observed that fat priests were less mobile and spent more time in the Chamber than thin ones, so a $\mu\alpha\delta\zeta\partial\omega\rho\iota\tau\ddot{\iota}\sigma\epsilon\tau$ was taken to mean any set of priests whose total weight was more than half the total weight of all priests, rather than a simple majority of the priests. When a group of thin priests complained that this was unfair, actual weights were replaced with symbolic weights based on a priest’s attendance record. The primary requirement for a $\mu\alpha\delta\zeta\partial\omega\rho\iota\tau\ddot{\iota}\sigma\epsilon\tau$ was that any two sets containing a $\mu\alpha\delta\zeta\partial\omega\rho\iota\tau\ddot{\iota}\sigma\epsilon\tau$ of priests had at least one priest in common. To maintain $B2$, the priest initiating a ballot $B$ chose $B_{qrm}$ to be a majority set.

Condition $B3$ requires that if $MaxVote(b, Q, \mathcal{B})_{dec}$ is not equal to BLANK, then a ballot with number $b$ and quorum $Q$ must have decree $MaxVote(b, Q, \mathcal{B})_{dec}$. If $MaxVote(b, Q, \mathcal{B})_{dec}$ equals BLANK, then the ballot can have any decree. To maintain $B3(\mathcal{B})$, before initiating a new ballot with ballot number $b$ and quorum $Q$, a priest $p$ had to find $MaxVote(b, Q, \mathcal{B})_{dec}$. To do this, $p$ had to find $MaxVote(b, q, \mathcal{B})$ for each priest $q$ in $Q$.

Recall that $MaxVote(b, q, \mathcal{B})$ is the vote with the largest ballot number less than $b$ among all the votes cast by $q$, or $null_q$ if $q$ did not vote in any ballot numbered less than $b$. Priest $p$ obtains $MaxVote(b, q, \mathcal{B})$ from $q$ by an exchange of messages. Therefore, the first two steps in the protocol for conducting a single ballot initiated by $p$ are:$^{10}$

$^{10}$ Priests $p$ and $q$ could be the same. For simplicity, the protocol is described with $p$ sending messages to himself in this case. In reality, a priest could talk to himself without the use of messengers.

(1) Priest p chooses a new ballot number b and sends a NextBallot (b) message to some set of priests. (2) A priest q responds to the receipt of a NextBallot (b) message by sending a

LastVote(b, v) message to p, where v is the vote with the largest ballot number less than b that q has cast, or his null vote null q if q did not vote in any ballot numbered less than b.

Priest q must use notes in the back of his ledger to remember what votes he had previously cast.

When q sends the LastVote(b, v) message, v equals MaxVote(b, q, B). But the set B of ballots changes as new ballots are initiated and votes are cast. Since priest p is going to use v as the value of MaxVote(b, q, B) when choosing a decree, to keep B3(B) true it is necessary that MaxVote(b, q, B) not change after q has sent the LastVote(b, v) message. To keep MaxVote(b, q, B) from changing, q must cast no new votes with ballot numbers between v bal and b. By sending the LastVote(b, v) message, q is promising not to cast any such vote. (To keep this promise, q must record the necessary information in his ledger.)

The next two steps in the balloting protocol (begun in step 1 by priest p) are:

(3) After receiving a LastVote(b, v) message from every priest in some majority set Q, priest p initiates a new ballot with number b, quorum Q, and decree d, where d is chosen to satisfy B3. He then records the ballot in the back of his ledger and sends a BeginBallot (b, d) message to every priest in Q. (4) Upon receipt of the BeginBallot (b, d) message, priest q decides whether or not to cast his vote in ballot number b. (He may not cast the vote if doing so would violate a promise implied by a LastVote(b , v ) message he has sent for some other ballot.) If q decides to vote for ballot number b, then he sends a Voted(b, q) message to p and records the vote in the back of his ledger. The execution of step 3 is considered to add a ballot B to B, where B bal = b, B qrm = Q, B vot = ∅ (no one has yet voted in this ballot), and B dec = d. In step 4, if priest q decides to vote in the ballot, then executing that step is considered to change the set B of ballots by adding q to the set B vot of voters in the ballot B ∈ B.

A priest has the option not to vote in step 4, even if casting a vote would not violate any previous promise. In fact, all the steps in this protocol are optional. For example, a priest q can ignore a NextBallot (b) message instead of executing step 2. Failure to take an action can prevent progress, but it cannot cause any inconsistency because it cannot make B1(B)–B3(B) false. Since the only effect not receiving a message can have is to prevent an action from happening, message loss also cannot cause inconsistency. Thus, the protocol guarantees consistency even if priests leave the chamber or messages are lost.

Receiving multiple copies of a message can cause an action to be repeated. Except in step 3, performing the action a second time has no effect. For example, sending several Voted (b, q) messages in step 4 has the same effect as sending just one. The repetition of step 3 is prevented by using the entry made in the back of the ledger when it is executed. Thus, the consistency condition is maintained even if a messenger delivers the same message several times.

Steps 1–4 describe the complete protocol for initiating a ballot and voting on it.

All that remains is to determine the results of the balloting and announce when a decree has been selected. Recall that a ballot is successful iff every priest in the quorum has voted. The decree of a successful ballot is the one chosen by the Synod. The rest of the protocol is:

(5) If $p$ has received a $Voted(b, q)$ message from every priest $q$ in $Q$ (the quorum for ballot number $b$), then he writes $d$ (the decree of that ballot) in his ledger and sends a $Success(d)$ message to every priest.

(6) Upon receiving a $Success(d)$ message, a priest enters decree $d$ in his ledger.

Steps 1–6 describe how an individual ballot is conducted. The preliminary protocol allows any priest to initiate a new ballot at any time. Each step maintains $B1(\mathcal{B})–B3(\mathcal{B})$, so the entire protocol also maintains these conditions. Since a priest enters a decree in his ledger only if it is the decree of a successful ballot, Theorem 1 implies that the priests’ ledgers are consistent. The protocol does not address the question of progress.

In step 3, if the decree $d$ is determined by condition $B3$, then it is possible that this decree is already written in the ledger of some priest. That priest need not be in the quorum $Q$; he could have left the Chamber. Thus, consistency would not be guaranteed if step 3 allowed any greater freedom in choosing $d$.

### 2.3 The Basic Protocol {#lamport-1998-paxos-s2-3 .section tag=0245}

In the preliminary protocol, a priest must record (i) the number of every ballot he has initiated, (ii) every vote he has cast, and (iii) every $LastVote$ message he has sent. Keeping track of all this information would have been difficult for the busy priests. The Paxons therefore restricted the preliminary protocol to obtain the more practical *basic protocol* in which each priest $p$ had to maintain only the following information in the back of his ledger:

$lastTried[p]$ The number of the last ballot that $p$ tried to initiate, or $-\infty$ if there was none.

$prevVote[p]$ The vote cast by $p$ in the highest-numbered ballot in which he voted, or $-\infty$ if he never voted.

$nextBal[p]$ The largest value of $b$ for which $p$ has sent a $LastVote(b, v)$ message, or $-\infty$ if he has never sent such a message.

Steps 1–6 of the preliminary protocol describe how a single ballot is conducted by its initiator, priest $p$. The preliminary protocol allows $p$ to conduct any number of ballots concurrently. In the basic protocol, he conducts only one ballot at a time—ballot number $lastTried[p]$. After $p$ initiates this ballot, he ignores messages that pertain to any other ballot that he had previously initiated. Priest $p$ keeps all information about the progress of ballot number $lastTried[p]$ on a slip of paper. If he loses that slip of paper, then he stops conducting the ballot.

In the preliminary protocol, each $LastVote(b, v)$ message sent by a priest $q$ represents a promise not to vote in any ballot numbered between $v_{bal}$ and $b$. In the basic protocol, it represents the stronger promise not to cast a new vote in any ballot numbered less than $b$. This stronger promise might prevent him from casting a vote in step 4 of the basic protocol that he would have been allowed to cast in the preliminary protocol. However, since the preliminary protocol always gives $q$ the option of not casting his vote, the basic protocol does not require him to do anything not allowed by the preliminary protocol.

Steps 1–6 of the preliminary protocol become the following six steps for conducting a ballot in the basic protocol. (All information used by p to conduct the ballot, other than lastTried [p], prevVote[p], and nextBal [p], is kept on a slip of paper.)

(1) Priest p chooses a new ballot number b greater than lastTried [p], sets lastTried [p] to b, and sends a NextBallot (b) message to some set of priests. (2) Upon receipt of a NextBallot (b) message from p with b > nextBal [q], priest q sets nextBal[q] to b and sends a LastVote(b, v) message to p, where v equals prevVote[q]. (A NextBallot (b) message is ignored if b ≤ nextBal [q].) (3) After receiving a LastVote(b, v) message from every priest in some majority set Q, where b = lastTried [p], priest p initiates a new ballot with number b, quorum Q, and decree d, where d is chosen to satisfy B3. He then sends a BeginBallot (b, d) message to every priest in Q. (4) Upon receipt of a BeginBallot (b, d) message with b = nextBal[q], priest q casts his vote in ballot number b, sets prevVote[q] to this vote, and sends a Voted (b, q) message to p. (A BeginBallot (b, d) message is ignored if b = nextBal[q].) (5) If p has received a Voted(b, q) message from every priest q in Q (the quorum for ballot number b), where b = lastTried [p], then he writes d (the decree of that ballot) in his ledger and sends a Success(d) message to every priest. (6) Upon receiving a Success(d) message, a priest enters decree d in his ledger.

The basic protocol is a restricted version of the preliminary protocol, meaning that every action allowed by the basic protocol is also allowed by the preliminary protocol. Since the preliminary protocol satisfies the consistency condition, the basic protocol also satisfies that condition. Like the preliminary protocol, the basic protocol does not require that any action ever be taken, so it does not addresses the question of progress.

The derivation of the basic protocol from B1–B3 made it obvious that the consistency condition was satisfied. However, some similarly “obvious” ancient wisdom had turned out to be false, and skeptical citizens demanded a more rigorous proof. Their Paxon mathematicians’ proof that the protocol satisfies the consistency condition is reproduced in the appendix.

### 2.4 The Complete Synod Protocol {#lamport-1998-paxos-s2-4 .section tag=0644}

The basic protocol maintains consistency, but it cannot ensure any progress because it states only what a priest may do; it does not require him to do anything. The complete protocol consists of the same six steps for conducting a ballot as the basic protocol. To help achieve progress, it includes the obvious additional requirement that priests perform steps 2–6 of the protocol as soon as possible. However, to meet the progress condition, it is necessary that some priest be required to perform step 1, which initiates a ballot. The key to the complete protocol lay in determining when a priest should initiate a ballot.

Never initiating a ballot will certainly prevent progress. However, initiating too may ballots can also prevent progress. If b is larger than any other ballot number, then the receipt of a NextBallot (b) message by priest q in step 2 may elicit a promise that prevents him from voting in step 4 for any previously initiated ballot. Thus, the initiation of a new ballot can prevent any previously initiated ballot from succeeding. If new ballots are continually initiated with increasing ballot numbers before the previous ballots have a chance to succeed, then no progress might be made.

Achieving the progress condition requires that new ballots be initiated until one succeeds, but that they not be initiated too frequently. To develop the complete protocol, the Paxons first had to know how long it took messengers to deliver messages and priests to respond. They determined that a messenger who did not leave the Chamber would always deliver a message within 4 minutes, and a priest who remained in the Chamber would always perform an action within 7 minutes of the event that caused the action. 11 Thus, if p and q were in the Chamber when some event caused p to send a message to q, and q responded with a reply to p, then p would receive that reply within 22 minutes if neither messenger left the Chamber. (Priest p would send the message within 7 minutes of the event, q would receive the message within 4 more minutes, he would respond within 7 minutes, and the reply would reach p within 4 more minutes.)

Suppose that only a single priest p was initiating ballots, and that he did so by sending a message to every priest in step 1 of the protocol. If p initiated a ballot when a majority set of priests was in the chamber, then he could expect to execute step 3 within 22 minutes of initiating the ballot, and to execute step 5 within another 22 minutes. If he was unable to execute the steps by those times, then either some priest or messenger left the Chamber after p initiated the ballot, or a larger-numbered ballot had previously been initiated by another priest (before p became the only priest to initiate ballots). To handle the latter possibility, p had to learn about any ballot numbers greater than lastTried [p] used by other priests. This could be done by extending the protocol to require that if a priest q received a NextBallot (b) or a BeginBallot (b, d) message from p with b < nextBal [q], then he sent p a message containing nextBal[q]. Priest p would then initiate a new ballot with a larger ballot number.

Still assuming that p was the only priest initiating ballots, suppose that he were required to initiate a new ballot iff (i) he had not executed step 3 or step 5 within the previous 22 minutes, or (ii) he learned that another priest had initiated a higher-numbered ballot. If the Chamber doors were locked with p and a majority set of priests inside, then a decree would be passed and recorded in the ledgers of all priests in the Chamber within 99 minutes. (It could take 22 minutes for p to start the next ballot, 22 more minutes to learn that another priest had initiated a larger-numbered ballot, then 55 minutes to complete steps 1–6 for a successful ballot.) Thus, the progress condition would be met if only a single priest, who did not leave the chamber, were initiating ballots.

The complete protocol therefore included a procedure for choosing a single priest, called the president, to initiate ballots. In most forms of government, choosing a

11 I am assuming a value of 30 seconds for the δζ∂ιφῐ, the Paxon unit of time. This value is within the range determined from studies of hourglass shards. The reaction time of priests was so long because they had to respond to every message within 7 minutes (14 δζ∂ιφῐ), even if a number of messages arrived simultaneously.

president can be a difficult problem. However, the difficultly arises only because most governments require that there be exactly one president at any time. In the United States, for example, chaos would result if some people thought Bush had been elected president while others thought that Dukakis had, since one of them might decide to sign a bill into law while the other decided to veto it. However, in the Paxon Synod, having multiple presidents could only impede progress; it could not cause inconsistency. For the complete protocol to satisfy the progress condition, the method for choosing the president needed only to satisfy the following presidential selection requirement:

If no one entered or left the Chamber, then after T minutes exactly one priest in the Chamber would consider himself to be the president.

If the presidential selection requirement were met, then the complete protocol would have the property that if a majority set of priests were in the chamber and no one entered or left the Chamber for T + 99 minutes, then at the end of that period every priest in the Chamber would have a decree written in his ledger.

The Paxons chose as president the priest whose name was last in alphabetical order among the names of all priests in the Chamber, though we don’t know exactly how this was done. The presidential selection requirement would have been satisfied if a priest in the Chamber sent a message containing his name to every other priest at least once every T − 11 minutes, and a priest considered himself to be president iff he received no message from a “higher-named” priest for T minutes.

The complete Synod protocol was obtained from the basic protocol by requiring priests to perform steps 2–6 promptly, adding a method for choosing a president who initiated ballots, and requiring the president to initiate ballots at the appropriate times. Many details of the protocol are not known. I have described simple methods for selecting a president and for deciding when the president should initiate a new ballot, but they are undoubtedly not the ones used in Paxos. The rules I have given require the president to keep initiating ballots even after a decree has been chosen, thereby ensuring that priests who have just entered the Chamber learn about the chosen decree. There were obviously better ways to make sure priests learned about the decree after it had been chosen. Also, in the course of selecting a president, each priest probably sent his value of lastTried [p] to the other priests, allowing the president to choose a large enough ballot number on his first try.

The Paxons realized that any protocol to achieve the progress condition must involve measuring the passage of time. 12 The protocols given above for selecting a president and initiating ballots are easily formulated as precise algorithms that set timers and perform actions when time-outs occur—assuming perfectly accurate timers. A closer analysis reveals that such protocols can be made to work with timers having a known bound on their accuracy. The skilled glass blowers of Paxos had no difficulty constructing suitable hourglass timers.

Given the sophistication of Paxon mathematicians, it is widely believed that they must have found an optimal algorithm to satisfy the presidential selection requirement. We can only hope that this algorithm will be discovered in future

12 However, many centuries were to pass before a rigorous proof of this result was given.[Fischer et al. 1985] excavations on Paxos.
