# The LLM Training Pipeline — Overview

> Notes from [LLM Training Overview](https://www.mostofashakib.com/blog/llm_training_overview).
> This is the map. Every other folder in this route is a zoom-in on stage 3 or 4.

Five stages, in order. Each one constrains the next — architecture decisions set
the inference bill, pretraining sets the capability ceiling, post-training
decides what actually gets elicited.

```
1. Architecture → 2. Pre-Training → 3. Post-Training → 4. Evaluation → 5. Inference Ops
```

---

## 1. Model Architecture

The transformer, and the levers on it.

| Component | Role | Why it's there |
|---|---|---|
| Token embeddings | Discrete tokens → vectors | The interface between text and math |
| Positional encoding | Injects order | Attention is permutation-invariant without it |
| Multi-head attention | Parallel relational lookup | Multiple heads attend to different relations at once |
| MLP / feed-forward | Non-linear transformation | Where most parameters and most stored knowledge live |
| Residual connections | Identity path around each block | Gradients survive depth |
| Normalization | Training stability | Keeps activation scale controlled across layers |

**Efficiency variants** — all trade quality for memory/speed on the KV cache:

- **MHA** — every head has its own K and V. Best quality, largest cache.
- **GQA** — heads share K/V in groups. The current default: most of MHA's quality
  at a fraction of the cache.
- **MQA** — all heads share one K/V pair. Smallest cache, most quality loss.

**MoE** — conditional computation. Route each token to a few experts so total
parameters grow without proportional compute per token. Distinguish *total* from
*active* parameters; a "trillion-parameter" MoE may activate 30B per token.

> Interview framing: every one of these is a memory-vs-quality decision, and the
> memory pressure comes from the KV cache at inference. See [../inference/](../inference/).

## 2. Pre-Training

- **Data**: unstructured internet-scale corpora. Quality filtering is most of the work.
- **Objective**: next-token prediction, cross-entropy loss.
- **Scaling laws**: Chinchilla established the compute-optimal ratio of parameters
  to training tokens — earlier models were badly undertrained for their size.
  Note the modern correction: if you serve a model heavily, *inference*-optimal
  beats compute-optimal, so you train a smaller model on far more tokens than
  Chinchilla suggests.
- **Mixed precision**: forward/backward in FP16 or BF16, master weights and
  gradient accumulation in FP32. BF16 is preferred — same exponent range as FP32,
  so no loss scaling needed.
- **Distributed training**: the engineering constraints are thermal and cost
  overrun as much as correctness.

**Output of this stage**: a base model. A capable but wild autocompleter. It has
the knowledge; it has no idea it's supposed to be an assistant.

## 3. Post-Training & Alignment

Turning the autocompleter into an instruction-following assistant.

- **SFT** on high-quality (often synthetic) demonstration data — behavioral cloning.
- **Full fine-tuning vs PEFT** — LoRA, QLoRA. See [../sft/](../sft/).
- **Preference tuning** — DPO, RLHF, RLVR. See [../preference-optimization/](../preference-optimization/).

This stage is the entire subject of the rest of this route.

## 4. Evaluation & Benchmark

- Classic benchmarks like MMLU are **saturating** — the top of the range no
  longer discriminates between frontier models.
- **LLM-as-a-judge** for nuanced failure diagnosis at scale. See [../evals/llm-as-a-judge.md](../evals/llm-as-a-judge.md).
- **Agentic evaluation** for multi-step behavior: tool routing accuracy, retrieval
  and recall of external context, long-horizon workflows without hallucination,
  generalization to novel inputs rather than memorized ones.

## 5. Inference Operations

The goal is latency and cost, not accuracy.

- **KV cache** — store past keys/values so each new token doesn't re-attend from scratch.
- **PagedAttention** — treat the cache like virtual memory pages, eliminating the
  fragmentation that wasted most of the GPU memory in naive serving.
- **Speculative decoding** — a small draft model proposes tokens, the big model
  verifies them in one batched pass.
- **Multi-token prediction** — predict several tokens per forward pass.
- **Decoding strategies** — greedy, beam search, sampling (temperature/top-k/top-p).

---

## How to use this in an interview

If asked anything open-ended about LLMs, draw these five boxes first. It
demonstrates you know where the question sits, and it gives you a structure to
answer within. Then go deep on the box they care about.

The highest-value thing to internalize: **each stage's failure looks like the
next stage's problem.** Bad pretraining data looks like a post-training
capability gap. Bad post-training looks like an eval regression. Bad eval design
looks like a production incident.
