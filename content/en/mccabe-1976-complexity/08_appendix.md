---
paper: mccabe-1976-complexity
title: A Complexity Measure
authors:
  - Thomas J. McCabe
year: 1976
venue: IEEE Transactions on Software Engineering
field: software
section_title: Appendix
kind: appendix
lang: en
source: http://www.literateprogramming.com/mccabe.pdf
pdf_sha256: be2ac1035940dfc7fa231e23b33bfa3c2f3e3d8ef3112e20cf92a35a7af537f6
pdf_pages: 12-13
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 63ffc07264343aa882d709b9805fd9064f16ba07c073b80170ac1cbca653cebd
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

A method of computing the number of possible paths in a structured program will be briefly outlined. This method associates an algebraic expression C with each of the structured constructs and assumes that the complexity of a basic functional or replacement statement is one. The various syntactic constructs used in structured programming and their control flow and complexity expressions are shown below. The symbol $\alpha$ stands for the number of iterations in a loop.

CONTROL FLOW:

A; b
C(A) x C(B)

IF A THEN B ELSE C
C(A) x [C(B) + C(C)]

WHILE A DO B
C(A) + [C(A) x C(B)]$^\alpha$ C(A)

C(A) x [C(A) + C(A) + C(A)]

[C(B) x C(A)]$^\alpha$

The program SEARCH below is used to illustrate. SEARCH performs a binary search for input parameter ITEM on a table T of length N. SEARCH sets F to 1 and J to ITEM’s index within T if the search is successful—otherwise F is set to 0 indicating that ITEM is not in T.

```text
PROCEDURE SEARCH (ITEM) INTEGER ITEM
BEGIN
INTEGER L, H;
F←0;
L←0;
H←N;
```

While H > L and F = 0 Do
    If T[J < (H+L) DIV 2] = item
        THEN
            If item < T[J]
                THEN
                    H ← J - 1
                ELSE
                    L ← J + 1
            ELSE
                F ← 1
        END
END

The flow graph for SEARCH is

[2] B. W. Boehm, "Software and its impact: A quantitative assessment," Datamation, vol. 19, pp. 48-59, May 1973.
[3] W. B. Cammack and H. J. Rogers, "Improving the programming process," IBM Tech. Rep. TR 00.2483, Oct. 1973.
[4] D. E. Knuth, "Structured programming with GOTO statements," Computing Surveys, vol. 6, pp. 261-301, Dec. 1974.
[5] R. Kosaraju, "Analysis of structured programs," J. Comput. Syst. Sci., vol. 9, pp. 232-255, Dec. 1974; also, Dep. Elec. Eng., The Johns Hopkins Univ., Baltimore, MD, Tech. Rep. 72-11, 1972.
[6] H. Legard and M. Marcotty, "A generalogy of control structures," Commun. Assoc. Comput. Mach., vol. 18, pp. 629-639, Nov. 1975.
[7] H. D. Mills, "Mathematical foundations for structured programming," Federal System Division, IBM Corp., Gaithersburg, MD, FSC 72-6012, 1972.

The algebraic complexity C would be computed as

$$
C_{(SEARCH)} = 1 \ 1 \ 1 \quad \{ 1 + (1 [1[1+1]+1])^{\alpha} 1 \}
= \{ 1 + (3)^{\alpha} \}.
$$

Assuming I to be at least 4, the lower bound for the expression $\{ 1 + 3^{\alpha} \}$ is 4 which indicates there are at least 4 paths to be tested. The first test would be from the immediate exit from the WHILE loop which could be tested by choosing H less than L initially. The next three tests (the three ways through the body of the loop) correspond to cases where ITEM = T[J], ITEM < T[1], and ITEM > T[J].
