# gen_strat_1 — test_idea

> Phase: `invention_loop` · round 2 · `gen_strat`
> Run: `run_6uOr5GlpaMfR` — Evaluating Embedding-Based Semantic Coherence for Readability Assessment: An Empirical Study
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_strat_1` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-07-09 00:50:22 UTC

````
<hypothesis>
Your strategy should advance this hypothesis.

kind: hypothesis
title: Semantic Coherence Distance for Readability Assessment
hypothesis: >-
  Text readability has a semantic coherence component that can be measured by computing distances between sentence embeddings
  in a semantic trajectory, capturing aspects of reading difficulty not reflected in surface-level readability formulas. However,
  this semantic distance signal may be complementary to rather than a replacement for traditional surface-based metrics, and
  its effectiveness depends critically on the choice of embedding space and evaluation dataset.
motivation: >-
  Current readability formulas (Flesch-Kincaid, etc.) rely on surface features like sentence length and word complexity, missing
  the dynamic flow of meaning. Information-theoretic approaches (compression/Kolmogorov complexity) capture static complexity
  but not the cognitive effort of semantic navigation. By treating text as a dynamical system trajectory through semantic
  space and measuring the optimal control energy needed to follow it, we can capture a fundamental aspect of readability:
  how much cognitive 'work' a reader must expend to track the evolving meaning.
assumptions:
- >-
  Text can be meaningfully represented as a trajectory in a continuous semantic embedding space
- >-
  Human reading comprehension requires cognitive resources proportional to the 'control effort' needed to track semantic changes
- >-
  Optimal control theory provides a valid framework for quantifying the minimum effort needed to navigate semantic transitions
- >-
  The energy cost of semantic transitions correlates with subjective reading difficulty
investigation_approach: >-
  1. Map sentences to embeddings (using SBERT or similar) to create a semantic trajectory. 2. Model the trajectory as a dynamical
  system: x(t+1) = x(t) + u(t) + noise, where x is the semantic state and u is the 'control input'. 3. Compute the LQR (Linear
  Quadratic Regulator) cost: sum of squared deviations from optimal path + control effort. 4. Alternative: compute the cumulative
  Wasserstein distance or semantic 'work' along the trajectory. 5. Compare against traditional readability formulas and human
  judgments on standard datasets (CLEAR corpus, WeeBit, etc.). 6. Evaluate whether SCE captures aspects of readability that
  traditional formulas miss (e.g., texts with simple words but jarring topic shifts).
success_criteria: >-
  1. SCE scores should correlate with human readability judgments at least as well as traditional formulas (Flesch-Kincaid,
  SMOG). 2. SCE should better predict reading comprehension scores than surface-based formulas on texts with simple vocabulary
  but poor semantic flow. 3. Ablation studies should show that the 'energy' component (penalizing large semantic jumps) is
  necessary for predictive power. 4. The method should be computationally feasible: <1 second per document on standard hardware.
related_works:
- >-
  Kolmogorov complexity using compression (Ehret 2018): Also uses information theory but measures static complexity of entire
  text rather than dynamic semantic navigation cost. Our approach is fundamentally different - we measure the optimal control
  energy of the semantic trajectory, not compression ratio.
- >-
  Bigram Semantic Distance (Kenett et al. 2017): Measures semantic distance between consecutive words/sentences. Our approach
  extends this by considering the optimal control effort over the ENTIRE trajectory (not just pairwise distances) and incorporates
  a dynamical systems framework.
- >-
  Coh-Metrix and coherence measures: Measure local coherence and connectivity. Our approach is global - measuring the total
  'energy' needed to follow the semantic flow, which captures both local coherence and global trajectory smoothness.
- >-
  Word Mover's Distance (Kusner et al. 2015): Uses optimal transport for document similarity. Our approach is different: we
  measure the control energy needed to follow a trajectory, not the transport cost between two static distributions.
inspiration: >-
  The hypothesis combines insights from three distant fields: (1) Control Theory - specifically Linear Quadratic Regulator
  (LQR) theory which minimizes energy for trajectory tracking, (2) Optimal Transport theory - which provides Wasserstein distance
  for measuring semantic transition costs, and (3) Physics/Dynamical Systems - which views readability as the 'work' required
  to move through semantic space. The core insight is that readable text should have a 'smooth' semantic trajectory requiring
  minimal control corrections, analogous to how a well-designed controller keeps a system on a desired path with minimal energy
  expenditure.
terms:
- term: Semantic Trajectory
  definition: >-
    The path traced by sequential units of text (sentences or paragraphs) when mapped to a continuous vector space representing
    meaning (e.g., through sentence embeddings).
- term: Control Energy
  definition: >-
    In control theory, the cumulative effort (measured as squared control inputs) required to make a system follow a desired
    trajectory. In our context, it represents the cognitive work needed to track semantic changes in text.
- term: LQR (Linear Quadratic Regulator)
  definition: >-
    An optimal control method that finds the control inputs minimizing a quadratic cost function of state deviations and control
    effort, commonly used in engineering to design stable, efficient controllers.
- term: Semantic Embedding Space
  definition: >-
    A high-dimensional vector space where words, sentences, or documents are mapped such that semantic similarity corresponds
    to geometric proximity (e.g., cosine similarity in the embedding space).
- term: Optimal Transport (Wasserstein Distance)
  definition: >-
    A mathematical framework for measuring the distance between probability distributions by computing the minimum 'cost'
    to transform one distribution into another, often visualized as moving 'mass' from one configuration to another.
summary: >-
  This hypothesis proposes a novel readability metric based on control theory: readable text requires minimal 'control energy'
  to follow its semantic trajectory. By modeling text as a dynamical system in embedding space and computing the optimal control
  cost, we can quantify readability as the cognitive work needed for semantic navigation.
_relation_rationale: >-
  Narrowed from grand control theory claims to testable semantic distance metric, same goal of capturing coherence.
_confidence_delta: decreased
_key_changes:
- >-
  Removed unsound control theory framing; SCD is now a simple heuristic metric, not derived from optimal control
- >-
  Acknowledged that measuring semantic coherence via embeddings is not novel (Coh-Metrix, etc.)
- >-
  Narrowed claims: SCD may be complementary to traditional formulas, not necessarily superior
- >-
  Added requirement to evaluate on real datasets (CLEAR, OneStopEnglish) not just synthetic data
- >-
  Added honesty about negative results: original experiment showed anti-correlation on synthetic data
- >-
  Removed LQR dynamical systems formulation that was not actually implemented or mathematically justified
- >-
  Changed 'control energy' terminology to 'semantic coherence distance' to avoid misleading claims
relation_type: evolution
</hypothesis>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. Use it for study design, proper baselines, and the evaluation/validity norms this field demands.

- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
</available_domain_handbooks>

<iteration_status>
Current iteration: 2 of 2
Remaining (including this one): 1
</iteration_status>

<previous_strategies>
Strategies from the PREVIOUS iteration. You can CONTINUE these directions,
ADAPT based on what worked and what didn't in the artifacts produced, or PIVOT if results suggest a better path.

--- Strategy 1 ---
kind: strategy
id: gen_strat_1_idx1
title: Foundation and Baseline Implementation for SCE Readability
objective: >-
  Establish the foundational elements for testing the Semantic Control Energy (SCE) hypothesis: survey evaluation landscape,
  acquire standard readability datasets, and implement the core SCE method with initial baseline comparisons.
rationale: >-
  As the first iteration in a 2-iteration cycle, we must establish three critical foundations: (1) Understanding what datasets
  and evaluation benchmarks exist for readability assessment, (2) Acquiring the necessary data for evaluation, and (3) Implementing
  the novel SCE method. This parallel approach ensures that when iteration 2 arrives, we have all building blocks ready for
  comprehensive evaluation and paper writing.
artifact_directions:
- id: research_iter1_dir1
  type: research
  objective: >-
    Survey readability evaluation landscape: identify standard datasets with human judgments, understand traditional readability
    formulas (Flesch-Kincaid, SMOG, etc.), and determine evaluation benchmarks used in the field.
  approach: >-
    Conduct web research to identify: (1) Standard readability datasets with human judgment data (CLEAR corpus, WeeBit, Newsela,
    OneStopEnglish), (2) Traditional readability formulas and their implementations, (3) Evaluation metrics and benchmarks
    used in recent readability assessment papers, (4) Existing gaps that SCE could address. Search for 'readability dataset
    human judgment', 'CLEAR corpus readability', 'WeeBit dataset', 'Newsela readability', and survey recent ACL/EMNLP papers
    on readability assessment.
  depends_on: []
- id: dataset_iter1_dir2
  type: dataset
  objective: >-
    Acquire and standardize 2-3 standard readability datasets with human judgments or grade-level annotations for evaluating
    the SCE method.
  approach: >-
    Download and standardize: (1) CLEAR corpus (if available) or WeeBit dataset from HuggingFace or direct sources - contains
    texts with human readability ratings, (2) Newsela dataset or similar with leveled texts (same content at different reading
    levels), (3) Standard readability benchmark like OneStopEnglish. Transform to JSON format with fields: {text, readability_score/grade_level,
    metadata}. Create train/validation/test splits. Prioritize datasets with human judgment data over surface-level features.
  depends_on: []
- id: experiment_iter1_dir3
  type: experiment
  objective: >-
    Implement the core Semantic Control Energy (SCE) method: map sentences to semantic embeddings, model text as dynamical
    system trajectory, compute control energy metric, and compare against traditional readability formulas on preliminary
    data.
  approach: >-
    Implement SCE computation: (1) Use SBERT (all-mpnet-base-v2) to embed sentences, (2) Model semantic trajectory as dynamical
    system x(t+1) = x(t) + u(t), (3) Compute control energy as sum of ||u(t)||^2 where u(t) = x(t+1) - x(t) (simple formulation
    for initial test), (4) Alternative: compute cumulative Wasserstein distance or semantic 'work' along trajectory, (5) Compare
    SCE scores against Flesch-Kincaid, SMOG, and other traditional formulas, (6) Test on any available text data (Wikipedia
    articles, Project Gutenberg books) to verify computational feasibility (<1 second per document). Output preliminary correlation
    analysis with traditional metrics.
  depends_on: []
expected_outcome: >-
  After this iteration, we will have: (1) A comprehensive understanding of the readability evaluation landscape and available
  datasets, (2) 2-3 standardized readability datasets ready for evaluation, and (3) A working implementation of the SCE method
  with preliminary results showing computational feasibility and initial comparisons to traditional formulas. This provides
  the foundation for iteration 2 to conduct comprehensive evaluation against human judgments and write the paper.
summary: >-
  Establish foundations for SCE readability research through parallel landscape survey, dataset acquisition, and initial method
  implementation.
</previous_strategies>

<dependency_rules>
- depends_on is a list of objects {id, label} — each entry references an existing artifact and tags how it is being used
- "id" can ONLY reference IDs from <existing_artifacts> — never IDs you are proposing (all new artifacts run in parallel)
- "label" is a SHORT free-text type label (a word or two, NOT a sentence) describing what role the dep plays — e.g. "dataset", "validates", "extends", "supersedes". Required on every dep.
- Setting depends_on provides the dependency's out_dependency_files to your artifact at execution time
- If no suitable existing artifacts exist, use empty depends_on
- New artifact IDs are assigned by the system after submission — do not invent IDs for your proposed artifacts
</dependency_rules>

<available_artifact_types>
Artifact types you can plan. Use this to choose the right types for your strategy objectives.

<artifact_types>
RESEARCH
Web research to answer key questions — like a researcher making decisions.
Runtime: LLM Agent, no code execution.
Tools: the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text).
Capabilities: Find, synthesize, and compare information across sources; survey SOTA and best practices.
Deps: REQUIRED none | OPTIONAL other RESEARCH to build on prior findings

EXPERIMENT
Run code to test hypotheses, implement methods, and collect empirical results.
Runtime: Python 3.12, UV (any pip package), isolated workspace, gradual scaling (mini → full data).
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-json (schema validation), aii-openrouter-llms (call any LLM — GPT, Gemini, Llama, etc.), domain-specific as needed.
Capabilities: Implement and run any code-based experiment, compare method vs baselines.
Deps: REQUIRED at least one DATASET | OPTIONAL RESEARCH for methodology guidance

DATASET
Collect, prepare, and merge datasets for experiments and analysis.
Runtime: Python 3.12, UV, isolated workspace.
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-hf-datasets (HuggingFace Hub — ML datasets, many UCI/OpenML/Kaggle mirrors), aii-owid-datasets (Our World in Data — global statistics), aii-json (schema validation). Also any Python source (sklearn.datasets, openml, direct URLs, APIs) — must verify within 300MB limit.
Capabilities: Search, acquire, transform, combine, and standardize data from any available source.
Deps: REQUIRED none | OPTIONAL RESEARCH for guidance on what data to collect

EVALUATION
Evaluate experiment results with metrics, statistical analysis, and validity checks.
Runtime: Python 3.12, UV (any evaluation library), isolated workspace, gradual scaling matching experiment.
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-json (schema validation), aii-openrouter-llms (call any LLM — GPT, Gemini, Llama, etc.), domain-specific as needed.
Capabilities: Compute any quantitative metrics and statistical tests, analyze validity and robustness.
Deps: REQUIRED at least one EXPERIMENT | OPTIONAL DATASET if reference data needed

PROOF
Formally prove mathematical statements in Lean 4 with automated iteration.
Runtime: LLM agent with Lean 4 compiler feedback loop.
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-lean (proof verification, Mathlib search, tactics: ring, linarith, nlinarith, omega, simp, etc.)
Capabilities: Formally verify properties and inequalities, iterative proof development, lemma decomposition.
Deps: REQUIRED none | OPTIONAL RESEARCH for mathematical background
</artifact_types>
</available_artifact_types>

<artifact_executor_scope>
IMPORTANT: Each artifact executor has a focused prompt that guides it to do ONE thing well. It will NOT perform tasks outside its scope — assigning the wrong work to the wrong artifact type wastes an iteration. Match the task to the right executor.

RESEARCH executor scope:
  Output: research_out.json with {answer, sources, follow_up_questions} + research_report.md
  DOES: Web research — search, read, synthesize information from papers/docs/APIs into a structured report
  DOES NOT: Run code, download files, execute scripts, compute anything — no shell/Python access
  Use for literature surveys, API documentation, technical specifications — pure information gathering

EXPERIMENT executor scope:
  Output: method_out.json with results (metrics, predictions, analysis) — the core computational work
  DOES: Implement and run methods/algorithms, compute metrics, compare approaches, produce quantitative results
  DOES NOT: Collect new datasets (depends on DATASET artifacts for input data), write formal proofs
  This is the right artifact for any code that processes data and produces results

DATASET executor scope:
  Output: data_out.json with rows of {input, output, metadata_fold, ...} — raw data only, no derived computations
  DOES: Download/generate datasets, analyze candidates to pick the best ones, standardize to JSON schema (features, labels, folds, metadata), validate schema, split into full/mini/preview
  DOES NOT: Run experiments, train models, compute derived statistics (PID/MI/correlations/synergy matrices) as final output
  If you need to COMPUTE something from data (synergy matrices, MI scores, timing benchmarks), use an EXPERIMENT artifact instead

EVALUATION executor scope:
  Output: eval_out.json with evaluation results
  DOES: Any evaluation of experiment results — metrics, statistical tests, ablations, comparisons, visualizations, robustness checks, error analysis, etc.
  DOES NOT: Implement new methods (use EXPERIMENT), collect data (use DATASET)
  This is for analyzing experiment outputs from any angle

PROOF executor scope:
  Output: Lean 4 proof files (.lean) with verified theorems
  DOES: Write and verify Lean 4 formal proofs with Mathlib, iterative compilation
  DOES NOT: Run Python experiments, collect data, do empirical analysis
  Use only when formal mathematical guarantees are needed
</artifact_executor_scope>

<artifact_planning_rules>
RESEARCH: Plan early — findings guide dataset selection, experiment design, and methodology.
EXPERIMENT: Must depend on at least one DATASET. Define clear metrics and baselines before running. Consider trying multiple method variations rather than a single approach.
DATASET:
- Plan for REAL third-party datasets (HuggingFace, Kaggle, direct-download URLs) — downloadable within time and size constraints
- Describe dataset criteria (domain, size, format) — executors find exact sources, but you can suggest candidates or search directions
- ALWAYS prefer real datasets over synthetic. Synthetic is a LAST RESORT only when no suitable real data exists
EVALUATION: Must depend on at least one EXPERIMENT. Focus on statistical rigor and validity checks.
PROOF: Use only when the hypothesis requires formal mathematical guarantees. Lean 4 + Mathlib.
</artifact_planning_rules>

<existing_artifacts>
--- Item 1 ---
id: art_6ieqVR18TTbx
type: research
title: Readability Evaluation Landscape Survey
summary: >-
  Comprehensive survey of the readability assessment landscape covering: (1) Standard datasets with human judgments (CLEAR,
  WeeBit, OneStopEnglish, Newsela, Cambridge), (2) Traditional readability formulas (Flesch-Kincaid, SMOG, ARI, Gunning Fog,
  Dale-Chall, Coleman-Liau) with implementations, (3) Modern ML methods (BERT, RoBERTa, Longformer) and their performance,
  (4) Evaluation metrics and benchmarks, (5) Identified gaps in current methods that Semantic Control Energy (SCE) could address.
  The research provides actionable recommendations for validating the SCE method including which datasets to use, which baselines
  to implement, and which metrics to report.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_6uOr5GlpaMfR/3_invention_loop/iter_1/gen_art/gen_art_research_1
out_expected_files:
- research_out.json
out_dependency_files:
  file_list:
  - research_out.json

--- Item 2 ---
id: art_vnKiwBm9Qy9H
type: dataset
title: Readability datasets for SCE evaluation
summary: >-
  Successfully collected, standardized, and validated 3 readability datasets for evaluating the Semantic Control Energy (SCE)
  readability method. The datasets include: (1) CLEAR Corpus - 4,724 examples with human readability judgments and traditional
  readability formula scores, (2) OneStopEnglish - 567 examples with 3 difficulty levels (Elementary/Intermediate/Advanced),
  and (3) WikiLarge - 299,062 examples of Wikipedia→Simple Wikipedia text simplification pairs. All datasets were standardized
  to the exp_sel_data_out.json schema with 'input' (text) and 'output' (readability score/difficulty) fields. Train/validation/test
  splits (70/15/15) were created with stratification by difficulty level where applicable. The final output contains 213,045
  training examples across all 3 datasets, validated against the schema and ready for SCE method evaluation. Dataset provenance
  was verified through published papers and HuggingFace Hub documentation. Total size is ~158MB, under the 300MB limit. Full
  documentation including README with usage examples was created.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_6uOr5GlpaMfR/3_invention_loop/iter_1/gen_art/gen_art_dataset_1
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json
out_dependency_files:
  file_list:
  - data.py
  - full_data_out.json
  - mini_data_out.json
  - preview_data_out.json
  data_file_paths:
  - full_data_out.json
  - mini_data_out.json
  - preview_data_out.json

--- Item 3 ---
id: art_CYCcKfEseq9J
type: experiment
title: Semantic Control Energy Readability Scoring
summary: >-
  Implemented Semantic Control Energy (SCE), a novel readability metric based on control theory that models text as a dynamical
  system trajectory in embedding space. The method computes the energy needed to track semantic transitions between sentences.
  Implemented baselines: Flesch-Kincaid, SMOG, and Coleman-Liau readability formulas. Experiment on synthetic dataset (21
  examples with varying readability levels) shows SCE achieves moderate positive correlation (Pearson r=0.43) with true grade
  levels, while traditional metrics achieve strong correlation (r>0.95). Processing time is <1ms per document. The output
  includes method.py implementation and method_out.json results in valid exp_gen_sol_out schema format with full/mini/preview
  versions.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_6uOr5GlpaMfR/3_invention_loop/iter_1/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json
out_dependency_files:
  file_list:
  - method.py
  - full_method_out.json
  - mini_method_out.json
  - preview_method_out.json
</existing_artifacts>

<current_paper>
The current paper draft — represents the research story so far.

Use this to understand what's working, what's not, and what gaps remain.
Gaps and weak results signal what to try differently — not what to conclude.

# Semantic Control Energy: A Dynamical Systems Approach to Text Readability Assessment

## Abstract

Traditional readability formulas (Flesch-Kincaid, SMOG, Coleman-Liau) rely on surface-level features such as sentence length and word complexity, which fail to capture the cognitive effort required to track meaning across a text. We introduce **Semantic Control Energy (SCE)**, a novel readability metric that models text as a dynamical system trajectory through semantic embedding space and quantifies the minimum "control energy" required to follow the semantic progression. Drawing on optimal control theory, SCE measures the cumulative squared norm of semantic transitions between sentences, yielding a scalar score that reflects how abruptly meaning shifts from one sentence to the next. We evaluate SCE on a synthetic readability dataset spanning three grade-level tiers (simple, medium, complex) and compare against three traditional baselines: Flesch-Kincaid, SMOG, and Coleman-Liau. While traditional formulas achieve strong Pearson correlations (r > 0.91) with true grade levels on texts where surface features dominate, SCE captures a complementary signal—the smoothness of semantic flow—that surface metrics cannot detect. We further analyze SCE's computational efficiency (<1 ms per document) and discuss its theoretical connection to optimal transport and dynamical systems approaches in natural language processing. Our proof-of-concept experiment establishes SCE as a theoretically grounded, computationally efficient readability signal that can augment traditional formulas, particularly for texts where semantic coherence—not vocabulary difficulty—is the primary barrier to comprehension.

**Keywords:** readability assessment, semantic trajectories, optimal control theory, dynamical systems, text embedding

---

# 1 Introduction

Readability assessment—the automatic prediction of how difficult a text is to understand—has practical importance in education, content recommendation, and assistive technologies for language learners. Traditional readability formulas such as Flesch-Kincaid Grade Level (FKGL) [7], the SMOG index [10], and the Coleman-Liau Index [3] have served as standard tools for decades. These formulas operate on surface-level statistics: they count words per sentence, syllables per word, and characters per word, then combine these counts in a linear regression to predict a "grade level" [1].

Despite their simplicity and widespread adoption, traditional formulas have a well-documented limitation: they rely on "weak proxies of word decoding (i.e., characters or syllables per word) and syntactic complexity (i.e., number of words per sentence)" while ignoring "text features that are important components of reading models including text cohesion and semantics" [1]. A text can use simple words yet remain incomprehensible if its sentences jump erratically between unrelated topics; conversely, a text can use sophisticated vocabulary yet remain readable if its semantic progression is smooth and well-signposted.

This limitation points to a deeper issue: readability is not merely a function of local lexical or syntactic difficulty. It is also a function of **semantic flow**—the cognitive work a reader must expend to track how meaning evolves across sentences and paragraphs. Current information-theoretic approaches (e.g., compression-based metrics, Kolmogorov complexity estimates) capture static text complexity but not the *dynamic* cost of semantic navigation [6].

In this paper, we propose a new framework for quantifying readability that draws on **optimal control theory** and **dynamical systems**. The core idea is to treat a text as a trajectory through a continuous semantic embedding space (e.g., SBERT embeddings [11]). Each sentence maps to a point in this space; the sequence of sentences traces a trajectory. The readability of the text corresponds to the "control energy" needed to traverse this trajectory—that is, how large the semantic "jumps" are from sentence to sentence, and how much cognitive effort is required to follow them.

Formally, we model the semantic trajectory as a discrete-time dynamical system:
$$
\mathbf{x}_{t+1} = \mathbf{x}_t + \mathbf{u}_t + \mathbf{w}_t
$$
where $\mathbf{x}_t \in \mathbb{R}^d$ is the semantic state (sentence embedding) at position $t$, $\mathbf{u}_t$ is the "control input" (the semantic transition from sentence $t$ to $t+1$), and $\mathbf{w}_t$ is noise. The **Semantic Control Energy (SCE)** of a text is defined as the cumulative squared norm of the control inputs:
$$
\text{SCE} = \frac{1}{T-1} \sum_{t=1}^{T-1} \|\mathbf{u}_t\|^2 = \frac{1}{T-1} \sum_{t=1}^{T-1} \|\mathbf{x}_{t+1} - \mathbf{x}_t\|^2
$$
where $T$ is the number of sentences. Intuitively, SCE measures the average "semantic work" needed to move from each sentence to the next. Texts with smooth, predictable semantic progressions have low SCE; texts with jarring topic shifts or repetitive loops have high SCE.

[FIGURE:fig1]

Our main contributions are:

1. **A novel readability metric grounded in control theory:** We define SCE and show how it captures semantic flow, a dimension of readability that traditional surface-based formulas cannot measure.

2. **An efficient algorithm:** SCE requires only sentence embedding extraction and pairwise difference computations, running in <1 ms per document on standard hardware.

3. **An empirical proof-of-concept:** We evaluate SCE on a synthetic dataset with three readability tiers and compare against Flesch-Kincaid, SMOG, and Coleman-Liau. We report Pearson correlations with true grade levels and analyze where SCE succeeds or fails relative to baselines.

4. **A discussion of limitations and future work:** We identify key improvements needed to make SCE competitive with state-of-the-art readability assessors, including the use of pretrained SBERT embeddings, evaluation on standard benchmarks (CLEAR, OneStopEnglish), and integration with machine learning models.

---

# 2 Related Work

## 2.1 Traditional Readability Formulas

The Flesch Reading Ease formula [7] and its derivative Flesch-Kincaid Grade Level [8] remain the most widely used readability metrics. FKGL predicts U.S. grade level from average sentence length and average word syllables. The SMOG index [10] counts polysyllabic words and is widely used for health-related texts. The Coleman-Liau Index [3] uses character counts rather than syllables, making it easier to computerize. The Automated Readability Index (ARI) similarly uses character-based features [5].

All these formulas share a common limitation: they treat readability as a linear function of surface statistics, ignoring semantics and discourse structure. The CLEAR corpus paper explicitly criticizes this approach, noting that traditional formulas "ignore many text features that are important components of reading models including text cohesion and semantics" [1].

## 2.2 Modern ML-based Readability Assessment

Recent work has applied transformer models to readability assessment. Imperial (2021) demonstrated that BERT embeddings alone can effectively predict readability [12]. Martinc et al. (2021) showed that BERT raises state-of-the-art classification accuracy on the WeeBit dataset by approximately 4% compared to traditional baselines [12]. Lee et al. (2021) achieved 99% classification accuracy on the OneStopEnglish dataset using a RoBERTa–Random Forest hybrid that combines neural and handcrafted linguistic features [9]. Meng et al. (2020) reported approximately 92% accuracy on WeeBit using a BERT-based ReadNet architecture [4].

These results demonstrate that neural models capture readability signals beyond surface statistics. However, they do not explicitly model semantic flow as a dynamical process. SCE offers a complementary approach: a theoretically interpretable metric that quantifies semantic coherence directly.

## 2.3 Semantic Coherence and Embedding-Based Metrics

Coh-Metrix measures textual coherence using Latent Semantic Analysis (LSA) to compute similarity between adjacent text segments [2]. While related to our approach, Coh-Metrix relies on LSA (which requires term-document matrix factorization) rather than modern contextual embeddings, and it measures static coherence rather than the *energy cost* of semantic navigation.

Word Mover's Distance (WMD) uses optimal transport to measure the distance between two documents in word embedding space [6]. WMD computes the minimum "cost" to transform one document's word distribution into another's. Our approach differs: we measure the control energy along a *trajectory* of sentences within a single document, not the transport cost between two static documents.

## 2.4 Control Theory and Dynamical Systems in NLP

Optimal control theory, particularly the Linear Quadratic Regulator (LQR), is widely used in engineering to design controllers that minimize energy expenditure [8]. In NLP, dynamical systems perspectives have been applied to semantic navigation [13] and concept trajectory analysis [4]. To our knowledge, SCE is the first application of control-theoretic energy minimization to readability assessment.

---

# 3 Methods

## 3.1 Problem Formulation

Given a text document $D$ consisting of $T$ sentences $\{s_1, s_2, \ldots, s_T\}$, our goal is to compute a scalar readability score $R(D) \in \mathbb{R}$ that correlates with human judgments of reading difficulty. Traditional approaches compute $R(D)$ from surface statistics (e.g., words per sentence). We instead compute $R(D)$ from the semantic trajectory induced by $D$ in embedding space.

## 3.2 Semantic Trajectory Construction

We map each sentence $s_t$ to a $d$-dimensional embedding vector $\mathbf{x}_t \in \mathbb{R}^d$. In our implementation, we explore two embedding strategies:

**Feature-based embedding (computationally efficient):** Each sentence is represented by a 10-dimensional feature vector:
- Normalized sentence length (characters / 200)
- Average word length in characters / 10
- Unique word ratio (#unique / #total words)
- Complex word ratio (#words with >6 characters / #total words)
- Normalized character count / 1000
- Normalized word count / 100
- Standard deviation of word lengths
- Binary indicators for question marks, semicolons, and capital letter usage

**SBERT embedding (semantically rich):** Each sentence is mapped to a 384-dimensional embedding using the `all-MiniLM-L6-v2` pretrained model [11]. This captures deep semantic relationships but requires more computation.

The sequence $\{\mathbf{x}_1, \mathbf{x}_2, \ldots, \mathbf{x}_T\}$ defines the semantic trajectory of the document.

## 3.3 Semantic Control Energy (SCE) Computation

The Semantic Control Energy is computed as:

$$
\text{SCE}(D) = \frac{1}{T-1} \sum_{t=1}^{T-1} \|\mathbf{x}_{t+1} - \mathbf{x}_t\|_2^2
$$

where $\|\cdot\|_2$ denotes the Euclidean norm. The normalization by $T-1$ ensures that SCE is comparable across documents of different lengths.

**Interpretation:** Each term $\|\mathbf{x}_{t+1} - \mathbf{x}_t\|_2^2$ is the squared "semantic jump" from sentence $t$ to $t+1$. Large jumps indicate abrupt topic changes or semantic discontinuities, which increase cognitive load. Small jumps indicate smooth semantic progression, which reduces cognitive load. The cumulative energy reflects the total cognitive work of reading the text.

[FIGURE:fig2]

## 3.4 Baseline Readability Formulas

We implement three standard baselines:

**Flesch-Kincaid Grade Level (FKGL):**
$$
\text{FKGL} = 0.39 \left(\frac{\text{total words}}{\text{total sentences}}\right) + 11.8 \left(\frac{\text{total syllables}}{\text{total words}}\right) - 15.59
$$

**SMOG Index:**
$$
\text{SMOG} = 1.0430 \sqrt{\frac{\text{polysyllables} \times 30}{\text{sentences}}} + 3.1291
$$
where "polysyllables" are words with 3 or more syllables.

**Coleman-Liau Index:**
$$
\text{Coleman-Liau} = 0.0588 \times \left(\frac{\text{characters}}{\text{words}} \times 100\right) - 0.296 \times \left(\frac{\text{words}}{\text{sentences}} \times 100\right) - 15.8
$$

All baselines are implemented from scratch in Python, with syllable counting via a rule-based algorithm.

## 3.5 Connection to Optimal Control Theory

SCE can be derived from an optimal control perspective. Consider a discrete-time linear dynamical system:
$$
\mathbf{x}_{t+1} = \mathbf{x}_t + \mathbf{u}_t + \mathbf{w}_t
$$
where the "control input" $\mathbf{u}_t$ represents the intended semantic transition, and $\mathbf{w}_t$ is zero-mean noise. The optimal control problem minimizes:
$$
J = \sum_{t=1}^{T-1} \|\mathbf{u}_t\|^2 + \lambda \sum_{t=1}^T \|\mathbf{x}_t - \mathbf{x}_t^{\text{ideal}}\|^2
$$
If we assume the observed trajectory $\{\mathbf{x}_t\}$ is optimal (i.e., the writer has minimized control effort subject to staying close to an ideal trajectory), then the minimum control cost is exactly SCE. Thus, SCE estimates the *a priori* cognitive effort needed to produce (or comprehend) the text.

---

# 4 Experiments

## 4.1 Dataset

We evaluate on a synthetic readability dataset consisting of 60 examples across three difficulty tiers:

- **Simple (grade 1-3):** 20 examples using basic vocabulary and simple sentence structures (e.g., "The cat sat on the mat.")
- **Medium (grade 4-8):** 20 examples using moderate vocabulary and compound sentences (e.g., "The environment faces many challenges today.")
- **Complex (grade 9-16):** 20 examples using sophisticated vocabulary and academic prose (e.g., "The implementation of comprehensive methodological frameworks necessitates a multifaceted approach.")

Each example has a "true" grade level assigned stochastically within its tier range. The dataset is designed to test whether SCE can distinguish texts with different semantic flow characteristics, independent of vocabulary difficulty.

[ARTIFACT:art_CYCcKfEseq9J]

## 4.2 Evaluation Protocol

We compute Pearson correlation between each method's predictions and the true grade levels. Pearson $r$ ranges from -1 to 1, with higher values indicating stronger linear agreement. We also measure computational efficiency: average processing time per document in milliseconds.

## 4.3 Results

Table 1 reports Pearson correlation coefficients for all methods.

| Method | Pearson $r$ | 95% CI |
|--------|-------------|---------|
| SCE (feature-based) | -0.214 | [-0.612, 0.271] |
| Flesch-Kincaid | 0.919 | [0.781, 0.969] |
| SMOG | 0.916 | [0.776, 0.967] |
| Coleman-Liau | -0.551 | [-0.813, -0.150] |

**Key findings:**

1. **Traditional formulas perform well on this dataset:** FKGL and SMOG achieve $r > 0.91$, confirming that surface statistics are strongly predictive when vocabulary and syntax differ systematically across tiers.

2. **SCE shows negative correlation:** The feature-based SCE implementation achieves $r = -0.214$, which is not statistically significant given the small sample size ($n=60$, $p > 0.05$). The negative sign indicates that documents with larger semantic jumps tend to have *lower* (easier) grade levels in this synthetic dataset—an artifact of how the data was constructed (simple texts use varied templates that produce varied feature vectors).

3. **Coleman-Liau performs poorly:** The negative correlation ($r = -0.551$) suggests the formula is miscalibrated for this dataset, likely because character-based features behave differently in short sentences.

[FIGURE:fig3]

## 4.4 Computational Efficiency

SCE processes documents in **0.56 milliseconds** on average (measured over 15 examples on a standard CPU). This is comparable to traditional formulas (<1 ms) and orders of magnitude faster than SBERT-based approaches (~50-200 ms depending on document length). The efficiency stems from SCE's simple computation: embedding extraction (or feature computation) followed by pairwise Euclidean distances.

## 4.5 Ablation: Embedding Strategy

We compare feature-based embeddings against SBERT embeddings on a 15-example subset. SBERT-based SCE achieves higher correlation with human judgments of semantic coherence (qualitative evaluation), but the improvement does not translate to higher Pearson $r$ with grade levels on this synthetic dataset. This suggests that **the choice of embedding space is critical**: feature-based embeddings capture surface properties (sentence length, word complexity) that correlate with grade level, while SBERT embeddings capture semantic properties that may not align with traditional grade-level annotations.

---

# 5 Discussion

## 5.1 Why SCE Underperforms on Synthetic Data

The negative correlation between SCE and grade level on our synthetic dataset reveals an important limitation: **SCE measures semantic jump magnitude, not vocabulary difficulty**. In our dataset, "simple" texts use varied templates ("The cat sits", "I like cake", "Mom runs fast") that produce varied feature vectors and hence large SCE values. "Complex" texts use consistent academic templates that produce similar feature vectors and hence small SCE values. Thus, SCE is **anti-correlated** with traditional grade level on this particular data.

This limitation is not a flaw in SCE itself, but rather a mismatch between what SCE measures (semantic coherence) and what traditional grade levels measure (vocabulary and syntax difficulty). In real-world texts, these two signals are often positively correlated: texts with difficult vocabulary also tend to have more complex semantic structures. However, they can also diverge—and it is precisely in these cases that SCE provides novel information.

## 5.2 When Does SCE Provide Novel Signal?

SCE is designed to detect texts that are **semantically incoherent despite using simple words**. Consider the following example:

> "Dogs bark loudly at mailboxes. The quantum vacuum fluctuates constantly. Yesterday's sandwich contained pickles. Economic indicators suggest inflationary pressure. Beethoven composed nine symphonies."

This text uses simple words and short sentences (FKGL would predict "easy"), but its semantic trajectory is extremely erratic (SCE would predict "difficult"). Human readers would find this text confusing not because of vocabulary, but because of topic whiplash. SCE captures this dimension of readability that traditional formulas miss.

[FIGURE:fig4]

## 5.3 Connection to Human Readability Judgments

The CLEAR corpus [1] provides human readability judgments from 1,116 teachers who made 111,347 pairwise comparisons of text excerpts. These judgments incorporate factors beyond vocabulary difficulty, including discourse coherence, background knowledge requirements, and genre conventions. SCE offers a way to operationalize "discourse coherence" as a quantifiable metric. We hypothesize that SCE will show stronger correlation with CLEAR judgments than with FKGL-predicted grade levels, because CLEAR captures global readability while FKGL captures local difficulty.

## 5.4 Limitations

1. **Embedding sensitivity:** SCE's performance depends heavily on the quality of the sentence embeddings. Feature-based embeddings are computationally efficient but cannot capture deep semantic relationships. SBERT embeddings are semantically rich but require more computation and may be biased toward certain domains.

2. **Small-scale evaluation:** Our experiments use a synthetic dataset of 60 examples. While this allows controlled analysis, it does not reflect the diversity of real-world texts. Evaluation on standard benchmarks (CLEAR, OneStopEnglish, WeeBit) is needed.

3. **Negative correlation on synthetic data:** As discussed above, SCE measures semantic jump magnitude, which anti-correlates with grade level on our synthetic data. This does not invalidate SCE, but it does mean that SCE and traditional formulas capture complementary signals.

4. **Noisy sentence boundaries:** SCE assumes sentences are the units of semantic transition. In practice, sentence tokenization errors (e.g., abbreviations like "Dr." causing false sentence breaks) can introduce noise into the semantic trajectory.

## 5.5 Future Work

1. **Evaluation on standard benchmarks:** The most important next step is to evaluate SCE on the CLEAR corpus [1], OneStopEnglish [14], and WikiLarge datasets. These provide real human judgments and established evaluation protocols.

2. **SBERT integration:** Replace feature-based embeddings with pretrained SBERT embeddings (`all-MiniLM-L6-v2` or `all-mpnet-base-v2`) to capture deep semantic relationships. This requires more computation but should improve correlation with human judgments.

3. **LQR-inspired formulation:** Extend SCE to a full LQR framework where the "optimal" semantic trajectory is learned from human judgments. This would allow SCE to adapt to different genres and reading levels.

4. **Hybrid models:** Combine SCE with traditional formulas in a machine learning model (e.g., linear regression with SCE and FKGL as features). This hybrid approach should outperform either metric alone.

5. **Optimal transport extension:** Replace Euclidean distance with Wasserstein distance (or Word Mover's Distance [6]) to account for the geometry of word embedding space. This would make SCE more robust to synonym substitutions and paraphrases.

---

# 6 Conclusion

We introduced Semantic Control Energy (SCE), a novel readability metric that models text as a dynamical system trajectory in embedding space and quantifies the cognitive work needed to track semantic changes. SCE is grounded in optimal control theory, computationally efficient (<1 ms per document), and captures a dimension of readability—semantic flow—that traditional surface-based formulas cannot measure.

Our proof-of-concept experiment on a synthetic dataset shows that SCE provides a complementary signal to traditional formulas. While FKGL and SMOG achieve strong correlation with grade levels on texts where vocabulary difficulty dominates ($r > 0.91$), SCE captures semantic coherence independent of vocabulary. The negative correlation we observe on synthetic data ($r = -0.214$) reflects this complementarity: SCE measures semantic jump magnitude, which is not always aligned with traditional grade level.

The broader contribution of this work is a new conceptual framework for readability assessment: **treating reading as a control problem**, where the reader must expend cognitive energy to track the writer's semantic trajectory. This framework opens several avenues for future research, including SBERT-based SCE, LQR-inspired formulations, and hybrid models that combine SCE with traditional formulas.

We release our implementation and synthetic dataset to facilitate further research. Future work should evaluate SCE on standard readability benchmarks (CLEAR, OneStopEnglish) and explore hybrid models that combine SCE with neural approaches for state-of-the-art readability assessment.

---

# Acknowledgments

We thank the AI Inventor system for facilitating this research. We also thank the creators of the CLEAR corpus, OneStopEnglish corpus, and WikiLarge dataset for making their data publicly available.

---

# References

[1] Crossley, S., Burling, A. B., & O'Reilly, T. (2021). The CommonLit Ease of Readability (CLEAR) Corpus. *Proceedings of the 14th International Conference on Educational Data Mining*, 381-386.

[2] Graesser, A. C., McNamara, D. S., & Kulikowich, J. M. (2011). Coh-Metrix: Providing multilevel analyses of text characteristics. *Educational Researcher*, 40(5), 223-234.

[3] Coleman, M., & Liau, T. L. (1975). A computer readability formula designed for machine scoring. *Journal of Applied Psychology*, 60(2), 283-284.

[4] Fernández, R., & Morris, R. (2026). Characterizing human semantic navigation in concept production as trajectories in embedding space. *arXiv preprint arXiv:2602.05971*.

[5] Kincaid, J. P., Fishburne, R. P., Rogers, R. L., & Chissom, B. S. (1975). Derivation of new readability formulas for Navy enlisted personnel. *Naval Technical Training Command Millington TN Research Branch*.

[6] Kusner, M. J., Sun, Y., Kolkin, N. I., & Weinberger, K. Q. (2015). From word embeddings to document distances. *Proceedings of the 32nd International Conference on Machine Learning*, 957-966.

[7] Flesch, R. (1948). A new readability yardstick. *Journal of Applied Psychology*, 32(3), 221-233.

[8] Kalman, R. E. (1960). Contributions to the theory of optimal control. *Boletín de la Sociedad Matemática Mexicana*, 5(1), 102-119.

[9] Lee, B. W., Jang, Y., & Lee, J. (2021). Pushing on text readability assessment: A transformer meets handcrafted linguistic features. *Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing*, 8385-8397.

[10] McLaughlin, G. H. (1969). SMOG grading: A new readability formula. *Journal of Reading*, 12(8), 639-646.

[11] Reimers, N., & Gurevych, I. (2019). Sentence-BERT: Sentence embeddings using siamese BERT-networks. *Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing*, 3982-3992.

[12] Martinc, M., & Pollak, S. (2021). Tackling the problem of readability assessment for Slovenian. *Natural Language Engineering*, 27(5), 581-603.

[13] Kumar, S., Zhang, X., & Leskovec, J. (2019). Predicting dynamic embedding trajectory in temporal interaction networks. *Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining*, 1269-1278.

[14] Vajjala, S., & Lucic, I. (2018). OneStopEnglish corpus: A new corpus for automatic readability assessment and text simplification. *Proceedings of the 13th Workshop on Innovative Use of NLP for Building Educational Applications*, 297-304.
</current_paper>

<reviewer_feedback>
Paper reviewer feedback from the previous iteration. Your strategy MUST address these critiques.
Prioritize major issues — these are the most impactful improvements to make.

- [MAJOR] (evidence) The experimental evaluation is fundamentally inadequate. The paper evaluates ONLY on a synthetic dataset with 21 examples (not 60 as claimed in Section 4.1), where 'true' grade levels are assigned randomly within ranges. This dataset has critical flaws: (1) Simple texts use varied templates that produce varied feature vectors (high SCE), while complex texts use consistent templates (low SCE), leading to artificial anti-correlation; (2) The sample size is far too small for reliable correlation estimation; (3) Synthetic data cannot generalize to real-world readability. Despite the authors preparing real datasets (CLEAR, OneStopEnglish, WikiLarge) as described in the supplementary materials (art_vnKiwBm9Qy9H), these were NOT used in the evaluation.
  Action: Evaluate SCE on the CLEAR corpus and OneStopEnglish dataset that were already prepared. These have real human judgments and established evaluation protocols. Report Pearson correlation with human judgments (CLEAR) and classification accuracy (OneStopEnglish). This is the minimum requirement for a readability paper.
- [MAJOR] (methodology) There are significant discrepancies between the paper description and the actual implementation: (1) Section 3.2 describes a 10-dimensional feature vector for SCE, but the code (method.py) only implements a 2-dimensional vector (normalized sentence length and word count); (2) The paper reports SCE correlation as r = -0.214 with 95% CI [-0.612, 0.271] in Table 1, but the RESULTS.md file shows r = 0.4340, and the actual experiment output shows inconsistent results; (3) The Flesch-Kincaid baseline is implemented incorrectly as 'words/3' rather than the proper formula (0.39*(words/sentences) + 11.8*(syllables/words) - 15.59). These discrepancies undermine the paper's credibility.
  Action: Ensure the implementation matches the paper description. Implement the full 10-dimensional feature vector OR use SBERT embeddings as described. Use established implementations (textstat package) for baseline formulas. Re-run experiments and report accurate results. Provide code that exactly reproduces the paper's numbers.
- [MAJOR] (novelty) The core idea of SCE—measuring semantic coherence via distances between sentence embeddings—is not novel. Coh-Metrix (2001) measures textual coherence using LSA to compute similarity between adjacent segments. Word Mover's Distance (2015) uses optimal transport for document similarity. More recent work uses SBERT embeddings to measure semantic similarity. The 'control energy' framing adds minimal novelty: SCE is simply the sum of squared Euclidean distances between consecutive embeddings, which is a straightforward baseline that does not require control theory. The paper's claim that 'SCE is the first application of control-theoretic energy minimization to readability assessment' is misleading—the connection to control theory is superficial.
  Action: Reframe the contribution more honestly. Acknowledge that measuring semantic coherence via embedding distances is established. Focus on what is truly novel: perhaps the specific formulation, computational efficiency, or empirical findings. Compare against Coh-Metrix and SBERT cosine similarity baselines to show SCE's relative advantage. Consider removing or de-emphasizing the control theory claims unless a rigorous connection can be established.
- [MAJOR] (rigor) The connection to optimal control theory in Section 3.5 is not mathematically sound. The paper states that SCE can be derived from minimizing J = sum(||u_t||^2) + lambda*sum(||x_t - x_t^ideal||^2), but then claims that if the observed trajectory is optimal, 'the minimum control cost is exactly SCE.' This is incorrect: the optimal control cost depends on the ideal trajectory x_t^ideal, which is never defined. Furthermore, the dynamical system formulation x_{t+1} = x_t + u_t + w_t is not used in the actual SCE computation—SCE simply computes ||x_{t+1} - x_t||^2, which ignores the noise term w_t and any notion of optimal control. The control theory framing appears to be post-hoc justification rather than genuine theoretical grounding.
  Action: Either provide a rigorous optimal control derivation that leads to SCE, or remove the control theory claims and present SCE as a simple heuristic metric. If keeping the control theory connection, define the ideal trajectory, derive the optimal controller, and show that SCE emerges from this derivation. Alternatively, reframe as 'inspired by control theory' rather than 'derived from'.
- [MINOR] (evidence) The paper reports 95% confidence intervals for Pearson correlations (Table 1), but with n=60 (or actually n=21 in the code), these CIs are unreliable. Pearson correlation CIs require assumptions about the underlying distribution that may not hold. Additionally, the CI for SCE [-0.612, 0.271] includes zero, indicating the correlation is not statistically significant, but the paper does not acknowledge this.
  Action: Report p-values alongside correlations to indicate statistical significance. Use bootstrap CIs rather than parametric CIs for small samples. Acknowledge when correlations are not statistically significant.
- [MINOR] (scope) The paper claims SCE is 'computationally efficient (<1 ms per document)' but this measurement is misleading. The feature-based embedding used in the experiment is trivial to compute, but the paper also promotes SBERT embeddings which take 50-200ms per document. The <1ms claim only applies to the feature-based version, which the paper acknowledges performs poorly. A fairer comparison would report timing for SBERT-based SCE, which is the version that would actually be used in practice.
  Action: Report computational efficiency for both feature-based and SBERT-based SCE. Compare against traditional formulas AND modern ML methods (BERT-based readability assessors). Acknowledge the trade-off between efficiency and accuracy.
- [MINOR] (clarity) Figure placeholders are used throughout the paper ([FIGURE:fig1], etc.) but no actual figures are provided. While the instructions say to assume figures show what captions describe, the figures are essential for understanding: (1) Figure 1 should illustrate the semantic trajectory concept; (2) Figure 2 should visualize SCE computation; (3) Figure 3 should show correlation results; (4) Figure 4 should illustrate the 'semantic whiplash' example. Without figures, the paper is difficult to follow.
  Action: Generate actual figures showing: (1) Semantic trajectories in embedding space for simple vs. complex texts; (2) SCE computation as squared distances; (3) Scatter plots of SCE vs. grade level; (4) Example of semantically incoherent text. Ensure figures are well-labeled and support the paper's claims.
</reviewer_feedback>

<task>
Generate 1 research strategy for THIS iteration.

**ARTIFACT LIMIT: Each strategy may contain AT MOST 3 artifact directions.** Focus on the highest-impact artifacts. Quality over quantity.

Each strategy should:
1. Define a clear OBJECTIVE - what novel contribution we're building toward
2. Plan artifacts to execute NOW - specify type, objective, approach, and depends_on for each
3. Account for parallel execution - all strategies and all planned artifacts run simultaneously, their artifacts are combined into one shared pool


</task><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_6uOr5GlpaMfR/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_6uOr5GlpaMfR/3_invention_loop/iter_2/gen_strat/gen_strat_1/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "ArtifactDep": {
      "description": "A single dependency on an existing artifact, with a short type label.\n\n``id`` and ``label`` are LLM-generated at strategy time. ``label`` is free-text but\nshort \u2014 a word or two naming the type of dependency, not a sentence.\n\n``relation_type`` and ``relation_rationale`` are populated later, in upd_hypo,\nusing the MultiCite citation-function typology (Lauscher et al., NAACL 2022).\nThey are absent at strategy time and may stay absent for legacy runs.",
      "properties": {
        "id": {
          "description": "ID of an existing artifact this artifact depends on",
          "title": "Id",
          "type": "string"
        },
        "label": {
          "description": "Short free-text label naming the type of this dependency (a word or two, not a sentence)",
          "title": "Label",
          "type": "string"
        }
      },
      "required": [
        "id",
        "label"
      ],
      "title": "ArtifactDep",
      "type": "object"
    },
    "ArtifactDirection": {
      "description": "High-level direction for an artifact to execute this iteration.\n\nID is code-assigned (LLMPrompt only \u2014 visible in prompts, not LLM-generated).",
      "properties": {
        "type": {
          "description": "Type of artifact to create",
          "enum": [
            "experiment",
            "research",
            "proof",
            "evaluation",
            "dataset"
          ],
          "title": "Type",
          "type": "string"
        },
        "objective": {
          "description": "What we want to achieve with this artifact",
          "title": "Objective",
          "type": "string"
        },
        "approach": {
          "description": "High-level direction/method",
          "title": "Approach",
          "type": "string"
        },
        "depends_on": {
          "description": "Existing artifacts this depends on, each with a short type label",
          "items": {
            "$ref": "#/$defs/ArtifactDep"
          },
          "title": "Depends On",
          "type": "array"
        }
      },
      "required": [
        "type",
        "objective",
        "approach"
      ],
      "title": "ArtifactDirection",
      "type": "object"
    },
    "Strategy": {
      "description": "A research strategy.\n\nContent fields have LLMPrompt + LLMStructOut markers.\n``id`` is code-assigned (LLMPrompt only \u2014 visible in prompts, not LLM-generated).\n\nID format: gen_strat_idx{N}",
      "properties": {
        "title": {
          "description": "Strategy name in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters).",
          "title": "Title",
          "type": "string"
        },
        "objective": {
          "description": "The novel contribution we're building toward",
          "title": "Objective",
          "type": "string"
        },
        "rationale": {
          "description": "Why this strategy is promising",
          "title": "Rationale",
          "type": "string"
        },
        "artifact_directions": {
          "description": "Artifacts to execute THIS iteration",
          "items": {
            "$ref": "#/$defs/ArtifactDirection"
          },
          "title": "Artifact Directions",
          "type": "array"
        },
        "expected_outcome": {
          "description": "What we'll have after this iteration's artifacts complete",
          "title": "Expected Outcome",
          "type": "string"
        },
        "summary": {
          "default": "",
          "description": "Brief summary of the strategy and its expected contribution",
          "title": "Summary",
          "type": "string"
        }
      },
      "required": [
        "title",
        "objective",
        "rationale",
        "artifact_directions",
        "expected_outcome"
      ],
      "title": "Strategy",
      "type": "object"
    }
  },
  "description": "Top-level wrapper for LLM strategy generation output.",
  "properties": {
    "strategies": {
      "description": "List of generated strategies",
      "items": {
        "$ref": "#/$defs/Strategy"
      },
      "title": "Strategies",
      "type": "array"
    }
  },
  "required": [
    "strategies"
  ],
  "title": "Strategies",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `/ai-inventor/aii_data/runs/run_6uOr5GlpaMfR/3_invention_loop/iter_2/gen_strat/gen_strat_1/.sdk_openhands_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-07-09 00:50:22 UTC

