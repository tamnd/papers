---
paper: lamport-1998-paxos
title: The Part-Time Parliament
authors:
  - Leslie Lamport
year: 1998
venue: ACM TOCS
field: systems
section: "4"
section_title: Relevance to Computer Science
tag: "0249"
kind: section
lang: en
source: https://lamport.azurewebsites.net/pubs/lamport-paxos.pdf
pdf_sha256: cd9544e9615bcd417a2c10063671cecca0b28ad4bc5db3f64467a83ecc7028d3
pdf_pages: 23-32
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 6c5b4947f83fec8eaa241d4e2783b4accbed6f6c785c8a8e9d3b2580453170d3
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

### 4.1 The State Machine Approach {#lamport-1998-paxos-s4-1 .section tag=024A}

Although Paxos’s Parliament was destroyed many centuries ago, its protocol is still useful. For example, consider a simple distributed database system that might be used as a name server. A state of the database consists of an assignment of values to names. Copies of the database are maintained by multiple servers. A client program can issue, to any server, a request to read or change the value assigned to a name. There are two kinds of read request: a slow read, which returns the value currently assigned to a name, and a fast read, which is faster but might not reflect a recent change to the database.

There is an obvious correspondence between this database system and the Paxon Parliament:

Parliament Distributed Database legislator ↔ server citizen ↔ client program current law ↔ database state command: read(name, client) update(name, val , client) response: (client, value of name) (client, “ok”) new state: Same as current state Same as current state except value of name changed to val

