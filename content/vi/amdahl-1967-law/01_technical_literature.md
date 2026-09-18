---
paper: amdahl-1967-law
title: Validity of the Single Processor Approach to Achieving Large Scale Computing Capabilities
authors:
  - Gene M. Amdahl
year: 1967
venue: AFIPS Spring Joint Computer Conference
field: architecture
section_title: Văn học Kỹ thuật
kind: section
lang: vi
source: https://www3.cs.stonybrook.edu/~rezaul/Spring-2012/CSE613/reading/Amdahl-1967.pdf
pdf_sha256: 81a363deb884ca23e495280eb9229df1064b4b3f79d662f270be35b50bea5318
pdf_pages: "2"
extraction: native
extraction_model: pdftotext version 24.02.0
content_sha256: 4a89db7c668e8b4ff5025d995c16d72a73c0e3c5bbfa3f13d23fd7176e97a8e3
translated_from: content/en/amdahl-1967-law/01_technical_literature.md
source_content_sha256: 9a9a7ba3d010cc0e5c81bd794c16943b6b3cadc8ae51ada02835f44ef45c0796
translation_model: gpt-5
translation_run: 20260918T153717Z
glossary_version: 7
glossary_terms_sha256: cb514473400f65abfd1e5d09e5f82163f246175d67293cbba8eac7dbb7d7b890
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

ảnh hưởng của những bất thường này đối với hiệu năng thực tế của một thiết bị xử lý song song, so với hiệu năng của nó trên một sự trừu tượng hóa đơn giản hóa và được chuẩn hóa của bài toán, dẫn đến sự suy giảm vào khoảng từ một nửa đến một bậc độ lớn.

Để tổng kết các ảnh hưởng của công việc quản lý dữ liệu và của những bất thường của bài toán, tác giả đã so sánh ba tổ chức máy khác nhau liên quan đến lượng phần cứng xấp xỉ bằng nhau. Máy A có ba mươi hai đơn vị thực thi số học được điều khiển bởi một luồng lệnh duy nhất. Máy B có các đơn vị thực thi số học đường ống với tối đa ba phép toán chồng lấp trên các vectơ gồm tám phần tử. Máy C có cùng các đơn vị thực thi đường ống, nhưng việc khởi tạo các phép toán riêng lẻ với cùng tốc độ như Máy B cho phép các phép toán trên phần tử vectơ. Hiệu năng của ba máy này được biểu diễn trong Hình I như một hàm của phần tỷ lệ số lượng lệnh cho phép tính song song. Vùng hoạt động có khả năng xảy ra được tập trung quanh một điểm tương ứng với 25% chi phí phụ trội quản lý dữ liệu và l0% các phép toán của bài toán bị buộc phải thực hiện tuần tự.

Hiệu năng lịch sử so với chi phí của máy tính đã được Giáo sư Knight nghiên cứu rất kỹ lưỡng. Dữ liệu được phân tích cẩn thận mà ông trình bày không chỉ phản ánh thời gian thực thi cho các phép toán số học và chi phí của cấu hình tối thiểu được khuyến nghị. Ông bao gồm các ảnh hưởng của dung lượng bộ nhớ, sự chồng lấp đầu vào-đầu ra đã trải nghiệm, và các khả năng chức năng đặc biệt. Đường khớp thống kê tốt nhất thu được tương ứng với hiệu năng tỷ lệ với bình phương của chi phí ở bất kỳ mức công nghệ nào. Kết quả này hỗ trợ rất hiệu quả cho “Grosch’s Law” thường được viện dẫn. Sử dụng phân tích này, có thể lập luận rằng nếu

