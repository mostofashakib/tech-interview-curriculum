# Supervised Fine-Tuning (SFT)

Teaching a base model the *format* of being an assistant. Also called
instruction tuning. The cheapest, highest-leverage stage of post-training.

**Notes in this folder:**
[sft-lora-and-quantization.md](sft-lora-and-quantization.md) — behavioral
cloning framing, TRL/Unsloth/vLLM tooling, LoRA and QLoRA mechanics, and the
full-vs-PEFT decision with memory math.

## Checklist

**Objective**
- [ ] Same cross-entropy as pretraining, restricted to assistant tokens
- [ ] Prompt masking: why you zero the loss on user turns, and when you don't
- [ ] Why SFT alone plateaus — it can only imitate, never exceed, its demonstrations

**Chat templates**
- [ ] Special tokens, role markers, turn boundaries, EOS/EOT handling
- [ ] System prompts: training with vs without, and generalization to unseen ones
- [ ] Template mismatch between training and inference — a top source of silent bugs
- [ ] Multi-turn: loss on every assistant turn vs only the last

**Mechanics**
- [ ] Sequence packing and why you need block-diagonal attention masks to do it right
- [ ] Padding vs packing, throughput impact
- [ ] Epochs: why 1–3 is typical and what overfitting looks like (verbatim regurgitation, degraded diversity)
- [ ] Learning rate selection; why it's ~10–100x lower than pretraining

**Parameter-efficient fine-tuning**
- [ ] LoRA: low-rank decomposition ΔW = BA, rank r, alpha scaling, which modules to target
- [ ] QLoRA: NF4 quantization, double quantization, paged optimizers
- [ ] When full fine-tuning genuinely beats LoRA, and when it doesn't
- [ ] Adapter merging and serving many adapters from one base model

**Variants worth knowing**
- [ ] Rejection-sampling fine-tuning (RFT) / best-of-n distillation
- [ ] Self-distillation and iterative SFT rounds
- [ ] Long-context extension as a post-training stage (RoPE scaling + long-doc SFT)

## The LoRA math to have ready

For a frozen weight `W ∈ R^(d×k)`, LoRA learns `ΔW = BA` where `B ∈ R^(d×r)`,
`A ∈ R^(r×k)`, `r ≪ min(d,k)`. Trainable params drop from `d·k` to `r(d+k)`.

Forward pass: `h = Wx + (α/r)·BAx`. `A` is initialized random-normal, `B` is
initialized to zero — so `ΔW = 0` at step 0 and training starts from the exact
base model. Be ready to explain why that initialization asymmetry matters.

## Questions to be ready for

- Why mask the loss on prompt tokens? What breaks if you don't?
- Your SFT model won't stop generating. Name three causes.
- Pick a LoRA rank for a 70B model on 50k examples. Justify it.
- Users report the model is more confident but less accurate after SFT. Why?

## Notes

_Add your own notes here._
