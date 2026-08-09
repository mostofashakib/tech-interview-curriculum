# SFT, LoRA, and Quantization — Practice

> Notes from [Post-Training LLMs](https://www.mostofashakib.com/blog/post-training-llms).
> The tooling-and-tradeoffs view. For the theory checklist see [README.md](README.md).

## SFT is behavioral cloning

You have demonstrations; you train the model to imitate them. That framing is
worth keeping because it tells you the ceiling immediately: **an imitation
learner cannot exceed its demonstrations.** Everything past that ceiling requires
preference optimization or RL, which is why
[../preference-optimization/](../preference-optimization/) exists.

## Tooling

**TRL (Hugging Face)** — abstracts the training mechanics: batching, gradient
accumulation, learning-rate scheduling, loss masking on prompt tokens. Worth
knowing what it hides from you, because interviewers ask about exactly those
pieces.

**Unsloth** — rewrites the hot kernels in Triton for roughly **2–5× speedup** on
the same hardware. Fused operations and hand-written backward passes rather than
an algorithmic change.

**vLLM** — serving and batch inference, built on **PagedAttention**. You need it
during post-training too, not just deployment: generating synthetic data and RL
rollouts is an inference-heavy workload.

> Recognize the pattern: post-training is a training loop wrapped around a very
> large inference workload. Teams that are fast at post-training are usually fast
> because their rollout generation is fast.

## LoRA

Freeze the base model. Inject trainable **rank-decomposition matrices** into the
attention projections.

```
h = Wx + (α/r)·BAx        W frozen;  B ∈ R^(d×r),  A ∈ R^(r×k),  r ≪ min(d,k)
```

- `A` initialized random-normal, `B` initialized to **zero** → `ΔW = 0` at step 0,
  so training begins exactly at the base model.
- Trainable parameters drop from `d·k` to `r(d+k)`.
- Target modules matter: attention projections (`q,k,v,o`) are the standard
  choice; adding the MLP projections increases capacity and cost.
- Adapters can be merged into the base weights for inference, or served
  separately so one base model backs many fine-tunes.

## Quantization

**QLoRA** — hold the frozen base weights in 4-bit (NF4) and train LoRA adapters
on top in higher precision. The base is only ever read, so quantization error
there is far cheaper than it would be on weights you're updating.

Supporting pieces: double quantization (quantize the quantization constants) and
paged optimizers (spill optimizer state to CPU on memory spikes).

The general rule to state in an interview: **quantize what you read, keep
precision on what you update.**

## Choosing full fine-tuning vs PEFT

| | Full fine-tuning | LoRA / QLoRA |
|---|---|---|
| Memory | Weights + grads + optimizer states for every parameter | A few % of that |
| Best for | Large data, big behavioral shift, new domain | Style, format, task adaptation |
| Serving | One model per fine-tune | One base + many swappable adapters |
| Risk | Catastrophic forgetting | Capacity ceiling if rank too low |

Default to LoRA. Reach for full fine-tuning when you have a lot of data and are
genuinely trying to move the model's capabilities rather than its behavior.

## The memory calculation to have ready

Full fine-tune, 7B params, bf16 + AdamW:

```
weights (bf16)        2 B/param →  14 GB
gradients (bf16)      2 B/param →  14 GB
AdamW m, v (fp32)     8 B/param →  56 GB
fp32 master weights   4 B/param →  28 GB
                                  ──────
                                  ~112 GB + activations
```

QLoRA on the same model: base weights in 4-bit ≈ 3.5 GB, and gradients and
optimizer state exist only for the adapter — often under 1% of the above. This
contrast is the cleanest way to explain why PEFT changed who can do post-training.
