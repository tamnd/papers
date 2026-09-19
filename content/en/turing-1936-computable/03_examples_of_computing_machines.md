---
paper: turing-1936-computable
title: On Computable Numbers, with an Application to the Entscheidungsproblem
authors:
  - A. M. Turing
year: 1936
venue: Proceedings of the London Mathematical Society
field: theory
section: "3"
section_title: Examples of computing machines
tag: 04C5
kind: section
lang: en
source: https://doi.org/10.1112/plms/s2-42.1.230
pdf_sha256: a126650c315e998ba96ea8248a60bde0afe60fec3e810acfc2b6c70d3b0e9f36
pdf_pages: 4-36
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 86a483ee931c8c8ade1c40f843d989969a6f36561586bf4780405794e0cd513d
edited: true
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

I. A machine can be constructed to compute the sequence 010101.... The machine is to have the four m-configurations "b", "c", "f", "e" and is capable of printing "0" and "1". The behaviour of the machine is described in the following table in which "R" means "the machine moves so that it scans the square immediately on the right of the one it was scanning previously". Similarly for "L". "E" means "the scanned symbol is erased" and "P" stands for "prints". This table (and all succeeding tables of the same kind) is to be understood to mean that for a configuration described in the first two columns the operations in the third column are carried out successively, and the machine then goes over into the m-configuration described in the last column. When the second column is left blank, it is understood that the behaviour of the third and fourth columns applies for any symbol and for no symbol. The machine starts in the m-configuration b with a blank tape.

Configuration

| m-config. | symbol | operations | final m-config. |
| --- | --- | --- | --- |
| b | None | P0, R | c |
| c | None | R | c |
| e | None | P1, R | f |
| f | None | R | b |

Behaviour

If (contrary to the description in § 1) we allow the letters $L, R$ to appear more than once in the operations column we can simplify the table considerably.

$$
m\text{-config.} \quad symbol \quad operations \quad final\ m\text{-config.}
$$

$$
\begin{cases}
\text{None} & P0 & b \\
b & 0 & R, R, P1 & b \\
b & 1 & R, R, P0 & b
\end{cases}
$$

II. As a slightly more difficult example we can construct a machine to compute the sequence 00101110111101111101111111.... The machine is to be capable of five $m$-configurations, viz. "o", "q", "p", "f", "b" and of printing "a", "x", "0", "1". The first three symbols on the tape will be "a a 0"; the other figures follow on alternate squares. On the intermediate squares we never print anything but "x". These letters serve to "keep the place" for us and are erased when we have finished with them. We also arrange that in the sequence of figures on alternate squares there shall be no blanks.

Configuration

