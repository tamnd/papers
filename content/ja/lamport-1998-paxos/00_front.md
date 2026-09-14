---
paper: lamport-1998-paxos
title: The Part-Time Parliament
authors:
  - Leslie Lamport
year: 1998
venue: ACM TOCS
field: systems
section_title: Front Matter
tag: "0002"
kind: front
lang: ja
source: https://lamport.azurewebsites.net/pubs/lamport-paxos.pdf
pdf_sha256: cd9544e9615bcd417a2c10063671cecca0b28ad4bc5db3f64467a83ecc7028d3
pdf_pages: 1-3
extraction: native
extraction_model: pdftotext version 26.09.0
content_sha256: 739bac5c8a1e929fa2c797310f8004c9f563cf2c78915f150fc29a6dec5ecc4d
translated_from: content/en/lamport-1998-paxos/00_front.md
source_content_sha256: 6fac3ffae0952fb7c9d43c72bac006ed766ea295dfe0b80314b76a08bf5a7a76
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: 9c1d74873f0850941dca2606ce296d509b8f605b085ea9e17a26ed91e2333e11
prompt_sha256: 28abc9ae7c2a46d63213afc528700760d76ff5866e775238c90c95b3052a886f
---

The Part-Time Parliament

Leslie Lamport

この論文は ACM Transactions on Computer Systems 16, 2 (May 1998), 133-169 に掲載された。軽微な修正は 29 August 2000 に行われた。

The Part-Time Parliament

LESLIE LAMPORT Digital Equipment Corporation

パクソス島での最近の考古学的発見により、非常勤議員たちがあちこちを移動する傾向にもかかわらず、議会が機能していたことが明らかになった。議員たちは、議場から頻繁に離脱し、また使者たちが忘れっぽかったにもかかわらず、議会記録の一貫したコピーを維持していた。パクソス議会のプロトコルは、分散システムの設計における状態機械アプローチを実装するための新しい方法を提供する。カテゴリおよび主題記述子: C2.4 [Computer-Communications Networks]: 分散システム—ネットワークオペレーティングシステム; D4.5 [Operating Systems]: 信頼性—耐障害性; J.1 [Administrative Data Processing]: 政府 一般用語: 設計、信頼性 追加キーワードおよびフレーズ: 状態機械、三相コミット、投票

この投稿論文は最近、TOCS編集部の書類棚の後ろから発見された。その古さにもかかわらず、編集長は出版する価値があると判断した。著者は現在ギリシャ諸島で現地調査を行っており連絡が取れないため、私は出版の準備を依頼された。

著者は、コンピューター科学にはわずかな関心しか持たない考古学者であるように見える。これは残念なことである。彼が記述する謎めいた古代パクソス文明は、ほとんどのコンピューター科学者にとって興味の対象ではないものの、その立法制度は、非同期環境で分散コンピューターシステムを実装する方法の優れたモデルである。
