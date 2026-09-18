---
paper: metcalfe-1976-ethernet
title: 'Ethernet: Distributed Packet Switching for Local Computer Networks'
authors:
  - Robert M. Metcalfe
  - David R. Boggs
year: 1976
venue: Communications of the ACM
field: networks
section_title: Front Matter
tag: "0053"
kind: front
lang: vi
source: https://www.cl.cam.ac.uk/teaching/0809/DigiCommI/metcalfe1976ethernet.pdf
pdf_sha256: e1e9d67146a1d0955a39b4fbb8e2951d6cefb4f7231a01acb9c78852280da227
pdf_pages: "1"
extraction: vision
extraction_model: gpt-5
content_sha256: a41ce7ba0e8b7431e1f42f4159d4a7974acb545e35d2ea2a9b97609952681ebd
translated_from: content/en/metcalfe-1976-ethernet/00_front.md
source_content_sha256: cde9ac93b9978bd817dbd9b101f21e4277f57c22d59d1aab17aa598c31ca29df
translation_model: gpt-5
translation_run: 20260918T110147Z
glossary_version: 7
glossary_terms_sha256: 5bfb74d0e4b3e9a8237f78ceae59e221549684c174791655271c5455f7fd5e4e
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Hệ thống Máy tính

G. Bell, S. Fuller và D. Siewiorek, Biên tập viên

Ethernet: Chuyển mạch Gói Phân tán cho các Mạng Máy tính Cục bộ

Robert M. Metcalfe và David R. Boggs  
Trung tâm Nghiên cứu Palo Alto của Xerox

Ethernet là một hệ thống truyền thông quảng bá phân nhánh để mang các gói dữ liệu số giữa các trạm tính toán được phân bố cục bộ. Cơ chế vận chuyển gói tin do Ethernet cung cấp đã được sử dụng để xây dựng các hệ thống có thể được xem như các mạng máy tính cục bộ hoặc các bộ đa xử lý ghép nối lỏng. Cơ sở truyền thông dùng chung của một Ethernet, Ether của nó, là một môi trường quảng bá thụ động không có điều khiển trung tâm. Việc phối hợp quyền truy cập vào Ether để phát quảng bá gói tin được phân tán giữa các trạm truyền đang tranh chấp bằng cách sử dụng phân xử thống kê có kiểm soát. Việc chuyển mạch các gói tin đến đích của chúng trên Ether được phân tán giữa các trạm nhận bằng cách sử dụng nhận dạng địa chỉ gói tin. Các nguyên tắc thiết kế và việc triển khai được mô tả, dựa trên kinh nghiệm với một Ethernet đang hoạt động gồm 100 nút dọc theo một kilômét cáp đồng trục. Một mô hình để ước lượng hiệu năng dưới tải nặng và một giao thức gói tin cho truyền thông có kiểm soát lỗi được đưa vào để hoàn chỉnh.

**Từ khóa và Cụm từ:** mạng máy tính, chuyển mạch gói, đa xử lý, điều khiển phân tán, tính toán phân tán, truyền thông quảng bá, phân xử thống kê

**Phân loại CR:** 3.81, 4.32, 6.35

Bản quyền © 1976, Association for Computing Machinery, Inc. Quyền chung cho phép tái bản, nhưng không nhằm mục đích lợi nhuận, toàn bộ hoặc một phần tài liệu này được cấp với điều kiện thông báo bản quyền của ACM được đưa vào và tham chiếu được thực hiện đến ấn phẩm, ngày phát hành của nó, và thực tế rằng các quyền tái bản đã được cấp theo sự cho phép của Association for Computing Machinery.

Địa chỉ hiện tại của các tác giả: R. M. Metcalfe, Transaction Technology, Inc., 10880 Wilshire Boulevard, Los Angeles, CA 94304; D. Boggs, Xerox Palo Alto Research Center, 3333 Coyote Hill Road, Palo Alto, CA 94304.
