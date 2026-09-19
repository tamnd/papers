---
paper: goldwasser-1985-zk
title: The Knowledge Complexity of Interactive Proof-Systems
authors:
  - Shafi Goldwasser
  - Silvio Micali
  - Charles Rackoff
year: 1985
venue: STOC
field: theory
section_title: Experiment
kind: section
lang: en
source: https://people.csail.mit.edu/silvio/Selected%20Scientific%20Papers/Proof%20Systems/The_Knowledge_Complexity_Of_Interactive_Proof_Systems.pdf
pdf_sha256: 17b24f25b180ba64559a089efb443337c61c916078f73be4c496bf8d27410222
pdf_pages: 14-15
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: f8815d60e2a387feab345198454c977a995451f8de8673d57b692f7d355603a1
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Choose for $U_{i+1}$ a random quadratic residue mod $x$, $u_{i+1}$. If $B'$ were $B$, we would choose $\mathrm{BIT}_{i+1}$ to be the $(i+1)$st bit of $r$. However, all we can say is that $\mathrm{BIT}_{i+1}$ is assigned the value $bit_{i+1} = f(x, y, H, v_i, u_{i+1})$, where $f$ is some $\{0, 1\}$-valued function computable in deterministic, polynomial time. If $bit_{i+1} = 0$, then $W_{i+1}$ gets the value $w_{i+1}$, a random square root of $u_{i+1} \mod x$; if $bit_{i+1} = 1$, then $W_{i+1}$ gets the value $w_{i+1}$, a random square root mod $x$ of $(u_{i+1} y) \mod x$.

Having characterized the view with the above experiment, we will now describe a probabilistic Turing machine $M$ that, given $(x, y) \in \mathrm{QR}$ and a string $H$, runs in expected polynomial time, and such that its output distribution $M((x, y), H)$ is *exactly* the same as $V_m$ above; that is, $M((x, y), H)$ is the same as $\mathrm{View}_{A,B'}((x, y), H)$. $M$ begins by choosing $r$ equals a random bit string (of the appropriate length). Assume that $v_i$ has been chosen for some $i, 1 \leq i < m$; $M$ outputs $u_{i+1}, bit_{i+1}, w_{i+1}$ according to the following program:

```text
DO FOREVER
    bitᵢ₊₁ := a random member of {0, 1}
    wᵢ₊₁ := a random member of Zₓ*
    IF bitᵢ₊₁ = 0 THEN
        uᵢ₊₁ := wᵢ₊₁² mod x
    ELSE
        uᵢ₊₁ := (wᵢ₊₁² y⁻¹) mod x
        IF bitᵢ₊₁ = f(x, y, H, vᵢ, uᵢ₊₁) THEN
            OUTPUT uᵢ₊₁, bitᵢ₊₁, wᵢ₊₁ and HALT
END DO
```

Two things about $M$'s program must be clarified. First, the way $M$ chooses a random member of $Z_x^*$ is by choosing random $m$-bit strings until one is found that is in $Z_x^*$; this halts in expected polynomial time. Secondly, by "$y^{-1}$" we mean that unique member of $Z_x^*$ which when multiplied by $y \mod x$ yields 1.

We now show that $M$ halts in expected time polynomial in $m$, with exactly the right output distribution.

Let $R', \{ U'_i, \mathrm{BIT}'_i, W'_i \}$ be the random variables corresponding to the output of $M$, and let $V'_i$ be defined similarly to $V_i$. Certainly $R'$ has exactly the same distribution as $R$. Let $1 \leq i < m$ and assume that $V'_i$ has exactly the same distribution as $V_i$, and assume that $M$ gives a value to $V'_i$ in expected time polynomial in $m$. Say that both $V_i$ and $V'_i$ have been given the value $v_i$; we wish to show that the above piece of program code halts in expected time polynomial in $m$, with the same output distribution as the above experiment, given that $V_i = V'_i = v_i$.

Consider the body of the DO loop up to but not including the last test. If $bit_{i+1} = 0$ at this point, then since every quadratic residue in $Z_x^*$ has the same number of square roots ($\mod x$), $u_{i+1}$ is equally likely to be any quadratic residue, and $w_{i+1}$ will be a random square root of $u_{i+1}$; if $bit_{i+1} = 1$ at this point, then $u_{i+1}$ will also be a random quadratic residue in this case (since $y$ is a quadratic residue), and $w_{i+1}$ will be a random square root of $(u_{i+1}y) \mod x$. Therefore, the body of the DO loop has the following effect (even though the following code may not be efficiently executable):
