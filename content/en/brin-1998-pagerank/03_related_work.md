---
paper: brin-1998-pagerank
title: The Anatomy of a Large-Scale Hypertextual Web Search Engine
authors:
  - Sergey Brin
  - Lawrence Page
year: 1998
venue: Computer Networks and ISDN Systems
field: algorithms
section: "3"
section_title: Related work
tag: 035E
kind: section
lang: en
source: https://doi.org/10.1016/s0169-7552(98)00110-x
pdf_sha256: 3a155ade395c7789876a0bc08a1842f909486438c1b1739ae531fa5c797d93f0
pdf_pages: 4-5
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: c192357023aba0c74901c1a396b7ec4a43932a7623c0c6a3f6f6de24e178a0bc
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Search research on the Web has a short and concise history. The World Wide Web Worm (WWW) [6] was one of the first Web search engines. It was subsequently followed by several academic search engines, many of which are now public companies. Compared to the growth of the Web and the importance of search engines there are precious few documents about recent search engines [8]. According to Michael Mauldin (chief scientist, Lycos Inc.) [5], “the various services (including Lycos) closely guard the details of these databases”. However, there has been a fair amount of work on specific features of search engines. Especially well represented is work which can get results by post-processing the results of existing commercial search engines, or produce small scale “individualized” search engines. Finally, there has been a lot of research on information retrieval systems, especially on well controlled collections [11].

However, work on information retrieval has mostly been on fairly small, well controlled collections such as the Text Retrieval Conference [10]. Things that work well on TREC often do not produce good results on the Web. For example, the standard vector space model tries to return the document that most closely approximates the query, given that both query and document are vectors defined by their word occurrence. On the Web, this strategy often returns very short documents that are the query plus a few words. For example, we have seen a major search engine return a page containing only “Bill Clinton Sucks” and picture from a “Bill Clinton” query. Given examples like these, we believe that the standard information retrieval work needs to be extended to deal effectively with the Web.

The Web is a vast collection of completely uncontrolled heterogeneous documents. Documents vary significantly in language, format, and style. There can be many orders of magnitude of difference in two documents’ size, quality, popularity, and trustworthiness. All of these are significant challenges to effective searching on the Web. They are somewhat mediated by the availability of auxiliary data such as hyperlinks and formatting and Google tries to take advantage of both of these.