$$
\begin{array}{llll}
m\text{-config.} & symbol & operations & final\ m\text{-config.} \\
b & P_0, R, P_0, R, P0, R, R, P0, L, L & o \\
o & \left\{\begin{array}{ll}
1 & R, Px, L, L, L \\
0 &
\end{array}\right. & o & q \\
q & \left\{\begin{array}{ll}
\text{Any (0 or 1)} & R, R \\
\text{None} & P1, L
\end{array}\right. & q & p \\
p & \left\{\begin{array}{ll}
x & E, R \\
\partial & R \\
\text{None} & L, L
\end{array}\right. & q & f \\
f & \left\{\begin{array}{ll}
\text{Any} & R, R \\
\text{None} & P0, L, L
\end{array}\right. & f & o
\end{array}
$$

To illustrate the working of this machine a table is given below of the first few complete configurations. These complete configurations are described by writing down the sequence of symbols which are on the tape,

Further examples.

(In the explanations the symbol “→” is used to signify “the machine goes into the m-configuration. . . .”)

```text
e(ε, β, α)      f(e₁(ε, β, α), β, α)
c₁(ε, β, α)    E        ε
e(β, α)         c(e(β, α), β, α)
```

From e(ε, β, α) the first α is erased and → ε. If there is no α→β.

From c(β, α) all letters α are erased and → β.

The last example seems somewhat more difficult to interpret than most. Let us suppose that in the list of m-configurations of some machine there appears e(b, x) (= q, say). The table is

```text
c(b, x)        e(c(b, x), b, x)
or             q                e(q, b, x).
```

Or, in greater detail:

```text
q c(q, b, x)
c(q, b, x)       f(c₁(q, b, x), b, x)
c₁(q, b, x)      E q.
```

In this we could replace c₁(q, b, x) by q' and then give the table for f (with the right substitutions) and eventually reach a table in which no m-functions appeared.

```text
pe(ε, β)        f(pe₁(ε, β), ε, θ)
pe₁(ε, β)   { Any    R, R    pe₁(ε, β)
              None   Pβ      ε
l(ε)            L        ε
r(ε)            R        ε
f'(ε, β, α)     f(l(ε), β, α)
f''(ε, β, α)    f(r(ε), β, α)
c(ε, β, α)      f'(c₁(ε), β, α)
c₁(ε) β pe(ε, β)      c(ε, β, α)
```

From pe(ε, β) the machine prints β at the end of the sequence of symbols and → ε.

The machine writes at the end the first symbol marked α and → ε.

q(\mathcal{E}) \begin{cases}
Any & R \\
None & R
\end{cases} q_1(\mathcal{E}) \begin{cases}
Any & R \\
None
\end{cases} q(\mathcal{E}, a) q_1(\mathcal{E}, a) \begin{cases}
a & \mathcal{E} \\
not\ a & L
\end{cases} pe_2(\mathcal{E}, a, \beta) ce_2(\mathcal{B}, a, \beta) ce_3(\mathcal{B}, a, \beta, \gamma) e(\mathcal{E}) \begin{cases}
\emptyset & R \\
Not\ \emptyset & L
\end{cases} e_1(\mathcal{E}) \begin{cases}
Any & R, E, R \\
None
\end{cases} q(\mathcal{E}) \quad q_1(\mathcal{E}) q(\mathcal{E}, a). \quad The\ machine\ finds\ the\ last\ symbol\ of\ form\ a.\ \rightarrow\ \mathcal{E}.

q_1(\mathcal{E})

\mathcal{E} q\left(q_1(\mathcal{E}, a)\right) pe_2(\mathcal{E}, a, \beta). \quad The\ machine\ prints\ a\ \beta\ at\ the\ end.

ce_3(\mathcal{B}, a, \beta, \gamma). \quad The\ machine\ copies\ down\ at\ the\ end\ first\ the\ symbols\ marked\ a,\ then\ those\ marked\ \beta,\ and\ finally\ those\ marked\ \gamma;\ it\ erases\ the\ symbols\ a,\ \beta,\ \gamma.

From\ e(\mathcal{E})\ the\ marks\ are\ erased\ from\ all\ marked\ symbols.\ \rightarrow\ \mathcal{E}.

5. Enumeration of computable sequences.

A computable sequence $\gamma$ is determined by a description of a machine which computes $\gamma$. Thus the sequence 0010111011101111... is determined by the table on p. 234, and, in fact, any computable sequence is capable of being described in terms of such a table.

It will be useful to put these tables into a kind of standard form. In the first place let us suppose that the table is given in the same form as the first table, for example, I on p. 233. That is to say, that the entry in the operations column is always of one of the forms $E : E, R : E, L : Pa : Pa, R : Pa, L : R : L$: or no entry at all. The table can always be put into this form by introducing more $m$-configurations. Now let us give numbers to the $m$-configurations, calling them $q_1, ..., q_R$, as in §1. The initial $m$-configuration is always to be called $q_1$. We also give numbers to the symbols $S_1, ..., S_m$ and, in particular, blank = $S_0$, $0 = S_1$, $1 = S_2$. The lines of the table are now of form

$$
\begin{array}{cccc}
m\text{-config.} & Symbol & Operations & Final m\text{-config.} \\
q_i & S_j & PS_k', L & q_m (N_1) \\
q_i & S_j & PS_k, R & q_m (N_2) \\
q_i & S_j & PS_k & q_m (N_3)
\end{array}
$$

Lines such as

$$
q_i \quad S_j \quad E, R \quad q_m
$$

are to be written as

$$
q_i \quad S_j \quad PS_0, R \quad q_m
$$

and lines such as

$$
q_i \quad S_j \quad R \quad q_m
$$

to be written as

$$
q_i \quad S_j \quad PS_j, R \quad q_m
$$

In this way we reduce each line of the table to a line of one of the forms $(N_1)$, $(N_2)$, $(N_3)$.

From each line of form $(N_1)$ let us form an expression $q_i S_j S_k L q_m$; from each line of form $(N_2)$ we form an expression $q_i S_j S_k R q_m$; and from each line of form $(N_3)$ we form an expression $q_i S_j S_k N q_m$.

Let us write down all expressions so formed from the table for the machine and separate them by semi-colons. In this way we obtain a complete description of the machine. In this description we shall replace $q_i$ by the letter "$D$" followed by the letter "$A$" repeated $i$ times, and $S_j$ by "$D$" followed by "$C$" repeated $j$ times. This new description of the machine may be called the standard description (S.D). It is made up entirely from the letters "$A$", "$C$", "$D$", "$L$", "$R$", "$N$", and from "$;$".

If finally we replace "$A$" by "$1$", "$C$" by "$2$", "$D$" by "$3$", "$L$" by "$4$", "$R$" by "$5$", "$N$" by "$6$", and "$;$" by "$7$" we shall have a description of the machine in the form of an arabic numeral. The integer represented by this numeral may be called a description number (D.N) of the machine. The D.N determine the S.D and the structure of the machine uniquely. The machine whose D.N is $n$ may be described as $\mathcal{M}(n)$.

To each computable sequence there corresponds at least one description number, while to no description number does there correspond more than one computable sequence. The computable sequences and numbers are therefore enumerable.

Let us find a description number for the machine I of §3. When we rename the $m$-configurations its table becomes:

$$
\begin{array}{cccc}
q_1 & S_0 & PS_1, R & q_2 \\
q_2 & S_0 & PS_0, R & q_3 \\
q_3 & S_0 & PS_2, R & q_4 \\
q_4 & S_0 & PS_0, R & q_1
\end{array}
$$

Other tables could be obtained by adding irrelevant lines such as

$$
q_1 \quad S_1 \quad PS_1, R \quad q_2
$$

Our first standard form would be

$$
q_1 S_0 S_1 Rq_2; \quad q_2 S_0 S_0 Rq_3; \quad q_3 S_0 S_2 Rq_4; \quad q_4 S_0 S_0 Rq_1;.
$$

The standard description is

DADDCRDAA;DAADDRDAAA;

$$
DAAADDCCRDAAAA;DAAAADDRDA;
$$

A description number is

31332531173113353111731113322531111731111335317 and so is

3133253117311335311173111332253111173111133531731323253117

A number which is a description number of a circle-free machine will be called a *satisfactory* number. In §8 it is shown that there can be no general process for determining whether a given number is satisfactory or not.

6. *The universal computing machine.*

It is possible to invent a single machine which can be used to compute any computable sequence. If this machine $\mathcal{U}$ is supplied with a tape on the beginning of which is written the S.D of some computing machine $\mathcal{M}$, then $\mathcal{U}$ will compute the same sequence as $\mathcal{M}$. In this section I explain in outline the behaviour of the machine. The next section is devoted to giving the complete table for $\mathcal{U}$.

Let us first suppose that we have a machine $\mathcal{M}'$ which will write down on the $F$-squares the successive complete configurations of $\mathcal{M}$. These might be expressed in the same form as on p. 235, using the second description, (C), with all symbols on one line. Or, better, we could transform this description (as in § 5) by replacing each $m$-configuration by "D" followed by "A" repeated the appropriate number of times, and by replacing each symbol by "D" followed by "C" repeated the appropriate number of times. The numbers of letters "A" and "C" are to agree with the numbers chosen in § 5, so that, in particular, "0" is replaced by "DC", "1" by "DCC", and the blanks by "D". These substitutions are to be made after the complete configurations have been put together, as in (C). Difficulties arise if we do the substitution first. In each complete configuration the blanks would all have to be replaced by "D", so that the complete configuration would not be expressed as a finite sequence of symbols.

If in the description of the machine II of § 3 we replace "o" by "DAA", "e" by "DCCC", "q" by "DAAA", then the sequence (C) becomes:

$$
DA : DCCCDCCCDAADCDDC : DCCCDCCCDAADCDDC : ... (C_1)
$$

(This is the sequence of symbols on $F$-squares.)

It is not difficult to see that if $\mathcal{M}$ can be constructed, then so can $\mathcal{M}'$. The manner of operation of $\mathcal{M}'$ could be made to depend on having the rules of operation ($i.e.$, the S.D) of $\mathcal{M}$ written somewhere within itself ($i.e.$ within $\mathcal{M}'$); each step could be carried out by referring to these rules. We have only to regard the rules as being capable of being taken out and exchanged for others and we have something very akin to the universal machine.

One thing is lacking: at present the machine $\mathcal{M}'$ prints no figures. We may correct this by printing between each successive pair of complete configurations the figures which appear in the new configuration but not in the old. Then (C_1) becomes

$$
DDA : 0 : 0 : DCCCDCCCDAADCDDC : DCCC ... (C_2)
$$

It is not altogether obvious that the $E$-squares leave enough room for the necessary "rough work", but this is, in fact, the case.

The sequences of letters between the colons in expressions such as (C_1) may be used as standard descriptions of the complete configurations. When the letters are replaced by figures, as in § 5, we shall have a numerical description of the complete configuration, which may be called its description number.

7. Detailed description of the universal machine.

A table is given below of the behaviour of this universal machine. The $m$-configurations of which the machine is capable are all those occurring in the first and last columns of the table, together with all those which occur when we write out the unabbreviated tables of those which appear in the table in the form of $m$-functions. *E.g.*, $e(\mathrm{anf})$ appears in the table and is an $m$-function. Its unabbreviated table is (see p. 239)

$$
\begin{array}{lll}
e(\mathrm{anf}) & \left\{\begin{array}{ll}
\varnothing & R \\
\text{not } \varnothing & L
\end{array}\right. & e_1(\mathrm{anf}) \\
e_1(\mathrm{anf}) & \left\{\begin{array}{ll}
\text{Any} & R, E, R \\
\text{None} & \mathrm{anf}
\end{array}\right. & e_1(\mathrm{anf})
\end{array}
$$

Consequently $e_1(\mathrm{anf})$ is an $m$-configuration of $\mathcal{U}$.

When $\mathcal{U}$ is ready to start work the tape running through it bears on it the symbol $\varnothing$ on an $F$-square and again $\varnothing$ on the next $E$-square; after this, on $F$-squares only, comes the S.D of the machine followed by a double colon "::" (a single symbol, on an $F$-square). The S.D consists of a number of instructions, separated by semi-colons.

Each instruction consists of five consecutive parts

(i) "*D*" followed by a sequence of letters "*A*". This describes the relevant $m$-configuration.

(ii) "*D*" followed by a sequence of letters "*C*". This describes the scanned symbol.

(iii) "*D*" followed by another sequence of letters "*C*". This describes the symbol into which the scanned symbol is to be changed.

(iv) "*L*", "*R*", or "*N*", describing whether the machine is to move to left, right, or not at all.

(v) "*D*" followed by a sequence of letters "*A*". This describes the final $m$-configuration.

The machine $\mathcal{U}$ is to be capable of printing "*A*", "*C*", "*D*", "*O*", "*1*", "*u*", "*v*", "*w*", "*x*", "*y*", "*z*". The S.D is formed from ";", "*A*", "*C*", "*D*", "*L*", "*R*", "*N*".

Subsidiary skeleton table.

$$
\begin{array}{llll}
\text{con}(\mathfrak{C}, \alpha) & \left\{\begin{array}{lll}
\text{Not } A & R, R & \text{con}(\mathfrak{C}, \alpha) \\
A & L, Pa, R & \text{con}_1(\mathfrak{C}, \alpha)
\end{array}\right. \\
\text{con}_1(\mathfrak{C}, \alpha) & \left\{\begin{array}{lll}
A & R, Pa, R & \text{con}_1(\mathfrak{C}, \alpha) \\
D & R, Pa, R & \text{con}_2(\mathfrak{C}, \alpha)
\end{array}\right. \\
\text{con}_2(\mathfrak{C}, \alpha) & \left\{\begin{array}{lll}
C & R, Pa, R & \text{con}_2(\mathfrak{C}, \alpha) \\
\text{Not } C & R, R & \mathfrak{C}
\end{array}\right.
\end{array}
$$

con(\mathfrak{C}, \alpha). Starting from an $F$-square, $S$ say, the sequence $C$ of symbols describing a configuration closest on the right of $S$ is marked out with letters $\alpha$. $\rightarrow \mathfrak{C}$.

con(\mathfrak{C}, ). In the final configuration the machine is scanning the square which is four squares to the right of the last square of $C$. $C$ is left unmarked.

The table for $\mathcal{U}$.

$$
\begin{array}{llll}
b & f(b_1, b_1, ::) \\
b_1 & R, R, P::, R, R, PD, R, R, PA & \text{anf} \\
\text{anf} & g(\text{anf}_1, :) \\
\text{anf}_1 & \text{con}(k\text{om}, y) \\
k\text{om} & \left\{\begin{array}{lll}
; & R, Pz, L & \text{con}(k\text{mp}, x) \\
z & L, L & \text{fom} \\
\text{not } z \text{ nor } ; & L & \text{fom}
\end{array}\right. \\
k\text{mp} & \text{cpe}\left(c(k\text{om}, x, y), \text{sim}, x, y\right)
\end{array}
$$

$\text{anf}$. Taking the long view, the last instruction relevant to the last configuration is found. It can be recognised afterwards as the instruction following the last semi-colon marked $z$. $\rightarrow \text{sim}$.

$\text{b}$. The machine prints :DA on the $F$-squares after :: $\rightarrow \text{anf}$.

$\text{anf}$. The machine marks the configuration in the last complete configuration with $y$. $\rightarrow \text{kom}$.

$\text{kom}$. The machine finds the last semi-colon not marked with $z$. It marks this semi-colon with $z$ and the configuration following it with $x$.

$\text{kmp}$. The machine compares the sequences marked $x$ and $y$. It erases all letters $x$ and $y$. $\rightarrow \text{sim}$ if they are alike. Otherwise $\rightarrow \text{kom}$.

ON COMPUTABLE NUMBERS.

```text
sim
f'(sim₁, sim₁, z)
sim₁
con (εim₂, )
sim₂
{
    A
    not A   R, Pu, R, R, R
}
sim₃
{
    not A   L, Py
    A       L, Py, R, R, R
}
e(mf, z)
sim₃
mf
g(mf, :)
mf₁
{
    not A   R, R
    A       L, L, L, L
}
mf₂
{
    C       R, Px, L, L, L
    :
    D       R, Px, L, L, L
}
mf₃
{
    not :   R, Pv, L, L, L
    :
}
mf₄
con(l(l(mf₅)), )
mf₅
{
    Any   R, Pw, R
    None  P:
}
sh
f(sh₁, inst, u)
sh₁
L, L, L
sh₂
{
    D   R, R, R, R
    not D
}
inst
sh₃
{
    C   R, R
    not C
}
sh₄
inst
sh₅
{
    C   R, R
    not C
}
pe₂(inst, 0, :)
inst
pe₂(inst, 1, :)
```

sim. The machine marks out the instructions. That part of the instructions which refers to operations to be carried out is marked with u, and the final m-configuration with y. The letters z are erased.

mf. The last complete configuration is marked out into four sections. The configuration is left unmarked. The symbol directly preceding it is marked with x. The remainder of the complete configuration is divided into two parts, of which the first is marked with v and the last with w. A colon is printed after the whole. → sh.

sh. The instructions (marked u) are examined. If it is found that they involve "Print 0" or "Print 1", then 0: or 1: is printed at the end.

```text
inst      g(l(inst₁), u)
inst₁   a   R, E   inst₁(a)
inst₁(L)   ce₅(ov, v, y, x, u, w)
inst₁(R)   ce₅(ov, v, x, u, y, w)
inst₁(N)   cc₅(ov, v, x, y, u, w)
ov e(anf)
```

inst. The next complete configuration is written down, carrying out the marked instructions. The letters u, v, w, x, y are erased. → anf.

8. Application of the diagonal process.

It may be thought that arguments which prove that the real numbers are not enumerable would also prove that the computable numbers and sequences cannot be enumerable*. It might, for instance, be thought that the limit of a sequence of computable numbers must be computable. This is clearly only true if the sequence of computable numbers is defined by some rule.

Or we might apply the diagonal process. "If the computable sequences are enumerable, let $a_n$ be the n-th computable sequence, and let $\phi_n(m)$ be the m-th figure in $a_n$. Let $\beta$ be the sequence with $1 - \phi_n(n)$ as its n-th figure. Since $\beta$ is computable, there exists a number $K$ such that $1 - \phi_n(n) = \phi_K(n)$ all $n$. Putting $n = K$, we have $1 = 2\phi_K(K)$, i.e. 1 is even. This is impossible. The computable sequences are therefore not enumerable".

The fallacy in this argument lies in the assumption that $\beta$ is computable. It would be true if we could enumerate the computable sequences by finite means, but the problem of enumerating computable sequences is equivalent to the problem of finding out whether a given number is the D.N of a circle-free machine, and we have no general process for doing this in a finite number of steps. In fact, by applying the diagonal process argument correctly, we can show that there cannot be any such general process.

The simplest and most direct proof of this is by showing that, if this general process exists, then there is a machine which computes $\beta$. This proof, although perfectly sound, has the disadvantage that it may leave the reader with a feeling that "there must be something wrong". The proof which I shall give has not this disadvantage, and gives a certain insight into the significance of the idea "circle-free". It depends not on constructing $\beta$, but on constructing $\beta'$, whose n-th figure is $\phi_n(n)$.

* Cf. Hobson, Theory of functions of a real variable (2nd ed., 1921), 87, 88.

We can show further that *there can be no machine* $\mathcal{C}$ *which, when supplied with the S.D of an arbitrary machine* $\mathcal{M}$, *will determine whether* $\mathcal{M}$ *ever prints a given symbol* (*0 say*).

We will first show that, if there is a machine $\mathcal{C}$, then there is a general process for determining whether a given machine $\mathcal{M}$ prints 0 infinitely often. Let $\mathcal{M}_1$ be a machine which prints the same sequence as $\mathcal{M}$, except that in the position where the first 0 printed by $\mathcal{M}$ stands, $\mathcal{M}_1$ prints $\overline{0}$. $\mathcal{M}_2$ is to have the first two symbols 0 replaced by $\overline{0}$, and so on. Thus, if $\mathcal{M}$ were to print

$$
ABA01AAAB0010AB...
$$

then $\mathcal{M}_1$ would print

$$
ABA\overline{0}1AAAB0010AB...
$$

and $\mathcal{M}_2$ would print

$$
ABA\overline{0}1AAAB\overline{0}010AB...
$$

Now let $\mathfrak{F}$ be a machine which, when supplied with the S.D of $\mathcal{M}$, will write down successively the S.D of $\mathcal{M}$, of $\mathcal{M}_1$, of $\mathcal{M}_2$, ... (there is such a machine). We combine $\mathfrak{F}$ with $\mathcal{C}$ and obtain a new machine, $\mathcal{G}$. In the motion of $\mathcal{C}$, first $\mathfrak{F}$ is used to write down the S.D of $\mathcal{M}$, and then $\mathcal{C}$ tests it.: 0: is written if it is found that $\mathcal{M}$ never prints 0; then $\mathfrak{F}$ writes the S.D of $\mathcal{M}_1$, and this is tested, : 0: being printed if and only if $\mathcal{M}_1$ never prints 0, and so on. Now let us test $\mathcal{C}$, with $\mathcal{G}$. If it is found that $\mathcal{G}$ never prints 0, then $\mathcal{M}$ prints 0 infinitely often; if $\mathcal{G}$ prints 0 sometimes, then $\mathcal{M}$ does not print 0 infinitely often.

Similarly there is a general process for determining whether $\mathcal{M}$ prints 1 infinitely often. By a combination of these processes we have a process for determining whether $\mathcal{M}$ prints an infinity of figures, *i.e.* we have a process for determining whether $\mathcal{M}$ is circle-free. There can therefore be no machine $\mathcal{C}$.

The expression "*there is a general process for determining ...*" has been used throughout this section as equivalent to "*there is a machine which will determine ...*". This usage can be justified if and only if we can justify our definition of "*computable*". For each of these "*general process*" problems can be expressed as a problem concerning a general process for determining whether a given integer $n$ has a property $G(n)$ [*e.g.* $G(n)$ might mean "*$n$ is satisfactory*" or "*$n$ is the Gödel representation of a provable formula*"], and this is equivalent to computing a number whose $n$-th figure is 1 if $G(n)$ is true and 0 if it is false.

9. *The extent of the computable numbers.*

No attempt has yet been made to show that the "computable" numbers include all numbers which would naturally be regarded as computable. All arguments which can be given are bound to be, fundamentally, appeals to intuition, and for this reason rather unsatisfactory mathematically. The real question at issue is "What are the possible processes which can be carried out in computing a number?"

The arguments which I shall use are of three kinds.

(a) A direct appeal to intuition.

(b) A proof of the equivalence of two definitions (in case the new definition has a greater intuitive appeal).

(c) Giving examples of large classes of numbers which are computable.

Once it is granted that computable numbers are all "computable", several other propositions of the same character follow. In particular, it follows that, if there is a general process for determining whether a formula of the Hilbert function calculus is provable, then the determination can be carried out by a machine.

I. [Type (a)]. This argument is only an elaboration of the ideas of §1.

Computing is normally done by writing certain symbols on paper. We may suppose this paper is divided into squares like a child's arithmetic book. In elementary arithmetic the two-dimensional character of the paper is sometimes used. But such a use is always avoidable, and I think that it will be agreed that the two-dimensional character of paper is no essential of computation. I assume then that the computation is carried out on one-dimensional paper, i.e. on a tape divided into squares. I shall also suppose that the number of symbols which may be printed is finite. If we were to allow an infinity of symbols, then there would be symbols differing to an arbitrarily small extent†. The effect of this restriction of the number of symbols is not very serious. It is always possible to use sequences of symbols in the place of single symbols. Thus an Arabic numeral such as

† If we regard a symbol as literally printed on a square we may suppose that the square is $0 \leq x \leq 1,\ 0 \leq y \leq 1$. The symbol is defined as a set of points in this square, viz. the set occupied by printer's ink. If these sets are restricted to be measurable, we can define the "distance" between two symbols as the cost of transforming one symbol into the other if the cost of moving unit area of printer's ink unit distance is unity, and there is an infinite supply of ink at $x = 2,\ y = 0$. With this topology the symbols form a conditionally compact space.

17 or 9999999999999999 is normally treated as a single symbol. Similarly in any European language words are treated as single symbols (Chinese, however, attempts to have an enumerable infinity of symbols). The differences from our point of view between the single and compound symbols is that the compound symbols, if they are too lengthy, cannot be observed at one glance. This is in accordance with experience. We cannot tell at a glance whether 9999999999999999 and 9999999999999999 are the same.

The behaviour of the computer at any moment is determined by the symbols which he is observing, and his "state of mind" at that moment. We may suppose that there is a bound $B$ to the number of symbols or squares which the computer can observe at one moment. If he wishes to observe more, he must use successive observations. We will also suppose that the number of states of mind which need be taken into account is finite. The reasons for this are of the same character as those which restrict the number of symbols. If we admitted an infinity of states of mind, some of them will be "arbitrarily close" and will be confused. Again, the restriction is not one which seriously affects computation, since the use of more complicated states of mind can be avoided by writing more symbols on the tape.

Let us imagine the operations performed by the computer to be split up into "simple operations" which are so elementary that it is not easy to imagine them further divided. Every such operation consists of some change of the physical system consisting of the computer and his tape. We know the state of the system if we know the sequence of symbols on the tape, which of these are observed by the computer (possibly with a special order), and the state of mind of the computer. We may suppose that in a simple operation not more than one symbol is altered. Any other changes can be split up into simple changes of this kind. The situation in regard to the squares whose symbols may be altered in this way is the same as in regard to the observed squares. We may, therefore, without loss of generality, assume that the squares whose symbols are changed are always "observed" squares.

Besides these changes of symbols, the simple operations must include changes of distribution of observed squares. The new observed squares must be immediately recognisable by the computer. I think it is reasonable to suppose that they can only be squares whose distance from the closest of the immediately previously observed squares does not exceed a certain fixed amount. Let us say that each of the new observed squares is within $L$ squares of an immediately previously observed square.

In connection with "immediate recognisability", it may be thought that there are other kinds of square which are immediately recognisable. In particular, squares marked by special symbols might be taken as immediately recognisable. Now if these squares are marked only by single symbols there can be only a finite number of them, and we should not upset our theory by adjoining these marked squares to the observed squares. If, on the other hand, they are marked by a sequence of symbols, we cannot regard the process of recognition as a simple process. This is a fundamental point and should be illustrated. In most mathematical papers the equations and theorems are numbered. Normally the numbers do not go beyond (say) 1000. It is, therefore, possible to recognise a theorem at a glance by its number. But if the paper was very long, we might reach Theorem 157767733443477; then, further on in the paper, we might find "... hence (applying Theorem 157767733443477) we have ...". In order to make sure which was the relevant theorem we should have to compare the two numbers figure by figure, possibly ticking the figures off in pencil to make sure of their not being counted twice. If in spite of this it is still thought that there are other "immediately recognisable" squares, it does not upset my contention so long as these squares can be found by some process of which my type of machine is capable. This idea is developed in III below.

The simple operations must therefore include:

(a) Changes of the symbol on one of the observed squares.

(b) Changes of one of the squares observed to another square within $L$ squares of one of the previously observed squares.

It may be that some of these changes necessarily involve a change of state of mind. The most general single operation must therefore be taken to be one of the following:

(A) A possible change (a) of symbol together with a possible change of state of mind.

(B) A possible change (b) of observed squares, together with a possible change of state of mind.

The operation actually performed is determined, as has been suggested on p. 250, by the state of mind of the computer and the observed symbols. In particular, they determine the state of mind of the computer after the operation is carried out.

We may now construct a machine to do the work of this computer. To each state of mind of the computer corresponds an "m-configuration" of the machine. The machine scans $B$ squares corresponding to the $B$ squares observed by the computer. In any move the machine can change a symbol on a scanned square or can change any one of the scanned squares to another square distant not more than $L$ squares from one of the other scanned squares. The move which is done, and the succeeding configuration, are determined by the scanned symbol and the $m$-configuration. The machines just described do not differ very essentially from computing machines as defined in § 2, and corresponding to any machine of this type a computing machine can be constructed to compute the same sequence, that is to say the sequence computed by the computer.

II. [Type (b)].

If the notation of the Hilbert functional calculus† is modified so as to be systematic, and so as to involve only a finite number of symbols, it becomes possible to construct an automatic‡ machine $K$, which will find all the provable formulae of the calculus§.

Now let $\alpha$ be a sequence, and let us denote by $G_\alpha(x)$ the proposition "The $x$-th figure of $\alpha$ is 1", so that — $G_\alpha(x)$ means "The $x$-th figure of $\alpha$ is 0". Suppose further that we can find a set of properties which define the sequence $\alpha$ and which can be expressed in terms of $G_\alpha(x)$ and of the propositional functions $N(x)$ meaning " $x$ is a non-negative integer" and $F(x, y)$ meaning " $y = x + 1$". When we join all these formulae together conjunctively, we shall have a formula, $\mathfrak{U}$ say, which defines $\alpha$. The terms of $\mathfrak{U}$ must include the necessary parts of the Peano axioms, viz.,

$$
(\exists u)\ N(u) \& (x)\left(N(x) \rightarrow (\exists y)\ F(x, y)\right) \& \left(F(x, y) \rightarrow N(y)\right),
$$

which we will abbreviate to $P$.

When we say "$\mathfrak{U}$ defines $\alpha$", we mean that — $\mathfrak{U}$ is not a provable formula, and also that, for each $n$, one of the following formulae (A$_n$) or (B$_n$) is provable.

$$
\mathfrak{U} \& F^{(n)} \rightarrow G_\alpha(u^{(n)}), \tag{A$_n$}$$
$$

\mathfrak{U} \& F^{(n)} \rightarrow \left(-G_\alpha(u^{(n)})\right), \tag{B$_n$},

$$

where $F^{(n)}$ stands for $F(u, u') \& F(u', u'') \& \ldots F(u^{(n-1)}, u^{(n)})$.

† The expression "the functional calculus" is used throughout to mean the *restricted* Hilbert functional calculus.

‡ It is most natural to construct first a choice machine (§ 2) to do this. But it is then easy to construct the required automatic machine. We can suppose that the choices are always choices between two possibilities 0 and 1. Each proof will then be determined by a sequence of choices $i_1, i_2, \ldots, i_n$ ($i_1 = 0$ or 1, $i_2 = 0$ or 1, ..., $i_n = 0$ or 1), and hence the number $2^n + i_1 2^{n-1} + i_2 2^{n-2} + \ldots + i_n$ completely determines the proof. The automatic machine carries out successively proof 1, proof 2, proof 3, ...

§ The author has found a description of such a machine.

‖ The negation sign is written before an expression and not over it.

¶ A sequence of $r$ primes is denoted by $'r$.

I say that $\alpha$ is then a computable sequence: a machine $\mathcal{K}_\alpha$ to compute $\alpha$ can be obtained by a fairly simple modification of $\mathcal{K}$.

We divide the motion of $\mathcal{K}_\alpha$ into sections. The $n$-th section is devoted to finding the $n$-th figure of $\alpha$. After the $(n-1)$-th section is finished a double colon :: is printed after all the symbols, and the succeeding work is done wholly on the squares to the right of this double colon. The first step is to write the letter "A" followed by the formula $(A_n)$ and then "B" followed by $(B_n)$. The machine $\mathcal{K}_\alpha$ then starts to do the work of $\mathcal{K}$, but whenever a provable formula is found, this formula is compared with $(A_n)$ and with $(B_n)$. If it is the same formula as $(A_n)$, then the figure "1" is printed, and the $n$-th section is finished. If it is $(B_n)$, then "0" is printed and the section is finished. If it is different from both, then the work of $\mathcal{K}$ is continued from the point at which it had been abandoned. Sooner or later one of the formulae $(A_n)$ or $(B_n)$ is reached; this follows from our hypotheses about $\alpha$ and $\mathfrak{U}$, and the known nature of $\mathcal{K}$. Hence the $n$-th section will eventually be finished. $\mathcal{K}_\alpha$ is circle-free; $\alpha$ is computable.

It can also be shown that the numbers $\alpha$ definable in this way by the use of axioms include all the computable numbers. This is done by describing computing machines in terms of the function calculus.

It must be remembered that we have attached rather a special meaning to the phrase "$\mathfrak{U}$ defines $\alpha$". The computable numbers do not include all (in the ordinary sense) definable numbers. Let $\delta$ be a sequence whose $n$-th figure is 1 or 0 according as $n$ is or is not satisfactory. It is an immediate consequence of the theorem of §8 that $\delta$ is not computable. It is (so far as we know at present) possible that any assigned number of figures of $\delta$ can be calculated, but not by a uniform process. When sufficiently many figures of $\delta$ have been calculated, an essentially new method is necessary in order to obtain more figures.

III. This may be regarded as a modification of I or as a corollary of II.

We suppose, as in I, that the computation is carried out on a tape; but we avoid introducing the "state of mind" by considering a more physical and definite counterpart of it. It is always possible for the computer to break off from his work, to go away and forget all about it, and later to come back and go on with it. If he does this he must leave a note of instructions (written in some standard form) explaining how the work is to be continued. This note is the counterpart of the "state of mind". We will suppose that the computer works in such a desultory manner that he never does more than one step at a sitting. The note of instructions must enable him to carry out one step and write the next note. Thus the state of progress of the computation at any stage is completely determined by the note of instructions and the symbols on the tape. That is, the state of the system may be described by a single expression (sequence of symbols), consisting of the symbols on the tape followed by $\Delta$ (which we suppose not to appear elsewhere) and then by the note of instructions. This expression may be called the "state formula". We know that the state formula at any given stage is determined by the state formula before the last step was made, and we assume that the relation of these two formulae is expressible in the functional calculus. In other words, we assume that there is an axiom $\mathcal{U}$ which expresses the rules governing the behaviour of the computer, in terms of the relation of the state formula at any stage to the state formula at the preceding stage. If this is so, we can construct a machine to write down the successive state formulae, and hence to compute the required number.

10. Examples of large classes of numbers which are computable.

It will be useful to begin with definitions of a computable function of an integral variable and of a computable variable, etc. There are many equivalent ways of defining a computable function of an integral variable. The simplest is, possibly, as follows. If $\gamma$ is a computable sequence in which 0 appears infinitely† often, and $n$ is an integer, then let us define $\xi(\gamma, n)$ to be the number of figures 1 between the $n$-th and the $(n+1)$-th figure 0 in $\gamma$. Then $\phi(n)$ is computable if, for all $n$ and some $\gamma$,

$$
\phi(n) = \xi(\gamma, n).
$$

An equivalent definition is this. Let $H(x, y)$ mean $\phi(x) = y$. Then, if we can find a contradiction-free axiom $\mathcal{U}_\phi$, such that $\mathcal{U}_\phi \rightarrow P$, and if for each integer $n$ there exists an integer $N$, such that

$$
\mathcal{U}_\phi \& F^{(N)} \rightarrow H(u^{(n)}, u^{(\phi(n))}),
$$

and such that, if $m \neq \phi(n)$, then, for some $N'$,

$$
\mathcal{U}_\phi \& F^{(N')} \rightarrow (-H(u^{(n)}, u^{(m)})),
$$

then $\phi$ may be said to be a computable function.

We cannot define general computable functions of a real variable, since there is no general method of describing a real number, but we can define a computable function of a computable variable. If $n$ is satisfactory, let $\gamma_n$ be the number computed by $\mathcal{M}(n)$, and let

$$
a_n = \tan \left( \pi (\gamma_n - \frac{1}{2}) \right),
$$

† If $\mathcal{M}$ computes $\gamma$, then the problem whether $\mathcal{M}$ prints 0 infinitely often is of the same character as the problem whether $\mathcal{M}$ is circle-free.

unless $\gamma_n = 0$ or $\gamma_n = 1$, in either of which cases $a_n = 0$. Then, as $n$ runs through the satisfactory numbers, $a_n$ runs through the computable numbers†. Now let $\phi(n)$ be a computable function which can be shown to be such that for any satisfactory argument its value is satisfactory‡. Then the function $f$, defined by $f(a_n) = a_{\phi(n)}$, is a computable function and all computable functions of a computable variable are expressible in this form.

Similar definitions may be given of computable functions of several variables, computable-valued functions of an integral variable, etc.

I shall enunciate a number of theorems about computability, but I shall prove only (ii) and a theorem similar to (iii).

(i) A computable function of a computable function of an integral or computable variable is computable.

(ii) Any function of an integral variable defined recursively in terms of computable functions is computable. *I.e.* if $\phi(m, n)$ is computable, and $r$ is some integer, then $\eta(n)$ is computable, where

$$
\eta(0) = r,
$$

$$
\eta(n) = \phi(n, \eta(n-1)).
$$

(iii) If $\phi(m, n)$ is a computable function of two integral variables, then $\phi(n, n)$ is a computable function of $n$.

(iv) If $\phi(n)$ is a computable function whose value is always 0 or 1, then the sequence whose $n$-th figure is $\phi(n)$ is computable.

Dedekind's theorem does not hold in the ordinary form if we replace "real" throughout by "computable". But it holds in the following form:

(v) If $G(\alpha)$ is a propositional function of the computable numbers and

$$(a)\quad (\exists \alpha)(\exists \beta)\left\{G(\alpha) \& \left(-G(\beta)\right)\right\},$$
$$(b)\quad G(\alpha) \& \left(-G(\beta)\right) \rightarrow (\alpha < \beta),$$

and there is a general process for determining the truth value of $G(\alpha)$, then

† A function $a_n$ may be defined in many other ways so as to run through the computable numbers.

‡ Although it is not possible to find a general process for determining whether a given number is satisfactory, it is often possible to show that certain classes of numbers are satisfactory.

there is a computable number $\xi$ such that

$$
G(\alpha) \to \alpha \leq \xi,
$$

$$
-G(\alpha) \to \alpha \geq \xi.
$$

In other words, the theorem holds for any section of the computables such that there is a general process for determining to which class a given number belongs.

Owing to this restriction of Dedekind's theorem, we cannot say that a computable bounded increasing sequence of computable numbers has a computable limit. This may possibly be understood by considering a sequence such as

$$
-1, -\frac{1}{2}, -\frac{1}{4}, -\frac{1}{8}, -\frac{1}{16}, \frac{1}{2}, \ldots
$$

On the other hand, (v) enables us to prove

(vi) If $\alpha$ and $\beta$ are computable and $\alpha < \beta$ and $\phi(\alpha) < 0 < \phi(\beta)$, where $\phi(\alpha)$ is a computable increasing continuous function, then there is a unique computable number $\gamma$, satisfying $\alpha < \gamma < \beta$ and $\phi(\gamma) = 0$.

*Computable convergence.*

We shall say that a sequence $\beta_n$ of computable numbers *converges computably* if there is a computable integral valued function $N(\epsilon)$ of the computable variable $\epsilon$, such that we can show that, if $\epsilon > 0$ and $n > N(\epsilon)$ and $m > N(\epsilon)$, then $|\beta_n - \beta_m| < \epsilon$.

We can then show that

(vii) A power series whose coefficients form a computable sequence of computable numbers is computably convergent at all computable points in the interior of its interval of convergence.

(viii) The limit of a computably convergent sequence is computable.

And with the obvious definition of "uniformly computably convergent":

(ix) The limit of a uniformly computably convergent computable sequence of computable functions is a computable function. Hence

(x) The sum of a power series whose coefficients form a computable sequence is a computable function in the interior of its interval of convergence.

From (viii) and $\pi = 4(1 - \frac{1}{3} + \frac{1}{5} - \ldots)$ we deduce that $\pi$ is computable.

From $e = 1 + 1 + \frac{1}{2!} + \frac{1}{3!} + \ldots$ we deduce that $e$ is computable.

From (vi) we deduce that all real algebraic numbers are computable.
From (vi) and (x) we deduce that the real zeros of the Bessel functions are computable.

Proof of (ii).

Let $H(x, y)$ mean "$\eta(x) = y$", and let $K(x, y, z)$ mean "$\phi(x, y) = z$". $\mathfrak{U}_\phi$ is the axiom for $\phi(x, y)$. We take $\mathfrak{U}_\eta$ to be

$$
\mathfrak{U}_\phi \& P \& \left( F(x, y) \rightarrow G(x, y) \right) \& \left( G(x, y) \& G(y, z) \rightarrow G(x, z) \right)
$$

$$
\& \left( F^{(r)} \rightarrow H(u, u^{(r)}) \right) \& \left( F(v, w) \& H(v, x) \& K(w, x, z) \rightarrow H(w, z) \right)
$$

$$
\& \left[ H(w, z) \& G(z, t) \vee G(t, z) \rightarrow (-H(w, t)) \right].
$$

I shall not give the proof of consistency of $\mathfrak{U}_\eta$. Such a proof may be constructed by the methods used in Hilbert and Bernays, Grundlagen der Mathematik (Berlin, 1934), p. 209 et seq. The consistency is also clear from the meaning.

Suppose that, for some $n, N$, we have shown

$$
\mathfrak{U}_\eta \& F^{(N)} \rightarrow H(u^{(n-1)}, u^{(\eta(n-1))}),
$$

then, for some $M$,

$$
\mathfrak{U}_\phi \& F^{(M)} \rightarrow K(u^{(n)}, u^{(\eta(n-1))}, u^{(\eta(n))}),
$$

$$
\mathfrak{U}_\eta \& F^{(M)} \rightarrow F(u^{(n-1)}, u^{(n)}) \& H(u^{(n-1)}, u^{(\eta(n-1))})
$$

$$
\& K(u^{(n)}, u^{(\eta(n-1))}, u^{(\eta(n))}),
$$

and

$$
\mathfrak{U}_\eta \& F^{(M)} \rightarrow [F(u^{(n-1)}, u^{(n)}) \& H(u^{(n-1)}, u^{(\eta(n-1))})
$$

$$
\& K(u^{(n)}, u^{(\eta(n-1))}, u^{(\eta(n))}) \rightarrow H(u^{(n)}, u^{(\eta(n))})].
$$

Hence

$$
\mathfrak{U}_\eta \& F^{(M)} \rightarrow H(u^{(n)}, u^{(\eta(n))}).
$$

Also

$$
\mathfrak{U}_\eta \& F^{(r)} \rightarrow H(u, u^{(\eta(0))}).
$$

Hence for each $n$ some formula of the form

$$
\mathfrak{U}_\eta \& F^{(M)} \rightarrow H(u^{(n)}, u^{(\eta(n))})
$$

is provable. Also, if $M' \geq M$ and $M' \geq m$ and $m \neq \eta(u)$, then

$$
\mathfrak{U}_\eta \& F^{(M')} \rightarrow G(u^{\eta((n))}, u^{(m)}) \vee G(u^{(m)}, u^{(\eta(n))})
$$

11. Application to the Entscheidungsproblem.

The results of §8 have some important applications. In particular, they can be used to show that the Hilbert Entscheidungsproblem can have no solution. For the present I shall confine myself to proving this particular theorem. For the formulation of this problem I must refer the reader to Hilbert and Ackermann's Grundzüge der Theoretischen Logik (Berlin, 1931), chapter 3.

I propose, therefore, to show that there can be no general process for determining whether a given formula $\mathfrak{U}$ of the functional calculus $\mathbf{K}$ is provable, *i.e.* that there can be no machine which, supplied with any one $\mathfrak{U}$ of these formulae, will eventually say whether $\mathfrak{U}$ is provable.

It should perhaps be remarked that what I shall prove is quite different from the well-known results of Gödel†. Gödel has shown that (in the formalism of Principia Mathematica) there are propositions $\mathfrak{U}$ such that neither $\mathfrak{U}$ nor $-\mathfrak{U}$ is provable. As a consequence of this, it is shown that no proof of consistency of Principia Mathematica (or of $\mathbf{K}$) can be given within that formalism. On the other hand, I shall show that there is no general method which tells whether a given formula $\mathfrak{U}$ is provable in $\mathbf{K}$, or, what comes to the same, whether the system consisting of $\mathbf{K}$ with $-\mathfrak{U}$ adjoined as an extra axiom is consistent.

If the negation of what Gödel has shown had been proved, *i.e.* if, for each $\mathfrak{U}$, either $\mathfrak{U}$ or $-\mathfrak{U}$ is provable, then we should have an immediate solution of the Entscheidungsproblem. For we can invent a machine $\mathcal{K}$ which will prove consecutively all provable formulae. Sooner or later $\mathcal{K}$ will reach either $\mathfrak{U}$ or $-\mathfrak{U}$. If it reaches $\mathfrak{U}$, then we know that $\mathfrak{U}$ is provable. If it reaches $-\mathfrak{U}$, then, since $\mathbf{K}$ is consistent (Hilbert and Ackermann, p. 65), we know that $\mathfrak{U}$ is not provable.

Owing to the absence of integers in $\mathbf{K}$ the proofs appear somewhat lengthy. The underlying ideas are quite straightforward.

Corresponding to each computing machine $\mathcal{M}$ we construct a formula $\mathrm{Un}(\mathcal{M})$ and we show that, if there is a general method for determining whether $\mathrm{Un}(\mathcal{M})$ is provable, then there is a general method for determining whether $\mathcal{M}$ ever prints 0.

The interpretations of the propositional functions involved are as follows:

$R_{S_i}(x, y)$ is to be interpreted as "in the complete configuration $x$ (of $\mathcal{M}$) the symbol on the square $y$ is $S$".

I(x, y) is to be interpreted as "in the complete configuration x the square y is scanned".

K_{q_m}(x) is to be interpreted as "in the complete configuration x the m-configuration is q_m.

F(x, y) is to be interpreted as "y is the immediate successor of x".

Inst \{q_i S_j S_k L q_l\} is to be an abbreviation for

$$(x, y, x', y') \left\{ \left( R_{S_j}(x, y) \& I(x, y) \& K_{q_i}(x) \& F(x, x') \& F(y', y) \right) \right.$$
$$\rightarrow \left( I(x', y') \& R_{S_k}(x', y) \& K_{q_l}(x') \right.$$
$$\left. \& (z) \left[ F(y', z) \vee \left( R_{S_j}(x, z) \rightarrow R_{S_k}(x', z) \right) \right] \right) \}$$

Inst \{q_i S_j S_k R q_l\} and Inst \{q_i S_j S_k N q_l\} are to be abbreviations for other similarly constructed expressions.

Let us put the description of .ll into the first standard form of §6. This description consists of a number of expressions such as "q_i S_j S_k L q_l" (or with R or N substituted for L). Let us form all the corresponding expressions such as Inst \{q_i S_j S_k L q_l\} and take their logical sum. This we call Des(.ll).

The formula Un(.ll) is to be

$$(\exists u) \left[ N(u) \& (x) \left( N(x) \rightarrow (\exists x') F(x, x') \right) \right.$$
$$\left. \& (y, z) \left( F(y, z) \rightarrow N(y) \& N(z) \right) \& (y) R_{S_u}(u, y) \right.$$
$$\left. \& I(u, u) \& K_{q_1}(u) \& Des(.ll) \right]$$
$$\rightarrow (\exists s) (\exists t) [N(s) \& N(t) \& R_{S_1}(s, t)].$$

[N(u) \& ... \& Des(.ll)] may be abbreviated to A(.ll).

When we substitute the meanings suggested on p. 259–60 we find that Un(.ll) has the interpretation "in some complete configuration of .M, S_1 (i.e. 0) appears on the tape". Corresponding to this I prove that

(a) If S_1 appears on the tape in some complete configuration of .ll, then Un(.ll) is provable.

(b) If Un(.ll) is provable, then S_1 appears on the tape in some complete configuration of .ll.

When this has been done, the remainder of the theorem is trivial.

1936.] ON COMPUTABLE NUMBERS.

Lemma 1. *If S₁ appears on the tape in some complete configuration of $\mathcal{M}$, then Un($\mathcal{M}$) is provable.* {#turing-1936-computable-lem-1 .statement tag=0954}

We have to show how to prove Un($\mathcal{M}$). Let us suppose that in the n-th complete configuration the sequence of symbols on the tape is $S_{r(n,0)}, S_{r(n,1)}, \ldots, S_{r(n,n)}$, followed by nothing but blanks, and that the scanned symbol is the i(n)-th, and that the m-configuration is $q_{k(n)}$. Then we may form the proposition

$$
R_{S_{r(n,0)}}(u^{(n)}, u) \& R_{S_{r(n,1)}}(u^{(n)}, u') \& \ldots \& R_{S_{r(n,n)}}(u^{(n)}, u^{(n)})
$$

$$
\& I(u^{(n)}, u^{(i(n))}) \& K_{q_{k(n)}}(u^{(n)})
$$

$$
\& (y) F((y, u') \vee F(u, y) \vee F(u', y) \vee \ldots \vee F(u^{(n-1)}, y) \vee R_{S_v}(u^{(n)}, y)),
$$

which we may abbreviate to $CC_n$.

As before, $F(u, u') \& F(u', u'') \& \ldots \& F(u^{(r-1)}, u^{(r)})$ is abbreviated to $F^{(r)}$.

I shall show that all formulae of the form $A(.ll) \& F^{(n)} \rightarrow CC_n$ (abbreviated to $CF_n$) are provable. The meaning of $CF_n$ is "The n-th complete configuration of $\mathcal{M}$ is so and so", where "so and so" stands for the actual n-th complete configuration of .ll. That $CF_n$ should be provable is therefore to be expected.

$CF_0$ is certainly provable, for in the complete configuration the symbols are all blanks, the m-configuration is $q_1$, and the scanned square is $u$, *i.e.* $CC_0$ is

$$
(y) R_{S_v}(u, y) \& I(u, u) \& K_{q_1}(u).
$$

$A(\mathcal{M}) \rightarrow CC_0$ is then trivial.

We next show that $CF_n \rightarrow CF_{n+1}$ is provable for each $n$. There are three cases to consider, according as in the move from the n-th to the (n+1)-th configuration the machine moves to left or to right or remains stationary. We suppose that the first case applies, *i.e.* the machine moves to the left. A similar argument applies in the other cases. If $r(n, i(n)) = a, r(n+1, i(n+1)) = c, k(i(n)) = b,$ and $k(i(n+1)) = d$, then Des ($\mathcal{M}$) must include Inst $\{ q_a S_b S_d L q_c \}$ as one of its terms, *i.e.*

$$
\text{Des } (\mathcal{M}) \rightarrow \text{Inst } \{ q_a S_b S_d L q_c \}.
$$

Hence $A(.ll) \& F^{(n+1)} \rightarrow \text{Inst } \{ q_a S_b S_d L q_c \} \& F^{(n+1)}$.

But $\text{Inst}\{ q_a S_b S_d L q_c \} \& F^{(n+1)} \rightarrow (CC_n \rightarrow CC_{n+1})$ is provable, and so therefore is

$$
A(.ll) \& F^{(n+1)} \rightarrow (CC_n \rightarrow CC_{n+1})
$$

and $(A(\mathcal{M}) \& F^{(n)} \to CC_n) \to (A(\mathcal{M}) \& F^{(n+1)} \to CC_{n+1}),$ i.e.

$$CF_n \to CF_{n+1}.$$

$CF_n$ is provable for each $n$. Now it is the assumption of this lemma that $S_1$ appears somewhere, in some complete configuration, in the sequence of symbols printed by $\mathcal{M}$; that is, for some integers $N, K, CC_N$ has $R_{S_1}(u^{(N)}, u^{(K)})$ as one of its terms, and therefore $CC_N \to R_{S_1}(u^{(N)}, u^{(K)})$ is provable. We have then

$$CC_N \to R_{S_1}(u^{(N)}, u^{(K)})$$

and

$$A(\mathcal{M}) \& F^{(N)} \to CC^N.$$

We also have

$$(\exists u) A(.ll.) \to (\exists u)(\exists u') ... (\exists u^{(N')})(A(.ll.) \& F^{(N)}),$$

where $N' = \max(N, K)$. And so

$$(\exists u) A(.ll.) \to (\exists u)(\exists u') ... (\exists u^{(N')}) R_{S_1}(u^{(N)}, u^{(K)}),$$

$$(\exists u) A(.ll.) \to (\exists u^{(N)})(\exists u^{(K)}) R_{S_1}(u^{(N)}, u^{(K)}),$$

$$(\exists u) A(.ll.) \to (\exists s)(\exists t) R_{S_1}(s, t),$$

i.e. Un(.ll.) is provable.

This completes the proof of Lemma 1.

Lemma 2. *If Un(.ll.) is provable, then S₁ appears on the tape in some complete configuration of .ll.* {#turing-1936-computable-lem-2 .statement tag=0955}

If we substitute any propositional functions for function variables in a provable formula, we obtain a true proposition. In particular, if we substitute the meanings tabulated on pp. 259–260 in Un(.ll.), we obtain a true proposition with the meaning "*S₁ appears somewhere on the tape in some complete configuration of .ll*".

We are now in a position to show that the Entscheidungsproblem cannot be solved. Let us suppose the contrary. Then there is a general (mechanical) process for determining whether Un(.ll.) is provable. By Lemmas 1 and 2, this implies that there is a process for determining whether $\mathcal{M}$ ever prints 0, and this is impossible, by §8. Hence the Entscheidungsproblem cannot be solved.

In view of the large number of particular cases of solutions of the Entscheidungsproblem for formulae with restricted systems of quantors, it is interesting to express Un(\mathcal{M}) in a form in which all quantors are at the beginning. Un(\mathcal{M}) is, in fact, expressible in the form

$$(u)(\exists x)(w)(\exists u_1)\ldots(\exists u_n)\mathcal{B},$$

where \mathcal{B} contains no quantors, and $n = 6$. By unimportant modifications we can obtain a formula, with all essential properties of Un(\mathcal{M}), which is of form (I) with $n = 5$.

Added 28 August, 1936.

APPENDIX.

Computability and effective calculability

The theorem that all effectively calculable ($\lambda$-definable) sequences are computable and its converse are proved below in outline. It is assumed that the terms "well-formed formula" (W.F.F.) and "conversion" as used by Church and Kleene are understood. In the second of these proofs the existence of several formulae is assumed without proof; these formulae may be constructed straightforwardly with the help of, e.g., the results of Kleene in "A theory of positive integers in formal logic", American Journal of Math., 57 (1935), 153-173, 219-244.

The W.F.F. representing an integer $n$ will be denoted by $N_n$. We shall say that a sequence $\gamma$ whose $n$-th figure is $\phi_\gamma(n)$ is $\lambda$-definable or effectively calculable if $1 + \phi_\gamma(u)$ is a $\lambda$-definable function of $n$, i.e. if there is a W.F.F. $M_\gamma$ such that, for all integers $n$,

$$\{M_\gamma\}(N_n)\ \mathrm{conv}\ N_{\phi_\gamma(n)+1},$$

i.e. $\{M_\gamma\}(N_n)$ is convertible into $\lambda xy.x(x(y))$ or into $\lambda xy.x(y)$ according as the $n$-th figure of $\lambda$ is 1 or 0.

To show that every $\lambda$-definable sequence $\gamma$ is computable, we have to show how to construct a machine to compute $\gamma$. For use with machines it is convenient to make a trivial modification in the calculus of conversion. This alteration consists in using $x, x', x'', \ldots$ as variables instead of $a, b, c, \ldots$. We now construct a machine $\mathcal{L}$ which, when supplied with the formula $M_\gamma$, writes down the sequence $\gamma$. The construction of $\mathcal{L}$ is somewhat similar to that of the machine $\mathcal{K}$ which proves all provable formulae of the functional calculus. We first construct a choice machine $\mathcal{L}_1$, which, if supplied with a W.F.F., $M$ say, and suitably manipulated, obtains any formula into which $M$ is convertible. $\mathcal{L}_1$ can then be modified so as to yield an automatic machine $\mathcal{L}_2$ which obtains successively all the formulae

It may be proved that there is a formula $V$ such that

$$
\left\{ \{V\}(N_{\xi(n+1)}) \right\}(N_{\xi(n)}) =
\begin{cases}
\operatorname{conv} N_1 & \text{if, in going from the } n\text{-th to the } (n+1)\text{-th complete configuration, the figure } 0 \text{ is printed.} \\
\operatorname{conv} N_2 & \text{if the figure } 1 \text{ is printed.} \\
\operatorname{conv} N_3 & \text{otherwise.}
\end{cases}
$$

Let $W_\gamma$ stand for

$$
\lambda u \left[ \{V\} \left( \{A_\gamma\} (\{U_\gamma\}(u)) \right) \right] (\{U_\gamma\}(u)),
$$

so that, for each integer $n$,

$$
\left\{ \{V\}(N_{\xi(n+1)}) \right\}(N_{\xi(n)}) \operatorname{conv} \{W_\gamma\}(N_n),
$$

and let $Q$ be a formula such that

$$
\left\{ \{Q\}(W_\gamma) \right\}(N_s) \operatorname{conv} N_{r(s)},
$$

where $r(s)$ is the $s$-th integer $q$ for which $\{W_\gamma\}(N_q)$ is convertible into either $N_1$ or $N_2$. Then, if $M_\gamma$ stands for

$$
\lambda w \left[ \{W_\gamma\} \left( \{Q\}(W_\gamma)(w) \right) \right],
$$

it will have the required property†.

The Graduate College,
Princeton University,
New Jersey, U.S.A.

† In a complete proof of the $\lambda$-definability of computable sequences it would be best to modify this method by replacing the numerical description of the complete configurations by a description which can be handled more easily with our apparatus. Let us choose certain integers to represent the symbols and the $m$-configurations of the machine. Suppose that in a certain complete configuration the numbers representing the successive symbols on the tape are $s_1 s_2 \ldots s_n$, that the $m$-th symbol is scanned, and that the $m$-configuration has the number $t$; then we may represent this complete configuration by the formula

$$
[N_{s_1}, N_{s_2}, \ldots, N_{s_{m-1}}, [N_t, N_{s_m}], [N_{s_{m+1}}, \ldots, N_{s_n}]],
$$

where

$$
[a, b] \text{ stands for } \lambda u \left[ \{ \{u\}(a) \}(b) \right],
$$

$$
[a, b, c] \text{ stands for } \lambda u \left[ \{ \{ \{u\}(a) \}(b) \}(c) \right],
$$

etc.
