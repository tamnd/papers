---
paper: hoare-1969-axiomatic
title: An Axiomatic Basis for Computer Programming
authors:
  - C. A. R. Hoare
year: 1969
venue: Communications of the ACM
field: languages
section: "3"
section_title: Program Execution
tag: "0313"
kind: section
lang: en
source: https://www.cs.cmu.edu/~crary/819-f09/Hoare69.pdf
pdf_sha256: f9b85de3537c0f1239cbe767cfd26ad49f2be07f0cc9021a6e46adfffb81dc12
pdf_pages: 2-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 06c2a0a4f841829019619a0f978a48bc899c6150aa8a1d8af663726b876d4f6f
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

As mentioned above, the purpose of this study is to provide a logical basis for proofs of the properties of a program. One of the most important properties of a program is whether or not it carries out its intended function. The intended function of a program, or part of a program, can be specified by making general assertions about the values which the relevant variables will take after execution of the program. These assertions will usually not ascribe particular values to each variable, but will rather specify certain general properties of the values and the relationships holding between them. We use the normal notations of mathematical logic to express these assertions, and the familiar rules of operator precedence have been used wherever possible to improve legibility.

In many cases, the validity of the results of a program (or part of a program) will depend on the values taken by the variables before that program is initiated. These initial preconditions of successful use can be specified by the same type of general assertion as is used to describe the results obtained on termination. To state the required connection between a precondition ($P$), a program ($Q$) and a description of the result of its execution ($R$), we introduce a new notation:

$$
P \{ Q \} R.
$$

This may be interpreted "If the assertion $P$ is true before initiation of a program $Q$, then the assertion $R$ will be true on its completion." If there are no preconditions imposed, we write **true** \{ $Q$ \} $R$.¹

The treatment given below is essentially due to Floyd [8] but is applied to texts rather than flowcharts.

### 3.1. Axiom of Assignment {#hoare-1969-axiomatic-s3-1 .section tag=0314}

Assignment is undoubtedly the most characteristic feature of programming a digital computer, and one that most clearly distinguishes it from other branches of mathematics. It is surprising therefore that the axiom governing our reasoning about assignment is quite as simple as any to be found in elementary logic.

Consider the assignment statement:

$$
x := f
$$

where
$x$ is an identifier for a simple variable;
$f$ is an expression of a programming language without side effects, but possibly containing $x$.

Now any assertion $P(x)$ which is to be true of (the value of) $x$ after the assignment is made must also have been true of (the value of) the expression $f$, taken *before* the assignment is made, i.e. with the old value of $x$. Thus if $P(x)$ is to be true after the assignment, then $P(f)$ must be true before the assignment. This fact may be expressed more formally:

D0  Axiom of Assignment

$$
\vdash P_0 \{ x := f \} P
$$

where
$x$ is a variable identifier;
$f$ is an expression;
$P_0$ is obtained from $P$ by substituting $f$ for all occurrences of $x$.

It may be noticed that D0 is not really an axiom at all, but rather an axiom schema, describing an infinite set of axioms which share a common pattern. This pattern is described in purely syntactic terms, and it is easy to check whether any finite text conforms to the pattern, thereby qualifying as an axiom, which may validly appear in any line of a proof.

¹ If this can be proved in our formal system, we use the familiar logical symbol for theoremhood: $\vdash P \{ Q \} R$

### 3.2. Rules of Consequence {#hoare-1969-axiomatic-s3-2 .section tag=0315}

In addition to axioms, a deductive science requires at least one rule of inference, which permits the deduction of new theorems from one or more axioms or theorems already proved. A rule of inference takes the form “If $\vdash X$ and $\vdash Y$ then $\vdash Z$”, i.e. if assertions of the form $X$ and $Y$ have been proved as theorems, then $Z$ also is thereby proved as a theorem. The simplest example of an inference rule states that if the execution of a program $Q$ ensures the truth of the assertion $R$, then it also ensures the truth of every assertion logically implied by $R$. Also, if $P$ is known to be a precondition for a program $Q$ to produce result $R$, then so is any other assertion which logically implies $P$. These rules may be expressed more formally:

