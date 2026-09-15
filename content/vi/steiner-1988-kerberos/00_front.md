---
paper: steiner-1988-kerberos
title: 'Kerberos: An Authentication Service for Open Network Systems'
authors:
  - Jennifer G. Steiner
  - Clifford Neuman
  - Jeffrey I. Schiller
year: 1988
venue: USENIX Winter Conference
field: security
section_title: Front Matter
tag: 019C
kind: front
lang: vi
source: http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.112.9002
pdf_sha256: 2dd6604c96afde95681d25fe32df9834aad32274d1bdbb44dd5f69d6b9660f59
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 6bb272bcb2eb9d211d64bb12275239ebedb6fb531578102b0401b0cdf5a1af6e
translated_from: content/en/steiner-1988-kerberos/00_front.md
source_content_sha256: 9e474d18dcc9446a1011c0bf72b3a6a42cb6d6041611756a306268973021818e
translation_model: gpt-5
translation_run: 20260915T013833Z
glossary_version: 6
glossary_terms_sha256: 363c21723d588ca6b8032fd3e2b0aa8dc6ab225b1f9ca1b6e98d75976e8b0d0a
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Kerberos: Một Dịch vụ Xác thực cho các Hệ thống Mạng Mở

Jennifer G. Steiner
Project Athena
Massachusetts Institute of Technology
Cambridge, MA 02139
steiner@ATHENA.MIT.EDU

Clifford Neuman†
Department of Computer Science, FR-35
University of Washington
Seattle, WA 98195
bcn@CS.WASHINGTON.EDU

Jeffrey I. Schiller
Project Athena
Massachusetts Institute of Technology
Cambridge, MA 02139
jis@ATHENA.MIT.EDU

TÓM TẮT

Trong một môi trường tính toán mạng mở, không thể tin cậy một workstation trong việc xác định chính xác người dùng của nó với các dịch vụ mạng. Kerberos cung cấp một phương pháp thay thế, trong đó một dịch vụ xác thực bên thứ ba đáng tin cậy được sử dụng để xác minh danh tính của người dùng. Bài báo này trình bày tổng quan về mô hình xác thực Kerberos được triển khai cho Project Athena của MIT. Bài báo mô tả các giao thức được máy khách, server và Kerberos sử dụng để thực hiện xác thực. Bài báo cũng mô tả việc quản lý và sao chép cơ sở dữ liệu cần thiết. Các cách nhìn về Kerberos từ góc độ người dùng, lập trình viên và quản trị viên được mô tả. Cuối cùng, vai trò của Kerberos trong bức tranh tổng thể của Athena được trình bày, cùng với danh sách các ứng dụng hiện đang sử dụng Kerberos để xác thực người dùng. Chúng tôi mô tả việc bổ sung xác thực Kerberos vào Sun Network File System như một nghiên cứu trường hợp về việc tích hợp Kerberos với một ứng dụng hiện có.
