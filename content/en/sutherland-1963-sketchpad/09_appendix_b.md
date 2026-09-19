---
paper: sutherland-1963-sketchpad
title: 'Sketchpad: A Man-Machine Graphical Communication System'
authors:
  - Ivan E. Sutherland
year: 1963
venue: MIT PhD thesis / AFIPS Spring Joint Computer Conference
field: graphics
section_title: Appendix B
kind: appendix
lang: en
source: https://www.cl.cam.ac.uk/techreports/UCAM-CL-TR-574.pdf
pdf_sha256: e052281b553622badc8dd308003c127617aa5723e4ec3dbfa79b781d8e712742
pdf_pages: 119-126
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 4fdb7d828f5b21b435044489520e14acd42c6a456c19014ae803ee9651e6790f
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

PUSH BUTTON CONTROLS

| BUTTON NAME | BIT NUMBER | FUNCTION |
| --- | --- | --- |
| Draw | 1.8 | Create a new straight line segment or circle arc. End of line or arc left attached to light pen. |
| Circle center | 1.7 | Center of circle is left where pen is pointing. Next thing drawn will be circle arc. |
| Move | 2.1 | Object pointed at moves with light pen. |
| Delete | 1.3 | Object pointed at removed from drawing. |
| Instance | 2.4 | Instance or picture whose number is in toggle register 25 is created. |
| Copy 20 | 3.6 | Four buttons. Copy definition picture indicated in toggle registers 20 to 23 respectively. These buttons can be set up to create equal length lines, dimension lines, etc. Any four functions can be available at once. |
| Copy 21 | 3.1 |  |
| Copy 22 | 2.5 |  |
| Copy 23 | 1.9 |  |
| Stop | 1.6 | Leave moving object wherever it is. Merge moving object if aiming at object of like type. Same as termination flick of the pen. |
| Text | 4.3 | Create line of text consisting only of the letter X. Typing while a piece of text is moving adds to the text displayed. |
| Number | 3.7 | Create a new set of digits and a scalar which is its value. Digits left moving. |
| Hold | 4.9 | Following pen flick not to be taken as termination signal. Used to set pen aside for typing text. |
| Garbage | 1.1 | If pen is tracking, recenter picture so that place pen is pointing at will be in the center. If pen not tracking, compact ring structure by removing garbage. |
| Constraint | 2.8 | Create a new constraint of the type numbered in toggle register 25. Dummy variables are created. Constraint left moving. |
| Horv | 2.9 | Apply horizontal or vertical constraint to line aimed at. Choice is based on 45° cutoff. |

| BUTTON NAME | BIT NUMBER | FUNCTION |
| --- | --- | --- |
| Designate | 2.2 | Designate object. For copying a definition picture with three or more ties. |
| Tie | 2.6 | Object pointed at is an attacher of this picture. |
| Fix | 3.3 | This object must not move during constraint satisfaction. Moving an object with the light pen unfixes it. |
| Unfix | 2.7 | All fixed and designated objects unfixed and undesignated. |
| IBM | 4.3 | Read tape record. Number of record on tape given in toggle 26. Typewriter confirms successful reading or writing. |
| Library | 3.9 | Read a record from the TX-2 library tape. Address of record given in toggle register 27. Typewriter confirms. |
| Library write | Special start point | Write a record on library tape. Typewriter confirms. |
| Change instance | 2.3 | Moving instance or instance pointed at is changed to type indicated in Toggle register 25. Can change resistor into diode, etc. |
| Dismember | 4.4 | Instance pointed at is reduced one level, i.e., its internal structure on the next level becomes usable. |
| Order | 4.6 | Lines are put in better order for plotting. |
| Disorder | 4.5 | Lines are put in worst order for plotting. |
| Punch | 4.7 | Punch plotter tape for object picture. |
| Plot | 4.8 | Plot object picture. |

The following dangerous functions only operate if “meta” button (4.10) is pressed as well.