```
Propose a simple, novel machine-learning method for scoring text readability and validate it.
```

### [3] SYSTEM-USER prompt · 2026-07-09 01:05:45 UTC

````
YOUR PREVIOUS SESSION WAS INTERRUPTED: A single operation exceeded the 720s message timeout. Each individual operation must complete within 720s. Do NOT mock, skip, or compromise your execution — still do the real work. Try to make operations run faster if possible. If a command genuinely takes longer than 720s, split it into sequential parts that each complete within the time limit.

Last messages before interruption:
  - [agent_system_user_prompt]: <hypothesis>
Your strategy should advance this hypothesis.

kind: hypothesis
title: Semantic Coherence Distance for Readability Assessment
hypothesis: >-
  Text readability has a semantic coherence component that can be measured by computing distances between sentence embeddings
  in a semantic traj
  - [agent_human_user_prompt]: Propose a simple, novel machine-learning method for scoring text readability and validate it.
  - [agent_think]: The user wants me to generate a research strategy for iteration 2 of 2 in the AI Inventor system. Let me analyze the current state:

1. **Hypothesis**: Semantic Coherence Distance for Readability Assessment - measuring readability through semantic trajectories and coherence distances, complementary 
  - [agent_response]: Looking at the reviewer feedback and the current state of the research, I need to address the major criticisms in this final iteration. The key issues are:

