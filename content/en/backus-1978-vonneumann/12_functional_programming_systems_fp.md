---
paper: backus-1978-vonneumann
title: Can Programming Be Liberated from the von Neumann Style? A Functional Style and Its Algebra of Programs
authors:
  - John Backus
year: 1978
venue: Communications of the ACM (Turing Award lecture)
field: languages
section: "11"
section_title: Functional Programming Systems (FP Systems)
tag: "0569"
kind: section
lang: en
source: https://www.cs.cmu.edu/~crary/819-f09/Backus78.pdf
pdf_sha256: 2e412a7986c7fd1bdd060d90d035faa9ecc8a29675f99206c243da90954ca423
pdf_pages: 7-12
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: e13b09cbd803c2fb0b77447e87dc5e462d76f9234dd0614c730416ecaa65aafc
edited: true
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

### 11.1 Introduction {#backus-1978-vonneumann-s11-1 .section tag=056A}

In this section we give an informal description of a class of simple applicative programming systems called functional programming (FP) systems, in which “programs” are simply functions without variables. The description is followed by some examples and by a discussion of various properties of FP systems.

An FP system is founded on the use of a fixed set of combining forms called functional forms. These, plus simple definitions, are the only means of building new functions from existing ones; they use no variables or substitution rules, and they become the operations of an associated algebra of programs. All the functions of an FP system are of one type: they map objects into objects and always take a single argument.

In contrast, a lambda-calculus based system is founded on the use of the lambda expression, with an associated set of substitution rules for variables, for building new functions. The lambda expression (with its substitution rules) is capable of defining all possible computable functions of all possible types and of any number of arguments. This freedom and power has its disadvantages as well as its obvious advantages. It is analogous to the power of unrestricted control statements in conventional languages: with unrestricted freedom comes chaos. If one constantly invents new combining forms to suit the occasion, as one can in the lambda calculus, one will not become familiar with the style or useful properties of the few combining forms that are adequate for all purposes. Just as structured programming eschews many control statements to obtain programs with simpler structure, better properties, and uniform methods for understanding their behavior, so functional programming eschews the lambda expression, substitution, and multiple function types. It thereby achieves programs built with familiar functional forms with known useful properties. These programs are so structured that their behavior can often be understood and proven by mechanical use of algebraic techniques similar to those used in solving high school algebra problems.

Functional forms, unlike most programming constructs, need not be chosen on an ad hoc basis. Since they are the operations of an associated algebra, one chooses only those functional forms that not only provide powerful programming constructs, but that also have attractive algebraic properties: one chooses them to maximize the strength and utility of the algebraic laws that relate them to other functional forms of the system.

In the following description we shall be imprecise in not distinguishing between (a) a function symbol or expression and (b) the function it denotes. We shall indicate the symbols and expressions used to denote functions by example and usage. Section 13 describes a formal extension of FP systems (FFP systems); they can serve to clarify any ambiguities about FP systems.

### 11.2 Description {#backus-1978-vonneumann-s11-2 .section tag=092F}

An FP system comprises the following:
1) a set O of *objects*;
2) a set F of *functions* that map objects into objects;
3) an operation, *application*;
4) a set F of *functional forms*; these are used to combine existing functions, or objects, to form new functions in F;
5) a set D of *definitions* that define some functions in F and assign a name to each.

What follows is an informal description of each of the above entities with examples.

### 11.2.1 Objects, O. {#backus-1978-vonneumann-s11-2-1 .section tag=0930}

An object $x$ is either an atom, a sequence $\langle x_1,\ldots,x_n\rangle$ whose elements $x_i$ are objects, or $\perp$ (“bottom” or “undefined”). Thus the choice of a set A of atoms determines the set of objects. We shall take A to be the set of nonnull strings of capital letters, digits, and special symbols not used by the notation of the FP system. Some of these strings belong to the class of atoms called “numbers.” The atom $\phi$ is used to denote the empty sequence and is the only object which is both an atom and a sequence.

