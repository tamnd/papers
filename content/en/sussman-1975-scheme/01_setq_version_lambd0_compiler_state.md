---
paper: sussman-1975-scheme
title: 'Scheme: An Interpreter for Extended Lambda Calculus'
authors:
  - Gerald Jay Sussman
  - Guy L. Steele Jr.
year: 1975
venue: MIT AI Memo 349
field: languages
section_title: (setq Version ((lambd0 (compiler-state) (version)) T))
kind: section
lang: en
source: https://dspace.mit.edu/server/api/core/bitstreams/70ab0fe6-0e7a-41ef-99fb-ac2c9481a05e/content
pdf_sha256: c2961e078943a26ae1f752b202290f561578b7ecf8b24b8929e3c1f99e6b2c52
pdf_pages: 31-32
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: a46915544a4f35a16fa73fd1bb0445a90bf9888ee89257f5f53e307541967da6
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The function SCHEME initializes the system driver. The two SETQ's merely set up version numbers. The top level loop itself is written in SCHEME, and is a LABELS which binds the function **TOP** to be a read-eval-print loop. The LISP global variable **TOP** is initialized to the closure of the **TOP** function for convenience and accessibility to user-defined functions.

(DEFUN SCHEME ()
(SETQ VERSION (VERSION) LISPVERSION (STATUS LISPVERSION))
(TERPRI)
(PRINC '|This is SCHEME|)
(PRINC VERSION)
(PRINC '| running in LISP|)
(PRINC LISPVERSION)
(SETQ **ENV** NIL **QUEUE** NIL
**PROCESS** (CREATE!PROCESS '(**TOP** '|SCHEME -- Toplevel|)))
(SWAPINPROCESS)
(ALARMCLOCK 'RUNTIME **QUANTUM**)
(MLOOP))

(SETQ **TOP**
'(BETA (LAMBDA (**MESSAGE**)
(LABELS (((**TOP1**
(LAMBDA (**IGNORE1** **IGNORE2** **IGNORE3**)
(**TOP1** (TERPRI) (PRINC '|=> |)
(PRINT (SET '* (EVALUATE (READ))))))))
(**TOP1** (TERPRI) (PRINC **MESSAGE**) NIL)))))
NIL))

When the LISP alarmclock tick occurs, the global register **TICK** is set to T. **QUANTUM**, the amount of runtime between ticks, is measured in micro-seconds.

(DEFUN SETTICK (X) (SETQ **TICK** T))
