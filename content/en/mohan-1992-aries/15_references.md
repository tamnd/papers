---
paper: mohan-1992-aries
title: 'ARIES: A Transaction Recovery Method Supporting Fine-Granularity Locking and Partial Rollbacks Using Write-Ahead Logging'
authors:
  - C. Mohan
  - Don Haderle
  - Bruce Lindsay
  - Hamid Pirahesh
  - Peter Schwarz
year: 1992
venue: ACM TODS
field: databases
section_title: References
tag: 074F
kind: references
lang: en
source: https://people.eecs.berkeley.edu/~brewer/cs262/Aries2.pdf
pdf_sha256: 1007fcedb6b8b465f97ee1c4e4d88420450b50b18ff5ad400a130b21e4961817
pdf_pages: 32-35
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 78568d38163fd4165e42fa7f748456508c266059080e3167f120257c01038908
edited: true
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

1. BAKER, J., CRUS, R., AND HADERLE, D. Method for assuring atomicity of multi-row update operations in a database system. U.S. Patent 4,498,145, IBM, Feb. 1985.
2. BADRINATH, B. R., AND RAMAMRITHAM, K. Semantics-based concurrency control: Beyond commutativity. In Proceedings 3rd IEEE International Conference on Data Engineering (Feb. 1987).
3. BERNSTEIN, P., HADZILACOS, V., AND GOODMAN, N. Concurrency Control and Recovery in Database Systems. Addison-Wesley, Reading, Mass., 1987.
4. BORR, A. Robustness to crash in a distributed database: A non-shared-memory multi-processor approach. In Proceedings 10th International Conference on Very Large Data Bases (Singapore, Aug. 1984).
5. CHAMBERLIN, D., GILBERT, A., AND YOST, R. A history of System R and SQL/Data System. In Proceedings 7th International Conference on Very Large Data Bases (Cannes, Sept. 1981).
6. CHANG, A., AND MERGEN, M. 801 storage: Architecture and programming. ACM Trans. Comput. Syst., 6, 1 (Feb. 1988), 28–50.
7. CHANG, P. Y., AND MYRE, W. W. OS/2 EE database manager: Overview and technical highlights. IBM Syst. J. 27, 2 (1988).
8. COPELAND, G., KHOSHAFIAN, S., SMITH, M., AND VALDURIEZ, P. Buffering schemes for permanent data. In Proceedings International Conference on Data Engineering (Los Angeles, Feb. 1986).

158 · C. Mohan et al.

ARIES: A Transaction Recovery Method

9. CLARK, B. E., AND CORRIGAN, M. J. Application System/400 performance characteristics. IBM Syst. J. 28, 3 (1989).

10. CHENG, J., LOOSELY, C., SHIBAMITAYA, A., AND WORTHINGTON, P. IBM Database 2 performance: Design, implementation, and tuning. IBM Syst. J. 23, 2 (1984).

11. CRUS, R., HAERDER, D., AND HERRON, H. Method for managing lock escalation in a multiprocessing, multiprogramming environment. U.S. Patent 4,716,528, IBM, Dec. 1987.

12. CRUS, R., MALIKEMUS, T., AND PUTZOLU, G. R. Index mini-pages IBM Tech. Disclosure Bull. 26, 4 (April 1983), 5460–5463.

13. CRUS, R., PUTZOLU, F., AND MORTENSON, J. A. Incremental data base log image copy IBM Tech. Disclosure Bull. 25, 7B (Dec. 1982), 3730–3732.

14. CRUS, R., AND PUTZOLU, F. Data base allocation table. IBM Tech. Disclosure Bull. 25, 7B (Dec. 1982), 3722–2724.

15. CRUS, R. Data recovery in IBM Database 2. IBM Syst. J. 23, 2 (1984).

16. CURTIS, R. Informix-Turbo, In Proceedings IEEE Compcon Spring '88 (Feb.–March 1988).

17. DASGUPTA, P., LEBLANC, R., JR., AND APPELLE, W. The Clouds distributed operating system. In Proceedings 8th International Conference on Distributed Computing Systems (San Jose, Calif., June 1988).

18. DATE, C. A Guide to INGRES. Addison-Wesley, Reading, Mass., 1987.

19. DEY, R., SHAN, M., AND TRAIGER, I. Method for dropping data sets. IBM Tech. Disclosure Bull. 25, 11A (April 1983), 5453–5455.

