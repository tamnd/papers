---
paper: ritchie-1974-unix
title: The UNIX Time-Sharing System
authors:
  - Dennis M. Ritchie
  - Ken Thompson
year: 1974
venue: Communications of the ACM
field: systems
section: "9"
section_title: Statistics
tag: "0620"
kind: section
lang: en
source: https://dsf.berkeley.edu/cs262/unix.pdf
pdf_sha256: 96bc5caa11cc13925165b6d36b78c55cc61a61e65a628c375511683a97442b51
pdf_pages: 10-11
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 569395b3a7d5c64784eb80e3d3d636e62a6c00599fecf079b82737d79c01c2ab
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The following statistics from UNIX are presented to show the scale of the system and to show how a system of this scale is used. Those of our users not involved in document preparation tend to use the system for program development, especially language work. There are few important “applications” programs.

### 9.1 Overall {#ritchie-1974-unix-s9-1 .section tag=0621}

72 user population
14 maximum simultaneous users
300 directories
4400 files
34000 512-byte secondary storage blocks used

### 9.2 Per day (24-hour day, 7-day week basis) {#ritchie-1974-unix-s9-2 .section tag=0622}

There is a “background” process that runs at the lowest possible priority; it is used to soak up any idle CPU time. It has been used to produce a million-digit approximation to the constant e − 2, and is now generating composite pseudoprimes (base 2).

1800 commands
4.3 CPU hours (aside from background)
70 connect hours
30 different users
75 logins

### 9.3 Command CPU Usage (cut off at 1%) {#ritchie-1974-unix-s9-3 .section tag=0623}

| 15.7% | C compiler | 1.7% | Fortran compiler |
| --- | --- | --- | --- |
| 15.2% | users’ programs | 1.6% | remove file |
| 11.7% | editor | 1.6% | tape archive |
| 5.8% | Shell (used as a command, including command times) | 1.6% | file system consistency check |
| 5.3% | chess | 1.4% | library maintainer |
| 3.3% | list directory | 1.3% | concatenate/print files |
| 3.1% | document formatter | 1.1% | paginate and print file |
| 1.6% | backup dumper | 1.0% | print disk usage |
| 1.8% | assembler |  | copy file |

### 9.4 Command Accesses (cut off at 1%) {#ritchie-1974-unix-s9-4 .section tag=0624}

| 15.3% | editor | 1.6% | debugger |
| --- | --- | --- | --- |
| 9.6% | list directory | 1.6% | Shell (used as a command) |
| 6.3% | remove file | 1.5% | print disk availability |
| 6.3% | C compiler | 1.4% | list processes executing |
| 6.0% | concatenate/print file | 1.4% | assembler |
| 6.0% | users’ programs | 1.4% | print arguments |
| 3.3% | list people logged on system | 1.2% | copy file |
| 3.2% | rename/move file | 1.1% | paginate and print file |
| 3.1% | file status | 1.1% | print current date/time |
| 1.8% | library maintainer | 1.1% | file system consistency check |
| 1.8% | document formatter | 1.0% | tape archive |
| 1.6% | execute another command conditionally |  |  |

### 9.5 Reliability {#ritchie-1974-unix-s9-5 .section tag=0625}

Our statistics on reliability are much more subjective than the others. The following results are true to the best of our combined recollections. The time span is over one year with a very early vintage 11/45.

There has been one loss of a file system (one disk out of five) caused by software inability to cope with a hardware problem causing repeated power fail traps. Files on that disk were backed up three days.

A “crash” is an unscheduled system reboot or halt. There is about one crash every other day; about two-thirds of them are caused by hardware-related difficulties such as power dips and inexplicable processor interrupts to random locations. The remainder are software failures. The longest uninterrupted up time was about two weeks. Service calls average one every three weeks, but are heavily clustered. Total up time has been about 98 percent of our 24-hour, 365-day schedule.

Acknowledgments. We are grateful to R.H. Canaday, L.L. Cherry, and L.E. McMahon for their contributions to UNIX. We are particularly appreciative of the inventiveness, thoughtful criticism, and constant support of R. Morris, M.D. McIlroy, and J.F. Ossanna.
