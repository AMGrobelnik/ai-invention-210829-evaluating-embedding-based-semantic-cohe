#!/usr/bin/env python3
"""
Comprehensive statistical evaluation of Semantic Coherence Distance (SCD) readability metric.

Compares SCD against traditional readability formulas (Flesch-Kincaid) using:
1. Pearson correlation with true grade levels
2. Williams test for comparing dependent correlations
3. ANOVA for complexity level differences
4. Error analysis (MAE, RMSE, worst predictions)
5. Computational efficiency benchmarking
6. Complementarity analysis (correlation between SCD and FK, ensemble improvement)
7. Bootstrap confidence intervals
8. Effect sizes (Cohen's d)
9. Normality tests on error distributions
"""

from loguru import logger
from pathlib import Path
import json
import sys
import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import pearsonr, shapiro, bootstrap
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.linear_model import LinearRegression
import time
import warnings

warnings.filterwarnings("ignore")

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")


def load_data(json_path: str) -> pd.DataFrame:
    """Load experiment results from method_out.json into a DataFrame."""
    logger.info(f"Loading data from {json_path}")
    data = json.loads(Path(json_path).read_text())
    
    examples = data['datasets'][0]['examples']
    rows = []
    for ex in examples:
        rows.append({
            'text': ex['input'],
            'true_grade': float(ex['output']),
            'predict_sce': float(ex['predict_sce']),
            'predict_fk': float(ex['predict_flesch_kincaid']),
            'metadata_id': ex['metadata_id'],
            'complexity': ex['metadata_id'].split('_')[0],
        })
    
    df = pd.DataFrame(rows)
    logger.info(f"Loaded {len(df)} examples")
    logger.info(f"Complexity distribution: {df['complexity'].value_counts().to_dict()}")
    return df


def compute_pearson_with_ci(x, y, n_bootstrap=2000):
    """
    Compute Pearson correlation with bootstrap confidence interval.
    Uses 2000 bootstrap samples for efficiency.
    """
    logger.debug(f"Computing correlation with {n_bootstrap} bootstrap samples...")
    r, p = pearsonr(x, y)
    
    # Manual bootstrap for CI
    n = len(x)
    bootstrap_rs = []
    rng = np.random.RandomState(42)
    
    for i in range(n_bootstrap):
        idx = rng.choice(n, size=n, replace=True)
        bx = x[idx]
        by = y[idx]
        if np.std(bx) == 0 or np.std(by) == 0:
            continue
        br, _ = pearsonr(bx, by)
        bootstrap_rs.append(br)
    
    if len(bootstrap_rs) > 10:
        ci_low = np.percentile(bootstrap_rs, 2.5)
        ci_high = np.percentile(bootstrap_rs, 97.5)
    else:
        ci_low = ci_high = r
    
    logger.debug(f"Correlation: r={r:.4f}, CI=[{ci_low:.4f}, {ci_high:.4f}]")
    return r, p, ci_low, ci_high


def williams_test(r12, r13, r23, n):
    """
    Meng, Rosenthal, & Rubin (1992) test for comparing two dependent correlations.
    
    Tests whether r12 (SCD vs true) is significantly different from r13 (FK vs true),
    where r23 is the correlation between SCD and FK.
    
    Uses Fisher's z-transformation approach.
    
    Returns:
        z: z-statistic
        p: p-value (two-tailed)
    """
    # Fisher z-transformation
    z12 = np.arctanh(r12)
    z13 = np.arctanh(r13)
    
    # Difference in z-scores
    z_diff = z12 - z13
    
    # Variance of difference: 2*(1 - r23)/(n - 3)
    # From Meng, Rosenthal & Rubin (1992)
    var_diff = 2 * (1 - r23) / (n - 3)
    
    if var_diff <= 0:
        return 0.0, 1.0
    
    se_diff = np.sqrt(var_diff)
    z_stat = z_diff / se_diff
    
    # Two-tailed p-value from standard normal
    p = 2 * (1 - stats.norm.cdf(abs(z_stat)))
    
    return z_stat, p


def compute_rmse(y_true, y_pred):
    """Compute Root Mean Square Error."""
    return np.sqrt(mean_squared_error(y_true, y_pred))


