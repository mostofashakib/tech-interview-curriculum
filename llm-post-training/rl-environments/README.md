# RL Environments

Where the model actually *does* something and gets scored for it. As post-training
shifted from static preference pairs toward RL on verifiable and agentic tasks,
the environment became the bottleneck — and one of the most in-demand skill sets
at AI labs right now.

The short version of why: **the algorithm is mostly solved and the reward signal
is mostly not.** GRPO is a page of math. Building an environment where the reward
means what you want it to mean is months of work.

---

## The mental model

```
        ┌──────────── policy (the LLM) ────────────┐
        │                                          │
   observation                                  action
        │                                          │
        └──── environment: state, tools, verifier ─┘
                            │
                          reward
```

Classic RL: state → action → reward, with an environment holding the state.
LLM RL keeps the shape but changes the pieces:

| Classic RL | LLM post-training |
|---|---|
| State | Conversation + tool outputs + retrieved context |
| Action | A generated token, turn, or tool call |
| Episode | One prompt → response, or a full agent trajectory |
| Reward | Verifier result, reward model score, or rubric judgment |
| Reset | New prompt sampled from the task distribution |

---

## Checklist

**Environment types**
- [ ] **Single-turn verifiable** — math with a checker, code with unit tests. Simplest and most productive.
- [ ] **Multi-turn conversational** — the reward depends on the whole dialogue
- [ ] **Tool-use / function-calling** — model calls tools, environment returns results
- [ ] **Code execution sandboxes** — run generated code, capture output, tests, and stack traces
- [ ] **Computer/browser use** — GUI or DOM state as observation
- [ ] **Games and simulators** — clean rewards, useful for studying RL dynamics
- [ ] **Self-play and debate** — the opponent is part of the environment

**Interface design**
- [ ] Gym-style contract: `reset()`, `step(action) → (obs, reward, done, info)`
- [ ] Observation format: what the model actually sees, and its token budget
- [ ] Action space: free text vs constrained/structured tool calls
- [ ] Episode termination: success, failure, step limit, timeout
- [ ] Statelessness and reproducibility — same seed, same episode

**Reward design**
- [ ] Verifiable rewards: unit tests, symbolic checkers, schema validators, exact match
- [ ] Sparse (final outcome only) vs dense (per-step) rewards
- [ ] **Outcome reward models (ORM) vs process reward models (PRM)** — score the answer vs score each reasoning step
- [ ] Partial credit and graded rewards
- [ ] Penalties: length, invalid tool calls, wasted steps, unsafe actions
- [ ] Reward shaping, and how it introduces unintended optima
- [ ] Multi-objective rewards and how to weight them

**Infrastructure**
- [ ] Sandboxing and isolation — you are executing model-generated code
- [ ] Parallel rollouts; environment throughput as the training bottleneck
- [ ] Determinism, seeding, and snapshot/restore
- [ ] Latency budget — a slow environment starves the trainer
- [ ] Handling flaky tools and external API failures without corrupting the reward
- [ ] Caching and replay of expensive environment steps

**Task distribution**
- [ ] Difficulty curriculum — too easy gives no gradient, too hard gives no signal
- [ ] Coverage over a capability taxonomy (same discipline as [../data/](../data/))
- [ ] Held-out environments to detect environment overfitting
- [ ] Automatic task generation and difficulty calibration

**Failure modes** — the section interviewers probe hardest
- [ ] **Reward hacking** — exploiting the verifier instead of solving the task
- [ ] **Verifier gaming** — writing code that special-cases the tests
- [ ] **Sparse reward collapse** — nothing ever succeeds, so nothing is learned
- [ ] **Entropy collapse** — the policy narrows to one strategy and stops exploring
- [ ] **Environment overfitting** — great in-env, useless out of it
- [ ] **Length exploitation** — padding reasoning because longer correlates with reward
- [ ] **Distribution shift** — the environment no longer matches how the policy behaves

---

## Why GRPO and environments fit together

Group-relative advantage needs **score spread within a group** of sampled
responses. A verifiable environment produces exactly that: sample 8 solutions,
3 pass, 5 fail, and the advantage falls out with no value model.

That coupling explains the architecture of modern reasoning models. If you can
articulate it, you've understood why this folder exists. See
[../preference-optimization/alignment-strategies-and-rl-algorithms.md](../preference-optimization/alignment-strategies-and-rl-algorithms.md).

## The design rule

**Every environment is a specification of what you want, written in a language
the optimizer will read adversarially.** Assume the policy will find the cheapest
path to reward. Before you run training, ask: what's the laziest strategy that
scores well here? Then close it.

This is the same question as "how would you break your own eval," which is why
this folder and [../evals/agentic-evaluation.md](../evals/agentic-evaluation.md)
are two views of one skill. The adverse conditions you test under are the
conditions you should train under.

## Questions to be ready for

- Design an RL environment for training a model to fix GitHub issues. Cover
  reward, termination, and anti-gaming.
- Sparse vs dense reward for multi-step math — which, and why?
- Your model passes all unit tests but the code is obviously wrong. What happened,
  and how do you fix the environment?
- ORM vs PRM: when is per-step supervision worth the labeling cost?
- Your environment runs at 2 episodes/sec and the GPUs are idle. What do you do?
- How do you build a curriculum without hand-labeling difficulty?
- How do you know your model learned the task rather than the environment?

## Video courses

- [Build a Real-World Reinforcement Learning Environment](https://www.youtube.com/playlist?list=PL58zEckBH8fDtNs79K0tqxzPT6Zr3iqDZ)
  — a build-along, not a lecture series, and useful for exactly that reason. The
  design questions above get much easier to answer once you have had to choose a
  reward and a termination condition yourself and watched a model exploit both.

## Notes

_Add your own notes and environment designs here._
