---
paper: ritchie-1974-unix
title: The UNIX Time-Sharing System
authors:
  - Dennis M. Ritchie
  - Ken Thompson
year: 1974
venue: Communications of the ACM
field: systems
section: "6"
section_title: The Shell
tag: "0615"
kind: section
lang: en
source: https://dsf.berkeley.edu/cs262/unix.pdf
pdf_sha256: 96bc5caa11cc13925165b6d36b78c55cc61a61e65a628c375511683a97442b51
pdf_pages: 7-9
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 48ba11254d78985a37ab5fd80a7139fabc9249fb9e9d11df7cc364647213c2d0
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

For most users, communication with UNIX is carried on with the aid of a program called the Shell. The Shell is a command line interpreter: it reads lines typed by the user and interprets them as requests to execute other programs. In simplest form, a command line consists of the command name followed by arguments to the command, all separated by spaces:

command arg₁ arg₂ ... argₙ

The Shell splits up the command name and the arguments into separate strings. Then a file with name command is sought; command may be a path name including the “/” character to specify any file in the system. If command is found, it is brought into core and executed. The arguments collected by the Shell are accessible to the command. When the command is finished, the Shell resumes its own execution, and indicates its readiness to accept another command by typing a prompt character.

If file command cannot be found, the Shell prefixes the string /bin/ to command and attempts again to find the file. Directory /bin contains all the commands intended to be generally used.

### 6.1 Standard I/O {#ritchie-1974-unix-s6-1 .section tag=0616}

The discussion of I/O in §3 above seems to imply that every file used by a program must be opened or created by the program in order to get a file descriptor for the file. Programs executed by the Shell, however, start off with two open files which have file descriptors 0 and 1. As such a program begins execution, file 1 is open for writing, and is best understood as the standard output file. Except under circumstances indicated below, this file is the user’s typewriter. Thus programs which wish to write informative or diagnostic information ordinarily use file descriptor 1. Conversely, file 0 starts off open for reading, and programs which wish to read messages typed by the user usually read this file.

The Shell is able to change the standard assignments of these file descriptors from the user’s typewriter printer and keyboard. If one of the arguments ‘to a command is prefixed by “>”, file descriptor 1 will, for the duration of the command, refer to the file named after the “>”. For example, ls ordinarily lists, on the typewriter, the names of the files in the current directory. The command ls >there creates a file called there and places the listing there. Thus the argument “>there” means, “place output on there.” On the other hand, ed ordinarily enters the editor, which takes requests from the user via his typewriter. The command ed <script interprets script as a file of editor commands; thus “<script” means, “take input from script.”

Although the file name following “<” or “>” appears to be an argument to the command, in fact it is interpreted completely by the Shell and is not passed to the command at all. Thus no special coding to handle I/O redirection is needed within each command; the command need merely use the standard file descriptors 0 and 1 where appropriate.

### 6.2 Filters {#ritchie-1974-unix-s6-2 .section tag=0617}

An extension of the standard I/O notion is used to direct output from one command to the input of another. A sequence of commands separated by vertical bars causes the Shell to execute all the commands simultaneously and to arrange that the standard output of each command be delivered to the standard input of the next command in the sequence. Thus in the command line ls | pr –2 | opr ls lists the names of the files in the current directory; its output is passed to pr, which paginates its input with dated headings. The argument “–2” means double column. Likewise the output from pr is input to opr. This command spools its input onto a file for off-line printing.

This process could have been carried out more clumsily by ls >temp1
pr –2 <temp1 >temp2
opr <temp2 followed by removal of the temporary files. In the absence of the ability to redirect output and input, a still clumsier method would have been to require the ls command to accept user requests to paginate its output, to print in multi-column format, and to arrange that its output be delivered off-line. Actually it would be surprising, and in fact unwise for efficiency reasons, to expect authors of commands such as ls to provide such a wide variety of output options.

A program such as pr which copies its standard input to its standard output (with processing) is called a filter. Some filters which we have found useful perform character transliteration, sorting of the input, and encryption and decryption.

### 6.3 Command Separators: Multitasking {#ritchie-1974-unix-s6-3 .section tag=0618}

Another feature provided by the Shell is relatively straightforward. Commands need not be on different lines; instead they may be separated by semicolons.

ls; ed will first list the contents of the current directory, then enter the editor.

A related feature is more interesting. If a command is followed by “&”, the Shell will not wait for the command to finish before prompting again; instead, it is ready immediately to accept a new command. For example, as source >output & causes source to be assembled, with diagnostic output going to output; no matter how long the assembly takes, the Shell returns immediately. When the Shell does not wait for the completion of a command, the identification of the process running that command is printed. This identification may be used to wait for the completion of the command or to terminate it. The “&” may be used several times in a line:

as source >output & ls >files & does both the assembly and the listing in the background. In the examples above using “&”, an output file other than the typewriter was provided; if this had not been done, the outputs of the various commands would have been intermingled.

The Shell also allows parentheses in the above operations. For example,

(date; ls) >x & prints the current date and time followed by a list of the current directory onto the file x. The Shell also returns immediately for another request.

### 6.4 The Shell as a Command: Command files {#ritchie-1974-unix-s6-4 .section tag=0619}

The Shell is itself a command, and may be called recursively. Suppose file tryout contains the lines as source
mv a.out testprog
testprog

