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
content_sha256: 51848c614d260aae87297f77e41049928bb285c12fcb2f9899f7836cf5cee027
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The most important measure of a search engine is the quality of its search results. While a complete user evaluation is beyond the scope of this paper, our own experience with Google has shown it to produce better results than the major commercial search engines for most searches. As an example which illustrates the use of PageRank, anchor text, and proximity, Fig. 2 shows Google’s results for a search on “bill clinton”. These results demonstrates some of Google’s features. The results are clustered by server. This helps considerably when sifting through result sets. A number of results are from the whitehouse.gov domain which is what one may reasonably expect from such a search. Currently, most major commercial search engines do not return any results from whitehouse.gov, much less the right ones. Notice that there is no title for the first result. Instead, Google relied on anchor text to determine this was a good answer to the query. Similarly, the fifth result is an email address which, of course, is not crawlable. It is also a result of anchor text.

All of the results are reasonably high quality pages and, at last check, none were broken links.

Query: bill clinton
http://www.whitehouse.gov/
100.00% (no date) (0K)
http://www.whitehouse.gov/
    Office of the President
        99.67% (Dec 23 1996) (2K) http://www.whitehouse.gov/WH/EOP/OP/html/OP_Home.html
    Welcome To The White House
        99.98% (Nov 09 1997) (5K)
    http://www.whitehouse.gov/WH/Welcome.html
    Send Electronic Mail to the President
        99.86% (Jul 14 1997) (5K) http://www.whitehouse.gov/WH/Mail/html/Mail_President.html mailto:president@whitehouse.gov
99.98%
    mailto:President@whitehouse.gov
        99.27%
The "Unofficial" Bill Clinton
94.06% (Nov 11 1997) (14K)
http://zpub.com/un/un-bc.html
    Bill Clinton Meets The Shrinks
        86.27% (Jun 29 1997) (63K)
    http://zpub.com/un/un-bc9.html
President Bill Clinton - The Dark Side
97.27% (Nov 10 1997) (15K)
http://www.realchange.org/clinton.htm
\$3 Bill Clinton
94.73% (no date) (4K)
http://www.gateway.net/~tjohnson/clinton1.html

Fig. 2. Sample results from Google. {#brin-1998-pagerank-fig-2 .figure tag=053E}

This is largely because they all have high PageRank. The PageRanks are the percentages in red along with bar graphs. Finally, there are no results about a Bill other than Clinton or about a Clinton other than Bill. This is because we place heavy importance on the proximity of word occurrences. Of course a true test of the quality of a search engine would involve an extensive user study or results analysis which we do not have room for here. Instead, we invite the reader to try Google for themselves at http://google.stanford.edu.

Aside from search quality, Google is designed to scale cost effectively to the size of the Web as it grows. One aspect of this is to use storage efficiently. Table 1 has a breakdown of some statistics and storage requirements of Google.

It is important for a search engine to crawl and index efficiently. This way information can be kept up to date and major changes to the system can be tested relatively quickly. In total it took roughly 9 days to download the 26 million pages (including errors). However, once the system was running smoothly.

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
