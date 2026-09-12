---
paper: floyd-1962-shortestpath
title: 'Algorithm 97: Shortest Path'
authors:
  - Robert W. Floyd
year: 1962
venue: Communications of the ACM
field: algorithms
section_title: Front Matter
tag: 003F
kind: front
lang: en
source: https://web.archive.org/web/20200531072111id_/https://dl.acm.org/doi/pdf/10.1145/367766.368168?download=true
pdf_sha256: fd7424d2a47593223e2b490e841613bd900bc140944cb4eb590cff0e529886a2
pdf_pages: 1-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 788b14d898f39ea55119fee7826ab2c26dfeaf295309895dff48392515b084d4
prompt_sha256: 329630a0b9175a55e4af1b8e281a3e67eeab250f8d643953b7dcde99743c7628
---

ALGORITHM 93

GENERAL ORDER ARITHMETIC

Millard H. Perstein

Control Data Corp., Palo Alto, Calif.

procedure arithmetic (a, b, c, op);

integer a, b, c, op;

comment This procedure will perform different order arithmetic operations with $b$ and $c$, putting the result in $a$. The order of the operation is given by $op$. For $op = 1$ addition is performed. For $op = 2$ multiplication, repeated addition, is done. Beyond these the operations are non-commutative. For $op = 3$ exponentiation, repeated multiplication, is done, raising $b$ to the power $c$. Beyond these the question of grouping is important. The innermost implied parentheses are at the right. The hyper-exponent is always $c$. For $op = 4$ tetration, repeated exponentiation, is done. For $op = 5, 6, 7$, etc., the procedure performs pentation, hexation, heptation, etc., respectively.

The routine was originally programmed in FORTRAN for the Control Data 160 desk-size computer. The original program was limited to tetration because subroutine recursiveness in Control Data 160 FORTRAN has been held down to four levels in the interests of economy.

The input parameter, $b, c$, and $op$, must be positive integers, not zero;

begin own integer d, e, f, drop;

if op = 1 then

begin a := b + c; go to 1

end if op = 2 then d := 0;

else d := 1; e := c; drop := op - 1;

for f := 1 step 1 until e do

begin arithmetic (a, b, d, drop);

d := a

end;
