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
section: C
section_title: Bản địa hóa ImageNet
tag: 01A3
kind: appendix
lang: vi
source: arxiv:1512.03385
pdf_sha256: 1e0651b6810ecba34a3dbc5b5b0209226f889004607c1f203540a48d64e5a93a
pdf_pages: "12"
extraction: vision
extraction_model: gpt-5
content_sha256: 07f4297b8334b2dbe55c193ec61a0d3e8be9385dbe7c6893468622a4e251f6a3
translated_from: content/en/he-2016-resnet/08_imagenet_localization.md
source_content_sha256: 46f961a65a59cf4eeaa619153116665c15b1df700c9cbe0bbd22cb30846dbb28
translation_model: gpt-5
translation_run: 20260915T013833Z
glossary_version: 6
glossary_terms_sha256: 0d0a9334a40352952769479a6ad339487dd551fe3d836bae9914ea196d2f4310
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Nhiệm vụ Bản địa hóa ImageNet (LOC) [36] yêu cầu phân loại và định vị các đối tượng. Theo [40, 41], chúng tôi giả định rằng các bộ phân loại ở mức ảnh trước tiên được sử dụng để dự đoán các nhãn lớp của một ảnh, và thuật toán bản địa hóa chỉ chịu trách nhiệm dự đoán các hộp bao quanh dựa trên các lớp đã dự đoán. Chúng tôi áp dụng chiến lược “hồi quy theo từng lớp” (PCR) [40, 41], học một bộ hồi quy hộp bao quanh cho mỗi lớp. Chúng tôi huấn luyện trước các mạng cho phân loại ImageNet rồi tinh chỉnh chúng cho bản địa hóa. Chúng tôi huấn luyện các mạng trên tập huấn luyện ImageNet 1000 lớp được cung cấp.

Thuật toán bản địa hóa của chúng tôi dựa trên khung RPN của [32] với một vài sửa đổi. Khác với cách trong [32] vốn không phụ thuộc danh mục, RPN của chúng tôi cho bản địa hóa được thiết kế dưới dạng *theo từng lớp*. RPN này kết thúc bằng hai lớp tích chập 1×1 song sinh cho phân loại nhị phân (*cls*) và hồi quy hộp (*reg*), như trong [32]. Các lớp *cls* và *reg* đều ở dạng *theo từng lớp*, trái ngược với [32]. Cụ thể, lớp *cls* có đầu ra 1000-d, và mỗi chiều là *hồi quy logistic nhị phân* để dự đoán có phải là một lớp đối tượng hay không; lớp *reg* có đầu ra 1000×4-d bao gồm các bộ hồi quy hộp cho 1000 lớp. Như trong [32], hồi quy hộp bao quanh của chúng tôi tham chiếu đến nhiều hộp “neo” bất biến theo phép dịch tại mỗi vị trí.

Giống như quá trình huấn luyện phân loại ImageNet của chúng tôi (Sec. 3.4), chúng tôi lấy mẫu ngẫu nhiên các vùng cắt 224×224 để tăng cường dữ liệu. Chúng tôi sử dụng kích thước lô nhỏ 256 ảnh để tinh chỉnh. Để tránh các mẫu âm chiếm ưu thế, 8 neo được lấy mẫu ngẫu nhiên cho mỗi ảnh, trong đó các neo dương và âm được lấy mẫu có tỷ lệ 1:1 [32]. Để kiểm thử, mạng được áp dụng trên toàn bộ ảnh theo cách tích chập đầy đủ.

