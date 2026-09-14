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
section: "4"
section_title: Kết quả lý thuyết
tag: 00C6
kind: section
lang: vi
source: arxiv:1406.2661
pdf_sha256: ff5819e3a7b713c3bd3107b7de3d51fe0a347aa5d8444f0efdcf2345ef0a8b63
pdf_pages: 3-5
extraction: vision
extraction_model: gpt-6-astra
content_sha256: 0bced615be0a7a0d12c8d2473b04c70636d8e9b0fb668b4ae369a5f507256050
translated_from: content/en/goodfellow-2014-gan/04_theoretical_results.md
source_content_sha256: 1d15ad3c47f4ca03cc21c1352f04d4732982e16fb3695b4b962e91ca04507c05
translation_model: gpt-5
translation_run: 20260914T064759Z
glossary_version: 5
glossary_terms_sha256: 95f35b8eeca7e5d682ff5338deefc303c320897501e75661c72974f88e8865d4
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
roundtrip: differs-materially
roundtrip_run: 20260914T070941Z
---

Bộ sinh $G$ định nghĩa ngầm một phân phối xác suất $p_g$ là phân phối của các mẫu $G(z)$ thu được khi $z\sim p_z$. Do đó, chúng tôi muốn Thuật toán 1 hội tụ đến một bộ ước lượng tốt của $p_{\mathrm{data}}$, nếu được cung cấp đủ năng lực và thời gian huấn luyện. Các kết quả của phần này được thực hiện trong thiết lập phi tham số, chẳng hạn chúng tôi biểu diễn một mô hình có năng lực vô hạn bằng cách nghiên cứu sự hội tụ trong không gian của các hàm mật độ xác suất.

Chúng tôi sẽ chỉ ra trong phần 4.1 rằng trò chơi minimax này có một cực đại toàn cục tại $p_g=p_{\mathrm{data}}$. Sau đó, chúng tôi sẽ chỉ ra trong phần 4.2 rằng Thuật toán 1 tối ưu hóa Eq 1, từ đó thu được kết quả mong muốn.

**Thuật toán 1** Huấn luyện mạng đối sinh bằng hạ gradient ngẫu nhiên theo lô nhỏ. Số bước áp dụng cho bộ phân biệt, $k$, là một siêu tham số. Chúng tôi sử dụng $k = 1$, lựa chọn ít tốn kém nhất trong các thí nghiệm của mình.

**for** số vòng lặp huấn luyện **do**

**for** $k$ bước **do**

- Lấy mẫu một lô nhỏ gồm $m$ mẫu nhiễu $\{z^{(1)}, \ldots, z^{(m)}\}$ từ tiên nghiệm nhiễu $p_g(z)$.
- Lấy mẫu một lô nhỏ gồm $m$ ví dụ $\{x^{(1)}, \ldots, x^{(m)}\}$ từ phân phối sinh dữ liệu $p_{\text{data}}(x)$.
- Cập nhật bộ phân biệt bằng cách tăng gradient ngẫu nhiên của nó:

$$\nabla_{\theta_d}\frac{1}{m}\sum_{i=1}^{m}\left[\log D\left(x^{(i)}\right)+\log\left(1-D\left(G\left(z^{(i)}\right)\right)\right)\right].$$

**end for**

- Lấy mẫu một lô nhỏ gồm $m$ mẫu nhiễu $\{z^{(1)}, \ldots, z^{(m)}\}$ từ tiên nghiệm nhiễu $p_g(z)$.
- Cập nhật bộ sinh bằng cách giảm gradient ngẫu nhiên của nó:

$$\nabla_{\theta_g}\frac{1}{m}\sum_{i=1}^{m}\log\left(1-D\left(G\left(z^{(i)}\right)\right)\right).$$

**end for**

Các cập nhật dựa trên gradient có thể sử dụng bất kỳ quy tắc học dựa trên gradient tiêu chuẩn nào. Chúng tôi sử dụng động lượng trong các thí nghiệm của mình.

