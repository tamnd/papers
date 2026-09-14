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
content_sha256: 3480fe95b0a366233db4617a9a73321f79ee5cbc97a96015d28f07b61de5146a
translated_from: content/en/mckeown-2008-openflow/00_front.md
source_content_sha256: c7e8d31637617bbb8444b7e0c18c6a50a4c45bcab406f2a4f69f47a10b8a8c6b
translation_model: gpt-5
translation_run: 20260914T163737Z
glossary_version: 6
glossary_terms_sha256: 3a5b9dd3cd6211761c92d70db4c4910c364b1cae9e5e732eea77349f449c860b
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

OpenFlow: Thúc đẩy đổi mới trong các mạng khuôn viên trường

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

Bài viết này là một ghi chú biên tập được gửi cho CCR. Bài viết CHƯA được phản biện.

Các tác giả hoàn toàn chịu trách nhiệm về nội dung kỹ thuật của bài viết này.

Có thể đăng nhận xét thông qua CCR Online.

TÓM TẮT

Bài whitepaper này đề xuất OpenFlow: một phương thức cho phép các nhà nghiên cứu chạy các giao thức thử nghiệm trên các mạng mà họ sử dụng hằng ngày. OpenFlow dựa trên một chuyển mạch Ethernet, với một bảng luồng (flow-table) nội bộ, và một giao diện được chuẩn hóa để thêm và xóa các mục nhập luồng. Mục tiêu của chúng tôi là khuyến khích các nhà cung cấp thiết bị mạng bổ sung OpenFlow vào các sản phẩm chuyển mạch của họ để triển khai trong các mạng trục khuôn viên trường đại học và các tủ đấu dây. Chúng tôi tin rằng OpenFlow là một sự thỏa hiệp thực dụng: một mặt, nó cho phép các nhà nghiên cứu chạy các thử nghiệm trên các chuyển mạch không đồng nhất theo một cách thống nhất, ở tốc độ đường truyền và với mật độ cổng cao; mặt khác, các nhà cung cấp không cần công khai cách thức hoạt động nội bộ của các chuyển mạch của họ. Ngoài việc cho phép các nhà nghiên cứu đánh giá ý tưởng của mình trong các điều kiện lưu lượng thực tế, OpenFlow có thể đóng vai trò là một thành phần hữu ích của khuôn viên trường trong các testbed quy mô lớn được đề xuất như GENI. Hai tòa nhà tại Stanford University sẽ sớm vận hành các mạng OpenFlow, sử dụng các chuyển mạch và bộ định tuyến Ethernet thương mại. Chúng tôi sẽ nỗ lực khuyến khích triển khai tại các trường khác; và chúng tôi khuyến khích bạn cân nhắc triển khai OpenFlow trong mạng của trường đại học mình.
