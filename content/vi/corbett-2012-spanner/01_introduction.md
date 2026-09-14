---
paper: corbett-2012-spanner
title: 'Spanner: Google''s Globally-Distributed Database'
authors:
  - James C. Corbett
  - Jeffrey Dean
  - Michael Epstein
  - Andrew Fikes
  - Christopher Frost
  - J. J. Furman
  - Sanjay Ghemawat
  - Andrey Gubarev
  - Christopher Heiser
  - Peter Hochschild
year: 2012
venue: OSDI
field: databases
section: "1"
section_title: Giới thiệu
tag: 00A0
kind: section
lang: vi
source: http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.258.9924
pdf_sha256: 61875779e75f603d21aefba6d9bd9816d4dd0c18cf41089f43707249e24bbf88
pdf_pages: 1-2
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: b9ff4b4d01058714894cc21e4681f93b0b35559b4a90cf4abdd144b3366f763b
translated_from: content/en/corbett-2012-spanner/01_introduction.md
source_content_sha256: 2c2fa58420db751e797b5e29bceffa251f9a575283d1b32c0c4fe3227b8369ce
translation_model: gpt-5
translation_run: 20260914T201546Z
glossary_version: 6
glossary_terms_sha256: a534ae50d60bff0e03804fd3c150e37d1876484531ab87df9c72dc4d0c455eb2
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Spanner là một cơ sở dữ liệu có khả năng mở rộng, phân tán toàn cầu, được thiết kế, xây dựng và triển khai tại Google. Ở mức trừu tượng cao nhất, nó là một cơ sở dữ liệu phân mảnh dữ liệu trên nhiều tập hợp máy trạng thái Paxos [[lamport-1998-paxos]] tại các datacenter trải rộng khắp thế giới. Sao chép được sử dụng để cung cấp tính sẵn sàng toàn cầu và tính cục bộ theo địa lý; các máy khách tự động chuyển đổi dự phòng giữa các bản sao. Spanner tự động phân mảnh lại dữ liệu trên các máy khi lượng dữ liệu hoặc số lượng server thay đổi, và nó tự động di chuyển dữ liệu giữa các máy (kể cả giữa các datacenter) để cân bằng tải và phản ứng với các sự cố. Spanner được thiết kế để mở rộng tới hàng triệu máy trên hàng trăm datacenter và hàng nghìn tỷ hàng cơ sở dữ liệu.

Các ứng dụng có thể sử dụng Spanner để đạt tính sẵn sàng cao, ngay cả khi xảy ra các thảm họa tự nhiên trên diện rộng, bằng cách sao chép dữ liệu của chúng trong phạm vi hoặc thậm chí giữa các lục địa. Khách hàng ban đầu của chúng tôi là F1 [35], một bản viết lại của backend quảng cáo của Google. F1 sử dụng năm bản sao trải rộng trên Hoa Kỳ. Hầu hết các ứng dụng khác có lẽ sẽ sao chép dữ liệu của chúng trên 3 đến 5 datacenter trong một vùng địa lý, nhưng với các chế độ sự cố tương đối độc lập. Nghĩa là, hầu hết các ứng dụng sẽ chọn độ trễ thấp hơn thay vì tính sẵn sàng cao hơn, miễn là chúng có thể chịu được 1 hoặc 2 sự cố datacenter.

Trọng tâm chính của Spanner là quản lý dữ liệu được sao chép xuyên datacenter, nhưng chúng tôi cũng đã dành rất nhiều thời gian để thiết kế và triển khai các tính năng cơ sở dữ liệu quan trọng trên nền tảng hạ tầng hệ thống phân tán của mình. Mặc dù nhiều dự án sử dụng Bigtable [9] một cách hiệu quả, chúng tôi cũng liên tục nhận được các phàn nàn từ người dùng rằng Bigtable có thể khó sử dụng đối với một số loại ứng dụng: những ứng dụng có lược đồ phức tạp, thay đổi theo thời gian, hoặc những ứng dụng muốn có tính nhất quán mạnh trong sự hiện diện của sao chép trên diện rộng. (Các nhận định tương tự đã được các tác giả khác đưa ra [37].) Nhiều ứng dụng tại Google đã chọn sử dụng Megastore [5] vì mô hình dữ liệu bán quan hệ và hỗ trợ sao chép đồng bộ của nó, mặc dù thông lượng ghi tương đối kém. Do đó, Spanner đã phát triển từ một kho lưu trữ khóa-giá trị có phiên bản giống Bigtable thành một cơ sở dữ liệu đa phiên bản theo thời gian. Dữ liệu được lưu trữ trong các bảng bán quan hệ có lược đồ; dữ liệu được tạo phiên bản, và mỗi phiên bản được tự động gán dấu thời gian với thời điểm xác nhận của nó; các phiên bản dữ liệu cũ chịu sự điều chỉnh của các chính sách thu gom rác có thể cấu hình; và các ứng dụng có thể đọc dữ liệu tại các dấu thời gian cũ. Spanner hỗ trợ các giao dịch mục đích chung, và cung cấp một ngôn ngữ truy vấn dựa trên SQL.

