# Fundamentals

The background every other folder in this route assumes.

**Notes in this folder:**
[llm-training-overview.md](llm-training-overview.md) — the five-stage pipeline
(architecture → pretraining → post-training → evaluation → inference ops). Read
it first; it's the map for the whole route.

## Checklist

**Transformer mechanics**
- [ ] Attention: QKV, scaled dot-product, why the `1/√d_k` scaling exists
- [ ] Multi-head vs grouped-query (GQA) vs multi-query (MQA) attention
- [ ] Positional encoding: absolute, learned, RoPE, and how RoPE enables context extension
- [ ] Decoder-only vs encoder-decoder, and why decoder-only won
- [ ] Normalization placement (pre-LN vs post-LN) and why pre-LN trains more stably
- [ ] Mixture-of-experts: routing, load balancing, active vs total params

**Pretraining, in enough depth to contrast with post-training**
- [ ] Next-token prediction objective, cross-entropy, perplexity
- [ ] Scaling laws: Chinchilla-optimal vs inference-optimal training
- [ ] What a base model can and cannot do (in-context learning, no instruction following)

**Post-training, framed**
- [ ] Why a base model needs post-training at all — the format/intent gap
- [ ] The three things post-training buys: instruction following, style/persona, safety
- [ ] Capability *elicitation* vs capability *injection* — post-training mostly elicits
  what pretraining already put there. Know the evidence for and against this claim.
- [ ] Alignment tax: where post-training makes benchmarks worse, and why

**Training mechanics you will be asked to reason about**
- [ ] Optimizer: AdamW, warmup, cosine/linear decay, why LR is much lower than pretraining
- [ ] Mixed precision: bf16 vs fp16, loss scaling, where fp32 master weights live
- [ ] Gradient accumulation, gradient checkpointing, and their compute/memory trade
- [ ] Parallelism: data, tensor, pipeline, FSDP/ZeRO stages — what each shards
- [ ] Memory math: given N params, estimate training memory (weights + grads + optimizer states + activations)

## The one derivation to have ready

Estimate the memory to full-finetune a 7B model in bf16 with AdamW:

```
weights (bf16)          2 bytes/param  → 14 GB
gradients (bf16)        2 bytes/param  → 14 GB
AdamW m, v (fp32)       8 bytes/param  → 56 GB
fp32 master weights     4 bytes/param  → 28 GB
                                        ─────────
                                        ~112 GB + activations
```

Then explain what LoRA, ZeRO-3, and 8-bit optimizers each remove from that
table. This calculation comes up constantly and doing it fluently is a strong
signal.

## Notes

_Add your own notes and worked derivations here._
