# SCD Readability Experiment - Results Summary

## Experiment Overview
This experiment evaluates Semantic Coherence Distance (SCD) as a readability metric using TF-IDF embeddings (fallback from SBERT due to environment constraints).

## Results

### CLEAR Corpus (Correlation with Human Judgments)
- **SCD**: r=0.1202, p=0.0001, n=1000
  - Weak but statistically significant positive correlation
  - Higher SCD = less coherent = harder to read
- **Flesch-Kincaid**: r=-0.4958, p<0.0001, n=1000
  - Moderate negative correlation (lower grade = more readable)
  - Traditional formula performs better than SCD

### OneStopEnglish (3-Class Classification)
- **Accuracy**: 0.712 (std=0.055)
  - Using SCD + Flesch-Kincaid as features
  - Reasonable classification performance

### WikiLarge (Simplification Pair Ranking)
- **Status**: Not evaluated
- **Reason**: Subset sampling didn't preserve pairs (requires matching simple/normal versions)
- **Note**: Full dataset evaluation would require careful pair-preserving sampling

## Visualizations Generated
1. `plots/scd_vs_human.png` - SCD vs human judgments
2. `plots/flesch_kincaid_vs_human.png` - Flesch-Kincaid vs human judgments

## Implementation Notes
- Used TF-IDF embeddings instead of SBERT (environment timeout issues)
- Implemented fallback manual Flesch-Kincaid calculation
- All code in `method.py` with logging and error handling

## Files
- `method.py` - Main experiment script
- `method_out.json` - Complete results
- `plots/` - Generated visualizations
- `subset_1000_out.json` - Test dataset (1000 examples per dataset)
