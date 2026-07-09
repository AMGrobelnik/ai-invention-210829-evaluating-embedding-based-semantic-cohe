# gen_full_paper — report_results

> Phase: `gen_paper_repo` · `gen_full_paper`
> Run: `run_6uOr5GlpaMfR` — Readability Scoring Model
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_full_paper` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-07-09 03:33:01 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_6uOr5GlpaMfR/4_gen_paper_repo/_4_assemble_paper/paper/workspace`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_6uOr5GlpaMfR/4_gen_paper_repo/_4_assemble_paper/paper/workspace/`:
GOOD: `/ai-inventor/aii_data/runs/run_6uOr5GlpaMfR/4_gen_paper_repo/_4_assemble_paper/paper/workspace/file.py`, `/ai-inventor/aii_data/runs/run_6uOr5GlpaMfR/4_gen_paper_repo/_4_assemble_paper/paper/workspace/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>

<task>
Create a publication-ready top-conference LaTeX paper with BibTeX from <paper_text> and <available_figures>, compile to PDF.
</task>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<paper_text>
title: >-
  Evaluating Embedding-Based Semantic Coherence for Readability Assessment: An Empirical Study
abstract: |-
  Traditional readability formulas (Flesch-Kincaid, SMOG, Coleman-Liau) rely on surface-level features—sentence length and word complexity—that fail to capture semantic coherence, a key dimension of reading difficulty. While measuring semantic coherence via embedding distances is an established technique (Coh-Metrix, 2004; TextDescriptives, 2023), comprehensive empirical evaluation on standard readability benchmarks remains limited. We evaluate **Semantic Coherence Distance (SCD)**, defined as the average cosine distance between consecutive sentence embeddings, on three datasets: the CLEAR corpus (n=1000, human judgments), OneStopEnglish (n=264, 3-class classification), and a synthetic dataset (n=60, controlled difficulty levels). Results show that SCD achieves statistically significant but weak correlation with human readability judgments on CLEAR (Pearson r=0.1202, p=0.0001), while Flesch-Kincaid achieves stronger correlation (r=-0.4958, p<0.0001). On OneStopEnglish, an ensemble of SCD and Flesch-Kincaid achieves 71.2% classification accuracy. On synthetic data, SCD correlates with true grade levels at r=0.5442 [95% CI: 0.3603, 0.7135], provides unique signal beyond Flesch-Kincaid (partial correlation r=0.294, p=0.022), and an ensemble of both metrics achieves the best performance (r=0.6777). We conclude that embedding-based semantic coherence captures complementary information to surface features, but alone is not competitive with traditional formulas. The contribution of this work is an honest empirical evaluation that quantifies when and how semantic coherence metrics add value to readability assessment.

  **Keywords:** readability assessment, semantic coherence, sentence embeddings, TF-IDF, empirical evaluation
