#!/usr/bin/env python3
import json
import numpy as np
from scipy.stats import pearsonr
from pathlib import Path

print("Loading data...")
data = json.loads(Path('full_method_out.json').read_text())
examples = data['datasets'][0]['examples']

true_grades = np.array([float(e['output']) for e in examples])
scd_scores = np.array([float(e['predict_sce']) for e in examples])
fk_scores = np.array([float(e['predict_flesch_kincaid']) for e in examples])

print(f"N = {len(true_grades)}")
print(f"True grade range: {np.min(true_grades):.2f} - {np.max(true_grades):.2f}")
print(f"SCD range: {np.min(scd_scores):.4f} - {np.max(scd_scores):.4f}")
print(f"FK range: {np.min(fk_scores):.2f} - {np.max(fk_scores):.2f}")

# Test correlation
r_scd, p_scd = pearsonr(scd_scores, true_grades)
r_fk, p_fk = pearsonr(fk_scores, true_grades)

print(f"\nSCD vs True: r = {r_scd:.4f}, p = {p_scd:.4f}")
print(f"FK vs True: r = {r_fk:.4f}, p = {p_fk:.4f}")
print("\nDone!")
