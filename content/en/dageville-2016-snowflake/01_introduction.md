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
section: "1"
section_title: INTRODUCTION
tag: "0489"
kind: section
lang: en
source: https://info.snowflake.net/rs/252-RFO-227/images/Snowflake_SIGMOD.pdf
pdf_sha256: b635081104c3647561a476ab5947f5782b2a5c4be5af43b48cea90dba1b9e332
pdf_pages: 1-2
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 99be645b672c3edec1931617676ae3a8e92e6e6ba028c534b9890b61010567e6
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The advent of the cloud marks a move away from software delivery and execution on local servers, and toward shared data centers and software-as-a-service solutions hosted by platform providers such as Amazon, Google, or Microsoft. The shared infrastructure of the cloud promises increased economies of scale, extreme scalability and availability, and a pay-as-you-go cost model that adapts to unpredictable usage demands. But these advantages can only be captured if the software itself is able to scale elastically over the pool of commodity resources that is the cloud. Traditional data warehousing solutions pre-date the cloud. They were designed to run on small, static clusters of well-behaved machines, making them a poor architectural fit.

But not only the platform has changed. Data has changed as well. It used to be the case that most of the data in a data warehouse came from sources within the organization: transactional systems, enterprise resource planning (ERP) applications, customer relationship management (CRM) applications, and the like. The structure, volume, and rate of the data were all fairly predictable and well known. But with the cloud, a significant and rapidly growing share of data comes from less controllable or external sources: application logs, web applications, mobile devices, social media, sensor data (Internet of Things). In addition to the growing volume, this data frequently arrives in schema-less, semi-structured formats [3]. Traditional data warehousing solutions are struggling with this new data. These solutions depend on deep ETL pipelines and physical tuning that fundamentally assume predictable, slow-moving, and easily categorized data from largely internal sources.

In response to these shortcomings, parts of the data warehousing community have turned to “Big Data” platforms such as Hadoop or Spark [8, 11]. While these are indispensable tools for data center-scale processing tasks, and the open source community continues to make big improvements such as the Stinger Initiative [48], they still lack much of the efficiency and feature set of established data warehousing technology. But most importantly, they require significant engineering effort to roll out and use [16].

We believe that there is a large class of use cases and workloads which can benefit from the economics, elasticity, and service aspects of the cloud, but which are not well served by either traditional data warehousing technology or by Big Data platforms. So we decided to build a completely new data warehousing system specifically for the cloud. The system is called the Snowflake Elastic Data Warehouse, or “Snowflake”. In contrast to many other systems in the cloud data management space, Snowflake is not based on Hadoop, PostgreSQL or the like. The processing engine and most of the other parts have been developed from scratch.

The key features of Snowflake are as follows.

Pure Software-as-a-Service (SaaS) Experience Users need not buy machines, hire database administrators, or install software. Users either already have their data in the cloud, or they upload (or mail [14]) it. They can then immediately manipulate and query their data using Snowflake’s graphical interface or standardized interfaces such as ODBC. In contrast to other Database-as-a-Service (DBaaS) offerings, Snowflake’s service aspect extends to the whole user experience. There are no tuning knobs, no physical design, no storage grooming tasks on the part of users.

Relational Snowflake has comprehensive support for ANSI SQL and ACID transactions. Most users are able to migrate existing workloads with little to no changes.

Semi-Structured Snowflake offers built-in functions and SQL extensions for traversing, flattening, and nesting of semi-structured data, with support for popular formats such as JSON and Avro. Automatic schema discovery and columnar storage make operations on schema-less, semi-structured data nearly as fast as over plain relational data, without any user effort.

Elastic Storage and compute resources can be scaled independently and seamlessly, without impact on data availability or performance of concurrent queries.

Highly Available Snowflake tolerates node, cluster, and even full data center failures. There is no downtime during software or hardware upgrades.

Durable Snowflake is designed for extreme durability with extra safeguards against accidental data loss: cloning, undrop, and cross-region backups.

Cost-efficient Snowflake is highly compute-efficient and all table data is compressed. Users pay only for what storage and compute resources they actually use.

Secure All data including temporary files and network traffic is encrypted end-to-end. No user data is ever exposed to the cloud platform. Additionally, role-based access control gives users the ability to exercise fine-grained access control on the SQL level.

Snowflake currently runs on the Amazon cloud (Amazon Web Services, AWS), but we may port it to other cloud platforms in the future. At the time of writing, Snowflake executes millions of queries per day over multiple petabytes of data, serving a rapidly growing number of small and large organizations from various domains.

Outline.
The paper is structured as follows. Section 2 explains the key design choice behind Snowflake: separation of storage and compute. Section 3 presents the resulting multi-cluster, shared-data architecture. Section 4 highlights differentiating features: continuous availability, semi-structured and schema-less data, time travel and cloning, and end-to-end security. Section 5 discusses related work. Section 6 concludes the paper with lessons learned and an outlook on ongoing work.
