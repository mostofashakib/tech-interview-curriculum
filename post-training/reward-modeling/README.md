# Reward Modeling

Learning a scalar proxy for human judgment, so preference optimization has
something to optimize against.

## Checklist

**Preference data**
- [ ] Pairwise comparisons vs ratings vs rankings — why pairwise dominates
- [ ] Annotator agreement rates (typically 60–75%) and what that ceiling implies
- [ ] Where preference data comes from: paid annotators, production thumbs, synthetic
- [ ] Tie handling and confidence-weighted preferences

**The model**
- [ ] Architecture: base LM + scalar head, initialized from the SFT checkpoint
- [ ] Bradley-Terry: `P(y_w ≻ y_l | x) = σ(r(x,y_w) − r(x,y_l))`
- [ ] Loss: `L = −E[log σ(r(x,y_w) − r(x,y_l))]`
- [ ] Why reward is shift-invariant, and why that's fine for RLHF but not for thresholding
- [ ] Reward model accuracy as an eval, and why high accuracy ≠ good downstream RLHF

**Failure modes**
- [ ] Length bias — the single most reliable reward-model pathology
- [ ] Sycophancy: rewarding agreement over correctness
- [ ] Formatting bias: markdown, bullets, headers scoring high regardless of content
- [ ] Overoptimization: reward keeps climbing while true quality falls (Goodhart)
- [ ] Distribution shift as the policy drifts away from the RM's training data

**Alternatives and extensions**
- [ ] Process reward models (PRM) vs outcome reward models (ORM) for reasoning
- [ ] Verifiable rewards: unit tests, math checkers, no learned RM at all (RLVR)
- [ ] LLM-as-judge as a reward signal, and its self-preference bias
- [ ] Rule-based / constitutional reward signals

## The derivation to have ready

From Bradley-Terry, the probability that `y_w` beats `y_l`:

```
P(y_w ≻ y_l | x) = exp(r(x,y_w)) / (exp(r(x,y_w)) + exp(r(x,y_l)))
                 = σ(r(x,y_w) − r(x,y_l))
```

Maximum likelihood over a preference dataset D gives the training loss directly.
Being able to go from "humans compare two answers" to that loss in three lines
is a standard whiteboard ask, and it sets up the DPO derivation next door.

## Questions to be ready for

- Your RM scores longer answers higher regardless of quality. Fix it. (Give at
  least three approaches: length-penalized reward, length-balanced pairs,
  debiasing at the data level.)
- RM eval accuracy is 78% but RLHF makes the model worse. What do you check?
- When would you skip the reward model entirely?
- Design a reward signal for a coding assistant.

## Notes

_Add your own notes here._
