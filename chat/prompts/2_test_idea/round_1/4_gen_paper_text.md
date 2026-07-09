# gen_paper_text — test_idea

> Phase: `invention_loop` · round 1 · `gen_paper_text`
> Run: `run_6uOr5GlpaMfR` — Readability Scoring Model
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_paper_text` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-07-09 00:36:26 UTC

````
<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. Use it for related-work positioning and how this field frames a genuinely novel contribution.

- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
</available_domain_handbooks>
<hypothesis>
The research hypothesis.

kind: hypothesis
title: Semantic Control Energy for Readability
hypothesis: >-
  Text readability can be quantified by the minimum 'control energy' required to traverse the semantic trajectory of a text,
  where readable texts require minimal energy to follow their semantic progression while unreadable texts require large energy
  corrections due to jarring semantic jumps or excessive repetition.
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
</hypothesis>

<all_artifacts>
FULL EVIDENCE BASE: All 3 research artifacts across all iterations.

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
</all_artifacts>

<new_artifacts_this_iteration>
NEW THIS ITERATION: These 3 artifacts were created to address the reviewer
feedback. Their findings should be the primary basis for your revisions.

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
</new_artifacts_this_iteration>

<data_files>
Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</data_files>

<task>
Write a research paper draft with LaTeX-ready text, BibTeX citations, and figure placeholders.

This is the FIRST paper draft. Write a complete research paper from scratch based on the hypothesis and all available artifacts.
</task>

<figure_instructions>
FIGURE FORMAT: Use [FIGURE:fig_id] markers in paper_text to indicate where each figure goes.
Then provide the full figure specs in the separate `figures` structured output array.
Each figure in the array must have an `id` matching a marker in the text. Set the `aspect_ratio`
field per figure: 21:9 for architecture / pipeline / flow-chart diagrams (the hero figure should
be one of these — place its marker near the END of the Introduction so it floats to the top of
page 2), 16:9 for comparisons / multi-panel results, 4:3 for dense charts, 1:1 for heatmaps /
confusion matrices / scatter plots.

Example in paper_text:
  "...our method achieves state-of-the-art results as shown below.\n\n[FIGURE:fig3]\n\nThe results demonstrate..."

Example in figures array (results comparison):
  {"id": "fig3", "title": "Performance Comparison", "caption": "Comparison of geometric mean query latency across optimizers.", "image_gen_detailed_description": "Grouped bar chart. X-axis: model names. Y-axis: latency (seconds, 0-5). Values: PostgreSQL=4.6s (red), Bao=2.8s (blue), RLQOpt=2.0s (green). Error bars +/-0.3-0.8. Sans-serif font, white background.", "aspect_ratio": "16:9", "summary": "Compares latency across optimizers"}

Example in figures array (architecture diagram, hero):
  {"id": "fig1", "title": "System Architecture", "caption": "End-to-end pipeline: encoder feeds latents into the planner, which queries the value head before emitting actions.", "image_gen_detailed_description": "Horizontal flow diagram, left to right. Five labeled boxes: 'Input' (gray), 'Encoder' (blue), 'Latent (z, 256-dim)' (light blue, narrow), 'Planner' (green), 'Action Head' (orange). Arrows labeled with shapes. Value head as separate green box below 'Planner', bidirectional arrow. Sans-serif font, clean white background, no 3D.", "aspect_ratio": "21:9", "summary": "Hero architecture diagram"}

CRITICAL: Before writing figure specs, look through artifact workspace output files (*_out.json)
and code to find ALL the exact values. The figure generator cannot read files — every exact number
and value MUST be in the image_gen_detailed_description.
</figure_instructions>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-paper-writing, aii-semscholar-bib.
TODO 2. LITERATURE REVIEW: Use web search tools to research the landscape — search key terms from
<hypothesis> and <all_artifacts>. Then use aii_semscholar_bib__fetch to batch-fetch real
BibTeX entries. Build a comprehensive Related Work section. Do NOT fabricate entries.
TODO 3. READ ARTIFACTS: Before writing each section, READ the relevant artifact source code, output
files, and data in the workspace. Extract concrete implementation details, technical innovations,
algorithmic specifics, and quantitative results. Do NOT write surface-level descriptions.

ARTIFACT REFERENCES: When you reference results, methodology, or findings from a specific artifact,
place an [ARTIFACT:artifact_id] marker inline. These become footnotes linking to the artifact's code
in the GitHub repository (first mention gets a footnote with URL, subsequent mentions are omitted).
Use the exact artifact ID from <all_artifacts>. Place the marker right after the claim it supports.
Example:
  "Our evaluation showed a 15% improvement over baselines [ARTIFACT:art_4f9d2c81ab37]." 
TODO 4. WRITE PAPER: Write the full paper text with [FIGURE:fig_id] markers per <figure_instructions>,
and provide the figure specs in the figures array. Cite with numeric references [1], [2], etc.
At the end of the paper text, include a full bibliography section. Do NOT compile LaTeX or generate
actual image/figure files. Your ONLY output is the structured JSON.
</todos><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_6uOr5GlpaMfR/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_6uOr5GlpaMfR/3_invention_loop/iter_1/gen_paper_text/gen_paper_text/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "FigureSpec": {
      "description": "Figure specification \u2014 structured output from paper writing agent.\n\nThe LLM fills these as a list in PaperText.figures.\nLater converted to Figure objects for viz gen.",
      "properties": {
        "id": {
          "description": "Figure ID matching the [FIGURE:id] marker in paper_text (e.g., 'fig1')",
          "title": "Id",
          "type": "string"
        },
        "title": {
          "description": "Figure title in plain, everyday language \u2014 short and jargon-free. Aim for about 4-8 words (~40 characters).",
          "title": "Title",
          "type": "string"
        },
        "caption": {
          "description": "LaTeX figure caption \u2014 appears below the figure in the paper. Should describe what the figure shows and highlight key takeaways.",
          "title": "Caption",
          "type": "string"
        },
        "image_gen_detailed_description": {
          "description": "Detailed image generation prompt \u2014 axes, labels, ALL numeric values, colors, aspect ratio, layout. The image generator cannot read files; this is its ONLY input.",
          "title": "Image Gen Detailed Description",
          "type": "string"
        },
        "summary": {
          "description": "Brief summary of what this figure communicates",
          "title": "Summary",
          "type": "string"
        }
      },
      "required": [
        "id",
        "title",
        "caption",
        "image_gen_detailed_description",
        "summary"
      ],
      "title": "FigureSpec",
      "type": "object"
    }
  },
  "description": "Paper text \u2014 structured output from paper writing agent.\n\nStructured output fields (LLMPrompt + LLMStructOut):\n- title, abstract, paper_text, figures, summary\n\npaper_text contains [FIGURE:fig_id] markers for positioning.\nfigures contains the full specs as structured objects.\n\nMetadata fields (plain, set by pipeline code):\n- id",
  "properties": {
    "title": {
      "description": "Paper title \u2014 clear, plain-language, and short so a non-expert understands the main contribution at a glance. Aim for about 6-10 words; avoid jargon and acronyms.",
      "title": "Title",
      "type": "string"
    },
    "abstract": {
      "description": "Paper abstract",
      "title": "Abstract",
      "type": "string"
    },
    "paper_text": {
      "description": "Full paper body text with markdown section headers (# Introduction, # Methods, # Results, # Discussion, # Conclusion). Use [FIGURE:fig_id] markers (e.g. [FIGURE:fig1]) to indicate where each figure should appear.",
      "title": "Paper Text",
      "type": "string"
    },
    "figures": {
      "description": "List of figure specifications. Each must have an id matching a [FIGURE:id] marker in paper_text.",
      "items": {
        "$ref": "#/$defs/FigureSpec"
      },
      "title": "Figures",
      "type": "array"
    },
    "summary": {
      "description": "Brief summary of the paper's main contribution and findings",
      "title": "Summary",
      "type": "string"
    }
  },
  "required": [
    "title",
    "abstract",
    "paper_text",
    "summary"
  ],
  "title": "PaperText",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `/ai-inventor/aii_data/runs/run_6uOr5GlpaMfR/3_invention_loop/iter_1/gen_paper_text/gen_paper_text/.sdk_openhands_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-07-09 00:36:26 UTC

