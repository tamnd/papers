---
paper: backus-1978-vonneumann
title: Can Programming Be Liberated from the von Neumann Style? A Functional Style and Its Algebra of Programs
authors:
  - John Backus
year: 1978
venue: Communications of the ACM (Turing Award lecture)
field: languages
section: "14"
section_title: Applicative State Transition Systems (AST Systems)
tag: "0578"
kind: section
lang: en
source: https://www.cs.cmu.edu/~crary/819-f09/Backus78.pdf
pdf_sha256: 2e412a7986c7fd1bdd060d90d035faa9ecc8a29675f99206c243da90954ca423
pdf_pages: 22-26
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 1e30ad83dfa8ec83d646d7638cf5ab46e09aa052cdb214439d5c0882708d2ee9
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

### 14.1 Introduction {#backus-1978-vonneumann-s14-1 .section tag=0579}

This section sketches a class of systems mentioned earlier as alternatives to von Neumann systems. It must be emphasized again that these applicative state transition systems are put forward not as practical programming systems in their present form, but as examples of a class in which applicative style programming is made available in a history sensitive, but non-von Neumann system. These systems are loosely coupled to states and depend on an underlying applicative system for both their programming language and the description of their state transitions. The underlying applicative system of the AST system described below is an FFP system, but other applicative systems could also be used.

To understand the reasons for the structure of AST systems, it is helpful first to review the basic structure of a von Neumann system, Algol, observe its limitations, and compare it with the structure of AST systems. After that review a minimal AST system is described; a small, top-down, self-protecting system program for file maintenance and running user programs is given, with directions for installing it in the AST system and for running an example user program. The system program uses “name functions” instead of conventional names and the user may do so too. The section concludes with subsections discussing variants of AST systems, their general properties, and naming systems.

### 14.2 The Structure of Algol Compared to That of AST Systems {#backus-1978-vonneumann-s14-2 .section tag=057A}

An Algol program is a sequence of statements, each representing a transformation of the Algol state, which is a complex repository of information about the status of various stacks, pointers, and variable mappings of identifiers onto values, etc. Each statement communicates with this constantly changing state by means of complicated protocols peculiar to itself and even to its different parts (e.g., the protocol associated with the variable $x$ depends on its occurrence on the left or right of an assignment, in a declaration, as a parameter, etc.).

It is as if the Algol state were a complex “store” that communicates with the Algol program through an enormous “cable” of many specialized wires. The complex communications protocols of this cable are fixed and include those for every statement type. The “meaning” of an Algol program must be given in terms of the total effect of a vast number of communications with the state via the cable and its protocols (plus a means for identifying the output and inserting the input into the state). By comparison with this massive cable to the Algol state/store, the cable that is the von Neumann bottleneck of a computer is a simple, elegant concept.

Thus Algol statements are not expressions representing state-to-state functions that are built up by the use of orderly combining forms from simpler state-to-state functions. Instead they are complex messages with context-dependent parts that nibble away at the state. Each part transmits information to and from the state over the cable by its own protocols. There is no provision for applying general functions to the *whole* state and thereby making large changes in it. The possibility of large, powerful transformations of the state $S$ by function application, $S \rightarrow f:S$, is in fact inconceivable in the von Neumann—cable and protocol—context: there could be no assurance that the new state $f:S$ would match the cable and its fixed protocols unless $f$ is restricted to the tiny changes allowed by the cable in the first place.

We want a computing system whose semantics does not depend on a host of baroque protocols for communicating with the state, and we want to be able to make large transformations in the state by the application of general functions. AST systems provide one way of achieving these goals. Their semantics has two protocols for getting information from the state: (1) get from it the definition of a function to be applied, and (2) get the whole state itself. There is one protocol for changing the state: compute the new state by function application. Besides these communications with the state, AST semantics is applicative (i.e. FFP). It does not depend on state changes because the state does not change at all during a computation. Instead, the result of a computation is output *and* a new state. The structure of an AST state is slightly restricted by one of its protocols: It must be possible to identify a definition (i.e. cell) in it. Its structure—it is a sequence—is far simpler than that of the Algol state.

Thus the structure of AST systems avoids the complexity and restrictions of the von Neumann state (with its communications protocols) while achieving greater power and freedom in a radically different and simpler framework.

### 14.3 Structure of an AST System {#backus-1978-vonneumann-s14-3 .section tag=057B}

An AST system is made up of three elements:

1) An *applicative subsystem* (such as an FFP system).
2) A *state* D that is the set of definitions of the applicative subsystem.
3) A set of *transition rules* that describe how inputs are transformed into outputs and how the state D is changed.

The programming language of an AST system is just that of its applicative subsystem. (From here on we shall assume that the latter is an FFP system.) Thus AST systems can use the FP programming style we have discussed. The applicative subsystem cannot change the state D and it does not change during the evaluation of an expression. A new state is computed along with output and replaces the old state when output is issued. (Recall that a set of definitions D is a sequence of cells; a cell name is the name of a defined function and its contents is the defining expression. Here, however, some cells may name data rather than functions; a data name $n$ will be used in $\uparrow n$ (fetch $n$) whereas a function name will be used as an operator itself.)

