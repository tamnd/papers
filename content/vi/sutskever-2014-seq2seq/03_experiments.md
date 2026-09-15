---
paper: sutskever-2014-seq2seq
title: Sequence to Sequence Learning with Neural Networks
authors:
  - Ilya Sutskever
  - Oriol Vinyals
  - Quoc V. Le
year: 2014
venue: NIPS
field: ai-ml
section: "3"
section_title: Thực nghiệm
tag: 00D4
kind: section
lang: vi
source: arxiv:1409.3215
pdf_sha256: 5c74e1db863e2d61b869c9b0603494b34c41fb05db1a4fa7f9a83d5a42b7350f
pdf_pages: 3-7
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: e616597407474a3240b126d74e54b1f9b1f3061d0e7f093d368a6545825b0070
translated_from: content/en/sutskever-2014-seq2seq/03_experiments.md
source_content_sha256: 6c6b106f5c9e76f20c9800f7151777f4bae76265d42fbf1cb7527630b5e2a3ac
translation_model: gpt-6-astra
translation_run: 20260915T022520Z
glossary_version: 6
glossary_terms_sha256: 0d0a9334a40352952769479a6ad339487dd551fe3d836bae9914ea196d2f4310
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Chúng tôi áp dụng phương pháp của mình cho tác vụ dịch máy (machine translation) từ tiếng Anh sang tiếng Pháp của WMT’14 theo hai cách. Chúng tôi dùng phương pháp này để dịch trực tiếp câu đầu vào mà không sử dụng hệ thống dịch máy thống kê (SMT) tham chiếu, đồng thời dùng nó để chấm lại điểm số cho các danh sách n bản dịch tốt nhất của một hệ thống SMT đường cơ sở. Chúng tôi báo cáo độ chính xác của các phương pháp dịch này, trình bày các bản dịch mẫu và trực quan hóa biểu diễn câu thu được.

### 3.1 Chi tiết về tập dữ liệu {#sutskever-2014-seq2seq-s3-1 .section tag=00D5}

Chúng tôi sử dụng tập dữ liệu tiếng Anh sang tiếng Pháp của WMT’14. Chúng tôi huấn luyện các mô hình trên một tập con gồm 12M câu, chứa 348M từ tiếng Pháp và 304M từ tiếng Anh, là một tập con sạch được “chọn lọc” từ [29]. Chúng tôi chọn tác vụ dịch này và tập con huấn luyện cụ thể này vì tập huấn luyện và tập kiểm thử đã được tách token, cùng với các danh sách 1000 bản dịch tốt nhất từ hệ thống SMT đường cơ sở [29], đều được công bố công khai.

Vì các mô hình ngôn ngữ nơ-ron thông thường dựa vào một biểu diễn vectơ cho mỗi từ, chúng tôi sử dụng một bộ từ vựng cố định cho cả hai ngôn ngữ. Chúng tôi dùng 160,000 từ xuất hiện thường xuyên nhất cho ngôn ngữ nguồn và 80,000 từ xuất hiện thường xuyên nhất cho ngôn ngữ đích. Mỗi từ ngoài bộ từ vựng được thay bằng một token đặc biệt “UNK”.

### 3.2 Giải mã và chấm lại điểm số {#sutskever-2014-seq2seq-s3-2 .section tag=00D6}

Phần cốt lõi của các thực nghiệm là huấn luyện một LSTM sâu, lớn trên nhiều cặp câu. Chúng tôi huấn luyện nó bằng cách cực đại hóa log xác suất của một bản dịch đúng $T$ khi biết câu nguồn $S$, do đó mục tiêu huấn luyện là

$$
\frac{1}{|\mathcal{S}|} \sum_{(T,S) \in \mathcal{S}} \log p(T|S)
$$

trong đó $\mathcal{S}$ là tập huấn luyện. Sau khi hoàn tất huấn luyện, chúng tôi tạo ra các bản dịch bằng cách tìm bản dịch có xác suất cao nhất theo LSTM:

$$
\hat{T} = \arg \max_T p(T|S)
$$

