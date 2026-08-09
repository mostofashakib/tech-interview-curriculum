# Alignment Strategies & RL Algorithms

> Notes from [Post-Training LLMs](https://www.mostofashakib.com/blog/post-training-llms).
> The densest material in this route. Read [../glossary.md](../glossary.md) first.

Two separate questions, often conflated:

1. **Where does the reward signal come from?** → DPO / RLHF / RLVR
2. **What algorithm consumes it?** → TRPO / PPO / GRPO

---

# Part 1 — Where the signal comes from

## DPO — Direct Preference Optimization

Maps preference pairs directly into a language-modeling loss. No reward model,
no rollouts, no RL machinery.

- **Cost**: lowest. Meaningfully less VRAM; it's a supervised loop.
- **Data**: a fixed offline set of (prompt, chosen, rejected) triples.
- **Limit**: offline. The model can only learn from responses collected before
  training started, so as the policy drifts, its own current outputs are never
  scored.

## RLHF — RL from Human Feedback

Sample outputs from the policy, score them with a learned reward model trained on
human preferences, optimize.

- **Signal**: scalar reward from a learned model, itself trained on preference
  pairs rather than fixed targets.
- **Strength**: online. Scores what the model actually produces right now.
- **Weakness**: you are optimizing against a *learned approximation* of human
  judgment. Every flaw in the RM becomes an optimization target.

## RLVR — RL from Verifiable Rewards

Replace the learned reward model with a **programmatic verifier**: unit tests, a
symbolic math checker, a compiler, a schema validator. Reward is binary or graded
by the verifier.

- **Strength**: the verifier cannot be flattered. This removes the single largest
  source of reward hacking.
- **Limit**: only applies where correctness is machine-checkable, and a weak
  verifier is worse than no verifier — the model will find its gaps. (Tests that
  don't cover an edge case become tests the model learns to satisfy trivially.)
- **Where it shines**: math, code, structured output, anything with a ground truth.

> The strategic read: the field moved toward RLVR because verifiable domains let
> you scale RL without scaling human labeling. If you can turn your task into a
> verifiable one, do that before you build a reward model.

---

# Part 2 — The algorithms

## TRPO — Trust Region Policy Optimization

Uses **second-order** information (the Fisher Information Matrix) to take the
largest policy step that provably stays within a KL "trust region."

- Mathematically principled, genuinely stable.
- Computationally expensive — you're working with curvature, not just gradients.
- **Rarely used today.** Know it as the thing PPO simplified, because that framing
  is exactly what the "why PPO?" question is looking for.

## PPO — Proximal Policy Optimization

The industry standard for instruct-tuning, and what ChatGPT-style RLHF ran on.
Replaces TRPO's second-order math with a cheap **first-order** approximation.

**Core objective** — probability ratio times advantage:

```
r_t(θ) = π_θ(a_t|s_t) / π_θ_old(a_t|s_t)

L(θ) = E[ r_t(θ) · A_t ]
```

**Clipped objective** — the whole trick. Clip the ratio so an update can't move
the policy too far in one step:

```
L_PPO(θ) = E[ min( r_t(θ)·A_t , clip(r_t(θ), 1−ε, 1+ε)·A_t ) ]
```

Typical `ε = 0.2`. The `min` makes the bound pessimistic: it removes the
incentive to move further when the update is already large in the favorable
direction, while leaving corrections in the unfavorable direction unclipped.

**KL penalty** — a second, independent leash, this one against the frozen
reference model:

```
L = L_PPO − β · D_KL(π_θ ‖ π_ref)
```

`β` controls penalty strength. **Adaptive KL control** adjusts `β` on the fly to
hit a target KL. Be precise about the distinction:

- The **clip** limits movement per *update step* (vs. the previous policy).
- The **KL penalty** limits total drift from the *original SFT model*.

They solve different problems and you need both.

**Requires a Value Model (critic)** to estimate advantages — a second trained
network alongside the policy.

**Known failure modes**: reward hacking, length bias, and — if `β` is too high —
*alignment inertia*, where the KL penalty is so strong the model refuses to move
and training accomplishes nothing.

## GRPO — Group Relative Policy Optimization

Powers the DeepSeek-R1 family. **Eliminates the value model.**

Instead of learning a baseline, sample a **group of 4–8 responses per prompt** and
use the group's own statistics as the baseline:

```
A_i = (r_i − μ) / σ        μ, σ over the group of sampled responses
```

Within a group, "was this response better than average for this prompt?" is
answered empirically. No critic needed.

- Large VRAM reduction versus PPO.
- Naturally suited to verifiable rewards — score 8 solutions, some pass, some
  fail, the advantage falls out.

---

## PPO vs GRPO

**The RLHF VRAM Wall**: PPO holds **four models** in memory simultaneously —
Actor (policy), Critic (value), Reward model, Reference model. That is the single
biggest practical barrier to running RLHF.

| | PPO | GRPO |
|---|---|---|
| Models in memory | 4 (actor, critic, reward, reference) | 3 — no critic |
| Baseline | Learned value function | Group mean/std over 4–8 samples |
| Gradient quality | Smoother, lower variance | Higher variance |
| Memory | The VRAM wall | Runs on far smaller setups |
| Depends on | Critic training well | Group quality and diversity |

**When to use which:**

- **PPO** — general instruct-tuning when you have the GPU cluster for it. You're
  buying stability and smoother gradients with infrastructure.
- **GRPO** — memory-constrained setups, or reasoning models where you have a
  verifiable reward function. The group baseline is most informative exactly when
  responses to one prompt genuinely differ in quality, which is what verifiable
  tasks give you.

Note the coupling: **GRPO and RLVR fit together.** Group-relative advantage needs
score spread within a group; a verifier produces exactly that. This is why
reasoning models converged on the combination.

---

## Cheat sheet

| Method | Reward source | Online? | Value model? | Main risk |
|---|---|---|---|---|
| DPO | Preference pairs (implicit) | No | No | Offline drift; both logprobs can fall |
| RLHF + PPO | Learned RM | Yes | Yes | Reward hacking; VRAM wall |
| RLVR + GRPO | Programmatic verifier | Yes | No | Verifier gaps; high variance |

## Questions to be ready for

- Why does PPO clip? What breaks without it?
- Clip vs KL penalty — why do you need both? (Very common follow-up.)
- Why did GRPO drop the value model, and what does that cost?
- You have 8 GPUs and a math dataset with checkable answers. Design the run.
- Your KL is spiking at step 300 and outputs are degenerating. Diagnose it.
- When is DPO the right call despite being strictly less powerful?