paper_text: "# 1 Introduction\n\nReadability assessment—the automatic prediction of how difficult a text is to understand—has\
  \ practical importance in education, content recommendation, and assistive technologies for language learners. Traditional\
  \ readability formulas such as Flesch-Kincaid Grade Level (FKGL) [8], the SMOG index [10], and the Coleman-Liau Index [3]\
  \ have served as standard tools for decades. These formulas operate on surface-level statistics: they count words per sentence,\
  \ syllables per word, and characters per word, then combine these counts in a linear regression to predict a \"grade level\"\
  \ [1].\n\nDespite their simplicity and widespread adoption, traditional formulas have a well-documented limitation: they\
  \ rely on \"weak proxies of word decoding (i.e., characters or syllables per word) and syntactic complexity (i.e., number\
  \ of words per sentence)\" while ignoring \"text features that are important components of reading models including text\
  \ cohesion and semantics\" [1]. A text can use simple words yet remain incomprehensible if its sentences jump erratically\
  \ between unrelated topics; conversely, a text can use sophisticated vocabulary yet remain readable if its semantic progression\
  \ is smooth and well-signposted.\n\nThis limitation has motivated researchers to incorporate semantic coherence into readability\
  \ assessment. **Semantic coherence** measures how meaningfully sentences connect to form a unified discourse. Coh-Metrix\
  \ (Graesser et al., 2004) computes LSA-based coherence metrics to measure semantic similarity between text segments [5].\
  \ TextDescriptives (2023) implements \"first-order coherence\" as the cosine similarity between consecutive sentence embeddings\
  \ [7]. Word Mover's Distance has been applied as a post-processing step for readability assessment (Imperial et al., 2021)\
  \ [6].\n\nGiven that measuring semantic coherence via embedding distances is an established technique, the contribution\
  \ of this paper is not methodological novelty. Rather, our contribution is a **comprehensive empirical evaluation** of how\
  \ semantic coherence distance performs across multiple standard readability benchmarks, compared against traditional formulas,\
  \ and in combination with them.\n\nSpecifically, we evaluate **Semantic Coherence Distance (SCD)**, defined as the average\
  \ cosine distance between consecutive sentence embeddings in a text. We implement SCD using TF-IDF embeddings (due to computational\
  \ constraints preventing SBERT use) and evaluate on three datasets:\n\n1. **CLEAR Corpus** (n=1000): Contains human readability\
  \ judgments from 1,116 teachers [1]. We report Pearson correlation between SCD/FK and human judgments.\n\n2. **OneStopEnglish**\
  \ (n=264): Contains texts at three difficulty levels (Elementary, Intermediate, Advanced) [11]. We report 3-class classification\
  \ accuracy using SCD and FK as features.\n\n3. **Synthetic Dataset** (n=60): Contains texts with controlled difficulty levels\
  \ (simple, medium, complex) \\footnote{Code: \\url{https://github.com/AMGrobelnik/ai-invention-210829-evaluating-embedding-based-semantic-cohe/tree/main/round-1/experiment-1}}.\
  \ We report correlation with true grade levels, Williams test for dependent correlations, complementarity analysis, and\
  \ ensemble performance.\n\nOur key findings are:\n\n1. SCD achieves statistically significant but weak correlation with\
  \ human readability judgments on CLEAR (r=0.1202, p=0.0001), while FK achieves stronger correlation (r=-0.4958, p<0.0001).\n\
  \n2. On OneStopEnglish, an ensemble of SCD and FK achieves 71.2% classification accuracy, demonstrating that the two signals\
  \ provide complementary information.\n\n3. On synthetic data, SCD correlates with true grade levels at r=0.5442 [0.3603,\
  \ 0.7135], provides unique signal beyond FK (partial r=0.294, p=0.022), and an ensemble achieves best performance (r=0.6777).\n\
  \n4. SCD is computationally efficient (0.022 ms per document), making it suitable for real-time applications.\n\n[FIGURE:fig1]\n\
  \n---\n\n# 2 Related Work\n\n## 2.1 Traditional Readability Formulas\n\nThe Flesch Reading Ease formula [8] and its derivative\
  \ Flesch-Kincaid Grade Level [8] remain the most widely used readability metrics. FKGL predicts U.S. grade level from average\
  \ sentence length and average word syllables. The SMOG index [10] counts polysyllabic words and is widely used for health-related\
  \ texts. The Coleman-Liau Index [3] uses character counts rather than syllables, making it easier to computerize.\n\nAll\
  \ these formulas share a common limitation: they treat readability as a linear function of surface statistics, ignoring\
  \ semantics and discourse structure. The CLEAR corpus paper explicitly criticizes this approach, noting that traditional\
  \ formulas \"ignore many text features that are important components of reading models including text cohesion and semantics\"\
  \ [1].\n\n## 2.2 Semantic Coherence for Readability\n\n**Coh-Metrix** (Graesser et al., 2004) analyzes texts on over 200\
  \ measures of cohesion, language, and readability [5]. It computes LSA-based coherence metrics that measure semantic similarity\
  \ between text segments. Coh-Metrix has been widely used for readability assessment since 2004.\n\n**TextDescriptives**\
  \ (2023) implements a \"first-order coherence\" metric defined as the cosine similarity between consecutive sentences using\
  \ word embeddings [7]. This is conceptually identical to the Semantic Coherence Distance (SCD) metric evaluated in this\
  \ paper.\n\n**Word Mover's Distance (WMD)** has been applied to readability assessment as a post-processing step (Imperial\
  \ et al., 2021) [6]. WMD is a more sophisticated optimal transport metric that measures semantic distance between documents\
  \ more accurately than simple embedding distances.\n\n**BERT embeddings** have been demonstrated to capture complexity signals\
  \ for readability assessment (Imperial, 2021) [9]. Transformer-based embeddings encode readability-related information and\
  \ can be used as features for readability classification.\n\n## 2.3 Our Contribution\n\nMeasuring semantic coherence via\
  \ sentence embedding distances is not novel. Coh-Metrix (2004) uses LSA for coherence [5], TextDescriptives (2023) implements\
  \ first-order coherence [7], and WMD has been applied to readability (2021) [6]. \n\nThe contribution of this work is an\
  \ **honest empirical evaluation** of SCD on standard readability datasets. We quantify:\n1. How SCD correlates with human\
  \ readability judgments (CLEAR corpus)\n2. Whether SCD improves classification accuracy (OneStopEnglish)\n3. Whether SCD\
  \ provides unique signal beyond traditional formulas (complementarity analysis)\n4. Whether an ensemble of SCD and FK outperforms\
  \ either metric alone\n\n---\n\n# 3 Methods\n\n## 3.1 Semantic Coherence Distance (SCD)\n\nGiven a text document $D$ consisting\
  \ of $T$ sentences $\\{s_1, s_2, \\ldots, s_T\\}$, we compute the Semantic Coherence Distance as:\n\n$$\n\\text{SCD}(D)\
  \ = \\frac{1}{T-1} \\sum_{t=1}^{T-1} d(\\mathbf{x}_t, \\mathbf{x}_{t+1})\n$$\n\nwhere $\\mathbf{x}_t \\in \\mathbb{R}^d$\
  \ is the embedding vector for sentence $s_t$, and $d(\\cdot, \\cdot)$ is cosine distance:\n\n$$\nd(\\mathbf{x}_t, \\mathbf{x}_{t+1})\
  \ = 1 - \\frac{\\mathbf{x}_t \\cdot \\mathbf{x}_{t+1}}{\\|\\mathbf{x}_t\\| \\|\\mathbf{x}_{t+1}\\|}\n$$\n\nSCD measures\
  \ the average semantic \"jump\" between consecutive sentences. Texts with smooth semantic progression have low SCD; texts\
  \ with abrupt topic changes have high SCD.\n\n**Interpretation:** SCD captures a specific dimension of readability—semantic\
  \ flow. A text with simple words but erratic topic shifts (\"The cat sat. Quantum physics studies particles. I like apples.\"\
  ) would have high SCD despite low FKGL. Conversely, a text with sophisticated vocabulary but smooth topical development\
  \ would have low SCD despite high FKGL.\n\n[FIGURE:fig2]\n\n## 3.2 Embedding Strategy\n\nDue to computational constraints\
  \ (SBERT embedding timed out in our environment), we use **TF-IDF embeddings** as a computationally efficient approximation:\n\
  \n1. Tokenize the document into sentences\n2. Fit a TF-IDF vectorizer on the sentences\n3. Transform each sentence to its\
  \ TF-IDF vector\n4. Compute cosine distances between consecutive sentence vectors\n\nWhile TF-IDF is less semantically rich\
  \ than SBERT embeddings, it provides a reasonable approximation for measuring topical coherence. We acknowledge this limitation\
  \ and discuss its implications in Section 5.\n\n## 3.3 Baseline: Flesch-Kincaid Grade Level\n\nWe implement Flesch-Kincaid\
  \ Grade Level using the `textstat` package (with manual fallback):\n\n$$\n\\text{FKGL} = 0.39 \\left(\\frac{\\text{total\
  \ words}}{\\text{total sentences}}\\right) + 11.8 \\left(\\frac{\\text{total syllables}}{\\text{total words}}\\right) -\
  \ 15.59\n$$\n\nFKGL predicts U.S. grade level from surface statistics. Lower values indicate easier texts.\n\n## 3.4 Ensemble\
  \ Model\n\nWe evaluate a simple ensemble that combines SCD and FK predictions:\n\n$$\n\\hat{y}_{\\text{ensemble}} = \\frac{z(\\\
  text{SCD}) + z(\\text{FK})}{2}\n$$\n\nwhere $z(\\cdot)$ denotes z-score standardization. The ensemble prediction is the\
  \ average of standardized SCD and FK predictions. This requires no training and serves as a simple baseline for combining\
  \ the two signals.\n\n---\n\n# 4 Experiments\n\n## 4.1 Datasets\n\n### 4.1.1 CLEAR Corpus\n\nThe CommonLit Ease of Readability\
  \ (CLEAR) Corpus contains 4,724 text excerpts with human readability judgments from 1,116 teachers (111,347 pairwise comparisons)\
  \ [1]. Each excerpt has a continuous readability score (lower = easier). We use a 1000-example subset for evaluation [ARTIFACT:art_6GfNHUSj2d-1].\n\
  \n### 4.1.2 OneStopEnglish\n\nThe OneStopEnglish corpus contains 567 texts at three difficulty levels: Elementary, Intermediate,\
  \ and Advanced [11]. Texts are parallel articles rewritten at different reading levels. We use 264 valid examples after\
  \ preprocessing [ARTIFACT:art_6GfNHUSj2d-1].\n\n### 4.1.3 Synthetic Dataset\n\nA synthetic dataset with 60 examples across\
  \ three difficulty tiers:\n- **Simple** (grade 1-3): 20 examples using basic vocabulary\n- **Medium** (grade 4-8): 20 examples\
  \ using moderate vocabulary\n- **Complex** (grade 9-16): 20 examples using academic prose\n\nEach example has a \"true\"\
  \ grade level assigned stochastically within its tier range .\n\n## 4.2 Evaluation Metrics\n\n- **Pearson correlation (r):**\
  \ Linear correlation between predictions and human judgments/true grade levels.\n- **Bootstrap 95% confidence interval:**\
  \ 2000 bootstrap samples for reliable CI estimation with small samples.\n- **Williams test:** Statistical test for comparing\
  \ two dependent correlations (SCD vs. FK on same data).\n- **Partial correlation:** Correlation between SCD and true grades,\
  \ controlling for FK predictions (quantifies unique signal).\n- **Classification accuracy:** For OneStopEnglish 3-class\
  \ classification using scikit-learn DecisionTreeClassifier.\n\n## 4.3 Results\n\n### 4.3.1 CLEAR Corpus (Human Judgments)\n\
  \nTable 1 reports Pearson correlations with human readability judgments (n=1000).\n\n| Method | Pearson r | p-value | 95%\
  \ CI |\n|--------|-----------|---------|--------|\n| SCD (TF-IDF) | 0.1202 | 0.0001 | [0.083, 0.157] |\n| Flesch-Kincaid\
  \ | -0.4958 | <0.0001 | [-0.539, -0.451] |\n\n**Key findings:**\n\n1. **SCD achieves statistically significant but weak\
  \ correlation** with human judgments (r=0.1202, p=0.0001). The positive sign indicates that higher SCD (less coherent) corresponds\
  \ to higher (more difficult) human judgments.\n\n2. **Flesch-Kincaid achieves stronger correlation** (r=-0.4958, p<0.0001).\
  \ The negative sign is expected: higher FKGL indicates more difficult texts, while lower human judgments indicate easier\
  \ texts.\n\n3. **SCD alone is not competitive with FK** on the CLEAR corpus. This suggests that surface features (sentence\
  \ length, word difficulty) remain the dominant signal for predicting human readability judgments.\n\n[FIGURE:fig3]\n\n###\
  \ 4.3.2 OneStopEnglish (Classification)\n\nUsing SCD and Flesch-Kincaid as features in a DecisionTreeClassifier with 5-fold\
  \ cross-validation:\n\n| Method | Accuracy (mean ± std) |\n|--------|----------------------|\n| SCD only | 0.484 ± 0.062\
  \ |\n| FK only | 0.656 ± 0.058 |\n| SCD + FK (ensemble) | **0.712 ± 0.055** |\n\n**Key findings:**\n\n1. **FK alone achieves\
  \ 65.6% accuracy**, outperforming SCD alone (48.4%).\n2. **The ensemble of SCD + FK achieves 71.2% accuracy**, demonstrating\
  \ that SCD provides complementary information to FK.\n3. The improvement from ensemble (71.2% vs. 65.6%) suggests that semantic\
  \ coherence captures aspects of readability not reflected in surface statistics.\n\n### 4.3.3 Synthetic Dataset (Controlled\
  \ Evaluation)\n\nTable 3 reports results on the synthetic dataset (n=60) with true grade levels \\footnote{Code: \\url{https://github.com/AMGrobelnik/ai-invention-210829-evaluating-embedding-based-semantic-cohe/tree/main/round-2/evaluation-1}}.\n\
  \n| Method | Pearson r | 95% CI | p-value |\n|--------|-----------|--------|---------|\n| SCD | 0.5442 | [0.3603, 0.7135]\
  \ | <0.001 |\n| Flesch-Kincaid | 0.6492 | [0.4882, 0.7764] | <0.001 |\n| Ensemble (SCD + FK) | **0.6777** | [0.5231, 0.7942]\
  \ | <0.001 |\n\n**Statistical tests:**\n\n1. **Williams test:** Comparing SCD (r=0.5442) vs. FK (r=0.6492): z = -1.30, p\
  \ = 0.19. The difference is **not statistically significant**.\n\n2. **Partial correlation:** SCD vs. true grades, controlling\
  \ for FK: r = 0.294, p = 0.022. This indicates that **SCD provides unique signal beyond FK** (p < 0.05).\n\n3. **Complementarity:**\
  \ Correlation between SCD and FK predictions: r = 0.5505. This moderate correlation suggests the two metrics capture related\
  \ but not identical information.\n\n4. **Ensemble improvement:** The ensemble achieves r = 0.6777, outperforming both SCD\
  \ alone (0.5442) and FK alone (0.6492).\n\n[FIGURE:fig4]\n\n\n\n### 4.3.4 Computational Efficiency\n\nSCD processes documents\
  \ in **0.022 milliseconds** on average (measured over 60 examples). Flesch-Kincaid processes documents in **0.004 milliseconds**.\
  \ Both meet the <1 second requirement for real-time applications.\n\nThe computational efficiency of TF-IDF-based SCD makes\
  \ it suitable for applications requiring real-time readability assessment, such as content recommendation systems or assistive\
  \ reading technologies.\n\n---\n\n# 5 Discussion\n\n## 5.1 Honest Assessment of SCD\n\nThe research literature clearly shows\
  \ that measuring semantic coherence via sentence embedding distances is **not novel**. Coh-Metrix (2004) uses LSA for coherence\
  \ [5], TextDescriptives (2023) implements first-order coherence [7], and Word Mover's Distance has been applied to readability\
  \ (2021) [6].\n\nOur empirical evaluation confirms that SCD alone is not competitive with traditional formulas:\n- On CLEAR:\
  \ SCD r=0.1202 vs. FK r=-0.4958\n- On OneStopEnglish: SCD accuracy 48.4% vs. FK accuracy 65.6%\n\nHowever, our results also\
  \ show that **SCD provides complementary information** to traditional formulas:\n- Partial correlation (SCD|FK) = 0.294,\
  \ p = 0.022 (unique signal)\n- Ensemble (SCD + FK) achieves best performance on both datasets\n\n## 5.2 When Does Semantic\
  \ Coherence Matter?\n\nSCD is designed to detect texts that are semantically incoherent despite using simple words. Consider\
  \ this example:\n\n> \"Dogs bark loudly at mailboxes. The quantum vacuum fluctuates constantly. Yesterday's sandwich contained\
  \ pickles. Economic indicators suggest inflationary pressure.\"\n\nThis text uses simple words and short sentences (FKGL\
  \ would predict \"easy\"), but its semantic trajectory is extremely erratic (SCD would predict \"difficult\"). Human readers\
  \ would find this text confusing not because of vocabulary, but because of topic whiplash.\n\nOur results suggest that such\
  \ cases exist but are not the dominant pattern in standard readability datasets. Most texts that are difficult (high FKGL)\
  \ are also semantically coherent (low SCD), and vice versa. The moderate correlation between SCD and FK (r=0.5505) on synthetic\
  \ data supports this.\n\n## 5.3 Limitations\n\n1. **TF-IDF embeddings:** Due to computational constraints, we used TF-IDF\
  \ rather than SBERT embeddings. SBERT would provide more semantically meaningful embeddings, potentially improving SCD correlation\
  \ with human judgments. This is a significant limitation that future work should address.\n\n2. **CLEAR corpus results:**\
  \ The weak correlation on CLEAR (r=0.1202) may reflect limitations of TF-IDF embeddings, or it may indicate that semantic\
  \ coherence is less important than surface features for the specific texts in CLEAR. We cannot distinguish these explanations\
  \ without SBERT-based evaluation.\n\n3. **Small-scale synthetic evaluation:** The synthetic dataset (n=60) is small, though\
  \ bootstrap CIs provide reliable uncertainty estimates. The controlled nature of the dataset allows analysis of complementarity\
  \ but does not reflect real-world text diversity.\n\n4. **Embedding sensitivity:** SCD's performance depends entirely on\
  \ the quality of sentence embeddings. Different embedding strategies (TF-IDF, SBERT, GPT embeddings) would produce different\
  \ SCD values and potentially different correlations.\n\n5. **Novelty:** As established in Section 2.3, SCD is not novel.\
  \ This paper's contribution is empirical evaluation, not methodological innovation.\n\n## 5.4 Future Work\n\n1. **SBERT-based\
  \ evaluation:** Replace TF-IDF with SBERT embeddings (`all-MiniLM-L6-v2` or `all-mpnet-base-v2`) to evaluate whether more\
  \ semantically rich embeddings improve SCD correlation with human judgments.\n\n2. **Evaluation on additional datasets:**\
  \ Evaluate SCD on WeeBit, WikiLarge, and Newsela datasets to test generalizability across text types.\n\n3. **Genre-specific\
  \ analysis:** Investigate whether SCD is more informative for certain genres (e.g., narrative texts with topic shifts) than\
  \ others (e.g., academic texts with stable topics).\n\n4. **Hybrid models:** Train machine learning models that combine\
  \ SCD with traditional formulas and other linguistic features, rather than using the simple ensemble in this paper.\n\n\
  5. **Optimal transport extension:** Replace cosine distance with Wasserstein distance (Word Mover's Distance) to account\
  \ for the geometry of word embedding space, as in Imperial et al. (2021) [6].\n\n---\n\n# 6 Conclusion\n\nWe evaluated Semantic\
  \ Coherence Distance (SCD)—the average cosine distance between consecutive sentence embeddings—for readability assessment\
  \ on three datasets: CLEAR corpus (human judgments), OneStopEnglish (classification), and a synthetic dataset (controlled\
  \ difficulty levels).\n\nOur key findings are:\n\n1. **SCD alone is not competitive with traditional formulas.** On CLEAR,\
  \ SCD achieves r=0.1202 vs. FK r=-0.4958. On OneStopEnglish, SCD achieves 48.4% vs. FK 65.6% accuracy.\n\n2. **SCD provides\
  \ complementary information to traditional formulas.** Partial correlation (SCD|FK) = 0.294 (p=0.022). Ensemble of SCD+FK\
  \ achieves best performance on both datasets (71.2% accuracy on OneStopEnglish, r=0.6777 on synthetic data).\n\n3. **SCD\
  \ is computationally efficient** (0.022 ms per document), suitable for real-time applications.\n\n4. **SCD is not novel.**\
  \ Measuring semantic coherence via embedding distances was established by Coh-Metrix (2004), TextDescriptives (2023), and\
  \ others.\n\nThe broader contribution of this work is an **honest empirical evaluation** that quantifies the added value\
  \ of semantic coherence metrics for readability assessment. We show that while SCD alone is not competitive with traditional\
  \ formulas, it captures complementary information that improves ensemble performance. Future work should evaluate SCD with\
  \ SBERT embeddings and on additional datasets to better understand when and how semantic coherence matters for readability.\n\
  \n---\n\n# Acknowledgments\n\nWe thank the AI Inventor system for facilitating this research. We also thank the creators\
  \ of the CLEAR corpus, OneStopEnglish corpus, and WikiLarge dataset for making their data publicly available.\n\n---\n\n\
  # References\n\n[1] Crossley, S., Burling, A. B., & O'Reilly, T. (2021). The CommonLit Ease of Readability (CLEAR) Corpus.\
  \ *Proceedings of the 14th International Conference on Educational Data Mining*, 381-386.\n\n[2] Coleman, M., & Liau, T.\
  \ L. (1975). A computer readability formula designed for machine scoring. *Journal of Applied Psychology*, 60(2), 283-284.\n\
  \n[3] Flesch, R. (1948). A new readability yardstick. *Journal of Applied Psychology*, 32(3), 221-233.\n\n[4] Graesser,\
  \ A. C., McNamara, D. S., & Kulikowich, J. M. (2011). Coh-Metrix: Providing multilevel analyses of text characteristics.\
  \ *Educational Researcher*, 40(5), 223-234.\n\n[5] Hlasse. (2023). TextDescriptives: A Python package for calculating text\
  \ descriptives. *Behavior Research Methods*.\n\n[6] Imperial, J. M., & Ong, E. (2021). A Simple Post-Processing Technique\
  \ for Improving Readability Assessment of Texts using Word Mover's Distance. *arXiv preprint arXiv:2103.07277*.\n\n[7] Imperial,\
  \ J. M. (2021). BERT Embeddings for Automatic Readability Assessment. *Recent Advances in Natural Language Processing*,\
  \ 611-618.\n\n[8] Kincaid, J. P., Fishburne, R. P., Rogers, R. L., & Chissom, B. S. (1975). Derivation of new readability\
  \ formulas for Navy enlisted personnel. *Naval Technical Training Command Millington TN Research Branch*.\n\n[9] Lee, B.\
  \ W., Jang, Y., & Lee, J. (2021). Pushing on text readability assessment: A transformer meets handcrafted linguistic features.\
  \ *Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing*, 8385-8397.\n\n[10] McLaughlin,\
  \ G. H. (1969). SMOG grading: A new readability formula. *Journal of Reading*, 12(8), 639-646.\n\n[11] Vajjala, S., & Lucic,\
  \ I. (2018). OneStopEnglish corpus: A new corpus for automatic readability assessment and text simplification. *Proceedings\
  \ of the 13th Workshop on Innovative Use of NLP for Building Educational Applications*, 297-304.\n\n[12] Reimers, N., &\
  \ Gurevych, I. (2019). Sentence-BERT: Sentence embeddings using siamese BERT-networks. *Proceedings of the 2019 Conference\
  \ on Empirical Methods in Natural Language Processing*, 3982-3992.\n\n---\n\n## BibTeX References (for reference.bib)\n\n\
  ```bibtex\n@article{Crossley2021,\n  author = {Crossley, Scott and Burling, A. B. and O'Reilly, Tenaha},\n  title = {The\
  \ CommonLit Ease of Readability (CLEAR) Corpus},\n  journal = {Proceedings of the 14th International Conference on Educational\
  \ Data Mining},\n  pages = {381--386},\n  year = {2021}\n}\n\n@article{Coleman1975,\n  author = {Coleman, M. and Liau, T.\
  \ L.},\n  title = {A computer readability formula designed for machine scoring},\n  journal = {Journal of Applied Psychology},\n\
  \  volume = {60},\n  number = {2},\n  pages = {283--284},\n  year = {1975}\n}\n\n@article{Flesch1948,\n  author = {Flesch,\
  \ Rudolf},\n  title = {A new readability yardstick},\n  journal = {Journal of Applied Psychology},\n  volume = {32},\n \
  \ number = {3},\n  pages = {221--233},\n  year = {1948}\n}\n\n@article{Graesser2011,\n  author = {Graesser, Arthur C. and\
  \ McNamara, Danielle S. and Kulikowich, Jonna M.},\n  title = {Coh-Metrix: Providing multilevel analyses of text characteristics},\n\
  \  journal = {Educational Researcher},\n  volume = {40},\n  number = {5},\n  pages = {223--234},\n  year = {2011}\n}\n\n\
  @article{Imperial2021WMD,\n  author = {Imperial, Joseph Marvin and Ong, Ethel},\n  title = {A Simple Post-Processing Technique\
  \ for Improving Readability Assessment of Texts using Word Mover's Distance},\n  journal = {arXiv preprint arXiv:2103.07277},\n\
  \  year = {2021}\n}\n\n@inproceedings{Imperial2021BERT,\n  author = {Imperial, Joseph Marvin},\n  title = {BERT Embeddings\
  \ for Automatic Readability Assessment},\n  booktitle = {Recent Advances in Natural Language Processing},\n  pages = {611--618},\n\
  \  year = {2021}\n}\n\n@inproceedings{Lee2021,\n  author = {Lee, Bruce W. and Jang, Yoo Sung and Lee, Jason},\n  title =\
  \ {Pushing on text readability assessment: A transformer meets handcrafted linguistic features},\n  booktitle = {Proceedings\
  \ of the 2021 Conference on Empirical Methods in Natural Language Processing},\n  pages = {8385--8397},\n  year = {2021}\n\
  }\n\n@article{McLaughlin1969,\n  author = {McLaughlin, G. Harry},\n  title = {SMOG grading: A new readability formula},\n\
  \  journal = {Journal of Reading},\n  volume = {12},\n  number = {8},\n  pages = {639--646},\n  year = {1969}\n}\n\n@inproceedings{Vajjala2018,\n\
  \  author = {Vajjala, Sowmya and Lucic, Ivana},\n  title = {OneStopEnglish corpus: A new corpus for automatic readability\
  \ assessment and text simplification},\n  booktitle = {Proceedings of the 13th Workshop on Innovative Use of NLP for Building\
  \ Educational Applications},\n  pages = {297--304},\n  year = {2018}\n}\n\n@inproceedings{Reimers2019,\n  author = {Reimers,\
  \ Nils and Gurevych, Iryna},\n  title = {Sentence-BERT: Sentence embeddings using siamese BERT-networks},\n  booktitle =\
  \ {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},\n  pages = {3982--3992},\n \
  \ year = {2019}\n}\n```"
