# Foundations

The concepts every other folder assumes, and the most heavily asked material in
ML interviews.

## Checklist

**The learning problem**
- [ ] Supervised vs unsupervised vs semi-supervised vs self-supervised vs reinforcement
- [ ] Training / validation / test split, and what each is *allowed* to be used for
- [ ] Empirical risk minimization; loss vs metric (you optimize one, you're judged on the other)
- [ ] iid assumption and what breaks when it doesn't hold (time series, grouped data, drift)
- [ ] No free lunch theorem — why "best algorithm" is not a well-posed question

**Bias-variance**
- [ ] The decomposition: `E[error] = bias² + variance + irreducible error`
- [ ] Underfitting vs overfitting, and how each looks on a learning curve
- [ ] Model complexity vs error — the classic U-curve
- [ ] Double descent: why the U-curve is incomplete for overparameterized models
- [ ] How more data affects bias vs variance (it fixes variance, not bias)

**Regularization**
- [ ] L1 (Lasso) — sparsity; *why* the corner of the constraint region produces exact zeros
- [ ] L2 (Ridge) — shrinkage; behavior under correlated features
- [ ] Elastic net
- [ ] Early stopping as implicit regularization
- [ ] Dropout, weight decay, data augmentation, label smoothing
- [ ] Bayesian reading: L2 = Gaussian prior, L1 = Laplace prior

**Validation**
- [ ] k-fold, stratified k-fold, leave-one-out
- [ ] Time-series CV — why random splits leak the future
- [ ] Group/nested CV — when the same entity appears in multiple rows
- [ ] Nested CV for honest hyperparameter selection
- [ ] **Data leakage**: target leakage, train-test contamination, fitting scalers before splitting

**Optimization**
- [ ] Gradient descent: batch, stochastic, mini-batch
- [ ] Learning rate, momentum, Adam/AdamW, schedules
- [ ] Convex vs non-convex; local minima vs saddle points (saddles are the real problem in high dimensions)
- [ ] Convergence diagnostics from loss curves

**Practical framing**
- [ ] Curse of dimensionality
- [ ] Class imbalance — resampling, class weights, threshold moving
- [ ] Generative vs discriminative models

## Questions to be ready for

- Explain bias-variance to a non-technical stakeholder. Then write the decomposition.
- Your model is 99% accurate and useless. What happened?
- Why does L1 produce sparsity and L2 not? (Draw the constraint regions.)
- Training accuracy 98%, validation 62%. Give five things you'd try, ordered.
- You have 500 labeled examples. How do you validate?
- Name three ways data leakage sneaks into a pipeline.
- When does more data *not* help?

## Notes

_Add your own notes here._
