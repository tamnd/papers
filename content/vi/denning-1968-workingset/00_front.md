---
paper: denning-1968-workingset
title: The Working Set Model for Program Behavior
authors:
  - Peter J. Denning
year: 1968
venue: Communications of the ACM
field: systems
section_title: Front Matter
tag: 004E
kind: front
lang: vi
source: https://doi.org/10.1145/800001.811670
pdf_sha256: 3585991156b07c7e878ea9dff16ef7721401adff09ee328f5ee247b016289e0f
pdf_pages: 1-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 1cbf8f6856a7ad358953ba365f110d41fb07200f93a7bf33056795ba09aaf0c8
translated_from: content/en/denning-1968-workingset/00_front.md
source_content_sha256: 1a0f412b8f796cd2bda77a1d352f7e118a00f27155e048d18edd6ba0345da370
translation_model: gpt-5
translation_run: 20260918T122832Z
glossary_version: 7
glossary_terms_sha256: f834761938c11bca59f7cb79948997ed0706af48cd70392678452699c034a7ad
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Mô hình Working Set cho Hành vi của Chương trình

Peter J. Denning

Viện Công nghệ Massachusetts, Cambridge, Massachusetts

Có lẽ lý do cơ bản nhất dẫn đến sự thiếu vắng một phương pháp xử lý tổng quát về phân bổ tài nguyên trong các hệ thống máy tính hiện đại là sự thiếu vắng một mô hình đầy đủ về hành vi của chương trình. Trong bài báo này, một mô hình mới, "mô hình working set", được phát triển. Working set của các trang liên kết với một tiến trình, được định nghĩa là tập hợp các trang được sử dụng gần đây nhất của nó, cung cấp tri thức quan trọng cho việc quản lý động các bộ nhớ phân trang. "Tiến trình" và "working set" được chỉ ra là những biểu hiện của cùng một hoạt động tính toán đang diễn ra; sau đó "nhu cầu bộ xử lý" và "nhu cầu bộ nhớ" được định nghĩa; và phân bổ tài nguyên được xây dựng thành bài toán cân bằng các nhu cầu với thiết bị sẵn có.

TỪ KHÓA VÀ CỤM TỪ: các khái niệm chung về hệ điều hành, đa xử lý, đa chương trình, hệ điều hành, hành vi chương trình, các mô hình chương trình, phân bổ tài nguyên, lập lịch, phân bổ lưu trữ

PHÂN LOẠI CR: 4.30, 4.32

1. Giới thiệu

Phân bổ tài nguyên là một công việc phức tạp. Gần đây đã có nhiều cuộc thảo luận về lập lịch tiến trình và quản lý bộ nhớ lõi, tuy nhiên việc phát triển các kỹ thuật đã tiến triển độc lập theo cả hai hướng này. Không ai phủ nhận rằng cần có một phương pháp tiếp cận thống nhất. Ở đây chúng tôi chỉ ra rằng có thể phát triển một phương pháp tiếp cận thống nhất. Bắt đầu từ quan sát rằng mọi chương trình đang chạy đều đặt ra các nhu cầu đồng thời lên tất cả tài nguyên hệ thống, đặc biệt là bộ xử lý và bộ nhớ, cuối cùng chúng tôi định nghĩa "nhu cầu hệ thống"; bài toán phân bổ sẽ bao gồm việc cân bằng các nhu cầu với các tài nguyên sẵn có.
