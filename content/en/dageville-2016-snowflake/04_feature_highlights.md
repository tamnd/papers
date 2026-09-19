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
section: "4"
section_title: FEATURE HIGHLIGHTS
tag: 079F
kind: section
lang: en
source: https://info.snowflake.net/rs/252-RFO-227/images/Snowflake_SIGMOD.pdf
pdf_sha256: b635081104c3647561a476ab5947f5782b2a5c4be5af43b48cea90dba1b9e332
pdf_pages: 6-10
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: c3bbc1d439044d5bd806d96ab44cb606ab30f5ed023f7b4a6b81249ab7e622f9
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Snowflake offers many features expected from a relational data warehouse: comprehensive SQL support, ACID transactions, standard interfaces, stability and security, customer support, and—of course—strong performance and scalability. Additionally, it introduces a number of other valuable features rarely or never-before seen in related systems. This section presents a few of these features that we consider technical differentiators.

### 4.1 Pure Software-as-a-Service Experience {#dageville-2016-snowflake-s4-1 .section tag=07A0}

Snowflake supports standard database interfaces (JDBC, ODBC, Python PEP-0249) and works with various third-party tools and services such as Tableau, Informatica, or Looker. However, it also provides the possibility to interact with the system using nothing but a web browser. A web UI may seem like a trivial thing, but it quickly proved itself to be a critical differentiator. The web UI makes it very easy to access Snowflake from any location and environment, dramatically reducing the complexity of bootstrapping and using the system. With a lot of data already in the cloud, it allowed many users to just point Snowflake at their data and query away, without downloading any software.

As may be expected, the UI allows not only SQL operations, but also gives access to the database catalog, user and system management, monitoring, usage information, and so forth. We continuously expand the UI functionality, working on aspects such as online collaboration, user feedback and support, and others.

But our focus on ease-of-use and service experience does not stop at the user interface; it extends to every aspect of the system architecture. There are no failure modes, no tuning knobs, no physical design, no storage grooming tasks. It is all about the data and the queries.

### 4.2 Continuous Availability {#dageville-2016-snowflake-s4-2 .section tag=07A1}

In the past, data warehousing solutions were well-hidden back-end systems, isolated from most of the world. In such environments, downtimes—both planned (software upgrades or administrative tasks) and unplanned (failures)—usually did not have a large impact on operations. But as data analysis became critical to more and more business tasks, continuous availability became an important requirement for any data warehouse. This trend mirrors the expectations on modern SaaS systems, most of which are always-on, customer-facing applications with no (planned) downtime.

Snowflake offers continuous availability that meets these expectations. The two main technical features in this regard are fault resilience and online upgrades.

### 4.2.1 Fault Resilience {#dageville-2016-snowflake-s4-2-1 .section tag=07A2}

Snowflake tolerates individual and correlated node failures at all levels of the architecture, shown in Figure 2. The Data Storage layer of Snowflake today is S3, which is replicated across multiple data centers called "availability zones" or AZs in Amazon terminology. Replication across AZs allows S3 to handle full AZ failures, and to guarantee 99.99% data availability and 99.999999999% durability. Matching S3’s architecture, Snowflake’s metadata store is also distributed and replicated across multiple AZs. If a node fails, other nodes can pick up the activities without much impact on end users. The remaining services of the Cloud Services layer consist of stateless nodes in multiple AZs, with a load balancer distributing user requests between them. It follows that a single node failure or even a full AZ failure causes no system-wide impact, possibly some failed queries for users currently connected to a failed node. These users will be redirected to a different node for their next query.

In contrast, Virtual Warehouses (VWs) are not distributed across AZs. This choice is for performance reasons. High network throughput is critical for distributed query execution, and network throughput is significantly higher within the same AZ. If one of the worker nodes fails during query execution, the query fails but is transparently re-executed, either with the node immediately replaced, or with a temporarily reduced number of nodes. To accelerate node replacement, Snowflake maintains a small pool of standby nodes. (These nodes are also used for fast VW provisioning.)

