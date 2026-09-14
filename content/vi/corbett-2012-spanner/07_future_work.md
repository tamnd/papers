---
paper: corbett-2012-spanner
title: 'Spanner: Google''s Globally-Distributed Database'
authors:
  - James C. Corbett
  - Jeffrey Dean
  - Michael Epstein
  - Andrew Fikes
  - Christopher Frost
  - J. J. Furman
  - Sanjay Ghemawat
  - Andrey Gubarev
  - Christopher Heiser
  - Peter Hochschild
year: 2012
venue: OSDI
field: databases
section: "7"
section_title: Công việc tương lai
tag: 00BD
kind: section
lang: vi
source: http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.258.9924
pdf_sha256: 61875779e75f603d21aefba6d9bd9816d4dd0c18cf41089f43707249e24bbf88
pdf_pages: 12-13
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: abc3b9fad5d416871ccff4e5d419c8d950815f2d11d5b997c24a875a8bd5748b
translated_from: content/en/corbett-2012-spanner/07_future_work.md
source_content_sha256: cb00969c20baf78a45379d261623dec886a4ef22b525d47269e983908ec64148
translation_model: gpt-5
translation_run: 20260914T201546Z
glossary_version: 6
glossary_terms_sha256: a534ae50d60bff0e03804fd3c150e37d1876484531ab87df9c72dc4d0c455eb2
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Chúng tôi đã dành phần lớn năm vừa qua làm việc với nhóm F1 để chuyển backend quảng cáo của Google từ MySQL sang Spanner. Chúng tôi đang tích cực cải thiện các công cụ giám sát và hỗ trợ của nó, cũng như tinh chỉnh hiệu năng của nó. Ngoài ra, chúng tôi đã làm việc để cải thiện chức năng và hiệu năng của hệ thống sao lưu/khôi phục của mình. Hiện tại chúng tôi đang triển khai ngôn ngữ lược đồ Spanner, việc bảo trì tự động các chỉ mục thứ cấp, và việc phân mảnh lại dựa trên tải tự động. Về dài hạn, có một vài tính năng mà chúng tôi dự định nghiên cứu. Thực hiện các thao tác đọc song song một cách lạc quan có thể là một chiến lược có giá trị để theo đuổi, nhưng các thử nghiệm ban đầu đã chỉ ra rằng việc triển khai đúng không hề tầm thường. Ngoài ra, chúng tôi dự định cuối cùng sẽ hỗ trợ các thay đổi trực tiếp của các cấu hình Paxos [22, 34].

Vì chúng tôi kỳ vọng nhiều ứng dụng sẽ sao chép dữ liệu của chúng trên các trung tâm dữ liệu tương đối gần nhau, TrueTime $\epsilon$ có thể ảnh hưởng đáng kể đến hiệu năng. Chúng tôi không thấy trở ngại không thể vượt qua nào trong việc giảm $\epsilon$ xuống dưới 1ms. Các khoảng thời gian truy vấn time-master có thể được giảm xuống, và các tinh thể đồng hồ tốt hơn tương đối rẻ. Độ trễ truy vấn time-master có thể được giảm bằng công nghệ mạng được cải thiện, hoặc thậm chí có thể tránh được thông qua công nghệ phân phối thời gian thay thế.

Cuối cùng, có những lĩnh vực rõ ràng cần được cải thiện. Mặc dù Spanner có khả năng mở rộng theo số lượng nút, các cấu trúc dữ liệu cục bộ của nút có hiệu năng tương đối kém trên các truy vấn SQL phức tạp, bởi vì chúng được thiết kế cho các truy cập khóa-giá trị đơn giản. Các thuật toán và cấu trúc dữ liệu từ tài liệu DB có thể cải thiện đáng kể hiệu năng của một nút đơn. Thứ hai, việc di chuyển dữ liệu tự động giữa các trung tâm dữ liệu để đáp ứng các thay đổi trong tải của máy khách từ lâu đã là một mục tiêu của chúng tôi, nhưng để mục tiêu đó có hiệu quả, chúng tôi cũng cần khả năng di chuyển các tiến trình ứng dụng máy khách giữa các trung tâm dữ liệu theo một cách tự động, phối hợp. Việc di chuyển các tiến trình đặt ra vấn đề còn khó khăn hơn nữa về quản lý việc thu nhận và phân bổ tài nguyên giữa các trung tâm dữ liệu.
