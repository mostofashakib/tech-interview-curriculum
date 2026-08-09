# Core Interview Preparation

A one-stop study repo for technical interviews. **Pick your career path below,
follow the route it gives you, and ignore everything else.**

---

## 🎯 Start here — pick your path

<table>
<tr><th>If you're targeting…</th><th>Study, in this order</th></tr>
<tr>
<td><b>Software Engineer</b><br><sub>product, backend, full-stack</sub></td>
<td>1. <a href="dsa/">DSA</a> &nbsp;→&nbsp; 2. <a href="software-engineering/">Software Engineering</a> &nbsp;→&nbsp; 3. <a href="behavioral/">Behavioral</a></td>
</tr>
<tr>
<td><b>Senior / Staff Engineer</b></td>
<td>1. <a href="software-engineering/system-design/">System Design</a> &nbsp;→&nbsp; 2. <a href="behavioral/">Behavioral</a> &nbsp;→&nbsp; 3. <a href="dsa/">DSA</a> (refresh)</td>
</tr>
<tr>
<td><b>ML Engineer / Data Scientist</b></td>
<td>1. <a href="machine-learning/">Machine Learning</a> &nbsp;→&nbsp; 2. <a href="machine-learning/ml-system-design/">ML System Design</a> &nbsp;→&nbsp; 3. <a href="dsa/">DSA</a> &nbsp;→&nbsp; 4. <a href="behavioral/">Behavioral</a></td>
</tr>
<tr>
<td><b>AI Lab / Research Engineer</b><br><sub>post-training, alignment, RL</sub></td>
<td>1. <a href="machine-learning/deep-learning/">Deep Learning</a> &nbsp;→&nbsp; 2. <a href="post-training/">Post-Training</a> &nbsp;→&nbsp; 3. <a href="dsa/">DSA</a> &nbsp;→&nbsp; 4. <a href="behavioral/">Behavioral</a></td>
</tr>
<tr>
<td><b>ML Infra / Inference</b></td>
<td>1. <a href="post-training/inference/">Inference</a> &nbsp;→&nbsp; 2. <a href="software-engineering/system-design/">System Design</a> &nbsp;→&nbsp; 3. <a href="post-training/">Post-Training</a> &nbsp;→&nbsp; 4. <a href="dsa/">DSA</a></td>
</tr>
<tr>
<td><b>New grad / intern</b></td>
<td>1. <a href="dsa/">DSA</a> (most of your time) &nbsp;→&nbsp; 2. <a href="software-engineering/cs-fundamentals/">CS Fundamentals</a> &nbsp;→&nbsp; 3. <a href="behavioral/">Behavioral</a></td>
</tr>
</table>

Every route has its own README with a suggested order and a question bank. Open
the first link in your row and start there.

---

## 📚 The five routes

### [dsa/](dsa/) — Data Structures & Algorithms
The coding round. Hand-written implementations, ~1000 solved problems organized
by company, a multi-month study curriculum, and reference books.

### [behavioral/](behavioral/) — Behavioral & Reverse Interview
Story bank method, STAR structure, a phone-screen cheat sheet, and the questions
you ask them.

### [software-engineering/](software-engineering/) — System Design & CS Fundamentals
System design framework and templates, OS / networks / databases / OOP /
architecture, language-specific questions, and web fundamentals.

### [machine-learning/](machine-learning/) — Classical ML
Foundations, supervised and unsupervised learning, deep learning, feature
engineering, model evaluation, ML system design, and the math underneath.

### [post-training/](post-training/) — LLM Post-Training
SFT, reward modeling, RLHF / DPO / GRPO, RL environments, evaluation and
LLM-as-a-judge, and inference optimization. Includes written notes derived from
[mostofashakib.com/blog](https://www.mostofashakib.com/blog).

Plus [resources/](resources/) — resume tips and general books.

---

## 🗺️ Repository map

```
dsa/
├── implementations/            arrays, strings, graphs, trie, pattern search
├── practice-problems/          ~1000 Java solutions by company and source
├── study-plan/                 Coding Interview University curriculum
├── google-interview/           "Hacking a Google Interview" handouts
└── references/                 cheat sheets, CP Handbook, EPI

behavioral/
├── behavioral-questions.docx
├── phone-interview-cheat-sheet.jpg
└── reverse-interview/          what to ask them

software-engineering/
├── system-design/              framework, template, curated references
├── cs-fundamentals/            OS, networks, databases, OOP, architecture
├── languages/                  java, javascript, python
└── web/                        frontend fundamentals

machine-learning/
├── math/                       linear algebra, probability, stats, optimization
├── foundations/                bias-variance, regularization, validation, leakage
├── supervised-learning/        regression, trees, ensembles, SVM, kNN, NB
├── unsupervised-learning/      clustering, PCA, anomaly detection
├── deep-learning/              backprop, CNNs, RNNs, transformers, optimizers
├── feature-engineering/        encoding, imputation, leakage, imbalance
├── model-evaluation/           metrics, ROC/PR, calibration, significance
├── ml-system-design/           end-to-end design rounds
└── interview-questions/        49-question bank

post-training/
├── glossary.md                 policy, trajectory, KL, Fisher information
├── fundamentals/               ★ the 5-stage LLM pipeline — start here
├── data/                       ★ taxonomies, synthetic data, rubrics
├── sft/                        ★ instruction tuning, LoRA, QLoRA
├── reward-modeling/            preference data, Bradley-Terry, failure modes
├── preference-optimization/    ★ DPO, RLHF, RLVR · TRPO, PPO, GRPO
├── rl-environments/            environment & reward design, anti-gaming
├── evals/                      ★ benchmarks, LLM-as-judge, agentic evaluation
├── inference/                  KV cache, quantization, speculative decoding
└── interview-questions/        derivations, debugging, design

resources/
├── resume/
└── books/

★ = contains written notes, not just checklists
```

---

## 🧭 How this repo is meant to be used

**Every folder has a README** that tells you what's in it, what order to study
it in, and what you'll be asked. You should never have to guess what a directory
is for.

**Checklists are the unit of study.** Most folders are a checkbox list of what to
know plus a question bank. Work down the list; if you can't answer a question out
loud, that's your next study session.

**Write your notes into the folder you're studying.** Each README ends with a
Notes section for exactly this. The repo gets more valuable the more of your own
work is in it.

**Follow the cross-links.** Routes reference each other where topics connect —
KL divergence in `machine-learning/math/` links to `post-training/`, agentic
evaluation links to RL environments. The connections are where interview
questions come from.

---

## Conventions

- Paths are kebab-case with no spaces — tab-completable and scriptable.
- Written notes cite their source at the top.
- `dsa/practice-problems/` and `dsa/study-plan/` are vendored from
  [kdn251/interviews](https://github.com/kdn251/interviews) and
  [jwasham/coding-interview-university](https://github.com/jwasham/coding-interview-university).
  Their internal structure is left alone so they stay easy to update.

## License

[MIT](LICENSE)