1. **MAJOR**: Evaluation only on inadequate synthetic data (21 examples) - need to use the prepared CLEAR and OneStopEnglish datasets
2. **MAJO
  - [agent_tool_call] file_editor: Tool: file_editor
{
  "command": "view",
  "path": "/ai-inventor/aii_data/runs/run_6uOr5GlpaMfR/user_uploads",
  "file_text": null,
  "old_str": null,
  "new_str": null,
  "insert_line": null,
  "view_range": null
}
  - [agent_tool_result] file_editor: Tool: file_editor
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "Here's the files and directories up to 2 levels deep in /ai-inventor/aii_data/runs/run_6uOr5GlpaMfR/user_uploads, excluding hidden items:\n/ai-inventor/aii_data/runs/run_6uOr5GlpaMfR/user_uploads/"}], "is_error":
  - [agent_response]: No user uploads. Now let me check the existing artifacts to understand what's available for this iteration. Let me view the workspace structure and check the existing experiment and dataset artifacts.
  - [agent_tool_call] file_editor: Tool: file_editor
{
  "command": "view",
  "path": "/ai-inventor/aii_data/runs/run_6uOr5GlpaMfR/3_invention_loop/iter_1/gen_art/gen_art_experiment_1",
  "file_text": null,
  "old_str": null,
  "new_str": null,
  "insert_line": null,
  "view_range": null
}
  - [agent_tool_result] file_editor: Tool: file_editor
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "Here's the files and directories up to 2 levels deep in /ai-inventor/aii_data/runs/run_6uOr5GlpaMfR/3_invention_loop/iter_1/gen_art/gen_art_experiment_1, excluding hidden items:\n/ai-inventor/aii_data/runs/run_6u

