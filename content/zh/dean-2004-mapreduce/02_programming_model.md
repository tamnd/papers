---
paper: dean-2004-mapreduce
title: 'MapReduce: Simplified Data Processing on Large Clusters'
authors:
  - Jeffrey Dean
  - Sanjay Ghemawat
year: 2004
venue: OSDI
field: systems
section: "2"
section_title: 编程模型
kind: section
lang: zh
source: https://www.usenix.org/legacy/events/osdi04/tech/full_papers/dean/dean.pdf
pdf_sha256: 9cfef3ef1b8fe1a1b66c7221f56c2eeca0b15d6608ea68b0c85a38bfbffd8ce5
pdf_pages: 2-3
extraction: vision
extraction_model: gpt-5
content_sha256: 714690bb40a91de841dcc1f89f71072870b4c0aea2975183b08be5c6146a0d1f
translated_from: content/en/dean-2004-mapreduce/02_programming_model.md
source_content_sha256: aaf581737cd4d87ef514b916c1ce15d8ee969caef455403515366f71228c9af2
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: 7271f7a32ca37292fd19d5ef38fdc1daa670346e7d1f46fdd75a6f589873c903
prompt_sha256: da0c2696badfbe5d93fdc534847b1b0ca3b25ec37e0ce29843665f6e701c278e
---

该计算接收一组输入键/值对，并产生一组输出键/值对。MapReduce 库的用户将该计算表示为两个函数：Map 和 Reduce。

由用户编写的 Map 接收一个输入对，并产生一组中间键/值对。MapReduce 库将与同一个中间键 $I$ 关联的所有中间值聚合在一起，并将它们传递给 Reduce 函数。

同样由用户编写的 Reduce 函数接收一个中间键 $I$ 和该键的一组值。它将这些值合并起来，形成一个可能更小的值集合。通常，每次调用 Reduce 只产生零个或一个输出值。中间值通过迭代器提供给用户的 reduce 函数。这使我们能够处理大到无法放入内存的值列表。

### 2.1 示例

考虑在一个大型文档集合中统计每个单词出现次数的问题。用户将编写类似如下伪代码的代码：

```text
map(String key, String value):
    // key: document name
    // value: document contents
    for each word w in value:
        EmitIntermediate(w, "1");

reduce(String key, Iterator values):
    // key: a word
    // values: a list of counts
    int result = 0;
    for each v in values:
        result += ParseInt(v);
    Emit(AsString(result));
```

map 函数输出每个单词以及与其关联的出现次数（在这个简单示例中只是‘1’）。reduce 函数将针对某个单词输出的所有计数相加。

此外，用户编写代码，用输入和输出文件的名称以及可选的调优参数填充一个 mapreduce 规范对象。然后用户调用 MapReduce 函数，并向其传递该规范对象。用户的代码与 MapReduce 库（使用 C++ 实现）链接在一起。附录 A 包含该示例的完整程序文本。

### 2.2 类型

尽管前面的伪代码以字符串输入和输出的形式编写，但从概念上讲，用户提供的 map 和 reduce 函数具有相关类型：

```text
map     (k1,v1)          → list(k2,v2)
reduce  (k2,list(v2))    → list(v2)
```

即，输入键和值来自与输出键和值不同的域。此外，中间键和值与输出键和值来自同一个域。

我们的 C++ 实现向用户定义的函数传递字符串并从中接收字符串，并由用户代码负责在字符串和适当类型之间进行转换。

### 2.3 更多示例

下面是几个可以很容易表示为 MapReduce 计算的有趣程序的简单示例。

分布式 Grep：如果某行匹配给定模式，map 函数就输出该行。reduce 函数是一个恒等函数，只是将提供的中间数据复制到输出。

URL 访问频率统计：map 函数处理网页请求的日志，并输出 $\langle URL,1\rangle$。reduce 函数将相同 URL 的所有值相加，并输出一个 $\langle URL,total\ count\rangle$ 对。

反向 Web 链接图：对于在名为 source 的页面中发现的每个指向目标 URL 的链接，map 函数输出 $\langle target,source\rangle$ 对。reduce 函数连接与给定目标 URL 关联的所有源 URL 列表，并输出该对：$\langle target,list(source)\rangle$

每个主机的词项向量：词项向量将文档或一组文档中出现的最重要单词总结为一个 $\langle word,frequency\rangle$ 对列表。map 函数为每个输入文档输出一个 $\langle hostname,term\ vector\rangle$ 对（其中 hostname 从文档的 URL 中提取）。reduce 函数接收给定主机的所有文档级词项向量。它将这些词项向量相加，丢弃低频词项，然后输出最终的 $\langle hostname,term\ vector\rangle$ 对。

图 1：执行概览

倒排索引：map 函数解析每个文档，并输出一个 $\langle word, document\ ID\rangle$ 对序列。reduce 函数接收给定单词的所有对，对相应的文档 ID 进行排序，并输出一个 $\langle word, list(document\ ID)\rangle$ 对。所有输出对的集合形成一个简单的倒排索引。很容易扩展该计算以跟踪单词位置。

分布式排序：map 函数从每条记录中提取键，并输出一个 $\langle key, record\rangle$ 对。reduce 函数原样输出所有对。该计算依赖于第 4.1 节中描述的分区机制以及第 4.2 节中描述的排序属性。
