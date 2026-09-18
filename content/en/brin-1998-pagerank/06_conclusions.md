---
paper: brin-1998-pagerank
title: The Anatomy of a Large-Scale Hypertextual Web Search Engine
authors:
  - Sergey Brin
  - Lawrence Page
year: 1998
venue: Computer Networks and ISDN Systems
field: algorithms
section: "6"
section_title: Conclusions
tag: "0365"
kind: section
lang: en
source: https://doi.org/10.1016/s0169-7552(98)00110-x
pdf_sha256: 3a155ade395c7789876a0bc08a1842f909486438c1b1739ae531fa5c797d93f0
pdf_pages: 9-10
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 7f1f96579b96d88d553425811df8b411cd5305b38b3c2c686b734ffecf446aff
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Google is designed to be a scalable search engine. The primary goal is to provide high quality search results over a rapidly growing World Wide Web. Google employs a number of techniques to improve search quality including page rank, anchor text, and proximity information. Furthermore, Google is a complete architecture for gathering Web pages, indexing them, and performing search queries over them.

### 6.1. Future work {#brin-1998-pagerank-s6-1 .section tag=0366}

A large-scale Web search engine is a complex system and much remains to be done. Our immediate goals are to improve search efficiency and to scale to approximately 100 million Web pages. Some simple improvements to efficiency include query caching, smart disk allocation, and subindices. Another area which requires much research is updates. We must have smart algorithms to decide what old Web pages should be recrawled and what new ones should be crawled. Work toward this goal has been done in [2]. One promising area of research is using proxy caches to build search databases, since they are demand driven. We are planning to add simple features supported by commercial search engines like boolean operators, negation, and stemming. However, other features are just starting to be explored such as relevance feedback and clustering (Google currently supports a simple hostname based clustering). We also plan to support user context (like the

Table 2
Search times

| Query | Initial query |  | Same query repeated (IO mostly cached) |  |
| --- | --- | --- | --- | --- |
|  | CPU time (s) | Total time (s) | CPU time (s) | Total time (s) |
| al gore | 0.09 | 2.13 | 0.06 | 0.06 |
| vice president | 1.77 | 3.84 | 1.66 | 1.80 |
| hard disks | 0.25 | 4.86 | 0.20 | 0.24 |
| search engines | 1.31 | 9.63 | 1.16 | 1.16 |

user’s location), and result summarization. We are also working to extend the use of link structure and link text. Simple experiments indicate PageRank can be personalized by increasing the weight of a user’s home page or bookmarks. As for link text, we are experimenting with using text surrounding links in addition to the link text itself. A Web search engine is a very rich environment for research ideas. We have far too many to list here so we do not expect this Future Work section to become much shorter in the near future.

### 6.2. High quality search {#brin-1998-pagerank-s6-2 .section tag=0367}

The biggest problem facing users of Web search engines today is the quality of the results they get back. While the results are often amusing and expand users’ horizons, they are often frustrating and consume precious time. For example, the top result for a search for “Bill Clinton” on one of the most popular commercial search engines was the Bill Clinton Joke of the Day: April 14, 1997⁷. Google is designed to provide higher quality search so as the Web continues to grow rapidly, information can be found easily. In order to accomplish this Google makes heavy use of hypertextual information consisting of link structure and link (anchor) text. Google also uses proximity and font information. While evaluation of a search engine is difficult, we have subjectively found that Google returns higher quality search results than current commercial search engines. The analysis of link structure via PageRank allows Google to evaluate the quality of Web pages. The use of link text as a description of what the link points to helps the search engine return relevant (and to some degree high quality) results. Finally, the use of proximity information helps increase relevance a great deal for many queries.

### 6.3. Scalable architecture {#brin-1998-pagerank-s6-3 .section tag=0368}

Aside from the quality of search, Google is designed to scale. It must be efficient in both space and time, and constant factors are very important when dealing with the entire Web. In implementing Google, we have seen bottlenecks in CPU, memory access, memory capacity, disk seeks, disk throughput, disk capacity, and network IO. Google has evolved to overcome a number of these bottlenecks during various operations. Google’s major data structures make efficient use of available storage space. Furthermore, the crawling, indexing, and sorting operations are efficient enough to be able to build an index of a substantial portion of the Web — 24 million pages, in less than one week. We expect to be able to build an index of 100 million pages in less than a month.

### 6.4. A research tool {#brin-1998-pagerank-s6-4 .section tag=0369}

In addition to being a high quality search engine, Google is a research tool. The data Google has collected has already resulted in many other papers submitted to conferences and many more on the way. Recent research such as [1] has shown a number of limitations to queries about the Web that may be answered without having the Web available locally. This means that Google (or a similar system) is not only a valuable research tool but a necessary one for a wide range of applications. We hope Google will be a resource for searchers and researchers all around the world and will spark the next generation of search engine technology.