20. DEWITT, D., GHANDEHARIZADEH, S., SCHNEIDER, D., BRICKER, A., HSIAO, H.-I., AND RASMUSSEN, R. The Gamma database machine project. IEEE Trans. Knowledge Data Eng. 2, 1 (March 1990).

21. DELORME, D., HOLM, M., LEE, W., PASSE, P., RICARD, G., TIMMS, G., JR., AND YOUNGREN, I. Database index journaling for enhanced recovery. U.S. Patent 4,819,156, IBM, April 1989

22. DIXON, G. N., PARRINGTON, G. D., SHRIVASTAVA, S., AND WHEATER, S. M. The treatment of persistent objects in Ariuna. Comput. J. 32, 4 (1989).

23. DUCHAMP, D. Transaction management. Ph.D. dissertation, Tech. Rep. CMU-CS-88-192, Carnegie-Mellon Univ., Dec. 1988.

24. EFFELSBERG, W., AND HAERDER, T. Principles of database buffer management. ACM Trans. Database Syst. 9, 4 (Dec. 1984).

25. ELHARDT, K., AND BAYER, R. A database cache for high performance and fast restart in database systems. ACM Trans Database Syst. 9, 4 (Dec. 1984).

26. FEKETE, A., LYNCH, N., MERRITT, M., AND WEHL, W. Commutativity-based locking for nested transactions. Tech. Rep. MIT/LCS/TM-370.b, MIT, July 1989.

27. FOSSUM, B. Data base integrity as provided for by a particular data base management system. In Data Base Management, J. W. Klumbie and K. L. Koffeman, Eds., North-Holland, Amsterdam, 1974.

28. GAWLICK, D., AND KINKADE, D. Varieties of concurrency control in IMS/VS Fast Path. IEEE Database Eng. 8, 2 (June 1985).

29. GARZA, J., AND KIM, W. Transaction management in an object-oriented database system. In Proceedings ACM-SIGMOD International Conference on Management of Data (Chicago, June 1988).

30. GHEITH, A., AND SCHWAN, K. CHAOSart: Support for real-time atomic transactions. In Proceedings 19th International Symposium on Fault-Tolerant Computing (Chicago, June 1989).

31. GRAY, J., MCJONES, P., BLASGEN, M., LINDSAY, B., LORIE, R., PRICE, T., PUTZOLU, F., AND TRAIGER, I. The recovery manager of the System R database manager. ACM Comput. Surv. 13, 2 (June 1981).

32. GRAY, J. Notes on data base operating systems. In Operating Systems—An Advanced Course, R. Bayer, R. Graham, and G. Seegmuller, Eds., LNCS Vol. 60, Springer-Verlag, New York, 1978.

33. HADZILACOS, V. A theory of reliability in database systems. J. ACM 35, 1 (Jan. 1988), 121–145.

34. HAERDER, T. Handling hot spot data in DB sharing systems. Inf. Syst. 13, 2 (1988), 155–166.

ACM Transactions on Database Systems, Vol. 17, No. 1, March 1992

159 · C. Mohan et al.

ARIES: A Transaction Recovery Method

35. HAERDER, D., AND JACKSON, R. IBM Database 2 overview. IBM Syst. J. 23, 2 (1984).

36. HAERDER, T., AND REUTER, A. Principles of transaction oriented database recovery—A taxonomy. ACM Comput. Surv. 15, 4 (Dec. 1983).

37. HELLAND, P. The TMF application programming interface: Program to program communication, transactions, and concurrency in the Tandem NonStop system. Tandem Tech. Rep. TR89.3, Tandem Computers, Feb. 1989.

38. HERLIHY, M., AND WEILH, W. Hybrid concurrency control for abstract data types. In Proceedings 7th ACM SIGACT-SIGMOD-SIGART Symposium on Principles of Database Systems (Austin, Tex., March 1988).

39. HERLIHY, M., AND WING, J. M. Avalon: Language support for reliable distributed systems. In Proceedings 17th International Symposium on Fault-Tolerant Computing (Pittsburgh, Pa., July 1987).

40. HASKIN, R., MALACHI, Y., SAWDON, W., AND CHAN, G. Recovery management in QuickSilver. ACM Trans. Comput. Syst. 6, 1 (Feb. 1988), 82–108.

41. IMS / VS Version 1 Release 3 Recovery / Restart. Doc. GG24-1652, IBM, April 1984.