If an entire AZ becomes unavailable though, all queries running on a given VW of that AZ will fail, and the user needs to actively re-provision the VW in a different AZ. With full-AZ failures being truly catastrophic and exceedingly rare events, we today accept this one scenario of partial system unavailability, but hope to address it in the future.

### 4.2.2 Online Upgrade {#dageville-2016-snowflake-s4-2-2 .section tag=07A3}

Snowflake provides continuous availability not only when failures occur, but also during software upgrades. The system is designed to allow multiple versions of the various services to be deployed side-by-side, both Cloud Services components and virtual warehouses. This is made possible by the fact that all services are effectively stateless. All hard state is kept in a transactional key-value store and is accessed through a mapping layer which takes care of metadata versioning and schema evolution. Whenever we change the metadata schema, we ensure backward compatibility with the previous version.

To perform a software upgrade, Snowflake first deploys the new version of the service alongside the previous version. User accounts are then progressively switched to the new version, at every which point all new queries issued by the respective user are directed to the new version. All queries that were executing against the previous version are allowed to run to completion. Once all queries and users have finished using the previous version, all services of that version are terminated and decommissioned.

Figure 3 shows a snapshot of an ongoing upgrade process. There are two versions of Snowflake running side-by-side, version 1 (light) and version 2 (dark). There are two versions of a single incarnation of Cloud Services, controlling two virtual warehouses (VWs), each having two versions. The load balancer directs incoming calls to the appropriate version of Cloud Services. The Cloud Services of one version only talk to VWs of a matching version.

As mentioned previously, both versions of Cloud Services share the same metadata store. What is more, VWs of different versions are able to share the same worker nodes and their respective caches. Consequently, there is no need to repopulate the caches after an upgrade. The entire process is transparent to the user with no downtime or performance degradation.

Online upgrade also has had a tremendous effect on our speed of development, and on how we handle critical bugs at Snowflake. At the time of writing, we upgrade all services once per week. That means we release features and improvements on a weekly basis. To ensure the upgrade process goes smoothly, both upgrade and downgrade are continuously tested in a special pre-production incarnation of Snowflake. In those rare cases where we find a critical bug in our production incarnation (not necessarily during an upgrade), we can very quickly downgrade to the previous version, or implement a fix and perform an out-of-schedule upgrade. This process is not as scary as it may sound, because we continuously test and exercise the upgrade/downgrade mechanism. It is highly automated and hardened at this point.

Figure.

