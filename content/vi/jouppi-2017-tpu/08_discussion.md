---
paper: jouppi-2017-tpu
title: In-Datacenter Performance Analysis of a Tensor Processing Unit
authors:
  - Norman P. Jouppi
  - Cliff Young
  - Nishant Patil
  - David Patterson
  - Gaurav Agrawal
  - Raminder Bajwa
  - Sarah Bates
  - Suresh Bhatia
  - Nan Boden
  - Al Borchers
year: 2017
venue: ISCA
field: architecture
section: "8"
section_title: Thảo luận
tag: "0197"
kind: section
lang: vi
source: arxiv:1704.04760
pdf_sha256: 19793e4ae1486630ac45a12facabc0e80609dd679db8ca7a3a040f8bf0d8e0be
pdf_pages: 12-13
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 7f4c21cc5f1361171dffe7eecadeb1259994a4826bbca4df76e7695d1b29cddc
translated_from: content/en/jouppi-2017-tpu/08_discussion.md
source_content_sha256: 810b2ad30140f38b5b482dc3ef7733422e761e484d8d815b35b254fe1c37190e
translation_model: gpt-5
translation_run: 20260914T201546Z
glossary_version: 6
glossary_terms_sha256: 1f83355a83baacb04f1185b8bd47b133f28d2f764f5d7ae919d5d9d0d7e083ee
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
roundtrip: differs-in-wording
roundtrip_run: 20260914T214350Z
---

Phần này tuân theo kiểu bác bỏ của [Hen18] đối với các ngụy biện và cạm bẫy.
• *Ngụy biện*: *Các ứng dụng suy luận NN trong các datacenter coi trọng thông lượng ngang với thời gian phản hồi.*
Chúng tôi rất ngạc nhiên khi các nhà phát triển của mình có những yêu cầu mạnh mẽ về thời gian phản hồi, vì một số người đã đề xuất vào năm 2014 rằng kích thước lô sẽ đủ lớn để TPU đạt hiệu năng cực đại hoặc rằng các yêu cầu về độ trễ sẽ không quá chặt chẽ. Một ứng dụng thúc đẩy là xử lý ảnh ngoại tuyến, và trực giác là nếu các dịch vụ tương tác cũng muốn sử dụng TPU, hầu hết chúng sẽ chỉ tích lũy các lô lớn hơn. Ngay cả các nhà phát triển của một ứng dụng vào năm 2014 quan tâm đến thời gian phản hồi (LSTM1) cũng nói rằng giới hạn là 10 ms vào năm 2014, nhưng đã giảm xuống còn 7 ms khi họ thực sự chuyển nó sang TPU. Mong muốn bất ngờ đối với TPU của nhiều dịch vụ như vậy kết hợp với tác động và sự ưu tiên dành cho thời gian phản hồi thấp đã thay đổi phương trình, với các nhà viết ứng dụng thường chọn giảm độ trễ thay vì chờ tích lũy các lô lớn hơn. May mắn thay, TPU có một mô hình thực thi đơn giản và có thể lặp lại để giúp đáp ứng các mục tiêu về thời gian phản hồi của các dịch vụ tương tác và có thông lượng cực đại cao đến mức ngay cả các kích thước lô nhỏ cũng tạo ra hiệu năng cao hơn các CPU và GPU đương thời.
• *Ngụy biện*: *Kiến trúc GPU K80 là sự phù hợp tốt cho suy luận NN.*
GPU theo truyền thống được xem là các kiến trúc có thông lượng cao dựa vào DRAM băng thông cao và hàng nghìn luồng để đạt được mục tiêu của chúng. Góc nhìn này giúp giải thích tại sao K80 chỉ nhanh hơn một chút khi suy luận so với Haswell và chậm hơn nhiều so với TPU. Các thế hệ kế nhiệm của K80 chắc chắn sẽ bao gồm các tối ưu hóa để cải thiện hiệu năng suy luận cực đại, nhưng do cách tiếp cận kiến trúc hướng tới thông lượng của chúng, việc GPU đáp ứng các giới hạn độ trễ nghiêm ngặt có thể khó khăn hơn. Và như Section 7 chỉ ra, vẫn còn nhiều dư địa để cải thiện TPU, vì vậy đây không phải là một mục tiêu dễ dàng.

