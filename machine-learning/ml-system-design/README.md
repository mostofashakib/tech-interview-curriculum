# ML System Design

The highest-variance round in ML interviews and the one that most determines
level. It's [../../software-engineering/system-design/](../../software-engineering/system-design/)
plus data, models, and feedback loops.

## The framework

Use this every time. Volunteer the structure at the start — it buys you credit
immediately and keeps you from rambling.

**1. Clarify the problem (5 min)**
- What exactly are we predicting? Convert the business goal to an ML objective.
- Is ML even the right tool? Say this out loud; sometimes the answer is rules.
- Scale: users, requests/sec, data volume
- Latency budget: real-time, near-real-time, or batch
- What does success mean in business terms?

**2. Frame it as an ML problem**
- Classification / regression / ranking / recommendation / generation
- What's the label, and where does it come from?
- Online vs batch inference
- Baseline first — always name the non-ML or simple baseline

**3. Data**
- Sources, volume, labels, and how labels are actually obtained
- Training data collection; implicit feedback and its biases
- Class imbalance, sampling strategy
- Train/val/test split respecting time and groups
- Privacy and compliance constraints

**4. Features**
- Candidate features grouped by entity (user, item, context, interaction)
- Real-time vs precomputed; feature store
- Cold start for new users and items

**5. Model**
- Baseline → simple model → complex model, with a reason for each step
- Trade-offs: latency, interpretability, training cost, maintenance
- Multi-stage architectures: **candidate generation → ranking → re-ranking**
- Why two stages: recall cheaply over millions, then spend compute on hundreds

**6. Evaluation**
- Offline metrics tied to the ML objective
- Online metrics tied to the business objective
- **Name the offline/online gap explicitly** — it's the most common follow-up
- A/B test design, guardrail metrics

**7. Serving and infrastructure**
- Model serving, batching, caching
- Latency budget broken down by component
- Scaling and fallback when the model is unavailable

**8. Monitoring and iteration**
- Data drift, concept drift, feature pipeline failures
- Performance degradation detection with delayed labels
- Retraining cadence and triggers
- **Feedback loops**: the model's outputs shape the data that trains the next model

## Classic problems

Work each one end to end, timed at 45 minutes:

| Problem | The interesting part |
|---|---|
| Video/content recommendation | Two-stage retrieval + ranking, cold start, diversity |
| Search ranking | Learning-to-rank, relevance labels, position bias |
| News feed ranking | Multi-objective (engagement vs quality), feedback loops |
| Ad click prediction (CTR) | Calibration matters — the probability *is* the price |
| Fraud detection | Extreme imbalance, adversarial drift, cost asymmetry |
| Spam/abuse detection | Adversaries adapt; label delay |
| Delivery time estimation | Regression with hard latency limits, spatial features |
| Product similarity / embeddings | Metric learning, ANN search |
| Churn prediction | Label definition is the whole problem |
| Dynamic pricing | Feedback loop into the training data |
| Autocomplete / query suggestion | Latency budget in single-digit ms |
| LLM-powered feature | Eval design, cost per call, fallbacks — see [../../post-training/evals/](../../post-training/evals/) |

## The three things that separate a senior answer

1. **You name a baseline and justify complexity against it.** Jumping to a deep
   model is a junior signal.
2. **You surface the feedback loop.** Recommenders train on data their own
   predictions generated. If you don't mention it, you haven't run one.
3. **You state what you'd monitor and how you'd know it broke.** Design that ends
   at "deploy" is incomplete.

## Questions to be ready for

- Design YouTube recommendations.
- Design fraud detection for a payments company.
- Design the ranking system for a marketplace search.
- Your recommender's CTR is up and retention is down. What's happening?
- Labels arrive 30 days late. How do you monitor?
- Design an LLM-powered support assistant, including its eval.

## Notes

_Write your worked designs here — one file per problem._
