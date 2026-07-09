# gen_plan_experiment_1 — test_idea

> Phase: `invention_loop` · round 2 · `gen_plan`
> Run: `run_6uOr5GlpaMfR` — Readability Scoring Model
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_plan_experiment_1` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-07-09 01:07:23 UTC

````
<hypothesis>
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
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. Use it for the methods, proper baselines, and evaluation this field demands.

- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
</available_domain_handbooks>

<artifact_direction>
Make this direction concrete and actionable. Keep the same type and respect dependencies.

id: experiment_iter2_dir1
type: experiment
objective: >-
  Evaluate SCD on CLEAR and OneStopEnglish with correct SBERT implementation and proper baselines
approach: >-
  Load datasets from art_vnKiwBm9Qy9H (CLEAR corpus with human readability judgments, OneStopEnglish with 3 difficulty levels).
  Implement SCD correctly: (1) Use all-MiniLM-L6-v2 SBERT model for sentence embeddings (not the incorrect 2D feature vector
  from prior code), (2) Compute semantic coherence distance as average pairwise cosine distance or squared Euclidean distance
  between consecutive sentence embeddings, (3) Normalize by document length. Implement baseline formulas correctly using textstat
  package (not buggy custom implementation): Flesch-Kincaid, SMOG, Coleman-Liau, Dale-Chall. For CLEAR: compute Pearson correlation
  between each method and human readability judgments (target_score field). For OneStopEnglish: compute classification accuracy
  (3-class: Elementary/Intermediate/Advanced) and F1 score. Add Coh-Metrix LSA baseline if computationally feasible. Output:
  correlations with 95% bootstrap CIs, p-values, classification metrics, scatter plots, and timing measurements.
depends_on:
- id: art_vnKiwBm9Qy9H
  label: dataset
  relation_type:
  relation_rationale:
</artifact_direction>

<dependencies>
Completed artifacts this artifact can use during execution.

--- Dependency 1 ---
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
</dependencies>

<instructions>
YOUR ROLE: Write a detailed PLAN for the artifact. A separate executor agent runs the actual artifact later.

You are a PLANNER, not an executor. Your output is a plan that tells the executor what to do and how.
Do NOT execute the artifact itself — a separate agent handles that. Your job is to plan it so well that the executor can follow your plan step by step.

You CAN and SHOULD: search the web, read papers, and explore library docs to make your plan concrete.
You CANNOT run shell commands or scripts — code execution is disabled. Research via web tools only.

Do NOT do the executor's job: don't download datasets, don't implement code, don't run experiments, don't write proofs, don't compute evaluations.

<artifact_executor_scope>
IMPORTANT: Each artifact executor has a focused prompt that guides it to do ONE thing well. It will NOT perform tasks outside its scope — assigning the wrong work to the wrong artifact type wastes an iteration. Match the task to the right executor.

EXPERIMENT executor scope:
  Output: method_out.json with results (metrics, predictions, analysis) — the core computational work
  DOES: Implement and run methods/algorithms, compute metrics, compare approaches, produce quantitative results
  DOES NOT: Collect new datasets (depends on DATASET artifacts for input data), write formal proofs
  This is the right artifact for any code that processes data and produces results
</artifact_executor_scope>

<artifact_planning_rules>
EXPERIMENT: Must depend on at least one DATASET. Define clear metrics and baselines before running. Consider trying multiple method variations rather than a single approach.
</artifact_planning_rules>

<compute_profiles>
Choose the compute profile this artifact needs for execution.
Available profiles for experiment artifacts:
  - gpu: 1x NVIDIA RTX A4500, 20GB VRAM, 7 vCPUs, 29GB RAM — ML training, CUDA, large models (fallback: GPUs cheap→expensive: 2000 Ada → A4000 → 4000 Ada → L4 → 4090 → 5090)
  - cpu_heavy: 4 vCPUs, 32GB RAM — large datasets, memory-intensive processing (fallback: CPUs cheap→expensive, then GPU hosts cheap→expensive (all ≥32GB RAM))

Set runpod_compute_profile to one of these exact tier names.
</compute_profiles>
GOOD PLANS: specific, actionable, consider failure scenarios, build on the suggested approach.
BAD PLANS: vague hand-waving, ignoring the suggested approach, missing critical executor details.
</instructions><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_6uOr5GlpaMfR/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_6uOr5GlpaMfR/3_invention_loop/iter_2/gen_plan/gen_plan_experiment_1/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "description": "Plan for an EXPERIMENT artifact.",
  "properties": {
    "title": {
      "description": "Plan title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters).",
      "title": "Title",
      "type": "string"
    },
    "summary": {
      "default": "",
      "description": "Brief summary",
      "title": "Summary",
      "type": "string"
    },
    "runpod_compute_profile": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": "cpu_light",
      "description": "Compute tier for execution \u2014 pick from the available profiles list (e.g., 'gpu', 'cpu_heavy', 'cpu_light'). Only used in RunPod mode.",
      "title": "Runpod Compute Profile"
    },
    "implementation_pseudocode": {
      "description": "High-level pseudocode for the experiment implementation",
      "title": "Implementation Pseudocode",
      "type": "string"
    },
    "fallback_plan": {
      "description": "What to do if the primary approach fails - alternative methods, simplified versions",
      "title": "Fallback Plan",
      "type": "string"
    },
    "testing_plan": {
      "description": "How to validate the experiment works: start with small/fast tests, look for confirmation signals before running full-scale experiments",
      "title": "Testing Plan",
      "type": "string"
    }
  },
  "required": [
    "title",
    "implementation_pseudocode",
    "fallback_plan",
    "testing_plan"
  ],
  "title": "ExperimentPlan",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `/ai-inventor/aii_data/runs/run_6uOr5GlpaMfR/3_invention_loop/iter_2/gen_plan/gen_plan_experiment_1/.sdk_openhands_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-07-09 01:07:23 UTC

