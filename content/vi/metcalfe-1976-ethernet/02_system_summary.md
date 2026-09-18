---
paper: metcalfe-1976-ethernet
title: 'Ethernet: Distributed Packet Switching for Local Computer Networks'
authors:
  - Robert M. Metcalfe
  - David R. Boggs
year: 1976
venue: Communications of the ACM
field: networks
section: "2"
section_title: Tóm tắt hệ thống
tag: "0298"
kind: section
lang: vi
source: https://www.cl.cam.ac.uk/teaching/0809/DigiCommI/metcalfe1976ethernet.pdf
pdf_sha256: e1e9d67146a1d0955a39b4fbb8e2951d6cefb4f7231a01acb9c78852280da227
pdf_pages: "2"
extraction: vision
extraction_model: gpt-5
content_sha256: a8f1ffadaf7ee03b1365e82fe464a07640e8b2fb8fd3e53a0878b59890da1995
translated_from: content/en/metcalfe-1976-ethernet/02_system_summary.md
source_content_sha256: 9d6d22309ed68c81951058e28f515a852019bca26bb203bca00c23e7a9e3f751
translation_model: gpt-5
translation_run: 20260917T145710Z
glossary_version: 6
glossary_terms_sha256: 3a5b9dd3cd6211761c92d70db4c4910c364b1cae9e5e732eea77349f449c860b
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Ethernet là một hệ thống truyền thông cục bộ giữa các trạm tính toán. Ethernet thử nghiệm của chúng tôi sử dụng các cáp đồng trục có các điểm đấu nối để truyền các gói tin dữ liệu số có độ dài thay đổi giữa, chẳng hạn, các máy vi tính cá nhân, các thiết bị in, các thiết bị lưu trữ file lớn, các trạm sao lưu băng từ, các máy tính trung tâm lớn hơn và các thiết bị truyền thông đường dài hơn.

Phương tiện truyền thông dùng chung, một Ether phân nhánh, là thụ động. Giao diện Ethernet của một trạm kết nối theo kiểu nối tiếp từng bit qua một cáp giao diện tới một bộ thu phát, rồi bộ thu phát này đấu nối vào Ether đang truyền. Một gói tin được phát quảng bá lên Ether, được tất cả các trạm nhận biết, và được các đích sao chép từ Ether sau khi lựa chọn nó dựa trên các bit địa chỉ ở đầu gói tin. Đây là chuyển mạch gói tin quảng bá và cần được phân biệt với chuyển mạch gói tin lưu-và-chuyển-tiếp, trong đó việc định tuyến được thực hiện bởi các phần tử xử lý trung gian. Để đáp ứng nhu cầu mở rộng, một Ethernet có thể được mở rộng bằng các bộ lặp gói tin để tái tạo tín hiệu, các bộ lọc gói tin để giới hạn lưu lượng và các cổng gói tin để mở rộng địa chỉ liên mạng.

Việc điều khiển được phân tán hoàn toàn giữa các trạm, với các quá trình truyền gói tin được phối hợp thông qua phân xử thống kê. Các quá trình truyền do một trạm khởi tạo sẽ nhường cho bất kỳ quá trình nào có thể đã đang diễn ra. Khi đã bắt đầu, nếu phát hiện nhiễu với các gói tin khác, quá trình truyền sẽ bị hủy và được trạm nguồn lập lịch lại. Sau một khoảng thời gian truyền không bị nhiễu nhất định, một gói tin được tất cả các trạm nhận biết và sẽ truyền đến hoàn tất mà không bị nhiễu. Các bộ điều khiển Ethernet tại các trạm va chạm đều tạo ra các khoảng thời gian truyền lại ngẫu nhiên để tránh các va chạm lặp lại. Giá trị trung bình của các khoảng thời gian truyền lại của một gói tin được điều chỉnh như một hàm của lịch sử va chạm nhằm giữ mức sử dụng Ether gần mức tối ưu khi tải mạng thay đổi.

Ngay cả khi được truyền mà không có nhiễu được nguồn phát hiện, một gói tin vẫn có thể không đến được đích mà không có lỗi; do đó, các gói tin chỉ được phân phối *với xác suất cao*. Các trạm yêu cầu tỷ lệ lỗi còn lại thấp hơn mức mà cơ chế truyền tải gói tin Ethernet thuần túy cung cấp phải tuân theo các giao thức gói tin được thỏa thuận lẫn nhau.
