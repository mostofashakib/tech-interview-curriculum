# LLM Evaluation & Benchmarks

> Notes from [LLM Evaluation & Benchmark](https://www.mostofashakib.com/blog/llm_evaluation).

## The framing that matters most

"Evaluation" is five different problems that get conflated:

1. **Output quality** — is the response any good?
2. **Correctness** — is it factually right and grounded in evidence?
3. **Reliability** — is it consistent across reruns, phrasings, and orderings?
4. **System constraints** — does it hold up under real latency, cost, and load?
5. **Metric integrity** — does the number reflect genuine improvement?

Point 5 is the one people skip. **A number going up does not mean the model got
better** — it may mean the model got better at the metric. Every eval discussion
should begin by naming which of the five you're actually solving.

---

## The six-step framework

| Step | What you do | Failure if skipped |
|---|---|---|
| 1. Task definition | Turn a vague goal into a measurable objective | You measure something adjacent to what you care about |
| 2. Define success | State the criteria explicitly: correctness, usefulness, latency | Disagreement about whether you passed |
| 3. Choose method | Match methodology to task structure | Reference metrics on open-ended tasks |
| 4. Dataset design | Build test sets weighted toward edge cases | Great scores, bad product |
| 5. Reliability | Validate that the metric is stable under perturbation | You chase noise |
| 6. Failure analysis | Cluster and inspect errors | You know the score but not the fix |

Step 6 is where the value is. A score tells you *whether*; failure analysis tells
you *what to generate next* — feeding straight back into
[../data/synthetic-data-and-rubrics.md](../data/synthetic-data-and-rubrics.md).

---

## Five kinds of evaluation

| Method | What it does | Use when |
|---|---|---|
| Reference-based | Compare output to ground-truth text | Constrained outputs with a real reference |
| Human evaluation | Raters score against a rubric | Calibration and benchmark creation |
| LLM-as-judge | A model scores other models | Scale, open-ended tasks |
| Task-based | Did the workflow actually complete? | Agents, tool use |
| Benchmark | Standard public datasets | Comparability, regression tracking |

### Reference-based metrics

| Metric | Basis | Strength | Weakness |
|---|---|---|---|
| **BLEU** | N-gram **precision** | Fast, automated, good for constrained output | Ignores meaning; punishes paraphrase; pushes models to be conservative |
| **ROUGE** | **Coverage/recall** of the reference | Useful for summarization | Rewards verbosity; encourages extractive copying |
| **METEOR** | Synonym matching, balanced P/R | More forgiving of paraphrase | Still reference-bound; useless for reasoning |

**The hard limitation**: reference metrics measure *similarity*, not *quality*.
They cannot evaluate instruction adherence, hallucination, tool correctness,
validity of a reasoning chain, or policy compliance. And because they measure
similarity, optimizing against them produces models that hedge toward the
average phrasing — gaming, not improvement.

### Human evaluation

The highest-nuance signal, and the most expensive. What makes it work:

- Clear rubrics, rater training, gold examples, an adjudication process for
  disagreements
- **Inter-rater agreement computed and reported** — low agreement means your
  criteria are ambiguous, not that your raters are bad

Because of cost, reserve humans for **calibration and benchmark creation**, then
scale with judges calibrated against that human data.

### LLM-as-judge

Scalable and flexible, but carries bias and calibration problems, and requires
**meta-evaluation — you must evaluate the judge.** Full treatment in
[llm-as-a-judge.md](llm-as-a-judge.md).

---

## Eleven evaluation dimensions

Score these separately. A single blended number hides everything.

| # | Dimension | Question |
|---|---|---|
| 1 | Correctness | Is the answer right? |
| 2 | Factuality | Are the claims true and evidence-grounded? |
| 3 | Completeness | Is anything essential missing? |
| 4 | Instruction following | Format, scope, constraints, tone respected? |
| 5 | Relevance | Does it address the actual question? |
| 6 | Clarity | Is it intelligible and well-organized? |
| 7 | Conciseness | Is there padding? |
| 8 | Reasoning quality | Is the multi-step logic coherent? |
| 9 | Safety | Harmful or prohibited content avoided? |
| 10 | Tool correctness | Right tool, right arguments, output read correctly, failures recovered? |
| 11 | Groundedness | Are claims tied to source material? |

---

## Quantifying factuality

Don't score "is this factual" holistically. **Decompose into atomic claims**, then
classify each one:

| Category | Meaning |
|---|---|
| **Supported** | Verified against available evidence |
| **Unsupported** | Not verified, but not contradicted either |
| **Contradicted** | Conflicts with the evidence |
| **Unverifiable** | Cannot be assessed given what's available |
| **Irrelevant** | Outside the scope of evaluation |

Then aggregate: proportion supported, contradiction rate, unsupported rate,
evidence coverage.

The five-way split matters. Collapsing *unsupported* and *contradicted* into
"wrong" is the most common mistake — they call for completely different fixes.
Unsupported is a retrieval or citation problem; contradicted is a hallucination
problem.

**Citation verification**: separately check that a cited passage actually supports
the claim attached to it. Models cite real sources for claims those sources don't
make. In high-stakes settings, pair LLM judgment with deterministic checks.

---

## Benchmarks

| Benchmark | Measures | Caveat |
|---|---|---|
| **MMLU** | Broad academic knowledge, multiple choice | Saturating; weak predictor of practical usefulness |
| **AIME** | Hard symbolic math reasoning | Narrow; unrepresentative of daily use |
| **PIQA** | Physical-world commonsense | Narrow slice of reasoning |
| **SWE-Bench** | Resolving real issues in real repositories | Tests genuine task completion, not style |
| **HarmBench** | Safety under adversarial/harmful prompts | Resistance to unsafe instructions |
| **TAU-Bench** | Agent behavior in tool-rich settings with user interaction | Surfaces failures QA benchmarks never see |

The progression to notice: **MMLU → SWE-Bench → TAU-Bench** tracks the field
moving from *knowledge recall* to *task completion* to *multi-turn agentic
behavior*. Being able to narrate that shift is a strong interview signal.

---

## Reliability and consistency

Measure and report:

- Run-to-run variance
- Inter-judge agreement
- Alignment with human labels
- Order sensitivity
- Rubric adherence rate
- Schema compliance for structured outputs

If you can't state the variance, you can't defend a 1-point improvement.

---

## Analysis and attribution

**Slice analysis** — disaggregate by domain, difficulty, length, language,
condition. An average that improves while a slice regresses is the standard way
a model ships broken. **Failure taxonomies beat aggregate scores.**

**Root-cause attribution** — trace failure clusters back to a dataset gap or a
rubric deficiency, then target the next synthetic data cycle at exactly that. This
closes the loop:

```
evaluate → cluster failures → attribute to data/rubric gap → generate → train → evaluate
```

---

## See also

- [llm-as-a-judge.md](llm-as-a-judge.md) — judge design, biases, calibration
- [agentic-evaluation.md](agentic-evaluation.md) — trajectory-level evaluation
- [README.md](README.md) — the full evals checklist and question bank