• *Cạm bẫy: Các kiến trúc sư đã bỏ qua các tác vụ NN quan trọng.*
Chúng tôi hài lòng với sự chú ý mà cộng đồng kiến trúc đang dành cho NN: 15% các bài báo tại ISCA 2016 nói về các bộ tăng tốc phần cứng cho NN [Alb16] [Che16a][Chi16][Han16][Kim16][LiK16][Liu16][Rea16] [Sha16]! Tuy nhiên, cả chín bài báo đều xem xét CNN, và chỉ hai bài đề cập đến các NN khác. CNN phức tạp hơn MLP và nổi bật trong các cuộc thi NN [Rus15], điều này có thể giải thích sức hấp dẫn của chúng, nhưng chúng chỉ chiếm khoảng 5% tải công việc NN trong datacenter của chúng tôi. Mặc dù CNN có thể phổ biến trong các thiết bị biên, khối lượng các mô hình tích chập vẫn chưa bắt kịp MLP và LSTM trong datacenter. Chúng tôi hy vọng các kiến trúc sư sẽ cố gắng tăng tốc MLP và LSTM với ít nhất sự nhiệt tình tương đương.
• *Cạm bẫy: Đối với phần cứng NN, Inferences Per Second (IPS) là một chỉ số hiệu năng tổng hợp không chính xác.*
Kết quả của chúng tôi cho thấy IPS là một bản tóm tắt hiệu năng tổng thể kém cho phần cứng NN, vì nó đơn giản là nghịch đảo của độ phức tạp của suy luận điển hình trong ứng dụng (ví dụ: số lượng, kích thước và kiểu của các lớp NN). Ví dụ, TPU chạy MLP1 4 lớp ở 360,000 IPS nhưng CNN1 89 lớp chỉ ở 4,700 IPS, vì vậy IPS của TPU thay đổi 75X! Do đó, việc sử dụng IPS làm chỉ số tốc độ duy nhất là *gây hiểu lầm nhiều hơn nữa* đối với các bộ tăng tốc NN so với việc MIPS hoặc FLOPS là đối với các bộ xử lý thông thường [Hen18], vì vậy IPS thậm chí còn nên bị xem nhẹ hơn. Để so sánh các máy NN tốt hơn, chúng ta cần một bộ phép đo chuẩn được viết ở mức cao để chuyển nó sang nhiều kiến trúc NN khác nhau. Fathom là một nỗ lực mới đầy hứa hẹn cho một bộ phép đo chuẩn như vậy [Ado16].
• *Ngụy biện: Kết quả GPU K80 sẽ tốt hơn nhiều nếu bật chế độ Boost.*
Bỏ qua tác động tiêu cực của chế độ Boost của K80 lên TCO (Section 3), chúng tôi đã đo nó trên LSTM1. Chế độ Boost tăng tốc độ xung nhịp lên hệ số tối đa 1.6—từ 560 đến 875 MHz—làm tăng hiệu năng 1.4X, nhưng nó cũng tăng công suất lên 1.3X. Mức tăng ròng về hiệu năng/Watt là 1.1X, và do đó đối với LSTM1, chế độ boost sẽ có tác động nhỏ đến phân tích tốc độ năng lượng của chúng tôi.
• *Ngụy biện: Kết quả CPU và GPU sẽ tương đương với TPU nếu chúng ta sử dụng chúng hiệu quả hơn hoặc so sánh với các phiên bản mới hơn.*
Ban đầu chúng tôi có kết quả 8-bit chỉ cho một DNN trên CPU, do lượng công việc đáng kể cần thiết để sử dụng hỗ trợ số nguyên AVX2 một cách hiệu quả. Lợi ích là ~3.5X. Việc trình bày tất cả kết quả CPU ở dạng dấu phẩy động ít gây nhầm lẫn hơn (và tốn ít không gian hơn), thay vì có một ngoại lệ với roofline riêng của nó. Nếu tất cả DNN có mức tăng tốc tương tự, tỷ lệ hiệu năng/Watt sẽ giảm từ 41-83X xuống 12-24X. GPU datacenter P40 mới 16-nm, 1.5GHz, 250W có thể thực hiện 47 Tera 8-bit ops/sec, nhưng không có sẵn vào đầu năm 2015, nên không cùng thời với ba nền tảng của chúng tôi. Chúng tôi cũng không thể biết phần tỷ lệ của đỉnh P40 được cung cấp trong các giới hạn thời gian cứng nhắc của mình. Nếu chúng tôi so sánh các chip mới hơn, Section 7 cho thấy chúng tôi có thể tăng gấp ba hiệu năng của TPU 28-nm, 0.7GHz, 40W chỉ bằng cách sử dụng bộ nhớ GDDR5 của K80 (với chi phí thêm 10W).
• *Cạm bẫy: Các bộ đếm hiệu năng được thêm vào như một ý nghĩ sau đối với phần cứng NN.*
TPU có 106 bộ đếm hiệu năng, và nếu có điều gì thì chúng tôi muốn có thêm một vài bộ nữa (xem Table 3). Lý do tồn tại của các bộ tăng tốc NN là hiệu năng, và còn quá sớm trong quá trình phát triển của chúng để có trực giác tốt về những gì đang diễn ra.
• *Ngụy biện: Sau hai năm tinh chỉnh phần mềm, con đường duy nhất còn lại để tăng hiệu năng TPU là nâng cấp phần cứng.*
Hiệu năng của CNN1 trên TPU có thể được cải thiện nếu các nhà phát triển và người viết trình biên dịch làm nhiều công việc hơn để ghép CNN1 với phần cứng TPU. Ví dụ, các nhà phát triển có thể tổ chức lại các ứng dụng để tổng hợp nhiều lô ngắn từ các lớp tích chập thành một lô đơn, sâu hơn (từ 32 đến 128) cho bốn lớp kết nối đầy đủ. Một lớp đơn như vậy sẽ cải thiện mức sử dụng của đơn vị ma trận (Table 3). Vì CNN1 hiện chạy nhanh hơn CPU hơn 70 lần trên TPU, các nhà phát triển CNN1 đã rất hài lòng, vì vậy không rõ liệu hoặc khi nào các tối ưu hóa như vậy sẽ được thực hiện.
