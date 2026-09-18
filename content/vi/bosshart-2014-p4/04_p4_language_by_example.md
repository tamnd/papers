---
paper: bosshart-2014-p4
title: 'P4: Programming Protocol-Independent Packet Processors'
authors:
  - Pat Bosshart
  - Dan Daly
  - Glen Gibb
  - Martin Izzard
  - Nick McKeown
  - Jennifer Rexford
  - Cole Schlesinger
  - Dan Talayco
  - Amin Vahdat
  - George Varghese
  - David Walker
year: 2014
venue: ACM SIGCOMM Computer Communication Review
field: networks
section: "4"
section_title: P4 NGÔN NGỮ QUA VÍ DỤ
tag: "0094"
kind: section
lang: vi
source: arxiv:1312.1719
pdf_sha256: 2bb0ccb7b5410868efdecc9ef5208d235c6f3aa75dee84aa992751aed117a42f
pdf_pages: 4-6
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 3cd115af08f4b6fe62a3c48f8d774b3a24414c381e17bcb1c7f4b72d562a87c1
translated_from: content/en/bosshart-2014-p4/04_p4_language_by_example.md
source_content_sha256: 38febf1d6dc10fb4a818de5f4c83b224e6407fbf26b752bb33e90de845423d9d
translation_model: gpt-5
translation_run: 20260918T153717Z
glossary_version: 7
glossary_terms_sha256: 5bfb74d0e4b3e9a8237f78ceae59e221549684c174791655271c5455f7fd5e4e
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Chúng tôi khám phá P4 bằng cách xem xét một ví dụ đơn giản một cách chi tiết. Nhiều triển khai mạng phân biệt giữa biên và lõi; các máy chủ cuối được kết nối trực tiếp với các thiết bị biên, và các thiết bị này lại được kết nối với nhau thông qua một lõi băng thông cao. Các giao thức hoàn chỉnh đã được thiết kế để hỗ trợ kiến trúc này (chẳng hạn như MPLS [11] và PortLand [12]), chủ yếu nhằm đơn giản hóa việc chuyển tiếp trong lõi.

Xét một ví dụ triển khai mạng L2 với các chuyển mạch top-of-rack (ToR) ở biên được kết nối bởi một lõi hai tầng. Chúng tôi giả sử số lượng máy chủ cuối đang tăng lên và các bảng L2 lõi đang bị tràn. MPLS là một lựa chọn để đơn giản hóa lõi, nhưng việc triển khai một giao thức phân phối nhãn với nhiều thẻ là một nhiệm vụ khó khăn. PortLand có vẻ thú vị nhưng yêu cầu viết lại các địa chỉ MAC, có khả năng làm hỏng các công cụ gỡ lỗi mạng hiện có, và yêu cầu các tác nhân mới phản hồi các yêu cầu ARP.

P4 cho phép chúng tôi biểu diễn một giải pháp tùy chỉnh với những thay đổi tối thiểu đối với kiến trúc mạng. Chúng tôi gọi ví dụ đồ chơi của mình là mTag: nó kết hợp định tuyến phân cấp của PortLand với các thẻ đơn giản giống MPLS. Các tuyến đường qua lõi được mã hóa bằng một thẻ 32-bit gồm bốn trường một byte. Thẻ 32-bit có thể mang một “tuyến nguồn” hoặc một bộ định vị đích (giống như Pseudo MAC của PortLand). Mỗi chuyển mạch lõi chỉ cần kiểm tra một byte của thẻ và chuyển mạch dựa trên thông tin đó. Trong ví dụ của chúng tôi, thẻ được thêm bởi chuyển mạch ToR đầu tiên, mặc dù nó cũng có thể được thêm bởi NIC của máy chủ cuối.

Ví dụ mTag được cố ý làm rất đơn giản để tập trung sự chú ý của chúng tôi vào ngôn ngữ lập trình P4. Chương trình P4 cho toàn bộ một chuyển mạch trong thực tế sẽ phức tạp hơn nhiều lần.

### 4.1 Các khái niệm P4 {#bosshart-2014-p4-s4-1 .section tag=0095}