The mv command causes the file a.out to be renamed testprog. a.out is the (binary) output of the assembler, ready to be executed. Thus if the three lines above were typed on the console, source would be assembled, the resulting program named testprog, and testprog executed. When the lines are in tryout, the command sh <tryout would cause the Shell sh to execute the commands sequentially.

The Shell has further capabilities, including the ability to substitute parameters and to construct argument lists from a specified subset of the file names in a directory. It is also possible to execute commands conditionally on character string comparisons or on existence of given files and to perform transfers of control within filed command sequences.

### 6.5 Implementation of the Shell {#ritchie-1974-unix-s6-5 .section tag=061A}

The outline of the operation of the Shell can now be understood. Most of tile time, the Shell is waiting for the user to type a command. When the new-line character ending the line is typed, the Shell’s read call returns. The Shell analyzes the command line, putting the arguments in a form appropriate for execute. Then fork is called. The child process, whose code of course is still that of the Shell, attempts to perform an execute with the appropriate arguments. If successful, this will bring in and start execution of the program whose name was given. Meanwhile, the other process resulting from the fork, which is the parent process, waits for the child process to die. When this happens, the Shell knows the command is finished, so it types its prompt and reads the typewriter to obtain another command.

Given this framework, the implementation of background processes is trivial; whenever a command line contains “&”, the Shell merely refrains from waiting for the process which it created to execute the command.

Happily, all of this mechanism meshes very nicely with the notion of standard input and output files. When a process is created by the fork primitive, it inherits not only the core image of its parent but also all the files currently open in its parent, including those with file descriptors 0 and 1. The Shell, of course, uses these files to read command lines and to write its prompts and diagnostics, and in the ordinary case its children—the command programs—inherit them automatically. When an argument with “<” or “>” is given however, the offspring process, just before it performs execute, makes the standard I/O file descriptor 0 or 1 respectively refer to the named file. This is easy because, by agreement, the smallest unused file descriptor is assigned when a new file is opened (or created); it is only necessary to close file 0 (or 1) and open the named file. Because the process in which the command program runs simply terminates when it is through, the association between a file specified after “<” or “>” and file descriptor 0 or 1 is ended automatically when the process dies. Therefore the Shell need not know the actual names of the files which are its own standard input and output since it need never reopen them.

Filters are straightforward extensions of standard I/O redirection with pipes used instead of files.

In ordinary circumstances, the main loop of the Shell never terminates. (The main loop includes that branch of the return from fork belonging to the parent process; that is, the branch which does a wait, then reads another command line.) The one thing which causes the Shell to terminate is discovering an end-of-file condition on its input file. Thus, when the Shell is executed as a command with a given input file, as in sh <comfile the commands in comfile will be executed until the end of comfile is reached; then the instance of the Shell invoked by sh will terminate. Since this Shell process is the child of another instance of the Shell, the wait executed in the latter will return, and another command may be processed.

### 6.6 Initialization {#ritchie-1974-unix-s6-6 .section tag=061B}

The instances of the Shell to which users type commands are themselves children of another process. The last step in the initialization of UNIX is the creation of a single process and the invocation (via execute) of a program called init. The role of init is to create one process for each typewriter channel which may be dialed up by a user. The various subinstances of init open the appropriate typewriters for input and output. Since when init was invoked there were no files open, in each process the typewriter keyboard will receive file descriptor 0 and the printer file descriptor 1. Each process types out a message requesting that the user log in and waits, reading the typewriter, for a reply. At the outset, no one is logged in, so each process simply hangs. Finally someone types his name or other identification. The appropriate instance of init wakes up, receives the log-in line, and reads a password file. If the user name is found, and if he is able to supply the correct password, init changes to the user’s default current directory, sets the process’s user ID to that of the person logging in, and performs an execute of the Shell. At this point the Shell is ready to receive commands and the logging-in protocol is complete.

Meanwhile, the mainstream path of init (the parent of all the subinstances of itself which will later become Shells) does a wait. If one of the child processes terminates, either because a Shell found an end of file or because a user typed an incorrect name or password, this path of init simply recreates the defunct process, which in turn reopens the appropriate input and output files and types another login message. Thus a user may log out simply by typing the end-of-file sequence in place of a command to the Shell.

### 6.7 Other Programs as Shell {#ritchie-1974-unix-s6-7 .section tag=061C}

The Shell as described above is designed to allow users full access to the facilities of the system since it will invoke the execution of any program with appropriate protection mode. Sometimes, however, a different interface to the system is desirable, and this feature is easily arranged.

Recall that after a user has successfully logged in by supplying his name and password, init ordinarily invokes the Shell to interpret command lines. The user’s entry in tile password file may contain the name of a program to be invoked after login instead of the Shell. This program is free to interpret the user’s messages in any way it wishes.

For example, the password file entries for users of a secretarial editing system specify that the editor ed is to be used instead of the Shell. Thus when editing system users log in, they are inside the editor and can begin work immediately; also, they can be prevented from invoking UNIX programs not intended for their use. In practice, it has proved desirable to allow a temporary escape from the editor to execute the formatting program and other utilities.

Several of the games (e.g. chess, blackjack, 3D tic-tac-toe) available on UNIX illustrate a much more severely restricted environment. For each of these an entry exists in the password file specifying that the appropriate game-playing program is to be invoked instead of the Shell. People who log in as a player of one of the games find themselves limited to the game and unable to investigate the presumably more interesting offerings of UNIX as a whole.
