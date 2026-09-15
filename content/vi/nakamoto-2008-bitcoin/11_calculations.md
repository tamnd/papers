---
paper: nakamoto-2008-bitcoin
title: 'Bitcoin: A Peer-to-Peer Electronic Cash System'
authors:
  - Satoshi Nakamoto
year: 2008
venue: bitcoin.org
field: security
section: "11"
section_title: Tính toán
tag: 000F
kind: section
lang: vi
source: https://bitcoin.org/bitcoin.pdf
pdf_sha256: b1674191a88ec5cdd733e4240a81803105dc412d6c6708d53ab94fc248f4f553
pdf_pages: 6-8
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 284e457cda8fbd2f66af8937d70c07a3692ca67e24b738e985ebbbbeeda19fab
translated_from: content/en/nakamoto-2008-bitcoin/11_calculations.md
source_content_sha256: e4e052e8ab33cb6257720a06a86d253d46ad4a09b8e1bc44c97a166261f46a58
translation_model: gpt-5
translation_run: 20260915T023027Z
glossary_version: 6
glossary_terms_sha256: 363c21723d588ca6b8032fd3e2b0aa8dc6ab225b1f9ca1b6e98d75976e8b0d0a
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Chúng tôi xem xét kịch bản một kẻ tấn công cố gắng tạo ra một chuỗi thay thế nhanh hơn chuỗi trung thực. Ngay cả khi điều này được thực hiện, nó không mở hệ thống cho các thay đổi tùy ý, chẳng hạn như tạo ra giá trị từ hư không hoặc lấy tiền chưa từng thuộc về kẻ tấn công. Các nút sẽ không chấp nhận một giao dịch không hợp lệ làm khoản thanh toán, và các nút trung thực sẽ không bao giờ chấp nhận một khối chứa chúng. Kẻ tấn công chỉ có thể cố gắng thay đổi một trong các giao dịch của chính mình để lấy lại tiền mà hắn vừa chi tiêu gần đây.

Cuộc đua giữa chuỗi trung thực và chuỗi của kẻ tấn công có thể được mô tả như một Random Walk Nhị thức. Sự kiện thành công là chuỗi trung thực được mở rộng thêm một khối, tăng khoảng cách dẫn trước của nó lên +1, và sự kiện thất bại là chuỗi của kẻ tấn công được mở rộng thêm một khối, làm giảm khoảng cách xuống -1.

Xác suất một kẻ tấn công bắt kịp từ một mức thiếu hụt nhất định tương tự với bài toán Gambler's Ruin. Giả sử một người đánh bạc với tín dụng không giới hạn bắt đầu từ mức thiếu hụt và thực hiện có thể là vô hạn lần thử để cố gắng đạt đến điểm hòa vốn. Chúng ta có thể tính xác suất anh ta từng đạt đến điểm hòa vốn, hoặc một kẻ tấn công từng bắt kịp chuỗi trung thực, như sau [8]:

$p =$ xác suất một nút trung thực tìm thấy khối tiếp theo
$q =$ xác suất kẻ tấn công tìm thấy khối tiếp theo
$q_z =$ xác suất kẻ tấn công sẽ từng bắt kịp từ phía sau z khối

$$
q_z = \begin{cases}
1 & \text{nếu } p \leq q \\
(q/p)^z & \text{nếu } p > q
\end{cases}
$$

Với giả định của chúng ta rằng $p > q$, xác suất giảm theo cấp số nhân khi số lượng khối mà kẻ tấn công phải bắt kịp tăng lên. Khi tỷ lệ cược chống lại hắn, nếu hắn không thực hiện một cú tiến lên may mắn ngay từ đầu, cơ hội của hắn trở nên nhỏ đến mức không đáng kể khi hắn tụt lại phía sau ngày càng xa.

