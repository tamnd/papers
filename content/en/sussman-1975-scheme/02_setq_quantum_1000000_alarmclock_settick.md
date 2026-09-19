---
paper: sussman-1975-scheme
title: 'Scheme: An Interpreter for Extended Lambda Calculus'
authors:
  - Gerald Jay Sussman
  - Guy L. Steele Jr.
year: 1975
venue: MIT AI Memo 349
field: languages
section_title: (setq **quantum** 1000000. Alarmclock 'settick)
kind: section
lang: en
source: https://dspace.mit.edu/server/api/core/bitstreams/70ab0fe6-0e7a-41ef-99fb-ac2c9481a05e/content
pdf_sha256: c2961e078943a26ae1f752b202290f561578b7ecf8b24b8929e3c1f99e6b2c52
pdf_pages: 32-33
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: a0245435e2aa03bbc159249cfe22f07477b67771f2be649b0efa2ffdcfb581ed
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

MLOOP is the main loop of the interpreter. It may be thought of as the instruction dispatch in the micro-code of the implementation machine. If an alarmclock tick has occurred, and interrupts are allowed, then the scheduler is called to switch processes. Otherwise the "instruction" specified by **PC** is executed via FASTCALL.

(DEFUN MLOOP ()
  (DO (((**TICK** NIL)) (NIL) ;DO forever
       (AND **TICK** (ALLOW) (SCHEDULE)))
    (FASTCALL **PC**)))

FASTCALL is essentially a FUNCALL optimized for compiled "microcode". Note the way it pulls the SUBR property to the front of the property list if possible for speed.

(DEFUN FASTCALL (ATSYM)
  (COND ((EQ (CAR (CDR ATSYM)) 'SUBR)
         (SUBRCALL NIL (CADR (CDR ATSYM))))
        (T ((LAMBDA (SUBR)
             (COND (SUBR (REMPROP ATSYM 'SUBR)
                       (PUTPROP ATSYM SUBR 'SUBR)
                       (SUBRCALL NIL SUBR))
                   (T (FUNCALL ATSYM)))))
           (GET ATSYM 'SUBR))))))

Interruptions are allowed unless the variable *ALLOW* is bound to NIL in the current environment. This is used to implement the EVALUATE!UNINTERRUPTIBLY primitive.

(DEFUN ALLOW ()
  ((LAMBDA (VCELL)
     (COND (VCELL (CADR VCELL))
           (T T)))
   (ASSQ '*ALLOW* **ENV**)))

Next comes the scheduler. It is apparently interrupt-driven, but in fact is not. The key here is to think microcode! There is one place in the microcoded instruction interpretation loop which checks to see if there is an interrupt pending; in our "machine", this occurs in MLOOP, where **TICK** is checked on every cycle. This is another case where we must beware of using too much of the power of the host language; just as we must avoid using host recursion directly to implement recursion, so we must avoid using host interrupts directly to implement interrupts. We may not modify any register during a host language interrupt, except one (such as **TICK**) which is specifically intended to signal interrupts. Thus, if we were to add an interrupt character facility to SCHEME similar to that in MacLISP [Moon], the MacLISP interrupt character function would merely set a register like **TICK** and dismiss; MLOOP would eventually notice that this register had changed and dispatch to the interrupt handler. All this implies that the "microcode" for the interrupt handlers does not itself contain critical code that must be protected from host language interrupts.

When the scheduler is invoked, if there is another process waiting on the process queue, then the current process is swapped out and put on the end of the queue, and a new process swapped in from the front of the queue. The process stored on the queue consists of an atom which has the current frame and **VAL** register on its property list. Note that the **TEM** register is not saved, and so cannot be used to pass information between instructions.

(DEFUN SCHEDULE ()
    (COND (**QUEUE**
        (SWAPOUTPROCESS)
        (NCONC **QUEUE** (LIST **PROCESS**))
        (SETQ **PROCESS** (CAR **QUEUE**)
            **QUEUE** (CDR **QUEUE**))
        (SWAPINPROCESS)))
    (SETQ **TICK** NIL)
    (ALARMCLOCK 'RUNTIME **QUANTUM**))

(DEFUN SWAPOUTPROCESS ()
    ((LAMBDA (**CLINK**)
        (PUTPROP **PROCESS** (SAVEUP **PC**) 'CLINK)
        (PUTPROP **PROCESS** **VAL** 'VAL))
     **CLINK**))

(DEFUN SWAPINPROCESS ()
    (SETQ **CLINK** (GET **PROCESS** 'CLINK)
        **VAL** (GET **PROCESS** 'VAL))
    (RESTORE))

Primitive operators are LISP functions, i.e. SUBRs, EXPRs, and LSUBRs.
