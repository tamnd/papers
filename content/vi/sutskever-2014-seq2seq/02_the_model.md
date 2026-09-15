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
section: "2"
section_title: Mô hình
tag: 00D3
kind: section
lang: vi
source: arxiv:1409.3215
pdf_sha256: 5c74e1db863e2d61b869c9b0603494b34c41fb05db1a4fa7f9a83d5a42b7350f
pdf_pages: "3"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 8aba2bb8a3fc0bfaa70c79884039fe41e834cb37ad0910980b789f12793819e7
translated_from: content/en/sutskever-2014-seq2seq/02_the_model.md
source_content_sha256: 21f617bbcc3b5cb3f29d8f7e988b09162e5b5ffa5bb001402dac52ca880cccc4
translation_model: gpt-5
translation_run: 20260915T023922Z
glossary_version: 6
glossary_terms_sha256: 0d0a9334a40352952769479a6ad339487dd551fe3d836bae9914ea196d2f4310
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Mạng nơ-ron hồi quy (Recurrent Neural Network - RNN) (RNN) [31], [[rumelhart-1986-backprop]] là một sự khái quát hóa tự nhiên của các mạng nơ-ron truyền thẳng cho các chuỗi. Cho một chuỗi các đầu vào $(x_1, \ldots, x_T)$, một RNN tiêu chuẩn tính toán một chuỗi các đầu ra $(y_1, \ldots, y_T)$ bằng cách lặp lại phương trình sau:

$$
h_t = \mathrm{sigm}\left(W^{hx} x_t + W^{hh} h_{t-1}\right)
$$

$$
y_t = W^{yh} h_t
$$

RNN có thể dễ dàng ánh xạ các chuỗi sang các chuỗi bất cứ khi nào sự căn chỉnh giữa các đầu vào và đầu ra được biết trước. Tuy nhiên, chưa rõ cách áp dụng RNN cho các bài toán mà chuỗi đầu vào và đầu ra có độ dài khác nhau với các mối quan hệ phức tạp và không đơn điệu.

Chiến lược đơn giản nhất cho việc học chuỗi tổng quát là ánh xạ chuỗi đầu vào tới một vectơ có kích thước cố định bằng cách sử dụng một RNN, sau đó ánh xạ vectơ tới chuỗi mục tiêu bằng một RNN khác (cách tiếp cận này cũng đã được Cho và cộng sự sử dụng [5]). Mặc dù về nguyên tắc nó có thể hoạt động vì RNN được cung cấp tất cả thông tin liên quan, việc huấn luyện các RNN sẽ khó khăn do các phụ thuộc dài hạn phát sinh (hình 1) [14], [4], [[hochreiter-1997-lstm]], [15]. Tuy nhiên, Long Short-Term Memory (LSTM) [[hochreiter-1997-lstm]] được biết đến với khả năng học các bài toán có phụ thuộc thời gian tầm xa, vì vậy một LSTM có thể thành công trong thiết lập này.

Mục tiêu của LSTM là ước lượng xác suất có điều kiện $p(y_1, \ldots, y_{T'} | x_1, \ldots, x_T )$ trong đó $(x_1, \ldots, x_T)$ là một chuỗi đầu vào và $y_1, \ldots, y_{T'}$ là chuỗi đầu ra tương ứng của nó, với độ dài $T'$ có thể khác $T$. LSTM tính toán xác suất có điều kiện này bằng cách trước tiên thu được biểu diễn có số chiều cố định $v$ của chuỗi đầu vào $(x_1, \ldots, x_T)$ được cho bởi trạng thái ẩn cuối cùng của LSTM, sau đó tính toán xác suất của $y_1, \ldots, y_{T'}$ bằng một công thức LSTM-LM tiêu chuẩn có trạng thái ẩn ban đầu được đặt thành biểu diễn $v$ của $x_1, \ldots, x_T$:

$$
p(y_1, \ldots, y_{T'} | x_1, \ldots, x_T ) = \prod_{t=1}^{T'} p(y_t | v, y_1, \ldots, y_{t-1})
$$

Trong phương trình này, mỗi phân phối $p(y_t | v, y_1, \ldots, y_{t-1})$ được biểu diễn bằng một softmax trên tất cả các từ trong từ vựng. Chúng tôi sử dụng công thức LSTM từ Graves [10]. Lưu ý rằng chúng tôi yêu cầu mỗi câu kết thúc bằng một ký hiệu kết thúc câu đặc biệt “<EOS>”, cho phép mô hình xác định một phân phối trên các chuỗi có mọi độ dài có thể. Lược đồ tổng thể được trình bày trong hình 1, trong đó LSTM được minh họa tính toán biểu diễn của “A”, “B”, “C”, “<EOS>” và sau đó sử dụng biểu diễn này để tính toán xác suất của “W”, “X”, “Y”, “Z”, “<EOS>”.

Các mô hình thực tế của chúng tôi khác với mô tả trên theo ba cách quan trọng. Thứ nhất, chúng tôi sử dụng hai LSTM khác nhau: một cho chuỗi đầu vào và một cho chuỗi đầu ra, bởi vì việc này làm tăng số lượng tham số mô hình với chi phí tính toán không đáng kể và giúp việc huấn luyện LSTM trên nhiều cặp ngôn ngữ đồng thời trở nên tự nhiên [18]. Thứ hai, chúng tôi nhận thấy rằng các LSTM sâu vượt trội đáng kể so với các LSTM nông, vì vậy chúng tôi chọn một LSTM có bốn lớp. Thứ ba, chúng tôi nhận thấy rằng việc đảo ngược thứ tự các từ của câu đầu vào có giá trị rất lớn. Ví dụ, thay vì ánh xạ câu $a, b, c$ sang câu $\alpha, \beta, \gamma$, LSTM được yêu cầu ánh xạ $c, b, a$ sang $\alpha, \beta, \gamma$, trong đó $\alpha, \beta, \gamma$ là bản dịch của $a, b, c$. Theo cách này, $a$ ở gần $\alpha$, $b$ khá gần với $\beta$, và cứ tiếp tục như vậy, một thực tế giúp SGD dễ dàng “thiết lập liên lạc” giữa đầu vào và đầu ra. Chúng tôi nhận thấy phép biến đổi dữ liệu đơn giản này cải thiện đáng kể hiệu năng của LSTM.
