# LLM as a Judge

> Notes from [LLM as a Judge](https://www.mostofashakib.com/blog/llm_as_a_judge).

Using a model to evaluate model outputs, for the large space of tasks where
exact matching and reference metrics don't capture quality.

---

## When to use one

**Good fit** — open-ended generation with many valid answers:
chatbot helpfulness, explanation quality, summarization, style-controlled
generation, pairwise comparison. Anything needing fine-grained rubrics across
several dimensions.

**Requires backup** — domains where correctness is expert-determined or
machine-checkable: math, law, medicine, code execution, fact-grounded QA. Use the
judge as **one layer**, combined with deterministic checks, tool-based
verification, or human experts.

> The rule: a judge is an *evaluator of quality*, not an *oracle of truth*. When a
> verifier exists, the verifier wins.

## What makes a good judge

- Genuine task understanding
- Consistent rubric adherence
- Stability across prompt variations
- Calibration against human raters
- **Independence from superficial signals** — length, tone, confidence, formatting

That last one is the whole ballgame, and it's what the bias list below is about.

## What judges are bad at

- Hidden factual errors
- Subtle logical mistakes
- Domain-specific technical accuracy
- Long agent traces with many tool calls
- Anything under an underspecified rubric

Note the shared cause: a judge evaluates what it can *see* in the text. An error
that requires independent verification to detect is invisible to it. A confident,
well-formatted, wrong answer is the judge's blind spot by construction.

---

## The seven biases

| # | Bias | What happens | Mitigation |
|---|---|---|---|
| 1 | **Position** | Favors whichever answer came first (or second), regardless of merit | Randomize order; score both arrangements and compare for consistency |
| 2 | **Verbosity** | Longer answers score higher | Instruct explicitly against rewarding length; normalize for length; measure quality-per-content |
| 3 | **Self-enhancement** | Prefers outputs matching its own style and reasoning | Judge with a different model family; ensemble multiple judges; strip identifying metadata |
| 4 | **Formal tone** | Authoritative-sounding answers win despite weak substance | Anchor scoring to factual accuracy and reasoning depth, not register |
| 5 | **Formatting** | Bullets and clean structure inflate scores independent of accuracy | Score correctness first; credit formatting only where it genuinely aids comprehension |
| 6 | **Confidence** | Assertive answers beat appropriately hedged ones | Prioritize correctness and justification, especially in ambiguous domains |
| 7 | **Refusal** | Over-rewards safe-sounding refusals, under-penalizes subtle harm | Explicit safety criteria; distinguish warranted refusal from unnecessary avoidance |

**Position bias is the one to fix first** — it's the largest effect, and the fix
(swap and average) is nearly free.

Biases 2, 4, 5, and 6 are one family: **the judge rewards the appearance of
quality.** They share a mitigation — force the rubric to be about substance and
say out loud in the prompt which surface features must not count.

---

## Aligning a judge

1. Replace vague rubrics with **concrete descriptions of good and bad** on each dimension
2. Provide **calibrated examples** — high- and low-quality answers, pre-scored
3. **Name the distortions to avoid** in the prompt: verbosity, polish, unjustified confidence, decorative formatting
4. **Decompose into dimensions** rather than asking for one overall score
5. **Validate against human judgments** on a calibration set
6. **Test stability**: randomize answer order, vary prompt wording, rerun repeatedly

Step 5 is the non-negotiable one. An uncalibrated judge is an unmeasured
instrument; you cannot interpret its output at all.

---

## Pointwise vs pairwise

| | Pointwise | Pairwise |
|---|---|---|
| **Task** | Score one answer against a rubric | Pick the better of two |
| **Output** | Absolute scores, pass/fail | Winner / tie |
| **Reliability** | Harder — the judge must invent an internal scale | Easier, generally more reliable |
| **Best for** | Longitudinal monitoring, error analysis, thresholds | Model ranking, A/B tests, preference-data generation |
| **Subtle differences** | Often missed | Detected well |

Practical split: **pairwise when comparing, pointwise when tracking.** You can't
watch quality over time with pairwise (no absolute anchor), and you can't reliably
resolve small gaps with pointwise.

Note the connection to [../reward-modeling/](../reward-modeling/): pairwise judging
produces exactly the preference pairs a reward model trains on. The same
component can serve evaluation and RLAIF data generation.

---

## Structured output

Judges must emit **strict JSON**, not prose. Free-form explanations can't be
aggregated, compared, or regression-tested.

**Pointwise schema:**

```json
{
  "correctness": 0,
  "factuality": 0,
  "completeness": 0,
  "instruction_following": 0,
  "conciseness": 0,
  "overall_score": 0.0,
  "final_verdict": "pass",
  "failure_tags": ["hallucination"],
  "rationale": "brief explanation"
}
```

- Dimension scores: 0–5 each
- `overall_score`: float
- `final_verdict`: `pass` | `fail`
- `failure_tags`: enum array — `hallucination`, `missing_info`,
  `instruction_violation`, `verbosity`, `other`
- `rationale`: short, and **last** — so it doesn't rationalize the scores into existence

**Pairwise schema:**

```json
{
  "winner": "A",
  "reasoning": "comparative explanation",
  "dimension_scores": {
    "correctness":  { "A": 0, "B": 0 },
    "completeness": { "A": 0, "B": 0 }
  }
}
```

- `winner`: `A` | `B` | `tie`
- `dimension_scores`: per-dimension scores for both answers

### Enforcing the schema — four layers

1. **Prompt-level** — state the schema and require strict JSON
2. **Schema-constrained decoding** — enforce at the API/decoder level so invalid tokens can't be sampled
3. **Programmatic validation** — check fields, ranges, enums; reject and retry on failure
4. **Deterministic postprocessing** — normalize values, handle nulls, version the schema

Layer 1 alone is not enforcement, it's a request. Interviewers like this
distinction because it separates people who've run judges in production from
people who've prompted one.

---

## Questions to be ready for

- Your judge rates checkpoint B higher. How much do you trust it, and what would change your mind?
- Name four judge biases and their fixes.
- Pointwise or pairwise for building a preference dataset? Why?
- How do you evaluate the judge itself?
- Your judge and your human raters disagree 30% of the time. What now?
- Why not just use a judge for math grading?