42. IMS / VS Version 2 Application Programming. Doc. SC26-4178, IBM, March 1986.

43. IMS / VS Extended Recovery Facility (XRF): Technical Reference. Doc. GG24-3153, IBM, April 1987.

44. IBM Workstation Data Save Facility / VM: General Information. Doc. GH24-5232, IBM, 1990.

45. KORTH, H. Locking primitives in a database system. JACM 30, 1 (Jan. 1983), 55–79.

46. LUM, V., DADAM, P., ERBE, R., GUENAUER, J., PISTOR, P., WALCH, G., WERNER, H., AND WOODFILL, J. Design of an integrated DBMS to support advanced applications. In Proceedings International Conference on Foundations of Data Organization (Kyoto, May 1985).

47. LEVINE, F., AND MOHAN, C. Method for concurrent record access, insertion, deletion and alteration using an index tree. U.S. Patent 4,914,569, IBM, April 1990.

48. LEWIS, R. Z. IMS Program Isolation Locking. Doc. GG66-3193, IBM Dallas Systems Center, Dec. 1990.

49. LINDSAY, B., HAAS, I., MOHAN, C., WILMS, P., AND YOST, R. Computation and communication in R*: A distributed database manager. ACM Trans. Comput. Syst. 2, 1 (Feb. 1984). Also in Proceedings 9th ACM Symposium on Operating Systems Principles (Bretton Woods, Oct. 1983). Also available as IBM Res. Rep. RJ3740, San Jose, Calif., Jan. 1983.

50. LINDSAY, B., MOHAN, C., AND PIRAHESH, H. Method for reserving space needed for “roll-back” actions. IBM Tech. Disclosure Bull. 29, 6 (Nov. 1986).

51. LISKOV, B., AND SCHEIFLER, R. Guardians and actions: Linguistic support for robust, distributed programs. ACM Trans. Program. Lang. Syst. 5, 3 (July 1983).

52. LINDSAY, B., SELINGER, P., GALFIERI, C., GRAY, J., LORIE, R., PUTZOLU, F., TRAIGER, I., AND WADE, B. Notes on distributed databases. IBM Res. Rep. RJ2571, San Jose, Calif., July 1979.

53. MCGEE, W. C. The information management system IMS/VS—Part II: Data base facilities; Part V: Transaction processing facilities. IBM Syst. J. 16, 2 (1977).

54. MOHAN, C., HAERDER, D., WANG, Y., AND CHENG, J. Single table access using multiple indexes: Optimization, execution, and concurrency control techniques. In Proceedings International Conference on Extending Data Base Technology (Venice, March 1990). An expanded version of this paper is available as IBM Res. Rep. RJ7341, IBM Almaden Research Center, March 1990.

55. MOHAN, C., FUSSELL, D., AND SILBERSCHATZ, A. Compatibility and commutativity of lock modes. Inf. Control 61, 1 (April 1984). Also available as IBM Res. Rep. RJ3948, San Jose, Calif., July 1983.

56. MOSS, E., GRIFFETH, N., AND GRAHAM, M. Abstraction in recovery management. In Proceedings ACM SIGMOD International Conference on Management of Data (Washington, D.C., May 1986).

57. MOHAN, C. ARIES/KVI: A key-value locking method for concurrency control of multiaction transactions operating on B-tree indexes. In Proceedings 16th International Conference on Very Large Data Bases (Brisbane, Aug. 1990). Another version of this paper is available as IBM Res. Rep. RJ7008, IBM Almaden Research Center, Sept. 1989.

58. MOHAN, C. Commit-LSN: A novel and simple method for reducing locking and latching in transaction processing systems. In Proceedings 16th International Conference on Very Large Data Bases (Brisbane, Aug. 1990). Also available as IBM Res. Rep. RJ7344, IBM Almaden Research Center, Feb. 1990.

59. MOHAN, C. ARIES/LHS: A concurrency control and recovery method using write-ahead logging for linear hashing with separators. IBM Res. Rep., IBM Almaden Research Center, Nov. 1990.

60. MOHAN, C. A cost-effective method for providing improved data availability during DBMS restart recovery after a failure. In Proceedings of the 4th International Workshop on High Performance Transaction Systems (Asilomar, Calif., Sept. 1991). Also available as IBM Res. Rep. RJ8114, IBM Almaden Research Center, April 1991.