Chúng tôi tìm bản dịch có xác suất cao nhất bằng một bộ giải mã tìm kiếm chùm (beam search) đơn giản từ trái sang phải, duy trì một số lượng nhỏ $B$ giả thuyết chưa hoàn chỉnh, trong đó một giả thuyết chưa hoàn chỉnh là tiền tố của một bản dịch nào đó. Ở mỗi bước thời gian, chúng tôi mở rộng từng giả thuyết chưa hoàn chỉnh trong chùm bằng từng từ có thể có trong bộ từ vựng. Điều này làm tăng mạnh số lượng giả thuyết, nên chúng tôi loại bỏ tất cả, chỉ giữ lại $B$ giả thuyết có xác suất cao nhất theo log xác suất của mô hình. Ngay khi ký hiệu “<EOS>” được nối vào một giả thuyết, giả thuyết đó được lấy ra khỏi chùm và thêm vào tập các giả thuyết hoàn chỉnh. Mặc dù bộ giải mã này mang tính xấp xỉ, nó dễ triển khai. Điều thú vị là hệ thống của chúng tôi hoạt động tốt ngay cả với kích thước chùm bằng 1, và chùm có kích thước bằng 2 mang lại phần lớn lợi ích của tìm kiếm chùm (Bảng 1).

Chúng tôi cũng dùng LSTM để chấm lại điểm số cho các danh sách 1000 bản dịch tốt nhất do hệ thống đường cơ sở [29] tạo ra. Để chấm lại điểm số cho một danh sách n bản dịch tốt nhất, chúng tôi tính log xác suất của từng giả thuyết bằng LSTM và lấy trung bình cộng của điểm số từ hệ thống đó và điểm số của LSTM.

### 3.3 Đảo ngược các câu nguồn {#sutskever-2014-seq2seq-s3-3 .section tag=00D7}

Mặc dù LSTM có khả năng giải quyết các bài toán có phụ thuộc dài hạn, chúng tôi phát hiện rằng LSTM học tốt hơn nhiều khi các câu nguồn được đảo ngược (các câu đích không được đảo ngược). Khi làm như vậy, độ bối rối (perplexity) của LSTM trên tập kiểm thử giảm từ 5.8 xuống 4.7, và điểm số BLEU trên tập kiểm thử của các bản dịch được giải mã tăng từ 25.9 lên 30.6.

Mặc dù chưa có lời giải thích đầy đủ cho hiện tượng này, chúng tôi cho rằng nguyên nhân là do việc đưa nhiều phụ thuộc ngắn hạn vào tập dữ liệu. Thông thường, khi nối một câu nguồn với một câu đích, mỗi từ trong câu nguồn đều ở xa từ tương ứng trong câu đích. Do đó, bài toán có “độ trễ thời gian tối thiểu” lớn [17]. Khi đảo ngược các từ trong câu nguồn, khoảng cách trung bình giữa các từ tương ứng trong ngôn ngữ nguồn và ngôn ngữ đích không thay đổi. Tuy nhiên, vài từ đầu tiên trong ngôn ngữ nguồn lúc này ở rất gần vài từ đầu tiên trong ngôn ngữ đích, nên độ trễ thời gian tối thiểu của bài toán giảm đáng kể. Vì vậy, lan truyền ngược (backpropagation) dễ “thiết lập liên lạc” giữa câu nguồn và câu đích hơn, từ đó cải thiện đáng kể hiệu năng tổng thể.

Ban đầu, chúng tôi cho rằng việc đảo ngược các câu đầu vào chỉ dẫn đến các dự đoán tự tin hơn ở phần đầu của câu đích và các dự đoán kém tự tin hơn ở phần sau. Tuy nhiên, các LSTM được huấn luyện trên các câu nguồn đảo ngược hoạt động tốt hơn nhiều trên các câu dài so với các LSTM được huấn luyện trên các câu nguồn nguyên bản (xem mục 3.7), cho thấy việc đảo ngược các câu đầu vào giúp LSTM sử dụng bộ nhớ tốt hơn.

### 3.4 Chi tiết huấn luyện {#sutskever-2014-seq2seq-s3-4 .section tag=00D8}