```
Propose a simple, novel machine-learning method for scoring text readability and validate it.
```

### [3] SKILL-INPUT — aii-web-tools · 2026-07-09 01:08:36 UTC

The agent loaded the **aii-web-tools** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-web-tools
description: "Web research toolkit: web search (Serper/Google), web page fetch as markdown (HTML and PDF), and regex grep over full page/PDF text. Use whenever a task needs to search the web, read a page, mine a paper/PDF, verify citations, or extract exact quotes, numbers, or methodology from a URL."
---

## Web tools

You have three web capabilities: **search**, **fetch**, and **grep** (exact
regex extraction over a full page or PDF).

**Pick where they come from, in this order:**

1. **If you have built-in `WebSearch` / `WebFetch` tools, PREFER those over the
   scripts below.** They may be **deferred tools** (listed by name but with
   schemas not yet loaded) — if so, call `ToolSearch("select:WebSearch,WebFetch")`
   ONCE to load them, then use them normally. Do not skip them just because they
   need that one extra load step; they are the preferred path. Pair them with the
   `aii_web_tools__fetch_grep` script below when you need exact text / numbers /
   methodology that a summary would miss, or when reading a PDF.
2. **Only if you have NO built-in `WebSearch` / `WebFetch`** (e.g. the OpenHands
   backend), use the scripts in this skill (below). They are our own
   implementations — Serper.dev for search, html2text + PyMuPDF for fetch, and
   regex grep over the full document text. They work without any built-in web
   tools.

Workflow either way: **search** (discover) → **fetch** (read for the gist) →
**grep** (pull exact details / read PDFs).

---

## Running the scripts

Run every script with the skill's pre-provisioned interpreter (it already has
`requests`, `html2text`, `pymupdf`, `python-dotenv`). Set `PY` once:

```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

### 1. Search the web (Serper.dev / Google)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "neuro-symbolic FOL translation LLM" --max-results 10
```

Returns ranked title / URL / snippet lines. Use it first to scan the
landscape; snippets are for discovery only — fetch a page before judging it.

### 2. Fetch a page as markdown (HTML or PDF)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" fetch --url "https://arxiv.org/abs/2303.11366" --max-chars 10000
```

`--max-chars` caps output (default 10000); `--char-offset N` pages further in.
Handles PDFs transparently via PyMuPDF.

### 3. Grep a page or PDF (exact regex extraction)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" grep --url "https://arxiv.org/pdf/2303.11366" --pattern "verbal reinforcement" --max-matches 20 --context-chars 200
```

Returns only the matching sections with surrounding context — the right tool
for exact numbers, table values, methodology, or long PDFs where a summary
would lose the detail. `-i` for case-insensitive.

**Parallelize** independent searches/fetches in one turn; only sequence a
fetch after the search that produced its URL.

---

## Notes

- The scripts call our ability server. If a script prints
  `Ability service not available`, the server is down — say so rather than
  silently improvising a different search method.
- Do **not** hand-roll your own `requests`/scraping for search when these
  tools are available: Serper returns clean Google results and the fetch/grep
  scripts already handle HTML, PDFs, and encoding.
````

### [4] SKILL-INPUT — aii-hf-datasets · 2026-07-09 01:10:31 UTC

The agent loaded the **aii-hf-datasets** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-hf-datasets
description: Searches, previews, and downloads datasets from HuggingFace Hub. Use when user needs machine learning datasets, training data, HuggingFace datasets, dataset discovery, or .parquet/.json exports.
---

## Contents

- Workflow (3-phase dataset discovery)
- Scripts (Search, Preview, Download)

**IMPORTANT - Parallel execution:** GNU `parallel` subshells do NOT inherit `source activate`. Use `export` for variables and **single-quoted** command templates so parallel's subshells can resolve them:
```
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

---

## Workflow: 3-Phase Dataset Discovery

### Phase 1: Search for Datasets
Find datasets with metadata (configs, splits, features, sizes)
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_search_datasets.py --query "sentiment analysis" --limit 5
```

### Phase 2: Preview Dataset (if promising)
Inspect metadata AND sample rows in one call
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_preview_datasets.py openai/gsm8k
```

### Phase 3: Download Dataset (if suitable)
Download after reviewing the preview
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_download_datasets.py openai/gsm8k --config main --split train
```

---

## Scripts

### Search HuggingFace Datasets (aii_hf_search_datasets.py)

Search and discover datasets on HuggingFace Hub.

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_search_datasets.py --query "text classification" --limit 5
```

**Parallel execution (multiple queries):**

IMPORTANT: Use full python path with GNU parallel (venv activate does NOT work in parallel subshells):
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_hf_search_datasets.py" && \
parallel -j 10 -k --group --will-cite '$PY $S --query {} --limit 3' ::: 'sentiment' 'classification' 'translation'
```

