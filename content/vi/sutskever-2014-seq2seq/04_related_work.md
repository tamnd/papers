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
section: "4"
section_title: Công trình liên quan
tag: "00E2"
kind: section
lang: vi
source: arxiv:1409.3215
pdf_sha256: 5c74e1db863e2d61b869c9b0603494b34c41fb05db1a4fa7f9a83d5a42b7350f
pdf_pages: 7-8
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: fe7174ad3821b7addc38dfa71b001811c6617d7adc228ff9804cbc64db66ad5f
translated_from: content/en/sutskever-2014-seq2seq/04_related_work.md
source_content_sha256: 1178ccdfc25a7a7177eee797fc64d04ae751c650315c47d5cdf0205019e8eb70
translation_model: gpt-5
translation_run: 20260915T023922Z
glossary_version: 6
glossary_terms_sha256: 0d0a9334a40352952769479a6ad339487dd551fe3d836bae9914ea196d2f4310
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Có một lượng lớn các công trình nghiên cứu về các ứng dụng của mạng nơ-ron vào dịch máy. Cho đến nay, cách đơn giản nhất và hiệu quả nhất để áp dụng Mô hình Ngôn ngữ RNN (RNNLM) [23] hoặc

Mô hình Ngôn ngữ Mạng Nơ-ron Truyền thẳng (NNLM) [3] vào một tác vụ MT là chấm điểm lại các danh sách n-best của một đường cơ sở MT mạnh [22], điều này cải thiện đáng tin cậy chất lượng dịch.

Gần đây hơn, các nhà nghiên cứu đã bắt đầu tìm hiểu các phương pháp đưa thông tin về ngôn ngữ nguồn vào NNLM. Các ví dụ của hướng nghiên cứu này bao gồm Auli et al. [1], những người kết hợp một NNLM với một mô hình chủ đề của câu đầu vào, qua đó cải thiện hiệu năng chấm điểm lại. Devlin et al. [8] đã theo một cách tiếp cận tương tự, nhưng họ tích hợp NNLM của mình vào bộ giải mã của một hệ thống MT và sử dụng thông tin căn chỉnh của bộ giải mã để cung cấp cho NNLM những từ hữu ích nhất trong câu đầu vào. Cách tiếp cận của họ đạt thành công lớn và đem lại những cải thiện đáng kể so với đường cơ sở của họ.

Công trình của chúng tôi có liên hệ chặt chẽ với Kalchbrenner và Blunsom [18], những người đầu tiên ánh xạ câu đầu vào thành một vectơ rồi ánh xạ ngược trở lại thành một câu, mặc dù họ ánh xạ các câu thành các vectơ bằng cách sử dụng mạng nơ-ron tích chập, vốn làm mất thứ tự của các từ. Tương tự như công trình này, Cho et al. [5] đã sử dụng một kiến trúc RNN giống LSTM để ánh xạ các câu thành các vectơ và ngược lại, mặc dù trọng tâm chính của họ là tích hợp mạng nơ-ron của mình vào một hệ thống SMT. Bahdanau et al. [2] cũng thử nghiệm các bản dịch trực tiếp bằng một mạng nơ-ron sử dụng cơ chế attention để khắc phục hiệu năng kém trên các câu dài mà Cho et al. [5] gặp phải và đạt được các kết quả đáng khích lệ. Tương tự, Pouget-Abadie et al. [26] đã cố gắng giải quyết vấn đề bộ nhớ của Cho et al. [5] bằng cách dịch các phần của câu nguồn theo cách tạo ra các bản dịch mượt mà, tương tự như một cách tiếp cận dựa trên cụm từ. Chúng tôi nghi ngờ rằng họ có thể đạt được những cải thiện tương tự chỉ bằng cách huấn luyện các mạng của mình trên các câu nguồn đã được đảo ngược.

Huấn luyện end-to-end cũng là trọng tâm của Hermann et al. [12], có mô hình biểu diễn các đầu vào và đầu ra bằng các mạng truyền thẳng, và ánh xạ chúng tới các điểm tương tự trong không gian. Tuy nhiên, cách tiếp cận của họ không thể tạo ra các bản dịch trực tiếp: để có được một bản dịch, họ cần thực hiện tra cứu vectơ gần nhất trong cơ sở dữ liệu các câu đã được tính toán trước, hoặc chấm điểm lại một câu.