CONTINUE FOLLOWING THESE INSTRUCTIONS:

<hypothesis>
Your strategy should advance this hypothesis.

kind: hypothesis
title: Semantic Coherence Distance for Readability Assessment
hypothesis: >-
  Text readability has a semantic coherence component that can be measured by computing distances between sentence embeddings
  in a semantic trajectory, capturing aspects of reading difficulty not reflected in surface-level readability formulas. However,
  this semantic distance signal may be complementary to rather than a replacement for traditional surface-based metrics, and
  its effectiveness depends critically on the choice of embedding space and evaluation dataset.
motivation: >-
  Current readability formulas (Flesch-Kincaid, etc.) rely on surface features like sentence length and word complexity, missing
  the dynamic flow of meaning. Information-theoretic approaches (compression/Kolmogorov complexity) capture static complexity
  but not the cognitive effort of semantic navigation. By treating text as a dynamical system trajectory through semantic
  space and measuring the optimal control energy needed to follow it, we can capture a fundamental aspect of readability:
  how much cognitive 'work' a reader must expend to track the evolving meaning.
assumptions:
- >-
  Text can be meaningfully represented as a trajectory in a continuous semantic embedding space
- >-
  Human reading comprehension requires cognitive resources proportional to the 'control effort' needed to track semantic changes
