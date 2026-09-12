---
paper: corbett-2012-spanner
title: 'Spanner: Google''s Globally-Distributed Database'
authors:
  - James C. Corbett
  - Jeffrey Dean
  - Michael Epstein
  - Andrew Fikes
  - Christopher Frost
  - J. J. Furman
  - Sanjay Ghemawat
  - Andrey Gubarev
  - Christopher Heiser
  - Peter Hochschild
year: 2012
venue: OSDI
field: databases
section: "3"
section_title: TrueTime
tag: 00A5
kind: section
lang: en
source: http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.258.9924
pdf_sha256: 61875779e75f603d21aefba6d9bd9816d4dd0c18cf41089f43707249e24bbf88
pdf_pages: 5-6
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: d2bb5ab6879c6762ffa848154e4205b016ec973179bcf36dd834ca729015c0c5
prompt_sha256: 329630a0b9175a55e4af1b8e281a3e67eeab250f8d643953b7dcde99743c7628
---

| Method | Returns |
| --- | --- |
| *TT.now()* | *TTinterval:* [earliest, latest] |
| *TT.after(t)* | true if $t$ has definitely passed |
| *TT.before(t)* | true if $t$ has definitely not arrived |

Table 1: TrueTime API. The argument $t$ is of type $TTstamp$. {#corbett-2012-spanner-tab-1 .table tag=00A6}

This section describes the TrueTime API and sketches its implementation. We leave most of the details for another paper: our goal is to demonstrate the power of having such an API. Table 1 lists the methods of the API. TrueTime explicitly represents time as a $TTinterval$, which is an interval with bounded time uncertainty (unlike standard time interfaces that give clients no notion of uncertainty). The endpoints of a $TTinterval$ are of type $TTstamp$. The $TT.now()$ method returns a $TTinterval$ that is guaranteed to contain the absolute time during which $TT.now()$ was invoked. The time epoch is analogous to UNIX time with leap-second smearing. Define the instantaneous error bound as $\epsilon$, which is half of the interval’s width, and the average error bound as $\bar{\epsilon}$. The $TT.after()$ and $TT.before()$ methods are convenience wrappers around $TT.now()$.

Denote the absolute time of an event $e$ by the function $t_{abs}(e)$. In more formal terms, TrueTime guarantees that for an invocation $tt = TT.now(), tt.earliest \leq t_{abs}(e_{now}) \leq tt.latest$, where $e_{now}$ is the invocation event.

The underlying time references used by TrueTime are GPS and atomic clocks. TrueTime uses two forms of time reference because they have different failure modes. GPS reference-source vulnerabilities include antenna and receiver failures, local radio interference, correlated failures (e.g., design faults such as incorrect leap-second handling and spoofing), and GPS system outages. Atomic clocks can fail in ways uncorrelated to GPS and each other, and over long periods of time can drift significantly due to frequency error.

TrueTime is implemented by a set of *time master* machines per datacenter and a *timeslave daemon* per machine. The majority of masters have GPS receivers with dedicated antennas; these masters are separated physically to reduce the effects of antenna failures, radio interference, and spoofing. The remaining masters (which we refer to as *Armageddon masters*) are equipped with atomic clocks. An atomic clock is not that expensive: the cost of an Armageddon master is of the same order as that of a GPS master. All masters’ time references are regularly compared against each other. Each master also cross-checks the rate at which its reference advances time against its own local clock, and evicts itself if there is substantial divergence. Between synchronizations, Armageddon masters advertise a slowly increasing time uncertainty that is derived from conservatively applied worst-case clock drift. GPS masters advertise uncertainty that is typically close to zero.

Every daemon polls a variety of masters [29] to reduce vulnerability to errors from any one master. Some are GPS masters chosen from nearby datacenters; the rest are GPS masters from farther datacenters, as well as some Armageddon masters. Daemons apply a variant of Marzullo’s algorithm [27] to detect and reject liars, and synchronize the local machine clocks to the non-liars. To protect against broken local clocks, machines that exhibit frequency excursions larger than the worst-case bound derived from component specifications and operating environment are evicted.

Between synchronizations, a daemon advertises a slowly increasing time uncertainty. $\epsilon$ is derived from conservatively applied worst-case local clock drift. $\epsilon$ also depends on time-master uncertainty and communication delay to the time masters. In our production environment, $\epsilon$ is typically a sawtooth function of time, varying from about 1 to 7 ms over each poll interval. $\bar{\epsilon}$ is therefore 4 ms most of the time. The daemon’s poll interval is currently 30 seconds, and the current applied drift rate is set at 200 microseconds/second, which together account

| Operation | Timestamp Discussion | Concurrency Control | Replica Required |
| --- | --- | --- | --- |
| Read-Write Transaction | § 4.1.2 | pessimistic | leader |
| Read-Only Transaction | § 4.1.4 | lock-free | leader for timestamp; any for read, subject to § 4.1.3 |
| Snapshot Read, client-provided timestamp | — | lock-free | any, subject to § 4.1.3 |
| Snapshot Read, client-provided bound | § 4.1.3 | lock-free | any, subject to § 4.1.3 |

Table 2: Types of reads and writes in Spanner, and how they compare. {#corbett-2012-spanner-tab-2 .table tag=00A7}

for the sawtooth bounds from 0 to 6 ms. The remaining 1 ms comes from the communication delay to the time masters. Excursions from this sawtooth are possible in the presence of failures. For example, occasional time-master unavailability can cause datacenter-wide increases in $\epsilon$. Similarly, overloaded machines and network links can result in occasional localized $\epsilon$ spikes.
