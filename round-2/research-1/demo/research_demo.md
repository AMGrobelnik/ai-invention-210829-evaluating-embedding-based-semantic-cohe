# SCD Novelty Assessment for Readability: Not Novel - Established Technique

## Summary

This research artifact provides a comprehensive assessment of whether Semantic Coherence Distance (SCD) using sentence embedding distances is novel for readability assessment. Through extensive literature review using web research tools, we investigated Coh-Metrix LSA-based coherence metrics (2004), TextDescriptives first-order coherence implementation (2023), Word Mover's Distance applications to readability (2021), semantic flow modeling (2019), and BERT embeddings for readability (2021). The findings conclusively show that SCD is NOT novel - it is a straightforward application of established techniques. Specifically: (1) Coh-Metrix has measured semantic coherence via LSA since 2004; (2) TextDescriptives implements 'first-order coherence' which is exactly cosine similarity between consecutive sentences; (3) Word Mover's Distance has already been applied to readability assessment; (4) Semantic flow in language networks has been researched; (5) BERT/SBERT embeddings have been used for readability. The research provides detailed reframing guidance for the paper, suggesting it focus on empirical evaluation on standard datasets, computational efficiency, or honest acknowledgment of applying straightforward methods. Template text for related work sections is provided.

## Research Findings

**Semantic Coherence Distance (SCD) using sentence embedding distances is NOT novel for readability assessment.** This research conclusively shows that SCD is a straightforward application of established techniques that have been in use for over 20 years [1][2][3][4][5].

## Key Findings

### 1. Coh-Metrix (2004) Already Measures Semantic Coherence

Coh-Metrix, developed by Graesser et al. (2004), analyzes texts on over 200 measures of cohesion, language, and readability [1]. Crucially, it already computes **LSA-based coherence metrics** that measure semantic similarity between text segments [1]. The tool has been widely used for readability assessment since 2004 and explicitly measures referential cohesion and semantic coherence using Latent Semantic Analysis (LSA) [1].

**Implication**: SCD proposes measuring semantic coherence via embedding distances, but Coh-Metrix has done this since 2004 using LSA. SCD is not novel in concept.

### 2. TextDescriptives Implements 'First-Order Coherence' (2023)

The TextDescriptives Python package implements a coherence component that calculates **'first-order coherence'** defined as:
> 'The cosine similarity between consecutive sentences' [2]

This is **exactly what SCD proposes** - computing cosine distances between consecutive sentence embeddings. The documentation states that TextDescriptives 'currently implements first-order and second-order coherence' using word embedding cosine similarity between sentences [2].

**Implication**: Computing cosine similarity between consecutive sentences is already implemented in standard NLP libraries (TextDescriptives). SCD is not novel.

### 3. Word Mover's Distance (WMD) Applied to Readability (2021)

Imperial et al. (2021) published 'A Simple Post-Processing Technique for Improving Readability Assessment of Texts using Word Mover's Distance' which applies **WMD as a post-processing step** for readability assessment [3]. WMD is a more sophisticated optimal transport metric that measures semantic distance between documents more accurately than simple embedding distances.

The paper states: 'In this study, we improve the conventional methodology of automatic readability assessment by incorporating the Word Mover's Distance (WMD) of ranked texts as an additional post-processing technique' [3].

**Implication**: Optimal transport metrics (WMD) have already been applied to readability assessment. SCD uses simpler cosine distances, not novel.

### 4. Semantic Flow in Language Networks (2019)

Corrêa Jr. et al. (2019) proposed a framework to characterize documents based on their **'semantic flow'** using sentence embeddings and network analysis [4]. The paper 'propose a framework to characterize documents based on their semantic flow. The proposed framework encompasses a network-based model that connected sentences based on their semantic similarity' [4].

They use Word2Vec embeddings to create sentence embeddings and model semantic transitions as a network, then extract motifs from the semantic flow patterns [4].

**Implication**: Modeling text as a semantic flow through embedding space has already been published. SCD's 'trajectory' concept is similar.

