---
paper: bosshart-2014-p4
title: 'P4: Programming Protocol-Independent Packet Processors'
authors:
  - Pat Bosshart
  - Dan Daly
  - Glen Gibb
  - Martin Izzard
  - Nick McKeown
  - Jennifer Rexford
  - Cole Schlesinger
  - Dan Talayco
  - Amin Vahdat
  - George Varghese
  - David Walker
year: 2014
venue: ACM SIGCOMM Computer Communication Review
field: networks
section: "6"
section_title: KẾT LUẬN
tag: 009D
kind: section
lang: vi
source: arxiv:1312.1719
pdf_sha256: 2bb0ccb7b5410868efdecc9ef5208d235c6f3aa75dee84aa992751aed117a42f
pdf_pages: "7"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 4560e0fdfd360fd4dacf8c7e1065fd55c520ea9350554e4b5d695c6f01a70fd8
translated_from: content/en/bosshart-2014-p4/06_conclusion.md
source_content_sha256: 80a6aa96195a65f9aa76e0574e7f3fe1cbb89f4966ef2b4c7287e9cec28edb9b
translation_model: gpt-5
translation_run: 20260914T163737Z
glossary_version: 6
glossary_terms_sha256: 3a5b9dd3cd6211761c92d70db4c4910c364b1cae9e5e732eea77349f449c860b
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Lời hứa của SDN là một mặt phẳng điều khiển duy nhất có thể trực tiếp điều khiển toàn bộ một mạng các chuyển mạch. OpenFlow hỗ trợ mục tiêu này bằng cách cung cấp một API duy nhất, không phụ thuộc nhà cung cấp. Tuy nhiên, OpenFlow ngày nay hướng tới các chuyển mạch có chức năng cố định, nhận biết một tập các trường phần đầu được xác định trước và xử lý các gói tin bằng một tập nhỏ các hành động được định nghĩa trước. Mặt phẳng điều khiển không thể biểu đạt cách các gói tin nên được xử lý để đáp ứng tốt nhất nhu cầu của các ứng dụng điều khiển.

Chúng tôi đề xuất một bước tiến hướng tới các chuyển mạch linh hoạt hơn, trong đó chức năng được đặc tả — và có thể được thay đổi — trong quá trình triển khai. Lập trình viên quyết định cách mặt phẳng chuyển tiếp xử lý các gói tin mà không cần lo lắng về các chi tiết triển khai. Một trình biên dịch chuyển đổi một chương trình mệnh lệnh thành một đồ thị phụ thuộc bảng có thể được ánh xạ tới nhiều chuyển mạch đích cụ thể, bao gồm cả các triển khai phần cứng được tối ưu hóa.

Chúng tôi nhấn mạnh rằng đây chỉ là bước đầu tiên, được thiết kế như một đề xuất sơ bộ cho OpenFlow 2.0 nhằm đóng góp vào cuộc tranh luận. Trong đề xuất này, một số khía cạnh của một chuyển mạch vẫn chưa được xác định (ví dụ, các nguyên thủy điều khiển tắc nghẽn, các chính sách xếp hàng, giám sát lưu lượng). Tuy nhiên, chúng tôi tin rằng cách tiếp cận sử dụng một ngôn ngữ cấu hình — và các trình biên dịch tạo ra các cấu hình mức thấp cho các đích cụ thể — sẽ dẫn tới các chuyển mạch trong tương lai cung cấp tính linh hoạt cao hơn, đồng thời khai phá tiềm năng của các mạng được định nghĩa bằng phần mềm.