summary: >-
  This paper evaluates Semantic Coherence Distance (SCD) for readability assessment on three datasets (CLEAR, OneStopEnglish,
  synthetic). SCD uses TF-IDF embeddings to compute average cosine distance between consecutive sentences. Results show SCD
  alone is not competitive with Flesch-Kincaid (CLEAR: r=0.1202 vs r=-0.4958), but provides complementary signal (partial
  r=0.294, p=0.022) and improves ensemble performance (71.2% accuracy on OneStopEnglish, r=0.6777 on synthetic). The paper
  honestly acknowledges SCD is not novel - it is an established technique - and focuses on empirical evaluation.
</paper_text>

<available_figures>
--- Item 1 ---
id: fig1
title: Semantic Coherence Distance Concept
caption: >-
  Illustration of Semantic Coherence Distance (SCD) computed as the average cosine distance between consecutive sentence embeddings
  in a text. Smooth semantic progression (top) results in low SCD, while abrupt topic changes (bottom) result in high SCD.
image_gen_detailed_description: >-
  Two-panel conceptual diagram. Top panel: Three sentences with similar meaning connected by short arrows labeled with small
  cosine distances (0.15, 0.12). Label: 'Smooth semantic flow, Low SCD'. Bottom panel: Three sentences with unrelated meanings
  connected by long arrows labeled with large cosine distances (0.78, 0.82). Label: 'Erratic topic changes, High SCD'. Sentences
  shown as text boxes. Arrows between boxes. Clean white background, sans-serif font.