There is one important constraint in the construction of objects: if $x$ is a sequence with $\perp$ as an element, then $x=\perp$. That is, the “sequence constructor” is “$\perp$-preserving.” Thus no proper sequence has $\perp$ as an element.

Examples of objects

$$
\perp \quad 1.5 \quad \phi \quad AB3 \quad \langle AB,1,2.3\rangle
$$

$$
\langle A,\langle B,C\rangle,D\rangle \quad \langle A,\perp\rangle=\perp
$$

### 11.2.2 Application. {#backus-1978-vonneumann-s11-2-2 .section tag=0931}

An FP system has a single operation, application. If $f$ is a function and $x$ is an object, then $f:x$ is an application and denotes the object which is the result of applying $f$ to $x$. $f$ is the operator of the application and $x$ is the operand.

Examples of applications

$$
+: \langle 1,2\rangle = 3 \qquad t1:\langle A,B,C\rangle=\langle B,C\rangle
$$

$$
1:\langle A,B,C\rangle=A \qquad 2:\langle A,B,C\rangle=B
$$

### 11.2.3 Functions, F. {#backus-1978-vonneumann-s11-2-3 .section tag=0932}

All functions $f$ in F map objects into objects and have a bottom-preserving property: $f:\perp=\perp$, for all $f$ in F. Every function in F is either *primitive*, that is, supplied with the system, or it is *defined* (see below), or it is a *functional form* (see below).

It is sometimes useful to distinguish between two cases in which $f:x=\perp$. If the computation of $f:x$ terminates and yields the object $\perp$, we say $f$ is undefined at $x$, that is, $f$ terminates but has no meaningful value at $x$. Otherwise we say $f$ is nonterminating at $x$.

Examples of primitive functions

Our intention is to provide FP systems with widely useful and powerful primitive functions rather than weak ones that could then be used to define useful ones. The following examples define some typical primitive functions, many of which are used in later examples of programs. In the following definitions we use a variant of McCarthy’s conditional expressions [17]; thus we write

$$
p_1\to e_1;\ldots;p_n\to e_n;e_{n+1}
$$

instead of McCarthy’s expression

$$
(p_1\to e_1,\ldots,p_n\to e_n,T\to e_{n+1}).
$$

The following definitions are to hold for all objects $x$, $x_i$, $y$, $y_i$, $z$, $z_i$:

Selector functions

$$
1:x=x=\langle x_1,\ldots,x_n\rangle\to x_1;\perp
$$

and for any positive integer $s$

$$
s:x=x=\langle x_1,\ldots,x_n\rangle\ \&\ n\geq s\to x_s;\perp
$$

Thus, for example, $3:\langle A,B,C\rangle=C$ and $2:\langle A\rangle=\perp$. Note that the function symbols 1, 2, etc. are distinct from the atoms 1, 2, etc.

Tail

$$
tl:x=x=\langle x_1\rangle\to\phi;
$$

$$
x=\langle x_1,\ldots,x_n\rangle\ \&\ n\geq2\to\langle x_2,\ldots,x_n\rangle;\perp
$$

Identity

$$
id:x=x
$$

Atom atom: $x=x$ is an atom $\to T$; $x\ne\bot\to F$; $\bot$

Equals eq: $x=<y,z>\ \&\ y=z\to T$; $x\ne<y,z>\ \&\ y\ne z\to F$; $\bot$

Null null: $x=x\to\phi\to T$; $x\ne\bot\to F$; $\bot$

Reverse reverse: $x=x\to\phi\to\phi$;  
$x=<x_1,\ldots,x_n>\to<x_n,\ldots,x_1>$; $\bot$

