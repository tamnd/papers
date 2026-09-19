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
pdf_pages: 143-144
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 57f7286d7dabb8f480492bab82d241b305a3603eb9182b61056fc32b663b74a6
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Key See hen.

Line A line segment. No representation for an infinite length line exists in Sketchpad.

Line segment A topological thing connecting two points. Contains no numerical information. Sometimes called a line.

List A particular form of storage structure in which each element stores not only the information pertinent to it but also the address of the next element. Not to be confused with a table.

Location A position in the coordinate system represented by a pair of coordinates. Not to be confused with a point which has a location. Also the address of a particular piece of information in storage.

Master A picture which is used to define the visible internal structure of an instance.

Merging Combination of two storage blocks to identify two picture parts, which must be of like type, permanently. The result of a merger of variables takes on the value of the historically older variable. In the ring structure, merging makes one block out of two, reducing the other to garbage. In certain cases merging is recursive.

Moving Changing the numerical information stored in a variable. Moving a point stores a new coordinate location over the previous one. Moving an instance, text, or digits includes size change and rotation. Moving a scalar implies changing its value but does not change the position of its display. Moving is also the state a thing is in when it is attached to the light pen; it may be stationary on the display. Moving is not to be confused with relocating.

N-component element A particular form of storage in which various properties of each object represented are stored in consecutive registers. Also the block of registers representing an object.

Numbers See scalars and digits. Number often refers to digits and scalars collectively. Also the binary numbers stored for a variable.

Object picture A particular picture currently being worked on. Especially a complicated picture of particular interest to a user as opposed to a definition or master picture which is to be used as a portion of the object picture.

Older The older of two blocks is the one with the lowest numbered address, illustrated higher on the page. Since new blocks are taken from the free space in addresses higher numbered than the drawing storage, an older block was usually created sooner.

Picture A storage device to collect together related drawing parts. A “sheet of paper”. Also the lines, points, instances, and constraints, etc., that are drawn in the picture, collectively. Pictures are numbered so that any one may be called to appear on the display. Within the limits of storage, as many pictures as desired may be set up and used.

Point  A specific representation in the *ring structure* used as an end point for a *line segment*. Not to be confused with *location* or *spot*. Also as a verb, to aim at something with the light pen.

Pointer  A storage register which contains the location of another storage register rather than numerical data. Such a register is said to point to the register whose address it contains.

Pseudo pen location  A *location* near the axis of the light pen which is used as the “point of the pencil”. The pseudo pen location lies exactly on an existing *point* or *line* or *circle* or at the intersection of *lines* if the pen is *aimed* at them.

Relocating  Changing the address at which a particular *block* is stored in memory. Not to be confused with *moving*.

Result  The single thing which remains after two things have been *merged*.

Ring  A set of *pointers* which closes on itself. In Sketchpad all rings point both forward and back. A ring is composed of one *hen* and many *chickens*.

Ring structure  The type of storage structure used to represent the drawing’s topology. See *ring*.

Satisfy  See *constraint satisfaction*.

Scalar  A one component vector whose value can be displayed by a set of *digits*. For display of the scalar itself a # is used.

Spot  One of the bright dots on the display. Not to be confused with *point* or *location*.

Table  A form of storage structure in which successive pieces of information are stored in successive registers in memory. Tables are the “conventional” form of storage. See also *list* and *ring structure*.

Termination  The process of taking things out of the *moving* state. Termination is usually done by giving a flick of the light pen. Pressing “stop” also terminates. Upon termination, *merging* may take place.

Texts  Lines of textual material typed in and appearing in a standard type style on the picture. Text is treated as a four component *variable*.

Tie  An *attacher*.

Value  The particular information stored in the numerical portion of a *variable*. E.g., the *location* of a *point*. Especially the value of a *scalar* as opposed to the *location* of the set of *digits* displaying this value.
