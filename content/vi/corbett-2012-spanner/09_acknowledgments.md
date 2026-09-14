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
section_title: Lời cảm ơn
kind: section
lang: vi
source: http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.258.9924
pdf_sha256: 61875779e75f603d21aefba6d9bd9816d4dd0c18cf41089f43707249e24bbf88
pdf_pages: "13"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 4986f3db30f5530c0087e22065913c5c413d904b5afa8716bcd3ff5323b886e1
translated_from: content/en/corbett-2012-spanner/09_acknowledgments.md
source_content_sha256: 239c6ef743466b469bdafa164f8a23d9abc1e6a1d770e9fb568db31892513bb6
translation_model: gpt-5
translation_run: 20260914T201546Z
glossary_version: 6
glossary_terms_sha256: a534ae50d60bff0e03804fd3c150e37d1876484531ab87df9c72dc4d0c455eb2
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Nhiều người đã giúp cải thiện bài báo này: người hỗ trợ của chúng tôi Jon Howell, người đã vượt xa trách nhiệm của mình; các phản biện ẩn danh; và nhiều Googler: Atul Adya, Fay Chang, Frank Dabek, Sean Dorward, Bob Gruber, David Held, Nick Kline, Alex Thomson, và Joel Wein. Ban quản lý của chúng tôi đã rất ủng hộ cả công việc của chúng tôi lẫn việc xuất bản bài báo này: Aristotle Balogh, Bill Coughran, Urs Hölzle, Doron Meyer, Cos Nicolaou, Kathy Polizzi, Sridhar Ramaswamy, và Shivakumar Venkataraman.

Chúng tôi đã xây dựng dựa trên công việc của các nhóm Bigtable và Megastore. Nhóm F1, đặc biệt là Jeff Shute, đã làm việc chặt chẽ với chúng tôi trong việc phát triển mô hình dữ liệu của chúng tôi và đã giúp rất nhiều trong việc truy tìm các lỗi về hiệu năng và tính đúng đắn. Nhóm Platforms, đặc biệt là Luiz Barroso và Bob Felderman, đã giúp biến True-Time thành hiện thực. Cuối cùng, nhiều Googler từng thuộc nhóm của chúng tôi: Ken Ashcraft, Paul Cychosz, Krzysztof Ostrowski, Amir Voskoboynik, Matthew Weaver, Theo Vassilakis, và Eric Veach; hoặc đã gia nhập nhóm của chúng tôi gần đây: Nathan Bales, Adam Beberg, Vadim Borisov, Ken Chen, Brian Cooper, Cian Cullinan, Robert-Jan Huijsman, Milind Joshi, Andrey Khorlin, Dawid Kuroczko, Laramie Leavitt, Eric Li, Mike Mammarella, Sunil Mushran, Simon Nielsen, Ovidiu Platon, Ananth Shrinivas, Vadim Susvorov, và Marcel van der Holst.
