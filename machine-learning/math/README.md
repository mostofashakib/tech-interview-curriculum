# Math

The prerequisites. Refresh whatever is rusty — this is the most common source of
"I knew this once" stalls in an ML interview.

## Linear algebra

- [ ] Vectors, dot product, norms (L1, L2, L∞), cosine similarity
- [ ] Matrix multiplication and what it means geometrically
- [ ] Rank, span, basis, linear independence
- [ ] Eigenvalues and eigenvectors; the connection to PCA
- [ ] SVD and its uses: PCA, low-rank approximation, pseudoinverse — and its
      direct appearance in LoRA
- [ ] Positive definite matrices; covariance matrices
- [ ] Matrix calculus: gradients of `xᵀAx`, `‖Ax − b‖²`

## Probability

- [ ] Conditional probability, **Bayes' theorem** (be able to apply it to a
      base-rate word problem cold — this is asked constantly)
- [ ] Independence vs conditional independence
- [ ] Distributions: Bernoulli, binomial, Poisson, normal, exponential, beta
- [ ] Expectation, variance, covariance, correlation
- [ ] Law of large numbers; central limit theorem
- [ ] Maximum likelihood estimation; MAP and its link to regularization
- [ ] Entropy, cross-entropy, **KL divergence** — the bridge to
      [../../post-training/](../../post-training/)

## Statistics

- [ ] Sampling, sampling distributions, standard error
- [ ] Confidence intervals and what they do and don't claim
- [ ] Hypothesis testing, p-values, type I and II errors, power
- [ ] t-test, chi-square, ANOVA
- [ ] Multiple comparisons and correction
- [ ] Bootstrap and permutation tests
- [ ] **Correlation ≠ causation**; confounders, Simpson's paradox
- [ ] A/B testing: sample size, MDE, peeking, novelty effects

## Optimization

- [ ] Convexity and why it matters
- [ ] Gradients, Hessians, second-order methods
- [ ] Lagrange multipliers and constrained optimization
- [ ] Gradient descent variants and convergence behavior
- [ ] Saddle points vs local minima in high dimensions

## The five to be fluent in

If time is short, these carry the most interview weight:

1. **Bayes' theorem applied to a base-rate problem.** ("A test is 99% accurate,
   disease prevalence is 0.1%, you test positive — what's the probability you
   have it?") Get this instantly and correctly.
2. **Cross-entropy and KL divergence** — definitions and the relationship. Used
   in every loss function you'll discuss and throughout post-training.
3. **Eigen-decomposition / SVD** — powers PCA and LoRA.
4. **MLE** — most losses are derived from it; deriving cross-entropy from MLE is
   a common ask.
5. **CLT and confidence intervals** — needed the moment you claim one model beat
   another.

## Notes

_Add your own notes and worked problems here._
