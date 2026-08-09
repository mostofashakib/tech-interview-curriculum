# Data

Most post-training work is data work. Interviewers weight this heavily because
it separates people who have run training jobs from people who have read about
them.

**Notes in this folder:**
[synthetic-data-and-rubrics.md](synthetic-data-and-rubrics.md) — capability
taxonomies, constraint-loaded generation, rubric design with a worked production
example, and judge-based filtering.

## Checklist

**Sourcing**
- [ ] Human-written demonstrations: cost, throughput, annotator quality control
- [ ] Synthetic generation: self-instruct, Evol-Instruct, distillation from a stronger model
- [ ] Model-in-the-loop: rejection sampling / best-of-n against a reward model or verifier
- [ ] Licensing and provenance — what you are actually allowed to train on

**Quality**
- [ ] Filtering: heuristic rules, perplexity filters, classifier-based, LLM-as-filter
- [ ] Deduplication: exact hashing, MinHash/LSH near-dup, semantic dedup via embeddings
- [ ] Diversity: why 10k diverse examples beat 500k near-duplicates (LIMA-style arguments)
- [ ] Difficulty and length distribution — and how they leak into model behavior

**Mixing**
- [ ] Domain mixture ratios and how to tune them
- [ ] Replay / rehearsal to prevent catastrophic forgetting of pretraining ability
- [ ] Safety data ratio, and the over-refusal cost of setting it too high

**Contamination**
- [ ] N-gram overlap detection against eval sets
- [ ] Why decontamination is harder than it looks (paraphrase, translation, reformatting)
- [ ] Canary strings and held-out eval discipline

## Questions to be ready for

- You have 1M raw examples and budget to train on 50k. How do you choose?
- Your model regressed on math after an SFT run. Walk me through diagnosing it.
- How do you build a preference dataset from scratch with 10 annotators?
- How would you detect that a vendor delivered LLM-generated data labeled as human?
- Distillation from a stronger model works well on benchmarks but the model
  feels worse in chat. What's happening?

## Notes

_Add your own notes here._