Một chương trình P4 chứa các định nghĩa của các thành phần chính sau:
• Phần đầu: Một định nghĩa phần đầu mô tả chuỗi và cấu trúc của một chuỗi các trường. Nó bao gồm đặc tả về độ rộng trường và các ràng buộc đối với giá trị trường.
• Bộ phân tích cú pháp: Một định nghĩa bộ phân tích cú pháp đặc tả cách xác định các phần đầu và các chuỗi phần đầu hợp lệ bên trong các gói tin.
• Bảng: Các bảng so khớp+hành động là cơ chế để thực hiện xử lý gói tin. Chương trình P4 định nghĩa các trường mà một bảng có thể so khớp và các hành động mà nó có thể thực thi.
• Hành động: P4 hỗ trợ xây dựng các hành động phức tạp từ các nguyên thủy đơn giản độc lập với giao thức. Các hành động phức tạp này có sẵn bên trong các bảng so khớp+hành động.
• Chương trình điều khiển: Chương trình điều khiển xác định thứ tự của các bảng so khớp+hành động được áp dụng cho một gói tin. Một chương trình mệnh lệnh đơn giản mô tả luồng điều khiển giữa các bảng so khớp+hành động.
Tiếp theo, chúng tôi chỉ ra cách mỗi thành phần này đóng góp vào việc định nghĩa một bộ xử lý mTag lý tưởng hóa trong P4.

### 4.2 Các định dạng phần đầu {#bosshart-2014-p4-s4-2 .section tag=0096}

Một thiết kế bắt đầu với đặc tả của các định dạng phần đầu. Một số ngôn ngữ dành riêng cho miền đã được đề xuất cho việc này [13, 14, 15]; P4 mượn một số ý tưởng từ chúng. Nói chung, mỗi phần đầu được đặc tả bằng cách khai báo một danh sách có thứ tự các tên trường cùng với độ rộng của chúng. Các chú thích trường tùy chọn cho phép các ràng buộc về khoảng giá trị hoặc độ dài tối đa cho các trường có kích thước thay đổi. Ví dụ, các phần đầu Ethernet và VLAN chuẩn được đặc tả như sau:

```text
header ethernet {
    fields {
        dst_addr : 48; // width in bits
        src_addr : 48;
        ethertype : 16;
    }
}

header vlan {
    fields {
        pcp : 3;
        cfi : 1;
        vid : 12;
        ethertype : 16;
    }
}
```

Phần đầu mTag có thể được thêm vào mà không thay đổi các khai báo hiện có. Các tên trường chỉ ra rằng lõi có hai lớp tập hợp. Mỗi chuyển mạch lõi được lập trình với các quy tắc để kiểm tra một trong các byte này được xác định bởi vị trí của nó trong phân cấp và hướng di chuyển (lên hoặc xuống).

```text
header mTag {
    fields {
        up1 : 8;
        up2 : 8;
        down1 : 8;
        down2 : 8;
        ethertype : 16;
    }
}
```

### 4.3 Bộ phân tích cú pháp gói tin {#bosshart-2014-p4-s4-3 .section tag=0097}

P4 giả định rằng chuyển mạch bên dưới có thể triển khai một máy trạng thái duyệt qua các phần đầu gói tin từ đầu đến cuối, trích xuất các giá trị trường khi nó thực hiện. Các giá trị trường được trích xuất được gửi đến các bảng so khớp+hành động để xử lý.

P4 mô tả trực tiếp máy trạng thái này dưới dạng tập hợp các chuyển tiếp từ một phần đầu sang phần đầu tiếp theo. Mỗi chuyển tiếp có thể được kích hoạt bởi các giá trị trong phần đầu hiện tại. Ví dụ, chúng tôi mô tả máy trạng thái mTag như sau.

```text
parser start{
ethernet;
}

parser ethernet {
    switch(ethertype) {
        case 0x8100: vlan;
        case 0x9100: vlan;
        case 0x800: ipv4;
        // Other cases
    }
}

parser vlan {
    switch(ethertype) {
        case 0xaaaa: mTag;
        case 0x800: ipv4;
        // Other cases
    }
}

parser mTag {
    switch(ethertype) {
        case 0x800: ipv4;
        // Other cases
    }
}
```