Fig. 2. State machine for simple database. {#lamport-1998-paxos-fig-2 .figure tag=022E}

A client’s request to change a value is performed by passing a decree. A slow read involves passing a decree, as described in Section 3.3.4. A fast read is performed by reading the server’s current version of the database. The Paxon Parliament protocol provides a distributed, fault-tolerant implementation of the database system,

This method of implementing a distributed database is an instance of the state machine approach, first proposed in [Lamport 1978]. In this approach, one first defines a state machine, which consists of a set of states, a set of commands, a set of responses, and a function that assigns a response/state pair (a pair consisting of a response and a state) to each command/state pair. Intuitively, a state machine executes a command by producing a response and changing its state; the command and the machine’s current state determine its response and its new state. For the distributed database, a state-machine state is just a database state. The statemachine commands and the function specifying the response and new state are described in Figure 2.

In the state-machine approach, a system is implemented with a network of server processes. The servers transform client requests into state machine commands, execute the commands, and transform the state-machine responses into replies to clients. A general algorithm ensures that all servers obtain the same sequence of commands, thereby ensuring that they all produce the same sequence of responses and state changes—assuming they all start from the same initial state. In the database example, a client request to perform a slow read or to change a value is transformed into a state-machine read or update command. That command is executed, and the state-machine response is transformed into a reply to the client, which is sent to him by the server who received his request. Since all servers perform the same sequence of state-machine commands, they all maintain consistent versions of the database. However, at any time, some servers may have earlier versions than others because a state-machine command need not be executed at the same time by all servers. A server uses his current version of the state to reply to a fast read request, without executing a state-machine command.

The functionality of the system is expressed by the state machine, which is just a function from command/state pairs to response/state pairs. Problems of synchronization and fault-tolerance are handled by the general algorithm with which servers obtain the sequence of commands. When designing a new system, only the state machine is new. The servers obtain the state-machine commands by a standard distributed algorithm that has already been proved correct. Functions are much easier to design, and to get right, than distributed algorithms.

The first algorithm for implementing an arbitrary state machine appeared in [Lamport 1978]. Later, algorithms were devised to tolerate up to any fixed number f of arbitrary failures [Lamport 1984]. These algorithms guarantee that, if fewer than f processes fail, then state machine commands are executed within a fixed length of time. The algorithms are thus suitable for applications requiring realtime response. 14 But if more than f failures occur, then different servers may have inconsistent copies of the state machine. Moreover, the inability of two servers to communicate with each other is equivalent to the failure of one of them. For a system to have a low probability of losing consistency, it must use an algorithm with a large value of f , which in turn implies a large cost in redundant hardware, communication bandwidth, and response time.

The Paxon Parliament’s protocol provides another way to implement an arbitrary state machine. The legislators’ law book corresponds to the machine state, and passing a decree corresponds to executing a state-machine command. The resulting algorithm is less robust and less expensive than the earlier algorithms. It does not tolerate arbitrary, malicious failures, nor does it guarantee bounded-time response. However, consistency is maintained despite the (benign) failure of any number of processes and communication paths. The Paxon algorithm is suitable for systems with modest reliability requirements that do not justify the expense of an extremely fault-tolerant, real-time implementation.

If the state machine is executed with an algorithm that guarantees boundedtime response, then time can be made part of the state, and machine actions can be triggered by the passage of time. For example, consider a system for granting ownership of resources. The state can include the time at which a client was granted a resource, and the state machine can automatically execute a command to revoke ownership if the client has held the resource too long.

With the Paxon algorithm, time cannot be made part of the state in such a natural way. If failures occur, it can take arbitrarily long to execute a command (pass a decree), and one command can be executed before (appear earlier in the sequence of decrees than) another command that was issued earlier. However, a state machine can still use real time the same way the Paxon Parliament did. For example, the method described in Section 3.3.3 for deciding who was the current cheese inspector can be used to decide who is the current owner of a resource.

### 4.2 Commit Protocols {#lamport-1998-paxos-s4-2 .section tag=024C}

The Paxon Synod protocol is similar to standard three-phase commit protocols [Bernstein et al. 1987; Skeen 1982]. A Paxon ballot and a three-phase commit protocol both involve the exchange of five messages between a coordinator (the president) and the other quorum members (legislators). A commit protocol chooses one of two values—commit or abort—while the Synod protocol chooses an arbitrary decree. To convert a commit protocol to a Synod protocol, one sends the decree in the initial round of messages. A commit decision means that this decree was passed, and an abort decision means that the “olive-day” decree was passed.

The Synod protocol differs from a converted commit protocol because the decree is not sent until the second phase. This allows the corresponding parliamentary protocol to execute the first phase just once for all decrees, so the exchange of only three messages is needed to pass each individual decree.

The theorems on which the Synod protocol is based are similar to results obtained

14 These algorithms were derived from the military protocols of another Mediterranean state.

by Dwork, Lynch, and Stockmeyer [Dwork et al. 1988]. However, their algorithms execute ballots sequentially in separate rounds, and they seem to be unrelated to the Synod protocol.

Much research has been done in the field since this article was written. The state-machine approach has been surveyed by Schneider [1990]. The recovery protocol by Keidar and Dolev [1996] and the totally-ordered broadcast algorithm of Fekete et al. [1997] are quite similar to the Paxon protocol described here. The author was also apparently unaware that the view management protocol by Oki and Liskov [1988] seems to be equivalent to the Paxon protocol.
Many of the refinements presented in this submission have also appeared in contemporary or subsequent articles. The method of delegation described in Section 3.3.3 is very similar to the leases mechanism of Gray and Cheriton [1989]. The technique of Section 3.3.4 in which the Paxons satisfy the monotonicity condition by using decree numbers is described by Ladin et al. [1992]. The technique of Section 3.3.6 for adding new legislators was also given by Schneider [1990].

Appendix: Proof of Consistency of the Synodic Protocol

A1 The Basic Protocol

The Synod’s basic protocol, described informally in Section 2.3, is stated here using modern algorithmic notation. We begin with the variables that a priest $p$ must maintain. First come the variables that represent information kept in his ledger. (For convenience, the vote $prevVote[p]$ used in Section 2.3 is replaced by its components $prevBal[p]$ and $prevDec[p]$.)

outcome$p$    The decree written in $p$'s ledger, or BLANK if there is nothing written there yet.
lastTried$p$  The number of the last ballot that $p$ tried to begin, or $-\infty$ if there was none.
prevBal$p$    The number of the last ballot in which $p$ voted, or $-\infty$ if he never voted.
prevDec$p$    The decree for which $p$ last voted, or BLANK if $p$ never voted.
nextBal$p$    The number of the last ballot in which $p$ agreed to participate, or $-\infty$ if he has never agreed to participate in a ballot.

Next come variables representing information that priest $p$ could keep on a slip of paper:

status$p$    One of the following values:
    idle      Not conducting or trying to begin a ballot
    trying    Trying to begin ballot number lastTried$p$
    polling   Now conducting ballot number lastTried$p$
    If $p$ has lost his slip of paper, then status$p$ is assumed to equal idle and the values of the following four variables are irrelevant.
prevVotes$p$  The set of votes received in LastVote messages for the current ballot (the one with ballot number lastTried$p$).

quorum[p] If status[p] = polling , then the set of priests forming the quorum of the current ballot; otherwise, meaningless. voters[p] If status[p] = polling , then the set of quorum members from whom p has received Voted messages in the current ballot; otherwise, meaningless. decree[p] If status[p] = polling , then the decree of the current ballot; otherwise, meaningless.

There is also the history variable B, which is the set of ballots that have been started and their progress—namely, which priests have cast votes. (A history variable is one used in the development and proof of an algorithm, but not actually implemented.)

Next come the actions that priest p may take. These actions are assumed to be atomic, meaning that once an action is begun, it must be completed before priest p begins any other action. An action is described by an enabling condition and a list of effects. The enabling condition describes when the action can be performed; actions that receive a message are enabled whenever a messenger has arrived with the appropriate message. The list of effects describes how the action changes the algorithm’s variables and what message, if any, it sends. (Each individual action sends at most one message.)

Recall that ballot numbers were partitioned among the priests. For any ballot number b, the Paxons defined owner(b) to be the priest who was allowed to use that ballot number.

The actions in the basic protocol are allowed actions; the protocol does not require that a priest ever do anything. No attempt at efficiency has been made; the actions allow p to do silly things, such as sending another BeginBallot message to a priest from whom he has already received a LastVote message.

Try New Ballot Always enabled.

– Set lastTried [p] to any ballot number b, greater than its previous value, such that owner(b) = p. – Set status[p] to trying. – Set prevVotes[p] to ∅.

Send NextBallot Message Enabled whenever status[p]=trying.

– Send a NextBallot (lastTried [p]) message to any priest.

Receive NextBallot (b) Message If b ≥ nextBal [p] then

– Set nextBal [p] to b.

Send LastVote Message Enabled whenever nextBal[p] > prevBal [p].

– Send a LastVote(nextBal [p], v) message to priest owner(nextBal [p]), where v pst = p, v bal = prevBal [p], and v dec = prevDec[p].

Receive *LastVote*(b, v) Message
If $b = lastTried[p]$ and $status[p] = trying$, then
    – Set $prevVotes[p]$ to the union of its original value and $\{v\}$.

Start Polling Majority Set $Q$
Enabled when $status[p] = trying$ and $Q \subseteq \{v_{pst} : v \in prevVotes[p]\}$, where $Q$ is a majority set.
    – Set $status[p]$ to *polling*.
    – Set $quorum[p]$ to $Q$.
    – Set $voters[p]$ to $\emptyset$.
    – Set $decree[p]$ to a decree $d$ chosen as follows: Let $v$ be the maximum element of $prevVotes[p]$. If $v_{bal} \neq -\infty$ then $d = v_{dec}$, else $d$ can equal any decree.
    – Set $\mathcal{B}$ to the union of its former value and $\{B\}$, where $B_{dec} = d$, $B_{qrm} = Q$, $B_{vot} = \emptyset$, and $B_{bal} = lastTried[p]$.

Send *BeginBallot* Message
Enabled when $status[p] = polling$.
    – Send a *BeginBallot*(lastTried[p], decree[p]) message to any priest in $quorum[p]$.

Receive *BeginBallot*(b, d) Message
If $b = nextBal[p] > prevBal[p]$ then
    – Set $prevBal[p]$ to $b$.
    – Set $prevDec[p]$ to $d$.
    – If there is a ballot $B$ in $\mathcal{B}$ with $B_{bal} = b$ [there will be], then choose any such $B$ [there will be only one] and let the new value of $\mathcal{B}$ be obtained from its old value by setting $B_{vot}$ equal to the union of its old value and $\{p\}$.

Send *Voted* Message
Enabled whenever $prevBal[p] \neq -\infty$.
    – Send a *Voted*(prevBal[p], p) message to owner(prevBal[p]).

Receive *Voted*(b, q) Message
If $b = lastTried[p]$ and $status[p] = polling$, then
    – Set $voters[p]$ to the union of its old value and $\{q\}$

Succeed
Enabled whenever $status[p] = polling$, $quorum[p] \subseteq voters[p]$, and $outcome[p] =$ BLANK.
    – Set $outcome[p]$ to $decree[p]$.

Send *Success* Message
Enabled whenever $outcome[p] \neq$ BLANK.
    – Send a *Success*(outcome[p]) message to any priest.

Receive *Success*(d) Message
If $outcome[p] =$ BLANK, then

– Set $outcome[p]$ to $d$.

This algorithm is an abstract description of the real protocol performed by Paxon priests. Do the algorithm’s actions accurately model the actions of the real priests? There were three kinds of actions that a priest could perform “atomically”: receiving a message, writing a note or ledger entry, and sending a message. Each of these is represented by a single action of the algorithm, except that Receive actions both receive a message and set a variable. We can pretend that the receipt of a message occurred when a priest acted upon the message; if he left the Chamber before acting upon it, then we can pretend that the message was never received. Since this pretense does not affect the consistency condition, we can infer the consistency of the basic Synod protocol from the consistency of the algorithm.

A2 Proof of Consistency

To prove the consistency condition, it is necessary to show that whenever $outcome[p]$ and $outcome[q]$ are both different from BLANK, they are equal. A rigorous correctness proof requires a complete description of the algorithm. The description given above is almost complete. Missing is a variable $\mathcal{M}$ whose value is the multiset of all messages in transit.$^{15}$ Each Send action adds a message to this multiset and each Receive action removes one. Also needed are actions to represent the loss and duplication of messages, as well as a Forget action that represents a priest losing his slip of paper.

With these additions, we get an algorithm that defines a set of possible behaviors, in which each change of state corresponds to one of the allowed actions. The Paxons proved correctness by finding a predicate $I$ such that

(1) $I$ is true initially.
(2) $I$ implies the desired correctness condition.
(3) Each allowed action leaves $I$ true.

The predicate $I$ was written as a conjunction $I1 \land \ldots \land I7$, where $I1–I5$ were in turn the conjunction of predicates $I1(p)–I5(p)$ for all priests $p$. Although most variables are mentioned in several of the conjuncts, each variable except $status[p]$ is naturally associated with one conjunct, and each conjunct can be thought of as a constraint on its associated variables. The definitions of the individual conjuncts of $I$ are given below, where a list of items marked by $\land$ symbols denotes the conjunction of those items. The variables associated with a conjunct are listed in bracketed comments.

$$
I1(p) \triangleq \quad \text{[Associated variable: } outcome[p]] \\
(outcome[p] \neq \text{BLANK}) \Rightarrow \exists B \in \mathcal{B} : (B_{qrm} \subseteq B_{vot}) \land (B_{dec} = outcome[p])
$$

$$
I2(p) \triangleq \quad \text{[Associated variable: } lastTried[p]] \\
\land owner(lastTried[p]) = p \\
\land \forall B \in \mathcal{B} : (owner(B_{bal}) = p) \Rightarrow \\
\quad \land B_{bal} \leq lastTried[p] \\
\quad \land (status[p] = trying) \Rightarrow (B_{bal} < lastTried[p])
$$

\footnotetext{15}{A multiset is a set that may contain multiple copies of the same element.}

I3(p) $\triangleq$ [Associated variables: prevBal[p], prevDec[p], nextBal[p]]
$\land \ prevBal[p] = MaxVote(\infty, p, \mathcal{B})_{bal}$
$\land \ prevDec[p] = MaxVote(\infty, p, \mathcal{B})_{dec}$
$\land \ nextBal[p] \geq prevBal[p]$

I4(p) $\triangleq$ [Associated variable: prevVotes[p]]
$(status[p] \neq idle) \Rightarrow$

$$
\forall v \in prevVotes[p] : \land v = MaxVote(lastTried[p], v_{pst}, \mathcal{B}) \\
\land nextBal[v_{pst}] \geq lastTried[p]
$$

I5(p) $\triangleq$ [Associated variables: quorum[p], voters[p], decree[p]]
$(status[p] = polling) \Rightarrow$

$$
\land quorum[p] \subseteq \{v_{pst} : v \in prevVotes[p]\} \\
\land \exists B \in \mathcal{B} : \land quorum[p] = B_{qrm} \\
\land decree[p] = B_{dec} \\
\land voters[p] \subseteq B_{vot} \\
\land lastTried[p] = B_{bal}
$$

I6 $\triangleq$ [Associated variable: $\mathcal{B}$]
$\land B1(\mathcal{B}) \land B2(\mathcal{B}) \land B3(\mathcal{B})$
$\land \forall B \in \mathcal{B} : B_{qrm}$ is a majority set

I7 $\triangleq$ [Associated variable: $\mathcal{M}$]
$\land \forall NextBallot(b) \in \mathcal{M} : (b \leq lastTried[owner(b)])$
$\land \forall LastVote(b, v) \in \mathcal{M} : \land v = MaxVote(b, v_{pst}, \mathcal{B})$

$$
\land nextBal[v_{pst}] \geq b
$$

$\land \forall BeginBallot(b, d) \in \mathcal{M} : \exists B \in \mathcal{B} : (B_{bal} = b) \land (B_{dec} = d)$
$\land \forall Voted(b, p) \in \mathcal{M} : \exists B \in \mathcal{B} : (B_{bal} = b) \land (p \in B_{vot})$
$\land \forall Success(d) \in \mathcal{M} : \exists p : outcome[p] = d \neq BLANK$

The Paxons had to prove that $I$ satisfies the three conditions given above. The first condition, that $I$ holds initially, requires checking that each conjunct is true for the initial values of all the variables. While not stated explicitly, these initial values can be inferred from the variables’ descriptions, and checking the first condition is straightforward. The second condition, that $I$ implies consistency, follows from $I1$, the first conjunct of $I6$, and Theorem 1. The hard part was proving the third condition, the invariance of $I$, which meant proving that $I$ is left true by every action. This condition is proved by showing that, for each conjunct of $I$, executing any action when $I$ is true leaves that conjunct true. The proofs are sketched below.

$I1(p)$ $\mathcal{B}$ is changed only by adding a new ballot or adding a new priest to $B_{vot}$ for some $B \in \mathcal{B}$, neither of which can falsify $I1(p)$. The value of $outcome[p]$ is changed only by the Succeed and Receive Success Message actions. The enabling condition and $I5(p)$ imply that $I1(p)$ is left true by the Succeed action. The enabling condition, $I1(p)$, and the last conjunct of $I7$ imply that $I1(p)$ is left true by the Receive Success Message action.

I2(p) This conjunct depends only on lastTried[p], status[p], and $\mathcal{B}$. Only the Try New Ballot action changes lastTried[p], and only that action can set status[p] to trying. Since the action increases lastTried[p] to a value b with owner(b) = p, it leaves I2(p) true. A completely new element is added to $\mathcal{B}$ only by a Start Polling action; the first conjunct of I2(p) and the specification of the action imply that adding this new element does not falsify the second conjunct of I2(p). The only other way $\mathcal{B}$ is changed is by adding a new priest to $B_{vot}$ for some $B \in \mathcal{B}$, which does not affect I2(p).

I3(p) Since votes are never removed from $\mathcal{B}$, the only action that can change MaxVote($\infty$, p, $\mathcal{B}$) is one that adds to $\mathcal{B}$ a vote cast by p. Only a Receive BeginBallot Message action can do that, and only that action changes prevBal[p] and prevDec[p]. The BeginBallot conjunct of I7 implies that this action actually does add a vote to $\mathcal{B}$, and B1($\mathcal{B}$) (the first conjunct of I6) implies that there is only one ballot to which the vote can be added. The enabling condition, the assumption that I3(p) holds before executing the action, and the definition of MaxVote then imply that the action leaves the first two conjuncts of I3(p) true. The third conjunct is left true because prevBal[p] is changed only by setting it to nextBal[p], and nextBal[p] is never decreased.

I4(p) This conjunct depends only upon the values of status[p], prevVotes[p], lastTried[p], nextBal[q] for some priests q, and $\mathcal{B}$. The value of status[p] is changed from idle to not idle only by a Try New Ballot action, which sets prevVotes[p] to $\emptyset$, making I4(p) vacuously true. The only other actions that change prevVotes[p] are the Forget action, which leaves I4(p) true because it sets status[p] to idle, and the Receive LastVote Message action. It follows from the enabling condition and the LastVote conjunct of I7 that the Receive LastVote Message action preserves I4(p). The value of lastTried[p] is changed only by the Try New Ballot action, which leaves I4(p) true because it sets status[p] to trying. The value of nextBal[q] can only increase, which cannot make I4(p) false. Finally, MaxVote(lastTried[p], $v_{pst}$, $\mathcal{B}$) can be changed only if $v_{pst}$ is added to $B_{vot}$ for some $B \in \mathcal{B}$ with $B_{bal} < lastTried[p]$. But $v_{pst}$ is added to $B_{vot}$ (by a Receive BeginBallot Message action) only if $nextBal[v_{pst}] = B_{bal}$, in which case I4(p) implies that $B_{bal} \geq lastTried[p]$.

I5(p) The value of status[p] is set to polling only by the Start Polling action. This action’s enabling condition guarantees that the first conjunct becomes true, and it adds the ballot to $\mathcal{B}$ that makes the second conjunct true. No other action changes quorum[p], decree[p], or lastTried[p] while leaving status[p] equal to polling. The value of prevVotes[p] cannot be changed while status[p] = polling, and $\mathcal{B}$ is changed only by adding new elements or by adding a new priest to $B_{vot}$. The only remaining possibility for falsifying I5(p) is the addition of a new element to voters[p] by the Receive Voted Message action. The Voted conjunct of I7, B1($\mathcal{B}$) (the first conjunct of I6), and the action’s enabling condition imply that the element added to voters[p] is in $B_{vot}$, where B is the ballot whose existence is asserted in I5(p).

I6 Since $B_{bal}$ and $B_{qrm}$ are never changed for any $B \in \mathcal{B}$, the only way B1($\mathcal{B}$), B2($\mathcal{B}$), and the second conjunct of I6 can be falsified is by adding a new ballot to

B, which is done only by the Start Polling Majority Set Q action when status[p] equals trying. It follows from the second conjunct of I2(p) that this action leaves B1(B) true; and the assertion, in the enabling condition, that Q is a majority set implies that the action leaves B2(B) and the second conjunct of I6 true. There are two possible ways of falsifying B3(B): changing MaxVote(B bal , B qrm , B) by adding a new vote to B, and adding a new ballot to B. A new vote is added only by the Receive BeginBallot Message action, and I3(p) implies that the action adds a vote later than any other vote cast by p in B, so it cannot change MaxVote(B bal , B qrm , B) for any B in B. Conjunct I4(p) implies that the new ballot added by the Start Polling action does not falsify B3(B).

I7 I7 can be falsified either by adding a new message to M or by changing the value of another variable on which I7 depends. Since lastTried [p] and nextBal [p] are never decreased, changing them cannot make I7 false. Since outcome[p] is never changed if its value is not blank, changing it cannot falsify I7. Since B is changed only by adding ballots and adding votes, the only change to it that can make I7 false is the addition of a vote by v pst that makes the LastVote(b, v) conjunct false by changing MaxVote(b, v pst , B). This can happen only if v pst votes in a ballot B with B bal < b. But v pst can vote only in ballot number nextBal [v pst ], and the assumption that this conjunct holds initially implies that nextBal [v pst ] ≥ b. Therefore, we need check only that every message that is sent satisfies the condition in the appropriate conjunct of I7.

NextBallot : Follows from the definition of the Send NextBallot Message action and the first conjunct of I2(p).

LastVote: The enabling condition of the Send LastVote Message action and I3(p) imply that MaxVote(nextBal [p], p, B) = MaxVote(∞, p, B), from which it follows that the LastVote message sent by the action satisfies the condition in I7.

BeginBallot : Follows from I5(p) and the definition of the Send BeginBallot Message action.

Voted : Follows from I3(p), the definition of MaxVote, and the definition of the Send Voted Message action.

Success: Follows from the definition of Send Success Message.
