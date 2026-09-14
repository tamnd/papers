---
paper: jouppi-2017-tpu
title: In-Datacenter Performance Analysis of a Tensor Processing Unit
authors:
  - Norman P. Jouppi
  - Cliff Young
  - Nishant Patil
  - David Patterson
  - Gaurav Agrawal
  - Raminder Bajwa
  - Sarah Bates
  - Suresh Bhatia
  - Nan Boden
  - Al Borchers
year: 2017
venue: ISCA
field: architecture
section_title: Front Matter
tag: 017C
kind: front
lang: vi
source: arxiv:1704.04760
pdf_sha256: 19793e4ae1486630ac45a12facabc0e80609dd679db8ca7a3a040f8bf0d8e0be
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 3a586984fa2be41d03e0a7b3fe896b01bb272fbab6a40f790054d1a3b7eee4a9
translated_from: content/en/jouppi-2017-tpu/00_front.md
source_content_sha256: 5e82a2a4149491a3ae9dcb43423377e04e03c2b0afe6955ad18f21a9b10a1674
translation_model: gpt-5
translation_run: 20260914T201546Z
glossary_version: 6
glossary_terms_sha256: 1f83355a83baacb04f1185b8bd47b133f28d2f764f5d7ae919d5d9d0d7e083ee
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Phân tích hiệu năng trong trung tâm dữ liệu của một Tensor Processing Unit™

Norman P. Jouppi, Cliff Young, Nishant Patil, David Patterson, Gaurav Agrawal, Raminder Bajwa, Sarah Bates, Suresh Bhatia, Nan Boden, Al Borchers, Rick Boyle, Pierre-luc Cantin, Clifford Chao, Chris Clark, Jeremy Coriell, Mike Daley, Matt Dau, Jeffrey Dean, Ben Gelb, Tara Vazir Ghaemmaghami, Rajendra Gottipati, William Gulland, Robert Hagmann, C. Richard Ho, Doug Hogberg, John Hu, Robert Hundt, Dan Hurt, Julian Ibarz, Aaron Jaffey, Alek Jaworski, Alexander Kaplan, Harshit Khaitan, Daniel Killebrew, Andy Koch, Naveen Kumar, Steve Lacy, James Laudon, James Law, Diemthu Le, Chris Leary, Zhuyuan Liu, Kyle Lucke, Alan Lundin, Gordon MacKean, Adriana Maggiore, Maire Mahony, Kieran Miller, Rahul Nagarajan, Ravi Narayanaswami, Ray Ni, Kathy Nix, Thomas Norrie, Mark Omernick, Narayana Penukonda, Andy Phelps, Jonathan Ross, Matt Ross, Amir Salek, Emad Samadiani, Chris Severn, Gregory Sizikov, Matthew Snelham, Jed Souter, Dan Steinberg, Andy Swing, Mercedes Tan, Gregory Thorson, Bo Tian, Horia Toma, Erick Tuttle, Vijay Vasudevan, Richard Walter, Walter Wang, Eric Wilcox, and Doe Hyun Yoon
Google, Inc., Mountain View, CA USA
Email: {jouppi, cliffy, nishantpatil, davidpatterson} @google.com

Sẽ được trình bày tại Hội nghị chuyên đề quốc tế lần thứ 44 về Kiến trúc Máy tính (ISCA), Toronto, Canada, ngày 26 tháng 6 năm 2017.

Tóm tắt
Nhiều kiến trúc sư cho rằng những cải thiện lớn về chi phí-năng lượng-hiệu năng hiện nay phải đến từ phần cứng chuyên biệt theo miền. Bài báo này đánh giá một ASIC tùy biến, được gọi là Tensor Processing Unit (TPU), được triển khai trong các trung tâm dữ liệu từ năm 2015 để tăng tốc giai đoạn suy luận của các mạng nơ-ron (NN). Thành phần cốt lõi của TPU là một đơn vị nhân ma trận MAC 65,536 8-bit, cung cấp thông lượng cực đại 92 TeraOps/giây (TOPS) và một bộ nhớ lớn (28 MiB) trên chip do phần mềm quản lý. Mô hình thực thi xác định của TPU phù hợp với yêu cầu thời gian đáp ứng ở phân vị thứ 99 của các ứng dụng NN của chúng tôi hơn so với các tối ưu hóa biến thiên theo thời gian của CPU và GPU (cache, thực thi ngoài thứ tự, đa luồng, đa tiến trình, nạp trước, ...) vốn giúp tăng thông lượng trung bình nhiều hơn là bảo đảm độ trễ. Việc thiếu các tính năng như vậy giúp giải thích tại sao, mặc dù có vô số MAC và một bộ nhớ lớn, TPU tương đối nhỏ và tiêu thụ ít điện năng. Chúng tôi so sánh TPU với CPU Intel Haswell cấp server và GPU Nvidia K80, là những bộ xử lý cùng thời được triển khai trong cùng các trung tâm dữ liệu. Tải công việc của chúng tôi, được viết bằng khung TensorFlow cấp cao, sử dụng các ứng dụng NN trong môi trường sản xuất (MLP, CNN và LSTM), đại diện cho 95% nhu cầu suy luận NN của các trung tâm dữ liệu của chúng tôi. Mặc dù mức sử dụng thấp đối với một số ứng dụng, trung bình TPU nhanh hơn khoảng 15X - 30X so với GPU hoặc CPU cùng thời, với TOPS/Watt cao hơn khoảng 30X - 80X. Hơn nữa, việc sử dụng bộ nhớ GDDR5 của GPU trong TPU sẽ tăng gấp ba TOPS đạt được và nâng TOPS/Watt lên gần 70X so với GPU và 200X so với CPU.
Từ khóa–DNN, MLP, CNN, RNN, LSTM, mạng nơ-ron, kiến trúc chuyên biệt theo miền, bộ tăng tốc