Distribute from left; distribute from right distl: $x=x=<y,\phi>\to\phi$;  
$x=<y,<z_1,\ldots,z_n>>\to<<y,z_1>,\ldots,<y,z_n>>$; $\bot$ distr: $x=x=<\phi,y>\to\phi$;  
$x=<<y_1,\ldots,y_n>,z>\to<<y_1,z>,\ldots,<y_n,z>>$; $\bot$

Length length: $x=x=<x_1,\ldots,x_n>\to n$; $x=\phi\to0$; $\bot$

Add, subtract, multiply, and divide

$+:x=x=<y,z>\ \&\ y,z$ are numbers $\to y+z$; $\bot$

$-:x=x=<y,z>\ \&\ y,z$ are numbers $\to y-z$; $\bot$

$\times:x=x=<y,z>\ \&\ y,z$ are numbers $\to y\times z$; $\bot$

$\div:x=x=<y,z>\ \&\ y,z$ are numbers $\to y\div z$; $\bot$

(where $y\ne0=\bot$)

Transpose trans: $x=x=<\phi,\ldots,\phi>\to\phi$;  
$x=<x_1,\ldots,x_n>\to<y_1,\ldots,y_m>$; $\bot$ where

$x_i=<x_{i1},\ldots,x_{im}>$ and

$y_j=<x_{1j},\ldots,x_{nj}>$, $1\le i\le n$, $1\le j\le m$.

And, or, not and: $x=x=<T,T>\to T$;  
$x=<T,F>\vee x=<F,T>\vee x=<F,F>\to F$; $\bot$ etc.

Append left; append right apndl: $x=x=<y,\phi>\to<y>$;  
$x=<y,<z_1,\ldots,z_n>>\to<y,z_1,\ldots,z_n>$; $\bot$ apndr: $x=x=<\phi,z>\to<z>$;  
$x=<<y_1,\ldots,y_n>,z>\to<y_1,\ldots,y_n,z>$; $\bot$

Right selectors; Right tail

1r: $x=x=<x_1,\ldots,x_n>\to x_n$; $\bot$

2r: $x=x=<x_1,\ldots,x_n>\ \&\ n\ge2\to x_{n-1}$; $\bot$ etc.

tlr: $x=x=<x_1>\to\phi$;  
$x=<x_1,\ldots,x_n>\ \&\ n\ge2\to<x_1,\ldots,x_{n-1}>$; $\bot$

Rotate left; rotate right rotl: $x=x\to\phi\to\phi$; $x=<x_1>\to<x_1>$;  
$x=<x_1,\ldots,x_n>\ \&\ n\ge2\to<x_2,\ldots,x_n,x_1>$; $\bot$ etc.

### 11.2.4 Functional forms, F. {#backus-1978-vonneumann-s11-2-4 .section tag=056B}

A functional form is an expression denoting a function; that function depends on the functions or objects which are the parameters of the expression. Thus, for example, if $f$ and $g$ are any functions, then $f\circ g$ is a functional form, the composition of $f$ and $g$, $f$ and $g$ are its parameters, and it denotes the function such that, for any object $x$,

$(f\circ g):x=f:(g:x)$.

Some functional forms may have objects as parameters. For example, for any object $x$, $\bar{x}$ is a functional form, the constant function of $x$, so that for any object $y$

$\bar{x}:y=y=\bot\to\bot;x$.

In particular, $\bot$ is the everywhere-$\bot$ function.

Below we give some functional forms, many of which are used later in this paper. We use $p$, $f$ and $g$ with and without subscripts to denote arbitrary functions; and $x$, $x_1,\ldots,x_n$, $y$ as arbitrary objects. Square brackets [...] are used to indicate the functional form for construction, which denotes a function, whereas pointed brackets $<...>$ denote sequences, which are objects. Parentheses are used both in particular functional forms (e.g. in condition) and generally to indicate grouping.

Composition

$(f\circ g):x=f:(g:x)$

Construction