Chúng tôi nhận thấy các mô hình LSTM khá dễ huấn luyện. Chúng tôi sử dụng các LSTM sâu có 4 lớp, với 1000 ô ở mỗi lớp và các embedding từ 1000 chiều, cùng bộ từ vựng đầu vào gồm 160,000 từ và bộ từ vựng đầu ra gồm 80,000 từ. Như vậy, LSTM sâu dùng 8000 số thực để biểu diễn một câu. Chúng tôi nhận thấy các LSTM sâu có hiệu năng vượt trội đáng kể so với các LSTM nông, trong đó mỗi lớp bổ sung làm giảm độ bối rối gần 10%, có thể là do trạng thái ẩn lớn hơn nhiều của chúng. Chúng tôi dùng softmax theo cách trực tiếp trên 80,000 từ tại mỗi đầu ra. LSTM thu được có 384M tham số, trong đó 64M là các kết nối hồi quy thuần túy (32M cho LSTM “bộ mã hóa” và 32M cho LSTM “bộ giải mã”). Chi tiết huấn luyện đầy đủ được trình bày dưới đây:

• Chúng tôi khởi tạo tất cả các tham số của LSTM theo phân phối đều trong khoảng từ -0.08 đến 0.08
• Chúng tôi sử dụng phương pháp hạ gradient ngẫu nhiên (stochastic gradient descent) không có động lượng, với tốc độ học cố định là 0.7. Sau 5 lượt huấn luyện, chúng tôi bắt đầu giảm tốc độ học đi một nửa sau mỗi nửa lượt huấn luyện. Chúng tôi huấn luyện các mô hình trong tổng cộng 7.5 lượt.
• Chúng tôi sử dụng các lô gồm 128 chuỗi để tính gradient và chia gradient cho kích thước lô (tức là 128).
• Mặc dù LSTM thường không gặp vấn đề tiêu biến gradient, chúng có thể gặp hiện tượng bùng nổ gradient. Vì vậy, chúng tôi áp đặt một ràng buộc cứng lên chuẩn của gradient [10, 25] bằng cách co giãn gradient khi chuẩn của nó vượt quá một ngưỡng. Với mỗi lô huấn luyện, chúng tôi tính $s = \|g\|_2$, trong đó $g$ là gradient đã chia cho 128. Nếu $s > 5$, chúng tôi đặt $g = \frac{5g}{s}$.
• Các câu khác nhau có độ dài khác nhau. Phần lớn các câu đều ngắn (ví dụ, độ dài 20-30), nhưng một số câu lại dài (ví dụ, độ dài $> 100$), do đó một lô nhỏ gồm 128 câu huấn luyện được chọn ngẫu nhiên sẽ có nhiều câu ngắn và ít câu dài, khiến phần lớn tính toán trong lô nhỏ bị lãng phí. Để giải quyết vấn đề này, chúng tôi bảo đảm rằng tất cả các câu trong một lô nhỏ có độ dài gần bằng nhau, nhờ đó tăng tốc gấp 2 lần.

### 3.5 Song song hóa {#sutskever-2014-seq2seq-s3-5 .section tag=00D9}

Một bản triển khai LSTM sâu bằng C++ với cấu hình từ mục trước trên một GPU duy nhất xử lý với tốc độ khoảng 1,700 từ mỗi giây. Tốc độ này quá chậm đối với mục đích của chúng tôi, nên chúng tôi song song hóa mô hình bằng một máy có 8 GPU. Mỗi lớp của LSTM được thực thi trên một GPU khác nhau và truyền các giá trị kích hoạt của nó sang GPU / lớp tiếp theo ngay khi chúng được tính xong. Các mô hình của chúng tôi có 4 lớp LSTM, mỗi lớp nằm trên một GPU riêng. 4 GPU còn lại được dùng để song song hóa softmax, nên mỗi GPU phụ trách phép nhân với một ma trận $1000 \times 20000$. Bản triển khai thu được đạt tốc độ 6,300 từ (gồm cả tiếng Anh và tiếng Pháp) mỗi giây với kích thước lô nhỏ là 128. Quá trình huấn luyện với bản triển khai này mất khoảng mười ngày.

### 3.6 Kết quả thực nghiệm {#sutskever-2014-seq2seq-s3-6 .section tag=00DA}

