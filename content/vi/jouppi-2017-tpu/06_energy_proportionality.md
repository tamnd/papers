---
paper: jouppi-2017-tpu
title: In-Datacenter Performance Analysis of a Tensor Processing Unit
authors:
  - Norman P. Jouppi
  - Cliff Young
  - Nishant Patil
  - David Patterson
  - Gaurav Agrawal
  - Raminder Bajwa
  - Sarah Bates
  - Suresh Bhatia
  - Nan Boden
  - Al Borchers
year: 2017
venue: ISCA
field: architecture
section: "6"
section_title: Tính tỷ lệ thuận với năng lượng
tag: "0191"
kind: section
lang: vi
source: arxiv:1704.04760
pdf_sha256: 19793e4ae1486630ac45a12facabc0e80609dd679db8ca7a3a040f8bf0d8e0be
pdf_pages: "10"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: d3f675a5a7bab35f6a66538905ef5002fa93e6900283c3ab502f13d6ed65064a
translated_from: content/en/jouppi-2017-tpu/06_energy_proportionality.md
source_content_sha256: 4048a39c09f779fe18ea5fd961414a6a4dddf28976444afbbf7dc9eb47aa9b1f
translation_model: gpt-5
translation_run: 20260914T201546Z
glossary_version: 6
glossary_terms_sha256: 1f83355a83baacb04f1185b8bd47b133f28d2f764f5d7ae919d5d9d0d7e083ee
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Thermal Design Power (TDP) ảnh hưởng đến chi phí cung cấp nguồn điện, vì cần cung cấp đủ điện năng và làm mát khi phần cứng hoạt động ở công suất tối đa. Tuy nhiên, chi phí điện năng dựa trên mức tiêu thụ trung bình khi tải công việc thay đổi trong ngày. [Bar07] nhận thấy rằng các server bận 100% trong chưa đến 10% thời gian và đề xuất tính tỷ lệ thuận với năng lượng: các server nên tiêu thụ công suất tỷ lệ thuận với lượng công việc được thực hiện. Ước tính công suất tiêu thụ trong phần trước dựa trên tỷ lệ của TDP đã được quan sát trong các datacenter của chúng tôi.

Chúng tôi đo hiệu năng và công suất khi mức sử dụng tải công việc được cung cấp thay đổi từ 0% đến 100%, được thu thập trong các nhóm với độ lệch tải công việc 10% [Lan09]. Hình 10 cho thấy công suất của server chia cho số die trên mỗi server đối với ba chip bằng cách thay đổi tải công việc của CNN0. Chúng tôi biểu diễn công suất tăng thêm (K80 và TPU) cũng như công suất tổng (K80+Haswell/4 và TPU+Haswell/2) cho GPU và TPU. Lưu ý rằng tất cả đều được cung cấp cùng kích thước lô.

Chúng tôi thấy rằng TPU có công suất thấp nhất—118W trên mỗi die cho tổng công suất (TPU+Haswell/2) và 40W trên mỗi die cho công suất tăng thêm (TPU trong Hình 10)—nhưng nó có tính tỷ lệ thuận với năng lượng kém: ở mức tải 10%, TPU sử dụng 88% công suất mà nó sử dụng ở mức 100%. (Lịch trình thiết kế ngắn đã ngăn việc đưa vào nhiều tính năng tiết kiệm năng lượng.) Không có gì đáng ngạc nhiên, Haswell có tính tỷ lệ thuận với năng lượng tốt nhất trong nhóm: nó sử dụng 56% công suất ở mức tải 10% so với khi ở mức 100%. K80 gần với CPU hơn TPU, sử dụng 66% công suất khi đầy tải ở mức tải công việc 10%. LSTM1, vốn không bị giới hạn bởi tính toán, hoạt động tương tự: ở mức tải 10%, CPU sử dụng 47% công suất đầy tải, GPU sử dụng 78%, và TPU sử dụng 94%.

Điều gì xảy ra với mức sử dụng công suất của server khi chạy CNN0 nếu nó trở thành máy chủ cho các bộ tăng tốc? Khi GPU và TPU ở mức tải 100%, server CPU sử dụng 52% công suất đầy tải cho GPU và 69% cho TPU. (CPU thực hiện nhiều công việc hơn cho TPU vì nó đang chạy nhanh hơn GPU rất nhiều.) Do đó, server Haswell cùng với bốn TPU sử dụng <20% công suất bổ sung nhưng chạy CNN0 nhanh hơn 80 lần so với riêng server Haswell (4 TPU so với 2 CPU).