$[f_1,\ldots,f_n]:x=<f_1:x,\ldots,f_n:x>$  (Recall that since $<\ldots,\bot,\ldots>=\bot$ and all functions are $\bot$-preserving, so is $[f_1,\ldots,f_n]$.)

Condition

$(p\to f,g):x=(p:x)=T\to f:x;\ (p:x)=F\to g:x;\ \bot$

Conditional expressions (used outside of FP systems to describe their functions) and the functional form condition are both identified by “$\to$”. They are quite different although closely related, as shown in the above definitions. But no confusion should arise, since the elements of a conditional expression all denote values, whereas the elements of the functional form condition all denote functions, never values. When no ambiguity arises we omit right-associated parentheses; we write, for example, $p_1\to f_1;p_2\to f_2;g$ for $(p_1\to f_1;(p_2\to f_2;g))$.

Constant (Here $x$ is an object parameter.)

$\bar{x}:y=y=\bot\to\bot;x$

Insert

$/f:x=x=<x_1>\to x_1;x=<x_1,\ldots,x_n>\ \&\ n\ge2$  
$\to f:<x_1,/f:<x_2,\ldots,x_n>>;\bot$

If $f$ has a unique right unit $u_f\ne\bot$, where $f:<x,u_f>\in\{x,\bot\}$ for all objects $x$, then the above definition is extended: $/f:\phi=u_f$. Thus

$/+:<4,5,6> = +:<4, +:<5,/+:<6>>>$

$= +:<4,+:<5,6>> = 15$

$/+:\phi=0$

Apply to all

$\alpha f:x=x=\phi\to\phi;$

$x=<x_1,\ldots,x_n>\to<f:x_1,\ldots,f:x_n>;\bot$

Communications of the ACM

August 1978

Volume 21

Number 8 p_i = distl:<m_i,n'> = <<m_i,n_1'>, ... , <m_i,n_s'>> \tag{1}
for i = 1, ... , r and $n_j'$ is the jth column of $n$ (the jth row of $n'$). Thus $p_i$, a sequence of row and column pairs, corresponds to the i-th product row. The operator $\alpha\alpha IP$, or $\alpha(\alpha IP)$, causes $\alpha IP$ to be applied to each $p_i$, which in turn causes IP to be applied to each row and column pair in each $p_i$. The result of the last step is therefore the sequence of rows comprising the product matrix. If either matrix is not rectangular, or if the length of a row of $m$ differs from that of a column of $n$, or if any element of $m$ or $n$ is not a number, the result is $\perp$.

This program MM does not name its arguments or any intermediate results; contains no variables, no loops, no control statements nor procedure declarations; has no initialization instructions; is not word-at-a-time in nature; is hierarchically constructed from simpler components; uses generally applicable housekeeping forms and operators (e.g., $\alpha f$, distl, distr, trans); is perfectly general; yields $\perp$ whenever its argument is inappropriate in any way; does not constrain the order of evaluation unnecessarily (all applications of IP to row and column pairs can be done in parallel or in any order); and, using algebraic laws (see below), can be transformed into more "efficient" or into more "explanatory" programs (e.g., one that is recursively defined). None of these properties hold for the typical von Neumann matrix multiplication program.

Although it has an unfamiliar and hence puzzling form, the program MM describes the essential operations of matrix multiplication without overdetermining the process or obscuring parts of it, as most programs do; hence many straightforward programs for the operation can be obtained from it by formal transformations. It is an inherently inefficient program for von Neumann computers (with regard to the use of space), but efficient ones can be derived from it and realizations of FP systems can be imagined that could execute MM without the prodigal use of space it implies. Efficiency questions are beyond the scope of this paper; let me suggest only that since the language is so simple and does not dictate any binding of lambda-type variables to data, there may be better opportunities for the system to do some kind of "lazy" evaluation [9, 10] and to control data management more efficiently than is possible in lambda-calculus based systems.

11.4 Remarks About FP Systems