Chúng tôi sử dụng điểm số BLEU có phân biệt chữ hoa và chữ thường [24] để đánh giá chất lượng các bản dịch. Chúng tôi tính các điểm số BLEU bằng multi-bleu.pl$^1$ trên các dự đoán và bản dịch chuẩn đã được tách token. Cách đánh giá điểm số BELU này nhất quán với [5] và [2], đồng thời tái lập điểm số 33.3 của [29]. Tuy nhiên, nếu đánh giá hệ thống WMT’14 tốt nhất [9] (có thể tải các dự đoán của hệ thống này từ statmt.org\matrix) theo cách này, chúng tôi thu được 37.0, cao hơn mức 35.8 được báo cáo trên statmt.org\matrix.

Các kết quả được trình bày trong bảng 1 và 2. Chúng tôi thu được kết quả tốt nhất với một tổ hợp (ensemble) các LSTM khác nhau về cách khởi tạo ngẫu nhiên và thứ tự ngẫu nhiên của các lô nhỏ. Mặc dù các bản dịch được giải mã từ tổ hợp LSTM không vượt qua hệ thống WMT’14 tốt nhất, đây là lần đầu tiên một hệ thống dịch thuần nơ-ron vượt qua đường cơ sở SMT dựa trên cụm từ trên một tác vụ dịch máy quy mô lớn

$^1$Có một số biến thể của điểm số BLEU, và mỗi biến thể được định nghĩa bằng một script perl.

| Phương pháp | Điểm số BLEU trên tập kiểm thử (ntst14) |
| --- | --- |
| Bahdanau và cộng sự [2] | 28.45 |
| Hệ thống đường cơ sở [29] | 33.30 |
| Một LSTM xuôi, kích thước chùm 12 | 26.17 |
| Một LSTM đảo ngược, kích thước chùm 12 | 30.59 |
| Tổ hợp 5 LSTM đảo ngược, kích thước chùm 1 | 33.00 |
| Tổ hợp 2 LSTM đảo ngược, kích thước chùm 12 | 33.27 |
| Tổ hợp 5 LSTM đảo ngược, kích thước chùm 2 | 34.50 |
| Tổ hợp 5 LSTM đảo ngược, kích thước chùm 12 | 34.81 |

