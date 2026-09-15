---
paper: nakamoto-2008-bitcoin
title: 'Bitcoin: A Peer-to-Peer Electronic Cash System'
authors:
  - Satoshi Nakamoto
year: 2008
venue: bitcoin.org
field: security
section: "1"
section_title: Giới thiệu
tag: "0005"
kind: section
lang: vi
source: https://bitcoin.org/bitcoin.pdf
pdf_sha256: b1674191a88ec5cdd733e4240a81803105dc412d6c6708d53ab94fc248f4f553
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 482128c474e111e79b7818132cde9efffae9c7852701875cf416259b6ab487a3
translated_from: content/en/nakamoto-2008-bitcoin/01_introduction.md
source_content_sha256: aaf1418ced3610827de9ca8753cc1e39df935e773a55e4a44250c2ef38daae71
translation_model: gpt-5
translation_run: 20260915T023027Z
glossary_version: 6
glossary_terms_sha256: 363c21723d588ca6b8032fd3e2b0aa8dc6ab225b1f9ca1b6e98d75976e8b0d0a
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Thương mại trên Internet đã gần như hoàn toàn dựa vào các tổ chức tài chính đóng vai trò là bên thứ ba đáng tin cậy để xử lý các khoản thanh toán điện tử. Mặc dù hệ thống hoạt động đủ tốt cho hầu hết các giao dịch, nó vẫn chịu những điểm yếu vốn có của mô hình dựa trên sự tin cậy. Các giao dịch hoàn toàn không thể đảo ngược thực sự không khả thi, vì các tổ chức tài chính không thể tránh việc đứng ra phân xử tranh chấp. Chi phí của việc phân xử làm tăng chi phí giao dịch, giới hạn kích thước giao dịch thực tế tối thiểu và loại bỏ khả năng thực hiện các giao dịch nhỏ mang tính ngẫu nhiên, đồng thời còn có một chi phí rộng hơn do mất khả năng thực hiện các khoản thanh toán không thể đảo ngược cho các dịch vụ không thể đảo ngược. Với khả năng đảo ngược, nhu cầu về sự tin cậy lan rộng hơn. Người bán phải cảnh giác với khách hàng của mình, gây phiền hà cho họ bằng cách yêu cầu nhiều thông tin hơn mức họ cần trong những trường hợp khác. Một tỷ lệ gian lận nhất định được chấp nhận như điều không thể tránh khỏi. Những chi phí và sự không chắc chắn trong thanh toán này có thể được tránh khi giao dịch trực tiếp bằng cách sử dụng tiền tệ vật lý, nhưng không tồn tại cơ chế nào để thực hiện thanh toán qua một kênh liên lạc mà không cần một bên đáng tin cậy.

Điều cần thiết là một hệ thống thanh toán điện tử dựa trên bằng chứng mật mã thay vì sự tin cậy, cho phép bất kỳ hai bên tự nguyện nào giao dịch trực tiếp với nhau mà không cần một bên thứ ba đáng tin cậy. Các giao dịch không khả thi về mặt tính toán để đảo ngược sẽ bảo vệ người bán khỏi gian lận, và các cơ chế ký quỹ thông thường có thể dễ dàng được triển khai để bảo vệ người mua. Trong bài báo này, chúng tôi đề xuất một giải pháp cho vấn đề chi tiêu kép bằng cách sử dụng một server dấu thời gian phân tán ngang hàng để tạo ra bằng chứng tính toán về thứ tự thời gian của các giao dịch. Hệ thống an toàn miễn là các nút trung thực cùng kiểm soát nhiều sức mạnh CPU hơn bất kỳ nhóm các nút tấn công nào hợp tác với nhau.
