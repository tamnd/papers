---
paper: mccarthy-1960-lisp
title: Recursive Functions of Symbolic Expressions and Their Computation by Machine, Part I
authors:
  - John McCarthy
year: 1960
venue: Communications of the ACM
field: languages
section: "2"
section_title: Functions and Function Definitions
tag: 024F
kind: section
lang: en
source: http://www-formal.stanford.edu/jmc/recursive.pdf
pdf_sha256: 3d981849e59505eff3f14397a177b409f5d978d43d114bdd67c956e74320fc92
pdf_pages: 2-8
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 09c565a51ff0c6a8a2cc23b079b7bf4eda3e98e2537232eb9b4ce20ac116ec2c
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

We shall need a number of mathematical ideas and notations concerning functions in general. Most of the ideas are well known, but the notion of conditional

1 expression is believed to be new , and the use of conditional expressions permits functions to be defined recursively in a new and convenient way.

a. Partial Functions. A partial function is a function that is defined only on part of its domain. Partial functions necessarily arise when functions are defined by computations because for some values of the arguments the computation defining the value of the function may not terminate. However, some of our elementary functions will be defined as partial functions.

b. Propositional Expressions and Predicates. A propositional expression is an expression whose possible values are T (for truth) and F (for falsity). We shall assume that the reader is familiar with the propositional connectives ∧ (“and”), ∨ (“or”), and ¬ (“not”). Typical propositional expressions are:

1 reference Kleene x<y (x < y) ∧ (b = c) x is prime

A predicate is a function whose range consists of the truth values T and F. c. Conditional Expressions. The dependence of truth values on the values of quantities of other kinds is expressed in mathematics by predicates, and the dependence of truth values on other truth values by logical connectives. However, the notations for expressing symbolically the dependence of quantities of other kinds on truth values is inadequate, so that English words and phrases are generally used for expressing these dependences in texts that describe other dependences symbolically. For example, the function |x| is usually defined in words. Conditional expressions are a device for expressing the dependence of quantities on propositional quantities. A conditional expression has the form

(p 1 → e 1 , · · · , p n → e n ) where the p’s are propositional expressions and the e’s are expressions of any kind. It may be read, “If p 1 then e 1 otherwise if p 2 then e 2 , · · · , otherwise if

2 p n then e n ,” or “p 1 yields e 1 , · · · , p n yields e n .”

We now give the rules for determining whether the value of

(p 1 → e 1 , · · · , p n → e n ) is defined, and if so what its value is. Examine the p’s from left to right. If a p whose value is T is encountered before any p whose value is undefined is encountered then the value of the conditional expression is the value of the corresponding e (if this is defined). If any undefined p is encountered before

I sent a proposal for conditional expressions to a CACM forum on what should be included in Algol 60. Because the item was short, the editor demoted it to a letter to the editor, for which CACM subsequently apologized. The notation given here was rejected for Algol 60, because it had been decided that no new mathematical notation should be allowed in Algol 60, and everything new had to be English. The if . . . then . . . else that Algol 60 adopted was suggested by John Backus.

a true $p$, or if all $p$'s are false, or if the $e$ corresponding to the first true $p$ is undefined, then the value of the conditional expression is undefined. We now give examples.

$$
(1 < 2 \rightarrow 4, 1 > 2 \rightarrow 3) = 4
$$

$$
(2 < 1 \rightarrow 4, 2 > 1 \rightarrow 3, 2 > 1 \rightarrow 2) = 3
$$

$$
(2 < 1 \rightarrow 4, T \rightarrow 3) = 3
$$

$$
(2 < 1 \rightarrow \frac{0}{0}, T \rightarrow 3) = 3
$$

$$
(2 < 1 \rightarrow 3, T \rightarrow \frac{0}{0}) \text{ is undefined}
$$

$$
(2 < 1 \rightarrow 3, 4 < 1 \rightarrow 4) \text{ is undefined}
$$