**Example output:**
```
Found 5 dataset(s) for query='text classification'

============================================================
Dataset 1: stanfordnlp/imdb
Downloads: 2,500,000 | Likes: 1,234
Description: Large Movie Review Dataset for binary sentiment classification...
Tags: text-classification, en, sentiment-analysis
```

**Result fields per dataset:**

Each entry in ``results`` carries:

- ``id`` / ``downloads`` / ``likes`` / ``tags`` / ``description`` — standard
  HF metadata
- ``has_loader_script`` (bool) — repo ships a top-level ``<repo>.py`` loader.
  ``datasets>=3`` won't run these directly; the dataset is reachable only
  via the Datasets Server's pre-converted parquet shards. Treat as a yellow
  flag.
- ``loadable`` (bool) — **prefer datasets where this is ``True``.** Means
  the dataset is reachable via *some* path: either native parquet (no
  script) or HF auto-converted the script's output to parquet. When
  ``False``, the script needs deps HF can't install (e.g. ``conllu``,
  custom audio decoders) and ``aii_hf_datasets__download_datasets`` will
  fail — pick a different candidate.

**Parameters:**

`--query` (optional)
- Search query string
- Example: `--query "sentiment analysis"`

`--limit` (optional)
- Maximum number of results (default: 5)

`--tags` (optional)
- Filter by tags (comma-separated)
- Format: `category:value`
- Examples: `language:en`, `task_categories:text-classification`

`--sort` (optional)
- Sort by field: `downloads`, `likes` (default: downloads)

**Tips:**
- Search displays full dataset metadata
- Use tags to filter: `--tags "language:en,task_categories:translation"`

---

### Preview HuggingFace Dataset (aii_hf_preview_datasets.py)

Inspect a specific dataset - shows metadata AND sample rows.

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_preview_datasets.py openai/gsm8k --num-rows 5
```

**Parallel execution (multiple datasets):**

IMPORTANT: Use full python path with GNU parallel:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_hf_preview_datasets.py" && \
parallel -j 10 -k --group --will-cite '$PY $S {} --num-rows 3' ::: 'openai/gsm8k' 'imdb' 'squad'
```

**Example output:**
```
============================================================
Dataset: openai/gsm8k
============================================================
Downloads: 425,109 | Likes: 1,102

Description: GSM8K (Grade School Math 8K) is a dataset of 8.5K high quality
linguistically diverse grade school math word problems...

Configs: main, socratic

--- Sample Rows (train) ---
Columns: question, answer

Row 1:
  question: Natalia sold clips to 48 of her friends in April...
  answer: Natalia sold 48/2 = <<48/2=24>>24 clips in May...
```

**Parameters:**

`dataset_id` (required, positional)
- HuggingFace dataset ID
- Examples: `openai/gsm8k`, `glue`, `imdb`

`--config` (optional)
- Dataset configuration/subset name
- Auto-detects first config if not specified

`--split` (optional)
- Split to preview (default: `train`)

`--num-rows` (optional)
- Number of sample rows (default: 5, max: 20)

**Tips:**
- Use after search to verify data structure
- Streaming mode - doesn't download full dataset

---

### Download HuggingFace Dataset (aii_hf_download_datasets.py)

Download datasets and save to files.

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_download_datasets.py openai/gsm8k --config main --split train
```

**Parallel execution (multiple datasets):**

IMPORTANT: Use full python path with GNU parallel. Use `eval {}` pattern when datasets need different flags (e.g. `--config`):
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_hf_download_datasets.py" && \
parallel -j 10 -k --group --will-cite 'eval {}' ::: '$PY $S openai/gsm8k --config main --split train' '$PY $S imdb --split train' '$PY $S squad --split train'
```

**Example output:**
```
Downloaded: openai/gsm8k

  train:
    Rows: 7,473
    Preview: temp/datasets/preview_openai_gsm8k_main_train.json
    Mini: temp/datasets/mini_openai_gsm8k_main_train.json
    Full: temp/datasets/full_openai_gsm8k_main_train.json
```

**Parameters:**

`dataset_id` (required, positional)
- HuggingFace dataset ID
- Examples: `openai/gsm8k`, `imdb`

`--config` (optional)
- Dataset configuration/subset name
- Use preview to see available configs

`--split` (optional)
- Specific split to load (e.g., `train`, `test`)
- If not specified, loads all splits

`--output-dir` (optional)
- Output directory (default: `temp/datasets/`)

**Output files (auto-saved):**
1. **Preview**: `preview_{dataset}_{split}.json` - 3 truncated rows - **READ THIS** for quick inspection
2. **Mini**: `mini_{dataset}_{split}.json` - 3 full rows - for development/testing
3. **Full**: `full_{dataset}_{split}.json` - All rows - **DO NOT READ directly** - use as input path for code

**Tips:**
- Only read preview file directly with Read tool
- Mini and full are input paths for processing code

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````

### [5] SKILL-INPUT — aii-json · 2026-07-09 01:15:38 UTC

