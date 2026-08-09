# Synthetic Data Generation & Rubric Design

> Notes from [Post-Training LLMs](https://www.mostofashakib.com/blog/post-training-llms).

Post-training runs on data you manufacture. Three sub-problems: deciding *what*
scenarios to generate, defining *what good looks like*, and *filtering* what
comes back.

---

## 1. Scenario / dataset design

Build a **structured taxonomy of capabilities** first, then generate against it.
Generating without a taxonomy gets you 50k variations of the same easy prompt.

Prompts should be **specific and constraint-loaded**, not generic. Compare:

- ❌ "Write a coding question."
- ✅ "Generate a Python debugging scenario involving a circular import between
  three modules, where the fix requires restructuring rather than a local patch."

The second produces a usable training example; the first produces noise.

**Deliberately cover the long tail.** The head of the distribution is already
handled by pretraining. The value of synthetic data is in the edge cases:
ambiguous requests, adversarial phrasings, multi-constraint tasks, cases where
the correct answer is "I need more information."

## 2. Rubric design

A rubric is a set of **independent grading dimensions**, each scored separately.
Independence matters — one blended "quality" score is unlearnable and
undebuggable.

Typical dimensions: conciseness, safety, logic/correctness, formatting.
Scales range from binary (0–1) to graded (0–5) depending on the dimension.

### Example: production rubric for a coding assistant

| Dimension | Scale | Rule |
|---|---|---|
| Format compliance | 0–1 | Does the output use the required XML structure? Binary. |
| Conciseness | penalty | −2 to −3 for unnecessary apologies or padding explanations |
| Logic / optimization | 1–5 | Graded on time complexity of the proposed solution |
| Security | 0–1 | Binary check for known unsafe patterns |

Two things to notice, both generalizable:

- **Binary where binary is honest.** Format compliance and security have a right
  answer. Forcing them onto a 1–5 scale invents disagreement.
- **Penalties, not just scores.** Conciseness is expressed as a deduction, which
  encodes "this is a defect to remove" rather than "this is a virtue to maximize."
  That framing prevents the model from over-optimizing terseness.

## 3. Data quality filtering: LLM-as-a-judge

Use a judge model as the gate that stops low-quality synthetic data from
entering the training set. This is the highest-leverage use of a judge — cheap,
scalable, and applied where a false positive costs one discarded example rather
than a wrong shipping decision.

The rubric you wrote in step 2 *is* the judge prompt. Same artifact, two uses:
filtering data going in, and scoring outputs coming out.

See [../evals/llm-as-a-judge.md](../evals/llm-as-a-judge.md) for prompt
construction, bias mitigation, and calibration.

---

## The loop

```
taxonomy → generate → judge/filter → train → evaluate → find blind spots
    ↑                                                          │
    └──────────────────────────────────────────────────────────┘
```

Evaluation isn't the end of the pipeline — it's what tells you which part of the
taxonomy to generate against next. See [../evals/](../evals/).

## Questions this section answers

- "How do you build a post-training dataset from nothing?" → taxonomy first, then
  constrained generation, then judge-filtering.
- "How do you keep synthetic data from collapsing into repetition?" → taxonomy
  coverage plus long-tail targeting plus dedup.
- "How do you decide what to generate next?" → failure analysis from evals feeds
  back into the taxonomy.