```
Propose a simple, novel machine-learning method for scoring text readability and validate it.
```

### [3] SKILL-INPUT — aii-paper-writing · 2026-07-09 00:36:35 UTC

The agent loaded the **aii-paper-writing** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-paper-writing
description: Academic paper writing guidance for AI research. Covers paper structure, figure placeholders, bibliography building with Semantic Scholar, and citation rules. Does NOT cover LaTeX compilation or figure file generation — see aii-paper-to-latex for that.
---

## Technical Papers

Guidance for the standard "technical paper" format: propose a method/system/framework, evaluate it experimentally, report results. This is the main track at most CS venues (NeurIPS, ICML, ICLR, ACL, AAAI, etc.). Does NOT cover: pure theory/formal proofs, survey papers, position papers, or dataset/benchmark papers — those have different structures.

### Paper Structure

Target 6-8 pages. Use formal academic language, third person. Support claims with evidence from artifacts.

#### Rough Page Budget (8-page paper)

| Section | Pages | Notes |
|---|---|---|
| Abstract | 0.3 | Problem, approach, key result |
| Introduction | 1.0-1.5 | The most important section |
| Related Work | 0.5-1.0 | Beginning or end (see below) |
| Methods | 1.5-2.0 | Architecture fig on page 1 |
| Experiments | 1.5-2.0 | Setup + results + ablations |
| Discussion | 0.5-1.0 | Limitations go here |
| Conclusion | 0.3-0.5 | Do not repeat the abstract |
| References | 0.5-1.0 | Not counted in page limit |