- >-
  Optimal control theory provides a valid framework for quantifying the minimum effort needed to navigate semantic transitions
- >-
  The energy cost of semantic transitions correlates with subjective reading difficulty
investigation_approach: >-
  1. Map sentences to embeddings (using SBERT or similar) to create a semantic trajectory. 2. Model the trajectory as a dynamical
  system: x(t+1) = x(t) + u(t) + noise, where x is the semantic state and u is the 'control input'. 3. Compute the LQR (Linear
  Quadratic Regulator) cost: sum of squared deviations from optimal path + control effort. 4. Alternative: compute the cumulative
  Wasserstein distance or semantic 'work' along the trajectory. 5. Compare against traditional readability formulas and human
  judgments on standard datasets (CLEAR corpus, WeeBit, etc.). 6. Evaluate whether SCE captures aspects of readability that
  traditional formulas miss (e.g., texts with simple words but jarring topic shifts).
success_criteria: >-
  1. SCE scores should correlate with human readability judgments at least as well as traditional formulas (Flesch-Kincaid,
  SMOG). 2. SCE should better predict reading comprehension scores than surface-based formulas on texts with simple vocabulary
  but poor semantic flow. 3. Ablation studies should show that the 'energy' component (penalizing large semantic jumps) is
  necessary for predictive power. 4. The method should be computationally feasible: <1 second per document on standard hardware.
related_works:
- >-
  Kolmogorov complexity using compression (Ehret 2018): Also uses information theory but measures static complexity of entire
  text rather than dynamic semantic navigation cost. Our approach is fundamentally different - we measure the optimal control
  energy of the semantic trajectory, not compression ratio.
- >-
  Bigram Semantic Distance (Kenett et al. 2017): Measures semantic distance between consecutive words/sentences. Our approach
  extends this by considering the optimal control effort over the ENTIRE trajectory (not just pairwise distances) and incorporates
  a dynamical systems framework.
- >-
  Coh-Metrix and coherence measures: Measure local coherence and connectivity. Our approach is global - measuring the total
  'energy' needed to follow the semantic flow, which captures both local coherence and global trajectory smoothness.
- >-
  Word Mover's Distance (Kusner et al. 2015): Uses optimal transport for document similarity. Our approach is different: we
  measure the control energy needed to follow a trajectory, not the transport cost between two static distributions.
inspiration: >-
  The hypothesis combines insights from three distant fields: (1) Control Theory - specifically Linear Quadratic Regulator
  (LQR) theory which minimizes energy for trajectory tracking, (2) Optimal Transport theory - which provides Wasserstein distance
  for measuring semantic transition costs, and (3) Physics/Dynamical Systems - which views readability as the 'work' required
  to move through semantic space. The core insight is that readable text should have a 'smooth' semantic trajectory requiring
  minimal control corrections, analogous to how a well-designed controller keeps a system on a desired path with minimal energy
  expenditure.
terms:
- term: Semantic Trajectory
  definition: >-
    The path traced by sequential units of text (sentences or paragraphs) when mapped to a continuous vector space representing
    meaning (e.g., through sentence embeddings).
- term: Control Energy
  definition: >-
    In control theory, the cumulative effort (measured as squared control inputs) required to make a system follow a desired
    trajectory. In our context, it represents the cognitive work needed to track semantic changes in text.
- term: LQR (Linear Quadratic Regulator)
  definition: >-
    An optimal control method that finds the control inputs minimizing a quadratic cost function of state deviations and control
    effort, commonly used in engineering to design stable, efficient controllers.
- term: Semantic Embedding Space
  definition: >-
    A high-dimensional vector space where words, sentences, or documents are mapped such that semantic similarity corresponds
    to geometric proximity (e.g., cosine similarity in the embedding space).
- term: Optimal Transport (Wasserstein Distance)
  definition: >-
    A mathematical framework for measuring the distance between probability distributions by computing the minimum 'cost'
    to transform one distribution into another, often visualized as moving 'mass' from one configuration to another.
summary: >-
  This hypothesis proposes a novel readability metric based on control theory: readable text requires minimal 'control energy'
  to follow its semantic trajectory. By modeling text as a dynamical system in embedding space and computing the optimal control
  cost, we can quantify readability as the cognitive work needed for semantic navigation.
_relation_rationale: >-
  Narrowed from grand control theory claims to testable semantic distance metric, same goal of capturing coherence.
_confidence_delta: decreased
_key_changes:
- >-
  Removed unsound control theory framing; SCD is now a simple heuristic metric, not derived from optimal control
- >-
  Acknowledged that measuring semantic coherence via embeddings is not novel (Coh-Metrix, etc.)
- >-
  Narrowed claims: SCD may be complementary to traditional formulas, not necessarily superior
- >-
  Added requirement to evaluate on real datasets (CLEAR, OneStopEnglish) not just synthetic data
- >-
  Added honesty about negative results: original experiment showed anti-correlation on synthetic data
- >-
  Removed LQR dynamical systems formulation that was not actually implemented or mathematically justified
- >-
  Changed 'control energy' terminology to 'semantic coherence distance' to avoid misleading claims
relation_type: evolution
</hypothesis>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. Use it for study design, proper baselines, and the evaluation/validity norms this field demands.

- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
</available_domain_handbooks>

<iteration_status>
Current iteration: 2 of 2
Remaining (including this one): 1
</iteration_status>

<previous_strategies>
Strategies from the PREVIOUS iteration. You can CONTINUE these directions,
ADAPT based on what worked and what didn't in the artifacts produced, or PIVOT if results suggest a better path.

--- Strategy 1 ---
kind: strategy
id: gen_strat_1_idx1
title: Foundation and Baseline Implementation for SCE Readability
objective: >-
  Establish the foundational elements for testing the Semantic Control Energy (SCE) hypothesis: survey evaluation landscape,
  acquire standard readability datasets, and implement the core SCE method with initial baseline comparisons.
rationale: >-
  As the first iteration in a 2-iteration cycle, we must establish three critical foundations: (1) Understanding what datasets
  and evaluation benchmarks exist for readability assessment, (2) Acquiring the necessary data for evaluation, and (3) Implementing
  the novel SCE method. This parallel approach ensures that when iteration 2 arrives, we have all building blocks ready for
  comprehensive evaluation and paper writing.
artifact_directions:
- id: research_iter1_dir1
  type: research
  objective: >-
    Survey readability evaluation landscape: identify standard datasets with human judgments, understand traditional readability
    formulas (Flesch-Kincaid, SMOG, etc.), and determine evaluation benchmarks used in the field.
  approach: >-
    Conduct web research to identify: (1) Standard readability datasets with human judgment data (CLEAR corpus, WeeBit, Newsela,
    OneStopEnglish), (2) Traditional readability formulas and their implementations, (3) Evaluation metrics and benchmarks
    used in recent readability assessment papers, (4) Existing gaps that SCE could address. Search for 'readability dataset
    human judgment', 'CLEAR corpus readability', 'WeeBit dataset', 'Newsela readability', and survey recent ACL/EMNLP papers
    on readability assessment.
  depends_on: []
- id: dataset_iter1_dir2
  type: dataset
  objective: >-
    Acquire and standardize 2-3 standard readability datasets with human judgments or grade-level annotations for evaluating
    the SCE method.
  approach: >-
    Download and standardize: (1) CLEAR corpus (if available) or WeeBit dataset from HuggingFace or direct sources - contains
    texts with human readability ratings, (2) Newsela dataset or similar with leveled texts (same content at different reading
    levels), (3) Standard readability benchmark like OneStopEnglish. Transform to JSON format with fields: {text, readability_score/grade_level,
    metadata}. Create train/validation/test splits. Prioritize datasets with human judgment data over surface-level features.
  depends_on: []
- id: experiment_iter1_dir3
  type: experiment
  objective: >-
    Implement the core Semantic Control Energy (SCE) method: map sentences to semantic embeddings, model text as dynamical
    system trajectory, compute control energy metric, and compare against traditional readability formulas on preliminary
    data.
  approach: >-
    Implement SCE computation: (1) Use SBERT (all-mpnet-base-v2) to embed sentences, (2) Model semantic trajectory as dynamical
    system x(t+1) = x(t) + u(t), (3) Compute control energy as sum of ||u(t)||^2 where u(t) = x(t+1) - x(t) (simple formulation
    for initial test), (4) Alternative: compute cumulative Wasserstein distance or semantic 'work' along trajectory, (5) Compare
    SCE scores against Flesch-Kincaid, SMOG, and other traditional formulas, (6) Test on any available text data (Wikipedia
    articles, Project Gutenberg books) to verify computational feasibility (<1 second per document). Output preliminary correlation
    analysis with traditional metrics.
  depends_on: []
expected_outcome: >-
  After this iteration, we will have: (1) A comprehensive understanding of the readability evaluation landscape and available
  datasets, (2) 2-3 standardized readability datasets ready for evaluation, and (3) A working implementation of the SCE method
  with preliminary results showing computational feasibility and initial comparisons to traditional formulas. This provides
  the foundation for iteration 2 to conduct comprehensive evaluation against human judgments and write the paper.
summary: >-
  Establish foundations for SCE readability research through parallel landscape survey, dataset acquisition, and initial method
  implementation.
</previous_strategies>

<dependency_rules>
- depends_on is a list of objects {id, label} — each entry references an existing artifact and tags how it is being used
- "id" can ONLY reference IDs from <existing_artifacts> — never IDs you are proposing (all new artifacts run in parallel)
- "label" is a SHORT free-text type label (a word or two, NOT a sentence) describing what role the dep plays — e.g. "dataset", "validates", "extends", "supersedes". Required on every dep.
- Setting depends_on provides the dependency's out_dependency_files to your artifact at execution time
- If no suitable existing artifacts exist, use empty depends_on
- New artifact IDs are assigned by the system after submission — do not invent IDs for your proposed artifacts
</dependency_rules>

<available_artifact_types>
Artifact types you can plan. Use this to choose the right types for your strategy objectives.

<artifact_types>
RESEARCH
Web research to answer key questions — like a researcher making decisions.
Runtime: LLM Agent, no code execution.
Tools: the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text).
Capabilities: Find, synthesize, and compare information across sources; survey SOTA and best practices.
Deps: REQUIRED none | OPTIONAL other RESEARCH to build on prior findings

EXPERIMENT
Run code to test hypotheses, implement methods, and collect empirical results.
Runtime: Python 3.12, UV (any pip package), isolated workspace, gradual scaling (mini → full data).
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-json (schema validation), aii-openrouter-llms (call any LLM — GPT, Gemini, Llama, etc.), domain-specific as needed.
Capabilities: Implement and run any code-based experiment, compare method vs baselines.
Deps: REQUIRED at least one DATASET | OPTIONAL RESEARCH for methodology guidance

DATASET
Collect, prepare, and merge datasets for experiments and analysis.
Runtime: Python 3.12, UV, isolated workspace.
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-hf-datasets (HuggingFace Hub — ML datasets, many UCI/OpenML/Kaggle mirrors), aii-owid-datasets (Our World in Data — global statistics), aii-json (schema validation). Also any Python source (sklearn.datasets, openml, direct URLs, APIs) — must verify within 300MB limit.
Capabilities: Search, acquire, transform, combine, and standardize data from any available source.
Deps: REQUIRED none | OPTIONAL RESEARCH for guidance on what data to collect

EVALUATION
Evaluate experiment results with metrics, statistical analysis, and validity checks.
Runtime: Python 3.12, UV (any evaluation library), isolated workspace, gradual scaling matching experiment.
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-json (schema validation), aii-openrouter-llms (call any LLM — GPT, Gemini, Llama, etc.), domain-specific as needed.
Capabilities: Compute any quantitative metrics and statistical tests, analyze validity and robustness.
Deps: REQUIRED at least one EXPERIMENT | OPTIONAL DATASET if reference data needed

