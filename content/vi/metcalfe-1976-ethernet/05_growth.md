---
paper: metcalfe-1976-ethernet
title: 'Ethernet: Distributed Packet Switching for Local Computer Networks'
authors:
  - Robert M. Metcalfe
  - David R. Boggs
year: 1976
venue: Communications of the ACM
field: networks
section: "5"
section_title: Tăng trưởng
tag: 02AB
kind: section
lang: vi
source: https://www.cl.cam.ac.uk/teaching/0809/DigiCommI/metcalfe1976ethernet.pdf
pdf_sha256: e1e9d67146a1d0955a39b4fbb8e2951d6cefb4f7231a01acb9c78852280da227
pdf_pages: "6"
extraction: vision
extraction_model: gpt-5
content_sha256: 16ff395e6e77d605837529fe75d580a3972b57bd64397bdb877eb456ac0c3376
translated_from: content/en/metcalfe-1976-ethernet/05_growth.md
source_content_sha256: 975fbad119581675bc88d8c988639ec071b22fc5464078cc491c3302b96eb0b1
translation_model: gpt-5
translation_run: 20260918T110147Z
glossary_version: 7
glossary_terms_sha256: 5bfb74d0e4b3e9a8237f78ceae59e221549684c174791655271c5455f7fd5e4e
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

### 5.1 Phạm vi tín hiệu {#metcalfe-1976-ethernet-s5-1 .section tag=02AC}

Có thể mở rộng một Ethernet đến một mức nhất định bằng cách thêm các bộ thu phát và Ether. Tại một thời điểm nào đó, các bộ thu phát và Ether sẽ không thể mang các tín hiệu cần thiết. *Phạm vi tín hiệu* có thể được mở rộng bằng một *bộ lặp gói tin* đơn giản không có bộ đệm. Trong Ethernet thử nghiệm của chúng tôi, nơi do sự đơn giản của bộ thu phát mà Ether không thể được phân nhánh một cách thụ động, một bộ lặp đơn giản có thể nối bất kỳ số lượng *phân đoạn* Ether nào để làm phong phú cấu trúc liên kết trong khi mở rộng phạm vi tín hiệu.

Chúng tôi vận hành một bộ lặp gói tin hai phân đoạn thử nghiệm, nhưng hy vọng tránh phụ thuộc vào chúng. Trong việc phân nhánh Ether và mở rộng phạm vi tín hiệu của nó, có sự đánh đổi giữa việc sử dụng các bộ thu phát tinh vi và sử dụng các bộ lặp. Với công suất và độ nhạy tăng lên, các bộ thu phát trở nên đắt hơn và kém tin cậy hơn. Việc đưa các bộ lặp vào một Ethernet làm cho Ether kết nối trung tâm trở nên chủ động. Sự cố của một bộ thu phát sẽ cắt đứt các liên lạc của chủ sở hữu nó; sự cố của một bộ lặp sẽ phân vùng Ether, cắt đứt nhiều liên lạc.

### 5.2 Phạm vi lưu lượng {#metcalfe-1976-ethernet-s5-2 .section tag=02AD}

Có thể mở rộng một Ethernet đến một mức nhất định bằng cách thêm Ether và các bộ lặp gói tin. Tại một thời điểm nào đó, Ether sẽ bận đến mức các trạm bổ sung chỉ còn chia nhỏ hơn nữa băng thông vốn đã không đủ. *Phạm vi lưu lượng* có thể được mở rộng bằng một bộ lặp lọc lưu lượng không có bộ đệm hoặc *bộ lọc gói tin*, bộ này chỉ chuyển các gói tin từ một phân đoạn Ether sang phân đoạn Ether khác nếu trạm đích nằm trên phân đoạn mới. Một bộ lọc gói tin cũng mở rộng phạm vi tín hiệu.

### 5.3 Phạm vi địa chỉ {#metcalfe-1976-ethernet-s5-3 .section tag=02AE}

Có thể mở rộng một Ethernet đến một mức nhất định bằng cách thêm Ether, các bộ lặp và các bộ lọc lưu lượng. Tại một thời điểm nào đó sẽ có quá nhiều trạm để được định địa chỉ bằng các địa chỉ 8-bit của Ethernet. *Phạm vi địa chỉ* có thể được mở rộng bằng *các cổng gói tin* và các quy ước định địa chỉ phần mềm mà chúng triển khai [[cerf-1974-tcpip]]. Địa chỉ có thể được mở rộng theo hai hướng: *xuống* vào trong trạm bằng cách thêm các trường để xác định các cổng đích hoặc các tiến trình bên trong một trạm, và *lên* vào trong liên mạng bằng cách thêm các trường để xác định các trạm đích trên các mạng từ xa. Một cổng cũng mở rộng các phạm vi lưu lượng và tín hiệu.

Chỉ có thể có một bộ lặp hoặc bộ lọc gói tin kết nối hai phân đoạn Ether; một gói tin được lặp lại vào một phân đoạn bởi nhiều bộ lặp sẽ gây nhiễu với chính nó. Tuy nhiên, không có giới hạn về số lượng cổng kết nối hai phân đoạn; một cổng chỉ lặp lại các gói tin được định địa chỉ cho chính nó như một trung gian. Sự cố của bộ lặp duy nhất kết nối hai phân đoạn sẽ phân vùng mạng; sự cố của một cổng không nhất thiết phải phân vùng mạng nếu có các đường đi qua các cổng khác giữa các phân đoạn.
