# ML Interview Questions

Work these out loud, timed. Write your answers into this folder.

## Foundations

1. Explain bias-variance to a non-technical stakeholder, then write the decomposition.
2. Training accuracy 98%, validation 62%. Five things you'd try, in order.
3. Why does L1 give sparsity and L2 not? Draw it.
4. When does more data not help?
5. You have 500 labeled examples. How do you validate?
6. Name three ways data leakage enters a pipeline.
7. What is double descent and why does it contradict the classic U-curve?

## Algorithms

8. Bagging vs boosting — mechanism, and when each.
9. Why does random forest sample features at each split?
10. Explain the kernel trick without an equation.
11. Derive the logistic regression gradient.
12. Why is Naive Bayes good at text despite a false assumption?
13. When does k-means fail? Name four situations.
14. PCA vs t-SNE — and what can't you conclude from a t-SNE plot?
15. Why does gradient boosting still beat neural nets on tabular data?

## Evaluation

16. 99% accurate fraud model. Is it good?
17. ROC-AUC vs PR-AUC at 1:1000 imbalance. Which, and why?
18. Your model ranks well but its probabilities are wrong. Does it matter?
19. Choose a threshold for cancer screening. Justify it.
20. Offline metrics up, online down. Five causes.
21. Model A beats B by 0.3% on test. Ship it?

## Features and data

22. 40% of a feature is missing. Options?
23. Encode a categorical with 50,000 levels.
24. Validation AUC is 0.99. What do you check first?
25. Why does target encoding leak, and how do you do it safely?
26. SMOTE or class weights? Defend it.

## Deep learning

27. Derive backprop for a two-layer network.
28. Why do ResNets allow 100+ layers?
29. Batch norm vs layer norm; why do transformers use layer norm?
30. Loss is NaN at step 50. Diagnose it.
31. Why did attention replace recurrence?
32. When is SGD with momentum better than Adam?

## System design (45 min each)

33. Design YouTube recommendations.
34. Design fraud detection for payments.
35. Design marketplace search ranking.
36. Design delivery-time estimation.
37. Design an abuse-detection system against adaptive adversaries.
38. CTR is up, retention is down. What's happening?
39. Labels arrive 30 days late. How do you monitor?
40. Design an LLM-powered support assistant, including its evaluation.

## Coding

41. Implement k-means from scratch.
42. Implement logistic regression with gradient descent, no libraries.
43. Implement train/test split with stratification.
44. Compute precision, recall, F1, and AUC from raw predictions.
45. Implement k-fold cross-validation.

> Pair these with [../../dsa/](../../dsa/) — ML loops almost always include a
> standard coding round too.

## Behavioral

46. Describe a model you shipped that didn't work. What did you learn?
47. How do you decide a model is good enough to deploy?
48. Tell me about a time the data was the problem, not the model.
49. Describe explaining a technical trade-off to a non-technical stakeholder.

> Pair with [../../behavioral/](../../behavioral/).

## Notes

_Write your worked answers here._
