---
paper: cook-1971-np
title: The Complexity of Theorem-Proving Procedures
authors:
  - Stephen A. Cook
year: 1971
venue: STOC
field: theory
section_title: Tóm tắt
kind: section
lang: vi
source: https://www.cs.toronto.edu/~sacook/homepage/1971.pdf
pdf_sha256: aacaca0dd6db8b409317a2de282734539c3186a72cff1cb4dd601c76a4ddfb75
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 7ceaac681b40421e225aa8bf09ba3c37885f594e3dd1083b6ce03fd32b666a5e
translated_from: content/en/cook-1971-np/01_summary.md
source_content_sha256: 56f97123718bb78eda5c316f7c253ad48e61d7b88fb594127abc34fc4e82eab5
translation_model: gpt-5
translation_run: 20260919T075800Z
glossary_version: 7
glossary_terms_sha256: a53d4b02c913445c3baaef8eee5fd81f1dcadf55e59409c12a52700dc0c85335
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Chỉ ra rằng mọi bài toán nhận dạng được giải bởi một máy Turing không tất định bị giới hạn thời gian đa thức đều có thể được "rút gọn" về bài toán xác định liệu một công thức mệnh đề đã cho có phải là một hằng đúng hay không. Ở đây "rút gọn" có nghĩa, một cách đại khái, là bài toán thứ nhất có thể được giải một cách tất định trong thời gian đa thức với điều kiện có sẵn một oracle để giải bài toán thứ hai. Từ khái niệm về khả năng rút gọn này, các bậc đa thức về độ khó được định nghĩa, và chỉ ra rằng bài toán xác định tính hằng đúng có cùng bậc đa thức với bài toán xác định liệu đồ thị thứ nhất trong hai đồ thị đã cho có đẳng cấu với một đồ thị con của đồ thị thứ hai hay không. Các ví dụ khác được thảo luận. Một phương pháp đo độ phức tạp của các thủ tục chứng minh cho phép tính vị từ được đưa ra và thảo luận.

Trong toàn bộ bài báo này, một tập các chuỗi có nghĩa là một tập các chuỗi trên một bảng chữ cái $\Sigma$ cố định, lớn, hữu hạn nào đó. Bảng chữ cái này đủ lớn để bao gồm các ký hiệu cho tất cả các tập được mô tả ở đây. Tất cả các máy Turing đều là các thiết bị nhận dạng tất định, trừ khi điều ngược lại được nêu rõ.
