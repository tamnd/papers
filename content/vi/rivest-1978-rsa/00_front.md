---
paper: rivest-1978-rsa
title: A Method for Obtaining Digital Signatures and Public-Key Cryptosystems
authors:
  - R. L. Rivest
  - A. Shamir
  - L. Adleman
year: 1978
venue: Communications of the ACM
field: security
section_title: Front Matter
tag: 019B
kind: front
lang: vi
source: https://doi.org/10.21236/ada606588
pdf_sha256: f7b1f78d9a7cbeb85e32b8c563a6db60771a5cc4bdc55580645f7cb778a4966b
pdf_pages: 1-2
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: b522b8c90a18eeb64fc301f144dd0c2b5957bab862709982dc39f7c92a2c52a4
translated_from: content/en/rivest-1978-rsa/00_front.md
source_content_sha256: a122f6e963bdec6d2a2f2fab3baf85cc2d021a0f98467e0ee78e686e4fbe9f55
translation_model: gpt-5
translation_run: 20260915T013833Z
glossary_version: 6
glossary_terms_sha256: 363c21723d588ca6b8032fd3e2b0aa8dc6ab225b1f9ca1b6e98d75976e8b0d0a
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Phương pháp thu nhận chữ ký số và các hệ mật mã khóa công khai

R.L. Rivest, A. Shamir, and L. Adleman*

Tóm tắt

Một phương pháp mã hóa được trình bày với tính chất mới là việc công khai một khóa mã hóa không làm lộ khóa giải mã tương ứng. Điều này có hai hệ quả quan trọng:

1. Không cần người đưa thư hoặc các phương tiện an toàn khác để truyền các khóa, vì một thông điệp có thể được mã hóa bằng khóa mã hóa được người nhận dự định công khai. Chỉ người đó có thể giải mã thông điệp, vì chỉ người đó biết khóa giải mã tương ứng.

2. Một thông điệp có thể được “ký” bằng một khóa giải mã được giữ bí mật. Bất kỳ ai cũng có thể xác minh chữ ký này bằng khóa mã hóa tương ứng được công khai. Chữ ký không thể bị giả mạo, và người ký không thể sau đó phủ nhận tính hợp lệ của chữ ký của mình. Điều này có các ứng dụng rõ ràng trong các hệ thống “thư điện tử” và “chuyển tiền điện tử”.

Một thông điệp được mã hóa bằng cách biểu diễn nó dưới dạng một số M, nâng M lên lũy thừa công khai được chỉ định e, rồi lấy phần dư khi kết quả được chia cho tích công khai được chỉ định, n, của hai số nguyên tố bí mật lớn p và q. Việc giải mã tương tự; chỉ sử dụng một lũy thừa bí mật khác, d, trong đó $e \cdot d \equiv 1 \pmod{(p-1)(q-1)}$. Tính bảo mật của hệ thống một phần dựa trên độ khó của việc phân tích thừa số của số chia được công bố, n.

Từ khóa và cụm từ: chữ ký số, hệ mật mã khóa công khai, quyền riêng tư, xác thực, bảo mật, phân tích thừa số, số nguyên tố, thư điện tử, truyền thông điệp, chuyển tiền điện tử, mật mã học.

Các phân loại CR: 2.12, 3.15, 3.50, 3.81, 5.25
