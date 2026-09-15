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
section: "1"
section_title: Giới thiệu
tag: 00D1
kind: section
lang: vi
source: arxiv:1409.3215
pdf_sha256: 5c74e1db863e2d61b869c9b0603494b34c41fb05db1a4fa7f9a83d5a42b7350f
pdf_pages: 1-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 8c8a2ac9ca0238cccffe5070dc41d9bc761adeec76f7ca3be832dc105a18094d
translated_from: content/en/sutskever-2014-seq2seq/01_introduction.md
source_content_sha256: 3a99e0d81f0870e6b4ce8deaee70f27b549a3f218cf648ca11a73661aee83c12
translation_model: gpt-5
translation_run: 20260915T022520Z
glossary_version: 6
glossary_terms_sha256: 0d0a9334a40352952769479a6ad339487dd551fe3d836bae9914ea196d2f4310
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Các mạng nơ-ron sâu (DNN) là các mô hình học máy cực kỳ mạnh mẽ đạt được hiệu năng xuất sắc trên những bài toán khó như nhận dạng tiếng nói [13, 7] và nhận dạng đối tượng trực quan [[krizhevsky-2012-imagenet]], [6], [[lecun-1998-lenet]], [20]. DNN mạnh mẽ vì chúng có thể thực hiện tính toán song song tùy ý trong một số lượng bước khiêm tốn. Một ví dụ đáng ngạc nhiên về sức mạnh của DNN là khả năng sắp xếp $N$ số $N$-bit chỉ bằng cách sử dụng 2 lớp ẩn có kích thước bậc hai [27]. Vì vậy, mặc dù mạng nơ-ron có liên quan đến các mô hình thống kê truyền thống, chúng học một phép tính phức tạp. Hơn nữa, các DNN lớn có thể được huấn luyện bằng lan truyền ngược có giám sát bất cứ khi nào tập huấn luyện được gán nhãn có đủ thông tin để đặc tả các tham số của mạng. Do đó, nếu tồn tại một cấu hình tham số của một DNN lớn đạt được kết quả tốt (ví dụ, vì con người có thể giải quyết nhiệm vụ rất nhanh), lan truyền ngược có giám sát sẽ tìm ra các tham số này và giải quyết bài toán.

Mặc dù có tính linh hoạt và sức mạnh, DNN chỉ có thể được áp dụng cho các bài toán mà đầu vào và mục tiêu có thể được mã hóa hợp lý bằng các vectơ có số chiều cố định. Đây là một hạn chế đáng kể, vì nhiều bài toán quan trọng được biểu diễn tốt nhất bằng các chuỗi có độ dài không được biết trước. Ví dụ, nhận dạng tiếng nói và dịch máy là các bài toán tuần tự. Tương tự, hỏi đáp cũng có thể được xem như việc ánh xạ một chuỗi các từ biểu diễn câu hỏi thành một chuỗi các từ biểu diễn câu trả lời. Vì vậy, rõ ràng rằng một phương pháp độc lập với miền học cách ánh xạ các chuỗi thành các chuỗi sẽ hữu ích.

Các chuỗi đặt ra một thách thức đối với DNN vì chúng yêu cầu số chiều của các đầu vào và đầu ra phải được biết và cố định. Trong bài báo này, chúng tôi chỉ ra rằng một ứng dụng trực tiếp của kiến trúc Long Short-Term Memory (LSTM) [[hochreiter-1997-lstm]] có thể giải quyết các bài toán chuỗi sang chuỗi tổng quát. Ý tưởng là sử dụng một LSTM để đọc chuỗi đầu vào, từng timestep một, nhằm thu được một biểu diễn vectơ có số chiều cố định lớn, sau đó sử dụng một LSTM khác để trích xuất chuỗi đầu ra từ vectơ đó (fig. 1). LSTM thứ hai về cơ bản là một mô hình ngôn ngữ mạng nơ-ron hồi quy [[rumelhart-1986-backprop]], [23], [30], ngoại trừ việc nó được điều kiện hóa trên chuỗi đầu vào. Khả năng học thành công của LSTM trên dữ liệu có các phụ thuộc thời gian phạm vi dài khiến nó trở thành lựa chọn tự nhiên cho ứng dụng này do độ trễ thời gian đáng kể giữa các đầu vào và các đầu ra tương ứng của chúng (fig. 1).

