# Feature Engineering

The part of ML that most determines real-world performance and gets the least
textbook coverage.

## Checklist

**Numerical features**
- [ ] Standardization vs min-max vs robust scaling — and which models require it
      (distance-based and gradient-based yes; trees no)
- [ ] Log / Box-Cox / Yeo-Johnson transforms for skew
- [ ] Binning and discretization
- [ ] Polynomial and interaction terms
- [ ] Outlier handling: clip, winsorize, remove, or model separately

**Categorical features**
- [ ] One-hot encoding and the dimensionality cost at high cardinality
- [ ] Label / ordinal encoding, and the false ordering it can imply
- [ ] **Target/mean encoding** and why it leaks unless done inside CV folds
- [ ] Frequency and count encoding
- [ ] Hashing trick for very high cardinality
- [ ] Embeddings for categoricals
- [ ] Unseen categories at inference time

**Missing data**
- [ ] MCAR / MAR / MNAR and why the mechanism dictates the fix
- [ ] Mean/median/mode imputation and the variance it destroys
- [ ] Model-based imputation, KNN imputation, MICE
- [ ] **Missingness as a feature** — an indicator column is often the strongest signal
- [ ] Models that handle NaN natively (LightGBM, XGBoost)

**Leakage** — the highest-cost mistake in applied ML
- [ ] **Target leakage**: a feature that encodes the future or the label itself
- [ ] **Train-test contamination**: fitting a scaler or encoder before splitting
- [ ] Temporal leakage in time series
- [ ] Group leakage: the same user/patient in both train and test
- [ ] Duplicate rows straddling the split
- [ ] The tell: implausibly good validation performance. Investigate before celebrating.

**Class imbalance**
- [ ] Random over/undersampling
- [ ] SMOTE and its variants; why synthetic minority points can be harmful in high dimensions
- [ ] Class weights in the loss
- [ ] Threshold moving as the cheapest fix, and often the best

**Feature selection**
- [ ] Filter methods: correlation, mutual information, chi-square
- [ ] Wrapper methods: forward/backward selection, RFE
- [ ] Embedded: L1, tree importances
- [ ] Permutation importance and SHAP
- [ ] Why correlated features distort importance measures

**Domain-specific**
- [ ] Text: TF-IDF, n-grams, embeddings
- [ ] Time series: lags, rolling windows, seasonality, date parts
- [ ] Geospatial: distances, clustering, geohashing

**Production**
- [ ] Train/serve skew — the same transform must run in both places
- [ ] Feature stores; point-in-time correctness
- [ ] Feature drift monitoring

## The rule

**Fit every transform on training data only, then apply to validation and test.**
Scalers, encoders, imputers, feature selectors — all of them. Put them in a
pipeline object so it's structurally impossible to get wrong. Most leakage is
this one rule broken casually.

## Questions to be ready for

- 40% of a feature is missing. Options, and how do you choose?
- Encode a categorical with 50,000 levels.
- Your validation AUC is 0.99. What do you check first?
- Why does target encoding leak, and how do you do it safely?
- SMOTE or class weights? Defend it.
- Which models need feature scaling and which don't — and why?

## Notes

_Add your own notes here._
