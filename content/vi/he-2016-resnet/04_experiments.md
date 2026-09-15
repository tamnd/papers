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
section: "4"
section_title: Thí nghiệm
tag: "0100"
kind: section
lang: vi
source: arxiv:1512.03385
pdf_sha256: 1e0651b6810ecba34a3dbc5b5b0209226f889004607c1f203540a48d64e5a93a
pdf_pages: 4-8
extraction: vision
extraction_model: gpt-5
content_sha256: 80a06d26214bb530b22a80653932f5830d7bbe0b45d765c40a7dc65620c408db
translated_from: content/en/he-2016-resnet/04_experiments.md
source_content_sha256: 64c0ae63181a41965fc6a87fa1a460a2063bb45fbad28f910f4836d1220e131b
translation_model: gpt-5
translation_run: 20260915T013833Z
glossary_version: 6
glossary_terms_sha256: 0d0a9334a40352952769479a6ad339487dd551fe3d836bae9914ea196d2f4310
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

### 4.1. Phân loại ImageNet {#he-2016-resnet-s4-1 .section tag=0101}

Chúng tôi đánh giá phương pháp của mình trên tập dữ liệu phân loại ImageNet 2012 [36] gồm 1000 lớp. Các mô hình được huấn luyện trên 1,28 triệu ảnh huấn luyện, và được đánh giá trên 50k ảnh xác thực. Chúng tôi cũng thu được kết quả cuối cùng trên 100k ảnh kiểm thử, được báo cáo bởi server kiểm thử. Chúng tôi đánh giá cả tỷ lệ lỗi top-1 và top-5.

Mạng Thuần. Trước tiên chúng tôi đánh giá các mạng thuần 18 lớp và 34 lớp. Mạng thuần 34 lớp được trình bày trong Hình 3 (giữa). Mạng thuần 18 lớp có dạng tương tự. Xem Bảng 1 để biết các kiến trúc chi tiết.

Các kết quả trong Bảng 2 cho thấy mạng thuần 34 lớp sâu hơn có lỗi xác thực cao hơn mạng thuần 18 lớp nông hơn. Để làm rõ nguyên nhân, trong Hình 4 (trái) chúng tôi so sánh lỗi huấn luyện/xác thực của chúng trong suốt quá trình huấn luyện. Chúng tôi đã quan sát thấy vấn đề suy giảm - mạng

```text
layer name     output size     18-layer              34-layer              50-layer                         101-layer                          152-layer
-------------------------------------------------------------------------------------------------------------------------------
conv1          112×112                                7×7, 64, stride 2
                                              3×3 max pool, stride 2
conv2_x        56×56           [3×3, 64            [3×3, 64            [1×1, 64                         [1×1, 64                          [1×1, 64
                                3×3, 64] ×2         3×3, 64] ×3         3×3, 64                          3×3, 64                           3×3, 64
                                                                        1×1, 256] ×3                    1×1, 256] ×3                     1×1, 256] ×3

conv3_x        28×28           [3×3, 128           [3×3, 128           [1×1, 128                        [1×1, 128                         [1×1, 128
                                3×3, 128] ×2        3×3, 128] ×4        3×3, 128                         3×3, 128                          3×3, 128
                                                                        1×1, 512] ×4                    1×1, 512] ×4                     1×1, 512] ×8

conv4_x        14×14           [3×3, 256           [3×3, 256           [1×1, 256                        [1×1, 256                         [1×1, 256
                                3×3, 256] ×2        3×3, 256] ×6        3×3, 256                         3×3, 256                          3×3, 256
                                                                        1×1, 1024] ×6                   1×1, 1024] ×23                   1×1, 1024] ×36

conv5_x        7×7             [3×3, 512           [3×3, 512           [1×1, 512                        [1×1, 512                         [1×1, 512
                                3×3, 512] ×2        3×3, 512] ×3        3×3, 512                         3×3, 512                          3×3, 512
                                                                        1×1, 2048] ×3                   1×1, 2048] ×3                    1×1, 2048] ×3
                1×1                                   average pool, 1000-d fc, softmax
FLOPs                                  1.8×10^9             3.6×10^9             3.8×10^9                         7.6×10^9                         11.3×10^9
```

