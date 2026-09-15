---
paper: he-2016-resnet
title: Deep Residual Learning for Image Recognition
authors:
  - Kaiming He
  - Xiangyu Zhang
  - Shaoqing Ren
  - Jian Sun
year: 2016
venue: CVPR
field: ai-ml
section: "1"
section_title: Introduction
tag: "0116"
kind: section
lang: vi
source: arxiv:1512.03385
pdf_sha256: 1e0651b6810ecba34a3dbc5b5b0209226f889004607c1f203540a48d64e5a93a
pdf_pages: 1-2
extraction: vision
extraction_model: gpt-5
content_sha256: 6dd3c31d63a335076ab4fcdf6ec7378255ee6327c8f290c94a772636b193d45b
translated_from: content/en/he-2016-resnet/01_introduction.md
source_content_sha256: 2721cdfcd5fa4c1d2fb4d7699661f0df236d55cfca1019e225e870a3982ccf46
translation_model: gpt-5
translation_run: 20260915T013833Z
glossary_version: 6
glossary_terms_sha256: 0d0a9334a40352952769479a6ad339487dd551fe3d836bae9914ea196d2f4310
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Các mạng nơ-ron tích chập sâu [22], [[krizhevsky-2012-imagenet]] đã dẫn đến một loạt đột phá trong phân loại ảnh [[krizhevsky-2012-imagenet]], [50], [40]. Các mạng sâu tự nhiên tích hợp các đặc trưng mức thấp/trung bình/cao [50] và các bộ phân loại theo cách thức đa lớp đầu-cuối, và các “mức” của đặc trưng có thể được làm phong phú nhờ số lượng lớp được xếp chồng (độ sâu). Các bằng chứng gần đây [41, 44] cho thấy độ sâu của mạng có tầm quan trọng then chốt, và các kết quả dẫn đầu [41, 44, 13, 16] trên tập dữ liệu ImageNet đầy thách thức [36] đều khai thác các mô hình “rất sâu” [41], với độ sâu từ mười sáu [41] đến ba mươi [16]. Nhiều tác vụ nhận dạng thị giác không tầm thường khác [8, 12, 7, 32, 27] cũng được hưởng lợi đáng kể từ các mô hình rất sâu.

