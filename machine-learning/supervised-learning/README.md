# Supervised Learning

Where most classical ML interview questions live.

## Checklist

**Linear regression**
- [ ] Assumptions: linearity, independence, homoscedasticity, normal residuals
- [ ] Closed-form normal equation vs gradient descent, and when each is preferable
- [ ] Multicollinearity — detection (VIF) and remedy
- [ ] R², adjusted R², and why R² always rises with more features

**Logistic regression**
- [ ] Sigmoid, log-odds, and interpreting a coefficient as an odds ratio
- [ ] Cross-entropy loss and its derivation from maximum likelihood
- [ ] Why not squared error for classification (non-convexity, gradient behavior)
- [ ] Multiclass: softmax vs one-vs-rest
- [ ] Still the correct baseline far more often than people expect — say so

**Decision trees**
- [ ] Splitting criteria: Gini, entropy/information gain, variance reduction
- [ ] Why trees overfit; pruning, depth limits, min-samples constraints
- [ ] Handling categoricals and missing values natively
- [ ] Feature importance and its bias toward high-cardinality features

**Ensembles** — expect at least one question here
- [ ] **Bagging**: bootstrap sampling, variance reduction, parallel training
- [ ] **Random forest**: bagging + random feature subsets; why decorrelating trees is the key idea
- [ ] **Boosting**: sequential, fits residuals, reduces bias
- [ ] AdaBoost vs gradient boosting
- [ ] XGBoost / LightGBM / CatBoost — what each actually contributes
- [ ] **Bagging vs boosting** — the canonical question. Variance vs bias; parallel vs sequential; robust to noise vs sensitive to it
- [ ] Stacking and blending
- [ ] Why gradient boosting still beats deep learning on tabular data

**SVM**
- [ ] Maximum margin intuition; support vectors
- [ ] Hard vs soft margin; the C parameter
- [ ] Kernel trick: polynomial, RBF; what "trick" means (never compute the mapping)
- [ ] Scaling requirements and complexity limits on large n

**kNN**
- [ ] Lazy learning; no training cost, expensive inference
- [ ] Choosing k; the bias-variance effect of k
- [ ] Distance metrics and why scaling is mandatory
- [ ] Degradation in high dimensions

**Naive Bayes**
- [ ] Bayes' theorem and the conditional independence assumption
- [ ] Gaussian / multinomial / Bernoulli variants
- [ ] Laplace smoothing
- [ ] Why it works well on text despite an assumption that's clearly false

## Comparison table to have internalized

| Model | Assumption | Handles non-linearity | Scaling needed | Interpretable | Notes |
|---|---|---|---|---|---|
| Linear/logistic reg. | Linear in features | No (without feature eng.) | Yes | High | Best baseline |
| Decision tree | None | Yes | No | High | Overfits alone |
| Random forest | None | Yes | No | Medium | Strong default |
| Gradient boosting | None | Yes | No | Medium | Usually best on tabular |
| SVM | Margin separability | Yes (kernel) | Yes | Low | Poor scaling in n |
| kNN | Local smoothness | Yes | Yes | Medium | Slow inference |
| Naive Bayes | Feature independence | No | No | High | Fast, great on text |

## Questions to be ready for

- Bagging vs boosting — mechanism and when to use each.
- Why does random forest choose a random feature subset at each split?
- Explain the kernel trick without writing an equation.
- Your gradient boosting model beats your neural net on tabular data. Why isn't that surprising?
- When is logistic regression the right final answer rather than the baseline?
- Derive the logistic regression gradient.

## Notes

_Add your own notes here._
