---
paper: dageville-2016-snowflake
title: The Snowflake Elastic Data Warehouse
authors:
  - Benoit Dageville
  - Thierry Cruanes
  - Marcin Zukowski
  - Vadim Antonov
  - Artin Avanes
  - Jon Bock
  - Jonathan Claybaugh
  - Daniel Engovatov
  - Martin Hentschel
  - Jiansheng Huang
  - Allison W. Lee
  - Ashish Motivala
  - Abdul Q. Munir
  - Steven Pelley
  - Peter Povinec
  - Greg Rahn
  - Spyridon Triantafyllis
  - Philipp Unterbrunner
year: 2016
venue: SIGMOD
field: databases
section: "7"
section_title: ACKNOWLEDGMENTS
tag: 07B3
kind: section
lang: en
source: https://info.snowflake.net/rs/252-RFO-227/images/Snowflake_SIGMOD.pdf
pdf_sha256: b635081104c3647561a476ab5947f5782b2a5c4be5af43b48cea90dba1b9e332
pdf_pages: "12"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: a622747bc2ded3d66ffd7bf57c43ce3f65c3c12a588765a77feb7f4ad2790f73
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Snowflake is the work of far too many people to list here. We would like to thank the entire Snowflake engineering team for their contributions to the product, and for all the hard work, effort, and pride they put into it. We also would like to thank all the other “Snowflakes” for their amazing work in bringing this product to the users and building a great company together. We are continuously impressed and humbled to work with such an excellent team.