Bảng 13 so sánh các kết quả bản địa hóa. Theo [41], trước tiên chúng tôi thực hiện kiểm thử “oracle” bằng cách sử dụng lớp đúng theo thực tế làm dự đoán phân loại. Bài báo của VGG [41] báo cáo lỗi cắt trung tâm là 33.1% (Bảng 13) khi sử dụng các lớp đúng theo thực tế. Với cùng thiết lập, phương pháp RPN của chúng tôi sử dụng mạng ResNet-101 giảm đáng kể lỗi cắt trung tâm xuống còn 13.3%. So sánh này chứng minh hiệu năng xuất sắc của khung của chúng tôi. Với kiểm thử dày đặc (tích chập đầy đủ) và đa tỷ lệ, ResNet-101 của chúng tôi có lỗi 11.7% khi sử dụng các lớp đúng theo thực tế. Sử dụng ResNet-101 để dự đoán các lớp (lỗi phân loại top-5 4.6%, Bảng 4), lỗi bản địa hóa top-5 là 14.4%.

```text
method                         top-5 localization err
                               val     test
OverFeat [40] (ILSVRC’13)      30.0    29.9
GoogLeNet [44] (ILSVRC’14)     -       26.7
VGG [41] (ILSVRC’14)           26.9    25.3
ours (ILSVRC’15)               8.9     9.0
```

Bảng 14. So sánh lỗi bản địa hóa (%) trên tập dữ liệu ImageNet với các phương pháp hiện đại nhất. {#he-2016-resnet-tab-14 .table tag=00F9}

Các kết quả trên chỉ dựa trên *mạng đề xuất* (RPN) trong Faster R-CNN [32]. Có thể sử dụng *mạng phát hiện* (Fast R-CNN [7]) trong Faster R-CNN để cải thiện kết quả. Tuy nhiên, chúng tôi nhận thấy rằng trên tập dữ liệu này, một ảnh thường chứa một đối tượng chi phối duy nhất, và các vùng đề xuất chồng lấn nhiều với nhau nên có các đặc trưng RoI-pooled rất tương tự. Do đó, việc huấn luyện lấy ảnh làm trung tâm của Fast R-CNN [7] tạo ra các mẫu có biến thiên nhỏ, điều này có thể không mong muốn đối với huấn luyện ngẫu nhiên. Dựa trên động lực này, trong thí nghiệm hiện tại, chúng tôi sử dụng R-CNN gốc [8] vốn lấy RoI làm trung tâm, thay cho Fast R-CNN.

Cài đặt R-CNN của chúng tôi như sau. Chúng tôi áp dụng RPN theo từng lớp được huấn luyện như trên vào các ảnh huấn luyện để dự đoán các hộp bao quanh cho lớp đúng theo thực tế. Các hộp được dự đoán này đóng vai trò là các đề xuất phụ thuộc lớp. Với mỗi ảnh huấn luyện, 200 đề xuất có điểm số cao nhất được trích xuất làm các mẫu huấn luyện để huấn luyện bộ phân loại R-CNN. Vùng ảnh được cắt từ một đề xuất, biến dạng thành 224×224 pixel, và đưa vào mạng phân loại như trong R-CNN [8]. Các đầu ra của mạng này bao gồm hai lớp fc song sinh cho *cls* và *reg*, cũng ở dạng theo từng lớp. Mạng R-CNN này được tinh chỉnh trên tập huấn luyện bằng cách sử dụng kích thước lô nhỏ 256 theo cách lấy RoI làm trung tâm. Để kiểm thử, RPN tạo ra 200 đề xuất có điểm số cao nhất cho mỗi lớp được dự đoán, và mạng R-CNN được sử dụng để cập nhật điểm số và vị trí hộp của các đề xuất này.

Phương pháp này giảm lỗi bản địa hóa top-5 xuống còn 10.6% (Bảng 13). Đây là kết quả của mô hình đơn lẻ của chúng tôi trên tập xác thực. Sử dụng một tổ hợp các mạng cho cả phân loại và bản địa hóa, chúng tôi đạt được lỗi bản địa hóa top-5 là 9.0% trên tập kiểm thử. Con số này vượt trội đáng kể so với các kết quả ILSVRC 14 (Bảng 14), cho thấy mức giảm lỗi tương đối 64%. *Kết quả này giành vị trí thứ 1 trong nhiệm vụ bản địa hóa ImageNet tại ILSVRC 2015.*