The agent loaded the **aii-json** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-json
description: JSON validation and formatting toolkit. Validate JSON files against schemas for experiment pipelines, and generate full/mini/preview versions of JSON datasets. Use for validating pipeline outputs, checking schema compliance, or creating size-optimized JSON variants.
---

## Contents

- Validating JSON (schema validation against experiment schemas)
- Formatting JSON (generate full/mini/preview versions)

**IMPORTANT - Parallel execution:** GNU `parallel` subshells do NOT inherit `source activate`. Use `export` for variables and **single-quoted** command templates so parallel's subshells can resolve them:
```
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

---

## Validating JSON

Validate JSON files against predefined schemas for experiment-based hypothesis selection, data collection, solution generation, and evaluation.

### Quick Start

1. Read the schema spec you need to adhere to (e.g., `schemas/exp_eval_sol_out.json`)
2. Create your output file following that schema structure
3. Validate:

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_validate_schema.py --format exp_eval_sol_out --file /path/to/eval_out.json
```

### Script: aii_json_validate_schema.py

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_validate_schema.py --format exp_eval_sol_out --file /tmp/eval_out.json
```

**Parallel execution (multiple validations):**

IMPORTANT: When validating multiple files, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_json_validate_schema.py" && \
parallel -j 50 -k --group --will-cite '$PY $S --format {1} --file {2}' ::: 'exp_sel_data_out' 'exp_gen_sol_out' 'exp_eval_sol_out' :::+ '/tmp/full_data_out.json' '/tmp/method_out.json' '/tmp/eval_out.json'
```

**Example output (success):**
```
Validating: aii_json_validate_schema.py
Format: exp_eval_sol_out

✓ Validation PASSED
```

**Example output (failure):**
```
Validating: aii_json_validate_schema.py
Format: exp_sel_data_out

✗ Validation FAILED

Errors:
  Path: datasets → 0 → examples → 0
  Error: 'output' is a required property
  Validator: required
```

**Parameters:**

`--format` (required)
- Format type to validate against
- Determines which schema to use

`--file` (required)
- Path to JSON file to validate
- Must be valid JSON
- **Always pass an absolute path.** Relative paths resolve from the
  ability server's CWD (typically ``/ai-inventor/aii_server``), not from
  your agent workspace, so ``data_out/x.json`` will silently look in the
  wrong directory and fail with "Could not load JSON file". The validate
  endpoint also accepts a ``workspace_dir`` arg if you need to keep a
  relative path — pass your workspace path there.

**Tips:**
- Fix errors in your JSON and rerun validation until it passes

### Schema Files

Schemas are stored in `.claude/skills/aii-json/schemas/`:

**Hypothesis Selection & Evaluation:**
- `sel_hypo_out.json` - Hypothesis Selection output (all hypotheses with selected flags)
- `feasibility_eval_all.json` - All hypotheses with feasibility scores
- `feasibility_eval_top.json` - Top 5 most feasible hypotheses
- `novelty_research_one.json` - Single hypothesis novelty research arguments with citations
- `novelty_eval_all.json` - All hypotheses with novelty scores
- `novelty_eval_top.json` - Single best selected hypothesis

**Experiment Pipeline:**
- `exp_sel_data_out.json` - Experiment Data Selection format
- `exp_gen_sol_out.json` - Experiment Solution Generation format
- `exp_eval_sol_out.json` - Experiment Solution Evaluation format

---

## Formatting JSON

Generate three size-optimized versions of a JSON file for efficient development and preview:
- **full**: Identical to original (all data)
- **mini**: First 3 items only (for quick testing)
- **preview**: Mini + all strings truncated to 200 chars (for quick inspection)

### Quick Start

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_format_mini_preview.py --input method_out.json
```

### Script: aii_json_format_mini_preview.py

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_format_mini_preview.py --input method_out.json
```

**Parallel execution (multiple files):**

IMPORTANT: When formatting multiple files, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_json_format_mini_preview.py" && \
parallel -j 50 -k --group --will-cite '$PY $S --input {}' ::: 'full_data_out.json' 'method_out.json' 'eval_out.json'
```

**Example output:**
```
Generated 3 versions:
  Full (50 items): /path/to/full_method_out.json
  Mini (3 items): /path/to/mini_method_out.json
  Preview (3 items, truncated): /path/to/preview_method_out.json
```

**Parameters:**

`--input` (required)
- Path to input JSON file
- Must have a top-level array
- Example: `method_out.json`, `full_data_out.json`

`--output-dir` (optional)
- Output directory for generated files
- Default: same directory as input file
- Files are prefixed with `full_`, `mini_`, `preview_`

**Output Files:**

All three files use the same base name with different prefixes:
- `full_{basename}.json` - Complete dataset (identical to original)
- `mini_{basename}.json` - First 3 array items only
- `preview_{basename}.json` - First 3 items with strings truncated to 200 chars

**Tips:**
- Input JSON must have a top-level array structure
- String truncation is recursive (applies to nested objects and arrays)
- Use preview files for quick inspection without reading large datasets
- Use mini files for developing/testing code before running on full dataset

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````

### [6] SKILL-INPUT — aii-python · 2026-07-09 01:16:59 UTC

The agent loaded the **aii-python** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-python
description: Python coding standards for experiment and evaluation scripts. Covers environment setup, logging, error handling, and code structure.
---

## Environment Setup

- Python 3.12+
- **NEVER use `pip` or `.venv/bin/pip`** — they are not installed. Use `uv` for ALL package operations:
  ```bash
  uv venv .venv --python=3.12
  source .venv/bin/activate  # or: .venv/bin/python script.py
  uv pip install pandas loguru  # NOT: pip install
  ```
- Create `.toml` file with dependencies, create uv `.venv` and activate it
- NO inline dependencies (no `# /// script` headers)

