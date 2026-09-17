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
section_title: Giới thiệu
tag: "0116"
kind: section
lang: vi
source: arxiv:1512.03385
pdf_sha256: 1e0651b6810ecba34a3dbc5b5b0209226f889004607c1f203540a48d64e5a93a
pdf_pages: 1-2
extraction: vision
extraction_model: gpt-5
content_sha256: f7babed82469a4f9e2c272035f0ec6741d0b2c79d29675d15a5486494465b290
translated_from: content/en/he-2016-resnet/01_introduction.md
source_content_sha256: 2721cdfcd5fa4c1d2fb4d7699661f0df236d55cfca1019e225e870a3982ccf46
translation_model: gpt-5
translation_run: 20260915T122820Z
glossary_version: 6
glossary_terms_sha256: 0d0a9334a40352952769479a6ad339487dd551fe3d836bae9914ea196d2f4310
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Các mạng nơ-ron tích chập sâu [22], [[krizhevsky-2012-imagenet]] đã dẫn đến một loạt đột phá trong phân loại ảnh [[krizhevsky-2012-imagenet]], [50], [40]. Các mạng sâu tự nhiên tích hợp các đặc trưng mức thấp/trung bình/cao [50] và các bộ phân loại theo cách nhiều lớp đầu-cuối, và các “mức” của đặc trưng có thể được làm phong phú hơn bởi số lượng lớp được xếp chồng (độ sâu). Các bằng chứng gần đây [41, 44] cho thấy độ sâu của mạng có tầm quan trọng then chốt, và các kết quả dẫn đầu [41, 44, 13, 16] trên tập dữ liệu ImageNet đầy thách thức [36] đều khai thác các mô hình “rất sâu” [41], với độ sâu từ mười sáu [41] đến ba mươi [16]. Nhiều tác vụ nhận dạng thị giác không tầm thường khác [8, 12, 7, 32, 27] cũng đã thu được nhiều lợi ích từ các mô hình rất sâu.

