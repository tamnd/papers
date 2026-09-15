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
section_title: Front Matter
tag: 00D0
kind: front
lang: vi
source: arxiv:1409.3215
pdf_sha256: 5c74e1db863e2d61b869c9b0603494b34c41fb05db1a4fa7f9a83d5a42b7350f
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: cbec336800d2289edeebc06e6d7e5a44c4cfcbe347831149bd959abe8e22c942
translated_from: content/en/sutskever-2014-seq2seq/00_front.md
source_content_sha256: 297862e336f823108331063e88f49bbe2e2107273660a937dd89aeaa8f360e25
translation_model: gpt-6-astra
translation_run: 20260915T022520Z
glossary_version: 6
glossary_terms_sha256: 0d0a9334a40352952769479a6ad339487dd551fe3d836bae9914ea196d2f4310
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Học từ chuỗi sang chuỗi với mạng nơ-ron (neural network)

Ilya Sutskever
Google
ilyasu@google.com

Oriol Vinyals
Google
vinyals@google.com

Quoc V. Le
Google
qvl@google.com

Tóm tắt

Mạng nơ-ron sâu (Deep Neural Networks, DNNs) là những mô hình mạnh đã đạt hiệu năng xuất sắc trên các tác vụ học khó. Mặc dù DNN hoạt động tốt khi có sẵn các tập huấn luyện lớn đã được gán nhãn, chúng không thể được dùng để ánh xạ chuỗi sang chuỗi. Trong bài báo này, chúng tôi trình bày một cách tiếp cận đầu cuối (end-to-end) tổng quát cho việc học chuỗi, với rất ít giả định về cấu trúc chuỗi. Phương pháp của chúng tôi sử dụng một mạng bộ nhớ dài-ngắn hạn (Long Short-Term Memory, LSTM) nhiều lớp để ánh xạ chuỗi đầu vào thành một vectơ có số chiều cố định, rồi dùng một LSTM sâu khác để giải mã chuỗi đích từ vectơ đó. Kết quả chính của chúng tôi là trên tác vụ dịch từ tiếng Anh sang tiếng Pháp của tập dữ liệu WMT’14, các bản dịch do LSTM tạo ra đạt điểm số BLEU là 34.8 trên toàn bộ tập kiểm thử, trong đó điểm số BLEU của LSTM bị trừ đối với các từ ngoài từ vựng. Ngoài ra, LSTM không gặp khó khăn với các câu dài. Để so sánh, một hệ thống dịch máy thống kê dựa trên cụm từ (SMT) đạt điểm số BLEU là 33.3 trên cùng tập dữ liệu. Khi chúng tôi dùng LSTM để xếp hạng lại 1000 giả thuyết do hệ thống SMT nói trên tạo ra, điểm số BLEU của hệ thống tăng lên 36.5, gần với kết quả tốt nhất trước đó trên tác vụ này. LSTM cũng học được các biểu diễn cụm từ và câu hợp lý, nhạy với thứ tự từ và tương đối bất biến đối với thể chủ động và thể bị động. Cuối cùng, chúng tôi nhận thấy rằng việc đảo ngược thứ tự từ trong tất cả các câu nguồn (nhưng không đảo trong các câu đích) cải thiện rõ rệt hiệu năng của LSTM, vì thao tác này tạo ra nhiều phụ thuộc ngắn hạn giữa câu nguồn và câu đích, giúp bài toán tối ưu hóa trở nên dễ hơn.