Hình 1. Lỗi huấn luyện (trái) và lỗi kiểm thử (phải) trên CIFAR-10 với các mạng “thuần” 20 lớp và 56 lớp. Mạng sâu hơn có lỗi huấn luyện cao hơn, và do đó lỗi kiểm thử cao hơn. Hiện tượng tương tự trên ImageNet được trình bày trong Hình 4. {#he-2016-resnet-fig-1 .figure tag=00E7}

Xuất phát từ tầm quan trọng của độ sâu, một câu hỏi được đặt ra: *Việc học các mạng tốt hơn có dễ dàng như việc xếp chồng thêm các lớp không?* Một trở ngại đối với việc trả lời câu hỏi này là vấn đề nổi tiếng về gradient tiêu biến/bùng nổ [1, 9], gây cản trở sự hội tụ ngay từ đầu. Tuy nhiên, vấn đề này phần lớn đã được giải quyết bằng khởi tạo chuẩn hóa [23, 9, 37, 13] và các lớp chuẩn hóa trung gian [16], cho phép các mạng có hàng chục lớp bắt đầu hội tụ khi sử dụng stochastic gradient descent (SGD) với lan truyền ngược [22].

Khi các mạng sâu hơn có khả năng bắt đầu hội tụ, một vấn đề *suy giảm* đã được bộc lộ: khi độ sâu của mạng tăng, độ chính xác đạt trạng thái bão hòa (điều này có thể không đáng ngạc nhiên) rồi suy giảm nhanh chóng. Điều đáng ngạc nhiên là sự suy giảm như vậy *không phải do overfitting*, và việc thêm nhiều lớp hơn vào một mô hình đủ sâu dẫn đến *lỗi huấn luyện cao hơn*, như được báo cáo trong [11, 42] và được kiểm chứng kỹ lưỡng qua các thực nghiệm của chúng tôi. Hình 1 cho thấy một ví dụ điển hình.

Sự suy giảm (về độ chính xác huấn luyện) cho thấy không phải tất cả các hệ thống đều dễ tối ưu hóa như nhau. Hãy xét một kiến trúc nông hơn và đối tác sâu hơn của nó, trong đó có thêm nhiều lớp lên trên. Tồn tại một nghiệm *theo cách xây dựng* cho mô hình sâu hơn: các lớp được thêm vào là *ánh xạ đồng nhất*, còn các lớp khác được sao chép từ mô hình nông hơn đã được học. Sự tồn tại của nghiệm được xây dựng này cho thấy một mô hình sâu hơn không nên tạo ra lỗi huấn luyện cao hơn đối tác nông hơn của nó. Nhưng các thực nghiệm cho thấy các bộ giải hiện tại của chúng tôi không thể tìm được các nghiệm

[^1]: http://image-net.org/challenges/LSVRC/2015/ và http://mscoco.org/dataset/#detections-challenge2015.

Hình 2. Học phần dư: một khối xây dựng. {#he-2016-resnet-fig-2 .figure tag=0117}

có chất lượng tương đương hoặc tốt hơn nghiệm được xây dựng (hoặc không thể làm được như vậy trong thời gian khả thi).

Trong bài báo này, chúng tôi giải quyết vấn đề suy giảm bằng cách đưa ra một khung *học phần dư sâu*. Thay vì hy vọng mỗi vài lớp được xếp chồng trực tiếp khớp với một ánh xạ nền tảng mong muốn, chúng tôi cho phép các lớp này tường minh khớp với một ánh xạ phần dư. Về mặt hình thức, ký hiệu ánh xạ nền tảng mong muốn là $\mathcal{H}(x)$, chúng tôi cho các lớp phi tuyến được xếp chồng khớp với một ánh xạ khác $\mathcal{F}(x) := \mathcal{H}(x) - x$. Ánh xạ ban đầu được viết lại thành $\mathcal{F}(x)+x$. Chúng tôi đưa ra giả thuyết rằng tối ưu hóa ánh xạ phần dư dễ hơn tối ưu hóa ánh xạ ban đầu, không có tham chiếu. Trong trường hợp cực đoan, nếu một ánh xạ đồng nhất là tối ưu, việc đẩy phần dư về không sẽ dễ hơn việc khớp một ánh xạ đồng nhất bằng một chồng các lớp phi tuyến.

Cách biểu diễn $\mathcal{F}(x)+x$ có thể được hiện thực hóa bằng các mạng nơ-ron truyền thẳng với các “kết nối tắt” (Hình 2). Các kết nối tắt [2, 34, 49] là những kết nối bỏ qua một hoặc nhiều lớp. Trong trường hợp của chúng tôi, các kết nối tắt đơn giản thực hiện *ánh xạ đồng nhất*, và đầu ra của chúng được cộng vào đầu ra của các lớp được xếp chồng (Hình 2). Các kết nối tắt đồng nhất không thêm tham số phụ cũng như độ phức tạp tính toán. Toàn bộ mạng vẫn có thể được huấn luyện đầu-cuối bằng SGD với lan truyền ngược, và có thể dễ dàng được hiện thực hóa bằng các thư viện phổ biến (*ví dụ*, Caffe [19]) mà không cần sửa đổi các bộ giải.

Chúng tôi trình bày các thực nghiệm toàn diện trên ImageNet [36] để chỉ ra vấn đề suy giảm và đánh giá phương pháp của mình. Chúng tôi cho thấy rằng: 1) Các mạng phần dư cực sâu của chúng tôi dễ tối ưu hóa, nhưng các mạng “thuần” đối tác (chỉ đơn giản xếp chồng các lớp) thể hiện lỗi huấn luyện cao hơn khi độ sâu tăng; 2) Các mạng phần dư sâu của chúng tôi có thể dễ dàng đạt được mức tăng độ chính xác nhờ độ sâu tăng đáng kể, tạo ra các kết quả tốt hơn đáng kể so với các mạng trước đây.

Các hiện tượng tương tự cũng được thể hiện trên tập CIFAR-10 [20], cho thấy những khó khăn trong tối ưu hóa và tác động của phương pháp của chúng tôi không chỉ tương tự với một tập dữ liệu cụ thể. Chúng tôi trình bày các mô hình được huấn luyện thành công trên tập dữ liệu này với hơn 100 lớp, và khảo sát các mô hình với hơn 1000 lớp.

Trên tập dữ liệu phân loại ImageNet [36], chúng tôi thu được các kết quả xuất sắc bằng các mạng phần dư cực sâu. Mạng phần dư 152 lớp của chúng tôi là mạng sâu nhất từng được trình bày trên ImageNet, trong khi vẫn có độ phức tạp thấp hơn các mạng VGG [41]. Tổ hợp của chúng tôi có lỗi top-5 **3.57%** trên *tập kiểm thử* ImageNet, và *giành vị trí thứ 1 trong cuộc thi phân loại ILSVRC 2015*. Các biểu diễn cực sâu cũng có hiệu năng khái quát hóa xuất sắc trên các tác vụ nhận dạng khác, và giúp chúng tôi tiếp tục *giành các vị trí thứ 1 ở: phát hiện ImageNet, định vị ImageNet, phát hiện COCO, và phân đoạn COCO* trong các cuộc thi ILSVRC & COCO 2015. Bằng chứng mạnh mẽ này cho thấy nguyên lý học phần dư có tính tổng quát, và chúng tôi kỳ vọng nó có thể áp dụng cho các bài toán thị giác và phi thị giác khác.
