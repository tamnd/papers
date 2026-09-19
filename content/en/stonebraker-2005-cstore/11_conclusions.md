---
paper: stonebraker-2005-cstore
title: 'C-Store: A Column-oriented DBMS'
authors:
  - Mike Stonebraker
  - Daniel J. Abadi
  - Adam Batkin
  - Xuedong Chen
  - Mitch Cherniack
  - Miguel Ferreira
  - Edmond Lau
  - Amerson Lin
  - Sam Madden
  - Elizabeth O'Neil
  - Pat O'Neil
  - Alex Rasin
  - Nga Tran
  - Stan Zdonik
year: 2005
venue: VLDB
field: databases
section: "11"
section_title: Conclusions
tag: 076A
kind: section
lang: en
source: https://www.vldb.org/archives/website/2005/program/paper/thu/p553-stonebraker.pdf
pdf_sha256: c619eacc696c847e0d7697edb9193a2c35f242b12ac2835f486970a07129eecb
pdf_pages: "12"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 3331845d2c9a89b9f2b92a37fd400679bb45c6062523a78e01200df701e5857a
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

This paper has presented the design of C-Store, a radical departure from the architecture of current DBMSs. Unlike current commercial systems, it is aimed at the “read-mostly” DBMS market. The innovative contributions embodied in C-Store include:
• A column store representation, with an associated query execution engine.
• A hybrid architecture that allows transactions on a column store.
• A focus on economizing the storage representation on disk, by coding data values and dense-packing the data.
• A data model consisting of overlapping projections of tables, unlike the standard fare of tables, secondary indexes, and projections.
• A design optimized for a shared nothing machine environment.
• Distributed transactions without a redo log or two phase commit.
• Efficient snapshot isolation.

Acknowledgements and References

We would like to thank David DeWitt for his helpful feedback and ideas.

This work was supported by the National Science Foundation under NSF Grant numbers IIS-0086057 and IIS-0325525.

[ADDA04] http://www.addamark.com/products/sls.htm
[BERE95] Hal Berenson et al. A Critique of ANSI SQL Isolation Levels. In Proceedings of SIGMOD, 1995.
[BONC04] Peter Boncz et. al.. MonetDB/X100: Hyper-pipelining Query Execution. In Proceedings CIDR 2004.
[CERI91] S. Ceri and J. Widom. Deriving Production Rules for Incremental View Maintenance. In VLDB, 1991.
[COPE88] George Copeland et. al. Data Placement in Bubba. In Proceedings SIGMOD 1988.
[DEWI90] David Dewitt et. al. The GAMMA Database machine Project. IEEE Transactions on Knowledge and Data Engineering, 2(1), March, 1990.
[DEWI92] David Dewitt and Jim Gray. Parallel Database Systems: The Future of High Performance Database Processing. Communications of the ACM, 1992.
[FREN95] Clark D. French. One Size Fits All Database Architectures Do Not Work for DSS. In Proceedings of SIGMOD, 1995.
[GRAE91] Goetz Graefe, Leonard D. Shapiro. Data Compression and Database Performance. In Proceedings of the Symposium on Applied Computing, 1991.
[GRAE93] G. Graefe. Query Evaluation Techniques for Large Databases. Computing Surveys, 25(2), 1993.
[GRAY92] Jim Gray and Andreas Reuter. Transaction Processing Concepts and Techniques, Morgan Kaufman, 1992.
[GRAY97] Gray et al. DataCube: A Relational Aggregation Operator Generalizing Group-By, Cross-Tab, and Sub-Totals. Data Mining and Knowledge Discovery, 1(1), 1997.
[HONG92] Wei Hong and Michael Stonebraker. Exploiting Inter-operator Parallelism in XPRS. In SIGMOD, 1992.
[KDB04] http://www.kx.com/products/database.php
[KOTI99] Yannis Kotidis, Nick Roussopoulos. DynaMat: A Dynamic View Management System for Data Warehouses. In Proceedings of SIGMOD, 1999.
[MOHA92] C. Mohan et. al: ARIES: A Transaction Recovery Method Supporting Fine-granularity Locking and Partial Rollbacks Using Write-ahead Logging. TODS, March 1992.
[ONEI96] Patrick O'Neil, Edward Cheng, Dieter Gawlick, and Elizabeth O'Neil, The Log-Structured Merge-Tree. Acta Informatica 33, June 1996.
[ONEI97] P. O’Neil and D. Quass. Improved Query Performance with Variant Indexes, In Proceedings of SIGMOD, 1997.
[ORAC04] Oracle Corporation. Oracle 9i Database for Data Warehousing and Business Intelligence. White Paper. http://www.oracle.com/solutions/business_intelligence/Oracle9idw_bwp.
[PAPA04] Stratos Papadomanolakis and Anastassia Ailamaki. AutoPart: Automating Schema Design for Large Scientific Databases Using Data Partitioning. In SSDBM 2004.
[RAMA02] Ravishankar Ramamurthy, David Dewitt. Qi Su: A Case for Fractured Mirrors. In Proceedings of VLDB, 2002.
[ROTH93] Mark A. Roth, Scott J. Van Horn: Database Compression. SIGMOD Record 22(3). 1993.
[SELI79] Patricia Selinger, Morton Astrahan, Donald Chamberlain, Raymond Lorie, Thomas Price. Access Path Selection in a Relational Database. In Proceedings of SIGMOD, 1979. http://www.sleepycat.com/docs/
[STAU96] Martin Staudt, Matthias Jarke. Incremental Maintenance of Externally Materialized Views. In VLDB, 1996.
[STON86] Michael Stonebraker. The Case for Shared Nothing. In Database Engineering, 9(1), 1986.
[SYBA04] http://www.sybase.com/products/databaseservers/sybaseiq
[TAND89] Tandem Database Group: NonStop SQL, A Distributed High Performance, High Availability Implementation of SQL. In Proceedings of HPTPS, 1989. http://www.redbooks.ibm.com/redbooks.nsf/0/8280b48d5e3997bf85256cbd007e4a96?OpenDocument
[VSAM04] Till Westmann, Donald Kossmann, Sven Helmer, Guido Moerkotte. The Implementation and Performance of Compressed Databases. SIGMOD Record 29(3), 2000.
[WEST00] Paul Westerman. Data Warehousing: Using the Wal-Mart Model. Morgan-Kaufmann Publishers , 2000.
[WITT87] I. Witten, R. Neal, and J. Cleary. Arithmetic coding for data compression. Comm. of the ACM, 30(6), June 1987.
[ZHAO97] Y. Zhao, P. Deshpande, and J. Naughton. An Array-Based Algorithm for Simultaneous Multidimensional Aggregates. In Proceedings of SIGMOD, 1997.