### 5. BERT Embeddings for Readability (2021)

Imperial (2021) demonstrated that **BERT embeddings capture complexity signals** that traditional surface metrics miss [5]. The paper 'BERT Embeddings for Automatic Readability Assessment... show efficacy even for low-resource languages' [5].

The research shows that sentence embeddings from transformer models encode readability-related information and can be used as features for readability classification [5].

**Implication**: Using embeddings (including SBERT) for readability assessment is established. SCD adds incremental value at best.

### 6. Bigram Semantic Distance in Psycholinguistics (2023)

Kenett et al. (2023) used **bigram semantic distance** to analyze continuous semantic flow in natural language [6]. They compute semantic distances between adjacent content words to measure conceptual cohesion and topic flow [6].

**Implication**: Computing semantic distances between adjacent units (words or sentences) for coherence assessment is established in psycholinguistics.

## Novelty Assessment: NOT NOVEL

**SCD is NOT novel** because:

1. **Coh-Metrix (2004)** already measures semantic coherence via LSA - 20 years ago [1]
2. **TextDescriptives (2023)** already implements 'first-order coherence' = cosine similarity between consecutive sentences [2]
3. **WMD (2021)** already applies optimal transport distances to readability [3]
4. **Semantic flow (2019)** already models text as trajectories through semantic space [4]
5. **BERT embeddings (2021)** already use sentence embeddings for readability [5]

**SCD = computing cosine distances between SBERT embeddings of consecutive sentences**

This is a straightforward application of established techniques. The specific combination may not have been published, but the components are all well-known.

## Reframing Guidance for Paper Contribution

Since SCD is not novel, the paper should be reframed to focus on:

### Option A: Empirical Evaluation on Standard Datasets (Recommended)
**Contribution**: First comprehensive evaluation of embedding-based coherence metrics on standard readability datasets (OneStopEnglish, Weebit, etc.)

**Template text for paper**:
> 'While measuring semantic coherence via sentence embeddings is an established technique (e.g., Coh-Metrix uses LSA-based coherence [1], and TextDescriptives implements first-order coherence via embedding similarity [2]), to our knowledge, there has been no systematic evaluation of how these metrics perform across multiple standard readability benchmarks. In this paper, we provide the first comprehensive empirical evaluation of Semantic Coherence Distance (SCD) computed via modern SBERT embeddings on [list datasets]...'

### Option B: Computational Efficiency
**Contribution**: SCD is simpler and faster than Coh-Metrix or WMD

**Template text**:
> 'Compared to Coh-Metrix which requires parsing and multiple NLP tools, or Word Mover's Distance which has O(n²) complexity, SCD can be computed in O(n) time with modern sentence transformers, making it suitable for real-time applications...'

### Option C: Specific Findings About WHEN Semantic Coherence Matters
**Contribution**: Empirical findings about which text types benefit most from coherence-based readability assessment

**Template text**:
> 'Our empirical analysis reveals that semantic coherence metrics are particularly informative for [narrative texts / informational texts / texts with high lexical diversity], whereas for [other text types], traditional surface metrics remain competitive...'

### Option D: Honest Paper (Best Option)
**Contribution**: Honest application of straightforward method with solid empirical validation

**Title**: 'Evaluating Embedding-Based Semantic Coherence for Readability Assessment: An Empirical Study'

**Template text for related work**:
> 'Measuring semantic coherence via embeddings is an established technique in readability assessment. Coh-Metrix (Graesser et al., 2004) computes LSA-based coherence metrics [1]. More recently, TextDescriptives implements first-order coherence as cosine similarity between consecutive sentences using word embeddings [2]. Word Mover's Distance has been applied as a post-processing step for readability assessment (Imperial et al., 2021) [3]. In this work, we apply straightforward SBERT embedding distances to compute Semantic Coherence Distance (SCD) and provide a comprehensive empirical evaluation on standard readability datasets...'

## Answers to Specific Questions from Artifact Direction

