# Agentic Evaluation

> Notes from [LLM Evaluation & Benchmark](https://www.mostofashakib.com/blog/llm_evaluation).

Evaluating sequential decision-making rather than single responses. The unit of
evaluation is the **trajectory**, not the answer.

## What changes

A single-turn eval asks "is this output good?" An agent eval asks about tool
selection, state management across steps, error recovery, and knowing when to
stop. **An agent can reach the right answer through a broken process, and that
process will fail on the next task.** Final-answer accuracy alone hides this
completely.

## Metrics beyond the final answer

| Metric | What it catches |
|---|---|
| Step success rate | Where in the trajectory things break |
| Tool selection accuracy | Wrong tool for the job |
| Argument validity | Right tool, malformed call |
| Output interpretation accuracy | Correct call, misread result |
| Recovery success rate | Behavior after a failure |
| Unnecessary call frequency | Cost and latency waste; flailing |

**Recovery rate is the most underrated of these.** Real environments fail
constantly. An agent that never recovers is unusable regardless of its
happy-path score.

## Test under adverse conditions

Don't only evaluate the clean path. Deliberately inject:

- Ambiguous instructions
- Missing or unavailable tools
- Unreliable / flaky tool performance
- Confusing or inconsistent APIs
- Contradictory signals
- Timeouts

This maps directly onto RL environment design — see
[../rl-environments/](../rl-environments/). The perturbations you evaluate under
are the perturbations you should train under.

---

## Five common failure modes

### 1. Route error
**What**: picks the wrong subworkflow or strategy.
**Causes**: ambiguous directives, weak tool descriptions, poor scaffolding.
**Fix**: clearer routing criteria, better tool documentation, targeted examples.

### 2. Hallucinating non-existent tools
**What**: invents function names or tools that aren't available.
**Causes**: large tool space, inconsistent naming, over-reliance on learned patterns.
**Fix**: explicit available-tool lists, simplified naming, mandatory validation before execution.

### 3. Unclear instructions
**What**: misinterprets an ambiguous user request.
**Causes**: no defined policy for when to ask for clarification or what to assume.
**Fix**: define clarification triggers, establish assumption protocols, test on deliberately ambiguous cases.

### 4. Poor API design
**What**: struggles with semantically inconsistent tool interfaces.
**Causes**: illogical or inconsistent naming across APIs.
**Fix**: semantic clarity, typed schemas, example calls, consistent argument patterns.

### 5. No response from tool call
**What**: the tool returns silence or times out.
**Causes**: infrastructure failure, or no detection of the failure at all.
**Fix**: return explicit error states, make the agent timeout-aware, intelligent retry policy, escalation path.

> Look at the fixes: **three of the five are fixed outside the model.** Better tool
> names, typed schemas, explicit error states. This is the most important
> practical insight in agentic evaluation — a large share of "the agent is dumb"
> is actually "the environment is badly designed." Say this in an interview.

---

## Remediation strategy

| Lever | Action |
|---|---|
| **Observability** | Log full traces — you cannot debug what you didn't record |
| **Tool design** | Clear naming, typed arguments |
| **Instruction design** | Explicit decision policies, not vibes |
| **Targeted training** | Train on the failure-mode clusters you found |
| **Evaluation coverage** | Include messy scenarios alongside ideal ones |
| **Recovery scoring** | Explicitly measure behavior after failure |

## Related benchmarks

- **TAU-Bench** — agent behavior in tool-rich environments with user interaction
- **SWE-Bench** — resolving real repository issues end-to-end

## Questions to be ready for

- Your agent has 70% task success. What do you look at next?
- How do you tell a model problem from a tool-design problem?
- Design an eval suite for a customer-support agent with 20 tools.
- How do you score an agent that reached the right answer by luck?
- What do you log to make agent failures debuggable after the fact?
