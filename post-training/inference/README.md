# Inference

Post-training decisions are constrained by what you can afford to serve. Expect
systems-flavored questions here — this is where the SWE half of your background
pays off.

## Checklist

**Decoding**
- [ ] Greedy, beam, temperature, top-k, top-p, min-p — and their effect on eval scores
- [ ] Repetition and frequency penalties, and why they're blunt instruments
- [ ] Structured/constrained decoding: grammars, JSON schemas, logit masking
- [ ] Best-of-n and self-consistency as inference-time compute scaling

**Serving mechanics**
- [ ] KV cache: size formula, why it dominates memory at long context
- [ ] Prefill vs decode — compute-bound vs memory-bandwidth-bound, and why they're
      scheduled differently
- [ ] Continuous batching and why it beats static batching so decisively
- [ ] PagedAttention and KV cache fragmentation
- [ ] Prefix caching for shared system prompts
- [ ] Speculative decoding: draft model, verification, acceptance rate, expected speedup

**Compression**
- [ ] Quantization: INT8, INT4, FP8, GPTQ/AWQ, weight-only vs weight-and-activation
- [ ] Where quantization hurts most (long-context reasoning, not short QA)
- [ ] Distillation into a smaller student
- [ ] Pruning and sparsity, and why they underdeliver in practice

**Economics**
- [ ] Time-to-first-token vs inter-token latency — which users actually feel
- [ ] Throughput/latency/cost triangle
- [ ] Estimating tokens/sec/GPU from memory bandwidth

## The KV cache math to have ready

```
KV bytes = 2 (K and V) × layers × kv_heads × head_dim × seq_len × batch × dtype_bytes
```

For a 70B-class model (80 layers, 8 KV heads via GQA, head_dim 128) in fp16 at
32k context, per sequence:

```
2 × 80 × 8 × 128 × 32768 × 2 bytes ≈ 10.7 GB
```

Per *sequence*. Then explain what GQA already saved you (versus 64 KV heads),
and what KV quantization would save next. This calculation is the fastest way to
show you understand why serving long context is hard.

## Questions to be ready for

- Why is prefill compute-bound and decode memory-bound?
- Your p99 latency is fine but throughput is terrible. Where do you look?
- When does speculative decoding *not* help?
- You must cut serving cost 50% with minimal quality loss. What's your order of operations?

## Notes

_Add your own notes here._
