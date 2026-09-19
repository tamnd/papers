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
section: "5"
section_title: RELATED WORK
tag: 07B1
kind: section
lang: en
source: https://info.snowflake.net/rs/252-RFO-227/images/Snowflake_SIGMOD.pdf
pdf_sha256: b635081104c3647561a476ab5947f5782b2a5c4be5af43b48cea90dba1b9e332
pdf_pages: 10-11
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: e0fd293b6ec5bae47c2d29d7b8f3ebef9bf4492dba6e5c446e2c25426aa9572b
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Cloud-based Parallel Database Systems. Amazon has a number of DBaaS products with Amazon Redshift being the data warehousing product among these. Having evolved from the parallel database system ParAccel, Redshift was arguably the first real data warehouse system offered as a service [30]. Redshift uses a classic shared-nothing architecture. Thus, while being scalable, adding or removing compute resources requires data redistribution. In contrast, Snowflake’s multi-cluster, shared data architecture allows users to instantly scale up, scale down, or even pause compute independently from storage without data movement—including the ability to integrate data across isolated compute resources. Also, following a pure service principle, Snowflake requires no physical tuning, data grooming, manual gathering of table statistics, or table vacuuming on the part of users. Although Redshift can ingest semi-structured data such as JSON as a VARCHAR, Snowflake has native support for semi-structured data, including important optimizations such as columnar storage.

Google’s Cloud Platform offers a fully managed query service known as BigQuery [44], which is the public implementation of Dremel [34]. The BigQuery service lets users run queries on terabytes of data at impressive speeds, parallelized across thousands of nodes. One of the inspirations for Snowflake was BigQuery’s support for JSON and nested data, which we find necessary for a modern analytics platform. But while BigQuery offers a SQL-like language, it has some fundamental deviations from the ANSI SQL syntax and semantics, making it tricky to use with SQL-based products. Also, BigQuery tables are append-only and require schemas. In comparison, Snowflake offers full DML (insert, update, delete, merge), ACID transactions, and does not require schema definitions for semi-structured data.

Microsoft SQL Data Warehouse (Azure SQL DW) is a recent addition to the Azure cloud platform and services based on SQL Server and its Analytics Platform System (APS) appliance [35, 37]. Similar to Snowflake, it separates storage from compute. Computational resources can be scaled through data warehouse units (DWUs). The degree of concurrency is capped though. For any data warehouse, the maximum number of concurrently executing queries is 32 [47]. Snowflake, in contrast, allows fully independent scaling of concurrent workloads via virtual warehouses. Snowflake users are also released from the burden of choosing appropriate distribution keys and other administrative tasks. And while Azure SQL DW does support queries over non-relational data via PolyBase [24], it does not have built-in support for semi-structured data comparable to Snowflake’s VARIANT type and related optimizations.

Document Stores and Big Data. Document stores such as MongoDB [39], Couchbase Server [23], and Apache Cassandra [6], have become increasingly popular among application developers in recent years, because of the scalability, simplicity, and schema flexibility they offer. However, one challenge that has resulted from the simple key-value and CRUD (create, read, update, and delete) API of these systems is the difficulty to express more complex queries. In response, we have seen the emergence of several SQL-like query languages such as N1QL [22] for Couchbase or CQL [19] for Apache Cassandra. Additionally, many “Big Data” engines now support queries over nested data, for example Apache Hive [9], Apache Spark [11], Apache Drill [7], Cloudera Impala [21], and Facebook Presto [43]. We believe that this shows a real need for complex analytics over schema-less and semi-structured data, and our semi-structured data support is inspired by many of these systems. Using schema inference, optimistic conversions, and columnar storage, Snowflake combines the flexibility of these systems with the storage efficiency and execution speed of a relational, column-oriented database.