Bảng 1. Các kiến trúc cho ImageNet. Các khối xây dựng được hiển thị trong dấu ngoặc vuông (xem thêm Hình 5), cùng với số lượng khối được xếp chồng. Việc giảm mẫu được thực hiện bởi conv3_1, conv4_1 và conv5_1 với stride bằng 2. {#he-2016-resnet-tab-1 .table tag=00E9}

Hình 4. Huấn luyện trên ImageNet. Các đường mảnh biểu thị lỗi huấn luyện, và các đường đậm biểu thị lỗi xác thực của các vùng cắt trung tâm. Trái: các mạng thuần 18 và 34 lớp. Phải: các ResNet 18 và 34 lớp. Trong đồ thị này, các mạng dư (residual network) không có tham số bổ sung so với các mạng thuần tương ứng của chúng. {#he-2016-resnet-fig-4 .figure tag=00EA}

|  | plain | ResNet |
|---|---:|---:|
| 18 layers | 27.94 | 27.88 |
| 34 layers | 28.54 | **25.03** |

Bảng 2. Lỗi top-1 (%, kiểm thử 10-crop) trên tập xác thực ImageNet. Ở đây các ResNet không có tham số bổ sung so với các mạng thuần tương ứng của chúng. Hình 4 cho thấy các quá trình huấn luyện. {#he-2016-resnet-tab-2 .table tag=00EB}

mạng thuần 34 lớp có lỗi *huấn luyện* cao hơn trong toàn bộ quá trình huấn luyện, mặc dù không gian nghiệm của mạng thuần 18 lớp là một không gian con của mạng 34 lớp.

Chúng tôi cho rằng khó khăn tối ưu hóa này *không có khả năng* là do gradient bị tiêu biến. Các mạng thuần này được huấn luyện với BN [16], điều này bảo đảm các tín hiệu lan truyền thuận có phương sai khác không. Chúng tôi cũng xác nhận rằng các gradient lan truyền ngược thể hiện các chuẩn lành mạnh với BN. Do đó, cả tín hiệu thuận lẫn tín hiệu ngược đều không bị tiêu biến. Trên thực tế, mạng thuần 34 lớp vẫn có thể đạt được độ chính xác cạnh tranh (Bảng 3), cho thấy bộ giải hoạt động ở một mức độ nào đó. Chúng tôi phỏng đoán rằng các mạng thuần sâu có thể có tốc độ hội tụ thấp theo hàm mũ, điều này ảnh hưởng đến việc giảm lỗi huấn luyện[^1]. Nguyên nhân của những khó khăn tối ưu hóa như vậy sẽ được nghiên cứu trong tương lai.

### Mạng Dư. {#he-2016-resnet-s-residual-networks .section tag=011C}

Tiếp theo chúng tôi đánh giá các mạng dư (*ResNets*) 18 lớp và 34 lớp. Các kiến trúc đường cơ sở giống như các mạng thuần ở trên, ngoại trừ việc một kết nối tắt được thêm vào mỗi cặp bộ lọc 3×3 như trong Hình 3 (phải). Trong phép so sánh đầu tiên (Bảng 2 và Hình 4 bên phải), chúng tôi sử dụng ánh xạ đồng nhất cho tất cả các kết nối tắt và đệm bằng số không để tăng số chiều (tùy chọn A). Vì vậy chúng *không có tham số bổ sung* so với các mạng thuần tương ứng.

Chúng tôi có ba quan sát chính từ Bảng 2 và Hình 4. Thứ nhất, tình huống bị đảo ngược với học phần dư (residual learning) – ResNet 34 lớp tốt hơn ResNet 18 lớp (hơn 2,8%). Quan trọng hơn, ResNet 34 lớp cho thấy lỗi huấn luyện thấp hơn đáng kể và có khả năng khái quát hóa đối với dữ liệu xác thực. Điều này cho thấy vấn đề suy giảm đã được xử lý tốt trong thiết lập này và chúng tôi đạt được mức tăng độ chính xác từ việc tăng độ sâu.

Thứ hai, so với đối tác thuần túy của nó, mô hình 34 lớp

[^1]: Chúng tôi đã thử nghiệm với nhiều vòng lặp huấn luyện hơn (3×) và vẫn quan sát thấy vấn đề suy giảm, cho thấy rằng vấn đề này không thể được giải quyết một cách khả thi chỉ bằng cách sử dụng nhiều vòng lặp hơn.

```text
model                 top-1 err.   top-5 err.
VGG-16 [41]           28.07        9.33
GoogLeNet [44]        -            9.15
PReLU-net [13]        24.27        7.38
---------------------------------------------
plain-34              28.54        10.02
ResNet-34 A           25.03        7.76
ResNet-34 B           24.52        7.46
ResNet-34 C           24.19        7.40
---------------------------------------------
ResNet-50             22.85        6.71
ResNet-101            21.75        6.05
ResNet-152            21.43        5.71
```

Bảng 3. Tỷ lệ lỗi (%, kiểm thử 10-crop) trên tập xác thực ImageNet. VGG-16 dựa trên bài kiểm thử của chúng tôi. ResNet-50/101/152 thuộc lựa chọn B chỉ sử dụng phép chiếu để tăng số chiều. {#he-2016-resnet-tab-3 .table tag=00EC}

```text
method                top-1 err.   top-5 err.
VGG [41] (ILSVRC’14)  -            8.43†
GoogLeNet [44] (ILSVRC’14)
                       -            7.89
---------------------------------------------
VGG [41] (v5)         24.4         7.1
PReLU-net [13]        21.59        5.71
BN-inception [16]     21.99        5.81
---------------------------------------------
ResNet-34 B           21.84        5.71
ResNet-34 C           21.53        5.60
ResNet-50             20.74        5.25
ResNet-101            19.87        4.60
ResNet-152            19.38        4.49
```

Bảng 4. Tỷ lệ lỗi (%) của các kết quả mô hình đơn trên tập xác thực ImageNet (ngoại trừ † được báo cáo trên tập kiểm thử). {#he-2016-resnet-tab-4 .table tag=00ED}

```text
method                         top-5 err. (test)
VGG [41] (ILSVRC’14)           7.32
GoogLeNet [44] (ILSVRC’14)     6.66
---------------------------------------------
VGG [41] (v5)                  6.8
PReLU-net [13]                4.94
BN-inception [16]             4.82
---------------------------------------------
ResNet (ILSVRC’15)            3.57
```

Bảng 5. Tỷ lệ lỗi (%) của các tổ hợp. Lỗi top-5 được đo trên tập kiểm thử của ImageNet và được báo cáo bởi test server. {#he-2016-resnet-tab-5 .table tag=00EE}

ResNet làm giảm lỗi top-1 xuống 3,5% (Bảng 2), là kết quả của việc giảm thành công lỗi huấn luyện (Hình 4 bên phải so với bên trái). So sánh này xác minh hiệu quả của học phần dư trên các hệ thống cực sâu.

Cuối cùng, chúng tôi cũng lưu ý rằng các mạng thuần túy/phần dư 18 lớp có độ chính xác tương đương (Bảng 2), nhưng ResNet 18 lớp hội tụ nhanh hơn (Hình 4 bên phải so với bên trái). Khi mạng “không quá sâu” (ở đây là 18 lớp), bộ giải SGD hiện tại vẫn có khả năng tìm được các nghiệm tốt cho mạng thuần túy. Trong trường hợp này, ResNet làm cho việc tối ưu hóa dễ dàng hơn bằng cách cung cấp sự hội tụ nhanh hơn ở giai đoạn đầu.

### Đường tắt Ánh xạ đồng nhất so với Phép chiếu. {#he-2016-resnet-s-identity-vs-projection-shortcuts .section tag=011D}

Chúng tôi đã chỉ ra rằng các đường tắt ánh xạ đồng nhất không có tham số giúp ích cho việc huấn luyện. Tiếp theo chúng tôi khảo sát các đường tắt phép chiếu (Eqn.(2)). Trong Bảng 3 chúng tôi so sánh ba lựa chọn: (A) các đường tắt zero-padding được sử dụng để tăng số chiều, và tất cả các đường tắt đều không có tham số (giống như Bảng 2 và Hình 4 bên phải); (B) các đường tắt phép chiếu được sử dụng để tăng số chiều, còn các đường tắt khác là ánh xạ đồng nhất; và (C) tất cả các đường tắt đều là phép chiếu.

Hình 5. Một hàm phần dư sâu hơn $\mathcal{F}$ cho ImageNet. Bên trái: một khối xây dựng (trên các bản đồ đặc trưng 56×56) như trong Hình 3 cho ResNet-34. Bên phải: một khối xây dựng “bottleneck” cho ResNet-50/101/152. {#he-2016-resnet-fig-5 .figure tag=011E}

Bảng 3 cho thấy cả ba lựa chọn đều tốt hơn đáng kể so với đối tác thuần túy. B tốt hơn A một chút. Chúng tôi cho rằng điều này là do các chiều được zero-padding trong A thực sự không có học phần dư. C tốt hơn B ở mức rất nhỏ, và chúng tôi quy điều này cho các tham số bổ sung được đưa vào bởi nhiều (mười ba) đường tắt phép chiếu. Nhưng các khác biệt nhỏ giữa A/B/C cho thấy các đường tắt phép chiếu không phải là yếu tố thiết yếu để giải quyết vấn đề suy giảm. Vì vậy chúng tôi không sử dụng lựa chọn C trong phần còn lại của bài báo này, nhằm giảm độ phức tạp bộ nhớ/thời gian và kích thước mô hình. Các đường tắt ánh xạ đồng nhất đặc biệt quan trọng để không làm tăng độ phức tạp của các kiến trúc bottleneck được giới thiệu dưới đây.

### Các Kiến trúc Bottleneck Sâu hơn. {#he-2016-resnet-s-deeper-bottleneck-architectures .section tag=011F}

Tiếp theo chúng tôi mô tả các mạng sâu hơn của mình cho ImageNet. Do những lo ngại về thời gian huấn luyện mà chúng tôi có thể chấp nhận được, chúng tôi sửa đổi khối xây dựng theo thiết kế bottleneck.^4 Với mỗi hàm phần dư $\mathcal{F}$, chúng tôi sử dụng một chồng gồm 3 lớp thay vì 2 (Hình 5). Ba lớp này là các tích chập 1×1, 3×3 và 1×1, trong đó các lớp 1×1 chịu trách nhiệm giảm rồi tăng (khôi phục) số chiều, để lại lớp 3×3 như một bottleneck với số chiều đầu vào/đầu ra nhỏ hơn. Hình 5 cho thấy một ví dụ, trong đó cả hai thiết kế có độ phức tạp thời gian tương tự.

Các đường tắt ánh xạ đồng nhất không có tham số đặc biệt quan trọng đối với các kiến trúc bottleneck. Nếu đường tắt ánh xạ đồng nhất trong Hình 5 (bên phải) được thay thế bằng phép chiếu, có thể chỉ ra rằng độ phức tạp thời gian và kích thước mô hình bị tăng gấp đôi, vì đường tắt được kết nối với hai đầu có số chiều cao. Do đó các đường tắt ánh xạ đồng nhất dẫn đến các mô hình hiệu quả hơn cho các thiết kế bottleneck.

### ResNet 50 lớp: {#he-2016-resnet-s-50-layer-resnet .section tag=0120}

Chúng tôi thay thế mỗi khối 2 lớp trong

[^1]: Các ResNet sâu hơn không dùng bottleneck (ví dụ, Hình 5 bên trái) cũng đạt được độ chính xác cao hơn nhờ tăng độ sâu (như đã chỉ ra trên CIFAR-10), nhưng không kinh tế bằng các ResNet bottleneck. Vì vậy việc sử dụng thiết kế bottleneck chủ yếu là do các cân nhắc thực tế. Chúng tôi cũng lưu ý rằng vấn đề suy giảm của các mạng thuần túy cũng được quan sát thấy đối với các thiết kế bottleneck.

mạng 34 lớp bằng khối bottleneck 3 lớp này, tạo thành một ResNet 50 lớp (Bảng 1). Chúng tôi sử dụng lựa chọn B để tăng số chiều. Mô hình này có 3,8 tỷ FLOP.

**ResNet 101 lớp và 152 lớp:** Chúng tôi xây dựng các ResNet 101 lớp và 152 lớp bằng cách sử dụng nhiều khối 3 lớp hơn (Bảng 1). Đáng chú ý là mặc dù độ sâu được tăng lên đáng kể, ResNet 152 lớp (11,3 tỷ FLOP) vẫn có *độ phức tạp thấp hơn* các mạng VGG-16/19 (15,3/19,6 tỷ FLOP).

Các ResNet 50/101/152 lớp chính xác hơn đáng kể so với phiên bản 34 lớp (Bảng 3 và 4). Chúng tôi không quan sát thấy vấn đề suy giảm và do đó thu được mức tăng độ chính xác đáng kể từ việc tăng mạnh độ sâu. Lợi ích của độ sâu được thể hiện trên mọi thước đo đánh giá (Bảng 3 và 4).

**So sánh với các phương pháp tiên tiến nhất.** Trong Bảng 4, chúng tôi so sánh với các kết quả mô hình đơn tốt nhất trước đó. Các ResNet 34 lớp đường cơ sở của chúng tôi đã đạt được độ chính xác rất cạnh tranh. ResNet 152 lớp của chúng tôi có lỗi kiểm định top-5 của một mô hình đơn là 4,49%. Kết quả mô hình đơn này vượt qua mọi kết quả tổ hợp trước đó (Bảng 5). Chúng tôi kết hợp sáu mô hình có độ sâu khác nhau để tạo thành một tổ hợp (chỉ có hai mô hình 152 lớp vào thời điểm nộp bài). Điều này dẫn đến lỗi top-5 **3,57%** trên tập kiểm thử (Bảng 5). *Mục này đã giành vị trí thứ nhất trong ILSVRC 2015.*

### 4.2. CIFAR-10 và Phân tích {#he-2016-resnet-s4-2 .section tag=0129}

Chúng tôi tiến hành thêm các nghiên cứu trên tập dữ liệu (dataset) CIFAR-10 [20], bao gồm 50k ảnh huấn luyện và 10k ảnh kiểm thử thuộc 10 lớp. Chúng tôi trình bày các thí nghiệm được huấn luyện trên tập huấn luyện và đánh giá trên tập kiểm thử. Trọng tâm của chúng tôi là hành vi của các mạng cực sâu, chứ không phải nhằm đẩy kết quả tiên tiến nhất lên cao hơn, vì vậy chúng tôi chủ ý sử dụng các kiến trúc đơn giản như sau.

Các kiến trúc thuần túy/phần dư tuân theo dạng trong Hình 3 (giữa/phải). Đầu vào của mạng là các ảnh 32×32, với giá trị trung bình theo từng pixel đã được trừ đi. Lớp đầu tiên là các tích chập (convolution) 3×3. Sau đó chúng tôi sử dụng một chồng gồm $n$ lớp với các tích chập 3×3 trên các bản đồ đặc trưng có kích thước lần lượt là {32, 16, 8}, với $2n$ lớp cho mỗi kích thước bản đồ đặc trưng. Số lượng bộ lọc lần lượt là {16, 32, 64}. Việc lấy mẫu xuống được thực hiện bằng các tích chập có bước nhảy bằng 2. Mạng kết thúc bằng một lớp gộp trung bình toàn cục, một lớp kết nối đầy đủ 10 đầu ra, và softmax. Tổng cộng có $6n+2$ lớp có trọng số được xếp chồng. Bảng sau tóm tắt kiến trúc:

| kích thước bản đồ đầu ra | 32×32 | 16×16 | 8×8 |
|---|---:|---:|---:|
| số lớp | 1+2n | 2n | 2n |
| số bộ lọc | 16 | 32 | 64 |

Khi các kết nối tắt được sử dụng, chúng được nối tới các cặp lớp 3×3 (tổng cộng 3$n$ kết nối tắt). Trên tập dữ liệu này chúng tôi sử dụng các kết nối tắt ánh xạ đồng nhất (identity) trong mọi trường hợp (*tức là*, lựa chọn A),

```text
                         method                 error (%)
                         Maxout [10]            9.38
                         NIN [25]               8.81
                         DSN [24]               8.22

                         # layers   # params
FitNet [35]                 19        2.5M      8.39
Highway [42, 43]            19        2.3M      7.54 (7.72±0.16)
Highway [42, 43]            32        1.25M     8.80
ResNet                      20        0.27M     8.75
ResNet                      32        0.46M     7.51
ResNet                      44        0.66M     7.17
ResNet                      56        0.85M     6.97
ResNet                     110        1.7M      6.43 (6.61±0.16)
ResNet                    1202       19.4M      7.93
```

Bảng 6. Lỗi phân loại trên tập kiểm thử CIFAR-10. Tất cả các phương pháp đều sử dụng tăng cường dữ liệu. Đối với ResNet-110, chúng tôi chạy 5 lần và hiển thị “tốt nhất (trung bình±độ lệch chuẩn)” như trong [43]. {#he-2016-resnet-tab-6 .table tag=00EF}

vì vậy các mô hình phần dư của chúng tôi có chính xác cùng độ sâu, độ rộng và số lượng tham số như các đối tác thuần túy.

Chúng tôi sử dụng weight decay bằng 0,0001 và momentum bằng 0,9, đồng thời áp dụng khởi tạo trọng số trong [13] và BN [16] nhưng không dùng dropout. Các mô hình này được huấn luyện với kích thước mini-batch là 128 trên hai GPU. Chúng tôi bắt đầu với tốc độ học là 0,1, chia nó cho 10 tại các vòng lặp 32k và 48k, và kết thúc huấn luyện tại 64k vòng lặp, được xác định trên phép chia train/val 45k/5k. Chúng tôi tuân theo phương pháp tăng cường dữ liệu đơn giản trong [24] để huấn luyện: đệm thêm 4 pixel ở mỗi phía, và lấy ngẫu nhiên một vùng cắt 32×32 từ ảnh đã được đệm hoặc ảnh lật ngang của nó. Đối với kiểm thử, chúng tôi chỉ đánh giá một góc nhìn duy nhất của ảnh gốc 32×32.

Chúng tôi so sánh $n=\{3,5,7,9\}$, tương ứng tạo ra các mạng 20, 32, 44 và 56 lớp. Hình 6 (trái) cho thấy hành vi của các mạng thuần túy. Các mạng thuần túy sâu bị ảnh hưởng bất lợi khi độ sâu tăng lên, và biểu hiện lỗi huấn luyện cao hơn khi trở nên sâu hơn. Hiện tượng này tương tự như trên ImageNet (Hình 4, trái) và trên MNIST (xem [42]), cho thấy rằng khó khăn tối ưu hóa như vậy là một vấn đề cơ bản.

Hình 6 (giữa) cho thấy hành vi của các ResNet. Tương tự như các trường hợp trên ImageNet (Hình 4, phải), các ResNet của chúng tôi vượt qua được khó khăn tối ưu hóa và thể hiện mức tăng độ chính xác khi độ sâu tăng lên.

Chúng tôi tiếp tục khảo sát $n = 18$, dẫn đến một ResNet 110 lớp. Trong trường hợp này, chúng tôi nhận thấy rằng tốc độ học ban đầu 0.1 hơi quá lớn để bắt đầu hội tụ[^1]. Vì vậy, chúng tôi sử dụng 0.01 để khởi động quá trình huấn luyện cho đến khi lỗi huấn luyện nhỏ hơn 80% (khoảng 400 lần lặp), sau đó quay lại 0.1 và tiếp tục huấn luyện. Phần còn lại của lịch huấn luyện được thực hiện như trước đây. Mạng 110 lớp này hội tụ tốt (Fig. 6, giữa). Nó có *ít hơn* tham số so với các mạng sâu và mỏng khác

[^1]: Với tốc độ học ban đầu là 0.1, nó bắt đầu hội tụ (<90% lỗi) sau vài epoch, nhưng vẫn đạt độ chính xác tương tự.

Figure 6. Huấn luyện trên CIFAR-10. Các đường nét đứt biểu thị lỗi huấn luyện, và các đường in đậm biểu thị lỗi kiểm thử. **Trái:** các mạng thông thường. Lỗi của plain-110 cao hơn 60% và không được hiển thị. **Giữa:** ResNets. **Phải:** ResNets với 110 và 1202 lớp. {#he-2016-resnet-fig-6 .figure tag=00F0}

Figure 7. Độ lệch chuẩn (std) của các phản hồi lớp trên CIFAR-10. Các phản hồi là đầu ra của mỗi lớp $3 \times 3$, sau BN và trước tính phi tuyến. **Trên:** các lớp được hiển thị theo thứ tự ban đầu. **Dưới:** các phản hồi được xếp hạng theo thứ tự giảm dần. {#he-2016-resnet-fig-7 .figure tag=012A}

các mạng như FitNet [35] và Highway [42] (Table 6), nhưng vẫn nằm trong số các kết quả hiện đại nhất (6.43%, Table 6).

**Phân tích các phản hồi lớp.** Fig. 7 hiển thị độ lệch chuẩn (std) của các phản hồi lớp. Các phản hồi là đầu ra của mỗi lớp $3 \times 3$, sau BN và trước tính phi tuyến khác (ReLU/addition). Đối với ResNets, phân tích này cho thấy cường độ phản hồi của các hàm dư. Fig. 7 cho thấy ResNets nhìn chung có các phản hồi nhỏ hơn so với các mạng thông thường tương ứng. Các kết quả này ủng hộ động lực cơ bản của chúng tôi (Sec.3.1) rằng các hàm dư có thể thường gần bằng không hơn các hàm không dư. Chúng tôi cũng nhận thấy rằng ResNet sâu hơn có độ lớn phản hồi nhỏ hơn, được chứng minh qua các so sánh giữa ResNet-20, 56 và 110 trong Fig. 7. Khi có nhiều lớp hơn, một lớp riêng lẻ của ResNets có xu hướng thay đổi tín hiệu ít hơn.

**Khảo sát trên 1000 lớp.** Chúng tôi khảo sát một mô hình sâu mạnh mẽ có hơn 1000 lớp. Chúng tôi đặt $n = 200$, dẫn đến một mạng 1202 lớp, được huấn luyện như mô tả ở trên. Phương pháp của chúng tôi cho thấy *không có khó khăn trong tối ưu hóa*, và mạng $10^3$ lớp này có thể đạt được *lỗi huấn luyện* $< 0.1\%$ (Fig. 6, phải). Lỗi kiểm thử của nó vẫn khá tốt (7.93%, Table 6).

Tuy nhiên, vẫn còn các vấn đề mở đối với những mô hình sâu mạnh mẽ như vậy. Kết quả kiểm thử của mạng 1202 lớp này kém hơn so với mạng 110 lớp của chúng tôi, mặc dù cả hai

| dữ liệu huấn luyện | 07+12 | 07++12 |
|---|---:|---:|
| dữ liệu kiểm thử | VOC 07 test | VOC 12 test |
| VGG-16 | 73.2 | 70.4 |
| ResNet-101 | **76.4** | **73.8** |

Table 7. mAP (%) phát hiện đối tượng trên các tập kiểm thử PASCAL VOC 2007/2012 sử dụng **đường cơ sở** Faster R-CNN. Xem thêm Table 10 và 11 để có các kết quả tốt hơn. {#he-2016-resnet-tab-7 .table tag=00F1}

| chỉ số | mAP@.5 | mAP@[.5, .95] |
|---|---:|---:|
| VGG-16 | 41.5 | 21.2 |
| ResNet-101 | **48.4** | **27.2** |

Table 8. mAP (%) phát hiện đối tượng trên tập xác thực COCO sử dụng **đường cơ sở** Faster R-CNN. Xem thêm Table 9 để có các kết quả tốt hơn. {#he-2016-resnet-tab-8 .table tag=00F2}

có lỗi huấn luyện tương tự. Chúng tôi cho rằng điều này là do quá khớp. Mạng 1202 lớp có thể lớn không cần thiết (19.4M) đối với tập dữ liệu nhỏ này. Các kỹ thuật điều chuẩn mạnh như maxout [10] hoặc dropout [14] được áp dụng để thu được các kết quả tốt nhất ([10, 25, 24, 35]) trên tập dữ liệu này. Trong bài báo này, chúng tôi không sử dụng maxout/dropout và chỉ đơn giản áp đặt điều chuẩn thông qua các kiến trúc sâu và mỏng theo thiết kế, mà không làm phân tán trọng tâm khỏi những khó khăn trong tối ưu hóa. Tuy nhiên, việc kết hợp với điều chuẩn mạnh hơn có thể cải thiện kết quả, điều mà chúng tôi sẽ nghiên cứu trong tương lai.

### 4.3. Phát hiện đối tượng trên PASCAL và MS COCO {#he-2016-resnet-s4-3 .section tag=0103}

Phương pháp của chúng tôi có hiệu năng tổng quát hóa tốt trên các tác vụ nhận dạng khác. Table 7 và 8 cho thấy các kết quả đường cơ sở phát hiện đối tượng trên PASCAL VOC 2007 và 2012 [5] và COCO [26]. Chúng tôi sử dụng *Faster R-CNN* [32] làm phương pháp phát hiện. Ở đây chúng tôi quan tâm đến những cải thiện khi thay thế VGG-16 [41] bằng ResNet-101. Cách triển khai phát hiện (xem phụ lục) khi sử dụng cả hai mô hình là giống nhau, do đó các cải thiện chỉ có thể được quy cho các mạng tốt hơn. Đáng chú ý nhất, trên tập dữ liệu COCO đầy thách thức, chúng tôi thu được mức tăng 6.0% trong chỉ số tiêu chuẩn của COCO (mAP@[.5, .95]), tương đương với cải thiện tương đối 28%. Sự cải thiện này hoàn toàn nhờ vào các biểu diễn đã học.

Dựa trên các mạng dư sâu, chúng tôi đã giành vị trí thứ 1 trong một số hạng mục tại các cuộc thi ILSVRC & COCO 2015: ImageNet detection, ImageNet localization, COCO detection, và COCO segmentation. Các chi tiết nằm trong phụ lục.
