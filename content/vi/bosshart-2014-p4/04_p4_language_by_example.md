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
content_sha256: 176254a57de0487a5f1c0378924e366793733bea9a3c0c8cca1739eaeeef6aef
translated_from: content/en/bosshart-2014-p4/04_p4_language_by_example.md
source_content_sha256: 38febf1d6dc10fb4a818de5f4c83b224e6407fbf26b752bb33e90de845423d9d
translation_model: gpt-5
translation_run: 20260915T033315Z
glossary_version: 6
glossary_terms_sha256: 3a5b9dd3cd6211761c92d70db4c4910c364b1cae9e5e732eea77349f449c860b
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Chúng tôi khảo sát P4 bằng cách xem xét một ví dụ đơn giản một cách chi tiết. Nhiều triển khai mạng phân biệt giữa biên và lõi; các máy chủ đầu cuối được kết nối trực tiếp với các thiết bị biên, đến lượt các thiết bị này được kết nối với nhau qua một lõi có băng thông cao. Toàn bộ các giao thức đã được thiết kế để hỗ trợ kiến trúc này (chẳng hạn như MPLS [11] và PortLand [12]), chủ yếu nhằm đơn giản hóa việc chuyển tiếp trong lõi.

Xét một triển khai mạng L2 ví dụ với các chuyển mạch top-of-rack (ToR) ở biên được kết nối qua một lõi hai tầng. Chúng tôi giả định số lượng máy chủ đầu cuối đang tăng và các bảng L2 của lõi đang bị tràn. MPLS là một lựa chọn để đơn giản hóa lõi, nhưng việc triển khai một giao thức phân phối nhãn với nhiều tag là một nhiệm vụ khó khăn. PortLand có vẻ thú vị nhưng yêu cầu viết lại các địa chỉ MAC—có thể làm hỏng các công cụ gỡ lỗi mạng hiện có—và yêu cầu các agent mới để phản hồi các yêu cầu ARP.

P4 cho phép chúng tôi biểu diễn một giải pháp tùy chỉnh với những thay đổi tối thiểu đối với kiến trúc mạng. Chúng tôi gọi ví dụ đồ chơi của mình là mTag: nó kết hợp định tuyến phân cấp của PortLand với các tag đơn giản giống MPLS. Các tuyến đi qua lõi được mã hóa bằng một tag 32-bit gồm bốn trường một byte. Tag 32-bit có thể mang một “source route” hoặc một bộ định vị đích (giống Pseudo MAC của PortLand). Mỗi chuyển mạch lõi chỉ cần kiểm tra một byte của tag và chuyển mạch dựa trên thông tin đó. Trong ví dụ của chúng tôi, tag được thêm bởi chuyển mạch ToR đầu tiên, mặc dù nó cũng có thể được thêm bởi NIC của máy chủ đầu cuối.

Ví dụ mTag cố ý rất đơn giản để tập trung sự chú ý của chúng tôi vào ngôn ngữ P4. Chương trình P4 cho toàn bộ một chuyển mạch trên thực tế sẽ phức tạp hơn nhiều lần.

### 4.1 Các khái niệm P4 {#bosshart-2014-p4-s4-1 .section tag=0095}

Một chương trình P4 chứa các định nghĩa của những thành phần chính sau:
• Headers: Định nghĩa phần đầu mô tả chuỗi và cấu trúc của một loạt các trường. Nó bao gồm đặc tả độ rộng của các trường và các ràng buộc đối với giá trị trường.
• Parsers: Định nghĩa bộ phân tích cú pháp chỉ rõ cách xác định các phần đầu và các chuỗi phần đầu hợp lệ trong các gói tin.
• Tables: Các bảng match+action là cơ chế thực hiện xử lý gói tin. Chương trình P4 định nghĩa các trường mà một bảng có thể khớp và các hành động mà nó có thể thực thi.
• Actions: P4 hỗ trợ xây dựng các hành động phức tạp từ các primitive đơn giản, độc lập với giao thức. Các hành động phức tạp này có sẵn trong các bảng match+action.
• Control Programs: Chương trình điều khiển xác định thứ tự của các bảng match+action được áp dụng cho một gói tin. Một chương trình mệnh lệnh đơn giản mô tả luồng điều khiển giữa các bảng match+action.
Tiếp theo, chúng tôi chỉ ra cách mỗi thành phần này góp phần vào việc định nghĩa một bộ xử lý mTag lý tưởng hóa trong P4.