aspect_ratio: '21:9'
summary: Conceptual diagram showing how SCD measures semantic flow between sentences
figure_path: figures/fig1_v0.jpg

--- Item 2 ---
id: fig2
title: SCD Computation Steps
caption: >-
  Computational steps for Semantic Coherence Distance: (1) Tokenize text into sentences, (2) Convert each sentence to TF-IDF
  embedding vector, (3) Compute cosine distance between consecutive embeddings, (4) Average all distances to get SCD score.
image_gen_detailed_description: >-
  Horizontal flowchart with 4 boxes connected by arrows. Box 1: 'Input Text' with sample text. Arrow to Box 2: 'Sentence Tokenization'
  with 3 sentence boxes. Arrow to Box 3: 'TF-IDF Embeddings' with 3 vector representations [0.2, 0.5, ...]. Arrow to Box 4:
  'Average Cosine Distance = SCD' with formula SCD = mean(d1, d2). Clean white background, sans-serif font.
aspect_ratio: '21:9'
summary: Flowchart showing SCD computation pipeline
figure_path: figures/fig2_v0.jpg

--- Item 3 ---
id: fig3
title: SCD vs Flesch-Kincaid on CLEAR Corpus
caption: >-
  Scatter plots showing correlation between readability metrics and human judgments on the CLEAR corpus (n=1000). Left: SCD
  shows weak positive correlation (r=0.1202, p=0.0001). Right: Flesch-Kincaid shows stronger negative correlation (r=-0.4958,
  p<0.0001). Each point represents one text excerpt.
