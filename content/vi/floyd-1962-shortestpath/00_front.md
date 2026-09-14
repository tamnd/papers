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
lang: vi
source: https://web.archive.org/web/20200531072111id_/https://dl.acm.org/doi/pdf/10.1145/367766.368168?download=true
pdf_sha256: fd7424d2a47593223e2b490e841613bd900bc140944cb4eb590cff0e529886a2
pdf_pages: 1-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: a837fdbfade460e310650f716debaf66f6063a5c603f87cb848375ec874824c5
translated_from: content/en/floyd-1962-shortestpath/00_front.md
source_content_sha256: 788b14d898f39ea55119fee7826ab2c26dfeaf295309895dff48392515b084d4
translation_model: gpt-6-astra
translation_run: 20260914T155157Z
glossary_version: 6
glossary_terms_sha256: 51f62d367854beec600f51894702ad34dfcde96c993d5c00a2f7a9873047d13f
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
roundtrip: same
roundtrip_run: 20260914T214350Z
---

THUẬT TOÁN 93

SỐ HỌC BẬC TỔNG QUÁT

Millard H. Perstein

Control Data Corp., Palo Alto, Calif.

procedure arithmetic (a, b, c, op);

integer a, b, c, op;

comment Thủ tục này thực hiện các phép toán số học thuộc các bậc khác nhau với $b$ và $c$, lưu kết quả vào $a$. Bậc của phép toán được cho bởi $op$. Với $op = 1$, phép cộng được thực hiện. Với $op = 2$, phép nhân, tức phép cộng lặp lại, được thực hiện. Ở các bậc cao hơn, các phép toán không có tính giao hoán. Với $op = 3$, phép lũy thừa, tức phép nhân lặp lại, được thực hiện, nâng $b$ lên lũy thừa $c$. Ở các bậc cao hơn nữa, cách nhóm các toán hạng là vấn đề quan trọng. Cặp dấu ngoặc ngầm định trong cùng nằm ở bên phải. Siêu số mũ (hyper-exponent) luôn là $c$. Với $op = 4$, phép lũy thừa chồng (tetration), tức phép lũy thừa lặp lại, được thực hiện. Với $op = 5, 6, 7$, v.v., thủ tục lần lượt thực hiện pentation, hexation, heptation, v.v.

Thủ tục này ban đầu được lập trình bằng FORTRAN cho máy tính Control Data 160 có kích thước bằng một chiếc bàn làm việc. Chương trình ban đầu chỉ hỗ trợ đến phép lũy thừa chồng vì khả năng đệ quy của chương trình con trong FORTRAN trên Control Data 160 bị giới hạn ở bốn mức nhằm tiết kiệm tài nguyên.

Các tham số đầu vào, $b, c$, và $op$, phải là các số nguyên dương, không được bằng không;

begin own integer d, e, f, drop;

if op = 1 then

begin a := b + c; go to 1

end if op = 2 then d := 0;

else d := 1; e := c; drop := op - 1;

for f := 1 step 1 until e do

begin arithmetic (a, b, d, drop);

d := a

end;
