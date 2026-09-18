---
paper: chiu-1989-aimd
title: Analysis of the Increase and Decrease Algorithms for Congestion Avoidance in Computer Networks
authors:
  - Dah-Ming Chiu
  - Raj Jain
year: 1989
venue: Computer Networks and ISDN Systems
field: networks
section: "4"
section_title: '**Nonlinear Controls**'
tag: 03D3
kind: section
lang: en
source: https://www.cse.wustl.edu/~jain/papers/cong_av.htm
pdf_sha256: fd0b0386c611744e744969d3c5ec3e236dc6036344128ed16e7f378a9e257be2
pdf_pages: 12-13
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: b59cf7d427edef28539dd1809b70e5dc8da3043621dc70916bd6fcabae70153b
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

In this section, we explore the behaviour of certain nonlinear controls. In particular, we show how they can be represented by the vector diagrams as in the case for linear controls. This technique again gives an intuitive feeling about how nonlinear controls work. The detailed analysis of nonlinear controls is beyond the scope of this paper. However, we will explain why we consider such nonlinear controls not suitable for practical purposes.

Let us consider in general state transition equations that are expressible as a power of the state:

$$
x_i(t+1) = x_i(t) + \alpha(x_i(t))^k,
$$

or, in terms of control,

$$
u_i(t) = \alpha(x_i(t))^k
$$

where $k$ can be any integer (positive, negative or zero), and $\alpha$ is a normalization constant that defines the step size and sign. Note that $k = 0$ gives the additive policy and $k = 1$ gives the multiplicative policy.

Now let us consider the two user vector representation for these controls. In Fig. 8 we first show the efficiency and fairness lines as before. Consider the point $x^{1'}$. Let $\theta(k)$ be the slope of $u(t)$. Then we know $\theta(0)$ is $45^\circ$ and $\theta(1)$ is the same as the slope for the initial state $x(t)$. As $k$ tends to infinity, $\theta(k)$ tends to $0^\circ$ and as $k$ tends to negative infinity, $\theta(k)$ tends to $90^\circ$.

Since fairness requires that the slope of the new state $x(t+1)$ be closer to $45^\circ$ than that of the initial state $x(t)$, we must have $k \leq 1$ (negative $k$ is fine).

Slopes for other three possibilities $x^L, x^{H'},$ and $x^{H'}$ are shown in the figure and can be similarly explained. Considering all four possibilities we see that the feasibility condition requires $k \leq 1$ for increase and $k \geq 1$ for decrease (with at least one inequality being strict), and appropriate values for $\alpha$ so the sign and step size are correct. The additive increase and multiplicative decrease control, for example, clearly satisfies this general condition.

Fig. 8. Vectorial representation for nonlinear controls. {#chiu-1989-aimd-fig-8 .figure tag=03D4}

A nonlinear control could generally include more components with different slopes:

$$
u_i(t) = \sum_{k=-\infty}^{\infty} \alpha_k (x_k(t))^k.
$$

Then the sum of the components must have a slope satisfying the above condition.

Although nonlinear controls offer us far more flexibility in trying to direct towards fairness, it also complicates the task of finding the right scaling factors, represented by $\alpha_k$ in the above equation. These parameters usually must be chosen relative to system parameters, such as the capacity $X_{goal}$ and maximum number of users $N_{max}$. Being too sensitive to system parameters reduces the robustness of the control. For this reason we spent less effort in exploring nonlinear controls. We will discuss the robustness question more in the next section.