image_gen_detailed_description: >-
  Two-panel scatter plot. Left panel: X-axis 'SCD', Y-axis 'Human readability judgment', points scattered with r=0.1202 in
  title. Right panel: X-axis 'Flesch-Kincaid', Y-axis 'Human readability judgment', points scattered with r=-0.4958 in title.
  Both plots have 1000 points in light blue, trend line in red. X-range 0-1 for SCD, 0-20 for FK. Y-range 0-1 for human judgments.
  Sans-serif font, white background.
aspect_ratio: '21:9'
summary: Scatter plots comparing SCD and FK correlation with human judgments on CLEAR
figure_path: figures/fig3_v0.jpg

--- Item 4 ---
id: fig4
title: Ensemble Improvement on Synthetic Data
caption: >-
  Bar chart comparing Pearson correlation with true grade levels on synthetic dataset (n=60). SCD alone: r=0.5442 [95% CI:
  0.3603, 0.7135]. Flesch-Kincaid alone: r=0.6492 [95% CI: 0.4882, 0.7764]. Ensemble (SCD+FK): r=0.6777 [95% CI: 0.5231, 0.7942].
  Error bars show 95% bootstrap confidence intervals. Williams test: p=0.19 (difference not significant).
image_gen_detailed_description: >-
  Grouped bar chart. X-axis: Method (SCD, Flesch-Kincaid, Ensemble). Y-axis: Pearson correlation r (0.0 to 0.8). Bars: SCD=0.5442
  (blue), FK=0.6492 (orange), Ensemble=0.6777 (green). Error bars: SCD [0.3603, 0.7135], FK [0.4882, 0.7764], Ensemble [0.5231,
  0.7942]. Bar width=0.6. Sans-serif font, white background.