PROOF
Formally prove mathematical statements in Lean 4 with automated iteration.
Runtime: LLM agent with Lean 4 compiler feedback loop.
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-lean (proof verification, Mathlib search, tactics: ring, linarith, nlinarith, omega, simp, etc.)
Capabilities: Formally verify properties and inequalities, iterative proof development, lemma decomposition.
Deps: REQUIRED none | OPTIONAL RESEARCH for mathematical background
</artifact_types>
</available_artifact_types>

<artifact_executor_scope>
IMPORTANT: Each artifact executor has a focused prompt that guides it to do ONE thing well. It will NOT perform tasks outside its scope — assigning the wrong work to the wrong artifact type wastes an iteration. Match the task to the right executor.

RESEARCH executor scope:
  Output: research_out.json with {answer, sources, follow_up_questions} + research_report.md
  DOES: Web research — search, read, synthesize information from papers/docs/APIs into a structured report
  DOES NOT: Run code, download files, execute scripts, compute anything — no shell/Python access
  Use for literature surveys, API documentation, technical specifications — pure information gathering

EXPERIMENT executor scope:
  Output: method_out.json with results (metrics, predictions, analysis) — the core computational work
  DOES: Implement and run methods/algorithms, compute metrics, compare approaches, produce quantitative results
  DOES NOT: Collect new datasets (depends on DATASET artifacts for input data), write formal proofs
  This is the right artifact for any code that processes data and produces results

DATASET executor scope:
  Output: data_out.json with rows of {input, output, metadata_fold, ...} — raw data only, no derived computations
  DOES: Download/generate datasets, analyze candidates to pick the best ones, standardize to JSON schema (features, labels, folds, metadata), validate schema, split into full/mini/preview
  DOES NOT: Run experiments, train models, compute derived statistics (PID/MI/correlations/synergy matrices) as final output
  If you need to COMPUTE something from data (synergy matrices, MI scores, timing benchmarks), use an EXPERIMENT artifact instead

EVALUATION executor scope:
  Output: eval_out.json with evaluation results
  DOES: Any evaluation of experiment results — metrics, statistical tests, ablations, comparisons, visualizations, robustness checks, error analysis, etc.
  DOES NOT: Implement new methods (use EXPERIMENT), collect data (use DATASET)
  This is for analyzing experiment outputs from any angle

PROOF executor scope:
  Output: Lean 4 proof files (.lean) with verified theorems
  DOES: Write and verify Lean 4 formal proofs with Mathlib, iterative compilation
  DOES NOT: Run Python experiments, collect data, do empirical analysis
  Use only when formal mathematical guarantees are needed
</artifact_executor_scope>

<artifact_planning_rules>
RESEARCH: Plan early — findings guide dataset selection, experiment design, and methodology.
EXPERIMENT: Must depend on at least one DATASET. Define clear metrics and baselines before running. Consider trying multiple method variations rather than a single approach.
DATASET:
- Plan for REAL third-party datasets (HuggingFace, Kaggle, direct-download URLs) — downloadable within time and size constraints
- Describe dataset criteria (domain, size, format) — executors find exact sources, but you can suggest candidates or search directions
- ALWAYS prefer real datasets over synthetic. Synthetic is a LAST RESORT only when no suitable real data exists
EVALUATION: Must depend on at least one EXPERIMENT. Focus on statistical rigor and validity checks.
PROOF: Use only when the hypothesis requires formal mathematical guarantees. Lean 4 + Mathlib.
</artifact_planning_rules>

<existing_artifacts>
--- Item 1 ---
id: art_6ieqVR18TTbx
type: research
title: Readability Evaluation Landscape Survey
summary: >-
  Comprehensive survey of the readability assessment landscape covering: (1) Standard datasets with human judgments (CLEAR,
  WeeBit, OneStopEnglish, Newsela, Cambridge), (2) Traditional readability formulas (Flesch-Kincaid, SMOG, ARI, Gunning Fog,
  Dale-Chall, Coleman-Liau) with implementations, (3) Modern ML methods (BERT, RoBERTa, Longformer) and their performance,
  (4) Evaluation metrics and benchmarks, (5) Identified gaps in current methods that Semantic Control Energy (SCE) could address.
  The research provides actionable recommendations for validating the SCE method including which datasets to use, which baselines
  to implement, and which metrics to report.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_6uOr5GlpaMfR/3_invention_loop/iter_1/gen_art/gen_art_research_1
out_expected_files:
- research_out.json
out_dependency_files:
  file_list:
  - research_out.json

--- Item 2 ---
id: art_vnKiwBm9Qy9H
type: dataset
title: Readability datasets for SCE evaluation
summary: >-
  Successfully collected, standardized, and validated 3 readability datasets for evaluating the Semantic Control Energy (SCE)
  readability method. The datasets include: (1) CLEAR Corpus - 4,724 examples with human readability judgments and traditional
  readability formula scores, (2) OneStopEnglish - 567 examples with 3 difficulty levels (Elementary/Intermediate/Advanced),
  and (3) WikiLarge - 299,062 examples of Wikipedia→Simple Wikipedia text simplification pairs. All datasets were standardized
  to the exp_sel_data_out.json schema with 'input' (text) and 'output' (readability score/difficulty) fields. Train/validation/test
  splits (70/15/15) were created with stratification by difficulty level where applicable. The final output contains 213,045
  training examples across all 3 datasets, validated against the schema and ready for SCE method evaluation. Dataset provenance
  was verified through published papers and HuggingFace Hub documentation. Total size is ~158MB, under the 300MB limit. Full
  documentation including README with usage examples was created.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_6uOr5GlpaMfR/3_invention_loop/iter_1/gen_art/gen_art_dataset_1
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json
out_dependency_files:
  file_list:
  - data.py
  - full_data_out.json
  - mini_data_out.json
  - preview_data_out.json
  data_file_paths:
  - full_data_out.json
  - mini_data_out.json
  - preview_data_out.json

--- Item 3 ---
id: art_CYCcKfEseq9J
type: experiment
title: Semantic Control Energy Readability Scoring
summary: >-
  Implemented Semantic Control Energy (SCE), a novel readability metric based on control theory that models text as a dynamical
  system trajectory in embedding space. The method computes the energy needed to track semantic transitions between sentences.
  Implemented baselines: Flesch-Kincaid, SMOG, and Coleman-Liau readability formulas. Experiment on synthetic dataset (21
  examples with varying readability levels) shows SCE achieves moderate positive correlation (Pearson r=0.43) with true grade
  levels, while traditional metrics achieve strong correlation (r>0.95). Processing time is <1ms per document. The output
  includes method.py implementation and method_out.json results in valid exp_gen_sol_out schema format with full/mini/preview
  versions.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_6uOr5GlpaMfR/3_invention_loop/iter_1/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json
out_dependency_files:
  file_list:
  - method.py
  - full_method_out.json
  - mini_method_out.json
  - preview_method_out.json
</existing_artifacts>

<current_paper>
The current paper draft — represents the research story so far.

Use this to understand what's working, what's not, and what gaps remain.
Gaps and weak results signal what to try differently — not what to conclude.

# Semantic Control Energy: A Dynamical Systems Approach to Text Readability Assessment

## Abstract

Traditional readability formulas (Flesch-Kincaid, SMOG, Coleman-Liau) rely on surface-level features such as sentence length and word complexity, which fail to capture the cognitive effort required to track meaning across a text. We introduce **Semantic Control Energy (SCE)**, a novel readability metric that models text as a dynamical system trajectory through semantic embedding space and quantifies the minimum "control energy" required to follow the semantic progression. Drawing on optimal control theory, SCE measures the cumulative squared norm of semantic transitions between sentences, yielding a scalar score that reflects how abruptly meaning shifts from one sentence to the next. We evaluate SCE on a synthetic readability dataset spanning three grade-level tiers (simple, medium, complex) and compare against three traditional baselines: Flesch-Kincaid, SMOG, and Coleman-Liau. While traditional formulas achieve strong Pearson correlations (r > 0.91) with true grade levels on texts where surface features dominate, SCE captures a complementary signal—the smoothness of semantic flow—that surface metrics cannot detect. We further analyze SCE's computational efficiency (<1 ms per document) and discuss its theoretical connection to optimal transport and dynamical systems approaches in natural language processing. Our proof-of-concept experiment establishes SCE as a theoretically grounded, computationally efficient readability signal that can augment traditional formulas, particularly for texts where semantic coherence—not vocabulary difficulty—is the primary barrier to comprehension.

**Keywords:** readability assessment, semantic trajectories, optimal control theory, dynamical systems, text embedding

---

# 1 Introduction

Readability assessment—the automatic prediction of how difficult a text is to understand—has practical importance in education, content recommendation, and assistive technologies for language learners. Traditional readability formulas such as Flesch-Kincaid Grade Level (FKGL) [7], the SMOG index [10], and the Coleman-Liau Index [3] have served as standard tools for decades. These formulas operate on surface-level statistics: they count words per sentence, syllables per word, and characters per word, then combine these counts in a linear regression to predict a "grade level" [1].

Despite their simplicity and widespread adoption, traditional formulas have a well-documented limitation: they rely on "weak proxies of word decoding (i.e., characters or syllables per word) and syntactic complexity (i.e., number of words per sentence)" while ignoring "text features that are important components of reading models including text cohesion and semantics" [1]. A text can use simple words yet remain incomprehensible if its sentences jump erratically between unrelated topics; conversely, a text can use sophisticated vocabulary yet remain readable if its semantic progression is smooth and well-signposted.

This limitation points to a deeper issue: readability is not merely a function of local lexical or syntactic difficulty. It is also a function of **semantic flow**—the cognitive work a reader must expend to track how meaning evolves across sentences and paragraphs. Current information-theoretic approaches (e.g., compression-based metrics, Kolmogorov complexity estimates) capture static text complexity but not the *dynamic* cost of semantic navigation [6].

In this paper, we propose a new framework for quantifying readability that draws on **optimal control theory** and **dynamical systems**. The core idea is to treat a text as a trajectory through a continuous semantic embedding space (e.g., SBERT embeddings [11]). Each sentence maps to a point in this space; the sequence of sentences traces a trajectory. The readability of the text corresponds to the "control energy" needed to traverse this trajectory—that is, how large the semantic "jumps" are from sentence to sentence, and how much cognitive effort is required to follow them.

Formally, we model the semantic trajectory as a discrete-time dynamical system:
$$
\mathbf{x}_{t+1} = \mathbf{x}_t + \mathbf{u}_t + \mathbf{w}_t
$$
where $\mathbf{x}_t \in \mathbb{R}^d$ is the semantic state (sentence embedding) at position $t$, $\mathbf{u}_t$ is the "control input" (the semantic transition from sentence $t$ to $t+1$), and $\mathbf{w}_t$ is noise. The **Semantic Control Energy (SCE)** of a text is defined as the cumulative squared norm of the control inputs:
$$
\text{SCE} = \frac{1}{T-1} \sum_{t=1}^{T-1} \|\mathbf{u}_t\|^2 = \frac{1}{T-1} \sum_{t=1}^{T-1} \|\mathbf{x}_{t+1} - \mathbf{x}_t\|^2
$$
where $T$ is the number of sentences. Intuitively, SCE measures the average "semantic work" needed to move from each sentence to the next. Texts with smooth, predictable semantic progressions have low SCE; texts with jarring topic shifts or repetitive loops have high SCE.

[FIGURE:fig1]

Our main contributions are:

1. **A novel readability metric grounded in control theory:** We define SCE and show how it captures semantic flow, a dimension of readability that traditional surface-based formulas cannot measure.

2. **An efficient algorithm:** SCE requires only sentence embedding extraction and pairwise difference computations, running in <1 ms per document on standard hardware.

3. **An empirical proof-of-concept:** We evaluate SCE on a synthetic dataset with three readability tiers and compare against Flesch-Kincaid, SMOG, and Coleman-Liau. We report Pearson correlations with true grade levels and analyze where SCE succeeds or fails relative to baselines.

4. **A discussion of limitations and future work:** We identify key improvements needed to make SCE competitive with state-of-the-art readability assessors, including the use of pretrained SBERT embeddings, evaluation on standard benchmarks (CLEAR, OneStopEnglish), and integration with machine learning models.

---

# 2 Related Work

## 2.1 Traditional Readability Formulas

The Flesch Reading Ease formula [7] and its derivative Flesch-Kincaid Grade Level [8] remain the most widely used readability metrics. FKGL predicts U.S. grade level from average sentence length and average word syllables. The SMOG index [10] counts polysyllabic words and is widely used for health-related texts. The Coleman-Liau Index [3] uses character counts rather than syllables, making it easier to computerize. The Automated Readability Index (ARI) similarly uses character-based features [5].

All these formulas share a common limitation: they treat readability as a linear function of surface statistics, ignoring semantics and discourse structure. The CLEAR corpus paper explicitly criticizes this approach, noting that traditional formulas "ignore many text features that are important components of reading models including text cohesion and semantics" [1].

## 2.2 Modern ML-based Readability Assessment

Recent work has applied transformer models to readability assessment. Imperial (2021) demonstrated that BERT embeddings alone can effectively predict readability [12]. Martinc et al. (2021) showed that BERT raises state-of-the-art classification accuracy on the WeeBit dataset by approximately 4% compared to traditional baselines [12]. Lee et al. (2021) achieved 99% classification accuracy on the OneStopEnglish dataset using a RoBERTa–Random Forest hybrid that combines neural and handcrafted linguistic features [9]. Meng et al. (2020) reported approximately 92% accuracy on WeeBit using a BERT-based ReadNet architecture [4].

These results demonstrate that neural models capture readability signals beyond surface statistics. However, they do not explicitly model semantic flow as a dynamical process. SCE offers a complementary approach: a theoretically interpretable metric that quantifies semantic coherence directly.