|  |  |  |
| --- | --- | --- |
| Delete constraints | 1.2 | All constraints in object picture are deleted. |
| Delete points | 1.4 | All unattached points in object picture are deleted. |
| Delete picture | 1.5 | Entire object picture is deleted. |
| IBM | 4.3 | Write IBM tape record. Typewriter confirms. |

| Line | TYPE | (C) | (Specific line block.) |
| --- | --- | --- | --- |
| – | ATATAP | (C) | Put into PATAP of picture if this line is an attacher. |
| – | BWHOS | (C) | Which picture this thing belongs to. |
| – | VORD | (C) | Put into SPECB of Movings if this line is moving. |
| – | LSP | (C) | Start point of line. Goes into PLS ring of point. |
| – | LEP | (C) | End point of line. |
| – |  |  |  |
| Circle | TYPE | (C) | (Specific circle block.) |
| – | ATATAP | (C) |  |
| – | BWHOS | (C) |  |
| – | VORD | (C) |  |
| – | CSP | (C) | Start point of circle arc. |
| – | CEP | (C) | End point of circle arc. |
| – | CIRCEN | (C) | Center point of circle. |
| – | { CVAL } " |  | Angle of circle arc (to avoid ambiguity). Radius of Circle (to save recomputation). |
| Point | TYPE | (C) | (Specific point block.) |
| – | ATATAP | (C) |  |
| – | BWHOS | (C) |  |
| – | VORD | (C) | Put in SPECB of Freedoms during maze-solving constraint satisfaction. |
| – | VFLW | (H) | Constraints which this variable will be used to satisfy. |
| – | VCON | (H) | Constraints on this variable. |
| – | PLS | (H) | Lines and Circles on this point |
| – | IPCOTP | (H) | Instance-point constraints which use this point for reference only. X coordinate of point. Y coordinate of point. |
| – | { PVAL } " |  |  |

| Dummy | TYPE | (C) | (Particular dummy variable.) |
| --- | --- | --- | --- |
| – | ATATAP | (C) |  |
| – | BWHOS | (C) |  |
| – | VORD | (C) |  |
| – | VFLW | (H) |  |
| – | VCON | (H) |  |
| – | { TPVAL } " |  | X coordinate. Y coordinate. |
| Digits | TYPE | (C) | (A particular set of digits. Size of digits is half height of figures.) |
| – | ATATAP | (C) |  |
| – | BWHOS | (C) |  |
| – | VORD | (C) |  |
| – | VFLW | (H) |  |
| – | VCON | (H) |  |
| – | NTOSHOW | (C) | Scalar whose value is to be shown. |
| – | { NVAL } " " " |  | Size times cosine of rotation. Size times sine of rotation. X position. Y position. |
| Scalar | TYPE |  | (A particular scalar block.) |
| – | ATATAP | (C) |  |
| – | BWHOS | (C) |  |
| – | VORD | (C) |  |
| – | VFLW | (H) |  |
| – | VCON | (H) |  |
| – | SSHOW | (H) | Digits showing this scalar’s value. |
| – | { SVAL } . |  | Value of scalar. |

| Constraint | TYPE | (C) | All constraint blocks have same format. If fewer than four variables, block will be shorter and VARIATION will be moved up. |
| --- | --- | --- | --- |
|  | _ |  |  |
|  | ATATAP | (C) |  |
|  | _ |  |  |
|  | BWHOS | (C) |  |
|  | _ |  |  |
|  | CVTS, VORD | (C) | Variable used to satisfy this constraint in maze-solving method. First constrained variable. |
|  | _ |  |  |
|  | VAR1 |  |  |
|  | _ |  |  |
|  | VAR2 |  | Second constrained variable. |
|  | _ |  |  |
|  | VAR3 |  |  |
|  | _ |  |  |
|  | VAR4 |  |  |
|  | _ |  |  |
|  | { VARIATION } _ |  | Code for variations within a constraint type. e.g., horizontal or vertical. |
