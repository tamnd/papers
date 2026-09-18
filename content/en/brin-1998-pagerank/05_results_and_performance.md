---
paper: brin-1998-pagerank
title: The Anatomy of a Large-Scale Hypertextual Web Search Engine
authors:
  - Sergey Brin
  - Lawrence Page
year: 1998
venue: Computer Networks and ISDN Systems
field: algorithms
section: "5"
section_title: Results and performance
tag: "0364"
kind: section
lang: en
source: https://doi.org/10.1016/s0169-7552(98)00110-x
pdf_sha256: 3a155ade395c7789876a0bc08a1842f909486438c1b1739ae531fa5c797d93f0
pdf_pages: 7-9
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: c98e41d720a38bda6d77acedfd7da58b6b4a4604162b955997d6f70c426023d5
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The most important measure of a search engine is the quality of its search results. While a complete user evaluation is beyond the scope of this paper, our own experience with Google has shown it to produce better results than the major commercial search engines for most searches. As an example which illustrates the use of PageRank, anchor text, and proximity, Fig. 2 shows Google’s results for a search on “bill clinton”. These results demonstrates some of Google’s features. The results are clustered by server. This helps considerably when sifting through result sets. A number of results are from the whitehouse.gov domain which is what one may reasonably expect from such a search. Currently, most major commercial search engines do not return any results from whitehouse.gov, much less the right ones. Notice that there is no title for the first result. Instead, Google relied on anchor text to determine this was a good answer to the query. Similarly, the fifth result is an email address which, of course, is not crawlable. It is also a result of anchor text.

All of the results are reasonably high quality pages and, at last check, none were broken links.

Table 1
Statistics

| Storage statistics |  |
| --- | --- |
| Total size of fetched pages | 147.8 GB |
| Compressed repository | 53.5 GB |
| Short inverted index | 4.1 GB |
| Full inverted index | 37.2 GB |
| Lexicon | 293 MB |
| Temporary anchor data (not in total) | 6.6 GB |
| Document index incl. variable width data | 9.7 GB |
| Links database | 3.9 GB |
| Total without repository | 55.2 GB |
| Total with repository | 108.7 GB |

| Web page statistics |  |
| --- | --- |
| Number of Web pages fetched | 24 million |
| Number of URLs seen | 76.5 million |
| Number of E-mail addresses | 1.7 million |
| Number of 404's | 1.6 million |

it ran much faster, downloading the last 11 million pages in just 63 hours, averaging just over 4 million pages per day or 48.5 pages per second. The indexer runs at roughly 54 pages per second. The sorters can be run completely in parallel; using four machines, the whole process of sorting takes about 24 hours.

Improving the performance of search was not the major focus of our research up to this point. The current version of Google answers most queries in between 1 and 10 seconds. This time is mostly dominated by disk IO over NFS (since our disks are spread over a number of machines). Furthermore, Google does not have many of the common optimizations used to speed up information retrieval systems, such as query caching, subindices on common terms, and other common optimizations. We intend to speed up Google considerably in the future. Table 2 has some sample query times from the current version of Google.
