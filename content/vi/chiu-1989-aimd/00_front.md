---
paper: chiu-1989-aimd
title: Analysis of the Increase and Decrease Algorithms for Congestion Avoidance in Computer Networks
authors:
  - Dah-Ming Chiu
  - Raj Jain
year: 1989
venue: Computer Networks and ISDN Systems
field: networks
section_title: Front Matter
tag: "0173"
kind: front
lang: vi
source: https://www.cse.wustl.edu/~jain/papers/cong_av.htm
pdf_sha256: fd0b0386c611744e744969d3c5ec3e236dc6036344128ed16e7f378a9e257be2
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 6625ca60a2d1260566914431234ccad4e39c4b8d22a746965260f68239fd2d47
translated_from: content/en/chiu-1989-aimd/00_front.md
source_content_sha256: bef6df3d4dd857698abefe1e5ba415e93976475582859bd5331e67415f388fb2
translation_model: gpt-5
translation_run: 20260915T060234Z
glossary_version: 6
glossary_terms_sha256: 3a5b9dd3cd6211761c92d70db4c4910c364b1cae9e5e732eea77349f449c860b
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Phân tích các thuật toán tăng và giảm cho tránh tắc nghẽn trong các mạng máy tính

Dah-Ming CHIU and Raj JAIN

Digital Equipment Corporation, 550 King Street (LKG1-2/A19),

Littleton, MA 01460-1289, U.S.A.

Địa chỉ mới: Raj Jain, Washington University in Saint Louis,

jain@cse.wustl.edu, http://www.cse.wustl.edu/~jain

Tóm tắt. Các cơ chế tránh tắc nghẽn cho phép một mạng hoạt động trong vùng tối ưu có độ trễ thấp và thông lượng cao, do đó ngăn mạng trở nên tắc nghẽn. Điều này khác với các cơ chế kiểm soát tắc nghẽn truyền thống, cho phép mạng phục hồi từ trạng thái tắc nghẽn có độ trễ cao và thông lượng thấp. Cả cơ chế tránh tắc nghẽn và cơ chế kiểm soát tắc nghẽn về cơ bản đều là các bài toán quản lý tài nguyên. Chúng có thể được xây dựng dưới dạng các bài toán điều khiển hệ thống, trong đó hệ thống cảm nhận trạng thái của nó và phản hồi thông tin này đến người dùng để họ điều chỉnh các điều khiển của mình.

Thành phần chính của bất kỳ sơ đồ tránh tắc nghẽn nào là thuật toán (hoặc hàm điều khiển) được người dùng sử dụng để tăng hoặc giảm tải của họ (cửa sổ hoặc tốc độ). Chúng tôi mô tả một cách trừu tượng một lớp rộng các thuật toán tăng/giảm như vậy và so sánh chúng bằng cách sử dụng một số chỉ số hiệu năng khác nhau. Các chỉ số chính là hiệu quả, tính công bằng, thời gian hội tụ và kích thước của dao động.

Chỉ ra rằng một thuật toán tăng cộng và giảm nhân đơn giản thỏa mãn các điều kiện đủ để hội tụ đến một trạng thái hiệu quả và công bằng bất kể trạng thái ban đầu của mạng. Đây là thuật toán cuối cùng được chọn để triển khai trong sơ đồ tránh tắc nghẽn được khuyến nghị cho Digital Networking Architecture và OSI Transport Class 4 Networks.

Từ khóa.
