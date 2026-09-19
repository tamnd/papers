---
paper: sussman-1975-scheme
title: 'Scheme: An Interpreter for Extended Lambda Calculus'
authors:
  - Gerald Jay Sussman
  - Guy L. Steele Jr.
year: 1975
venue: MIT AI Memo 349
field: languages
section_title: (defun Primop (x) (getl X '(subr Expr Lsubr)))
kind: section
lang: en
source: https://dspace.mit.edu/server/api/core/bitstreams/70ab0fe6-0e7a-41ef-99fb-ac2c9481a05e/content
pdf_sha256: c2961e078943a26ae1f752b202290f561578b7ecf8b24b8929e3c1f99e6b2c52
pdf_pages: 33-37
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 3a12275e6319732cf4ffe8c83d2073a47e0af552ce895bf87733b535ac72cd3b
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

SAVEUP conses a new frame onto the **CLINK** structure. It saves the values of all important registers. It takes one argument, RETAG, which is the instruction to return to when the computation is restored.

(DEFUN SAVEUP (RETAG)
    (SETQ **CLINK** (LIST **EXP** **UNEVLIS** **ENV** **EVLIS** RETAG **CLINK**)))

RESTORE restores a computation from the CLINK. The use of TEMP is a kludge to optimize the compilation of the "microcode".

(DEFUN RESTORE ()
(PROG (TEMP)
    (SETQ TEMP (OR **CLINK**
        (ERROR '|PROCESS RAN OUT - RESTORE|
            **EXP**
            'FAIL-ACT))
    **EXP** (CAR TEMP)
    TEMP (CDR TEMP)
    **UNEVLIS** (CAR TEMP)
    TEMP (CDR TEMP)
    **ENV** (CAR TEMP)
    TEMP (CDR TEMP)
    **EVLIS** (CAR TEMP)
    TEMP (CDR TEMP)
    **PC** (CAR TEMP)
    TEMP (CDR TEMP)
    **CLINK** (CAR TEMP)))))

This is the central function of the SCHEME interpreter. This "instruction" expects **EXP** to contain an expression to evaluate, and **ENV** to contain the environment for the evaluation. The fact that we have arrived here indicates that **PC** contains 'AEVAL, and so we need not change **PC** if the next instruction is also to be AEVAL. Besides the obvious objects likes numbers, identifiers, LAMBDA expressions, and BETA expressions (closures), there are also several other objects of interest. There are primitive operators (LISP functions); AINTs (which are to SCHEME as FSUBRs like COND are to LISP); and AMACROs, which are used to implement DO, AND, OR, COND, BLOCK, etc.

(DEFUN AEVAL ()
(COND ((ATOM **EXP**)
      (COND ((NUMBERP **EXP**)
            (SETQ **VAL** **EXP**)
            (RESTORE))
            ((PRIMOP **EXP**)
             (SETQ **VAL** **EXP**)
             (RESTORE))
            ((SETQ **TEM** (ASSQ **EXP** **ENV**))
             (SETQ **VAL** (CADR **TEM**))
             (RESTORE))
            (T (SETQ **VAL** (SYMEVAL **EXP**))
               (RESTORE))))
      ((ATOM (CAR **EXP**))
       (COND ((SETQ **TEM** (GET (CAR **EXP**) 'AINT))
              (SETQ **PC** **TEM**))
             ((EQ (CAR **EXP**) 'LAMBDA)
              (SETQ **VAL** (LIST 'BETA **EXP** **ENV**))
              (RESTORE))
             ((SETQ **TEM** (GET (CAR **EXP**) 'AMACRO))
              (SETQ **EXP** (FUNCALL **TEM** **EXP**)))
             (T (SETQ **EVLIS** NIL
                        **UNEVLIS** **EXP**
                        **PC** 'EVLIS))))
       ((EQ (CAAR **EXP**) 'LAMBDA)
        (SETQ **EVLIS** (LIST (CAR **EXP**))
              **UNEVLIS** (COR **EXP**)
              **PC** 'EVLIS))
        (T (SETQ **EVLIS** NIL
                   **UNEVLIS** **EXP**
                   **PC** 'EVLIS))))

We come to EVLIS when a combination is encountered. The intention is to evaluate each component of the combination and then apply the resulting function to the resulting arguments. We use the register **UNEVLIS** to hold the list of components yet to be evaluated, and the register **EVLIS** to hold the list of evaluated components. We assume that these have been set up by AEVAL. Note that in the case of an explicit LAMBDA expression in the CAR of a combination **UNEVLIS** is initialized to be the list of unevaluated arguments and **EVLIS** is initialized to be the list containing the lambda expression.

EVLIS checks to see if there remain any more components yet to be evaluated. If not, it applies the function. Note that the primitive operators are applied using the LISP function APPLY. Note also how a BETA expression controls the environment in which its body is to be evaluated. DELTA expressions are CATCH tags (see CATCH). It is interesting that the evaluated components are collected in the reverse order from that which we need them in, and so we must reverse the list before applying the function. Do you see why we must not use side effects (e.g. the NREVERSE function) to reverse the list? Think about CATCH!

If there remain components yet to be evaluated, EVLIS saves up a frame, so that execution can be resumed at EVLIS1 when the evaluation of the component returns with a value. It then sets up **EXP** to point to the component to be evaluated and dispatches to AEVAL.

(DEFUN EVLIS ()
    (COND ((NULL **UNEVLIS**)
        (SETQ **EVLIS** (REVERSE **EVLIS**))
        (COND ((ATOM (CAR **EVLIS**))
            (SETQ **VAL** (APPLY (CAR **EVLIS**) (CDR **EVLIS**)))
            (RESTORE))
            ((EQ (CAAR **EVLIS**) 'LAMBOA)
                (SETQ **ENV** (PAIRLIS (CADAR **EVLIS**) (CDR **EVLIS**) **ENV**)
                    **EXP** (CADDAR **EVLIS**)
                    **PC** 'AEVAL))
            ((EQ (CAAR **EVLIS**) 'BETA)
                (SETQ **ENV** (PAIRLIS (CADR (CADAR **EVLIS**))
                    (COR **EVLIS**)
                    (CADDAR **EVLIS**))
                    **EXP** (CADOR (CADAR **EVLIS**))
                    **PC** 'AEVAL))
            ((EQ (CAAR **EVLIS**) 'DELTA)
                (SETQ **CLINK** (CADAR **EVLIS**))
                (RESTORE))
                (T (ERROR '|BAD FUNCTION - EVARGLIST| **EXP** 'FAIL-ACT))))
        (T (SAVEUP 'EVLIS1)
            (SETQ **EXP** (CAR **UNEVLIS**)
                **PC** 'AEVAL))))

The purpose of EVLIS1 is to gobble up the value, passed in the **VAL** register, of the subexpression just evaluated. It saves this value on the list in the **EVLIS** register, pops off the unevaluated subexpression from the **UNEVLIS** register, and dispatches back to EVLIS.

(DEFUN EVLIS1 ()
    (SETQ **EVLIS** (CONS **VAL** **EVLIS**)
        **UNEVLIS** (CDR **UNEVLIS**)
        **PC** 'EVLIS))

Here is the code for the various AINTs. On arrival at the instruction for an AINT, **EXP** contains the expression whose functional position contains the name of the AINT. None of the arguments have been evaluated, and no new control frame has been created. Note that each AINT is defined by the presence of an AINT property on the property list of the LISP atom which is its name. The value of this property is the LISP function which is the first "instruction" of the AINT.

EVALUATE is similar to the LISP function EVAL; it evaluates its argument, which should result in a s-expression, which is then fed back into the SCHEME expression evaluator (AEVAL).

(DEFPROP EVALUATE EVALUATE AINT)

(DEFUN EVALUATE ()
    (SAVEUP 'EVALUATE1)
    (SETQ **EXP** (CADR **EXP**)
          **PC** 'REVAL))

(DEFUN EVALUATE1 ()
    (SETQ **EXP** **VAL**
          **PC** 'REVAL))

IF evaluates its first argument, with a return address of IF1. IF1 examines the resulting **VAL**, and gives either the second or third argument to AEVAL depending on whether the **VAL** was non-NIL or NIL.

(DEFPROP IF IF AINT)

(DEFUN IF ()
    (SAVEUP 'IF1)
    (SETQ **EXP** (CADR **EXP**)
          **PC** 'AEVAL))

(DEFUN IF1 ()
    (COND (**VAL** (SETQ **EXP** (CADDDR **EXP**)))
          (T (SETQ **EXP** (CADDDR **EXP**))))
    (SETQ **PC** 'AEVAL))

As it was in the beginning, is now, and ever shall be: QUOTE without end. (Amen, amen.)

(DEFPROP QUOTE AQUOTE AINT)

(DEFUN AQUOTE ()
    (SETQ **VAL** (CADR **EXP**))
    (RESTORE))

LABELS merely feeds its second argument to AEVAL after constructing a fiendishly clever environment structure. This is done in two stages: first the skeleton of the structure is created, with null environments in the closures of the bound functions; next the created environment is clobbered into each of the closures.
