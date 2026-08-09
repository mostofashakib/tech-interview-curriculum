# Post-Training

Everything that happens to a language model **after** pretraining: turning a raw
next-token predictor into a model that follows instructions, reasons, uses tools,
and is safe to ship.

This route is for AI lab and research-engineer interviews. Start with
[fundamentals/llm-training-overview.md](fundamentals/llm-training-overview.md)
for the map, then [glossary.md](glossary.md) for the vocabulary.

## The pipeline

```
pretraining → SFT → reward modeling → preference optimization → evals
   (base)    (instruct)  (RM/verifier)   (RLHF / DPO / GRPO)     (ship?)
                 ↑____ data curation feeds every stage ____↑
                 ↑____ RL environments produce the reward ____↑
```

If you can draw this and explain what each arrow costs, what it buys, and how it
fails, you can hold a conversation about post-training.

## Contents

| Folder | Covers | Written notes |
|---|---|---|
| [fundamentals/](fundamentals/) | Transformer recap, the 5-stage pipeline, training memory math | [llm-training-overview.md](fundamentals/llm-training-overview.md) |
| [data/](data/) | Taxonomies, synthetic data, rubrics, filtering, contamination | [synthetic-data-and-rubrics.md](data/synthetic-data-and-rubrics.md) |
| [sft/](sft/) | Instruction tuning, chat templates, LoRA/QLoRA, TRL/Unsloth/vLLM | [sft-lora-and-quantization.md](sft/sft-lora-and-quantization.md) |
| [reward-modeling/](reward-modeling/) | Preference data, Bradley-Terry, RM failure modes | — |
| [preference-optimization/](preference-optimization/) | DPO, RLHF, RLVR; TRPO, PPO, GRPO | [alignment-strategies-and-rl-algorithms.md](preference-optimization/alignment-strategies-and-rl-algorithms.md) |
| [rl-environments/](rl-environments/) | Environment design, reward design, sandboxes, anti-gaming | — |
| [evals/](evals/) | Benchmarks, judges, factuality, agentic evaluation | [llm-evaluation.md](evals/llm-evaluation.md), [llm-as-a-judge.md](evals/llm-as-a-judge.md), [agentic-evaluation.md](evals/agentic-evaluation.md) |
| [inference/](inference/) | KV cache, quantization, speculative decoding, serving economics | — |
| [interview-questions/](interview-questions/) | Question bank across the route | — |

Plus [glossary.md](glossary.md) — policy, value function, trajectory, KL
divergence, Fisher information. Read it before the RL sections.

> Folders marked "—" are checklists and question banks awaiting your notes.
> The written notes are derived from
> [mostofashakib.com/blog](https://www.mostofashakib.com/blog), linked at the top
> of each file.

## Suggested path

1. **[fundamentals/llm-training-overview.md](fundamentals/llm-training-overview.md)** — the five stages, so you know where every later topic sits
2. **[glossary.md](glossary.md)** — policy, trajectory, KL, advantage
3. **[data/](data/)** — most real post-training work is data work, and interviewers know it
4. **[sft/](sft/)** — behavioral cloning, and why it has a ceiling
5. **[reward-modeling/](reward-modeling/) → [preference-optimization/](preference-optimization/)** — one continuous story; do them together
6. **[rl-environments/](rl-environments/)** — where the reward signal actually comes from
7. **[evals/](evals/)** — last to study, first to be asked about
8. **[inference/](inference/)** — the constraint everything else lives under
9. **[interview-questions/](interview-questions/)** — drill

## Study rule

For every technique, be able to answer four things:

- **What problem does it solve?** (why doesn't SFT alone suffice?)
- **What is the objective function?** Write it down. Derive DPO from the RLHF objective.
- **How does it fail?** (reward hacking, mode collapse, sycophancy, length bias)
- **What does it cost?** (compute, data, human labeling, wall-clock, VRAM)

Covering all four reads as experience. Covering only the first reads as
blog-post knowledge.

## Prerequisites

Neural network fundamentals, backprop, and optimizers come from
[../machine-learning/deep-learning/](../machine-learning/deep-learning/). KL
divergence, cross-entropy, and MLE come from
[../machine-learning/math/](../machine-learning/math/).

## Video courses

Course recommendations sit in the folder they belong to: CS336 and CME295 in
[fundamentals/](fundamentals/), CS329H and CS224R in
[preference-optimization/](preference-optimization/). One spans the whole route
and has no narrower home:

- [Stanford CS329A — Self-Improving AI Agents](https://www.youtube.com/playlist?list=PLangBM27OtEA)
  — self-training, agentic RL, and evaluation loops treated as one subject.
  Closest thing to a course on where post-training is currently heading, which
  makes it useful for the "what would you do next" end of an interview.