**Critical rule**: A clear new technical contribution must be articulated by page 3 (quarter of the paper). If the reader doesn't know what you did by then, you've lost them.

#### Section Details

**Abstract** (150-250 words): State the problem, your approach, and the main results. Be factual and comprehensive. Do not repeat the abstract word-for-word later in the paper.

**Introduction** — Follow this 5-paragraph structure:

1. **What is the problem?** Define the task concretely.
2. **Why is it interesting and important?** Real-world impact, scale.
3. **Why is it hard?** Why do naive approaches fail?
4. **Why hasn't it been solved before?** What's wrong with prior solutions? How does yours differ?
5. **What are the key components of your approach and results?** Include specific limitations.

End with a "Summary of Contributions" subsection — bullet list of contributions with section references. This doubles as an outline, saving space.

**Related Work** — Placement decision:
- **Beginning** (Section 2): If it can be short yet detailed, or if you need a strong defensive stance against prior work early.
- **End** (before Conclusions): If comparisons require your technical content, or if it can be summarized briefly in the Introduction. Can be titled "Discussion and Related Work."

**Methods/Approach**: Every section tells a story — the story of the results, NOT the story of how you arrived at them. Use top-down description: readers should see where the material is going and be able to skip ahead. Move gory details to appendices.

**Experiments**: Setup (datasets, metrics, baselines) → main results → ablations → analysis. Every claim needs quantitative evidence.

**Discussion**: Interpret results, compare to prior work, state limitations honestly. Limitations should be specific and actionable, not vague disclaimers.

**Conclusion**: Short summarizing paragraph. Do NOT repeat material from the Abstract or Introduction. Make original claims more concrete (e.g., reference quantitative results). Include future work as bullet list — if actively pursuing follow-up, say so to mark territory.

#### Writing Quality Rules