## Logging

Use `loguru` for all logging. Add a file sink alongside stdout.

```python
from loguru import logger
import sys

logger.remove()  # Remove default handler
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")
```

Rules:
- Log every major step (data loading, processing start/end, results)
- If applicable, log every LLM API call input and output
- Truncate long outputs in logs (add truncation logic for potentially large strings)
- Use `logger.error()` in except blocks (traceback auto-captured)

## Error Handling

- Wrap major operations in try/except blocks
- Use `@logger.catch(reraise=True)` decorator on main functions — without `reraise=True`, the script exits 0 even on uncaught exceptions, hiding failures from downstream consumers
- Use explicit exception types, not bare `except:`
- Never silently swallow exceptions — always log them

```python
@logger.catch(reraise=True)
def main():
    try:
        data = load_data(path)
    except FileNotFoundError:
        logger.error("Data file not found")
        raise
    except json.JSONDecodeError:
        logger.error("Invalid JSON in data file")
        raise
```

## Code Structure

- Use `pathlib.Path` for file operations: `Path("data/input.json").read_text()` not `open(...).read()`
- Use type hints for function signatures
- Use keyword arguments for functions with more than 4 parameters
- No hardcoded paths — derive from script location or accept as arguments

## Script Pattern

Standard pattern for experiment/evaluation scripts:

```python
#!/usr/bin/env python3
"""Brief description of what this script does."""

from loguru import logger
from pathlib import Path
import json
import sys

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

@logger.catch(reraise=True)
def main():
    # Load data
    data_path = Path("full_data_out.json")
    logger.info(f"Loading data from {data_path}")
    data = json.loads(data_path.read_text())
    logger.info(f"Loaded {len(data['examples'])} examples")

    # Process
    results = []
    for i, example in enumerate(data["examples"]):
        try:
            result = process(example)
            results.append(result)
        except Exception:
            logger.error(f"Failed on example {i}")
            continue

    # Save output
    output = {"examples": results}
    Path("method_out.json").write_text(json.dumps(output, indent=2))
    logger.info(f"Saved {len(results)} results")

if __name__ == "__main__":
    main()
```
````

### [7] SYSTEM-USER prompt · 2026-07-09 01:19:37 UTC

````
YOUR PREVIOUS SESSION WAS INTERRUPTED: A single operation exceeded the 720s message timeout. Each individual operation must complete within 720s. Do NOT mock, skip, or compromise your execution — still do the real work. Try to make operations run faster if possible. If a command genuinely takes longer than 720s, split it into sequential parts that each complete within the time limit.