Bảng 1: Hiệu năng của LSTM trên tập kiểm thử dịch từ tiếng Anh sang tiếng Pháp WMT’14 (ntst14). Lưu ý rằng một tổ hợp 5 LSTM với chùm có kích thước 2 có chi phí thấp hơn một LSTM duy nhất với chùm có kích thước 12. {#sutskever-2014-seq2seq-tab-1 .table tag=00DB}

| Phương pháp | Điểm số BLEU trên tập kiểm thử (ntst14) |
| --- | --- |
| Hệ thống đường cơ sở [29] | 33.30 |
| Cho và cộng sự [5] | 34.54 |
| Kết quả WMT’14 tốt nhất [9] | 37.0 |
| Chấm điểm lại 1000 bản dịch tốt nhất của đường cơ sở bằng một LSTM xuôi | 35.61 |
| Chấm điểm lại 1000 bản dịch tốt nhất của đường cơ sở bằng một LSTM đảo ngược | 35.85 |
| Chấm điểm lại 1000 bản dịch tốt nhất của đường cơ sở bằng một tổ hợp 5 LSTM đảo ngược | 36.5 |
| Chấm điểm lại bằng oracle các danh sách 1000 bản dịch tốt nhất của đường cơ sở | ~45 |

Bảng 2: Các phương pháp sử dụng mạng nơ-ron (neural network) cùng với một hệ thống SMT trên tập kiểm thử dịch từ tiếng Anh sang tiếng Pháp WMT’14 (ntst14). {#sutskever-2014-seq2seq-tab-2 .table tag=00DC}

với khoảng cách đáng kể, mặc dù không thể xử lý các từ ngoài từ vựng. LSTM chỉ kém kết quả WMT’14 tốt nhất trong khoảng 0.5 điểm BLEU nếu được dùng để chấm điểm lại danh sách 1000 bản dịch tốt nhất của hệ thống đường cơ sở.

### 3.7 Hiệu năng trên các câu dài {#sutskever-2014-seq2seq-s3-7 .section tag=00DD}

Chúng tôi ngạc nhiên khi phát hiện rằng LSTM xử lý tốt các câu dài, như được thể hiện định lượng trong hình 3. Bảng 3 trình bày một số ví dụ về các câu dài và bản dịch của chúng.

### 3.8 Phân tích mô hình {#sutskever-2014-seq2seq-s3-8 .section tag=00DE}

Hình.

Hình 2: Hình này thể hiện phép chiếu PCA 2 chiều của các trạng thái ẩn LSTM thu được sau khi xử lý các cụm từ trong các hình. Các cụm từ được phân cụm theo nghĩa, mà trong các ví dụ này chủ yếu là một hàm của thứ tự từ, điều khó nắm bắt bằng mô hình túi từ (bag-of-words). Lưu ý rằng cả hai cụm đều có cấu trúc bên trong tương tự nhau. {#sutskever-2014-seq2seq-fig-2 .figure tag=00DF}

Một trong những đặc trưng hấp dẫn của mô hình chúng tôi là khả năng biến một chuỗi từ thành một vectơ có số chiều cố định. Hình 2 trực quan hóa một số biểu diễn đã học được. Hình này cho thấy rõ rằng các biểu diễn nhạy với thứ tự từ, đồng thời khá ít nhạy với

| Kiểu | Câu |
| --- | --- |
| Mô hình của chúng tôi | Ulrich UNK, thành viên hội đồng quản trị của hãng sản xuất ô tô Audi, khẳng định rằng việc thu gom điện thoại di động trước các cuộc họp hội đồng quản trị để chúng không bị sử dụng làm thiết bị nghe lén từ xa đã là thông lệ trong nhiều năm. |
| Bản dịch chuẩn | Ulrich Hackenberg, thành viên hội đồng quản trị của hãng sản xuất ô tô Audi, cho biết việc thu gom điện thoại di động trước các cuộc họp hội đồng quản trị, để chúng không thể bị sử dụng làm thiết bị nghe lén từ xa, đã là thông lệ trong nhiều năm. |
| Mô hình của chúng tôi | “Điện thoại di động thực sự là một vấn đề, không chỉ vì chúng có khả năng gây nhiễu các thiết bị dẫn đường, mà chúng tôi còn biết, theo FCC, rằng chúng có thể gây nhiễu các trạm thu phát sóng di động khi ở trên không”, UNK nói. |
| Bản dịch chuẩn | “Điện thoại di động thực sự là một vấn đề, không chỉ vì chúng có thể gây nhiễu các thiết bị dẫn đường, mà còn vì chúng tôi biết, theo FCC, rằng chúng có thể gây nhiễu các trạm thu phát sóng di động nếu được sử dụng trên máy bay”, Rosenker cho biết. |
| Mô hình của chúng tôi | Với việc hỏa táng, có một “cảm giác bạo lực đối với thi thể của người thân yêu”, vốn sẽ bị “biến thành một đống tro” trong thời gian rất ngắn thay vì trải qua một quá trình phân hủy “đồng hành cùng các giai đoạn đau buồn”. |
| Bản dịch chuẩn | Với việc hỏa táng, có “sự bạo lực đối với thi thể người thân yêu”, vốn sẽ bị “biến thành một đống tro” trong thời gian rất ngắn, chứ không phải sau một quá trình phân hủy, vốn “sẽ đồng hành cùng các giai đoạn đau buồn”. |

Bảng 3: Một vài ví dụ về các bản dịch dài do LSTM tạo ra, đặt cạnh các bản dịch chuẩn (ground truth). Có thể dùng Google translate để kiểm tra rằng các bản dịch này hợp lý. {#sutskever-2014-seq2seq-tab-3 .table tag=00E0}

Hình.

Hình 3: Đồ thị bên trái biểu diễn hiệu năng của hệ thống chúng tôi theo độ dài câu, trong đó trục x tương ứng với các câu kiểm thử được sắp xếp theo độ dài và được ghi nhãn bằng độ dài chuỗi thực tế. Không có sự suy giảm nào đối với các câu có ít hơn 35 từ, và chỉ có sự suy giảm nhỏ đối với những câu dài nhất. Đồ thị bên phải biểu diễn hiệu năng của LSTM trên các câu có số lượng từ hiếm tăng dần, trong đó trục x tương ứng với các câu kiểm thử được sắp xếp theo “thứ hạng tần suất từ trung bình”. {#sutskever-2014-seq2seq-fig-3 .figure tag=00E1}

việc thay thế thể chủ động bằng thể bị động. Các phép chiếu hai chiều được thu được bằng phân tích thành phần chính (PCA).