We give below the transition rules for the elementary AST system we shall use for examples of programs. These are perhaps the simplest of many possible transition rules that could determine the behavior of a great variety of AST systems.

14.3.1 Transition rules for an elementary AST system. When the system receives an input $x$, it forms the application (*SYSTEM:*$x$) and then proceeds to obtain its meaning in the FFP subsystem, using the current state D as the set of definitions. *SYSTEM* is the distinguished name of a function defined in D (i.e. it is the “system program”). Normally the result is a pair

$$
\mu(SYSTEM:x) = <o,d>
$$

where $o$ is the system output that results from input $x$ and $d$ becomes the new state D for the system’s next input. Usually $d$ will be a copy or partly changed copy of the old state. If $\mu(SYSTEM:x)$ is not a pair, the output is an error message and the state remains unchanged.

14.3.2 Transition rules: exception conditions and startup. Once an input has been accepted, our system will not accept another (except $<RESET,x>$, see below) until an output has been issued and the new state, if any, installed. The system will accept the input $<RESET,x>$ at any time. There are two cases: (a) If $SYSTEM$ is defined in the current state D, then the system aborts its current computation without altering D and treats $x$ as a new normal input; (b) if $SYSTEM$ is not defined in D, then $x$ is appended to D as its first element. (This ends the complete description of the transition rules for our elementary AST system.)

If $SYSTEM$ is defined in D it can always prevent any change in its own definition. If it is not defined, an ordinary input $x$ will produce $\mu(SYSTEM:x) = \perp$ and the transition rules yield an error message and an unchanged state; on the other hand, the input $<RESET,<CELL,SYSTEM,s>>$ will define $SYSTEM$ to be $s$.

14.3.3 Program access to the state; the function $\rho DEFS$. Our FFP subsystem is required to have one new primitive function, defs, named $DEFS$ such that for any object $x \neq \perp$,

$$
\text{defs}:x = \rho DEFS:x = D
$$

where D is the current state and set of definitions of the AST system. This function allows programs access to the whole state for any purpose, including the essential one of computing the successor state.

### 14.4 An Example of a System Program {#backus-1978-vonneumann-s14-4 .section tag=057C}

The above description of our elementary AST system, plus the FFP subsystem and the FP primitives and functional forms of earlier sections, specify a complete history-sensitive computing system. Its input and output behavior is limited by its simple transition rules, but otherwise it is a powerful system once it is equipped with a suitable set of definitions. As an example of its use we shall describe a small system program, its installation, and operation.

Our example system program will handle queries and updates for a file it maintains, evaluate FFP expressions, run general user programs that do not damage the file or the state, and allow authorized users to change the set of definitions and the system program itself. All inputs it accepts will be of the form $<key,input>$ where $key$ is a code that determines both the input class (\emph{system-change}, \emph{expression}, \emph{program}, \emph{query}, \emph{update}) and also the identity of the user and his authority to use the system for the given input class. We shall not specify a format for $key$. \emph{Input} is the input itself, of the class given by $key$.

14.4.1 General plan of the system program. The state D of our AST system will contain the definitions of all nonprimitive functions needed for the system program and for users’ programs. (Each definition is in a cell of the sequence D.) In addition, there will be a cell in D named $FILE$ with contents $file$, which the system maintains. We shall give FP definitions of functions and later show how to get them into the system in their FFP form. The transition rules make the input the operand of $SYSTEM$, but our plan is to use name-functions to refer to data, so the first thing we shall do with the input is to create two cells named $KEY$ and $INPUT$ with contents $key$ and $input$ and append these to D. This sequence of cells has one each for $key$, $input$, and $file$; it will be the operand of our main function called subsystem. Subsystem can then obtain $key$ by applying $\uparrow KEY$ to its operand, etc. Thus the definition

Def system $\equiv$ pair $\rightarrow$ subsystem$\circ f; [\overline{NONPAIR}, \text{def}s]$ where

$$
f \equiv \downarrow INPUT \circ [2, \downarrow KEY \circ [1, \text{def}s]]
$$

causes the system to output $NONPAIR$ and leave the state unchanged if the input is not a pair. Otherwise, if it is $<key,input>$, then

$$
f:<key,input> = <<CELL,INPUT,input>,
<CELL,KEY,key>, d_1, ... , d_n>
$$

where $D = <d_1, ... , d_n>$. (We might have constructed a different operand than the one above, one with just three cells, for $key$, $input$, and $file$. We did not do so because real programs, unlike subsystem, would contain many name functions referring to data in the state, and this “standard” construction of the operand would suffice then as well.)

14.4.2 The “subsystem” function. We now give the FP definition of the function subsystem, followed by brief explanations of its six cases and auxiliary functions.