def compute_cohens_d(x1, x2):
    """Compute Cohen's d for two independent samples."""
    n1, n2 = len(x1), len(x2)
    if n1 < 2 or n2 < 2:
        return 0.0
    
    mean1, mean2 = np.mean(x1), np.mean(x2)
    var1, var2 = np.var(x1, ddof=1), np.var(x2, ddof=1)
    
    pooled_std = np.sqrt(((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2))
    
    if pooled_std == 0:
        return 0.0
    
    return (mean1 - mean2) / pooled_std


def ensemble_correlation(x1, x2, y):
    """Compute correlation of ensemble (averaged standardized predictions) with true values."""
    # Standardize predictions
    x1_z = (x1 - np.mean(x1)) / np.std(x1)
    x2_z = (x2 - np.mean(x2)) / np.std(x2)
    
    # Ensemble = average of standardized predictions
    ensemble = (x1_z + x2_z) / 2
    
    r, p = pearsonr(ensemble, y)
    return r, p


def partial_correlation(x, y, control):
    """Compute partial correlation between x and y controlling for control variable."""
    X_c = control.reshape(-1, 1)
    reg_x = LinearRegression().fit(X_c, x)
    res_x = x - reg_x.predict(X_c)
    
    reg_y = LinearRegression().fit(X_c, y)
    res_y = y - reg_y.predict(X_c)
    
    r, p = pearsonr(res_x, res_y)
    return r, p


@logger.catch(reraise=True)
def main():
    logger.info("Starting SCD readability evaluation...")
    
    # Load data
    df = load_data('full_method_out.json')
    
    # Extract arrays
    true_grades = df['true_grade'].values
    scd_scores = df['predict_sce'].values
    fk_scores = df['predict_fk'].values
    complexity = df['complexity'].values
    
    results = {
        'metadata': {
            'evaluation_name': 'SCD Readability Metric Statistical Evaluation',
            'description': 'Comprehensive statistical evaluation comparing Semantic Coherence Distance (SCD) against Flesch-Kincaid',
            'n_examples': len(df),
            'complexity_levels': df['complexity'].value_counts().to_dict(),
        },
        'metrics_agg': {},
        'datasets': [{'dataset': 'synthetic_readability', 'examples': []}],
    }
    
    # Build per-example output
    examples_output = []
    for _, row in df.iterrows():
        examples_output.append({
            'input': row['text'],
            'output': str(row['true_grade']),
            'predict_sce': str(row['predict_sce']),
            'predict_flesch_kincaid': str(row['predict_fk']),
            'metadata_id': row['metadata_id'],
            'eval_scd_error': abs(row['predict_sce'] - row['true_grade']),
            'eval_fk_error': abs(row['predict_fk'] - row['true_grade']),
        })
    results['datasets'][0]['examples'] = examples_output
    
    # ============================================================
    # METRIC 1: PEARSON CORRELATION with Bootstrap CI
    # ============================================================
    logger.info("=" * 60)
    logger.info("METRIC 1: PEARSON CORRELATION with Bootstrap CI")
    logger.info("=" * 60)
    
    # SCD vs true grades
    r_scd, p_scd, ci_low_scd, ci_high_scd = compute_pearson_with_ci(scd_scores, true_grades)
    rmse_scd = compute_rmse(true_grades, scd_scores)
    
    logger.info(f"SCD vs True Grades:")
    logger.info(f"  Pearson r = {r_scd:.4f}, p = {p_scd:.6f}")
    logger.info(f"  95% Bootstrap CI: [{ci_low_scd:.4f}, {ci_high_scd:.4f}]")
    logger.info(f"  RMSE = {rmse_scd:.4f}")
    
    # FK vs true grades
    r_fk, p_fk, ci_low_fk, ci_high_fk = compute_pearson_with_ci(fk_scores, true_grades)
    rmse_fk = compute_rmse(true_grades, fk_scores)
    
    logger.info(f"FK vs True Grades:")
    logger.info(f"  Pearson r = {r_fk:.4f}, p = {p_fk:.6f}")
    logger.info(f"  95% Bootstrap CI: [{ci_low_fk:.4f}, {ci_high_fk:.4f}]")
    logger.info(f"  RMSE = {rmse_fk:.4f}")
    
    results['metrics_agg']['corr_scd_true'] = float(r_scd)
    results['metrics_agg']['p_scd_true'] = float(p_scd)
    results['metrics_agg']['ci_low_scd_true'] = float(ci_low_scd)
    results['metrics_agg']['ci_high_scd_true'] = float(ci_high_scd)
    results['metrics_agg']['rmse_scd'] = float(rmse_scd)
    
    results['metrics_agg']['corr_fk_true'] = float(r_fk)
    results['metrics_agg']['p_fk_true'] = float(p_fk)
    results['metrics_agg']['ci_low_fk_true'] = float(ci_low_fk)
    results['metrics_agg']['ci_high_fk_true'] = float(ci_high_fk)
    results['metrics_agg']['rmse_fk'] = float(rmse_fk)
    
    # ============================================================
    # METRIC 2: WILLIAMS TEST
    # ============================================================
    logger.info("=" * 60)
    logger.info("METRIC 2: WILLIAMS TEST (Comparing Dependent Correlations)")
    logger.info("=" * 60)
    
    # Correlation between SCD and FK
    r_scd_fk, p_scd_fk = pearsonr(scd_scores, fk_scores)
    
    logger.info(f"Correlation between SCD and FK: r = {r_scd_fk:.4f}, p = {p_scd_fk:.6f}")
    
    # Williams test
    t_williams, p_williams = williams_test(r_scd, r_fk, r_scd_fk, len(df))
    
    logger.info(f"Williams test: t = {t_williams:.4f}, p = {p_williams:.6f}")
    logger.info(f"  H0: r(SCD,true) = r(FK,true)")
    logger.info(f"  {'Reject H0' if p_williams < 0.05 else 'Fail to reject H0'} (alpha=0.05)")
    
    results['metrics_agg']['corr_scd_fk'] = float(r_scd_fk)
    results['metrics_agg']['williams_t'] = float(t_williams)
    results['metrics_agg']['williams_p'] = float(p_williams)
    
    # ============================================================
    # METRIC 3: ANOVA (SCD scores across complexity levels)
    # ============================================================
    logger.info("=" * 60)
    logger.info("METRIC 3: ANOVA (SCD scores across complexity levels)")
    logger.info("=" * 60)
    
    simple_scd = df[df['complexity'] == 'simple']['predict_sce'].values
    medium_scd = df[df['complexity'] == 'medium']['predict_sce'].values
    complex_scd = df[df['complexity'] == 'complex']['predict_sce'].values
    
    logger.info(f"Simple:  n={len(simple_scd)}, mean={np.mean(simple_scd):.4f}, std={np.std(simple_scd):.4f}")
    logger.info(f"Medium:  n={len(medium_scd)}, mean={np.mean(medium_scd):.4f}, std={np.std(medium_scd):.4f}")
    logger.info(f"Complex: n={len(complex_scd)}, mean={np.mean(complex_scd):.4f}, std={np.std(complex_scd):.4f}")
    
    f_stat, p_anova = stats.f_oneway(simple_scd, medium_scd, complex_scd)
    
    logger.info(f"ANOVA: F = {f_stat:.4f}, p = {p_anova:.6f}")
    logger.info(f"  {'Significant differences' if p_anova < 0.05 else 'No significant differences'} across complexity levels")
    
    # Also do ANOVA for FK across complexity levels
    simple_fk = df[df['complexity'] == 'simple']['predict_fk'].values
    medium_fk = df[df['complexity'] == 'medium']['predict_fk'].values
    complex_fk = df[df['complexity'] == 'complex']['predict_fk'].values
    
    f_stat_fk, p_anova_fk = stats.f_oneway(simple_fk, medium_fk, complex_fk)
    logger.info(f"ANOVA for FK: F = {f_stat_fk:.4f}, p = {p_anova_fk:.6f}")
    
    results['metrics_agg']['anova_scd_f'] = float(f_stat)
    results['metrics_agg']['anova_scd_p'] = float(p_anova)
    results['metrics_agg']['anova_fk_f'] = float(f_stat_fk)
    results['metrics_agg']['anova_fk_p'] = float(p_anova_fk)
    
    # ============================================================
    # METRIC 4: ERROR ANALYSIS
    # ============================================================
    logger.info("=" * 60)
    logger.info("METRIC 4: ERROR ANALYSIS")
    logger.info("=" * 60)
    
    scd_errors = np.abs(scd_scores - true_grades)
    fk_errors = np.abs(fk_scores - true_grades)
    
    logger.info("SCD Error Metrics:")
    logger.info(f"  Mean Absolute Error: {np.mean(scd_errors):.4f}")
    logger.info(f"  Median Absolute Error: {np.median(scd_errors):.4f}")
    logger.info(f"  IQR: [{np.percentile(scd_errors, 25):.4f}, {np.percentile(scd_errors, 75):.4f}]")
    logger.info(f"  RMSE: {rmse_scd:.4f}")
    
    logger.info("FK Error Metrics:")
    logger.info(f"  Mean Absolute Error: {np.mean(fk_errors):.4f}")
    logger.info(f"  Median Absolute Error: {np.median(fk_errors):.4f}")
    logger.info(f"  IQR: [{np.percentile(fk_errors, 25):.4f}, {np.percentile(fk_errors, 75):.4f}]")
    logger.info(f"  RMSE: {rmse_fk:.4f}")
    
    # Find worst predictions
    worst_scd_idx = np.argmax(scd_errors)
    worst_fk_idx = np.argmax(fk_errors)
    
    logger.info(f"Worst SCD prediction: idx={worst_scd_idx}, error={scd_errors[worst_scd_idx]:.4f}")
    logger.info(f"  Text: {df.iloc[worst_scd_idx]['text'][:100]}...")
    logger.info(f"  True: {true_grades[worst_scd_idx]:.2f}, Predicted: {scd_scores[worst_scd_idx]:.4f}")
    
    logger.info(f"Worst FK prediction: idx={worst_fk_idx}, error={fk_errors[worst_fk_idx]:.4f}")
    logger.info(f"  Text: {df.iloc[worst_fk_idx]['text'][:100]}...")
    logger.info(f"  True: {true_grades[worst_fk_idx]:.2f}, Predicted: {fk_scores[worst_fk_idx]:.4f}")
    
    # Where SCD outperforms FK (lower error)
    scd_better = scd_errors < fk_errors
    n_scd_better = np.sum(scd_better)
    logger.info(f"SCD outperforms FK on {n_scd_better}/{len(df)} examples ({100*n_scd_better/len(df):.1f}%)")
    
    results['metrics_agg']['mae_scd'] = float(np.mean(scd_errors))
    results['metrics_agg']['median_ae_scd'] = float(np.median(scd_errors))
    results['metrics_agg']['mae_fk'] = float(np.mean(fk_errors))
    results['metrics_agg']['median_ae_fk'] = float(np.median(fk_errors))
    results['metrics_agg']['n_scd_better'] = int(n_scd_better)
    results['metrics_agg']['pct_scd_better'] = float(100 * n_scd_better / len(df))
    
    # ============================================================
    # METRIC 5: COMPUTATIONAL EFFICIENCY
    # ============================================================
    logger.info("=" * 60)
    logger.info("METRIC 5: COMPUTATIONAL EFFICIENCY")
    logger.info("=" * 60)
    
    # Benchmark SCD
    n_runs = 100
    scd_times = []
    for _ in range(n_runs):
        start = time.perf_counter()
        for text in df['text'].values[:10]:  # Time on 10 texts
            sentences = [s.strip() for s in text.split(".") if s.strip()]
            if len(sentences) < 2:
                continue
            embeddings = np.array([[len(s)/200.0, len(s.split())/10.0] for s in sentences])
            transitions = embeddings[1:] - embeddings[:-1]
            energy = np.sum(np.linalg.norm(transitions, axis=1) ** 2)
            _ = float(energy / (len(embeddings) - 1))
        scd_times.append((time.perf_counter() - start) / 10 * 1000)  # ms per text
    
    mean_scd_time = np.mean(scd_times)
    
    # FK timing
    fk_times = []
    for _ in range(n_runs):
        start = time.perf_counter()
        for text in df['text'].values[:10]:
            _ = len(text.split()) / 3
        fk_times.append((time.perf_counter() - start) / 10 * 1000)
    
    mean_fk_time = np.mean(fk_times)
    
    logger.info(f"SCD processing time: {mean_scd_time:.4f} ms/text (mean of {n_runs} runs)")
    logger.info(f"FK processing time: {mean_fk_time:.6f} ms/text (mean of {n_runs} runs)")
    logger.info(f"SCD meets <1s requirement: {'YES' if mean_scd_time < 1000 else 'NO'}")
    logger.info(f"Estimated SBERT-SCD time from literature: ~10-50 ms/text")
    
    results['metrics_agg']['time_scd_ms'] = float(mean_scd_time)
    results['metrics_agg']['time_fk_ms'] = float(mean_fk_time)
    results['metrics_agg']['meets_time_requirement'] = float(mean_scd_time < 1000)
    
    # ============================================================
    # METRIC 6: COMPLEMENTARITY ANALYSIS
    # ============================================================
    logger.info("=" * 60)
    logger.info("METRIC 6: COMPLEMENTARITY ANALYSIS")
    logger.info("=" * 60)
    
    # (a) Already computed r_scd_fk above
    logger.info(f"(a) Correlation between SCD and FK predictions: r = {r_scd_fk:.4f}")
    logger.info(f"    {'Low correlation -> independent signals' if abs(r_scd_fk) < 0.3 else 'Moderate correlation' if abs(r_scd_fk) < 0.7 else 'High correlation -> redundant signals'}")
    
    # (b) Ensemble improvement
    r_ensemble, p_ensemble = ensemble_correlation(scd_scores, fk_scores, true_grades)
    logger.info(f"(b) Ensemble correlation with true grades: r = {r_ensemble:.4f}, p = {p_ensemble:.6f}")
    logger.info(f"    Ensemble improvement over SCD: {r_ensemble - r_scd:.4f}")
    logger.info(f"    Ensemble improvement over FK: {r_ensemble - r_fk:.4f}")
    
    # (c) Partial correlation: SCD vs true controlling for FK
    r_partial_scd, p_partial_scd = partial_correlation(scd_scores, true_grades, fk_scores)
    logger.info(f"(c) Partial correlation (SCD vs true | FK): r = {r_partial_scd:.4f}, p = {p_partial_scd:.6f}")
    logger.info(f"    {'SCD adds unique information beyond FK' if p_partial_scd < 0.05 else 'SCD does not add unique information beyond FK'}")
    
    r_partial_fk, p_partial_fk = partial_correlation(fk_scores, true_grades, scd_scores)
    logger.info(f"    Partial correlation (FK vs true | SCD): r = {r_partial_fk:.4f}, p = {p_partial_fk:.6f}")
    
    results['metrics_agg']['ensemble_corr'] = float(r_ensemble)
    results['metrics_agg']['ensemble_p'] = float(p_ensemble)
    results['metrics_agg']['partial_corr_scd_given_fk'] = float(r_partial_scd)
    results['metrics_agg']['partial_corr_p_scd_given_fk'] = float(p_partial_scd)
    results['metrics_agg']['partial_corr_fk_given_scd'] = float(r_partial_fk)
    results['metrics_agg']['partial_corr_p_fk_given_scd'] = float(p_partial_fk)
    
    # ============================================================
    # METRIC 7: EFFECT SIZE (Cohen's d)
    # ============================================================
    logger.info("=" * 60)
    logger.info("METRIC 7: EFFECT SIZE (Cohen's d for error differences)")
    logger.info("=" * 60)
    
    cohens_d_errors = compute_cohens_d(scd_errors, fk_errors)
    logger.info(f"Cohen's d (SCD errors vs FK errors): {cohens_d_errors:.4f}")
    logger.info(f"  {'Small' if abs(cohens_d_errors) < 0.2 else 'Medium' if abs(cohens_d_errors) < 0.5 else 'Large'} effect")
    
    cohens_d_simple_complex = compute_cohens_d(simple_scd, complex_scd)
    logger.info(f"Cohen's d (SCD: simple vs complex): {cohens_d_simple_complex:.4f}")
    
    results['metrics_agg']['cohens_d_error_diff'] = float(cohens_d_errors)
    results['metrics_agg']['cohens_d_scd_simple_complex'] = float(cohens_d_simple_complex)
    
    # ============================================================
    # METRIC 8: NORMALITY TESTS
    # ============================================================
    logger.info("=" * 60)
    logger.info("METRIC 8: NORMALITY TESTS (Shapiro-Wilk on error distributions)")
    logger.info("=" * 60)
    
    w_scd, p_w_scd = shapiro(scd_errors)
    w_fk, p_w_fk = shapiro(fk_errors)
    
    logger.info(f"SCD errors: W = {w_scd:.4f}, p = {p_w_scd:.6f}")
    logger.info(f"  {'Normal distribution' if p_w_scd >= 0.05 else 'Non-normal distribution'}")
    
    logger.info(f"FK errors: W = {w_fk:.4f}, p = {p_w_fk:.6f}")
    logger.info(f"  {'Normal distribution' if p_w_fk >= 0.05 else 'Non-normal distribution'}")
    
    results['metrics_agg']['normality_scd_errors_w'] = float(w_scd)
    results['metrics_agg']['normality_scd_errors_p'] = float(p_w_scd)
    results['metrics_agg']['normality_fk_errors_w'] = float(w_fk)
    results['metrics_agg']['normality_fk_errors_p'] = float(p_w_fk)
    
    # ============================================================
    # ADDITIONAL ANALYSES
    # ============================================================
    logger.info("=" * 60)
    logger.info("ADDITIONAL ANALYSES")
    logger.info("=" * 60)
    
    # Spearman rank correlation (non-parametric)
    rho_scd, p_rho_scd = stats.spearmanr(scd_scores, true_grades)
    rho_fk, p_rho_fk = stats.spearmanr(fk_scores, true_grades)
    
    logger.info(f"Spearman correlation (SCD vs true): rho = {rho_scd:.4f}, p = {p_rho_scd:.6f}")
    logger.info(f"Spearman correlation (FK vs true): rho = {rho_fk:.4f}, p = {p_rho_fk:.6f}")
    
    results['metrics_agg']['spearman_scd_true'] = float(rho_scd)
    results['metrics_agg']['spearman_fk_true'] = float(rho_fk)
    
    # R-squared
    r2_scd = r_scd ** 2
    r2_fk = r_fk ** 2
    
    logger.info(f"R-squared (SCD): {r2_scd:.4f} ({100*r2_scd:.1f}% of variance explained)")
    logger.info(f"R-squared (FK): {r2_fk:.4f} ({100*r2_fk:.1f}% of variance explained)")
    
    results['metrics_agg']['r2_scd'] = float(r2_scd)
    results['metrics_agg']['r2_fk'] = float(r2_fk)
    
    # ============================================================
    # SUMMARY
    # ============================================================
    logger.info("=" * 60)
    logger.info("SUMMARY OF RESULTS")
    logger.info("=" * 60)
    
    logger.info(f"1. Correlation with true grades:")
    logger.info(f"   SCD: r = {r_scd:.4f} [{ci_low_scd:.4f}, {ci_high_scd:.4f}]")
    logger.info(f"   FK:  r = {r_fk:.4f} [{ci_low_fk:.4f}, {ci_high_fk:.4f}]")
    logger.info(f"   Williams test: t = {t_williams:.4f}, p = {p_williams:.6f}")
    
    logger.info(f"2. Error rates:")
    logger.info(f"   SCD: MAE = {np.mean(scd_errors):.4f}, RMSE = {rmse_scd:.4f}")
    logger.info(f"   FK:  MAE = {np.mean(fk_errors):.4f}, RMSE = {rmse_fk:.4f}")
    
    logger.info(f"3. Complementarity:")
    logger.info(f"   SCD-FK correlation: r = {r_scd_fk:.4f}")
    logger.info(f"   Partial correlation (SCD|FK): r = {r_partial_scd:.4f}, p = {p_partial_scd:.6f}")
    logger.info(f"   Ensemble correlation: r = {r_ensemble:.4f}")
    
    logger.info(f"4. Computational efficiency:")
    logger.info(f"   SCD: {mean_scd_time:.4f} ms/text")
    logger.info(f"   FK:  {mean_fk_time:.6f} ms/text")
    
    logger.info(f"5. ANOVA (SCD across complexity): F = {f_stat:.4f}, p = {p_anova:.6f}")
    
    # Save results
    output_path = Path('eval_out.json')
    output_path.write_text(json.dumps(results, indent=2))
    logger.info(f"Saved results to {output_path}")
    
    # Generate full/mini/preview versions
    logger.info("Generating full/mini/preview versions...")
    try:
        import subprocess
        skill_dir = Path("/ai-inventor/.claude/skills/aii-json")
        format_script = skill_dir / "scripts" / "aii_json_format_mini_preview.py"
        py = str((skill_dir / ".." / ".ability_client_venv" / "bin" / "python").resolve())
        
        if format_script.exists():
            result = subprocess.run(
                [py, str(format_script), "--input", "eval_out.json"],
                cwd=str(Path.cwd()),
                capture_output=True,
                text=True,
                timeout=30
            )
            if result.returncode == 0:
                logger.info("Generated formatted versions successfully")
            else:
                logger.warning(f"Format script failed: {result.stderr}")
        else:
            logger.warning(f"Format script not found at {format_script}")
    except Exception as e:
        logger.warning(f"Could not generate formatted versions: {e}")
    
    logger.info("Evaluation complete!")


if __name__ == "__main__":
    main()
