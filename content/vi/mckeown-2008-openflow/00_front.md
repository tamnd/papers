---
paper: mckeown-2008-openflow
title: 'OpenFlow: Enabling Innovation in Campus Networks'
authors:
  - Nick McKeown
  - Tom Anderson
  - Hari Balakrishnan
  - Guru Parulkar
  - Larry Peterson
  - Jennifer Rexford
  - Scott Shenker
  - Jonathan Turner
year: 2008
venue: ACM SIGCOMM Computer Communication Review
field: networks
section_title: Front Matter
tag: "0175"
kind: front
lang: vi
source: http://ccr.sigcomm.org/online/files/p69-v38n2n-mckeown.pdf
pdf_sha256: f71746e44666eec5baf625764a347cb142fb21e60dd4b647eefe73ac262aeb60
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 321d54c94ca752ded958efa71b2c1142e4237406ccb2367ebee63f36091e4e5f
translated_from: content/en/mckeown-2008-openflow/00_front.md
source_content_sha256: c7e8d31637617bbb8444b7e0c18c6a50a4c45bcab406f2a4f69f47a10b8a8c6b
translation_model: gpt-5
translation_run: 20260918T153717Z
glossary_version: 7
glossary_terms_sha256: 5bfb74d0e4b3e9a8237f78ceae59e221549684c174791655271c5455f7fd5e4e
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

OpenFlow: Thúc đẩy đổi mới trong các mạng khuôn viên

Nick McKeown

Stanford University

Guru Parulkar

Stanford University

Tom Anderson

University of Washington

Larry Peterson

Princeton University

Hari Balakrishnan

MIT

Jennifer Rexford

Princeton University

Scott Shenker

University of California, Berkeley

Jonathan Turner

Washington University in St. Louis

Bài báo này là một ghi chú biên tập được gửi tới CCR. Bài báo CHƯA được phản biện.

Các tác giả chịu hoàn toàn trách nhiệm về nội dung kỹ thuật của bài báo này.

Có thể đăng nhận xét thông qua CCR Online.

TÓM TẮT

Sách trắng này đề xuất OpenFlow: một phương thức cho phép các nhà nghiên cứu chạy các giao thức thử nghiệm trong những mạng mà họ sử dụng hằng ngày. OpenFlow dựa trên một chuyển mạch Ethernet, với một bảng luồng nội bộ (flow-table), và một giao diện được chuẩn hóa để thêm và loại bỏ các mục nhập luồng. Mục tiêu của chúng tôi là khuyến khích các nhà cung cấp mạng bổ sung OpenFlow vào các sản phẩm chuyển mạch của họ để triển khai trong các mạng trục khuôn viên đại học và các tủ đấu nối dây. Chúng tôi tin rằng OpenFlow là một sự thỏa hiệp thực dụng: một mặt, nó cho phép các nhà nghiên cứu chạy các thử nghiệm trên những chuyển mạch không đồng nhất theo một cách thống nhất với tốc độ đường truyền và mật độ cổng cao; mặt khác, các nhà cung cấp không cần phải công khai cách thức hoạt động nội bộ của các chuyển mạch của họ. Ngoài việc cho phép các nhà nghiên cứu đánh giá ý tưởng của họ trong các bối cảnh lưu lượng thực tế, OpenFlow có thể đóng vai trò là một thành phần hữu ích của khuôn viên trong các testbed quy mô lớn được đề xuất như GENI. Hai tòa nhà tại Stanford University sẽ sớm vận hành các mạng OpenFlow, sử dụng các chuyển mạch Ethernet và bộ định tuyến thương mại. Chúng tôi sẽ làm việc để khuyến khích việc triển khai tại các trường khác; và chúng tôi khuyến khích bạn xem xét triển khai OpenFlow trong mạng trường đại học của mình.
