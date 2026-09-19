---
paper: ritchie-1974-unix
title: The UNIX Time-Sharing System
authors:
  - Dennis M. Ritchie
  - Ken Thompson
year: 1974
venue: Communications of the ACM
field: systems
section: "5"
section_title: Processes and Images
tag: 060F
kind: section
lang: en
source: https://dsf.berkeley.edu/cs262/unix.pdf
pdf_sha256: 96bc5caa11cc13925165b6d36b78c55cc61a61e65a628c375511683a97442b51
pdf_pages: 6-7
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 3b5fce664fec3959c498cc9da5bce8430de5f2b17c41033cf43a497b493c27d7
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

An image is a computer execution environment. It includes a core image, general register values, status of open files, current directory, and the like. An image is the current state of a pseudo computer.

A process is the execution of an image. While the processor is executing on behalf of a process, the image must reside in core; during the execution of other processes it remains in core unless the appearance of an active, higher-priority process forces it to be swapped out to the fixed-head disk.

The user-core part of an image is divided into three logical segments. The program text segment begins at location 0 in the virtual address space. During execution, this segment is write-protected and a single copy of it is shared among all processes executing the same program. At the first 8K byte boundary above the program text segment in the virtual address space begins a non-shared, writable data segment, the size of which may be extended by a system call. Starting at the highest address in the virtual address space is a stack segment, which automatically grows downward as the hardware’s stack pointer fluctuates.

### 5.1 Processes {#ritchie-1974-unix-s5-1 .section tag=0610}

Except while UNIX is bootstrapping itself into operation, a new process can come into existence only by use of the fork system call:

processid = fork (label)

When fork is executed by a process, it splits into two independently executing processes. The two processes have independent copies of the original core image, and share any open files. The new processes differ only in that one is considered the parent process: in the parent, control returns directly from the fork, while in the child, control is passed to location label. The processid returned by the fork call is the identification of the other process.

Because the return points in the parent and child process are not the same, each image existing after a fork may determine whether it is the parent or child process.

### 5.2 Pipes {#ritchie-1974-unix-s5-2 .section tag=0611}

Processes may communicate with related processes using the same system read and write calls that are used for file system I/O. The call filep = pipe( ) returns a file descriptor filep and creates an interprocess channel called a pipe. This channel, like other open flies, is passed from parent to child process in the image by the fork call. A read using a pipe file descriptor waits until another process writes using the file descriptor for the same pipe. At this point, data are passed between the images of the two processes. Neither process need know that a pipe, rather than an ordinary file, is involved.

Although interprocess communication via pipes is a quite valuable tool (see §6.2), it is not a completely general mechanism since the pipe must be set up by a common ancestor of the processes involved.

### 5.3 Execution of Programs {#ritchie-1974-unix-s5-3 .section tag=0612}

Another major system primitive is invoked by execute(file, arg₁, arg₂, ..., argₙ) which requests the system to read in and execute the program named by file, passing it string arguments arg₁, arg₂, ..., argₙ. Ordinarily, arg₁ should be the same string as file, so that the program may determine the name by which it was invoked. All the code and data in the process using execute is replaced from the file, but open files, current directory, and interprocess relationships are unaltered. Only if the call fails, for example because file could not be found or because its execute-permission bit was not set, does a return take place from the execute primitive; it resembles a “jump” machine instruction rather than a subroutine call.

### 5.4 Process Synchronization {#ritchie-1974-unix-s5-4 .section tag=0613}

Another process control system call processid = wait( ) causes its caller to suspend execution until one of its children has completed execution. Then wait returns the processid of the terminated process. An error return is taken if the calling process has no descendants. Certain status from the child process is also available. Wait may also present status from a grandchild or more distant ancestor; see §5.5.

### 5.5 Termination {#ritchie-1974-unix-s5-5 .section tag=0614}

Lastly, exit (status) terminates a process, destroys its image, closes its open files, and generally obliterates it. When the parent is notified through the wait primitive, the indicated status is available to the parent; if the parent has already terminated, the status is available to the grandparent, and so on. Processes may also terminate as a result of various illegal actions or user-generated signals (§7 below).
