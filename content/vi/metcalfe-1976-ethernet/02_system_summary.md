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
content_sha256: e01ba2e5bbad34b73b89dc972da6ab25679032524eb6f6ce502a7a04425a8316
translated_from: content/en/metcalfe-1976-ethernet/02_system_summary.md
source_content_sha256: 9d6d22309ed68c81951058e28f515a852019bca26bb203bca00c23e7a9e3f751
translation_model: gpt-5
translation_run: 20260918T110147Z
glossary_version: 7
glossary_terms_sha256: 5bfb74d0e4b3e9a8237f78ceae59e221549684c174791655271c5455f7fd5e4e
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Ethernet là một hệ thống dành cho giao tiếp cục bộ giữa các trạm tính toán. Ethernet thử nghiệm của chúng tôi sử dụng các cáp đồng trục có điểm nối để truyền các gói tin dữ liệu số có độ dài thay đổi giữa, ví dụ, các máy tính mini cá nhân, các cơ sở in ấn, các thiết bị lưu trữ file lớn, các trạm sao lưu băng từ, các máy tính trung tâm lớn hơn và các thiết bị truyền thông đường dài hơn.

Cơ sở giao tiếp dùng chung, một Ether phân nhánh, là thụ động. Giao diện Ethernet của một trạm kết nối theo kiểu bit nối tiếp thông qua một cáp giao diện tới một bộ thu phát, bộ này lần lượt nối vào Ether đang truyền. Một gói tin được phát quảng bá lên Ether, được tất cả các trạm nghe thấy và được các đích sao chép từ Ether bằng cách lựa chọn nó theo các bit địa chỉ đứng đầu của gói tin. Đây là chuyển mạch gói tin quảng bá và cần được phân biệt với chuyển mạch gói tin lưu trữ và chuyển tiếp, trong đó việc định tuyến được thực hiện bởi các phần tử xử lý trung gian. Để đáp ứng các yêu cầu của sự phát triển, một Ethernet có thể được mở rộng bằng cách sử dụng các bộ lặp gói tin để tái tạo tín hiệu, các bộ lọc gói tin để bản địa hóa lưu lượng và các cổng gói tin để mở rộng địa chỉ liên mạng.

Điều khiển được phân tán hoàn toàn giữa các trạm, với việc truyền các gói tin được phối hợp thông qua phân xử thống kê. Các lần truyền do một trạm khởi tạo sẽ trì hoãn trước bất kỳ lần truyền nào có thể đã đang diễn ra. Khi đã bắt đầu, nếu phát hiện sự can thiệp với các gói tin khác, một lần truyền sẽ bị hủy bỏ và được trạm nguồn lập lịch lại. Sau một khoảng thời gian truyền không có can thiệp nhất định, một gói tin được tất cả các trạm nghe thấy và sẽ chạy đến khi hoàn thành mà không bị can thiệp. Các bộ điều khiển Ethernet trong các trạm xảy ra va chạm mỗi bộ tạo ra các khoảng thời gian truyền lại ngẫu nhiên để tránh các va chạm lặp lại. Giá trị trung bình của các khoảng thời gian truyền lại của một gói tin được điều chỉnh như một hàm của lịch sử va chạm để giữ mức sử dụng Ether gần với mức tối ưu khi tải mạng thay đổi.

Ngay cả khi được truyền mà không có can thiệp do nguồn phát hiện, một gói tin vẫn có thể không đến được đích mà không có lỗi; do đó, các gói tin được phân phối *chỉ với xác suất cao*. Các trạm yêu cầu tỷ lệ lỗi dư thấp hơn mức được cung cấp bởi cơ chế vận chuyển gói tin Ethernet cơ bản phải tuân theo các giao thức gói tin được thỏa thuận lẫn nhau.
