---
paper: sutherland-1963-sketchpad
title: 'Sketchpad: A Man-Machine Graphical Communication System'
authors:
  - Ivan E. Sutherland
year: 1963
venue: MIT PhD thesis / AFIPS Spring Joint Computer Conference
field: graphics
section_title: Acronyms
kind: appendix
lang: en
source: https://www.cl.cam.ac.uk/techreports/UCAM-CL-TR-574.pdf
pdf_sha256: e052281b553622badc8dd308003c127617aa5723e4ec3dbfa79b781d8e712742
pdf_pages: 141-142
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: aebc9c6ec6fc381bc16e9e62f60b1dab782d2c05294bdb38ccdfda0da90ed2c8
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

4-thing  A four component variable: text, digits, or instance.

Aim  To place the light pen so that light from the picture part aimed at falls on the photocell and so that the center of the light pen field of view is sufficiently close to the picture part.

Atomic  Axiomatic, fundamental, built in. The atomic constraints are listed in Appendix A. The atomic operations are each controlled by a push button listed in Appendix B.

Attacher  For instances, a particular point designated in the master for which in the instance the light pen will have a particular affinity. Also the related point created in the picture containing the instance when the instance was created.

For copying, any drawing part designated in the definition picture. Attachers may be recursively merged with object picture parts when the definition is copied.

Balance  The property of equal weight among constraints obtained by making error in a constraint equal to displacement.

Block  A set of consecutive registers used to represent a picture part. An n-component element.

Chicken  A subordinate ring member, composed of two registers one of which references the block containing the hen for this ring, the other references the next and previous chickens in the ring.

Circle  A circle arc. A full circle is a circle arc 360° or more in length.

Constraint  A specific storage representation of a relationship between variables which limits the freedom of the variables, i.e., reduces the number of degrees of freedom of the system. Also, constraint is sometimes used to mean a type of constraint, as in “there are seventeen atomic constraints.”

Constraint satisfaction  The process of moving variables so that all the conditions on them embodied in the constraints are met. It is not always possible.

Copying Duplication in storage the ring structure of a definition picture. A copy is not to be confused with an instance. Any instance may be changed into a copy by dismembering.

Definition A master picture. Especially a picture to be used for copying, usually containing a combination of atomic constraints. Also the error computation routine associated with a constraint.

Delete To erase. Deleted blocks become garbage.

Digits A set of five decimal digits plus sign, leading zeros suppressed. As a variable digits may be moved, rotated, or made larger on the display. The particular value displayed is that of an associated scalar and may be changed only by moving the scalar.

Dismembering The process of changing an instance into a copy by creating in the ring structure a duplicate of the internal structure of the instance’s master and removing the instance. A dismembered instance becomes a group of lines, etc., which may be individually moved, deleted, etc. Dismembering peels off only one layer of instance at a time.

Dummy variable A particular two component variable used to locate the arms of a constraint when it is first created. Dummy variables may merge with any other kind of variable leaving any attached constraints applying to that variable. Display for a dummy variable is a ×.

Error The number computed by the definition subroutine for a constraint. Error is zero if the constraint is satisfied and grows monotonically as the constrained variables are moved.

File A storage structure. A file may be in either list form or table form. Also a collection of magnetic tape records.

Free A variable which has so few constraints on it that it may be moved to satisfy all of them. Such a variable will be in the FREEDOMS ring.

Garbage Free storage inside the range of storage addresses being used to represent the drawing.

Hen A pair of registers in a block used to indicate the first and last references made to that block by the chickens belonging in the hen’s ring. Also called a key.

Instance A fixed geometry subpicture represented very compactly in storage by reference to a master and indication by four numbers of the size, rotation, and location of the subpicture. Internal structure of an instance is visible and may contain other instances, but since it is identical in appearance to the master it cannot be changed without changing the master. Except for size, rotation, and location, all instances of one master look the same.
