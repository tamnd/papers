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
content_sha256: 6d05f18eba28dcfb1f8de528c51fb01ec8ba50ad3e71b0cd11ae4981bd72bd10
translated_from: content/en/metcalfe-1976-ethernet/05_growth.md
source_content_sha256: 975fbad119581675bc88d8c988639ec071b22fc5464078cc491c3302b96eb0b1
translation_model: gpt-5
translation_run: 20260917T145710Z
glossary_version: 6
glossary_terms_sha256: 3a5b9dd3cd6211761c92d70db4c4910c364b1cae9e5e732eea77349f449c860b
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

### 5.1 Phạm vi tín hiệu {#metcalfe-1976-ethernet-s5-1 .section tag=02AC}

Có thể mở rộng một Ethernet đến một giới hạn nhất định bằng cách bổ sung các bộ thu phát và Ether. Đến một lúc nào đó, các bộ thu phát và Ether sẽ không thể truyền các tín hiệu cần thiết. *Phạm vi tín hiệu* có thể được mở rộng bằng một *bộ lặp gói tin* đơn giản, không có bộ đệm. Trong Ethernet thử nghiệm của chúng tôi, do tính đơn giản của các bộ thu phát nên Ether không thể được phân nhánh một cách thụ động, một bộ lặp đơn giản có thể nối bất kỳ số lượng *đoạn* Ether nào để làm phong phú cấu trúc liên kết đồng thời mở rộng phạm vi tín hiệu.

Chúng tôi vận hành một bộ lặp gói tin thử nghiệm gồm hai đoạn, nhưng hy vọng tránh phải phụ thuộc vào chúng. Khi phân nhánh Ether và mở rộng phạm vi tín hiệu của nó, có sự đánh đổi giữa việc sử dụng các bộ thu phát phức tạp và sử dụng các bộ lặp. Khi công suất và độ nhạy tăng lên, các bộ thu phát trở nên đắt hơn và kém tin cậy hơn. Việc đưa các bộ lặp vào một Ethernet làm cho Ether liên kết trung tâm trở nên chủ động. Sự cố của một bộ thu phát sẽ cắt đứt liên lạc của trạm sở hữu nó; sự cố của một bộ lặp sẽ phân vùng Ether, cắt đứt nhiều liên lạc.

### 5.2 Phạm vi lưu lượng {#metcalfe-1976-ethernet-s5-2 .section tag=02AD}

Có thể mở rộng một Ethernet đến một giới hạn nhất định bằng cách bổ sung Ether và các bộ lặp gói tin. Đến một lúc nào đó, Ether sẽ bận đến mức các trạm bổ sung chỉ làm chia nhỏ hơn nữa băng thông vốn đã không đủ. *Phạm vi lưu lượng* có thể được mở rộng bằng một bộ lặp lọc lưu lượng không có bộ đệm hoặc *bộ lọc gói tin*, chỉ chuyển các gói tin từ một đoạn Ether này sang đoạn Ether khác nếu trạm đích nằm trên đoạn mới. Bộ lọc gói tin cũng mở rộng phạm vi tín hiệu.

### 5.3 Phạm vi địa chỉ {#metcalfe-1976-ethernet-s5-3 .section tag=02AE}

Có thể mở rộng một Ethernet đến một giới hạn nhất định bằng cách bổ sung Ether, các bộ lặp và các bộ lọc lưu lượng. Đến một lúc nào đó sẽ có quá nhiều trạm để có thể định địa chỉ bằng các địa chỉ 8-bit của Ethernet. *Phạm vi địa chỉ* có thể được mở rộng bằng *các cổng gói tin* và các quy ước định địa chỉ bằng phần mềm mà chúng triển khai [[cerf-1974-tcpip]]. Các địa chỉ có thể được mở rộng theo hai hướng: *xuống* vào trong trạm bằng cách bổ sung các trường để xác định các cổng đích hoặc các tiến trình bên trong một trạm, và *lên* vào liên mạng bằng cách bổ sung các trường để xác định các trạm đích trên các mạng từ xa. Một cổng cũng mở rộng phạm vi lưu lượng và phạm vi tín hiệu.

Chỉ có thể có một bộ lặp hoặc bộ lọc gói tin kết nối hai đoạn Ether; một gói tin được nhiều bộ lặp lặp lại lên một đoạn sẽ gây nhiễu cho chính nó. Tuy nhiên, không có giới hạn về số lượng cổng kết nối hai đoạn; một cổng chỉ lặp lại các gói tin được định địa chỉ cho chính nó với tư cách là một trung gian. Sự cố của bộ lặp duy nhất kết nối hai đoạn sẽ phân vùng mạng; sự cố của một cổng không nhất thiết phải phân vùng mạng nếu có các đường đi qua các cổng khác giữa các đoạn.