### 4.2 Các định dạng phần đầu {#bosshart-2014-p4-s4-2 .section tag=0096}

Một thiết kế bắt đầu bằng đặc tả các định dạng phần đầu. Một số ngôn ngữ dành riêng cho miền đã được đề xuất cho mục đích này [13, 14, 15]; P4 vay mượn một số ý tưởng từ chúng. Nhìn chung, mỗi phần đầu được đặc tả bằng cách khai báo một danh sách có thứ tự các tên trường cùng với độ rộng của chúng. Các chú thích trường tùy chọn cho phép đặt các ràng buộc về phạm vi giá trị hoặc độ dài tối đa đối với các trường có kích thước thay đổi. Ví dụ, các phần đầu Ethernet và VLAN tiêu chuẩn được đặc tả như sau:

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

Phần đầu mTag có thể được thêm vào mà không thay đổi các khai báo hiện có. Tên các trường cho biết lõi có hai lớp tổng hợp. Mỗi chuyển mạch lõi được lập trình với các quy tắc để kiểm tra một trong các byte này, được xác định bởi vị trí của nó trong hệ thống phân cấp và hướng di chuyển (lên hoặc xuống).

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

P4 giả định rằng chuyển mạch bên dưới có thể triển khai một máy trạng thái duyệt qua các phần đầu gói tin từ đầu đến cuối, đồng thời trích xuất các giá trị trường. Các giá trị trường được trích xuất được gửi tới các bảng match+action để xử lý.

P4 mô tả trực tiếp máy trạng thái này dưới dạng tập các chuyển tiếp từ phần đầu này sang phần đầu tiếp theo. Mỗi chuyển tiếp có thể được kích hoạt bởi các giá trị trong phần đầu hiện tại. Ví dụ, chúng tôi mô tả máy trạng thái mTag như sau.

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

Phân tích cú pháp bắt đầu ở trạng thái start và tiếp tục cho đến khi đạt đến một trạng thái dừng tường minh hoặc gặp một trường hợp không được xử lý (có thể được đánh dấu là lỗi). Khi đạt đến một trạng thái dành cho một phần đầu mới, máy trạng thái trích xuất phần đầu bằng cách sử dụng đặc tả của nó và tiếp tục xác định chuyển tiếp tiếp theo. Các phần đầu được trích xuất được chuyển tới quá trình xử lý match+action ở nửa sau của đường ống chuyển mạch.

Bộ phân tích cú pháp cho $mTag$ rất đơn giản: nó chỉ có bốn trạng thái. Các bộ phân tích cú pháp trong mạng thực tế đòi hỏi nhiều trạng thái hơn; ví dụ, bộ phân tích cú pháp do Gibb *et. al.* [16, Figure 3(e)] định nghĩa mở rộng đến hơn một trăm trạng thái.

### 4.4 Đặc tả bảng {#bosshart-2014-p4-s4-4 .section tag=0123}

Tiếp theo, lập trình viên mô tả cách các trường phần đầu đã được định nghĩa sẽ được khớp trong các giai đoạn match+action (ví dụ, chúng nên được khớp chính xác, theo phạm vi hay bằng wildcard?) và những hành động nào nên được thực hiện khi một khớp xảy ra.

Trong ví dụ $mTag$ đơn giản của chúng tôi, chuyển mạch biên khớp với đích L2 và VLAN ID, đồng thời chọn một $mTag$ để thêm vào phần đầu. Lập trình viên định nghĩa một bảng để khớp với các trường này và áp dụng một hành động để thêm phần đầu $mTag$ (xem bên dưới). Thuộc tính **reads** khai báo các trường cần khớp, được xác định cùng với kiểu khớp (exact, ternary, v.v.). Thuộc tính **actions** liệt kê các hành động khả dĩ có thể được bảng áp dụng cho một gói tin. Các hành động được giải thích trong phần tiếp theo. Thuộc tính **max_size** chỉ định số lượng mục nhập mà bảng cần hỗ trợ.

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