- Define all notation/terminology before use, only once. Group global definitions in Preliminaries.
- Do NOT use nonreferential "this", "that", "these", "it". Always specify the referent. BAD: "This is important because..." GOOD: "This accuracy gap is important because..."
- Do NOT use "etc." unless remaining items are completely obvious. BAD: "We measure volatility, scalability, etc." GOOD: "We measure volatility and scalability."
- Do NOT write "for various reasons" — state the actual reasons.
- "That" is defining, "which" is nondefining. "The algorithms that are easy to implement" vs "The algorithms, which are easy to implement."
- Use italics for definitions and quotes, not for emphasis. Context alone should provide emphasis.

### Figure Format

Figures use a hybrid marker + structured array approach. ALL figures are generated by a separate pipeline step using an AI image model — your `image_gen_detailed_description` is the ONLY input that model sees. It cannot read files or access data. Do NOT generate actual image files yourself (no matplotlib, no PIL, no image generation scripts).

**In paper_text**: Place `[FIGURE:fig_id]` markers where figures should appear.

**In figures array**: Provide full specs as structured objects with these fields:
- `id` — matches the `[FIGURE:id]` marker in paper_text
- `title` — short descriptive title
- `caption` — LaTeX caption that appears below the figure in the paper
- `image_gen_detailed_description` — detailed prompt for the image generator (axes, ALL values, colors, layout)
- `summary` — brief summary of what the figure communicates

Example in paper_text:
```
...our method achieves state-of-the-art results as shown below.

[FIGURE:fig_1]

The results in Figure 1 demonstrate...
```

Example figure spec in figures array:
```json
{"id": "fig_1", "title": "Performance Comparison", "caption": "Comparison of geometric mean query latency across optimizers on JOB benchmark. RLQOpt achieves 2.3x speedup over PostgreSQL.", "image_gen_detailed_description": "Grouped bar chart. X-axis: model names. Y-axis: accuracy (0.0-1.0). Values: ModelA=0.847, ModelB=0.762, Baseline=0.531. Error bars with std: 0.02, 0.03, 0.05. Sans-serif font, white background.", "summary": "Compares accuracy of proposed methods vs baseline."}
```

Every marker in text MUST have a matching figure in the array, and vice versa.

#### Data Precision Requirement

`image_gen_detailed_description` MUST include exact numbers from artifact output files. Read the actual output files before writing figure specs.

- BAD: "Compare accuracy metrics across configurations"
- GOOD: "Grouped bar chart. X-axis: model names. Y-axis: accuracy (0.0-1.0). Values: K=3: 0.765, K=5: 0.729, Baseline: 0.121."

#### Figure vs Table Decision

Do NOT create figures for tabular data (rows/columns of text or numbers). Use `\begin{table}` in LaTeX instead. Figures are for actual visualizations only (charts, plots, diagrams).

#### Figure Placement Strategy

Be intentional with figure ordering. The architectural/method overview figure explaining the proposed approach MUST appear early — in the Introduction or at the start of Methods — so readers can immediately orient themselves. Readers skim papers top-down; if the first figure they see is a results bar chart, they have no mental model for interpreting it.

Recommended ordering:
1. **Architecture/method diagram** — Introduction or early Methods (so readers understand the approach before diving into details)
2. **Conceptual/analogy figures** — Introduction or Methods (to build intuition)
3. **Results figures** (bar charts, line plots, scatter plots) — Results section
4. **Analysis/ablation figures** — Discussion or later Results

#### Guidelines

- Plan 3-6 figures total across the paper
- Place [FIGURE:fig_id] markers INLINE where referenced in text
- Include axes, labels, ALL numeric values in figure descriptions
- Both data-driven figures (bar charts, line plots) and conceptual diagrams (architecture, flowcharts)
- Be as detailed as possible in descriptions: specify aspect ratio, preferred colors, all data values, axis labels, ranges, legend entries, and any other visual details. The more specific the description, the better the generated figure

### Bibliography with Semantic Scholar

Build `./references.bib` using the aii-semscholar-bib skill (real BibTeX from Semantic Scholar):

