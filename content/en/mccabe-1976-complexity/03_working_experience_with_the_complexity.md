---
paper: mccabe-1976-complexity
title: A Complexity Measure
authors:
  - Thomas J. McCabe
year: 1976
venue: IEEE Transactions on Software Engineering
field: software
section: III
section_title: WORKING EXPERIENCE WITH THE COMPLEXITY MEASURE
tag: 03AC
kind: section
lang: en
source: http://www.literateprogramming.com/mccabe.pdf
pdf_sha256: be2ac1035940dfc7fa231e23b33bfa3c2f3e3d8ef3112e20cf92a35a7af537f6
pdf_pages: 2-7
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: e6be71150c0d006f056f12a35280034053c154fab1a1fe266d76c13bf759fd2e
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

In this section a system which automates the complexity measure will be described. The control structures of several PDP-10 Fortran programs and their corresponding complexity measures will be illustrated.

To aid the author’s research into control structure complexity a tool was built to run on a PDP-10 that analyzes the structure of Fortran programs. The tool, FLOW, was written in APL to input the source code from Fortran files on disk. FLOW would then break a Fortran job into distinct subroutines and analyze the control structure of each subroutine. It does this by breaking the Fortran subroutines into blocks that are delimited by statements that affect control flow: IF, GOTO, referenced LABELS, DO, etc. The flow between the blocks is then represented in an $n$ by $n$ matrix (where $n$ is the number of blocks), having a 1 in the $i$-$j$th position if block i can branch to block j in 1 step. FLOW also produces the “blocked” listing of the original program, computes the cyclomatic complexity, and produces a reachability matrix (there is a 1 in the $i$-$j$th position if block i can branch to block j in any number of steps). An example of FLOW’s output is shown below.

```fortran
IMPLICIT INTEGER(A-Z)
COMMON / ALLOC / MEM(2048),LM,LU,LV,LW,LX,LY,LQ,LWEX
     NCHARS,NWORDS
DIMENSION MEMORY(2048),INHEAD(4),ITRANS(128)
TYPE 1
FORMAT(DOMOLKI STRUCTURE FILE NAME? $)
NAMDML=0
ACCEPT 2,NAMDML
FORMAT(A5)
CALL ALCHAN(ICHAN)
CALL IFILE(ICHAN,'DSK',NAMDML,'DAT',0,0)
CALL READB(ICHAN,INHEAD,132,NREAD,$990,$990)
NCHARS=INHEAD(1)
NWORDS=INHEAD(2)
```

[^1]: The role of the variable p will be explained in Section IV. For these examples assume p = 1.

IEEE TRANSACTIONS ON SOFTWARE ENGINEERING, DECEMBER 1976

```fortran
NTOT=(NCHARS+7)*NWORDS
LTOT=(NCHARS+5)*NWORDS
******** BLOCK NO. 1 *******************************
      IF(LTOT,GT,2048) GO TO 900
******** BLOCK NO. 2 *******************************
      CALL READB(ICHAN,MEMORY,LTOT,NREAD,$990,$990)
      LM=0
      LU=NCHARS*NWORDS+LM
      LV=NWORDS+LU
      LW=NWORDS+LV
      LX=NWORDS+LW
      LY=NWORDS+LX
      LQ=NWORDS+LY
      LWEX=NWORDS+LQ
      BLOCK NO. 3
******** DO 700 I=1,NWORDS *************************
      MEMORY(LWEX+I)=(MEMORY(LW+I),OR,(MEMORY(LW+I)*2))
700   CONTINUE
******** BLOCK NO. 4 *******************************
      CALL EXTEXT(ITRANS)
      STOP
******** BLOCK NO. 5 *******************************
900   TYPE 3,LTOT
3     FORMAT('STRUCTURE TOO LARGE FOR CORE; ',I8,' WORDS'
     1 ' SEE COOPER ' /)
      STOP
******** BLOCK NO. 6 *******************************
990   TYPE $
4     FORMAT(' READ ERROR, OR STRUCTURE FILE ERROR; ' /
     1 ' SEE COOPER ' /)
      STOP
      END
```

CONNECTIVITY MATRIX

| 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|
| 0 | 1 | 1 | 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 |

Figure.

-DL,DL,DL,DL,DL,DL,DL,DL,DL,DL,DL,DL,DL

CYCLOMATIC COMPLEXITY = 3

| 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|
| 0 | 1 | 1 | 1 | 1 | 1 | 1 |
| 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| 0 | 0 | 0 | 1 | 1 | 1 | 1 |
| 0 | 0 | 0 | 1 | 1 | 1 | 1 |
| 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 |

END

At this point a few of the control graphs that were found in live programs will be presented. The actual control graphs from FLOW appear on a DATA DISK CRT but they are hand drawn here for purposes of illustration. The graphs are presented in increasing order of complexity in order to suggest the correlation between the complexity numbers and our intuitive notion of control flow complexity.

Figure.

Figure.

Figure.

V(G) = 8

V(G) = 8

V(G) = 8

V(G)=10

V(G)=10

V(G)=11

One of the more interesting aspects of the automatic approach is that although FLOW could be implemented much more efficiently in a compiler level language, it is still possible to go through a year's worth of a programmer's Fortran code in about 20 min. After seeing several of a programmer's control graphs on a CRT one can often recognize "style" by noting similar patterns in the graphs. For example, one programmer had an affinity for sequencing numerous simple loops as in

Figure.

V(G) = 10

Figure.

V(G) = 19

It was later revealed that these programs were eventually to run on a CDC6600 and the "tight" loops were designed to stay within the hardware stack.

These results have been used in an operational environment by advising project members to limit their software modules by cyclomatic complexity instead of physical size. The particular upper bound that has been used for cyclomatic complexity is 10 which seems like a reasonable, but not magical, upper limit. Programmers have been required to calculate complexity as they create software modules. When the complexity exceeded 10 they had to either recognize and modularize subfunctions or redo the software. The intention was to keep the "size" of the modules manageable and allow for testing all the independent paths (which will be elaborated upon in Section VII.) The only situation in which this limit has seemed unreasonable is when a large number of independent cases followed a selection function (a large case statement), which was allowed.

It has been interesting to note how individual programmer's style relates to the complexity measure. The author has been delighted to find several programmers who never had formal training in structured programming but consistently write code in the 3 to 7 complexity range which is quite well structured. On the other hand, FLOW has found several programmers who frequently wrote code in the 40 to 50 complexity range (and who claimed there was no other way to do it). On one occasion the author was given a DEC tape of 24 Fortran subroutines that were part of a large real-time graphics system. It was rather disquieting to find, in a system where reliability is critical, subroutines of the following complexity: 16, 17, 24, 24, 32, 34, 41, 54, 56, and 64. After confronting the project members with these results the author was told that the subroutines on the DEC tape were chosen because they were troublesome and indeed a close correlation was found between the ranking of subroutines by complexity and a ranking by reliability (performed by the project members).