P4 định nghĩa một tập hợp các hành động nguyên thủy từ đó các hành động phức tạp hơn được xây dựng. Mỗi chương trình P4 khai báo một tập hợp các hàm hành động được tạo thành từ các hành động nguyên thủy; các hàm hành động này đơn giản hóa việc đặc tả và nạp dữ liệu cho bảng. P4 giả định thực thi song song các hành động nguyên thủy bên trong một hàm hành động. (Các chuyển mạch không có khả năng thực thi song song có thể mô phỏng ngữ nghĩa này.)

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

Nếu một hành động cần các tham số (ví dụ: giá trị up1 cho mTag), nó được cung cấp từ bảng khớp tại thời gian chạy.

Trong ví dụ này, chuyển mạch chèn mTag sau thẻ VLAN, sao chép ethertype của thẻ VLAN vào mTag để chỉ ra nội dung theo sau, và đặt ethertype của thẻ VLAN thành 0xaaaa để báo hiệu mTag. Không được trình bày ở đây là đặc tả hành động nghịch đảo để loại bỏ một mTag khỏi gói tin và bảng áp dụng hành động này trong các chuyển mạch biên.

Các hành động nguyên thủy của P4 bao gồm:
• set_field: Đặt một trường cụ thể trong phần đầu thành một giá trị. Các phép đặt có mặt nạ được hỗ trợ.
• copy_field: Sao chép một trường sang trường khác.
• add_header: Đặt một thể hiện phần đầu cụ thể (và tất cả các trường của nó) thành hợp lệ.
• remove_header: Xóa (“pop”) một phần đầu (và tất cả các trường của nó) khỏi một gói tin.
• increment: Tăng hoặc giảm giá trị trong một trường.
• checksum: Tính checksum trên một tập hợp các trường phần đầu nào đó (ví dụ: checksum IPv4).
Chúng tôi kỳ vọng hầu hết các triển khai chuyển mạch sẽ hạn chế xử lý hành động để chỉ cho phép những sửa đổi phần đầu nhất quán với định dạng gói tin đã được chỉ định.

### 4.6 Chương trình điều khiển {#bosshart-2014-p4-s4-6 .section tag=0106}

Một khi các bảng và hành động được định nghĩa, nhiệm vụ còn lại duy nhất là chỉ định luồng điều khiển từ bảng này đến bảng tiếp theo. Luồng điều khiển được đặc tả như một chương trình thông qua một tập hợp các hàm, điều kiện và tham chiếu bảng.

Hình.

Hình 4: Biểu đồ luồng cho ví dụ mTag. {#bosshart-2014-p4-fig-4 .figure tag=0098}

Hình 4 cho thấy biểu diễn đồ họa của luồng điều khiển mong muốn cho việc triển khai mTag trên các chuyển mạch biên. Sau khi phân tích cú pháp, bảng source_check xác minh tính nhất quán giữa gói tin nhận được và cổng đầu vào. Ví dụ, mTag chỉ nên xuất hiện trên các cổng được kết nối với các chuyển mạch lõi. source_check cũng loại bỏ mTag khỏi gói tin, ghi lại liệu gói tin có mTag trong metadata hay không. Các bảng sau đó trong đường ống có thể khớp với metadata này để tránh gắn thẻ lại gói tin.

Sau đó bảng local_switching được thực thi. Nếu bảng này “bỏ lỡ”, điều đó chỉ ra rằng gói tin không được gửi đến một máy chủ được kết nối cục bộ. Trong trường hợp đó, mTag_table (được định nghĩa ở trên) được áp dụng cho gói tin. Cả điều khiển chuyển tiếp cục bộ và lõi đều có thể được xử lý bởi bảng egress_check, bảng này xử lý trường hợp đích không xác định bằng cách gửi một thông báo lên ngăn xếp điều khiển SDN.

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
