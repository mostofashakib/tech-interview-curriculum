# Preference Optimization

Pushing the model beyond imitation — optimizing directly for what people prefer.
This is the technical heart of the route and where the hardest questions land.

**Notes in this folder:**
[alignment-strategies-and-rl-algorithms.md](alignment-strategies-and-rl-algorithms.md)
— DPO vs RLHF vs RLVR (where the signal comes from), then TRPO vs PPO vs GRPO
(what consumes it), with the clipped objective, the KL penalty, the RLHF VRAM
wall, and a selection cheat sheet.

## Checklist

**The RLHF objective**
- [ ] `max_π E[r(x,y)] − β·KL(π ‖ π_ref)` — know every term and why the KL is there
- [ ] Reference policy = the SFT checkpoint; what happens as β → 0 and β → ∞
- [ ] Why KL is a constraint against reward hacking, not a regularizer for generalization

**PPO**
- [ ] Policy gradient → REINFORCE → actor-critic → PPO, and what each step fixes
- [ ] Clipped surrogate objective and what the clip prevents
- [ ] Value head, GAE, advantage normalization
- [ ] The four models in memory at once (policy, ref, RM, value) and the cost that implies
- [ ] Practical instability: KL spikes, value loss blowup, entropy collapse

**DPO**
- [ ] The key insight: the optimal RLHF policy has a closed form, so the reward can
      be reparameterized in terms of the policy — no RM, no rollouts
- [ ] Loss: `−log σ(β·log[π(y_w|x)/π_ref(y_w|x)] − β·log[π(y_l|x)/π_ref(y_l|x)])`
- [ ] Why it's offline, and what that costs you versus PPO
- [ ] Known pathology: DPO can lower the probability of *both* chosen and rejected
- [ ] Variants: IPO (fixes DPO's overfitting on deterministic prefs), KTO (no pairs
      needed), ORPO (merges SFT and preference into one stage), SimPO (reference-free)

**GRPO and the reasoning era**
- [ ] Group-relative advantage: sample G completions, use group mean/std as baseline
- [ ] Why dropping the value model matters at scale
- [ ] RLVR — verifiable rewards for math and code, no learned RM
- [ ] Long chain-of-thought and how RL elicits it
- [ ] Entropy collapse and diversity loss in long RL runs

**Cross-cutting**
- [ ] Online vs offline vs iterative-offline, and why online generally wins
- [ ] Reward hacking taxonomy: length, formatting, sycophancy, refusal-gaming,
      test-case gaming, judge manipulation
- [ ] Constitutional AI / RLAIF — replacing human feedback with model feedback
- [ ] Best-of-n and rejection sampling as an inference-time alternative to RL

## The derivation to have ready

The optimal solution to the KL-constrained objective is:

```
π*(y|x) = (1/Z(x)) · π_ref(y|x) · exp(r(x,y)/β)
```

Rearranging for the reward:

```
r(x,y) = β·log[π*(y|x) / π_ref(y|x)] + β·log Z(x)
```

Substitute into the Bradley-Terry loss. `Z(x)` depends only on `x`, so it
cancels in the difference — and you have DPO, with no reward model anywhere.

Being able to run this derivation cleanly is close to a rite of passage for
post-training interviews. Practice it on paper until it's automatic.

## Questions to be ready for

- Derive DPO from the RLHF objective. (Expect this.)
- When would you pick PPO over DPO, given DPO is simpler and cheaper?
- Your KL is exploding at step 300. Diagnose it.
- Reward goes up, human eval goes down. What now?
- Why does GRPO drop the value model, and what do you lose?
- Design an RL setup for a model that must be good at math *and* stay a pleasant
  conversationalist.

## Video courses

- [Stanford CS329H — Machine Learning from Human Preferences](https://www.youtube.com/playlist?list=PLoROMvodv4rNm525zyAObP4al43WAifZz)
  (Autumn 2024) — the course for this folder. Preference data, reward models,
  RLHF and its alternatives, taught as an open research area rather than a
  recipe, which is where the honest answers about failure modes come from.
- [Stanford CS224R — Deep Reinforcement Learning](https://www.youtube.com/playlist?list=PLoROMvodv4rPwxE0ONYRa_itZFdaKCylL)
  — the RL that PPO, TRPO, and GRPO are built on. Worth the time if policy
  gradients still feel like a formula you memorized rather than something you
  can derive on a whiteboard.

## Notes

_Add your own notes here._