61. MOSS, E., LEBAN, B., AND CHRYSANTHIS, P. Fine grained concurrency for the database cache. In Proceedings 3rd IEEE International Conference on Data Engineering (Los Angeles, Calif., July 1980).

62. MOHAN, C., AND LEVINE, F. ARIES/IM: An efficient and high concurrency index management method using write-ahead logging. IBM Res. Rep. RJ6846, IBM Almaden Research Center, Aug. 1989.

63. MOHAN, C., AND LINDSAY, B. Efficient commit protocols for the tree of processes model of distributed transactions. In Proceedings 2nd ACM SIGACT/SIGOPS Symposium on Principles of Distributed Computing (Montreal, Aug. 1983). Also available as IBM Res. Rep. RJ3881, IBM San Jose Research Laboratory, June 1983.

64. MOHAN, C., LINDSAY, B., AND OBERMARCK, R. Transaction management in the R* distributed database management system. ACM Trans. Database Syst. 11, 4 (Dec. 1986).

65. MOHAN, C., AND NARANG, I. Recovery and coherency-control protocols for fast intersystem page transfer and fine-granularity locking in a shared disks transaction environment. In Proceedings 17th International Conference on Very Large Data Bases (Barcelona, Sept. 1991). A longer version is available as IBM Res. Rep. RJ8017, IBM Almaden Research Center, March 1991.

66. MOHAN, C., AND NARANG, I. Efficient locking and caching of data in the multisystem distributed computing: Page recovery using multiple logs in the shared disks environment. IBM Res. Rep. RJ7343, IBM Almaden Research Center, March 1990.

68. MOHAN, C., NARANG, I., SILEN, S. Solutions to hot spot problems in a shared disks transaction environment. In Proceedings of the 4th International Workshop on High Performance Transaction Systems (Asilomar, Calif., Sept. 1991). Also available as IBM Res. Rep. RJ8301, IBM Almaden Research Center, Aug. 1991.

69. MOHAN, C., AND PIRAHESH, H. ARIES-RRH: Restricted repeating of history in the ARIES transaction recovery method. In Proceedings 7th International Conference on Data Engineering (Kobe, April 1990) Research Center, Feb. 1990

70. MOHAN, C., AND ROTHERMEL, K. Recovery protocol for nested transactions using write-ahead logging. IBM Tech. Disclosure Bull. 31, 4 (Sept. 1988).

71. MOSS, E. Checkpoint and restart in distributed transaction systems. In Proceedings 3rd Symposium on Reliability in Distributed Software and Database Systems (Clearwater Beach, Oct. 1983).

72. MOSS, E. Log-based recovery for nested transactions. In Proceedings 13th International Conference on Very Large Data Bases (Brighton, Sept. 1987).

73. MOHAN, C., TRIEBER, K., AND OBERMARCK, R. Algorithms for the management of remote backup databases for disaster recovery. IBM Res. Rep. RJ7885, IBM Almaden Research Center, Nov. 1990.

74. NETT, E., KAISER, J., AND KROGER, R. Providing recoverability in a transaction oriented distributed operating system. In Proceedings 6th International Conference on Distributed Computing Systems (Cambridge, May 1986).

57. O'NEILL, P. The Escrow transaction method. ACM Trans. Database Syst. 11, 4 (Dec. 1986).

75. NOE, J., KAISER, J., KROGER, R., AND NETT, E. The commit/abort problem in type-specific locking. GMD Tech. Rep. 267, GMD mbH, Sankt Augustin, Sept. 1987.

76. OBERMARCK, R. IMS/VS program isolation feature. IBM Res. Rep. RJ2879, San Jose, Calif., July 1980.

77. O'NEILL, P. The Escrow transaction method. ACM Trans. Database Syst. 11, 4 (Dec. 1986).

78. ONG, K. SYNAPSE approach to database recovery. In Proceedings 3rd ACM SIGACT-SIGMOD Symposium on Principles of Database Systems (Waterloo, April 1984).

79. PEINL, P., REUTER, A., AND SAMMER, H. High contention in a stock trading database: A case study. In Proceedings ACM SIGMOD International Conference on Management of Data (Chicago, June 1988).

80. PETERSON, R. J., AND STRICKLAND, J. P. Log write-ahead protocols and IMS/VS logging. In Proceedings 2nd ACM SIGACT-SIGMOD Symposium on Principles of Database Systems (Atlanta, Ga., March 1983).