gấp đôi lượng phần cứng được khai thác trong một hệ thống đơn lẻ, ta có thể kỳ vọng thu được gấp bốn lần hiệu năng. Khó khăn duy nhất liên quan đến việc biết cách khai thác phần cứng bổ sung này. Tại bất kỳ thời điểm nào, rất khó dự đoán cách các nút thắt trước đây trong một máy tính tuần tự sẽ được khắc phục một cách hiệu quả. Nếu điều đó dễ dàng, chúng đã không còn là các nút thắt. Đúng là theo các ví dụ lịch sử, những trở ngại liên tiếp đã được vượt qua, vì vậy thích hợp để trích dẫn Mục sư Adam Clayton Powell-"Keep the faith, baby!" Nếu thay vào đó quyết định cải thiện hiệu năng bằng cách đặt hai bộ xử lý cạnh nhau với bộ nhớ dùng chung, ta sẽ có xấp xỉ 2.2 lần lượng phần cứng. Hai phần mười bổ sung trong phần cứng thực hiện việc chuyển mạch crossbar cho việc chia sẻ. Hiệu năng đạt được kết quả sẽ vào khoảng 1.8. Con số sau được suy ra từ giả định rằng mỗi bộ xử lý sử dụng một nửa số bộ nhớ trong khoảng một nửa thời gian. Các xung đột bộ nhớ phát sinh trong hệ thống dùng chung sẽ kéo dài việc thực thi một trong hai phép toán thêm một phần tư thời gian thực thi. Kết quả ròng là sự suy giảm hiệu năng trên chi phí xuống còn 0.8 thay vì cải thiện lên 2.0 đối với bộ xử lý đơn lớn hơn.

Phân tích so sánh với các bộ xử lý kết hợp ít dễ dàng và hiển nhiên hơn nhiều. Trong một số điều kiện nhất định của các định dạng đều đặn, có một cách tiếp cận khá trực tiếp. Xét một bộ xử lý kết hợp được thiết kế để nhận dạng mẫu, trong đó các quyết định bên trong từng phần tử được chuyển tiếp đến một tập hợp các phần tử khác. Trong thiết kế bộ xử lý kết hợp, các phần tử nhận sẽ có một tập hợp các địa chỉ nguồn nhận biết bằng các kỹ thuật kết hợp liệu nó có nhận quyết định của phần tử hiện đang đưa ra quyết định hay không. Để tạo ra một bộ xử lý không kết hợp chuyên dụng tương ứng, ta sẽ xem một phần tử nhận và các địa chỉ nguồn của nó như một lệnh, với các quyết định nhị phân được duy trì trong các thanh ghi. Xét việc sử dụng bộ nhớ màng mỏng, một chu kỳ kết hợp sẽ dài hơn một chu kỳ đọc không phá hủy. Trong công nghệ như vậy, bộ xử lý không kết hợp chuyên dụng có thể được kỳ vọng cần khoảng một phần tư số chu kỳ bộ nhớ so với phiên bản kết hợp và chỉ khoảng một phần sáu thời gian. Các con số này được tính toán trên toàn bộ nhiệm vụ nhận dạng, với các tỷ lệ hơi khác nhau trong từng giai đoạn. Ở đây không đưa ra một khẳng định chung, mà chỉ cho rằng mỗi yêu cầu cần được khảo sát từ cả hai cách tiếp cận.

Sơ đồ ở trên minh họa “Amdahl’s Law” cho thấy một máy có mức độ song song cao gặp khó khăn hơn trong việc đạt được một phần hợp lý của hiệu năng đỉnh do thành phần tuần tự của tính toán đã cho và chi phí phụ trội của sự phối hợp (ví dụ: đồng bộ hóa) giữa các bộ xử lý. Giả sử một bài toán có kích thước cố định, Amdahl phỏng đoán rằng hầu hết các chương trình sẽ yêu cầu ít nhất 25% tính toán phải là tuần tự (chỉ một lệnh được thực thi tại một thời điểm), với chi phí phụ trội do sự phối hợp liên bộ xử lý trung bình là 10%. Các đường cong cho thấy càng phụ thuộc nhiều vào tính song song để đạt hiệu năng, hệ thống càng có khả năng chậm hơn trong trường hợp có khả năng xảy ra, 65%. Đường cong thấp nhất (A) biểu diễn bộ xử lý SIMD rộng 32, và đường cong trên cùng (C) dành cho bộ xử lý vectơ đã sửa đổi. Các bài toán được mở rộng làm giảm thành phần tuần tự và chi phí phụ trội phối hợp xuống mức không đáng kể, khiến số lượng lớn bộ xử lý trở nên rất hiệu quả trong những trường hợp đó. Justin Rattner, Intel Senior Fellow, justin.rattner@intel.com, July 2007.

20 IEEE SSCS NEWS

Summer 2007