Some of the simplest applications of conditional expressions are in giving such definitions as

$$
|x| = (x < 0 \rightarrow -x, T \rightarrow x)
$$

$$
\delta_{ij} = (i = j \rightarrow 1, T \rightarrow 0)
$$

$$
sgn(x) = (x < 0 \rightarrow -1, x = 0 \rightarrow 0, T \rightarrow 1)
$$

d. *Recursive Function Definitions.* By using conditional expressions we can, without circularity, define functions by formulas in which the defined function occurs. For example, we write

$$
n! = (n = 0 \rightarrow 1, T \rightarrow n \cdot (n - 1)!)
$$

When we use this formula to evaluate 0! we get the answer 1; because of the way in which the value of a conditional expression was defined, the meaningless expression $0 \cdot (0 - 1)!$ does not arise. The evaluation of $2!$ according to this definition proceeds as follows:

$$
\begin{align*}
2! &= (2 = 0 \rightarrow 1, T \rightarrow 2 \cdot (2 - 1)!) \\
   &= 2 \cdot 1! \\
   &= 2 \cdot (1 = 0 \rightarrow 1T \rightarrow \cdot(1 - 1)!)) \\
   &= 2 \cdot 1 \cdot 0! \\
   &= 2 \cdot 1 \cdot (0 = 0 \rightarrow 1, T \rightarrow 0 \cdot (0 - 1)!)) \\
   &= 2 \cdot 1 \cdot 1 \\
   &= 2
\end{align*}
$$

We now give two other applications of recursive function definitions. The greatest common divisor, $gcd(m,n)$, of two positive integers m and n is computed by means of the Euclidean algorithm. This algorithm is expressed by the recursive function definition:

$$
gcd(m, n) = (m > n \rightarrow gcd(n, m), rem(n, m) = 0 \rightarrow m, T \rightarrow gcd(rem(n, m), m))
$$

where $rem(n, m)$ denotes the remainder left when $n$ is divided by $m$.

The Newtonian algorithm for obtaining an approximate square root of a number $a$, starting with an initial approximation $x$ and requiring that an acceptable approximation $y$ satisfy $|y^2 - a| < \epsilon$, may be written as

$$
\text{sqrt}(a, x, \epsilon)
$$

$$
= (|x^2 - a| < \epsilon \rightarrow x, T \rightarrow \text{sqrt } (a, \frac{1}{2}(x + \frac{a}{x}), \epsilon))
$$

The simultaneous recursive definition of several functions is also possible, and we shall use such definitions if they are required.

There is no guarantee that the computation determined by a recursive definition will ever terminate and, for example, an attempt to compute n! from our definition will only succeed if $n$ is a non-negative integer. If the computation does not terminate, the function must be regarded as undefined for the given arguments.

The propositional connectives themselves can be defined by conditional expressions. We write

$$
\begin{align*}
p \land q &\ =\ (p \rightarrow q, T \rightarrow F) \\
p \lor q &\ =\ (p \rightarrow T, T \rightarrow q) \\
\neg p &\ =\ (p \rightarrow F, T \rightarrow T) \\
p \supset q &\ =\ (p \rightarrow q, T \rightarrow T)
\end{align*}
$$

It is readily seen that the right-hand sides of the equations have the correct truth tables. If we consider situations in which $p$ or $q$ may be undefined, the connectives $\land$ and $\lor$ are seen to be noncommutative. For example if $p$ is false and $q$ is undefined, we see that according to the definitions given above $p \land q$ is false, but $q \land p$ is undefined. For our applications this noncommutativity is desirable, since $p \land q$ is computed by first computing $p$, and if $p$ is false $q$ is not computed. If the computation for $p$ does not terminate, we never get around to computing $q$. We shall use propositional connectives in this sense hereafter.

