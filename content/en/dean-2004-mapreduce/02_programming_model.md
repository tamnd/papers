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
section_title: Programming Model
tag: 006C
kind: section
lang: en
source: https://www.usenix.org/legacy/events/osdi04/tech/full_papers/dean/dean.pdf
pdf_sha256: 9cfef3ef1b8fe1a1b66c7221f56c2eeca0b15d6608ea68b0c85a38bfbffd8ce5
pdf_pages: 2-3
extraction: vision
extraction_model: gpt-5
content_sha256: c7e67fc6b1103b4953278edc167bdfc9009815abad8934e8d5cc8c236f7a0d6f
prompt_sha256: e1b070d511afab62a45db64b491e759e38eaa12f6c7943b773a942f4f2f70935
---

The computation takes a set of input key/value pairs, and produces a set of output key/value pairs. The user of the MapReduce library expresses the computation as two functions: Map and Reduce.

Map, written by the user, takes an input pair and produces a set of intermediate key/value pairs. The MapReduce library groups together all intermediate values associated with the same intermediate key $I$ and passes them to the Reduce function.

The Reduce function, also written by the user, accepts an intermediate key $I$ and a set of values for that key. It merges together these values to form a possibly smaller set of values. Typically just zero or one output value is produced per Reduce invocation. The intermediate values are supplied to the user’s reduce function via an iterator. This allows us to handle lists of values that are too large to fit in memory.

### 2.1 Example {#dean-2004-mapreduce-s2-1 .section tag=006D}

Consider the problem of counting the number of occurrences of each word in a large collection of documents. The user would write code similar to the following pseudo-code:

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

The map function emits each word plus an associated count of occurrences (just ‘1’ in this simple example). The reduce function sums together all counts emitted for a particular word.

In addition, the user writes code to fill a mapreduce specification object with the names of the input and output files, and optional tuning parameters. The user then invokes the MapReduce function, passing it the specification object. The user’s code is linked together with the MapReduce library (implemented in C++). Appendix A contains the full program text for this example.

### 2.2 Types {#dean-2004-mapreduce-s2-2 .section tag=006E}

Even though the previous pseudo-code is written in terms of string inputs and outputs, conceptually the map and reduce functions supplied by the user have associated types:

```text
map     (k1,v1)          → list(k2,v2)
reduce  (k2,list(v2))    → list(v2)
```

I.e., the input keys and values are drawn from a different domain than the output keys and values. Furthermore, the intermediate keys and values are from the same domain as the output keys and values.

Our C++ implementation passes strings to and from the user-defined functions and leaves it to the user code to convert between strings and appropriate types.

### 2.3 More Examples {#dean-2004-mapreduce-s2-3 .section tag=006F}

Here are a few simple examples of interesting programs that can be easily expressed as MapReduce computations.

Distributed Grep: The map function emits a line if it matches a supplied pattern. The reduce function is an identity function that just copies the supplied intermediate data to the output.

Count of URL Access Frequency: The map function processes logs of web page requests and outputs $\langle URL,1\rangle$. The reduce function adds together all values for the same URL and emits a $\langle URL,total\ count\rangle$ pair.

Reverse Web-Link Graph: The map function outputs $\langle target,source\rangle$ pairs for each link to a target URL found in a page named source. The reduce function concatenates the list of all source URLs associated with a given target URL and emits the pair: $\langle target,list(source)\rangle$

Term-Vector per Host: A term vector summarizes the most important words that occur in a document or a set of documents as a list of $\langle word,frequency\rangle$ pairs. The map function emits a $\langle hostname,term\ vector\rangle$ pair for each input document (where the hostname is extracted from the URL of the document). The reduce function is passed all per-document term vectors for a given host. It adds these term vectors together, throwing away infrequent terms, and then emits a final $\langle hostname,term\ vector\rangle$ pair.

Figure 1: Execution overview {#dean-2004-mapreduce-fig-1 .figure tag=0070}

Inverted Index: The map function parses each document, and emits a sequence of $\langle word, document\ ID\rangle$ pairs. The reduce function accepts all pairs for a given word, sorts the corresponding document IDs and emits a $\langle word, list(document\ ID)\rangle$ pair. The set of all output pairs forms a simple inverted index. It is easy to augment this computation to keep track of word positions.

Distributed Sort: The map function extracts the key from each record, and emits a $\langle key, record\rangle$ pair. The reduce function emits all pairs unchanged. This computation depends on the partitioning facilities described in Section 4.1 and the ordering properties described in Section 4.2.
