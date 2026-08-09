# Evals

"How would you know if this worked?" is the most common question in
post-training interviews. Have a real answer.

**Notes in this folder:**

- [llm-evaluation.md](llm-evaluation.md) — the five evaluation problems, the
  six-step framework, reference metrics and their limits, the eleven dimensions,
  factuality via atomic claims, and the benchmark landscape
- [llm-as-a-judge.md](llm-as-a-judge.md) — the seven biases and their fixes,
  calibration, pointwise vs pairwise, structured-output schemas and enforcement
- [agentic-evaluation.md](agentic-evaluation.md) — trajectory-level metrics, the
  five agent failure modes, and remediation

## Checklist

**Benchmark types**
- [ ] Knowledge/reasoning: MMLU-style multiple choice and its ceiling problems
- [ ] Math and code: GSM8K, MATH, HumanEval/MBPP — verifiable, hence valuable
- [ ] Instruction following: IFEval and constraint-satisfaction style evals
- [ ] Chat quality: arena-style head-to-head, MT-Bench
- [ ] Safety: refusal rate, over-refusal, jailbreak robustness, red-team suites
- [ ] Long-context: needle-in-a-haystack and its known weaknesses as a proxy

**Methodology**
- [ ] Log-likelihood scoring vs generative scoring, and why they disagree
- [ ] Prompt sensitivity — a few words of formatting can move a score several points
- [ ] pass@k vs pass@1, and when each is the honest metric
- [ ] Temperature and sampling settings as part of the eval definition
- [ ] Confidence intervals; how many samples you need to call a 1-point difference

**LLM-as-judge**
- [ ] Position bias and the swap-and-average fix
- [ ] Self-preference bias — judges favor their own family's outputs
- [ ] Verbosity bias
- [ ] Calibrating against human agreement before trusting a judge at all
- [ ] Rubric design and grading with reference answers

**Human eval**
- [ ] Pairwise preference collection, win rate, ties
- [ ] Inter-annotator agreement and what an acceptable floor looks like
- [ ] Cost and latency, and why it forces you to use automated proxies

**Practice**
- [ ] Held-out sets and contamination hygiene
- [ ] Regression suites — catching what a new checkpoint broke
- [ ] Capability vs safety trade-off curves
- [ ] Production signals: thumbs, retry rate, conversation length, escalation rate

## Questions to be ready for

- Design an eval suite for a new instruct model from scratch. Budget: two weeks.
- MMLU is up 2 points and users say the model got worse. Reconcile that.
- How do you evaluate a model that's better than your best annotator?
- How do you tell contamination from genuine capability gain?
- Your judge model rates checkpoint B higher; how much do you trust it and what
  would change your mind?

## Notes

_Add your own notes here._