aspect_ratio: '21:9'
summary: Bar chart showing ensemble improvement over individual metrics on synthetic data
figure_path: figures/fig4_v0.jpg
</available_figures>

<figure_requirements>
CRITICAL: Include ALL figures from <available_figures>. No exceptions.

- Every figure MUST use \includegraphics{figures/filename.jpg}
- Do NOT skip, convert to tables, or describe without inserting
- Each needs: \begin{figure*|figure}[placement], \includegraphics, \caption, \label, \end{...} — pick env + placement by the figure's `aspect_ratio` field (see PLACEMENT below). Constrain every \includegraphics with `width=\linewidth,height=0.4\textheight,keepaspectratio` (single-column) or `width=\textwidth,height=0.45\textheight,keepaspectratio` (figure*). Use exactly these option keys — `max height=` is NOT valid LaTeX
- Use the `caption` field from each figure for \caption{...} — do NOT invent new captions
- Place figures where their [FIGURE:fig_id] markers appear in paper_text
- VERIFICATION: paper.tex MUST have exact same number of \includegraphics as <available_figures>
- Do NOT generate new figure images (no matplotlib, no PIL, no image generation). Use ONLY the pre-generated figures from <available_figures>. They were already created by a previous pipeline step.

PLACEMENT BY ASPECT RATIO (use the `aspect_ratio` field on each figure):
- `21:9` (architecture diagrams / hero figures): \begin{figure*}[!t] (full two-column width, top of page). The hero architecture diagram should appear EARLY in the paper — typically at the top of page 2. Marker placement in paper_text already determines this; preserve it.
- `16:9` (comparisons, multi-panel results): \begin{figure*}[!t] for full-width or \begin{figure}[!htbp] for single-column.
- `4:3` / `1:1` / `3:2` / `3:4` / `9:16`: \begin{figure}[!htbp] (single-column).
</figure_requirements>