Là một cơ sở dữ liệu phân tán toàn cầu, Spanner cung cấp một số tính năng thú vị. Thứ nhất, các cấu hình sao chép cho dữ liệu có thể được các ứng dụng điều khiển động với mức độ chi tiết cao. Các ứng dụng có thể chỉ định các ràng buộc để kiểm soát datacenter nào chứa dữ liệu nào, dữ liệu cách người dùng bao xa (để kiểm soát độ trễ đọc), các bản sao cách nhau bao xa (để kiểm soát độ trễ ghi), và có bao nhiêu bản sao được duy trì (để kiểm soát độ bền, tính sẵn sàng và hiệu năng đọc). Dữ liệu cũng có thể được hệ thống di chuyển động và minh bạch giữa các datacenter để cân bằng việc sử dụng tài nguyên trên các datacenter. Thứ hai, Spanner có hai tính năng khó triển khai trong một cơ sở dữ liệu phân tán: nó cung cấp các thao tác đọc và ghi nhất quán bên ngoài [16], và các thao tác đọc nhất quán toàn cục trên cơ sở dữ liệu tại một dấu thời gian. Các tính năng này cho phép Spanner hỗ trợ sao lưu nhất quán, các lần thực thi MapReduce nhất quán [12], và các cập nhật lược đồ nguyên tử, tất cả ở quy mô toàn cầu, ngay cả khi có các giao dịch đang diễn ra.

Các tính năng này được hỗ trợ bởi thực tế rằng Spanner gán các dấu thời gian xác nhận có ý nghĩa toàn cầu cho các giao dịch, mặc dù các giao dịch có thể được phân tán. Các dấu thời gian phản ánh thứ tự tuần tự hóa. Ngoài ra, thứ tự tuần tự hóa thỏa mãn tính nhất quán bên ngoài (hoặc tương đương, tính tuyến tính hóa [20]): nếu một giao dịch $T_1$ xác nhận trước khi một giao dịch khác $T_2$ bắt đầu, thì dấu thời gian xác nhận của $T_1$ nhỏ hơn của $T_2$. Spanner là hệ thống đầu tiên cung cấp các đảm bảo như vậy ở quy mô toàn cầu.

Yếu tố then chốt cho các tính chất này là một API TrueTime mới và phần triển khai của nó. API này trực tiếp phơi bày sự không chắc chắn của đồng hồ, và các đảm bảo trên các dấu thời gian của Spanner phụ thuộc vào các cận mà phần triển khai cung cấp. Nếu độ không chắc chắn lớn, Spanner sẽ giảm tốc độ để chờ hết khoảng không chắc chắn đó. Phần mềm quản lý cụm của Google cung cấp một triển khai của API TrueTime. Triển khai này giữ cho độ không chắc chắn nhỏ (thường nhỏ hơn 10ms) bằng cách sử dụng nhiều tham chiếu đồng hồ hiện đại (GPS và đồng hồ nguyên tử).

Section 2 mô tả cấu trúc triển khai của Spanner, tập tính năng của nó, và các quyết định kỹ thuật đã đưa vào thiết kế của chúng. Section 3 mô tả API TrueTime mới của chúng tôi và phác thảo phần triển khai của nó. Section 4 mô tả cách Spanner sử dụng TrueTime để triển khai các giao dịch phân tán nhất quán bên ngoài, các giao dịch chỉ đọc không khóa, và các cập nhật lược đồ nguyên tử. Section 5 cung cấp một số phép đo chuẩn về hiệu năng của Spanner và hành vi của TrueTime, đồng thời thảo luận về các kinh nghiệm của F1. Sections 6, 7, and 8 mô tả công việc liên quan và trong tương lai, đồng thời tóm tắt các kết luận của chúng tôi.
