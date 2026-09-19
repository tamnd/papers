---
paper: hochreiter-1997-lstm
title: Long Short-Term Memory
authors:
  - Sepp Hochreiter
  - Jurgen Schmidhuber
year: 1997
venue: Neural Computation
field: ai-ml
section: "2"
section_title: PREVIOUS WORK
tag: "0882"
kind: section
lang: en
source: doi:10.1162/neco.1997.9.8.1735
pdf_sha256: ceb9e53dbc0493f5b3bf5520ed940f3e6b526064d17b2118d77e51f79c0edcc6
pdf_pages: 2-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 2ec156131692ef7d71989e090fed9d3a861e0674908ab6053b5b7c1670e550ef
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

This section will focus on recurrent nets with time-varying inputs (as opposed to nets with stationary inputs and fixpoint-based gradient calculations, e.g., Almeida 1987, Pineda 1987).

**Gradient-descent variants.** The approaches of Elman (1988), Fahlman (1991), Williams (1989), Schmidhuber (1992a), Pearlmutter (1989), and many of the related algorithms in Pearlmutter’s comprehensive overview (1995) suffer from the same problems as BPTT and RTRL (see Sections 1 and 3).

**Time-delays.** Other methods that seem practical for short time lags only are Time-Delay Neural Networks (Lang et al. 1990) and Plate’s method (Plate 1993), which updates unit activations based on a weighted sum of old activations (see also de Vries and Principe 1991). Lin et al. (1995) propose variants of time-delay networks called NARX networks.

**Time constants.** To deal with long time lags, Mozer (1992) uses time constants influencing changes of unit activations (deVries and Principe’s above-mentioned approach (1991) may in fact be viewed as a mixture of TDNN and time constants). For long time lags, however, the time constants need external fine tuning (Mozer 1992). Sun et al.’s alternative approach (1993) updates the activation of a recurrent unit by adding the old activation and the (scaled) current net input. The net input, however, tends to perturb the stored information, which makes long-term storage impractical.

**Ring’s approach.** Ring (1993) also proposed a method for bridging long time lags. Whenever a unit in his network receives conflicting error signals, he adds a higher order unit influencing appropriate connections. Although his approach can sometimes be extremely fast, to bridge a time lag involving 100 steps may require the addition of 100 units. Also, Ring’s net does not generalize to unseen lag durations.

**Bengio et al.’s approaches.** Bengio et al. (1994) investigate methods such as simulated annealing, multi-grid random search, time-weighted pseudo-Newton optimization, and discrete error propagation. Their “latch” and “2-sequence” problems are very similar to problem 3a with minimal time lag 100 (see Experiment 3). Bengio and Frasconi (1994) also propose an EM approach for propagating targets. With $n$ so-called “state networks”, at a given time, their system can be in one of only $n$ different states. See also beginning of Section 5. But to solve continuous problems such as the “adding problem” (Section 5.4), their system would require an unacceptable number of states (i.e., state networks).

**Kalman filters.** Puskorius and Feldkamp (1994) use Kalman filter techniques to improve recurrent net performance. Since they use “a derivative discount factor imposed to decay exponentially the effects of past dynamic derivatives,” there is no reason to believe that their Kalman Filter Trained Recurrent Networks will be useful for very long minimal time lags.

**Second order nets.** We will see that LSTM uses multiplicative units (MUs) to protect error flow from unwanted perturbations. It is not the first recurrent net method using MUs though. For instance, Watrous and Kuhn (1992) use MUs in second order nets. Some differences to LSTM are: (1) Watrous and Kuhn’s architecture does not enforce constant error flow and is not designed to solve long time lag problems. (2) It has fully connected second-order sigma-pi units, while the LSTM architecture’s MUs are used only to gate access to constant error flow. (3) Watrous and Kuhn’s algorithm costs $O(W^2)$ operations per time step, ours only $O(W)$, where $W$ is the number of weights. See also Miller and Giles (1993) for additional work on MUs.

Simple weight guessing. To avoid long time lag problems of gradient-based approaches we may simply randomly initialize all network weights until the resulting net happens to classify all training sequences correctly. In fact, recently we discovered (Schmidhuber and Hochreiter 1996, Hochreiter and Schmidhuber 1996, 1997) that simple weight guessing solves many of the problems in (Bengio 1994, Bengio and Frasconi 1994, Miller and Giles 1993, Lin et al. 1995) faster than the algorithms proposed therein. This does not mean that weight guessing is a good algorithm. It just means that the problems are very simple. More realistic tasks require either many free parameters (e.g., input weights) or high weight precision (e.g., for continuous-valued parameters), such that guessing becomes completely infeasible.

Adaptive sequence chunkers. Schmidhuber’s hierarchical chunker systems (1992b, 1993) do have a capability to bridge arbitrary time lags, but only if there is local predictability across the subsequences causing the time lags (see also Mozer 1992). For instance, in his postdoctoral thesis (1993), Schmidhuber uses hierarchical recurrent nets to rapidly solve certain grammar learning tasks involving minimal time lags in excess of 1000 steps. The performance of chunker systems, however, deteriorates as the noise level increases and the input sequences become less compressible. LSTM does not suffer from this problem.