D1  Rules of Consequence
    If $\vdash P\{Q\}R$ and $\vdash R \supset S$ then $\vdash P\{Q\}S$
    If $\vdash P\{Q\}R$ and $\vdash S \supset P$ then $\vdash S\{Q\}R$

### 3.3. Rule of Composition {#hoare-1969-axiomatic-s3-3 .section tag=0316}

A program generally consists of a sequence of statements which are executed one after another. The statements may be separated by a semicolon or equivalent symbol denoting procedural composition: $(Q_1 ; Q_2 ; \cdots ; Q_n )$. In order to avoid the awkwardness of dots, it is possible to deal initially with only two statements $(Q_1 ; Q_2 )$, since longer sequences can be reconstructed by nesting, thus $(Q_1 ; (Q_2 ; (\cdots (Q_{n-1} ; Q_n ) \cdots )))$. The removal of the brackets of this nest may be regarded as convention based on the associativity of the “;-operator”, in the same way as brackets are removed from an arithmetic expression $(t_1 + (t_2 + (\cdots (t_{n-1} + t_n ) \cdots )))$.

The inference rule associated with composition states that if the proven result of the first part of a program is identical with the precondition under which the second part of the program produces its intended result, then the whole program will produce the intended result, provided that the precondition of the first part is satisfied.

In more formal terms:

D2  Rule of Composition
    If $\vdash P\{Q_1\}R_1$ and $\vdash R_1\{Q_2\}R$ then $\vdash P\{ (Q_1 ; Q_2 ) \}R$

### 3.4. Rule of Iteration {#hoare-1969-axiomatic-s3-4 .section tag=0317}

The essential feature of a stored program computer is the ability to execute some portion of program $(S)$ repeatedly until a condition $(B)$ goes false. A simple way of expressing such an iteration is to adapt the Algol 60 while notation:

while $B$ do $S$

In executing this statement, a computer first tests the condition $B$. If this is false, $S$ is omitted, and execution of the loop is complete. Otherwise, $S$ is executed and $B$ is tested again. This action is repeated until $B$ is found to be false. The reasoning which leads to a formulation of an inference rule for iteration is as follows. Suppose $P$ to be an assertion which is always true on completion of $S$, provided that it is also true on initiation. Then obviously $P$ will still be true after any number of iterations of the statement $S$ (even no iterations). Furthermore, it is known that the controlling condition $B$ is false when the iteration finally terminates. A slightly more powerful formulation is possible in light of the fact that $B$ may be assumed to be true on initiation of $S$:

D3  Rule of Iteration
    If $\vdash P \land B\{S\}P$ then $\vdash P\{\text{while } B \text{ do } S\} \neg B \land P$

### 3.5. Example {#hoare-1969-axiomatic-s3-5 .section tag=0318}

The axioms quoted above are sufficient to construct the proof of properties of simple programs, for example, a routine intended to find the quotient $q$ and remainder $r$ obtained on dividing $x$ by $y$. All variables are assumed to range over a set of nonnegative integers conforming to the axioms listed in Table I. For simplicity we use the trivial but inefficient method of successive subtraction. The proposed program is:

$$
((r := x;\ q := 0);\ \text{while}\ y \leq r\ \text{do}\ (r := r - y;\ q := 1 + q))
$$

An important property of this program is that when it terminates, we can recover the numerator $x$ by adding to the remainder $r$ the product of the divisor $y$ and the quotient $q$ (i.e. $x = r + y \times q$). Furthermore, the remainder is less than the divisor. These properties may be expressed formally:

$$
\text{true}\{Q\} \neg y \leq r \land x = r + y \times q
$$

where $Q$ stands for the program displayed above. This expresses a necessary (but not sufficient) condition for the “correctness” of the program.

A formal proof of this theorem is given in Table III. Like all formal proofs, it is excessively tedious, and it would be fairly easy to introduce notational conventions which would significantly shorten it. An even more powerful method of reducing the tedium of formal proofs is to derive general rules for proof construction out of the simple rules accepted as postulates. These general rules would be shown to be valid by demonstrating how every theorem proved with their assistance could equally well (if more tediously) have been proved without. Once a powerful set of supplementary rules has been developed, a “formal proof” reduces to little more than an informal indication of how a formal proof could be constructed.