8. REFERENCES
[1] D. J. Abadi, S. R. Madden, and N. Hachem. Column-stores vs. row-stores: How different are they really? In Proc. SIGMOD, 2008.
[2] A. Ailamaki, D. J. DeWitt, M. D. Hill, and M. Skounakis. Weaving relations for cache performance. In Proc. VLDB, 2001.
[3] S. Alsubaiee et al. AsterixDB: A scalable, open source DBMS. PVLDB, 7(14):1905–1916, 2014.
[4] Amazon Elastic Compute Cloud (EC2).
aws.amazon.com/ec2/instance-types
[5] Amazon Simple Storage Service (S3). aws.amazon.com/s3
[6] Apache Cassandra. cassandra.apache.org
[7] Apache Drill. drill.apache.org
[8] Apache Hadoop. hadoop.apache.org
[9] Apache Hive. hive.apache.org
[10] Apache Parquet. parquet.apache.org
[11] Apache Spark. spark.apache.org
[12] AWS CloudHSM. aws.amazon.com/cloudhsm
[13] E. Barker. NIST SP 800-57 – Recommendation for Key Management – Part 1: General (Revision 4), chapter 7. 2016.
[14] J. Barr. AWS Import/Export Snowball – Transfer 1 petabyte per week using Amazon-owned storage appliances.
aws.amazon.com/blogs/aws/aws-importexport-snowball-transfer-1-petabyte-per-week-using-amazon-owned-storage-appliances/ 2015.
[15] P. Boncz, M. Zukowski, and N. Nes. MonetDB/X100: Hyper-pipelining query execution. In Proc. CIDR, 2005.
[16] V. R. Borkar, M. J. Carey, and C. Li. Big data platforms: What’s next? ACM Crossroads, 19(1):44–49, 2012.
[17] M. J. Cahill, U. Röhm, and A. D. Fekete. Serializable isolation for snapshot databases. In Proc. SIGMOD, 2008.
[18] B. Calder et al. Windows Azure Storage: A highly available storage service with strong consistency. In Proc. SOSP, 2011.
[19] Cassandra Query Language (CQL).
cassandra.apache.org/doc/cql3/CQL.html
[20] Cloud Storage – Google Cloud Platform.
cloud.google.com/storage
[21] Cloudera Impala. impala.io
[22] Couchbase N1QL. couchbase.com/n1ql
[23] Couchbase Server. couchbase.com
[24] D. J. DeWitt, A. Halverson, R. Nehme, S. Shankar, J. Aguilar-Saborit, A. Avanes, M. Flasza, and J. Gramling. Split query processing in Polybase. In Proc. SIGMOD, 2013.
[25] D. J. DeWitt, S. Madden, and M. Stonebraker. How to build a high-performance data warehouse.
db.csail.mit.edu/madden/high_perf.pdf 2006.
[26] D. Ferraiolo, D. R. Kuhn, and R. Chandramouli. Role-based access control. Artech House Publishers, 2003.
[27] G. Graefe. Volcano: An extensible and parallel query evaluation system. IEEE TKDE, 6(1), 1994.
[28] G. Graefe. The cascades framework for query optimization. Data Engineering Bulletin, 18, 1995.
[29] G. Graefe. Fast loads and fast queries. In Data Warehousing and Knowledge Discovery, volume 5691 of LNCS. Springer, 2009.
[30] A. Gupta et al. Amazon Redshift and the case for simpler data warehouses. In Proc. SIGMOD, 2015.
[31] D. Karger, E. Lehman, T. Leighton, R. Panigrahy, M. Levine, and D. Lewin. Consistent hashing and random trees: Distributed caching protocols for relieving hot spots on the world wide web. In Proc. STOC, 1997.
[32] J. Krueger, M. Grund, C. Tinnefeld, H. Plattner, A. Zeier, and F. Faerber. Optimizing write performance for read optimized databases. In Proc. DASFAA, 2010.
[33] S. Manegold, M. L. Kersten, and P. Boncz. Database architecture evolution: Mammals flourished long before dinosaurs became extinct. PVLDB, 2(2):1648–1653, 2009.
[34] S. Melnik, A. Gubarev, J. J. Long, G. Romer, S. Shivakumar, M. Tolton, and T. Vassilakis. Dremel: Interactive analysis of web-scale datasets. PVLDB, 3(1-2):330–339, 2010.
[35] Microsoft Analytics Platform System. www.microsoft.com/en-us/server-cloud/products/analytics-platform-system
[36] Microsoft Azure Blob Storage.
azure.microsoft.com/en-us/services/storage/blobs
[37] Microsoft Azure SQL DW.
azure.microsoft.com/en-us/services/sql-data-warehouse
[38] G. Moerkotte. Small materialized aggregates: A light weight index structure for data warehousing. In Proc. VLDB, 1998.
[39] MongoDB. mongodb.com
[40] J. K. Mullin. Optimal semijoins for distributed database systems. IEEE TSE, 16(5):558–560, 1990.
[41] T. Neumann. Efficiently compiling efficient query plans for modern hardware. PVLDB, 4(9):539–550, 2011.
[42] A. Pavlo, E. Paulson, A. Rasin, D. J. Abadi, D. J. DeWitt, S. Madden, and M. Stonebraker. A comparison of approaches to large-scale data analysis. In Proc. SIGMOD, 2009.
[43] Presto. prestodb.io
[44] K. Sato. An inside look at Google BigQuery.
cloud.google.com/files/BigQueryTechnicalWP.pdf 2012.
[45] J. Schad, J. Dittrich, and J.-A. Quiané-Ruiz. Runtime measurements in the cloud: Observing, analyzing, and reducing variance. PVLDB, 3(1):460–471, 2010.
[46] K. Shvachko, H. Kuang, S. Radia, and R. Chansler. The Hadoop distributed file system. In Proc. MSST, 2010.
[47] SQL DW Concurrency.
azure.microsoft.com/en-us/documentation/articles/sql-data-warehouse-develop-concurrency
[48] Stinger.next: Enterprise SQL at Hadoop scale.
hortonworks.com/innovation/stinger
[49] L. Sun, M. J. Franklin, S. Krishnan, and R. S. Xin. Fine-grained partitioning for aggressive data skipping. In Proc. SIGMOD, 2014.