81. RENGARAJAN, T. K., SPIRO, P., AND WRIGHT, W. High availability mechanisms of VAX DBMS software. Digital Tech. J. 8 (Feb. 1989).

82. REUTER, A. A fast transaction-oriented logging scheme for UNDO recovery. IEEE Trans. Softw. Eng. SE-6, 4 (July 1980).

83. REUTER, A. Concurrency on high-traffic data elements. In Proceedings ACM SIGACT-SIGMOD Symposium on Principles of Database Systems (Los Angeles, March 1982).

84. REUTER, A. Performance analysis of recovery techniques. ACM Trans. Database Syst. 9, 4 (Dec. 1984), 526-559.

85. ROTHERMEL, K., AND MOHAN, C. ARIES/NT: A recovery method based on write-ahead logging for nested transactions. In Proceedings 15th International Conference on Very Large Data Bases (Amsterdam, Aug. 1989). A longer version of this paper is available as IBM Res. Rep. RJ6650, IBM Almaden Research Center, Jan. 1989.

86. ROWE, L., AND STONEBRAKER, M. The commercial INGRES epilogue. Ch. 3 in The INGRES Papers, Stonebraker, M., Ed., Addison-Wesley, Reading, Mass., 1986.

87. SCHWARZ, P., CHANG, W., FREYTAG, J., LOHMAN, G., MCPEHRSON, J., MOHAN, C., AND PIRAHESH, H. Extensibility in the Starburst database system. In Proceedings Workshop on Object-Oriented Data Base Systems (Asilomar, Calif., Sept. 1986). Also available as IBM Res. Rep. RJ5311, San Jose, Calif., Sept. 1986.

88. SCHWARZ, P. Transactions on typed objects. Ph.D. dissertation, Tech. Rep. CMU-CS-84-166, Carnegie Mellon Univ., Dec. 1984.

89. SHASHA, D., AND GOODMAN, N. Concurrent search structure algorithms. ACM Trans. Database Syst. 13, 1 (March 1988).

90. SPECTOR, A., PAUSCH, R., AND BRUELL, G. Camelot: A flexible, distributed transaction processing system. In Proceedings IEEE Compcon Spring '88 (San Francisco, Calif., March 1988).

91. SPRATT, L. The transaction resolution journal: Extending the before journal. ACM Oper. Syst. Rev. 19, 3 (July 1985).

92. STONEBRAKER, M. The design of the POSTGRES storage system. In Proceedings 13th International Conference on Very Large Data Bases (Brighton, Sept. 1987).

93. STILLWELL, J. W., AND RADER, P. M. IMS/VS Version 1 Release 3 Fast Path Notebook. Doc. G320-0149-0, IBM, Sept. 1984.

94. STRICKLAND, J., UHROWCZIK, P., AND WATTS, V. IMS/VS: An evolving system. IBM Syst. J. 21, 4 (1982).

95. THE TANDEM DATABASE GROUP. NonStop SQL: A distributed, high-performance, high-availability implementation of SQL. In Lecture Notes in Computer Science Vol. 359, D. Gawlick, M. Haynie, and A. Reuter, Eds., Springer-Verlag, New York, 1989.

96. TENG, J., AND GUMAER, R. Managing IBM Database 2 buffers to maximize performance. IBM Syst. J. 23, 2 (1984).

97. TRAIGER, I. Virtual memory management for database systems. ACM Oper. Syst. Rev. 16, 4 (Oct. 1982), 26-48.

98. VURAL, S. A simulation study for the performance analysis of the ARIES transaction recovery method. M.Sc. thesis, Middle East Technical Univ., Ankara, Feb. 1990.

ACM Transactions on Database Systems, Vol. 17, No. 1, March 1992.

99. WATSON, C. T., AND ABERLE, G. F. System/38 machine database support. In IBM Syst. 38/Tech. Dev., Doc. G580-0237, IBM July 1980.

100. WEIKUM, G. Principles and realization strategies of multi-level transaction management. ACM Trans. Database Syst. 16, 1 (Mar. 1991).

101. WEINSTEIN, M., PAGE, T., Jr., LIVEZEY, B., AND POPEK, G. Transactions and synchronization in a distributed operating system. In Proceedings 10th ACM Symposium on Operating Systems Principles (Orcas Island, Dec. 1985).

Received January 1989; revised November 1990; accepted April 1991

ACM Transactions on Database Systems, Vol. 17, No. 1, March 1992.