Figure 3: Online Upgrade {#dageville-2016-snowflake-fig-3 .figure tag=07A4}

### 4.3 Semi-Structured and Schema-Less Data {#dageville-2016-snowflake-s4-3 .section tag=07A5}

Snowflake extends the standard SQL type system with three types for semi-structured data: VARIANT, ARRAY, and OBJECT. Values of type VARIANT can store any value of native SQL type (DATE, VARCHAR etc.), as well as variable-length ARRAYS of values, and JavaScript-like OBJECTs, maps from strings to VARIANT values. The latter are also called documents in the literature, giving rise to the notion of document stores (MongoDB [39], Couchbase [23]).

ARRAY and OBJECT are just restrictions of type VARIANT. The internal representation is the same: a self-describing, compact binary serialization which supports fast key-value lookup, as well as efficient type tests, comparison, and hashing. VARIANT columns can thus be used as join keys, grouping keys, and ordering keys, just like any other column.

The VARIANT type allows Snowflake to be used in an ELT (Extract-Load-Transform) manner rather than a traditional ETL (Extract-Transform-Load) manner. There is no need to specify document schemas or to perform transformations on the load. Users can load their input data from JSON, Avro, or XML format directly into a VARIANT column; Snowflake handles parsing and type inference (cf. Section 4.3.3). This approach, aptly called “schema later” in the literature, allows for schema evolution by decoupling information producers from information consumers and any intermediaries. In contrast, any change in data schemas in a conventional ETL pipeline requires coordination between multiple departments in an organization, which can take months to execute.

Another advantage of ELT and Snowflake is that later, if transformation is desired, it can be performed using the full power of a parallel SQL database, including operations such as joins, sorting, aggregation, complex predicates and so forth, which are typically missing or inefficient in conventional ETL toolchains. On that point, Snowflake also features procedural user-defined functions (UDFs) with full JavaScript syntax and integration with the VARIANT data type. Support for procedural UDFs further increases the number of ETL tasks that can be pushed into Snowflake.

### 4.3.1 Post-relational Operations {#dageville-2016-snowflake-s4-3-1 .section tag=07A6}

The most important operation on documents is extraction of data elements, either by field name (for OBJECTs), or by offset (for ARRAYS). Snowflake provides extraction operations in both functional SQL notation and JavaScript-like path syntax. The internal encoding makes extraction very efficient. A child element is just a pointer inside the parent element; no copying is required. Extraction is often followed by a cast of the resulting VARIANT value to a standard SQL type. Again, the encoding makes these casts very efficient.

The second common operation is flattening, i.e. pivoting a nested document into multiple rows. Snowflake uses SQL lateral views to represent flattening operations. This flattening can be recursive, allowing the complete conversion of the hierarchical structure of the document into a relational table amenable to SQL processing. The opposite operation to flattening is aggregation. Snowflake introduces a few new aggregate and analytic functions such as ARRAY_AGG and OBJECT_AGG for this purpose.

### 4.3.2 Columnar Storage and Processing {#dageville-2016-snowflake-s4-3-2 .section tag=07A7}

The use of a serialized (binary) representation for semi-structured data is a conventional design choice for integrating semi-structured data into relational databases. The rowwise representation, unfortunately, makes storage and processing of such data less efficient than that of columnar relational data—which is the usual reason for transforming semi-structured data into plain relational data.

Figure 4: TPC-H SF100 and SF1000 Performance: Relational vs. Schema-less Row Format {#dageville-2016-snowflake-fig-4 .figure tag=07A8}

Cloudera Impala [21] (using Parquet [10]) and Google Dremel [34] have demonstrated that columnar storage of semi-structured data is possible and beneficial. However, Impala and Dremel (and its externalization BigQuery [44]) require users to provide complete table schemas for columnar storage. To achieve *both* the flexibility of a schema-less serialized representation and the performance of a columnar relational database, Snowflake introduces a novel automated approach to type inference and columnar storage.

As mentioned in Section 3.1, Snowflake stores data in a hybrid columnar format. When storing semi-structured data, the system automatically performs statistical analysis of the collection of documents within a single table file, to perform automatic type inference and to determine which (typed) paths are frequently common. The corresponding columns are then removed from the documents and stored separately, using the same compressed columnar format as native relational data. For these columns, Snowflake even computes materialized aggregates for use by pruning (cf. Section 3.3.3), as with plain relational data.

During a scan, the various columns can be reassembled into a single column of type VARIANT. Most queries, however, are only interested in a subset of the columns of the original document. In those cases, Snowflake pushes projection and cast expressions down into the scan operator, so that only the necessary columns are accessed and cast directly into the target SQL type.

The optimizations described above are performed *independently* for every table file, which allows for efficient storage and extraction even under schema evolution. However, it does raise challenges with respect to query optimization, in particular pruning. Suppose a query has a predicate over a path expression, and we would like to use pruning to restrict the set of files to be scanned. The path and corresponding column may be present in most files, but only frequent enough to warrant metadata in some of the files. The conservative solution is to simply scan all files for which there is no suitable metadata. Snowflake improves over this solution by computing Bloom filters over all *paths* (not values!) present in the documents. These Bloom filters are saved along with the other file metadata, and probed by the query optimizer during pruning. Table files which do not contain paths required by a given query can safely be skipped.

### 4.3.3 *Optimistic Conversion* {#dageville-2016-snowflake-s4-3-3 .section tag=07A9}

Because some native SQL types, notably date/time values, are represented as strings in common external formats such as JSON or XML, these values need to be converted from strings to their actual type either at write time (during insert or update) or at read time (during queries). Without a typed schema or equivalent hints, these string conversions need to be performed at read time, which, in a read-dominated workload, is less efficient than doing the conversions once, during the write. Another problem with untyped data is the lack of suitable metadata for pruning, which is especially important in case of dates. (Analytical workloads frequently have range predicates on date columns.)

But applied at write time, automatic conversions may lose information. For example, a field containing numeric product identifiers may actually not be a number but a string with significant leading zeros. Similarly, what looks like a date could really be the content of a text message. Snowflake solves the problem by performing optimistic data conversion, and preserving both the result of the conversion and the original string (unless a fully reversible conversion exists), in separate columns. If a query later requires the original string, it is easily retrieved or reconstructed. Because unused columns are not loaded and accessed, the impact of any double storage on query performance is minimal.

### 4.3.4 *Performance* {#dageville-2016-snowflake-s4-3-4 .section tag=07AA}

To assess the combined effects of columnar storage, optimistic conversion, and pruning over semi-structured data on query performance, we conducted a set of experiments using TPC-H-like\footnote{Experimental results were obtained using a faithful implementation of TPC-H data generation and queries. Nonetheless, the data, queries, and numbers have not been verified by the TPC and do not constitute official benchmark results.} data and queries.

We created two types of database schemas. First, a conventional, relational TPC-H schema. Second, a “schema-less” database schema, where every table consisted of a single column of type VARIANT. We then generated clustered (sorted) SF100 and SF1000 data sets (100 GB and 1 TB respectively), stored the data sets in plain JSON format (i.e., dates became strings), and loaded that data into Snowflake, using both the relational and schema-less database schemas. No hints of any kind regarding the fields, types, and clustering of the schema-less data were given to the system, and no other tuning was done. We then defined a few views on top of the schema-less databases, in order to be able to run the exact same set of TPC-H queries against all four databases. (At the time of writing, Snowflake does not use views for type inference or other optimizations, so this was purely a syntactic convenience.)

Finally, we ran all 22 TPC-H queries against the four databases, using a medium standard warehouse⁵ Figure 4 shows the results. Numbers were obtained over three runs with warm caches. Standard errors were insignificant and thus omitted from the results.

As can be seen, the overhead of schema-less storage and query processing was around 10% for all but two queries (Q9 and Q17 over SF1000). For these two queries, we determined the reason for the slow-down to be a sub-optimal join order, caused by a known bug in distinct value estimation. We continue to make improvements to metadata collection and query optimization over semi-structured data.

In summary, the query performance over semi-structured data with relatively stable and simple schemas (i.e. the majority of machine-generated data found in practice), is nearly on par with the performance over conventional relational data, enjoying all the benefits of columnar storage, columnar execution, and pruning—without the user effort.

### 4.4 Time Travel and Cloning {#dageville-2016-snowflake-s4-4 .section tag=07AB}

In Section 3.3.2, we discussed how Snowflake implements Snapshot Isolation (SI) on top of multi-version concurrency control (MVCC). Write operations (insert, update, delete, merge) on a table produce a newer version of the table by adding and removing whole files.

When files are removed by a new version, they are retained for a configurable duration (currently up to 90 days). File retention allows Snowflake to read earlier versions of tables very efficiently; that is, to perform time travel on the database. Users can access this feature from SQL using the convenient AT or BEFORE syntax. Timestamps can be absolute, relative with respect to current time, or relative with respect to previous statements (referred to by ID).

SELECT * FROM my_table AT(TIMESTAMP => 'Mon, 01 May 2015 16:20:00 -0700'::timestamp);
SELECT * FROM my_table AT(OFFSET => -60*5); -- 5 min ago
SELECT * FROM my_table BEFORE(STATEMENT => '8e5d0ca9-005e-44e6-b858-a8f5b37c5726');

One can even access different versions of the same table in a single query.

SELECT new.key, new.value, old.value FROM my_table new
JOIN my_table AT(OFFSET => -86400) old -- 1 day ago
ON new.key = old.key WHERE new.value <> old.value;

Based on the same underlying metadata, Snowflake introduces the UNDROP keyword to quickly restore tables, schemas, or whole databases that have been dropped accidentally.

DROP DATABASE important_db; -- whoops!
UNDROP DATABASE important_db;

Snowflake also implements a functionality we call cloning, expressed through the new keyword CLONE. Cloning a table creates a new table with the same definition and contents quickly and without making physical copies of table

⁵We currently do not disclose pricing and hardware details, but a medium standard warehouse consists of a very small number of inexpensive EC2 instances.

Figure.

Figure 5: Encryption Key Hierarchy {#dageville-2016-snowflake-fig-5 .figure tag=07AC}

files. The clone operation simply copies the metadata of the source table. Right after cloning, both tables refer to the same set of files, but both tables can be modified independently thereafter. The clone feature also supports whole schemas or databases, which allows for very efficient snapshots. Snapshots are good practice before a large batch of updates, or when performing lengthy, exploratory data analysis. The CLONE keyword can even be combined with AT and BEFORE, allowing such snapshots to be made after the fact.

CREATE DATABASE recovered_db CLONE important_db BEFORE(
    STATEMENT => '8e5d0ca9-005e-44e6-b858-a8f5b37c5726');

### 4.5 Security {#dageville-2016-snowflake-s4-5 .section tag=07AD}

Snowflake is designed to protect user data against attacks on all levels of the architecture, including the cloud platform. To this end, Snowflake implements two-factor authentication, (client-side) encrypted data import and export, secure data transfer and storage, and role-based access control (RBAC [26]) for database objects. At all times, data is encrypted before being sent over the network, and before being written to local disk or shared storage (S3). Thus, Snowflake provides full end-to-end data encryption and security.

### 4.5.1 Key Hierarchy {#dageville-2016-snowflake-s4-5-1 .section tag=07AE}

Snowflake uses strong AES 256-bit encryption with a hierarchical key model rooted in AWS CloudHSM [12]. Encryption keys are automatically rotated and re-encrypted ("rekeyed") to ensure that keys complete the full NIST 800-57 cryptographic key-management life cycle [13]. Encryption and key management are entirely transparent to the user and require no configuration or management.

The Snowflake key hierarchy, shown in Figure 5, has four levels: root keys, account keys, table keys, and file keys. Each layer of (parent) keys encrypts i.e. wraps the layer of (child) keys below. Each account key corresponds to one user account, each table key corresponds to one database table, and each file key corresponds to one table file.

Hierarchical key models are good security practice because they constrain the amount of data each key protects. Each layer reduces the scope of keys below it, as indicated by the boxes in Figure 5. Snowflake’s hierarchical key model ensures isolation of user data in its multi-tenant architecture, because each user account has a separate account key.

### 4.5.2 Key Life Cycle {#dageville-2016-snowflake-s4-5-2 .section tag=07AF}

Orthogonal to constraining the amount of data each key protects, Snowflake also constrains the duration of time during which a key is usable. Encryption keys go through four phases: (1) a pre-operational creation phase, (2) an operational phase where keys are used to encrypt (originator-usage period) and decrypt (recipient-usage period), (3) a post-operational phase where keys are no longer in use, and (4) a destroyed phase. Phases 1, 3, and 4 are trivial to implement. Phase 2 requires one to limit the originator-usage and recipient-usage periods. Only when a key no longer encrypts any required data, it can be moved on to phases 3 and 4. Snowflake limits the originator-usage period using *key rotation* and the recipient-usage period using *rekeying*.

**Key rotation** creates new versions of keys at regular intervals (say, one month). After each such interval, a new version of a key is created and the previous version of the key is “retired”. The retired version is still usable, but only to decrypt data. When wrapping new child keys in the key hierarchy, or when writing to tables, only the latest, active version of the key is used to encrypt the data.

**Rekeying** is the process of re-encrypting old data with new keys. After a specific time interval (say, one year), data that has been encrypted with a retired key is re-encrypted with an active key. This rekeying is orthogonal to key rotation. While key rotation ensures that a key is transferred from its active state (originator usage) to a retired state (recipient usage), rekeying ensures that a key can be transferred from its retired state to being destroyed.

Figure 6 shows the life cycle of a single table key. Assume keys are rotated once per month, and data is rekeyed once per year. Table files 1 and 2 are created in April 2014, using key 1 version 1 (k1v1). In May 2014, key 1 is rotated to version 2 (k1v2), and table file 3 is created using k1v2. In June 2014, key 1 is rotated to version 3 (k1v3), and two more table files are created. No more inserts or updates are made to the table after June 2014. In April 2015, k1v1 becomes one year old and needs to be destroyed. A new key, key 2 version 1 (k2v1), is created, and all files associated with k1v1 are rekeyed using k2v1. In May 2015, the same happens to k1v2 and table file 3 is rekeyed using k2v2. In June 2015, table files 4 and 5 are rekeyed using k2v3.

An analogous scheme is implemented between account keys and table keys, and between the root key and account keys. Each level of the key hierarchy undergoes key rotation and rekeying, including the root key. Key rotation and rekeying of account keys and the root key do not require re-encryption of files. Only the *keys* of the immediate lower level need to be re-encrypted.

The relationship between table keys and file keys is different though. File keys are not wrapped by table keys. Instead, file keys are cryptographically derived from the combination of table key and (unique) file name. It follows that whenever a table key changes, all of its related file keys change, so the affected table files need to be re-encrypted. The big benefit of key derivation, however, is that it removes the need to create, manage, and pass around individual file keys. A system like Snowflake that handles billions of files would have to handle many gigabytes of file keys otherwise.

We chose this design also because Snowflake’s separation of storage and compute allows it to perform re-encryption without impacting user workloads. Rekeying works in the background, using different worker nodes than queries. After files are rekeyed, Snowflake atomically updates the metadata of database tables to point to the newly encrypted files. The old files are deleted once all ongoing queries are finished.

### 4.5.3 End-to-End Security {#dageville-2016-snowflake-s4-5-3 .section tag=07B0}

Snowflake uses AWS CloudHSM as a tamper-proof, highly secure way to generate, store, and use the root keys of the key hierarchy. AWS CloudHSM is a set of hardware security modules (HSMs) that are connected to a virtual private cluster within AWS. The root keys never leave the HSM devices. All cryptographic operations using root keys are performed within the HSMs themselves. Thus, lower-level keys cannot be unwrapped without authorized access to the HSM devices. The HSMs are also used to generate keys at the account and table levels, including during key rotation and rekeying. We configured AWS CloudHSM in its high-availability configuration to minimize the possibility of service outages.

In addition to data encryption, Snowflake protects user data in the following ways:

1. Isolation of storage through access policies on S3.
2. Role-based access control within user accounts for fine-grained access control to database objects.
3. Encrypted data import and export without the cloud provider (Amazon) ever seeing data in the clear.
4. Two-factor- and federated authentication for secure access control.

In summary, Snowflake provides a hierarchical key model rooted in AWS CloudHSM and uses key rotation and rekeying to ensure that encryption keys follow a standardized life cycle. Key management is entirely transparent to the user and requires no configuration, management, or downtime. It is part of a comprehensive security strategy that enables full end-to-end encryption and security.
