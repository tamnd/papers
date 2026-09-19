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
section: "6"
section_title: LESSONS LEARNED AND OUTLOOK
tag: 07B2
kind: section
lang: en
source: https://info.snowflake.net/rs/252-RFO-227/images/Snowflake_SIGMOD.pdf
pdf_sha256: b635081104c3647561a476ab5947f5782b2a5c4be5af43b48cea90dba1b9e332
pdf_pages: 11-12
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 0d7f657abd6e706252e0067f2c81437528bc8397b4a7da0e6f1778f2f6c035f2
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

When Snowflake was founded in 2012, the database world was fully focused on SQL on Hadoop, with over a dozen systems appearing within a short time span. At that time, the decision to work in a completely different direction, to build a “classic” data warehouse system for the cloud, seemed a contrarian and risky move. After 3 years of development we are confident that it was the right one. Hadoop has not replaced RDBMSs; it has complemented them. People still want a relational database, but one that is more efficient, flexible, and better suited for the cloud.

Snowflake has met our hopes of what a system built for the cloud can provide to both its users and its authors. The elasticity of the multi-cluster, shared data architecture has changed how users approach their data processing tasks. The SaaS model not only has made it easy for users to try out and adopt the system, but has also dramatically helped our development and testing. With a single production version and online upgrades, we are able to release new features, provide improvements, and fix problems much faster than we would possibly be able to do under a traditional development model.

While we had hoped that the semi-structured extensions would prove useful, we were surprised by the speed of adoption. We discovered a very popular model, where organizations would use Hadoop for two things: for storing JSON, and for converting it to a format that can be loaded into an RDBMS. By providing a system that can efficiently store and process semi-structured data as-is—with a powerful SQL interface on top—we found Snowflake replacing not only traditional database systems, but also Hadoop clusters.

It was not a painless journey of course. While our team has over 100 years of database-development expertise combined, we did make avoidable mistakes along the way, including overly simplistic early implementations of some relational operators, not incorporating all datatypes early on in the engine, not early-enough focus on resource management, postponing work on comprehensive date and time functionality etc. Also, our continuous focus on avoiding tuning knobs raised a series of engineering challenges, ultimately bringing about many exciting technical solutions. As a result, today, Snowflake has only one tuning parameter: how much performance the user wants (and is willing to pay for).

While Snowflake’s performance is already very competitive, especially considering the no-tuning aspect, we know of many optimizations that we have not had the time for yet. Somewhat unexpected though, core performance turned out to be almost never an issue for our users. The reason is that elastic compute via virtual warehouses can offer the performance boost occasionally needed. That made us focus our development efforts on other aspects of the system.

The biggest technical challenges we face are related to the SaaS and multi-tenancy aspects of the system. Building a metadata layer that can support hundreds of users concurrently was a very challenging and complex task. Handling various types of node failures, network failures, and supporting services is a never-ending fight. Security has been and will continue to be a big topic: protecting the system and the users’ data from external attacks, the users themselves, and our internal users as well. Maintaining a live system of hundreds of nodes running millions of queries per day, while bringing a lot of satisfaction, requires a highly integrated approach to development, operations, and support.

Snowflake users continue to throw increasingly bigger and more complex problems at the system, influencing its evolution. We are currently working on improving the data access performance by providing additional metadata structures and data re-organization tasks—with a focus on minimal to no user interaction. We continue to improve and extend core query processing functionality, both for standard SQL and semi-relational extensions. We plan to further improve the skew handling and load balancing strategies, whose importance increases along with the scale of our users’ workloads. We work on solutions simplifying workload management to the users, making the system even more elastic. And we work on integration with external systems, including issues such as high-frequency data loading.

The biggest future challenge for Snowflake is the transition to a full self-service model, where users can sign up and interact with the system without our involvement at any phase. It will bring a lot of security, performance, and support challenges. We are looking forward to them.