Đã có một số nỗ lực liên quan nhằm giải quyết bài toán học chuỗi sang chuỗi tổng quát bằng mạng nơ-ron. Phương pháp của chúng tôi có liên quan chặt chẽ với Kalchbrenner và Blunsom [18], những người đầu tiên ánh xạ toàn bộ câu đầu vào thành vectơ, và có liên quan với Cho et al. [5], mặc dù phương pháp sau chỉ được sử dụng để chấm điểm lại các giả thuyết được tạo ra bởi một hệ thống dựa trên cụm từ. Graves [10] giới thiệu một cơ chế attention khả vi mới cho phép mạng nơ-ron tập trung vào các phần khác nhau của đầu vào, và một biến thể thanh lịch của ý tưởng này đã được áp dụng thành công cho dịch máy bởi Bahdanau et al. [2]. Connectionist Sequence Classification là một kỹ thuật phổ biến khác để ánh xạ các chuỗi thành các chuỗi bằng mạng nơ-ron, nhưng nó giả định một sự căn chỉnh đơn điệu giữa các đầu vào và đầu ra [11].

Figure.

Figure 1: Mô hình của chúng tôi đọc một câu đầu vào “ABC” và tạo ra “WXYZ” làm câu đầu ra. Mô hình dừng đưa ra dự đoán sau khi xuất ra token kết thúc câu. Lưu ý rằng LSTM đọc câu đầu vào theo chiều ngược lại, bởi vì việc này tạo ra nhiều phụ thuộc ngắn hạn trong dữ liệu khiến bài toán tối ưu hóa dễ dàng hơn nhiều. {#sutskever-2014-seq2seq-fig-1 .figure tag=00D2}

Kết quả chính của công trình này là như sau. Trong bài toán dịch tiếng Anh sang tiếng Pháp WMT’14, chúng tôi thu được điểm số BLEU là 34.81 bằng cách trực tiếp trích xuất các bản dịch từ một tổ hợp gồm 5 LSTM sâu (với 384M tham số và trạng thái có số chiều 8,000 cho mỗi LSTM) sử dụng một bộ giải mã tìm kiếm chùm tia đơn giản từ trái sang phải. Đây là kết quả tốt nhất đạt được bằng dịch trực tiếp với các mạng nơ-ron lớn. Để so sánh, điểm số BLEU của một đường cơ sở SMT trên tập dữ liệu này là 33.30 [29]. Điểm số BLEU 34.81 đạt được bởi một LSTM với từ vựng gồm 80k từ, vì vậy điểm số bị phạt bất cứ khi nào bản dịch tham chiếu chứa một từ không được bao phủ bởi 80k từ này. Kết quả này cho thấy một kiến trúc mạng nơ-ron có kích thước từ vựng nhỏ, tương đối chưa được tối ưu hóa, vẫn còn nhiều khả năng cải thiện, vượt trội hơn một hệ thống SMT dựa trên cụm từ.

Cuối cùng, chúng tôi sử dụng LSTM để chấm điểm lại các danh sách 1000-best được công khai của đường cơ sở SMT trên cùng bài toán [29]. Bằng cách đó, chúng tôi thu được điểm số BLEU là 36.5, cải thiện đường cơ sở thêm 3.2 điểm BLEU và gần với kết quả tốt nhất trước đây đã được công bố trên bài toán này (là 37.0 [9]).

Đáng ngạc nhiên, LSTM không gặp suy giảm trên các câu rất dài, mặc dù kinh nghiệm gần đây của các nhà nghiên cứu khác với những kiến trúc liên quan [26]. Chúng tôi có thể đạt kết quả tốt trên các câu dài vì chúng tôi đảo ngược thứ tự của các từ trong câu nguồn nhưng không đảo ngược các câu đích trong tập huấn luyện và tập kiểm thử. Bằng cách đó, chúng tôi đưa vào nhiều phụ thuộc ngắn hạn khiến bài toán tối ưu hóa đơn giản hơn nhiều (xem sec. 2 và 3.3). Do đó, SGD có thể học được các LSTM không gặp khó khăn với các câu dài. Mẹo đơn giản đảo ngược các từ trong câu nguồn là một trong những đóng góp kỹ thuật then chốt của công trình này.

Một thuộc tính hữu ích của LSTM là nó học cách ánh xạ một câu đầu vào có độ dài biến đổi thành một biểu diễn vectơ có số chiều cố định. Do các bản dịch có xu hướng là các câu diễn giải lại của các câu nguồn, mục tiêu huấn luyện dịch khuyến khích LSTM tìm ra các biểu diễn câu nắm bắt được ý nghĩa của chúng, vì các câu có ý nghĩa tương tự sẽ ở gần nhau trong khi các câu có ý nghĩa khác nhau sẽ ở xa nhau. Một đánh giá định tính hỗ trợ cho nhận định này, cho thấy mô hình của chúng tôi nhận biết được thứ tự từ và khá bất biến đối với thể chủ động và thể bị động.