<artifact_links>
The paper_text contains \footnote{Code: \url{...}} references linking to artifact source code
on GitHub. Include \usepackage{hyperref} and \usepackage{url}.
Preserve these exactly as-is — do not remove, rewrite, or convert them to plain text.
The URLs will not resolve yet (the repo is deployed after compilation) — do NOT try to verify or fix them.
</artifact_links>

<headings>
NEVER use inline math (``$...$``) inside ``\section{...}`` / ``\subsection{...}`` / ``\subsubsection{...}`` arguments — hyperref's bookmark builder errors out (``Token not allowed in a PDF string``) and the PDF outline breaks. If a section heading needs a math-looking term, use the text equivalent (``d star`` not ``$d^*$``, ``alpha-equivalent`` not ``$\alpha$-equivalent``) or wrap it in ``\texorpdfstring{$math$}{plain}``. Inline math inside body paragraphs is fine.
</headings>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-paper-to-latex, aii-semscholar-bib.
TODO 2. Review <paper_text> and <available_figures>. Copy all figure images into ./figures/ in your workspace. Count figures — MUST include every one. Plan placements per section. Build `./references.bib` via aii_semscholar_bib__fetch — collect DOIs/ArXiv IDs from <paper_text> and batch-fetch all BibTeX in one call. Do NOT fabricate entries.
TODO 3. Create `./paper.tex` per aii-paper-to-latex skill's setup, write ALL sections, insert ALL figures from <available_figures>, include `./references.bib` via \bibliography. Compile to PDF per skill's process. Fix errors.
TODO 4. CRITICAL VERIFICATION: Run `grep -c 'includegraphics' paper.tex`, confirm count equals figures in <available_figures>. If not, add missing figures. Verify `./paper.pdf` was created.
TODO 5. VISUAL REVIEW: Write Python script to convert EVERY page of paper.pdf to PNG at 150 DPI (use pdf2image or pymupdf). Then read ALL page screenshots — each page image costs ~1,600 tokens so a 15-page paper is only ~24K tokens. You MUST read every page. The ONLY exception is if all page images would not fit in your remaining context — in that case, read as many as fit and state which pages you are skipping and why. Check every page for layout issues, overlapping figures, cut-off text, bad spacing, formatting problems. Fix issues and recompile.
TODO 6. FINAL READ: Check page count (`pdfinfo paper.pdf` or pymupdf). Read entire paper.pdf — check for missing sections, unclear explanations, inconsistencies, typos. Fix and recompile. The ONLY exception is if all pages would not fit in your remaining context — in that case, read as many pages as fit and state which pages you are skipping and why.
</todos>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_6uOr5GlpaMfR/4_gen_paper_repo/_4_assemble_paper/paper/workspace/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "FullPaperExpectedFiles": {
      "description": "All expected output files from full paper generation.",
      "properties": {
        "paper_tex_path": {
          "description": "Path to LaTeX source file. Example: 'paper.tex'",
          "title": "Paper Tex Path",
          "type": "string"
        },
        "paper_pdf_path": {
          "description": "Path to compiled PDF. Example: 'paper.pdf'",
          "title": "Paper Pdf Path",
          "type": "string"
        },
        "references_bib_path": {
          "description": "Path to BibTeX bibliography file. Example: 'references.bib'",
          "title": "References Bib Path",
          "type": "string"
        },
        "figure_paths": {
          "description": "Paths to all figure image files. Example: ['figures/fig1_v0.jpg', 'figures/fig2_v0.jpg']",
          "items": {
            "type": "string"
          },
          "title": "Figure Paths",
          "type": "array"
        }
      },
      "required": [
        "paper_tex_path",
        "paper_pdf_path",
        "references_bib_path",
        "figure_paths"
      ],
      "title": "FullPaperExpectedFiles",
      "type": "object"
    }
  },
  "description": "Full paper \u2014 structured output from paper generation.",
  "properties": {
    "title": {
      "description": "Paper title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance. Aim for about 4-8 words (~40 characters).",
      "maxLength": 90,
      "minLength": 12,
      "title": "Title",
      "type": "string"
    },
    "summary": {
      "description": "Brief summary of the generated paper: sections written, figures included, compilation status",
      "maxLength": 5000,
      "minLength": 500,
      "title": "Summary",
      "type": "string"
    },
    "out_expected_files": {
      "$ref": "#/$defs/FullPaperExpectedFiles",
      "description": "All output files you created. Must include paper.tex, paper.pdf, references.bib, and paths to all figure files."
    }
  },
  "required": [
    "title",
    "summary",
    "out_expected_files"
  ],
  "title": "FullPaper",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `/ai-inventor/aii_data/runs/run_6uOr5GlpaMfR/4_gen_paper_repo/_4_assemble_paper/paper/workspace/.sdk_openhands_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-07-09 03:33:01 UTC

```
Propose a simple, novel machine-learning method for scoring text readability and validate it.
```

### [3] SKILL-INPUT — aii-paper-to-latex · 2026-07-09 03:33:18 UTC

The agent loaded the **aii-paper-to-latex** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-paper-to-latex
description: LaTeX paper assembly and compilation. Covers document setup, figure inclusion from pre-generated JPEGs, compilation process, and output files. Use when assembling a paper from pre-written text and pre-generated figures into a compiled PDF.
---

## LaTeX Paper Assembly

Assembles a research paper from paper text, pre-generated figure JPEGs, and bibliography into a compiled PDF.

### Document Setup

```latex
\documentclass[11pt,letterpaper]{article}
\usepackage{graphicx, geometry, amsmath, hyperref, natbib, booktabs, xcolor, listings}
\geometry{margin=1in}
\hypersetup{colorlinks=true, linkcolor=black, citecolor=black, urlcolor=black}
```

### Figure Inclusion

CRITICAL: Include ALL figures. Every figure MUST appear in the paper.

```latex
\begin{figure}[!htbp]
  \centering
  \includegraphics[width=0.92\textwidth,keepaspectratio]{figures/filename.jpg}
  \caption{Descriptive caption.}
  \label{fig:label}
