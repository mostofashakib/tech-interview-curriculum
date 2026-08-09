# Model Evaluation

Cheap to learn, disproportionately asked. "Why is accuracy the wrong metric
here?" appears in nearly every ML interview.

## Checklist

**Classification metrics**
- [ ] Confusion matrix; be able to draw it and label all four cells without hesitating
- [ ] Precision = TP/(TP+FP) — of what I flagged, how much was right
- [ ] Recall = TP/(TP+FN) — of what was there, how much did I catch
- [ ] F1, and Fβ when precision and recall aren't equally important
- [ ] Specificity, sensitivity, and the medical-testing vocabulary
- [ ] **Accuracy's failure under imbalance** — 99% accuracy on a 1% positive rate is the null model
- [ ] **ROC-AUC**: TPR vs FPR, threshold-independent, interpretation as ranking probability
- [ ] **PR-AUC**: why it's the right curve under heavy imbalance (ROC looks great when it shouldn't)
- [ ] Log loss and Brier score
- [ ] Multiclass averaging: macro vs micro vs weighted — and what each hides

**The precision/recall trade-off**
- [ ] Threshold selection as a *business* decision, not a modeling one
- [ ] Cost-sensitive evaluation: what does a false positive actually cost?
- [ ] Recall-first domains (disease screening, fraud) vs precision-first (spam, content removal)

**Regression metrics**
- [ ] MSE, RMSE, MAE — and when outlier sensitivity is a feature vs a bug
- [ ] MAPE and its blowup near zero
- [ ] R² and adjusted R²
- [ ] Huber loss as the robust middle ground

**Calibration**
- [ ] What calibration means: a 0.7 prediction should be right 70% of the time
- [ ] Reliability diagrams, expected calibration error
- [ ] Platt scaling, isotonic regression
- [ ] Why discrimination and calibration are independent — a model can rank perfectly and be badly calibrated
- [ ] When calibration matters (any downstream decision using the probability) and when it doesn't (pure ranking)

**Ranking and recommendation**
- [ ] Precision@k, Recall@k, MAP, NDCG, MRR

**Rigor**
- [ ] Confidence intervals via bootstrap
- [ ] Statistical significance between two models; paired tests
- [ ] Multiple comparisons — testing 20 variants finds a winner by chance
- [ ] A/B testing: sample size, power, novelty effects, peeking
- [ ] Offline/online metric divergence, and why it's the norm not the exception

**Slicing**
- [ ] Per-segment performance; average scores masking subgroup regressions
- [ ] Fairness metrics: demographic parity, equalized odds, and their mutual incompatibility

## Metric selection cheat sheet

| Situation | Use | Not |
|---|---|---|
| Balanced classes | Accuracy, F1 | — |
| Heavy imbalance | PR-AUC, recall@precision | Accuracy, ROC-AUC |
| Probabilities drive a decision | Log loss + calibration | Accuracy |
| Ranking | NDCG, MAP | Accuracy |
| Regression with outliers | MAE, Huber | MSE |
| Cost asymmetric | Cost-weighted metric | F1 |

## Questions to be ready for

- 99% accurate fraud model. Is it good? (No — state the base rate first.)
- ROC-AUC vs PR-AUC under 1:1000 imbalance. Which and why?
- Your model ranks well but its probabilities are wrong. Does it matter?
- Pick a threshold for a cancer screening model. Justify it.
- Offline metrics up, online metrics down. Name five causes.
- Model A beats model B by 0.3% on the test set. Ship it?

## Notes

_Add your own notes here._