### Q1: Is SCD truly novel or just a straightforward application of embedding distances?
**A**: SCD is a **straightforward application** of embedding distances. Computing cosine similarity between consecutive sentence embeddings is implemented in TextDescriptives as 'first-order coherence' [2]. Coh-Metrix has measured semantic coherence since 2004 using LSA [1].

### Q2: What specific advantage does SCD have?
**A**: Potential advantages (if any) are:
- **Computational efficiency**: Faster than Coh-Metrix or WMD
- **Modern embeddings**: SBERT may capture better semantics than LSA
- **Simplicity**: Easy to implement and understand

However, these are **incremental improvements**, not novel contributions.

### Q3: Should control theory claims be removed?
**A**: **YES.** The artifact direction already indicates these claims were removed. The paper should focus on empirical evaluation, not theoretical claims about control theory.

## Confidence Level

**High confidence** (9/10) that SCD is not novel. The evidence is clear:
- Coh-Metrix (2004) uses LSA for coherence [1]
- TextDescriptives (2023) implements first-order coherence [2]  
- WMD applied to readability (2021) [3]
- Semantic flow modeling (2019) [4]

**What would change this assessment**: If SCD uses a novel combination of embeddings + trajectory smoothness + cumulative distance that hasn't been published. But based on current evidence, this is unlikely.

## Recommendations

1. **Acknowledge prior work explicitly** - Do not claim novelty for computing embedding distances
2. **Focus on empirical results** - Comprehensive evaluation on standard datasets is valuable
3. **Compare with Coh-Metrix and WMD** - Situate SCD in the landscape of coherence metrics
4. **Be honest about contributions** - 'We apply straightforward embedding distances and show empirical results' is a valid (though incremental) contribution
5. **Consider reframing as a survey/evaluation paper** rather than a method proposal

## Sources

[1] [Coh-Metrix: Analysis of text on cohesion and language (2004)](https://files.eric.ed.gov/fulltext/ED566390.pdf) — Coh-Metrix analyzes texts on over 200 measures of cohesion, language, and readability. Uses LSA-based coherence metrics to measure semantic similarity between text segments. Established tool for readability assessment since 2004.

[2] [TextDescriptives Documentation - Coherence Component (2023)](https://hlasse.github.io/TextDescriptives/coherence.html) — Implements 'first-order coherence' defined as cosine similarity between consecutive sentences using word embeddings. This is exactly what SCD proposes. Shows SCD is not novel.

[3] [A Simple Post-Processing Technique for Improving Readability Assessment of Texts using Word Mover's Distance (2021)](https://arxiv.org/abs/2103.07277) — Applies Word Mover's Distance (WMD) as a post-processing step for readability assessment. WMD is a more sophisticated optimal transport metric than simple cosine distances used in SCD.

[4] [Semantic flow in language networks (2019)](https://arxiv.org/abs/1905.07595) — Proposes a framework to characterize documents based on their semantic flow using sentence embeddings and network analysis. Models text as trajectories through semantic space, similar to SCD's concept.

[5] [BERT Embeddings for Automatic Readability Assessment (2021)](https://arxiv.org/abs/2106.07935) — Demonstrates that BERT embeddings capture complexity signals for readability assessment. Shows using sentence embeddings for readability is established.

[6] [Bigram Semantic Distance as an Index of Continuous Semantic Flow in Natural Language (2023)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10790181/) — Uses bigram semantic distance to analyze continuous semantic flow. Computing semantic distances between adjacent units for coherence assessment is established in psycholinguistics.

## Follow-up Questions

- Does SCD use cumulative distances or just pairwise distances? If cumulative, has 'cumulative semantic distance' been published for readability assessment?
- What specific SBERT model does SCD use? Does the choice of embedding model affect readability assessment results significantly?
- Has anyone compared LSA (Coh-Metrix) vs. SBERT for coherence assessment? This would be a valuable empirical contribution for the paper.

---
*Generated by AI Inventor Pipeline*