\end{figure}
```

Rules:
- ALWAYS use `[!htbp]` float placement (NOT `[t]` or `[h]` alone)
- ALWAYS constrain with `width` and `keepaspectratio` to prevent page takeover
- Every figure needs `\caption`, `\label`, and a `\ref` in the text
- Do NOT convert figures to tables or describe them without inserting the image
- Do NOT skip any figures

### Compilation Process

Run each command separately (do NOT chain with `&&` — pdflatex often exits non-zero on warnings, which would skip bibtex and leave citations as `??`):

```bash
pdflatex -interaction=nonstopmode paper.tex
bibtex paper
pdflatex -interaction=nonstopmode paper.tex
pdflatex -interaction=nonstopmode paper.tex
```

All four commands are required. Skipping bibtex causes `??` in all citations.
Fix any errors between runs. Verify `./paper.pdf` was created.

### Output Files

- `./paper.tex` — LaTeX source
- `./references.bib` — bibliography file
- `./paper.pdf` — compiled PDF
- `./figures/*.jpg` — all figure images (pre-generated, copied into workspace)
````

### [4] SKILL-INPUT — aii-semscholar-bib · 2026-07-09 03:33:18 UTC

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

### [5] SYSTEM-USER prompt · 2026-07-09 03:41:13 UTC

```
<validation-feedback>
Attempt 1 failed validation.

Schema validation found 1 problem — fix ALL of them at once:
  - at `title`: 'Evaluating Embedding-Based Semantic Coherence for Readability Assessment: An Empirical Study' is too long (at most 90 characters, got 92)
Every required field must be present and every field type must match the schema.

Please use the Write tool to overwrite `.sdk_openhands_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```
