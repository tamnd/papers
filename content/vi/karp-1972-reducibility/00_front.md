---
paper: karp-1972-reducibility
title: Reducibility Among Combinatorial Problems
authors:
  - Richard M. Karp
year: 1972
venue: Complexity of Computer Computations
field: theory
section_title: Front Matter
tag: 003A
kind: front
lang: vi
source: https://doi.org/10.1007/978-1-4684-2001-2_9
pdf_sha256: ae57cf641ae4f1924bdc4d7ef865edb2411c44e3040e8e546d01f1545e288e89
pdf_pages: 1-2
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 49cbc02977313333ebfee92226ce7f4a90ca90ec8817ad2c231f7027419ad56d
translated_from: content/en/karp-1972-reducibility/00_front.md
source_content_sha256: c04b8bbc6c2a7aebbe904b3efaa08d0fc2f24fa6d7276ff92ca2ec383b049ad8
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: 6d9e5417e9b1c2ea0332cc910589a2f1f7989033c37ee6d1610f4912cdc9e218
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
roundtrip: same
roundtrip_run: 20260914T214350Z
---

Khả quy giữa các bài toán tổ hợp

Richard M. Karp

Lời giới thiệu của Richard M. Karp

Trong suốt những năm 1960, tôi nghiên cứu các bài toán tối ưu hóa tổ hợp, bao gồm thiết kế mạch logic cùng Paul Roth, cân bằng dây chuyền lắp ráp và bài toán người bán hàng rong cùng Mike Held. Những trải nghiệm này giúp tôi nhận ra rằng các bài toán tối ưu hóa rời rạc tưởng chừng đơn giản có thể ẩn chứa những mầm mống của sự bùng nổ tổ hợp. Công trình của Dantzig, Fulkerson, Hoffman, Edmonds, Lawler và những người tiên phong khác về luồng mạng, ghép cặp và matroid đã giúp tôi làm quen với những thuật toán thanh lịch và hiệu quả đôi khi có thể xây dựng được. Các bài báo của Jack Edmonds và một vài cuộc thảo luận quan trọng với ông đã thu hút sự chú ý của tôi đến sự phân biệt then chốt giữa khả năng giải được trong thời gian đa thức và khả năng giải được trong thời gian siêu đa thức. Tôi cũng chịu ảnh hưởng bởi sự nhấn mạnh của Jack về các định lý min-max như một công cụ để kiểm chứng nhanh các nghiệm tối ưu, điều đã báo trước định nghĩa của Steve Cook về lớp độ phức tạp NP. Một ảnh hưởng khác là đề xuất của George Dantzig rằng quy hoạch nguyên có thể đóng vai trò như một khuôn dạng phổ quát cho các bài toán tối ưu hóa tổ hợp.

Trong suốt những năm 1960, tôi theo dõi những phát triển trong lý thuyết độ phức tạp tính toán, do Rabin, Blum, Hartmanis, Stearns và những người khác tiên phong. Vào cuối những năm 1960, trong khi giảng dạy một khóa học về lý thuyết hàm đệ quy tại Học viện Bách khoa Brooklyn, tôi nghiên cứu cuốn sách tuyệt đẹp của Hartley Rogers về lý thuyết hàm đệ quy. Trải nghiệm này giúp tôi nhận thức sâu sắc vai trò then chốt của các phép quy dẫn trong lý thuyết hàm đệ quy, đồng thời khiến tôi tự hỏi liệu các phép quy dẫn dưới đệ quy có thể đóng một vai trò tương tự trong lý thuyết độ phức tạp hay không, nhưng khi đó tôi vẫn chưa theo đuổi sự tương tự này.