Bây giờ chúng ta xem xét người nhận một giao dịch mới cần phải chờ bao lâu trước khi có đủ sự chắc chắn rằng người gửi không thể thay đổi giao dịch. Chúng ta giả định người gửi là một kẻ tấn công muốn khiến người nhận tin rằng hắn đã thanh toán cho người nhận trong một khoảng thời gian, sau đó chuyển nó thành thanh toán lại cho chính hắn sau khi một khoảng thời gian trôi qua. Người nhận sẽ được cảnh báo khi điều đó xảy ra, nhưng người gửi hy vọng sẽ quá muộn.

Người nhận tạo một cặp khóa mới và đưa khóa công khai cho người gửi ngay trước khi ký. Điều này ngăn người gửi chuẩn bị trước một chuỗi các khối bằng cách liên tục làm việc trên nó cho đến khi hắn đủ may mắn để vượt lên đủ xa, sau đó thực hiện giao dịch vào thời điểm đó. Khi giao dịch được gửi đi, người gửi không trung thực bắt đầu bí mật làm việc trên một chuỗi song song chứa một phiên bản thay thế của giao dịch của hắn.

Người nhận chờ cho đến khi giao dịch được thêm vào một khối và $z$ khối đã được liên kết sau nó. Anh ta không biết chính xác mức độ tiến triển mà kẻ tấn công đã đạt được, nhưng giả sử các khối trung thực mất thời gian trung bình kỳ vọng cho mỗi khối, tiến triển tiềm năng của kẻ tấn công sẽ là một phân phối Poisson với giá trị kỳ vọng:

$$
\lambda = z \frac{q}{p}
$$

Để có được xác suất kẻ tấn công vẫn có thể bắt kịp vào lúc này, chúng ta nhân mật độ Poisson cho mỗi mức tiến triển mà hắn có thể đã đạt được với xác suất hắn có thể bắt kịp từ điểm đó:

$$
\sum_{k=0}^{\infty} \frac{\lambda^k e^{-\lambda}}{k!} \left\{ \begin{array}{ll}
(q/p)^{(z-k)} & \text{nếu } k \leq z \\
1 & \text{nếu } k > z
\end{array} \right.
$$

Sắp xếp lại để tránh tính tổng phần đuôi vô hạn của phân phối...

$$
1 - \sum_{k=0}^{z} \frac{\lambda^k e^{-\lambda}}{k!} (1 - (q/p)^{(z-k)})
$$

Chuyển đổi sang mã C...

```c
#include <math.h>
double AttackerSuccessProbability(double q, int z)
{
    double p = 1.0 - q;
    double lambda = z * (q / p);
    double sum = 1.0;
    int i, k;
    for (k = 0; k <= z; k++)
    {
        double poisson = exp(-lambda);
        for (i = 1; i <= k; i++)
            poisson *= lambda / i;
        sum -= poisson * (1 - pow(q / p, z - k));
    }
    return sum;
}
```

Chạy một số kết quả, chúng ta có thể thấy xác suất giảm theo cấp số nhân với z.

```text
q=0.1
z=0    P=1.0000000
z=1    P=0.2045873
z=2    P=0.0509779
z=3    P=0.0131722
z=4    P=0.0034552
z=5    P=0.0009137
z=6    P=0.0002428
z=7    P=0.0000647
z=8    P=0.0000173
z=9    P=0.0000046
z=10   P=0.0000012
```

```text
q=0.3
z=0    P=1.0000000
z=5    P=0.1773523
z=10   P=0.0416605
z=15   P=0.0101008
z=20   P=0.0024804
z=25   P=0.0006132
z=30   P=0.0001522
z=35   P=0.0000379
z=40   P=0.0000095
z=45   P=0.0000024
z=50   P=0.0000006
```

Giải để tìm P nhỏ hơn 0.1%...

```text
P < 0.001
q=0.10   z=5
q=0.15   z=8
q=0.20   z=11
q=0.25   z=15
q=0.30   z=24
q=0.35   z=41
q=0.40   z=89
q=0.45   z=340
```
