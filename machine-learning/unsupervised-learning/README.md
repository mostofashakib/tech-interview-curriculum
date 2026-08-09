# Unsupervised Learning

Structure without labels. Less frequently asked than supervised, but the
questions are often deeper because there's no accuracy number to hide behind.

## Checklist

**Clustering**
- [ ] **k-means**: Lloyd's algorithm, k-means++ initialization, convergence to local optima
- [ ] Choosing k: elbow method, silhouette score, gap statistic — and why all are unsatisfying
- [ ] k-means assumptions: spherical, equally-sized, equally-dense clusters (and what breaks each)
- [ ] **Hierarchical**: agglomerative vs divisive, linkage criteria, dendrograms
- [ ] **DBSCAN**: density-based, finds arbitrary shapes, labels outliers, no k needed; eps/minPts sensitivity
- [ ] **GMM**: soft assignment, EM algorithm, k-means as a special case
- [ ] Evaluation without labels: silhouette, Davies-Bouldin, Calinski-Harabasz

**Dimensionality reduction**
- [ ] **PCA**: covariance eigendecomposition or SVD, explained variance ratio, choosing components
- [ ] PCA assumes linearity and that variance means information — know both failure cases
- [ ] Why you must center (and usually standardize) before PCA
- [ ] **t-SNE**: local structure, perplexity, why distances *between* clusters are meaningless
- [ ] **UMAP**: faster, preserves more global structure
- [ ] Autoencoders as non-linear dimensionality reduction
- [ ] Matrix factorization: SVD, NMF

**Anomaly detection**
- [ ] Statistical thresholds, z-score, IQR
- [ ] Isolation Forest
- [ ] One-class SVM
- [ ] Autoencoder reconstruction error
- [ ] The evaluation problem: extreme imbalance, few or no labels

**Association and recommendation**
- [ ] Apriori, FP-growth; support/confidence/lift
- [ ] Collaborative filtering: user-based, item-based, matrix factorization
- [ ] Cold start and the popularity bias problem

## The question people fumble

**"How do you know your clustering is any good?"**

There is no ground truth, so the honest answer has three parts: internal metrics
(silhouette, Davies-Bouldin) measure geometric quality but not usefulness;
stability analysis (do clusters survive resampling and reseeding?) tests whether
they're real; and downstream/expert validation is the only thing that tests
whether they're *useful*. Say all three. Candidates who name only the first
sound like they've never clustered real data.

## Questions to be ready for

- k-means found 3 clusters. How do you know that's right?
- When does k-means fail badly? (Non-spherical, varying density, differing sizes, outliers.)
- PCA vs t-SNE — when each, and what can't you conclude from a t-SNE plot?
- You have 10M rows and 5000 features. Reduce dimensionality. Walk me through it.
- Detect fraud with no labels. Approach?

## Notes

_Add your own notes here._
