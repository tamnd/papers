---
paper: castro-1999-pbft
title: Practical Byzantine Fault Tolerance
authors:
  - Miguel Castro
  - Barbara Liskov
year: 1999
venue: OSDI
field: security
section: "3"
section_title: Service Properties
tag: "0499"
kind: section
lang: en
source: https://www.scs.stanford.edu/nyu/03sp/sched/bfs.pdf
pdf_sha256: 9b8d5842c967894eaa2d6aa71d4354d26c4f76880f859a117d96042b4a37efc1
pdf_pages: 2-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: cabf72800d9f457aa0b85e4136c1e7ecd176dea4568409ac3bc423ad541a5895
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Our algorithm can be used to implement any deterministic replicated service with a state and some operations. The operations are not restricted to simple reads or writes of portions of the service state; they can perform arbitrary deterministic computations using the state and operation arguments. Clients issue requests to the replicated service to invoke operations and block waiting for a reply. The replicated service is implemented by $n$ replicas. Clients and replicas are non-faulty if they follow the algorithm in Section 4 and if no attacker can forge their signature.

The algorithm provides both safety and liveness assuming no more than $\lfloor \frac{n-1}{3} \rfloor$ replicas are faulty. Safety means that the replicated service satisfies linearizability [14] (modified to account for Byzantine-faulty clients [4]): it behaves like a centralized implementation that executes operations atomically one at a time. Safety requires the bound on the number of faulty replicas because a faulty replica can behave arbitrarily, e.g., it can destroy its state.

Safety is provided regardless of how many faulty clients are using the service (even if they collude with faulty replicas): all operations performed by faulty clients are observed in a consistent way by non-faulty clients. In particular, if the service operations are designed to preserve some invariants on the service state, faulty clients cannot break those invariants.

The safety property is insufficient to guard against faulty clients, e.g., in a file system a faulty client can write garbage data to some shared file. However, we limit the amount of damage a faulty client can do by providing access control: we authenticate clients and deny access if the client issuing a request does not have the right to invoke the operation. Also, services may provide operations to change the access permissions for a client. Since the algorithm ensures that the effects of access revocation operations are observed consistently by all clients, this provides a powerful mechanism to recover from attacks by faulty clients.

The algorithm does not rely on synchrony to provide safety. Therefore, it must rely on synchrony to provide liveness; otherwise it could be used to implement consensus in an asynchronous system, which is not possible [9]. We guarantee liveness, i.e., clients eventually receive replies to their requests, provided at most $\lfloor \frac{n-1}{3} \rfloor$ replicas are faulty and delay($t$) does not grow faster than $t$ indefinitely. Here, $\mathrm{delay}(t)$ is the time between the moment $t$ when a message is sent for the first time and the moment when it is received by its destination (assuming the sender keeps retransmitting the message until it is received). (A more precise definition can be found in [4].) This is a rather weak synchrony assumption that is likely to be true in any real system provided network faults are eventually repaired, yet it enables us to circumvent the impossibility result in [9].

The resiliency of our algorithm is optimal: $3f + 1$ is the minimum number of replicas that allow an asynchronous system to provide the safety and liveness properties when up to $f$ replicas are faulty (see [2] for a proof). This many replicas are needed because it must be possible to proceed after communicating with $n - f$ replicas, since $f$ replicas might be faulty and not responding. However, it is possible that the $f$ replicas that did not respond are not faulty and, therefore, $f$ of those that responded might be faulty. Even so, there must still be enough responses that those from non-faulty replicas outnumber those from faulty ones, i.e., $n - 2f > f$. Therefore $n > 3f$.

The algorithm does not address the problem of fault-tolerant privacy: a faulty replica may leak information to an attacker. It is not feasible to offer fault-tolerant privacy in the general case because service operations may perform arbitrary computations using their arguments and the service state; replicas need this information in the clear to execute such operations efficiently. It is possible to use secret sharing schemes [35] to obtain privacy even in the presence of a threshold of malicious replicas [13] for the arguments and portions of the state that are opaque to the service operations. We plan to investigate these techniques in the future.
