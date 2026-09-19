---
paper: deutsch-1984-smalltalk
title: Efficient Implementation of the Smalltalk-80 System
authors:
  - L. Peter Deutsch
  - Allan M. Schiffman
year: 1984
venue: POPL
field: languages
section_title: Special Difficulties
kind: section
lang: en
source: https://doi.org/10.1145/800017.800542
pdf_sha256: 300584e302ee0fa5a006ee363d9e3f1b0df043c3259580e32dcd409e9a09871d
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 7826523b9be094f1bf8a3b61edea1f6efd2c9b6387f84fa5aeb816f3196ad795
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The standard Smalltalk-80 system implementation is based on an ideal virtual machine or v-machine. The compiler generates code for this machine, and the implementor's documentation describes the system as an interpreter for the v-machine instruction set, similar to the Pascal P-system [Ammann 75] [Ammann 77]. One unusual feature of the Smalltalk-80 v-machine is that it makes runtime state such as procedure activations visible to the programmer as data objects. This is similar to the "spaghetti stack" model of Interlisp [XSIS 83], but more straightforward: Interlisp uses a programmer-visible indirection mechanism to reference procedure activations, whereas the Smalltalk-80 programmer treats procedure activations just like any other data objects.

The Smalltalk-80 language approaches programming with generic data types through message-passing and dynamic typing. To invoke a procedure (method in Smalltalk-80 terminology), a message is sent to a data object (the receiver), which selects the method to be executed. This means that a method address must be found at runtime. At a given lexical point in the code, only the message name (selector) is known. To perform a message-send, the data type (class) of the receiver is extracted, and the selector is used as a hash index into a table of the message dictionary of the class, which maps selectors to methods. The task of method-lookup is complicated by the inheritance property of classes -- a class may be defined as a subclass to another, inheriting all of the methods of the superclass. If the initial method-lookup fails, the lookup algorithm tries again using the message dictionary of the superclass of the receiver's class, continuing in this way up the class hierarchy until a method corresponding to the selector is found or the top of the inheritance hierarchy is reached.

The Smalltalk-80 language uses the organization of objects into classes to provide strong information hiding. Only the methods associated with a given class (and its subclasses) can access directly the state of an instance of that class. All access from "outside" must be through messages. Because of this, a Smalltalk-80 program must often make procedure calls to access state where languages such as Pascal could compile a direct access to a field of a record. This makes the performance of the method-lookup algorithm even more critical.