e. *Functions and Forms.* It is usual in mathematics—outside of mathematical logic—to use the word “function” imprecisely and to apply it to forms such as $y^2 + x$. Because we shall later compute with expressions for functions, we need a distinction between functions and forms and a notation for expressing this distinction. This distinction and a notation for describing it, from which we deviate trivially, is given by Church [3].

Let $f$ be an expression that stands for a function of two integer variables. It should make sense to write $f(3, 4)$ and the value of this expression should be determined. The expression $y^2 + x$ does not meet this requirement; $y^2 + x(3, 4)$ is not a conventional notation, and if we attempted to define it we would be uncertain whether its value would turn out to be 13 or 19. Church calls an expression like $y^2 + x$, a form. A form can be converted into a function if we can determine the correspondence between the variables occurring in the form and the ordered list of arguments of the desired function. This is accomplished by Church’s $\lambda$-notation.

If $\mathcal{E}$ is a form in variables $x_1, \cdots, x_n$, then $\lambda((x_1, \cdots, x_n), \mathcal{E})$ will be taken to be the function of $n$ variables whose value is determined by substituting the arguments for the variables $x_1, \cdots, x_n$ in that order in $\mathcal{E}$ and evaluating the resulting expression. For example, $\lambda((x, y), y^2 + x)$ is a function of two variables, and $\lambda((x, y), y^2 + x)(3, 4) = 19$.

The variables occurring in the list of variables of a $\lambda$-expression are dummy or bound, like variables of integration in a definite integral. That is, we may change the names of the bound variables in a function expression without changing the value of the expression, provided that we make the same change for each occurrence of the variable and do not make two variables the same that previously were different. Thus $\lambda((x, y), y^2 + x), \lambda((u, v), v^2 + u)$ and $\lambda((y, x), x^2 + y)$ denote the same function.

We shall frequently use expressions in which some of the variables are bound by $\lambda$'s and others are not. Such an expression may be regarded as defining a function with parameters. The unbound variables are called free variables.

An adequate notation that distinguishes functions from forms allows an unambiguous treatment of functions of functions. It would involve too much of a digression to give examples here, but we shall use functions with functions as arguments later in this report.

Difficulties arise in combining functions described by $\lambda$-expressions, or by any other notation involving variables, because different bound variables may be represented by the same symbol. This is called collision of bound variables. There is a notation involving operators that are called combinators for combining functions without the use of variables. Unfortunately, the combinatorial expressions for interesting combinations of functions tend to be lengthy and unreadable.

f. *Expressions for Recursive Functions.* The $\lambda$-notation is inadequate for naming functions defined recursively. For example, using $\lambda$'s, we can convert the definition

$$
\mathrm{sqrt}(a, x, \epsilon) = (|x^2 - a| < \epsilon \rightarrow x, T \rightarrow \mathrm{sqrt}(a, \frac{1}{2}(x + \frac{a}{x}), \epsilon))
$$

into

$$
\mathrm{sqrt} = \lambda((a, x, \epsilon), (|x^2 - a| < \epsilon \rightarrow x, T \rightarrow \mathrm{sqrt}(a, \frac{1}{2}(x + \frac{a}{x}), \epsilon)))
$$

but the right-hand side cannot serve as an expression for the function because there would be nothing to indicate that the reference to $\mathrm{sqrt}$ within the expression stood for the expression as a whole.

In order to be able to write expressions for recursive functions, we introduce another notation. *label*$(a, \mathcal{E})$ denotes the expression $\mathcal{E}$, provided that occurrences of $a$ within $\mathcal{E}$ are to be interpreted as referring to the expression as a whole. Thus we can write label(sqrt, $\lambda((a, x, \epsilon), (|x^2 - a| < \epsilon \rightarrow x, T \rightarrow \sqrt{a, \frac{1}{2}(x + \frac{a}{x}), \epsilon}))$) as a name for our sqrt function.

The symbol $a$ in label $(a, \mathcal{E})$ is also bound, that is, it may be altered systematically without changing the meaning of the expression. It behaves differently from a variable bound by a $\lambda$, however.
