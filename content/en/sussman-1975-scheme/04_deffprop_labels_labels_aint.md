---
paper: sussman-1975-scheme
title: 'Scheme: An Interpreter for Extended Lambda Calculus'
authors:
  - Gerald Jay Sussman
  - Guy L. Steele Jr.
year: 1975
venue: MIT AI Memo 349
field: languages
section_title: (deffprop Labels Labels Aint)
kind: section
lang: en
source: https://dspace.mit.edu/server/api/core/bitstreams/70ab0fe6-0e7a-41ef-99fb-ac2c9481a05e/content
pdf_sha256: c2961e078943a26ae1f752b202290f561578b7ecf8b24b8929e3c1f99e6b2c52
pdf_pages: 38-40
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 016a6970a4f71bd046a921a53a2195afc9af46295633ee6b7f5a8cac6d3bcd9d
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

(DEFUN LABELS ()
    (SETQ **TEM** (MAPCAR '(LAMBDA (DEF)
        (LIST (CAR DEF)
            (LIST 'BETA (CADR DEF) NIL))))
        (CADR **EXP**)))
    (MAPC '(LAMBDA (VC) (RPLACA (CODADR VC) **TEM**)) **TEM**)
    (SETQ **ENV** (NCONC **TEM** **ENV**)
        **EXP** (CADOR **EXP**)
        **PC** 'AEVAL))

We now come to the multiprocess primitives.
CREATE!PROCESS temporarily creates a new set of machine registers (by the lambda-binding mechanism of the host language), establishes the new process in those registers, swaps it out, and returns the new process id; returning causes the old machine registers to be restored.

(DEFUN CREATE!PROCESS (EXP)
    ((LAMBDA (**PROCESS** **EXP** **ENV** **UNEVLIS** **EVLIS** **PC** **CLINK** **VAL**)
        (SWAPOUTPROCESS)
        **PROCESS**)
        (GENSYM)
        EXP
        **ENV**
        NIL
        NIL
        'AEVAL
        (LIST NIL NIL NIL NIL 'TERMINATE NIL)
        NIL))

(DEFUN START!PROCESS (P)
    (COND ((OR (NOT (ATOM P)) (NOT (GET P 'CLINK)))
        (ERROR '|BAD PROCESS -- START!PROCESS| **EXP** 'FAIL-ACT))
        (OR (EQ P **PROCESS**) (MEMQ P **QUEUE**)
            (SETQ **QUEUE** (NCONC **QUEUE** (LIST P)))))
    P)

(DEFUN STOP!PROCESS (P)
    (COND ((MEMQ P **QUEUE**)
        (SETQ **QUEUE** (DELQ P **QUEUE**)))
        ((EQ P **PROCESS**) (TERMINATE))))
    P)

TERMINATE is an internal microcode routine which terminates the current process. If the current process is the only one, then all processes have been stopped, and so a new SCHEME top level is created; otherwise TERMINATE pulls the next process off the scheduler queue and swaps it in. Note that we cannot use SWAPINPROCESS because a RESTORE will happen in EVLIS as soon as TERMINATE completes (this is a very deep global property of the interpreter, and a fine source of bugs; much care is required).

(DEFUN TERMINATE ()
(COND ((NULL **QUEUE**)
      (SETQ **PROCESS**
            (CREATE!PROCESS '(**TOP** |SCHEME -- QUEUEOUT|))))
      (T (SETQ **PROCESS** (CAR **QUEUE**)
           **QUEUE** (CDR **QUEUE**))))
      (SETQ **CLINK** (GET **PROCESS** 'CLINK))
      (SETQ **VAL** (GET **PROCESS** 'VAL))
      'TERMINATE-VALUE)

EVALUATE!UNINTERRUPTIBLY merely binds the variable *ALLOW* to NIL, and then evaluates its argument. This is why this primitive follows the scoping rules for variables!

(DEFFPROP EVALUATE!UNINTERRUPTIBLY EVALUATE!UNINTERRUPTIBLY AINT)

(DEFUN EVALUATE!UNINTERRUPTIBLY ()
      (SETQ **ENV** (CONS (LIST '*ALLOW* NIL) **ENV**)
            **EXP** (CADR **EXP**)
            **PC** 'REVAL))

DEFINE closes the function to be defined in the null environment, and installs the closure in the LISP value cell.

(DEFFPROP DEFINE DEFINE AINT)

(DEFUN DEFINE ()
      (SET (CADR **EXP**) (LIST 'BETA (CADOR **EXP**) NIL))
      (SETQ **VAL** (CADR **EXP**))
      (RESTORE))

ASET looks up the specified variable in the current environment, and clobbers the value cell in the environment with the new value. If the variable is not bound in the current environment, the LISP value cell is set. Note that ASET does not need to be an AINT, since it does not fool with order of evaluation; all it needs is access to the "machine register" **ENV**.

(DEFUN ASET (VAR VALU)
      (SETQ **TEM** (ASSQ VAR **ENV**))
      (COND (**TEM** (RPLACA (CDR **TEM**) VALU))
            (T (SET VAR VALU))))

CATCH binds the tag variable to a DELTA expression which contains the current CLINK. When AEVAL applies such an expression as a function (of one argument), it makes the **CLINK** in the DELTA expression be the **CLINK**, places the value of the argument in **VAL**, and does a RESTORE. The effect is to return from the CATCH expression with the argument to the DELTA expression as its value (can you see why?).

(DEFFPROP CATCH ACATCH AINT)

(DEFUN ACATCH ()
    (SETQ **ENV** (CONS (LIST (CAOR **EXP**) (LIST 'DELTA **CLINK**)) **ENV**)
          **EXP** (CADDR **EXP**)
          **PC** 'REVAL))

PAIRLIS is as in the LISP 1.5 Programmer's Manual [McCarthy].

(DEFUN PAIRLIS (X Y Z)
    (DO ((I X (CDR I))
         (J Y (CDR J))
         (L Z (CONS (LIST (CAR I) (CAR J)) L)))
        ((AND (NULL I) (NULL J)) L)
        (AND (OR (NULL I) (NULL J))
             (ERROR 'WRONG NUMBER OF ARGUMENTS - PAIRLIS|
                    **EXP**
                    'WRNG-N0-ARCS))))

AMACROS are fairly complicated beasties, and have very little to do with the basic issues of the implementation of SCHEME per se, so the code for them will not be given here. AMACROS behave almost exactly like MacLISP macros [Moon].

This is the end of the SCHEME interpreter!