### 4.1 Tính tối ưu toàn cục của $p_g = p_{\text{data}}$ {#goodfellow-2014-gan-s4-1 .section tag=00C7}

Trước tiên, chúng tôi xét bộ phân biệt tối ưu $D$ đối với một bộ sinh $G$ bất kỳ đã cho.

**Mệnh đề 1.** *Với $G$ cố định, bộ phân biệt tối ưu $D$ là* {#goodfellow-2014-gan-prop-1 .statement tag=00C8}

$$D_G^*(x)=\frac{p_{\text{data}}(x)}{p_{\text{data}}(x)+p_g(x)}\tag{2}$$
{#goodfellow-2014-gan-eq-2 .equation tag=014B}

*Chứng minh.* Tiêu chuẩn huấn luyện cho bộ phân biệt D, với một bộ sinh G bất kỳ, là cực đại hóa đại lượng $V(G,D)$

$$\begin{aligned}
V(G,D)&=\int_x p_{\text{data}}(x)\log(D(x))dx+\int_z p_z(z)\log(1-D(g(z)))dz\\
&=\int_x p_{\text{data}}(x)\log(D(x))+p_g(x)\log(1-D(x))dx
\end{aligned}\tag{3}$$
{#goodfellow-2014-gan-eq-3 .equation tag=014C}

Với mọi $(a,b)\in\mathbb{R}^2\setminus\{0,0\}$, hàm $y\rightarrow a\log(y)+b\log(1-y)$ đạt cực đại của nó trong $[0,1]$ tại $\frac{a}{a+b}$. Bộ phân biệt không cần được định nghĩa bên ngoài $Supp(p_{\text{data}})\cup Supp(p_g)$, hoàn tất chứng minh. $\square$

Tiêu chuẩn huấn luyện cho $D$ có thể được diễn giải là cực đại hóa log-likelihood để ước lượng xác suất có điều kiện $P(Y=y|x)$, trong đó $Y$ chỉ ra liệu $x$ đến từ $p_{\text{data}}$ (với $y=1$) hay từ $p_g$ (với $y=0$). Trò chơi minimax trong Eq. 1 giờ đây có thể được viết lại thành:

$$\begin{aligned}
C(G)&=\max_D V(G,D)\\
&=\mathbb{E}_{x\sim p_{\text{data}}}\left[\log D_G^*(x)\right]+\mathbb{E}_{z\sim p_z}\left[\log(1-D_G^*(G(z)))\right]\\
&=\mathbb{E}_{x\sim p_{\text{data}}}\left[\log D_G^*(x)\right]+\mathbb{E}_{x\sim p_g}\left[\log(1-D_G^*(x))\right]\\
&=\mathbb{E}_{x\sim p_{\text{data}}}\left[\log\frac{p_{\text{data}}(x)}{p_{\text{data}}(x)+p_g(x)}\right]+\mathbb{E}_{x\sim p_g}\left[\log\frac{p_g(x)}{p_{\text{data}}(x)+p_g(x)}\right]
\end{aligned}\tag{4}$$
{#goodfellow-2014-gan-eq-4 .equation tag=014D}

**Định lý 1.** *Cực tiểu toàn cục của tiêu chuẩn huấn luyện ảo $C(G)$ đạt được khi và chỉ khi $p_g = p_{\mathrm{data}}$. Tại điểm đó, $C(G)$ đạt giá trị $-\log 4$.* {#goodfellow-2014-gan-thm-1 .statement tag=0111}

*Chứng minh.* Với $p_g = p_{\mathrm{data}}$, $D_G^*(x) = \frac{1}{2}$, (xét Eq. 2). Do đó, bằng cách xét Eq. 4 tại $D_G^*(x) = \frac{1}{2}$, ta có $C(G) = \log \frac{1}{2} + \log \frac{1}{2} = -\log 4$. Để thấy rằng đây là giá trị tốt nhất có thể của $C(G)$, chỉ đạt được khi $p_g = p_{\mathrm{data}}$, hãy xét

$$\mathbb{E}_{x\sim p_{\mathrm{data}}}[-\log 2] + \mathbb{E}_{x\sim p_g}[-\log 2] = -\log 4$$

và bằng cách trừ biểu thức này khỏi $C(G) = V(D_G^*, G)$, ta thu được:

$$C(G) = -\log(4) + KL\left(p_{\mathrm{data}} \left\| \frac{p_{\mathrm{data}} + p_g}{2}\right.\right) + KL\left(p_g \left\| \frac{p_{\mathrm{data}} + p_g}{2}\right.\right) \tag{5}$$
{#goodfellow-2014-gan-eq-5 .equation tag=014E}

trong đó KL là phân kỳ Kullback–Leibler. Trong biểu thức trên, ta nhận ra phân kỳ Jensen–Shannon giữa phân phối của mô hình và quá trình sinh dữ liệu:

$$C(G) = -\log(4) + 2 \cdot JSD(p_{\mathrm{data}} \| p_g) \tag{6}$$
{#goodfellow-2014-gan-eq-6 .equation tag=014F}

Vì phân kỳ Jensen–Shannon giữa hai phân phối luôn không âm và chỉ bằng không khi chúng bằng nhau, ta đã chứng minh rằng $C^* = -\log(4)$ là cực tiểu toàn cục của $C(G)$ và nghiệm duy nhất là $p_g = p_{\mathrm{data}}$, tức là mô hình sinh tái tạo hoàn hảo quá trình sinh dữ liệu. $\square$

### 4.2 Hội tụ của Thuật toán 1 {#goodfellow-2014-gan-s4-2 .section tag=0112}

**Mệnh đề 2.** *Nếu $G$ và $D$ có đủ năng lực, và tại mỗi bước của Thuật toán 1, bộ phân biệt được phép đạt tới tối ưu của nó với $G$ cho trước, và $p_g$ được cập nhật sao cho cải thiện tiêu chuẩn* {#goodfellow-2014-gan-prop-2 .statement tag=0113}

$$\mathbb{E}_{x\sim p_{\mathrm{data}}}[\log D_G^*(x)] + \mathbb{E}_{x\sim p_g}[\log(1 - D_G^*(x))]$$

*thì $p_g$ hội tụ đến $p_{\mathrm{data}}$*

*Chứng minh.* Xét $V(G, D) = U(p_g, D)$ như một hàm của $p_g$ theo cách đã thực hiện trong tiêu chuẩn trên. Lưu ý rằng $U(p_g, D)$ là hàm lồi theo $p_g$. Các đạo hàm dưới của một supremum của các hàm lồi bao gồm đạo hàm của hàm tại điểm đạt cực đại. Nói cách khác, nếu $f(x) = \sup_{\alpha\in\mathcal{A}} f_\alpha(x)$ và $f_\alpha(x)$ là hàm lồi theo $x$ với mọi $\alpha$, thì $\partial f_\beta(x) \in \partial f$ nếu $\beta = \arg \sup_{\alpha\in\mathcal{A}} f_\alpha(x)$. Điều này tương đương với việc tính một cập nhật gradient descent cho $p_g$ tại $D$ tối ưu ứng với $G$ tương ứng. $\sup_D U(p_g, D)$ là hàm lồi theo $p_g$ với một cực trị toàn cục duy nhất như đã chứng minh trong Định lý 1, do đó với các cập nhật $p_g$ đủ nhỏ, $p_g$ hội tụ đến $p_x$, hoàn tất chứng minh. $\square$

Trong thực tế, các mạng đối kháng biểu diễn một họ phân phối $p_g$ hữu hạn thông qua hàm $G(z; \theta_g)$, và chúng tôi tối ưu $\theta_g$ thay vì chính $p_g$. Việc sử dụng perceptron nhiều lớp để định nghĩa $G$ đưa vào nhiều điểm tới hạn trong không gian tham số. Tuy nhiên, hiệu năng xuất sắc của perceptron nhiều lớp trong thực tế cho thấy chúng là một mô hình hợp lý để sử dụng mặc dù thiếu các bảo đảm lý thuyết.
