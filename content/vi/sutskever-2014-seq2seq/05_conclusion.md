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
section: "5"
section_title: Kết luận
tag: "00E3"
kind: section
lang: vi
source: arxiv:1409.3215
pdf_sha256: 5c74e1db863e2d61b869c9b0603494b34c41fb05db1a4fa7f9a83d5a42b7350f
pdf_pages: "8"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 5211d1a3bdae6d3d1da19579c7d5bb25c08066ff7d8c932b565a03d56fee0ec3
translated_from: content/en/sutskever-2014-seq2seq/05_conclusion.md
source_content_sha256: 27656d29e6fde66bd2643ea1faf08882d3461b2b145d2784d77cbc36e390b758
translation_model: gpt-5
translation_run: 20260915T023922Z
glossary_version: 6
glossary_terms_sha256: 0d0a9334a40352952769479a6ad339487dd551fe3d836bae9914ea196d2f4310
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Trong công trình này, chúng tôi đã chỉ ra rằng một LSTM sâu lớn, có từ vựng hạn chế và hầu như không đưa ra giả định nào về cấu trúc bài toán, có thể vượt trội hơn một hệ thống dựa trên SMT tiêu chuẩn có từ vựng không giới hạn trong một tác vụ MT quy mô lớn. Thành công của phương pháp đơn giản dựa trên LSTM của chúng tôi trên MT cho thấy nó có thể hoạt động tốt trên nhiều bài toán học chuỗi khác, với điều kiện chúng có đủ dữ liệu huấn luyện.

Chúng tôi ngạc nhiên trước mức độ cải thiện đạt được bằng cách đảo ngược các từ trong các câu nguồn. Chúng tôi kết luận rằng điều quan trọng là tìm ra một cách mã hóa bài toán có số lượng phụ thuộc ngắn hạn lớn nhất, vì chúng làm cho bài toán học đơn giản hơn nhiều. Cụ thể, trong khi chúng tôi không thể huấn luyện một RNN tiêu chuẩn trên bài toán dịch không đảo ngược (được minh họa trong hình 1), chúng tôi tin rằng một RNN tiêu chuẩn có thể dễ dàng được huấn luyện khi các câu nguồn được đảo ngược (mặc dù chúng tôi chưa xác minh điều này bằng thực nghiệm).

Chúng tôi cũng ngạc nhiên trước khả năng của LSTM trong việc dịch chính xác các câu rất dài. Ban đầu chúng tôi tin rằng LSTM sẽ thất bại trên các câu dài do bộ nhớ hạn chế của nó, và các nhà nghiên cứu khác đã báo cáo hiệu năng kém trên các câu dài với một mô hình tương tự của chúng tôi [5, 2, 26]. Tuy nhiên, các LSTM được huấn luyện trên tập dữ liệu đã đảo ngược gặp rất ít khó khăn khi dịch các câu dài.

Quan trọng nhất, chúng tôi đã chứng minh rằng một phương pháp đơn giản, trực tiếp và tương đối chưa được tối ưu hóa có thể vượt trội hơn một hệ thống SMT, vì vậy các nghiên cứu tiếp theo có khả năng sẽ dẫn đến độ chính xác dịch thuật còn cao hơn nữa. Những kết quả này cho thấy phương pháp của chúng tôi có khả năng sẽ hoạt động tốt trên các bài toán chuỗi sang chuỗi đầy thách thức khác.
