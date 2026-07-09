# Evaluation Results Summary: SCD Readability Metric

## Key Findings

### 1. Correlation with True Grade Levels
- **SCD vs True**: Pearson r = 0.5442 [95% CI: 0.3603, 0.7135], p < 0.001
- **FK vs True**: Pearson r = 0.6492 [95% CI: 0.4882, 0.7764], p < 0.001
- Williams test: z = -1.30, p = 0.19 (not statistically significant difference)

### 2. Error Analysis
- **SCD**: MAE = 6.74, RMSE = 8.05
- **FK**: MAE = 3.14, RMSE = 4.60
- SCD outperforms FK on only 1/60 examples (1.7%)
- Cohen's d for error difference = 0.91 (large effect - FK is more accurate)

### 3. Complementarity Analysis
- Correlation between SCD and FK predictions: r = 0.55 (moderate)
- Partial correlation (SCD vs true | FK): r = 0.29, p = 0.02 (significant - SCD adds unique information)
- Ensemble correlation (SCD+FK): r = 0.68 (improvement over either alone)

### 4. ANOVA (SCD across complexity levels)
- F = 22.62, p < 0.001 (significant differences)
- Simple: mean = 0.004, Medium: mean = 0.007, Complex: mean = 0.425

### 5. Computational Efficiency
- SCD: 0.022 ms/text (< 1 second requirement: YES)
- FK: 0.004 ms/text

### 6. Normality Tests
- SCD errors: W = 0.92, p < 0.001 (non-normal)
- FK errors: W = 0.79, p < 0.001 (non-normal)
- Non-parametric tests recommended for future analyses

## Conclusions

1. **SCD correlates with readability** (r = 0.54, p < 0.001) but not as strongly as FK (r = 0.65)
2. **SCD captures unique signal** beyond FK (partial r = 0.29, p = 0.02)
3. **SCD is computationally feasible** (< 1 ms per document)
4. **Ensemble of SCD+FK performs best** (r = 0.68)
5. **SCD differentiates complexity levels** (ANOVA p < 0.001)

## Recommendation
SCD appears to be complementary to rather than a replacement for traditional readability formulas. The two signals (semantic coherence vs surface features) provide independent information that can be combined for improved readability prediction.