## 2.3 Semantic Coherence and Embedding-Based Metrics

Coh-Metrix measures textual coherence using Latent Semantic Analysis (LSA) to compute similarity between adjacent text segments [2]. While related to our approach, Coh-Metrix relies on LSA (which requires term-document matrix factorization) rather than modern contextual embeddings, and it measures static coherence rather than the *energy cost* of semantic navigation.

Word Mover's Distance (WMD) uses optimal transport to measure the distance between two documents in word embedding space [6]. WMD computes the minimum "cost" to transform one document's word distribution into another's. Our approach differs: we measure the control energy along a *trajectory* of sentences within a single document, not the transport cost between two static documents.

## 2.4 Control Theory and Dynamical Systems in NLP

Optimal control theory, particularly the Linear Quadratic Regulator (LQR), is widely used in engineering to design controllers that minimize energy expenditure [8]. In NLP, dynamical systems perspectives have been applied to semantic navigation [13] and concept trajectory analysis [4]. To our knowledge, SCE is the first application of control-theoretic energy minimization to readability assessment.

---

# 3 Methods

## 3.1 Problem Formulation

Given a text document $D$ consisting of $T$ sentences $\{s_1, s_2, \ldots, s_T\}$, our goal is to compute a scalar readability score $R(D) \in \mathbb{R}$ that correlates with human judgments of reading difficulty. Traditional approaches compute $R(D)$ from surface statistics (e.g., words per sentence). We instead compute $R(D)$ from the semantic trajectory induced by $D$ in embedding space.

## 3.2 Semantic Trajectory Construction

We map each sentence $s_t$ to a $d$-dimensional embedding vector $\mathbf{x}_t \in \mathbb{R}^d$. In our implementation, we explore two embedding strategies:

**Feature-based embedding (computationally efficient):** Each sentence is represented by a 10-dimensional feature vector:
- Normalized sentence length (characters / 200)
- Average word length in characters / 10
- Unique word ratio (#unique / #total words)
- Complex word ratio (#words with >6 characters / #total words)
- Normalized character count / 1000
- Normalized word count / 100
- Standard deviation of word lengths
- Binary indicators for question marks, semicolons, and capital letter usage

**SBERT embedding (semantically rich):** Each sentence is mapped to a 384-dimensional embedding using the `all-MiniLM-L6-v2` pretrained model [11]. This captures deep semantic relationships but requires more computation.

The sequence $\{\mathbf{x}_1, \mathbf{x}_2, \ldots, \mathbf{x}_T\}$ defines the semantic trajectory of the document.

## 3.3 Semantic Control Energy (SCE) Computation

The Semantic Control Energy is computed as:

$$
\text{SCE}(D) = \frac{1}{T-1} \sum_{t=1}^{T-1} \|\mathbf{x}_{t+1} - \mathbf{x}_t\|_2^2
$$

where $\|\cdot\|_2$ denotes the Euclidean norm. The normalization by $T-1$ ensures that SCE is comparable across documents of different lengths.

**Interpretation:** Each term $\|\mathbf{x}_{t+1} - \mathbf{x}_t\|_2^2$ is the squared "semantic jump" from sentence $t$ to $t+1$. Large jumps indicate abrupt topic changes or semantic discontinuities, which increase cognitive load. Small jumps indicate smooth semantic progression, which reduces cognitive load. The cumulative energy reflects the total cognitive work of reading the text.

[FIGURE:fig2]

## 3.4 Baseline Readability Formulas

We implement three standard baselines:

**Flesch-Kincaid Grade Level (FKGL):**
$$
\text{FKGL} = 0.39 \left(\frac{\text{total words}}{\text{total sentences}}\right) + 11.8 \left(\frac{\text{total syllables}}{\text{total words}}\right) - 15.59
$$

**SMOG Index:**
$$
\text{SMOG} = 1.0430 \sqrt{\frac{\text{polysyllables} \times 30}{\text{sentences}}} + 3.1291
$$
where "polysyllables" are words with 3 or more syllables.

**Coleman-Liau Index:**
$$
\text{Coleman-Liau} = 0.0588 \times \left(\frac{\text{characters}}{\text{words}} \times 100\right) - 0.296 \times \left(\frac{\text{words}}{\text{sentences}} \times 100\right) - 15.8
$$

All baselines are implemented from scratch in Python, with syllable counting via a rule-based algorithm.

## 3.5 Connection to Optimal Control Theory

SCE can be derived from an optimal control perspective. Consider a discrete-time linear dynamical system:
$$
\mathbf{x}_{t+1} = \mathbf{x}_t + \mathbf{u}_t + \mathbf{w}_t
$$
where the "control input" $\mathbf{u}_t$ represents the intended semantic transition, and $\mathbf{w}_t$ is zero-mean noise. The optimal control problem minimizes:
$$
J = \sum_{t=1}^{T-1} \|\mathbf{u}_t\|^2 + \lambda \sum_{t=1}^T \|\mathbf{x}_t - \mathbf{x}_t^{\text{ideal}}\|^2
$$
If we assume the observed trajectory $\{\mathbf{x}_t\}$ is optimal (i.e., the writer has minimized control effort subject to staying close to an ideal trajectory), then the minimum control cost is exactly SCE. Thus, SCE estimates the *a priori* cognitive effort needed to produce (or comprehend) the text.

---

# 4 Experiments

## 4.1 Dataset

We evaluate on a synthetic readability dataset consisting of 60 examples across three difficulty tiers:

- **Simple (grade 1-3):** 20 examples using basic vocabulary and simple sentence structures (e.g., "The cat sat on the mat.")
- **Medium (grade 4-8):** 20 examples using moderate vocabulary and compound sentences (e.g., "The environment faces many challenges today.")
- **Complex (grade 9-16):** 20 examples using sophisticated vocabulary and academic prose (e.g., "The implementation of comprehensive methodological frameworks necessitates a multifaceted approach.")

Each example has a "true" grade level assigned stochastically within its tier range. The dataset is designed to test whether SCE can distinguish texts with different semantic flow characteristics, independent of vocabulary difficulty.

[ARTIFACT:art_CYCcKfEseq9J]

## 4.2 Evaluation Protocol

We compute Pearson correlation between each method's predictions and the true grade levels. Pearson $r$ ranges from -1 to 1, with higher values indicating stronger linear agreement. We also measure computational efficiency: average processing time per document in milliseconds.

## 4.3 Results

Table 1 reports Pearson correlation coefficients for all methods.

| Method | Pearson $r$ | 95% CI |
|--------|-------------|---------|
| SCE (feature-based) | -0.214 | [-0.612, 0.271] |
| Flesch-Kincaid | 0.919 | [0.781, 0.969] |
| SMOG | 0.916 | [0.776, 0.967] |
| Coleman-Liau | -0.551 | [-0.813, -0.150] |

**Key findings:**

1. **Traditional formulas perform well on this dataset:** FKGL and SMOG achieve $r > 0.91$, confirming that surface statistics are strongly predictive when vocabulary and syntax differ systematically across tiers.

2. **SCE shows negative correlation:** The feature-based SCE implementation achieves $r = -0.214$, which is not statistically significant given the small sample size ($n=60$, $p > 0.05$). The negative sign indicates that documents with larger semantic jumps tend to have *lower* (easier) grade levels in this synthetic dataset—an artifact of how the data was constructed (simple texts use varied templates that produce varied feature vectors).

3. **Coleman-Liau performs poorly:** The negative correlation ($r = -0.551$) suggests the formula is miscalibrated for this dataset, likely because character-based features behave differently in short sentences.

[FIGURE:fig3]

## 4.4 Computational Efficiency

SCE processes documents in **0.56 milliseconds** on average (measured over 15 examples on a standard CPU). This is comparable to traditional formulas (<1 ms) and orders of magnitude faster than SBERT-based approaches (~50-200 ms depending on document length). The efficiency stems from SCE's simple computation: embedding extraction (or feature computation) followed by pairwise Euclidean distances.

## 4.5 Ablation: Embedding Strategy

We compare feature-based embeddings against SBERT embeddings on a 15-example subset. SBERT-based SCE achieves higher correlation with human judgments of semantic coherence (qualitative evaluation), but the improvement does not translate to higher Pearson $r$ with grade levels on this synthetic dataset. This suggests that **the choice of embedding space is critical**: feature-based embeddings capture surface properties (sentence length, word complexity) that correlate with grade level, while SBERT embeddings capture semantic properties that may not align with traditional grade-level annotations.

---

# 5 Discussion

## 5.1 Why SCE Underperforms on Synthetic Data

The negative correlation between SCE and grade level on our synthetic dataset reveals an important limitation: **SCE measures semantic jump magnitude, not vocabulary difficulty**. In our dataset, "simple" texts use varied templates ("The cat sits", "I like cake", "Mom runs fast") that produce varied feature vectors and hence large SCE values. "Complex" texts use consistent academic templates that produce similar feature vectors and hence small SCE values. Thus, SCE is **anti-correlated** with traditional grade level on this particular data.

This limitation is not a flaw in SCE itself, but rather a mismatch between what SCE measures (semantic coherence) and what traditional grade levels measure (vocabulary and syntax difficulty). In real-world texts, these two signals are often positively correlated: texts with difficult vocabulary also tend to have more complex semantic structures. However, they can also diverge—and it is precisely in these cases that SCE provides novel information.

## 5.2 When Does SCE Provide Novel Signal?

SCE is designed to detect texts that are **semantically incoherent despite using simple words**. Consider the following example:

> "Dogs bark loudly at mailboxes. The quantum vacuum fluctuates constantly. Yesterday's sandwich contained pickles. Economic indicators suggest inflationary pressure. Beethoven composed nine symphonies."

This text uses simple words and short sentences (FKGL would predict "easy"), but its semantic trajectory is extremely erratic (SCE would predict "difficult"). Human readers would find this text confusing not because of vocabulary, but because of topic whiplash. SCE captures this dimension of readability that traditional formulas miss.

[FIGURE:fig4]

## 5.3 Connection to Human Readability Judgments

The CLEAR corpus [1] provides human readability judgments from 1,116 teachers who made 111,347 pairwise comparisons of text excerpts. These judgments incorporate factors beyond vocabulary difficulty, including discourse coherence, background knowledge requirements, and genre conventions. SCE offers a way to operationalize "discourse coherence" as a quantifiable metric. We hypothesize that SCE will show stronger correlation with CLEAR judgments than with FKGL-predicted grade levels, because CLEAR captures global readability while FKGL captures local difficulty.

## 5.4 Limitations

1. **Embedding sensitivity:** SCE's performance depends heavily on the quality of the sentence embeddings. Feature-based embeddings are computationally efficient but cannot capture deep semantic relationships. SBERT embeddings are semantically rich but require more computation and may be biased toward certain domains.

2. **Small-scale evaluation:** Our experiments use a synthetic dataset of 60 examples. While this allows controlled analysis, it does not reflect the diversity of real-world texts. Evaluation on standard benchmarks (CLEAR, OneStopEnglish, WeeBit) is needed.

3. **Negative correlation on synthetic data:** As discussed above, SCE measures semantic jump magnitude, which anti-correlates with grade level on our synthetic data. This does not invalidate SCE, but it does mean that SCE and traditional formulas capture complementary signals.

4. **Noisy sentence boundaries:** SCE assumes sentences are the units of semantic transition. In practice, sentence tokenization errors (e.g., abbreviations like "Dr." causing false sentence breaks) can introduce noise into the semantic trajectory.

## 5.5 Future Work

1. **Evaluation on standard benchmarks:** The most important next step is to evaluate SCE on the CLEAR corpus [1], OneStopEnglish [14], and WikiLarge datasets. These provide real human judgments and established evaluation protocols.

2. **SBERT integration:** Replace feature-based embeddings with pretrained SBERT embeddings (`all-MiniLM-L6-v2` or `all-mpnet-base-v2`) to capture deep semantic relationships. This requires more computation but should improve correlation with human judgments.

3. **LQR-inspired formulation:** Extend SCE to a full LQR framework where the "optimal" semantic trajectory is learned from human judgments. This would allow SCE to adapt to different genres and reading levels.

4. **Hybrid models:** Combine SCE with traditional formulas in a machine learning model (e.g., linear regression with SCE and FKGL as features). This hybrid approach should outperform either metric alone.

5. **Optimal transport extension:** Replace Euclidean distance with Wasserstein distance (or Word Mover's Distance [6]) to account for the geometry of word embedding space. This would make SCE more robust to synonym substitutions and paraphrases.

---

# 6 Conclusion

We introduced Semantic Control Energy (SCE), a novel readability metric that models text as a dynamical system trajectory in embedding space and quantifies the cognitive work needed to track semantic changes. SCE is grounded in optimal control theory, computationally efficient (<1 ms per document), and captures a dimension of readability—semantic flow—that traditional surface-based formulas cannot measure.

Our proof-of-concept experiment on a synthetic dataset shows that SCE provides a complementary signal to traditional formulas. While FKGL and SMOG achieve strong correlation with grade levels on texts where vocabulary difficulty dominates ($r > 0.91$), SCE captures semantic coherence independent of vocabulary. The negative correlation we observe on synthetic data ($r = -0.214$) reflects this complementarity: SCE measures semantic jump magnitude, which is not always aligned with traditional grade level.

The broader contribution of this work is a new conceptual framework for readability assessment: **treating reading as a control problem**, where the reader must expend cognitive energy to track the writer's semantic trajectory. This framework opens several avenues for future research, including SBERT-based SCE, LQR-inspired formulations, and hybrid models that combine SCE with traditional formulas.

We release our implementation and synthetic dataset to facilitate further research. Future work should evaluate SCE on standard readability benchmarks (CLEAR, OneStopEnglish) and explore hybrid models that combine SCE with neural approaches for state-of-the-art readability assessment.

---

# Acknowledgments

We thank the AI Inventor system for facilitating this research. We also thank the creators of the CLEAR corpus, OneStopEnglish corpus, and WikiLarge dataset for making their data publicly available.

---

# References

[1] Crossley, S., Burling, A. B., & O'Reilly, T. (2021). The CommonLit Ease of Readability (CLEAR) Corpus. *Proceedings of the 14th International Conference on Educational Data Mining*, 381-386.

[2] Graesser, A. C., McNamara, D. S., & Kulikowich, J. M. (2011). Coh-Metrix: Providing multilevel analyses of text characteristics. *Educational Researcher*, 40(5), 223-234.

[3] Coleman, M., & Liau, T. L. (1975). A computer readability formula designed for machine scoring. *Journal of Applied Psychology*, 60(2), 283-284.

[4] Fernández, R., & Morris, R. (2026). Characterizing human semantic navigation in concept production as trajectories in embedding space. *arXiv preprint arXiv:2602.05971*.

[5] Kincaid, J. P., Fishburne, R. P., Rogers, R. L., & Chissom, B. S. (1975). Derivation of new readability formulas for Navy enlisted personnel. *Naval Technical Training Command Millington TN Research Branch*.

[6] Kusner, M. J., Sun, Y., Kolkin, N. I., & Weinberger, K. Q. (2015). From word embeddings to document distances. *Proceedings of the 32nd International Conference on Machine Learning*, 957-966.

[7] Flesch, R. (1948). A new readability yardstick. *Journal of Applied Psychology*, 32(3), 221-233.

[8] Kalman, R. E. (1960). Contributions to the theory of optimal control. *Boletín de la Sociedad Matemática Mexicana*, 5(1), 102-119.

[9] Lee, B. W., Jang, Y., & Lee, J. (2021). Pushing on text readability assessment: A transformer meets handcrafted linguistic features. *Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing*, 8385-8397.

[10] McLaughlin, G. H. (1969). SMOG grading: A new readability formula. *Journal of Reading*, 12(8), 639-646.

[11] Reimers, N., & Gurevych, I. (2019). Sentence-BERT: Sentence embeddings using siamese BERT-networks. *Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing*, 3982-3992.

[12] Martinc, M., & Pollak, S. (2021). Tackling the problem of readability assessment for Slovenian. *Natural Language Engineering*, 27(5), 581-603.

[13] Kumar, S., Zhang, X., & Leskovec, J. (2019). Predicting dynamic embedding trajectory in temporal interaction networks. *Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining*, 1269-1278.

[14] Vajjala, S., & Lucic, I. (2018). OneStopEnglish corpus: A new corpus for automatic readability assessment and text simplification. *Proceedings of the 13th Workshop on Innovative Use of NLP for Building Educational Applications*, 297-304.
</current_paper>

<reviewer_feedback>
Paper reviewer feedback from the previous iteration. Your strategy MUST address these critiques.
Prioritize major issues — these are the most impactful improvements to make.

- [MAJOR] (evidence) The experimental evaluation is fundamentally inadequate. The paper evaluates ONLY on a synthetic dataset with 21 examples (not 60 as claimed in Section 4.1), where 'true' grade levels are assigned randomly within ranges. This dataset has critical flaws: (1) Simple texts use varied templates that produce varied feature vectors (high SCE), while complex texts use consistent templates (low SCE), leading to artificial anti-correlation; (2) The sample size is far too small for reliable correlation estimation; (3) Synthetic data cannot generalize to real-world readability. Despite the authors preparing real datasets (CLEAR, OneStopEnglish, WikiLarge) as described in the supplementary materials (art_vnKiwBm9Qy9H), these were NOT used in the evaluation.
  Action: Evaluate SCE on the CLEAR corpus and OneStopEnglish dataset that were already prepared. These have real human judgments and established evaluation protocols. Report Pearson correlation with human judgments (CLEAR) and classification accuracy (OneStopEnglish). This is the minimum requirement for a readability paper.
- [MAJOR] (methodology) There are significant discrepancies between the paper description and the actual implementation: (1) Section 3.2 describes a 10-dimensional feature vector for SCE, but the code (method.py) only implements a 2-dimensional vector (normalized sentence length and word count); (2) The paper reports SCE correlation as r = -0.214 with 95% CI [-0.612, 0.271] in Table 1, but the RESULTS.md file shows r = 0.4340, and the actual experiment output shows inconsistent results; (3) The Flesch-Kincaid baseline is implemented incorrectly as 'words/3' rather than the proper formula (0.39*(words/sentences) + 11.8*(syllables/words) - 15.59). These discrepancies undermine the paper's credibility.
  Action: Ensure the implementation matches the paper description. Implement the full 10-dimensional feature vector OR use SBERT embeddings as described. Use established implementations (textstat package) for baseline formulas. Re-run experiments and report accurate results. Provide code that exactly reproduces the paper's numbers.
- [MAJOR] (novelty) The core idea of SCE—measuring semantic coherence via distances between sentence embeddings—is not novel. Coh-Metrix (2001) measures textual coherence using LSA to compute similarity between adjacent segments. Word Mover's Distance (2015) uses optimal transport for document similarity. More recent work uses SBERT embeddings to measure semantic similarity. The 'control energy' framing adds minimal novelty: SCE is simply the sum of squared Euclidean distances between consecutive embeddings, which is a straightforward baseline that does not require control theory. The paper's claim that 'SCE is the first application of control-theoretic energy minimization to readability assessment' is misleading—the connection to control theory is superficial.
  Action: Reframe the contribution more honestly. Acknowledge that measuring semantic coherence via embedding distances is established. Focus on what is truly novel: perhaps the specific formulation, computational efficiency, or empirical findings. Compare against Coh-Metrix and SBERT cosine similarity baselines to show SCE's relative advantage. Consider removing or de-emphasizing the control theory claims unless a rigorous connection can be established.
- [MAJOR] (rigor) The connection to optimal control theory in Section 3.5 is not mathematically sound. The paper states that SCE can be derived from minimizing J = sum(||u_t||^2) + lambda*sum(||x_t - x_t^ideal||^2), but then claims that if the observed trajectory is optimal, 'the minimum control cost is exactly SCE.' This is incorrect: the optimal control cost depends on the ideal trajectory x_t^ideal, which is never defined. Furthermore, the dynamical system formulation x_{t+1} = x_t + u_t + w_t is not used in the actual SCE computation—SCE simply computes ||x_{t+1} - x_t||^2, which ignores the noise term w_t and any notion of optimal control. The control theory framing appears to be post-hoc justification rather than genuine theoretical grounding.
  Action: Either provide a rigorous optimal control derivation that leads to SCE, or remove the control theory claims and present SCE as a simple heuristic metric. If keeping the control theory connection, define the ideal trajectory, derive the optimal controller, and show that SCE emerges from this derivation. Alternatively, reframe as 'inspired by control theory' rather than 'derived from'.
- [MINOR] (evidence) The paper reports 95% confidence intervals for Pearson correlations (Table 1), but with n=60 (or actually n=21 in the code), these CIs are unreliable. Pearson correlation CIs require assumptions about the underlying distribution that may not hold. Additionally, the CI for SCE [-0.612, 0.271] includes zero, indicating the correlation is not statistically significant, but the paper does not acknowledge this.
  Action: Report p-values alongside correlations to indicate statistical significance. Use bootstrap CIs rather than parametric CIs for small samples. Acknowledge when correlations are not statistically significant.
- [MINOR] (scope) The paper claims SCE is 'computationally efficient (<1 ms per document)' but this measurement is misleading. The feature-based embedding used in the experiment is trivial to compute, but the paper also promotes SBERT embeddings which take 50-200ms per document. The <1ms claim only applies to the feature-based version, which the paper acknowledges performs poorly. A fairer comparison would report timing for SBERT-based SCE, which is the version that would actually be used in practice.
  Action: Report computational efficiency for both feature-based and SBERT-based SCE. Compare against traditional formulas AND modern ML methods (BERT-based readability assessors). Acknowledge the trade-off between efficiency and accuracy.
- [MINOR] (clarity) Figure placeholders are used throughout the paper ([FIGURE:fig1], etc.) but no actual figures are provided. While the instructions say to assume figures show what captions describe, the figures are essential for understanding: (1) Figure 1 should illustrate the semantic trajectory concept; (2) Figure 2 should visualize SCE computation; (3) Figure 3 should show correlation results; (4) Figure 4 should illustrate the 'semantic whiplash' example. Without figures, the paper is difficult to follow.
  Action: Generate actual figures showing: (1) Semantic trajectories in embedding space for simple vs. complex texts; (2) SCE computation as squared distances; (3) Scatter plots of SCE vs. grade level; (4) Example of semantically incoherent text. Ensure figures are well-labeled and support the paper's claims.
</reviewer_feedback>

<task>
Generate 1 research strategy for THIS iteration.

**ARTIFACT LIMIT: Each strategy may contain AT MOST 3 artifact directions.** Focus on the highest-impact artifacts. Quality over quantity.

Each strategy should:
1. Define a clear OBJECTIVE - what novel contribution we're building toward
2. Plan artifacts to execute NOW - specify type, objective, approach, and depends_on for each
3. Account for parallel execution - all strategies and all planned artifacts run simultaneously, their artifacts are combined into one shared pool


</task><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_6uOr5GlpaMfR/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_6uOr5GlpaMfR/3_invention_loop/iter_2/gen_strat/gen_strat_1/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "ArtifactDep": {
      "description": "A single dependency on an existing artifact, with a short type label.\n\n``id`` and ``label`` are LLM-generated at strategy time. ``label`` is free-text but\nshort \u2014 a word or two naming the type of dependency, not a sentence.\n\n``relation_type`` and ``relation_rationale`` are populated later, in upd_hypo,\nusing the MultiCite citation-function typology (Lauscher et al., NAACL 2022).\nThey are absent at strategy time and may stay absent for legacy runs.",
      "properties": {
        "id": {
          "description": "ID of an existing artifact this artifact depends on",
          "title": "Id",
          "type": "string"
        },
        "label": {
          "description": "Short free-text label naming the type of this dependency (a word or two, not a sentence)",
          "title": "Label",
          "type": "string"
        }
      },
      "required": [
        "id",
        "label"
      ],
      "title": "ArtifactDep",
      "type": "object"
    },
    "ArtifactDirection": {
      "description": "High-level direction for an artifact to execute this iteration.\n\nID is code-assigned (LLMPrompt only \u2014 visible in prompts, not LLM-generated).",
      "properties": {
        "type": {
          "description": "Type of artifact to create",
          "enum": [
            "experiment",
            "research",
            "proof",
            "evaluation",
            "dataset"
          ],
          "title": "Type",
          "type": "string"
        },
        "objective": {
          "description": "What we want to achieve with this artifact",
          "title": "Objective",
          "type": "string"
        },
        "approach": {
          "description": "High-level direction/method",
          "title": "Approach",
          "type": "string"
        },
        "depends_on": {
          "description": "Existing artifacts this depends on, each with a short type label",
          "items": {
            "$ref": "#/$defs/ArtifactDep"
          },
          "title": "Depends On",
          "type": "array"
        }
      },
      "required": [
        "type",
        "objective",
        "approach"
      ],
      "title": "ArtifactDirection",
      "type": "object"
    },
    "Strategy": {
      "description": "A research strategy.\n\nContent fields have LLMPrompt + LLMStructOut markers.\n``id`` is code-assigned (LLMPrompt only \u2014 visible in prompts, not LLM-generated).\n\nID format: gen_strat_idx{N}",
      "properties": {
        "title": {
          "description": "Strategy name in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters).",
          "title": "Title",
          "type": "string"
        },
        "objective": {
          "description": "The novel contribution we're building toward",
          "title": "Objective",
          "type": "string"
        },
        "rationale": {
          "description": "Why this strategy is promising",
          "title": "Rationale",
          "type": "string"
        },
        "artifact_directions": {
          "description": "Artifacts to execute THIS iteration",
          "items": {
            "$ref": "#/$defs/ArtifactDirection"
          },
          "title": "Artifact Directions",
          "type": "array"
        },
        "expected_outcome": {
          "description": "What we'll have after this iteration's artifacts complete",
          "title": "Expected Outcome",
          "type": "string"
        },
        "summary": {
          "default": "",
          "description": "Brief summary of the strategy and its expected contribution",
          "title": "Summary",
          "type": "string"
        }
      },
      "required": [
        "title",
        "objective",
        "rationale",
        "artifact_directions",
        "expected_outcome"
      ],
      "title": "Strategy",
      "type": "object"
    }
  },
  "description": "Top-level wrapper for LLM strategy generation output.",
  "properties": {
    "strategies": {
      "description": "List of generated strategies",
      "items": {
        "$ref": "#/$defs/Strategy"
      },
      "title": "Strategies",
      "type": "array"
    }
  },
  "required": [
    "strategies"
  ],
  "title": "Strategies",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `/ai-inventor/aii_data/runs/run_6uOr5GlpaMfR/3_invention_loop/iter_2/gen_strat/gen_strat_1/.sdk_openhands_agent_struct_out.json`.

Propose a simple, novel machine-learning method for scoring text readability and validate it.
````

### [4] SYSTEM-USER prompt · 2026-07-09 01:06:30 UTC

```
<verification_results>
Your previous response had issues that need fixing:

DEPENDENCY ERRORS (depends_on can ONLY reference IDs from <existing_artifacts>):
  - Strategy 1: Artifact 'evaluation_iter2_dir3' (evaluation): missing required dependency. Must have at least one dependency of type: {'experiment'}

</verification_results>

<task>
Fix ALL issues above and regenerate your strategies:

1. Fix dependency errors:
   - depends_on is a list of {id, label} objects — every entry MUST have a non-empty short label
   - id can ONLY reference IDs from <existing_artifacts>
   - You CANNOT reference artifacts you are proposing in this strategy as dependencies (they all run in parallel)
   - Follow the dependency type rules (e.g., experiments require datasets)
   - If no suitable existing artifacts exist, use depends_on: []

Output the corrected JSON with the fixed strategies.
</task>
```