Hình 1. Lỗi huấn luyện (trái) và lỗi kiểm thử (phải) trên CIFAR-10 với các mạng “thuần” 20 lớp và 56 lớp. Mạng sâu hơn có lỗi huấn luyện cao hơn, và do đó có lỗi kiểm thử cao hơn. Các hiện tượng tương tự trên ImageNet được trình bày trong Hình 4. {#he-2016-resnet-fig-1 .figure tag=00E7}

Bị thúc đẩy bởi tầm quan trọng của độ sâu, một câu hỏi được đặt ra: \*Liệu việc học các mạng tốt hơn có dễ dàng như việc xếp chồng thêm các lớp không?\* Một trở ngại để trả lời câu hỏi này là vấn đề nổi tiếng về gradient biến mất/bùng nổ [1, 9], gây cản trở sự hội tụ ngay từ đầu. Tuy nhiên, vấn đề này phần lớn đã được giải quyết bằng khởi tạo được chuẩn hóa [23, 9, 37, 13] và các lớp chuẩn hóa trung gian [16], cho phép các mạng với hàng chục lớp bắt đầu hội tụ khi thực hiện giảm gradient ngẫu nhiên (SGD) với lan truyền ngược [22].

Khi các mạng sâu hơn có thể bắt đầu hội tụ, một vấn đề \*suy giảm\* đã được phát hiện: khi độ sâu của mạng tăng lên, độ chính xác đạt trạng thái bão hòa (điều này có thể không đáng ngạc nhiên) và sau đó suy giảm nhanh chóng. Không ngờ rằng, sự suy giảm như vậy \*không phải do quá khớp\*, và việc thêm nhiều lớp hơn vào một mô hình đủ sâu dẫn đến \*lỗi huấn luyện cao hơn\*, như được báo cáo trong [11, 42] và được xác minh kỹ lưỡng bởi các thí nghiệm của chúng tôi. Hình 1 cho thấy một ví dụ điển hình.

Sự suy giảm (của độ chính xác huấn luyện) cho thấy không phải tất cả các hệ thống đều dễ tối ưu hóa như nhau. Hãy xem xét một kiến trúc nông hơn và phiên bản sâu hơn tương ứng của nó, bổ sung thêm các lớp vào đó. Tồn tại một giải pháp \*bằng cách xây dựng\* cho mô hình sâu hơn: các lớp được thêm vào là \*ánh xạ đồng nhất\*, và các lớp còn lại được sao chép từ mô hình nông hơn đã được học. Sự tồn tại của giải pháp được xây dựng này cho thấy rằng một mô hình sâu hơn sẽ không tạo ra lỗi huấn luyện cao hơn so với phiên bản nông hơn tương ứng. Nhưng các thí nghiệm cho thấy rằng các bộ giải hiện có của chúng tôi không thể tìm thấy các giải pháp

[^1]: http://image-net.org/challenges/LSVRC/2015/ và http://mscoco.org/dataset/#detections-challenge2015.

Hình 2. Học phần dư: một khối xây dựng. {#he-2016-resnet-fig-2 .figure tag=0117}

có chất lượng tương đương hoặc tốt hơn giải pháp được xây dựng (hoặc không thể thực hiện điều đó trong thời gian khả thi).

Trong bài báo này, chúng tôi giải quyết vấn đề suy giảm bằng cách giới thiệu một khung \*học phần dư sâu\*. Thay vì hy vọng rằng mỗi vài lớp được xếp chồng sẽ trực tiếp khớp với ánh xạ nền tảng mong muốn, chúng tôi cho phép rõ ràng các lớp này khớp với một ánh xạ phần dư. Về mặt hình thức, ký hiệu ánh xạ nền tảng mong muốn là $\mathcal{H}(x)$, chúng tôi cho phép các lớp phi tuyến được xếp chồng khớp với một ánh xạ khác $\mathcal{F}(x) := \mathcal{H}(x) - x$. Ánh xạ ban đầu được chuyển đổi thành $\mathcal{F}(x)+x$. Chúng tôi đưa ra giả thuyết rằng việc tối ưu hóa ánh xạ phần dư dễ hơn so với tối ưu hóa ánh xạ ban đầu, không có tham chiếu. Ở mức cực đoan, nếu một ánh xạ đồng nhất là tối ưu, việc đẩy phần dư về không sẽ dễ hơn so với việc khớp một ánh xạ đồng nhất bằng một chồng các lớp phi tuyến.

Cách biểu diễn $\mathcal{F}(x)+x$ có thể được hiện thực hóa bởi các mạng nơ-ron truyền thẳng với các “kết nối tắt” (Hình 2). Các kết nối tắt [2, 34, 49] là những kết nối bỏ qua một hoặc nhiều lớp. Trong trường hợp của chúng tôi, các kết nối tắt chỉ đơn giản thực hiện ánh xạ \*đồng nhất\*, và đầu ra của chúng được cộng vào đầu ra của các lớp được xếp chồng (Hình 2). Các kết nối tắt đồng nhất không thêm bất kỳ tham số bổ sung nào cũng như độ phức tạp tính toán. Toàn bộ mạng vẫn có thể được huấn luyện đầu-cuối bằng SGD với lan truyền ngược, và có thể dễ dàng được triển khai bằng cách sử dụng các thư viện thông dụng (\*ví dụ\*, Caffe [19]) mà không cần sửa đổi các bộ giải.

Chúng tôi trình bày các thí nghiệm toàn diện trên ImageNet [36] để chỉ ra vấn đề suy giảm và đánh giá phương pháp của mình. Chúng tôi chỉ ra rằng: 1) Các mạng dư cực sâu của chúng tôi dễ tối ưu hóa, nhưng các mạng “thuần” tương ứng (chỉ đơn giản xếp chồng các lớp) thể hiện lỗi huấn luyện cao hơn khi độ sâu tăng lên; 2) Các mạng dư sâu của chúng tôi có thể dễ dàng thu được lợi ích về độ chính xác từ việc tăng độ sâu đáng kể, tạo ra các kết quả tốt hơn nhiều so với các mạng trước đây.

Các hiện tượng tương tự cũng được thể hiện trên tập CIFAR-10 [20], cho thấy rằng những khó khăn trong tối ưu hóa và các tác động của phương pháp của chúng tôi không chỉ tương tự với một tập dữ liệu cụ thể. Chúng tôi trình bày các mô hình được huấn luyện thành công trên tập dữ liệu này với hơn 100 lớp, và khảo sát các mô hình với hơn 1000 lớp.

Trên tập dữ liệu phân loại ImageNet [36], chúng tôi thu được các kết quả xuất sắc bằng các mạng dư cực sâu. Mạng dư 152 lớp của chúng tôi là mạng sâu nhất từng được trình bày trên ImageNet, đồng thời vẫn có độ phức tạp thấp hơn các mạng VGG [41]. Tổ hợp của chúng tôi có lỗi top-5 \*\*3.57%\*\* trên tập \*kiểm thử\* ImageNet, và \*giành vị trí thứ nhất trong cuộc thi phân loại ILSVRC 2015\*. Các biểu diễn cực sâu cũng có hiệu năng tổng quát hóa xuất sắc trên các tác vụ nhận dạng khác, và giúp chúng tôi tiếp tục \*giành các vị trí thứ nhất trong: phát hiện ImageNet, định vị ImageNet, phát hiện COCO, và phân đoạn COCO\* trong các cuộc thi ILSVRC & COCO 2015. Bằng chứng mạnh mẽ này cho thấy nguyên lý học phần dư là tổng quát, và chúng tôi kỳ vọng rằng nó có thể áp dụng cho các vấn đề thị giác và phi thị giác khác.
