# Machine Learning

Classical and traditional ML — everything that isn't LLM post-training. This is
the route for ML engineer, data scientist, and applied scientist loops, and it's
the foundation the [llm-post-training/](../llm-post-training/) route assumes.

> **Which route do I need?**
> Classical ML / MLE / DS roles → this route.
> AI lab, research engineer, LLM roles → this route for fundamentals, then
> [llm-post-training/](../llm-post-training/).
> Almost every ML loop also has a coding round → [../dsa/](../dsa/).

## Contents

| Folder | Covers |
|---|---|
| [foundations/](foundations/) | Bias-variance, overfitting, regularization, validation, the learning problem |
| [supervised-learning/](supervised-learning/) | Linear/logistic regression, trees, ensembles, SVM, kNN, Naive Bayes |
| [unsupervised-learning/](unsupervised-learning/) | Clustering, PCA, dimensionality reduction, anomaly detection |
| [deep-learning/](deep-learning/) | Backprop, CNNs, RNNs, transformers, optimizers, regularization |
| [feature-engineering/](feature-engineering/) | Encoding, scaling, missing data, leakage, imbalance |
| [model-evaluation/](model-evaluation/) | Metrics, ROC/PR, calibration, statistical significance |
| [ml-system-design/](ml-system-design/) | End-to-end ML system design rounds |
| [math/](math/) | Linear algebra, probability, statistics, optimization |
| [interview-questions/](interview-questions/) | Question bank across the route |

## Suggested order

1. **[math/](math/)** if it's rusty — everything else leans on it, and it's the
   most common source of "I knew this once" stalls.
2. **[foundations/](foundations/)** — bias-variance and validation are the single
   most-asked topics in ML interviews.
3. **[supervised-learning/](supervised-learning/)** — most interview questions live here.
4. **[model-evaluation/](model-evaluation/)** — cheap to learn, disproportionately
   asked. "Why is accuracy the wrong metric here?" is nearly guaranteed.
5. **[feature-engineering/](feature-engineering/)** and
   **[unsupervised-learning/](unsupervised-learning/)**.
6. **[deep-learning/](deep-learning/)** — depth depends on the role.
7. **[ml-system-design/](ml-system-design/)** — the highest-variance round at
   senior level. Give it real time.

## The framing that gets you hired

For every algorithm, be able to answer five things:

- **What assumption does it make?** (linear separability, independence, iid, stationarity)
- **What's the objective function?** Write it down.
- **How does it overfit, and how do you stop it?**
- **What's the complexity** in train and inference, in n and d?
- **When would you *not* use it?**

Reciting an algorithm's definition is table stakes. Naming the assumption it
makes and the situation that breaks it is what separates candidates.

## Notes

_Fill each folder with your own notes as you study._