Def subsystem $\equiv$
is-system-change$\uparrow KEY \rightarrow$ [report-change, apply]$\circ [\uparrow INPUT, \text{def}s];$
is-expression$\uparrow KEY \rightarrow [\uparrow INPUT, \text{def}s];$
is-program$\uparrow KEY \rightarrow$ system-check$\circ$apply$\circ [\uparrow INPUT, \text{def}s];$
is-query$\uparrow KEY \rightarrow$ [query-response$\circ [\uparrow INPUT, \uparrow FILE], \text{def}s];$
is-update$\uparrow KEY \rightarrow$
[report-update, $\downarrow FILE \circ$update, def$s$]
\hspace{1cm} $\circ [\uparrow INPUT, \uparrow FILE];$
[report-error$\circ [\uparrow KEY, \uparrow INPUT], \text{def}s$].

This subsystem has five “$p \rightarrow f$” clauses and a final default function, for a total of six classes of inputs; the treatment of each class is given below. Recall that the \emph{operand} of subsystem is a sequence of cells containing $key$, $input$, and $file$ as well as all the defined functions of D, and that subsystem:\emph{operand} = $<output, newstate>$.

Default inputs. In this case the result is given by the last (default) function of the definition when $key$ does not satisfy any of the preceding clauses. The output is report-error: $<key,input>$. The state is unchanged since it is given by defs:\emph{operand} = D. (We leave to the reader’s imagination what the function report-error will generate from its operand.)

Our miniature system program has no provision for giving control to a user’s program to process many inputs, but it would not be difficult to give it that capability while still monitoring the user’s program with the option of taking control back.

### 14.5 Variants of AST Systems {#backus-1978-vonneumann-s14-5 .section tag=057D}

A major extension of the AST systems suggested above would provide combining forms, “system forms,” for building a new AST system from simpler, component AST systems. That is, a system form would take AST systems as parameters and generate a new AST system, just as a functional form takes functions as parameters and generates new functions. These system forms would have properties like those of functional forms and would become the “operations” of a useful “algebra of systems” in much the same way that functional forms are the “operations” of the algebra of programs. However, the problem of finding useful system forms is much more difficult, since they must handle RESETS, match inputs and outputs, and combine history-sensitive systems rather than fixed functions.

Moreover, the usefulness or need for system forms is less clear than that for functional forms. The latter are essential for building a great variety of functions from an initial primitive set, whereas, even without system forms, the facilities for building AST systems are already so rich that one could build virtually any system (with the general input and output properties allowed by the given AST scheme). Perhaps system forms would be useful for building systems with complex input and output arrangements.

### 14.6 Remarks About AST Systems {#backus-1978-vonneumann-s14-6 .section tag=057E}

As I have tried to indicate above, there can be innumerable variations in the ingredients of an AST system—how it operates, how it deals with input and output, how and when it produces new states, and so on. In any case, a number of remarks apply to any reasonable AST system:
a) A state transition occurs once per major computation and can have useful mathematical properties. State transitions are not involved in the tiniest details of a computation as in conventional languages; thus the linguistic von Neumann bottleneck has been eliminated. No complex “cable” or protocols are needed to communicate with the state.
b) Programs are written in an applicative language that can accommodate a great range of changeable parts, parts whose power and flexibility exceed that of any von Neumann language so far. The word-at-a-time style is replaced by an applicative style; there is no division of programming into a world of expressions and a world of statements. Programs can be analyzed and optimized by an algebra of programs.
c) Since the state cannot change during the computation of system:x, there are no side effects. Thus independent applications can be evaluated in parallel.
d) By defining appropriate functions one can, I believe, introduce major new features at any time, using the same framework. Such features must be built into the framework of a von Neumann language. I have in mind such features as: “stores” with a great variety of naming systems, types and type checking, communicating parallel processes, nondeterminacy and Dijkstra’s “guarded command” constructs [8], and improved methods for structured programming.
e) The framework of an AST system comprises the syntax and semantics of the underlying applicative system plus the system framework sketched above. By current standards, this is a tiny framework for a language and is the only fixed part of the system.

### 14.7 Naming Systems in AST and von Neumann Models {#backus-1978-vonneumann-s14-7 .section tag=057F}

In an AST system, naming is accomplished by functions as indicated in Section 13.3.3. Many useful functions for altering and accessing a store can be defined (e.g. push, pop, purge, typed fetch, etc.). All these definitions and their associated naming systems can be introduced without altering the AST framework. Different kinds of “stores” (e.g., with “typed cells”) with individual naming systems can be used in one program. A cell in one store may contain another entire store.

The important point about AST naming systems is that they utilize the functional nature of names (Reynolds’ GEDANKEN [19] also does so to some extent within a von Neumann framework). Thus name functions can be composed and combined with other functions by functional forms. In contrast, functions and names in von Neumann languages are usually disjoint concepts and the function-like nature of names is almost totally concealed and useless, because a) names cannot be applied as functions; b) there are no general means to combine names with other names and functions; c) the objects to which name functions apply (stores) are not accessible as objects.

The failure of von Neumann languages to treat names as functions may be one of their more important weaknesses. In any case, the ability to use names as functions and stores as objects may turn out to be a useful and important programming concept, one which should be thoroughly explored.