Việc phân tích cú pháp bắt đầu ở trạng thái bắt đầu và tiếp tục cho đến khi đạt tới một trạng thái dừng tường minh hoặc gặp một trường hợp chưa được xử lý (có thể được đánh dấu là một lỗi). Khi đạt tới một trạng thái dành cho một phần đầu mới, máy trạng thái trích xuất phần đầu bằng cách sử dụng đặc tả của nó và tiếp tục xác định chuyển tiếp tiếp theo. Các phần đầu được trích xuất được chuyển tiếp đến xử lý so khớp+hành động ở phần sau của đường ống chuyển mạch.

Bộ phân tích cú pháp cho $mTag$ rất đơn giản: nó chỉ có bốn trạng thái. Các bộ phân tích cú pháp trong các mạng thực tế yêu cầu nhiều trạng thái hơn; ví dụ, bộ phân tích cú pháp được định nghĩa bởi Gibb *et. al.* [16, Figure 3(e)] mở rộng đến hơn một trăm trạng thái.

### 4.4 Đặc tả bảng {#bosshart-2014-p4-s4-4 .section tag=0123}

Tiếp theo, lập trình viên mô tả cách các trường phần đầu đã định nghĩa được so khớp trong các giai đoạn so khớp+hành động (ví dụ, chúng có nên là các so khớp chính xác, các khoảng, hay các ký tự đại diện?) và những hành động nào nên được thực hiện khi một so khớp xảy ra.

Trong ví dụ $mTag$ đơn giản của chúng tôi, chuyển mạch biên khớp với đích L2 và VLAN ID, đồng thời chọn một $mTag$ để thêm vào phần đầu. Lập trình viên định nghĩa một bảng để khớp trên các trường này và áp dụng một hành động để thêm phần đầu $mTag$ (xem bên dưới). Thuộc tính **reads** khai báo các trường cần khớp, được xác định kèm theo kiểu khớp (exact, ternary, v.v.). Thuộc tính **actions** liệt kê các hành động khả dĩ có thể được áp dụng cho một gói tin bởi bảng. Các hành động được giải thích trong phần tiếp theo. Thuộc tính **max_size** chỉ định số mục nhập mà bảng cần hỗ trợ.

Đặc tả bảng cho phép trình biên dịch quyết định lượng bộ nhớ cần thiết và kiểu bộ nhớ (ví dụ: TCAM hoặc SRAM) để triển khai bảng.

```text
table mTag_table {
reads {
        ethernet.dst_addr : exact;
        vlan.vid : exact;
    }
    actions {
        // At runtime, entries are programmed with params
        // for the mTag action. See below.
        add_mTag;
    }
    max_size : 20000;
}
```

Để đầy đủ và phục vụ thảo luận sau này, chúng tôi trình bày các định nghĩa ngắn gọn về những bảng khác được tham chiếu bởi Chương trình điều khiển (\S4.6).

```text
table source_check {
    // Verify mtag only on ports to the core
    reads {
        mtag : valid; // Was mtag parsed?
        metadata.ingress_port : exact;
    }
    actions { // Each table entry specifies *one* action
        // If inappropriate mTag, send to CPU
        fault_to_cpu;
// If mtag found, strip and record in metadata
        strip_mtag;
// Otherwise, allow the packet to continue
        pass;
    }
    max_size : 64; // One rule per port
}

table local_switching {
    // Reads destination and checks if local
    // If miss occurs, goto mtag table.
}

table egress_check {
    // Verify egress is resolved
    // Do not retag packets received with tag
    // Reads egress and whether packet was mTagged
}
```

### 4.5 Đặc tả hành động {#bosshart-2014-p4-s4-5 .section tag=0124}

P4 định nghĩa một tập hợp các hành động nguyên thủy từ đó các hành động phức tạp hơn được xây dựng. Mỗi chương trình P4 khai báo một tập hợp các hàm hành động được tạo thành từ các hành động nguyên thủy; các hàm hành động này đơn giản hóa đặc tả và việc nạp dữ liệu cho bảng. P4 giả định thực thi song song các hành động nguyên thủy bên trong một hàm hành động. (Các chuyển mạch không có khả năng thực thi song song có thể mô phỏng ngữ nghĩa này.)

Hành động **add_mTag** được đề cập ở trên được triển khai như sau:

```text
action add_mTag(up1, up2, down1, down2, egr_spec) {
    add_header(mTag);
    // Copy VLAN ethertype to mTag
    copy_field(mTag.ethertype, vlan.ethertype);
// Set VLAN’s ethertype to signal mTag
set_field(vlan.ethertype, 0xaaaa);
set_field(mTag.up1, up1);
set_field(mTag.up2, up2);
set_field(mTag.down1, down1);
set_field(mTag.down2, down2);
// Set the destination egress port as well
set_field(metadata.egress_spec, egr_spec);
}
```

Nếu một hành động cần các tham số (ví dụ, giá trị up1 cho mTag), nó được cung cấp từ bảng khớp tại thời gian chạy.

Trong ví dụ này, chuyển mạch chèn mTag sau thẻ VLAN, sao chép ethertype của thẻ VLAN vào mTag để chỉ ra nội dung tiếp theo, và đặt ethertype của thẻ VLAN thành 0xaaaa để báo hiệu mTag. Không được trình bày là đặc tả hành động nghịch đảo để loại bỏ một mTag khỏi một gói tin và bảng để áp dụng hành động này trong các chuyển mạch biên.

Các hành động nguyên thủy của P4 bao gồm:
• set_field: Đặt một trường cụ thể trong một phần đầu thành một giá trị. Các phép đặt có mặt nạ được hỗ trợ.
• copy_field: Sao chép một trường sang một trường khác.
• add_header: Đặt một thể hiện phần đầu cụ thể (và tất cả các trường của nó) là hợp lệ.
• remove_header: Xóa (“pop”) một phần đầu (và tất cả các trường của nó) khỏi một gói tin.
• increment: Tăng hoặc giảm giá trị trong một trường.
• checksum: Tính toán checksum trên một tập hợp các trường phần đầu nào đó (ví dụ, checksum IPv4).
Chúng tôi kỳ vọng rằng hầu hết các triển khai chuyển mạch sẽ hạn chế xử lý hành động để chỉ cho phép các sửa đổi phần đầu nhất quán với định dạng gói tin được đặc tả.

### 4.6 Chương trình điều khiển {#bosshart-2014-p4-s4-6 .section tag=0106}

Một khi các bảng và hành động được định nghĩa, nhiệm vụ còn lại duy nhất là đặc tả luồng điều khiển từ một bảng đến bảng tiếp theo. Luồng điều khiển được đặc tả như một chương trình thông qua một tập hợp các hàm, điều kiện và tham chiếu bảng.

Hình.

Hình 4: Biểu đồ luồng cho ví dụ mTag. {#bosshart-2014-p4-fig-4 .figure tag=0098}

Hình 4 cho thấy biểu diễn đồ họa của luồng điều khiển mong muốn cho việc triển khai mTag trên các chuyển mạch biên. Sau khi phân tích cú pháp, bảng source_check xác minh tính nhất quán giữa gói tin nhận được và cổng vào. Ví dụ, các mTag chỉ nên xuất hiện trên các cổng được kết nối với các chuyển mạch lõi. source_check cũng loại bỏ các mTag khỏi gói tin, ghi lại liệu gói tin có một mTag trong metadata hay không. Các bảng sau đó trong đường ống có thể khớp trên metadata này để tránh gắn thẻ lại gói tin.

Bảng local_switching sau đó được thực thi. Nếu bảng này “misses,” điều đó chỉ ra rằng gói tin không được gửi đến một máy chủ được kết nối cục bộ. Trong trường hợp đó, mTag_table (được định nghĩa ở trên) được áp dụng cho gói tin. Cả điều khiển chuyển tiếp cục bộ và lõi có thể được xử lý bởi bảng egress_check, bảng này xử lý trường hợp đích không xác định bằng cách gửi một thông báo lên ngăn xếp điều khiển SDN.

Biểu diễn mệnh lệnh của đường ống xử lý gói tin này như sau:

```text
control main() {
    // Verify mTag state and port are consistent
    table(source_check);
// If no error from source_check, continue
    if (!defined(metadata.ingress_error)) {
        // Attempt to switch to end hosts
        table(local_switching);
if (!defined(metadata.egress_spec)) {
            // Not a known local host; try mtagging
            table(mTag_table);
        }
// Check for unknown egress state or bad retagging with mTag.
        table(egress_check);
    }
}
```