1. Collect DOIs, ArXiv IDs, or titles for all papers you need to cite
2. Call `aii_semscholar_bib__fetch` with the full list in one batch
3. Write the returned .bib text into `./references.bib`

Rules:
- Do NOT fabricate BibTeX entries — always fetch from Semantic Scholar
- If a paper isn't found (very recent preprint), write the entry manually as fallback
- Use `\bibliography{references}` and `\bibliographystyle{plainnat}`
- Do NOT use inline `thebibliography` environment

### Citation Format (for Research Artifacts)

When writing research with numbered citations:

1. Every factual claim MUST have a numbered citation: `[1]`, `[2]`, `[1, 3]`, etc.
2. Each source in the "sources" array MUST have an "index" field
3. The index MUST EXACTLY MATCH citation numbers in the text
4. NEVER cite a number without a matching source index
5. Example: "LLMs show 40% improvement with multi-agent collaboration [1]."
````

### [4] SKILL-INPUT — aii-semscholar-bib · 2026-07-09 00:36:35 UTC

The agent loaded the **aii-semscholar-bib** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-semscholar-bib
description: Build bibliographies using Semantic Scholar. Batch-fetch BibTeX for papers by DOI, ArXiv ID, or title. Use when writing papers, generating reference lists, or building .bib files.
---

## Tool: `aii_semscholar_bib__fetch`

Batch-fetch BibTeX entries from Semantic Scholar. Pass all references in a single call — the tool handles batching internally.

### How it works

1. **DOI/ArXiv refs** → batched into POST /paper/batch calls (up to 500 per API call, auto-chunked)
2. **Title-only refs** → individual GET /paper/search/match (1s delay between)
3. **Post-process** → fix entry type, fix citation key (AuthorYYYY), inject DOI

The ability server runs a single worker (`max_threads: 1`). Multiple concurrent tool calls are queued — each runs independently (no cross-request aggregation). Batching happens within each request.

### Input format

```json
{
  "references": [
    {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
    {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
    {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
  ]
}
```

Each reference object can have:
- `doi` — DOI string (ArXiv DOIs like `10.48550/arXiv.XXXX.XXXXX` auto-convert to ArXiv IDs)
- `arxiv` — ArXiv ID (e.g. `"2305.14325"`)
- `title` — Paper title (used for search/match when no DOI/ArXiv)
- `author` — First author last name (for cleaner citation key)
- `year` — Publication year (int, for citation key)

At least one of `doi`, `arxiv`, or `title` is required per reference.

### Output format

```json
{
  "success": true,
  "bib_text": "@inproceedings{Vaswani2017, ...}\n\n@article{Wei2022, ...}",
  "total": 3,
  "found": 3,
  "failed_count": 0,
  "entries": [{"citation_key": "Vaswani2017", "bibtex": "...", "title": "...", "doi": "...", "arxiv": ""}],
  "failed": []
}
```

### Workflow

1. Collect DOIs, ArXiv IDs, or titles for all papers you need to cite
2. Call `aii_semscholar_bib__fetch` with the full list in **one call**
3. Save `bib_text` from the response to your `references.bib` file
4. Check `failed` — for any missed papers, follow the **fallback procedure** below

### Fallback for failed references (MANDATORY)

NEVER fabricate BibTeX. For each failed reference:
1. **WebSearch** for `"Title" author year` (try `site:arxiv.org` too)
2. **WebFetch** the paper page → extract title, authors, year, venue, DOI/ArXiv ID
3. If DOI/ArXiv found → retry `aii_semscholar_bib__fetch` with it
4. Last resort: write BibTeX by hand using **only verified info from the actual paper page**

---

### CLI (for manual use / debugging)

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-semscholar-bib" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_semscholar_bib__fetch.py --refs '[
  {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
  {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
  {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
]'
```

`--json, -j` — output raw JSON instead of .bib text

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````

### [5] SKILL-INPUT — aii-web-tools · 2026-07-09 00:37:06 UTC

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