Last messages before interruption:
  - [agent_tool_call] file_editor: Tool: file_editor
{
  "command": "create",
  "path": "/ai-inventor/aii_data/runs/run_6uOr5GlpaMfR/3_invention_loop/iter_2/gen_plan/gen_plan_experiment_1/validate_json.py",
  "file_text": "#!/usr/bin/env python3\n\"\"\"Validate the plan JSON file\"\"\"\nimport json\n\nplan_path = \"/ai-inventor/aii_d
  - [agent_tool_call] invoke_skill: Tool: invoke_skill
{
  "name": "aii-python"
}
  - [agent_tool_result] file_editor: Tool: file_editor
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "File created successfully at: /ai-inventor/aii_data/runs/run_6uOr5GlpaMfR/3_invention_loop/iter_2/gen_plan/gen_plan_experiment_1/validate_json.py"}], "is_error": false, "command": "create", "path": "/ai-inventor/
  - [agent_tool_result] invoke_skill: Tool: invoke_skill
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "## Environment Setup\n\n- Python 3.12+\n- **NEVER use `pip` or `.venv/bin/pip`** \u2014 they are not installed. Use `uv` for ALL package operations:\n  ```bash\n  uv venv .venv --python=3.12\n  source .venv/bin/
  - [agent_response]: Let me run the validation script to check if the JSON is valid:
  - [agent_tool_call] file_editor: Tool: file_editor
{
  "command": "view",
  "path": "/ai-inventor/aii_data/runs/run_6uOr5GlpaMfR/3_invention_loop/iter_2/gen_plan/gen_plan_experiment_1/.sdk_openhands_agent_struct_out.json",
  "file_text": null,
  "old_str": null,
  "new_str": null,
  "insert_line": null,
  "view_range": [
    1,
   
  - [agent_tool_result] file_editor: Tool: file_editor
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "NOTE: We only show up to 8 since there're only 8 lines in this file.\nHere's the result of running `cat -n` on /ai-inventor/aii_data/runs/run_6uOr5GlpaMfR/3_invention_loop/iter_2/gen_plan/gen_plan_experiment_1/.s
  - [agent_response]: I can see there are escape issues in the JSON file. The quotes within the pseudocode are causing problems. Let me recreate the file with proper JSON escaping:
  - [agent_tool_call] file_editor: Tool: file_editor
{
  "command": "create",
  "path": "/ai-inventor/aii_data/runs/run_6uOr5GlpaMfR/3_invention_loop/iter_2/gen_plan/gen_plan_experiment_1/.sdk_openhands_agent_struct_out.json",
  "file_text": "{\n  \"title\": \"Test Semantic Coherence Distance for Readability\",\n  \"summary\": \"Eval
  - [agent_tool_result] file_editor: Tool: file_editor
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "Invalid `path` parameter: /ai-inventor/aii_data/runs/run_6uOr5GlpaMfR/3_invention_loop/iter_2/gen_plan/gen_plan_experiment_1/.sdk_openhands_agent_struct_out.json. File already exists at: /ai-inventor/aii_data/run
  - [agent_response]: I need to use `str_replace` to update the file. Let me first read the current content and then replace it:
  - [agent_tool_call] file_editor: Tool: file_editor
{
  "command": "str_replace",
  "path": "/ai-inventor/aii_data/runs/run_6uOr5GlpaMfR/3_invention_loop/iter_2/gen_plan/gen_plan_experiment_1/.sdk_openhands_agent_struct_out.json",
  "file_text": null,
  "old_str": "{\n  \"title\": \"Test Semantic Coherence Distance for Readability\"
  - [agent_tool_result] file_editor: Tool: file_editor
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "The file /ai-inventor/aii_data/runs/run_6uOr5GlpaMfR/3_invention_loop/iter_2/gen_plan/gen_plan_experiment_1/.sdk_openhands_agent_struct_out.json has been edited. Here's the result of running `cat -n` on a snippet
  - [agent_response]: The JSON file has been updated. Now let me verify that the JSON is valid by checking its structure. Let me also clean up the temporary files and create a final summary:
  - [agent_tool_call] file_editor: Tool: file_editor
{
  "command": "create",
  "path": "/ai-inventor/aii_data/runs/run_6uOr5GlpaMfR/3_invention_loop/iter_2/gen_plan/gen_plan_experiment_1/validate_plan.py",
  "file_text": "#!/usr/bin/env python3\n\"\"\"Quick validation of the plan JSON file\"\"\"\nimport json\n\nplan_path = \"/ai-inv
  - [agent_tool_result] file_editor: Tool: file_editor
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "File created successfully at: /ai-inventor/aii_data/runs/run_6uOr5GlpaMfR/3_invention_loop/iter_2/gen_plan/gen_plan_experiment_1/validate_plan.py"}], "is_error": false, "command": "create", "path": "/ai-inventor/
  - [agent_response]: Let me try running the validation:
  - [agent_tool_call] think: Tool: think
{
  "thought": "Let me review what I've created:\n\n1. I've created a detailed experiment plan in the `.sdk_openhands_agent_struct_out.json` file\n2. The plan has all required fields: title, summary, runpod_compute_profile, implementation_pseudocode, fallback_plan, testing_plan\n3. The p
  - [agent_tool_result] think: Tool: think
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "Your thought has been logged."}], "is_error": false, "kind": "ThinkObservation"}
  - [agent_response]: Let me create a Python script that will generate the proper JSON file with correct escaping:

CONTINUE FOLLOWING THESE INSTRUCTIONS:

<hypothesis>
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
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. Use it for the methods, proper baselines, and evaluation this field demands.

- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
</available_domain_handbooks>

<artifact_direction>
Make this direction concrete and actionable. Keep the same type and respect dependencies.

id: experiment_iter2_dir1
type: experiment
objective: >-
  Evaluate SCD on CLEAR and OneStopEnglish with correct SBERT implementation and proper baselines
approach: >-
  Load datasets from art_vnKiwBm9Qy9H (CLEAR corpus with human readability judgments, OneStopEnglish with 3 difficulty levels).
  Implement SCD correctly: (1) Use all-MiniLM-L6-v2 SBERT model for sentence embeddings (not the incorrect 2D feature vector
  from prior code), (2) Compute semantic coherence distance as average pairwise cosine distance or squared Euclidean distance
  between consecutive sentence embeddings, (3) Normalize by document length. Implement baseline formulas correctly using textstat
  package (not buggy custom implementation): Flesch-Kincaid, SMOG, Coleman-Liau, Dale-Chall. For CLEAR: compute Pearson correlation
  between each method and human readability judgments (target_score field). For OneStopEnglish: compute classification accuracy
  (3-class: Elementary/Intermediate/Advanced) and F1 score. Add Coh-Metrix LSA baseline if computationally feasible. Output:
  correlations with 95% bootstrap CIs, p-values, classification metrics, scatter plots, and timing measurements.
depends_on:
- id: art_vnKiwBm9Qy9H
  label: dataset
  relation_type:
  relation_rationale:
</artifact_direction>

<dependencies>
Completed artifacts this artifact can use during execution.

--- Dependency 1 ---
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
</dependencies>

<instructions>
YOUR ROLE: Write a detailed PLAN for the artifact. A separate executor agent runs the actual artifact later.

You are a PLANNER, not an executor. Your output is a plan that tells the executor what to do and how.
Do NOT execute the artifact itself — a separate agent handles that. Your job is to plan it so well that the executor can follow your plan step by step.

You CAN and SHOULD: search the web, read papers, and explore library docs to make your plan concrete.
You CANNOT run shell commands or scripts — code execution is disabled. Research via web tools only.

Do NOT do the executor's job: don't download datasets, don't implement code, don't run experiments, don't write proofs, don't compute evaluations.

<artifact_executor_scope>
IMPORTANT: Each artifact executor has a focused prompt that guides it to do ONE thing well. It will NOT perform tasks outside its scope — assigning the wrong work to the wrong artifact type wastes an iteration. Match the task to the right executor.

EXPERIMENT executor scope:
  Output: method_out.json with results (metrics, predictions, analysis) — the core computational work
  DOES: Implement and run methods/algorithms, compute metrics, compare approaches, produce quantitative results
  DOES NOT: Collect new datasets (depends on DATASET artifacts for input data), write formal proofs
  This is the right artifact for any code that processes data and produces results
</artifact_executor_scope>

<artifact_planning_rules>
EXPERIMENT: Must depend on at least one DATASET. Define clear metrics and baselines before running. Consider trying multiple method variations rather than a single approach.
</artifact_planning_rules>

<compute_profiles>
Choose the compute profile this artifact needs for execution.
Available profiles for experiment artifacts:
  - gpu: 1x NVIDIA RTX A4500, 20GB VRAM, 7 vCPUs, 29GB RAM — ML training, CUDA, large models (fallback: GPUs cheap→expensive: 2000 Ada → A4000 → 4000 Ada → L4 → 4090 → 5090)
  - cpu_heavy: 4 vCPUs, 32GB RAM — large datasets, memory-intensive processing (fallback: CPUs cheap→expensive, then GPU hosts cheap→expensive (all ≥32GB RAM))

Set runpod_compute_profile to one of these exact tier names.
</compute_profiles>
GOOD PLANS: specific, actionable, consider failure scenarios, build on the suggested approach.
BAD PLANS: vague hand-waving, ignoring the suggested approach, missing critical executor details.
</instructions><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_6uOr5GlpaMfR/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_6uOr5GlpaMfR/3_invention_loop/iter_2/gen_plan/gen_plan_experiment_1/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "description": "Plan for an EXPERIMENT artifact.",
  "properties": {
    "title": {
      "description": "Plan title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters).",
      "title": "Title",
      "type": "string"
    },
    "summary": {
      "default": "",
      "description": "Brief summary",
      "title": "Summary",
      "type": "string"
    },
    "runpod_compute_profile": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": "cpu_light",
      "description": "Compute tier for execution \u2014 pick from the available profiles list (e.g., 'gpu', 'cpu_heavy', 'cpu_light'). Only used in RunPod mode.",
      "title": "Runpod Compute Profile"
    },
    "implementation_pseudocode": {
      "description": "High-level pseudocode for the experiment implementation",
      "title": "Implementation Pseudocode",
      "type": "string"
    },
    "fallback_plan": {
      "description": "What to do if the primary approach fails - alternative methods, simplified versions",
      "title": "Fallback Plan",
      "type": "string"
    },
    "testing_plan": {
      "description": "How to validate the experiment works: start with small/fast tests, look for confirmation signals before running full-scale experiments",
      "title": "Testing Plan",
      "type": "string"
    }
  },
  "required": [
    "title",
    "implementation_pseudocode",
    "fallback_plan",
    "testing_plan"
  ],
  "title": "ExperimentPlan",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `/ai-inventor/aii_data/runs/run_6uOr5GlpaMfR/3_invention_loop/iter_2/gen_plan/gen_plan_experiment_1/.sdk_openhands_agent_struct_out.json`.