11.4.1 FP systems as programming languages. FP systems are so minimal that some readers may find it difficult to view them as programming languages. Viewed as such, a function $f$ is a program, an object $x$ is the contents of the store, and $f:x$ is the contents of the store after program $f$ is activated with $x$ in the store. The set of definitions is the program library. The primitive functions and the functional forms provided by the system are the basic statements of a particular programming language. Thus, depending on the choice of primitive functions and functional forms, the FP framework provides for a large class of languages with various styles and capabilities. The algebra of programs associated with each of these depends on its particular set of functional forms. The primitive functions, functional forms, and programs given in this paper comprise an effort to develop just one of these possible styles.

11.4.2 Limitations of FP systems. FP systems have a number of limitations. For example, a given FP system is a fixed language; it is not history sensitive: no program can alter the library of programs. It can treat input and output only in the sense that $x$ is an input and $f:x$ is the output. If the set of primitive functions and functional forms is weak, it may not be able to express every computable function.

An FP system cannot compute a program since function expressions are not objects. Nor can one define new functional forms within an FP system. (Both of these limitations are removed in formal functional programming (FFP) systems in which objects "represent" functions.) Thus no FP system can have a function, apply, such that apply:$<x,y> \equiv x:y$ because, on the left, $x$ is an object, and, on the right, $x$ is a function. (Note that we have been careful to keep the set of function symbols and the set of objects distinct: thus $l$ is a function symbol, and $l$ is an object.)

The primary limitation of FP systems is that they are not history sensitive. Therefore they must be extended somehow before they can become practically useful. For discussion of such extensions, see the sections on FFP and AST systems (Sections 13 and 14).

11.4.3 Expressive power of FP systems. Suppose two FP systems, $\mathrm{FP}_1$ and $\mathrm{FP}_2$, both have the same set of objects and the same set of primitive functions, but the set of functional forms of $\mathrm{FP}_1$ properly includes that of $\mathrm{FP}_2$. Suppose also that both systems can express all computable functions on objects. Nevertheless, we can say that $\mathrm{FP}_1$ is more expressive than $\mathrm{FP}_2$, since every function expression in $\mathrm{FP}_2$ can be duplicated in $\mathrm{FP}_1$, but by using a functional form not belonging to $\mathrm{FP}_2$, $\mathrm{FP}_1$ can express some functions more directly and easily than $\mathrm{FP}_2$.

I believe the above observation could be developed into a theory of the expressive power of languages in which a language A would be *more expressive* than language B under the following roughly stated conditions. First, form all possible functions of all types in A by applying all existing functions to objects and to each other in all possible ways until no new function of any type can be formed. (The set of objects is a type; the set of continuous functions [T→U] from type T to type U is a type. If $f \in [T \to U]$ and $t \in T$, then $ft$ in U can be formed by applying $f$ to $t$.) Do the same in language B. Next, compare each type in A to the corresponding type in B. If, for every type, A's type includes B's corresponding type, then A is more expressive than B (or equally expressive). If some type of A’s functions is incomparable to B’s, then A and B are not comparable in expressive power.

11.4.4 Advantages of FP systems. The main reason FP systems are considerably simpler than either conventional languages or lambda-calculus-based languages is that they use only the most elementary fixed naming system (naming a function in a definition) with a simple fixed rule of substituting a function for its name. Thus they avoid the complexities both of the naming systems of conventional languages and of the substitution rules of the lambda calculus. FP systems permit the definition of different naming systems (see Sections 13.3.4 and 14.7) for various purposes. These need not be complex, since many programs can do without them completely. Most importantly, they treat names as functions that can be combined with other functions without special treatment.

FP systems offer an escape from conventional word-at-a-time programming to a degree greater even than APL [12] (the most successful attack on the problem to date within the von Neumann framework) because they provide a more powerful set of functional forms within a unified world of expressions. They offer the opportunity to develop higher level techniques for thinking about, manipulating, and writing programs.
