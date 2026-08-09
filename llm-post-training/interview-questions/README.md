# Interview Questions

A question bank spanning the route. Work through these out loud, on a
whiteboard, against a timer. Write your answers into this folder as you go.

## Derivations (expect at least one)

1. Derive the DPO loss from the KL-constrained RLHF objective.
2. Derive the Bradley-Terry reward-model loss from pairwise preferences.
3. Write the PPO clipped surrogate objective and explain what the clip prevents.
4. Show the GRPO advantage estimate and explain why no value model is needed.
5. Estimate training memory for full fine-tuning an N-parameter model with AdamW in bf16.
6. Compute KV cache size for a given architecture, context length, and batch size.

## Conceptual

7. Why isn't SFT enough? What can preference optimization do that imitation can't?
8. What does the KL term in the RLHF objective actually buy you?
9. PPO vs DPO vs GRPO — pick one for a stated scenario and defend it.
10. What is reward hacking? Give four distinct mechanisms.
11. Explain the alignment tax. Is it avoidable?
12. Does post-training add capabilities or elicit existing ones? Argue both sides.
13. Why do RLHF'd models become sycophantic, and how would you counteract it?
14. When are verifiable rewards better than a learned reward model? When are they not enough?
15. Explain catastrophic forgetting in post-training and three mitigations.

## Debugging (the most predictive category)

16. Training loss is decreasing but eval scores are flat. Walk through your diagnosis.
17. KL divergence spikes at step 300 and the model starts producing gibberish.
18. The model won't emit EOS and rambles until the token limit.
19. Reward climbs steadily; human preference win rate falls. What happened?
20. The model refuses harmless requests after a safety-data run. Fix it without
    losing the safety gains.
21. Your DPO run lowered the log-probability of the chosen responses. Is that a bug?
22. Benchmarks improved but production thumbs-down rate rose 15%.
23. The model behaves well in your eval harness and badly in the product. Name
    five things that could differ.

## RL environments

- Design an RL environment for training a model to fix GitHub issues. Cover
  reward, termination, and anti-gaming.
- Sparse vs dense reward for multi-step math — which, and why?
- Your model passes every unit test but the code is obviously wrong. What
  happened, and how do you fix the *environment*?
- ORM vs PRM: when is per-step supervision worth the labeling cost?
- Your environment runs at 2 episodes/sec and the GPUs sit idle. What do you do?
- How do you know the model learned the task rather than the environment?

## Design (open-ended, 30–45 min)

24. Design the full post-training pipeline for a new 8B instruct model. Data,
    stages, evals, timeline, team.
25. Design a preference-collection system for 100 annotators. Cover quality control.
26. You have 1000 H100-hours. Allocate them across SFT, RM, and RL, and justify it.
27. Design an eval suite that catches regressions a leaderboard would miss.
28. Make an existing model better at agentic tool use. Where do you start?
29. Post-train a model for a specialized domain (medical, legal) without
    degrading general ability.
30. Your model must be helpful and harmless, and those conflict on a real class
    of prompts. How do you decide, and how do you encode that decision in training?

## Behavioral, with an AI-lab slant

31. Describe a time you shipped something you weren't fully confident in.
32. Tell me about a result you couldn't reproduce. What did you do?
33. How do you decide when a model is good enough to ship?
34. Describe a disagreement with a colleague over a technical approach.

> These pair with [../../behavioral/](../../behavioral/) — same stories, tuned to
> a research-engineering audience.

## Notes

_Write your worked answers here._
