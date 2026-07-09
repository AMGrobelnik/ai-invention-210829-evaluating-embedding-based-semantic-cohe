# Dataset Preparation Summary

## Selected Datasets

After evaluating 12+ candidate datasets from HuggingFace Hub, I selected the **3 best datasets** for evaluating the Semantic Control Energy (SCE) readability method:

### 1. CLEAR Corpus (CommonLit Ease of Readability)
- **Size**: 4,724 examples (train: 3,306, val: 709, test: 709)
- **Quality**: ⭐⭐⭐⭐⭐ Highest quality
- **Readability Labels**: Human judgments (BT_easiness), traditional formulas (Flesch, Flesch-Kincaid, ARI, SMOG)
- **Provenance**: ✅ Verified - EDM 2021 paper, 135+ HF downloads
- **Use Case**: Primary evaluation dataset with human-validated readability scores

### 2. OneStopEnglish Corpus
- **Size**: 567 examples (train: 396, val: 85, test: 86)
- **Quality**: ⭐⭐⭐⭐ Good quality
- **Readability Labels**: 3 difficulty levels (Elementary=1, Intermediate=3, Advanced=5)
- **Provenance**: ✅ Verified - ACL 2018 paper, 81+ HF downloads
- **Use Case**: Classification benchmark with clear difficulty categorization

### 3. WikiLarge
- **Size**: 299,062 examples (train: 209,343, val: 44,859, test: 44,860)
- **Quality**: ⭐⭐⭐ Large-scale, simplification pairs
- **Readability Labels**: Complexity inferred from Wikipedia vs. Simple Wikipedia
- **Provenance**: ✅ Verified - Standard text simplification benchmark, 236+ HF downloads
- **Use Case**: Large-scale evaluation, training data for simplification models

## Dataset Statistics

| Metric | CLEAR | OneStopEnglish | WikiLarge | Total |
|--------|-------|-----------------|-----------|-------|
| Train Examples | 3,306 | 396 | 209,343 | 213,045 |
| Val Examples | 709 | 85 | 44,859 | 45,653 |
| Test Examples | 709 | 86 | 44,860 | 45,655 |
| Total | 4,724 | 567 | 299,062 | 304,353 |
| Avg Text Length | ~200 words | ~150 words | ~20 words | - |
| Has Human Labels | ✅ | ✅ | ❌ | - |
| Has Difficulty Levels | ✅ | ✅ | ✅ | - |
| Has Traditional Formulas | ✅ | ❌ | ❌ | - |

## Data Schema

All datasets standardized to `exp_sel_data_out.json` schema:

```json
{
  "metadata": {
    "description": "Readability datasets for SCE evaluation",
    "total_examples": 304353,
    "sources": ["clear_corpus", "onestop_english", "wikilarge"]
  },
  "datasets": [
    {
      "dataset": "clear_corpus",
      "examples": [
        {
          "input": "text content...",
          "output": "-0.556",  // readability score
          "metadata_source": "CLEAR",
          "metadata_difficulty": 3,
          "metadata_grade_level": "10",
          "metadata_flesch_reading_ease": "71.33",
          ...
        },
        ...
      ]
    },
    ...
  ]
}
```

## Files Generated

### Main Deliverables
- `full_data_out.json` - 213,045 training examples in exp_sel_data_out schema
- `mini_full_data_out.json` - 9 examples (3 per dataset) for quick testing
- `preview_full_data_out.json` - 9 examples with truncated text for inspection

### Standardized Datasets (temp/datasets/standardized/)
- `clear_corpus/splits/` - Train/val/test splits (4.7K examples)
- `onestop_english/splits/` - Train/val/test splits (567 examples)
- `wikilarge/splits/` - Train/val/test splits (299K examples)
- `*_mini.json` - 10-example mini datasets
- `*_preview.json` - 3-example preview datasets

### Documentation
- `README.md` - Full dataset documentation with usage examples
- `temp/datasets/dataset_summary_final.json` - Dataset summary statistics

## Validation Results

✅ **Schema Validation**: `full_data_out.json` validated against `exp_sel_data_out.json` schema - PASSED
✅ **Data Quality**: No empty texts, all required fields present
✅ **Provenance**: All datasets verified with papers and citations
✅ **Size**: Total 304K examples, ~158MB (under 300MB limit)
✅ **Splits**: 70/15/15 train/val/test, stratified by difficulty where applicable

## Why These 3 Datasets?

### Meets All Ideal Criteria:
1. ✅ **Human readability judgments** - CLEAR has BT_easiness scores
2. ✅ **Diverse text types** - Literature (CLEAR), news (OneStopEnglish), Wikipedia (WikiLarge)
3. ✅ **Known benchmarks** - All 3 published in peer-reviewed papers
4. ✅ **Accessible** - Downloaded from HuggingFace Hub
5. ✅ **Manageable size** - 304K examples, ~158MB total
6. ✅ **Text + labels** - Standardized to input/output schema
7. ✅ **Metadata** - Source, genre, author, readability formulas, etc.

### Enables SCE Evaluation:
- **Traditional formulas** - CLEAR has Flesch, Flesch-Kincaid, ARI, SMOG for baseline comparison
- **Difficulty levels** - OneStopEnglish provides ordinal difficulty (1-5 scale)
- **Large-scale testing** - WikiLarge enables evaluation on diverse texts
- **Human validation** - CLEAR scores are human-validated for ground truth

## Next Steps

These datasets are ready for:
1. **Baseline evaluation** - Traditional readability formulas
2. **SCE method evaluation** - Novel Semantic Control Energy method
3. **Model training** - Train readability assessment models
4. **Benchmarking** - Compare against published results

---

**Date**: 2026-07-08
**Status**: ✅ Complete - All datasets prepared, validated, and documented