Propose a simple, novel machine-learning method for scoring text readability and validate it.
````

### [8] SKILL-INPUT — aii-use-hardware · 2026-07-09 01:20:16 UTC

The agent loaded the **aii-use-hardware** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-use-hardware
description: Detect hardware and use it responsibly. Covers CPU/RAM/GPU detection, memory-safe data processing, and resource-aware computation.
---

**Step 1** — Run `bash scripts/get_hardware.sh` (relative to this skill's directory).

Read the `=== CGROUP ===` section carefully. If `Type: cgroup v1` or `cgroup v2`:
- You are in a **container with hard resource limits**. Exceeding them = OOM kill, no recovery.
- **Never** use `psutil.virtual_memory().total`, `free -h`, `/proc/meminfo`, `os.cpu_count()`, or `nproc` for resource limits — these report **host** values, not your container's allocation.
- **Always** read limits from the cgroup paths shown in the output, or use the Python helpers below.
- For **runtime memory monitoring**, read current usage from cgroup too:
  - v2: `/sys/fs/cgroup/memory.current`
  - v1: `/sys/fs/cgroup/memory/memory.usage_in_bytes`

**Step 2** — Use Step 1 results to pick package variants **before** installing.

Defaults often target the most powerful environment — PyPI's `torch` ships with CUDA libs even on CPU-only hosts. Wrong variant = wasted disk, slow setup, possible import-time failures.

If `=== GPU ===` shows `No GPU`, install torch's CPU build (skips ~4.5GB of CUDA libs):
```bash
uv pip install torch --extra-index-url https://download.pytorch.org/whl/cpu
```
Same idea for any library whose wheel selection depends on detected hardware (GPU/CPU-only builds, architecture-specific wheels).

After install, sanity-check imports right away (`python -c "import torch"`). Disk-pressure or interrupted installs leave half-built wheels (e.g. `libtorch_global_deps.so` missing) — catch these before the experiment runs.

**Step 3** — Set Python constants from the Step 1 results:
```python
import os, math, torch, psutil
from pathlib import Path

def _detect_cpus() -> int:
    """Detect actual CPU allocation (containers/pods/bare metal)."""
    try:  # cgroups v2 quota
        parts = Path("/sys/fs/cgroup/cpu.max").read_text().split()
        if parts[0] != "max":
            return math.ceil(int(parts[0]) / int(parts[1]))
    except (FileNotFoundError, ValueError): pass
    try:  # cgroups v1 quota
        q = int(Path("/sys/fs/cgroup/cpu/cpu.cfs_quota_us").read_text())
        p = int(Path("/sys/fs/cgroup/cpu/cpu.cfs_period_us").read_text())
        if q > 0:
            return math.ceil(q / p)
    except (FileNotFoundError, ValueError): pass
    try:  # CPU affinity (cpuset — used by RunPod, Docker --cpuset-cpus)
        return len(os.sched_getaffinity(0))
    except (AttributeError, OSError): pass
    return os.cpu_count() or 1

def _container_ram_gb() -> float | None:
    """Read RAM limit from cgroup (containers/pods)."""
    for p in ["/sys/fs/cgroup/memory.max", "/sys/fs/cgroup/memory/memory.limit_in_bytes"]:
        try:
            v = Path(p).read_text().strip()
            if v != "max" and int(v) < 1_000_000_000_000:
                return int(v) / 1e9
        except (FileNotFoundError, ValueError): pass
    return None

NUM_CPUS = _detect_cpus()
HAS_GPU = torch.cuda.is_available()
VRAM_GB = torch.cuda.get_device_properties(0).total_mem / 1e9 if HAS_GPU else 0
DEVICE = torch.device("cuda" if HAS_GPU else "cpu")
TOTAL_RAM_GB = _container_ram_gb() or psutil.virtual_memory().total / 1e9
AVAILABLE_RAM_GB = min(psutil.virtual_memory().available / 1e9, TOTAL_RAM_GB)
```

## Step 4 — Set Memory Limits

OOM kills the entire container. **Every script MUST set RAM and VRAM limits at startup.**

Decide the budget based on what the script actually needs. Estimate data size × 2-5x for in-memory overhead, then add ~50% breathing room for temporaries. You may use up to 90% of available RAM/VRAM, but **scale gradually** — start small (e.g. 30-50%), verify it works, then increase toward the limit. Never exceed 90% to keep a buffer for the OS, system processes, and the agent runtime itself. Going over crashes the container/machine with no recovery.

```python
import resource, psutil

_avail = psutil.virtual_memory().available
RAM_BUDGET = ???  # YOU decide: estimate what this script needs (in bytes)
assert RAM_BUDGET < _avail, f"Budget {RAM_BUDGET/1e9:.1f}GB > available {_avail/1e9:.1f}GB"
resource.setrlimit(resource.RLIMIT_AS, (RAM_BUDGET * 3, RAM_BUDGET * 3))  # 3x: virtual > RSS; raises MemoryError on exceed

if HAS_GPU:
    _free, _total = torch.cuda.mem_get_info(0)
    VRAM_BUDGET = ???  # YOU decide: estimate GPU memory needs
    torch.cuda.set_per_process_memory_fraction(min(VRAM_BUDGET / _total, 0.95))  # raises OutOfMemoryError on exceed
```

## Memory-Safe Data Processing

- **One at a time**: load one large object → process → `del obj; gc.collect()` → next
- **Load only what you need**: select specific tables/columns/rows, not entire databases
- **Test small first**: run on a sample before scaling to full data to estimate memory/time
- **Free intermediates in loops**: don't accumulate large results — aggregate incrementally
- **Size before loading**: check file/dataset size before loading; if it's >30% of `RAM_BUDGET`, chunk it

## Common Mistakes (from real crashes)

- **Skipping this skill entirely** — loading data with no RAM detection, no limits, no budget. Container OOM-killed, all agents lost.
- **Using `psutil.virtual_memory().total` instead of `_container_ram_gb()`** — reports host RAM (e.g. 66 GB) when container limit is 28 GB. You MUST use the cgroup-aware functions above.
- **Loading all tables from a multi-table database at once** — one agent loaded 14 RelBench tables simultaneously, spiked past container limit.
- **Setting no memory limits** — without `resource.setrlimit` (RAM) and `set_per_process_memory_fraction` (VRAM), a runaway script OOM-kills the container instead of raising a catchable error.
- **Using `os.cpu_count()` directly** — returns host CPUs (e.g. 192) instead of container limit (e.g. 4) on RunPod/Docker. Always use `_detect_cpus()` above which checks cgroup quota → CPU affinity → `os.cpu_count()` in order.

## Hardware Use

- Keep these results in mind for ALL subsequent tasks — don't assume more than detected
- GPU if available and parallelizable, multiprocessing if multiple CPUs
- Push available resources to their full potential — don't leave hardware idle
````
