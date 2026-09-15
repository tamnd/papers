---
paper: goodfellow-2014-gan
title: Generative Adversarial Nets
authors:
  - Ian J. Goodfellow
  - Jean Pouget-Abadie
  - Mehdi Mirza
  - Bing Xu
  - David Warde-Farley
  - Sherjil Ozair
  - Aaron Courville
  - Yoshua Bengio
year: 2014
venue: NIPS
field: ai-ml
section: "3"
section_title: Mạng đối kháng
tag: 00C3
kind: section
lang: vi
source: arxiv:1406.2661
pdf_sha256: ff5819e3a7b713c3bd3107b7de3d51fe0a347aa5d8444f0efdcf2345ef0a8b63
pdf_pages: 2-3
extraction: vision
extraction_model: gpt-6-astra
content_sha256: 2a95c16bc4e8d2ce7d913a5a8259e993f73b43ed2d358135b7f6a4a456be9ff5
translated_from: content/en/goodfellow-2014-gan/03_adversarial_nets.md
source_content_sha256: ff7821dc77a57394deb3070ec820aedcf565d4263a8f0633cecb1bd742a41264
translation_model: gpt-6-astra
translation_run: 20260915T022520Z
glossary_version: 6
glossary_terms_sha256: 0d0a9334a40352952769479a6ad339487dd551fe3d836bae9914ea196d2f4310
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Khung mô hình hóa đối kháng (adversarial modeling) dễ áp dụng nhất khi cả hai mô hình đều là perceptron đa lớp (multilayer perceptron). Để học phân phối $p_g$ của bộ sinh trên dữ liệu $\boldsymbol{x}$, chúng tôi định nghĩa một phân phối tiên nghiệm trên các biến nhiễu đầu vào $p_z(\boldsymbol{z})$, sau đó biểu diễn một ánh xạ tới không gian dữ liệu dưới dạng $G(\boldsymbol{z}; \theta_g)$, trong đó $G$ là một hàm khả vi được biểu diễn bằng một perceptron đa lớp có các tham số $\theta_g$. Chúng tôi cũng định nghĩa một perceptron đa lớp thứ hai $D(\boldsymbol{x}; \theta_d)$ xuất ra một giá trị vô hướng duy nhất. $D(\boldsymbol{x})$ biểu diễn xác suất $\boldsymbol{x}$ đến từ dữ liệu thay vì từ $p_g$. Chúng tôi huấn luyện $D$ để tối đa hóa xác suất gán nhãn đúng cho cả các ví dụ huấn luyện lẫn các mẫu từ $G$. Đồng thời, chúng tôi huấn luyện $G$ để tối thiểu hóa $\log(1 - D(G(\boldsymbol{z})))$:

Nói cách khác, $D$ và $G$ tham gia trò chơi minimax hai người chơi sau đây với hàm giá trị $V(G,D)$:

$$\min_G \max_D V(D,G) = \mathbb{E}_{x\sim p_{\mathrm{data}}(x)}[\log D(x)] + \mathbb{E}_{z\sim p_z(z)}[\log(1-D(G(z)))]. \tag{1}$$
{#goodfellow-2014-gan-eq-1 .equation tag=00C4}

Trong phần tiếp theo, chúng tôi trình bày một phân tích lý thuyết về mạng đối kháng, về cơ bản cho thấy tiêu chí huấn luyện cho phép khôi phục phân phối sinh dữ liệu khi $G$ và $D$ có đủ năng lực biểu diễn, tức là trong giới hạn phi tham số. Xem Hình 1 để có cách giải thích ít hình thức hơn và mang tính sư phạm hơn về phương pháp này. Trong thực tế, chúng tôi phải triển khai trò chơi bằng một phương pháp số có tính lặp. Việc tối ưu hóa $D$ đến khi hoàn tất trong vòng lặp bên trong của quá trình huấn luyện đòi hỏi chi phí tính toán quá lớn, và trên các tập dữ liệu hữu hạn sẽ dẫn đến quá khớp (overfitting). Thay vào đó, chúng tôi luân phiên thực hiện $k$ bước tối ưu hóa $D$ và một bước tối ưu hóa $G$. Nhờ vậy, $D$ được duy trì gần nghiệm tối ưu của nó, miễn là $G$ thay đổi đủ chậm. Chiến lược này tương tự cách quá trình huấn luyện SML/PCD [31, 29] duy trì các mẫu từ một chuỗi Markov từ bước học này sang bước học tiếp theo nhằm tránh phải thực hiện giai đoạn khởi động của chuỗi Markov trong vòng lặp bên trong của quá trình học. Thủ tục này được trình bày một cách hình thức trong Thuật toán 1.

Trong thực tế, phương trình 1 có thể không cung cấp đủ gradient để $G$ học tốt. Ở giai đoạn đầu của quá trình học, khi $G$ còn kém, $D$ có thể bác bỏ các mẫu với độ tin cậy cao vì chúng rõ ràng khác với dữ liệu huấn luyện. Trong trường hợp này, $\log(1-D(G(z)))$ bão hòa. Thay vì huấn luyện $G$ để tối thiểu hóa $\log(1-D(G(z)))$, chúng tôi có thể huấn luyện $G$ để tối đa hóa $\log D(G(z))$. Hàm mục tiêu này dẫn đến cùng một điểm bất động của động lực học của $G$ và $D$ nhưng cung cấp các gradient mạnh hơn nhiều ở giai đoạn đầu của quá trình học.

Hình 1: Các mạng đối kháng sinh (generative adversarial nets) được huấn luyện bằng cách đồng thời cập nhật phân phối phân biệt ($D$, màu xanh dương, nét đứt) để phân biệt các mẫu từ phân phối sinh dữ liệu (màu đen, nét chấm) $p_x$ với các mẫu từ phân phối sinh $p_g$ ($G$) (màu xanh lá, nét liền). Đường ngang phía dưới là miền lấy mẫu của $z$, trong trường hợp này là lấy mẫu đều. Đường ngang phía trên là một phần miền của $x$. Các mũi tên hướng lên cho thấy cách ánh xạ $x=G(z)$ tạo ra phân phối không đều $p_g$ trên các mẫu đã biến đổi. $G$ co lại ở các vùng có mật độ cao và giãn ra ở các vùng có mật độ thấp của $p_g$. (a) Xét một cặp đối kháng gần hội tụ: $p_g$ tương tự $p_{\mathrm{data}}$ và $D$ là một bộ phân loại chính xác một phần. (b) Trong vòng lặp bên trong của thuật toán, $D$ được huấn luyện để phân biệt các mẫu với dữ liệu, hội tụ đến $D^*(x)=\frac{p_{\mathrm{data}}(x)}{p_{\mathrm{data}}(x)+p_g(x)}$. (c) Sau một lần cập nhật $G$, gradient của $D$ đã dẫn $G(z)$ dịch chuyển đến các vùng có khả năng được phân loại là dữ liệu cao hơn. (d) Sau một số bước huấn luyện, nếu $G$ và $D$ có đủ năng lực biểu diễn, chúng sẽ đạt đến một điểm mà cả hai đều không thể cải thiện vì $p_g=p_{\mathrm{data}}$. Bộ phân biệt (discriminator) không thể phân biệt hai phân phối, tức là $D(x)=\frac{1}{2}$. {#goodfellow-2014-gan-fig-1 .figure tag=00C5}
