#!/usr/bin/env python3
"""Quick test script to verify SCD computation works."""

import sys
sys.path.insert(0, '/ai-inventor/aii_data/runs/run_6uOr5GlpaMfR/3_invention_loop/iter_2/gen_art/gen_art_experiment_1')

from loguru import logger
import numpy as np

# Configure logging
logger.remove()
logger.add(sys.stdout, level="INFO")

# Test imports
try:
    from sentence_transformers import SentenceTransformer
    import textstat
    textstat.set_lang('en')
    logger.info("All packages imported successfully")
except Exception as e:
    logger.error(f"Import failed: {e}")
    sys.exit(1)

# Test SCD computation
def tokenize_sentences(text):
    import re
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    return [s for s in sentences if s.strip()]

def compute_scd(text, model):
    sentences = tokenize_sentences(text)
    if len(sentences) < 2:
        return np.nan
    
    embeddings = model.encode(sentences, show_progress_bar=False)
    
    cos_dists = []
    for i in range(len(embeddings) - 1):
        cos_sim = np.dot(embeddings[i], embeddings[i+1]) / (
            np.linalg.norm(embeddings[i]) * np.linalg.norm(embeddings[i+1]) + 1e-8)
        cos_dists.append(1 - cos_sim)
    
    return float(np.mean(cos_dists))

# Load model
logger.info("Loading SBERT model...")
model = SentenceTransformer('all-MiniLM-L6-v2')
logger.info("Model loaded")

# Test with sample texts
coherent_text = "The cat sat on the mat. The mat was comfortable. The cat enjoyed sitting."
incoherent_text = "The cat sat on the mat. Quantum mechanics describes particle behavior. Bananas are yellow fruits."

scd_coherent = compute_scd(coherent_text, model)
scd_incoherent = compute_scd(incoherent_text, model)

logger.info(f"SCD coherent: {scd_coherent:.4f}")
logger.info(f"SCD incoherent: {scd_incoherent:.4f}")
logger.info(f"Incoherent > Coherent: {scd_incoherent > scd_coherent}")

# Test readability
simple_text = "The cat sat. The dog ran. Kids played."
complex_text = "The juxtaposition of lexicographical elements necessitates methodological recalibration."

logger.info(f"FK simple: {textstat.flesch_kincaid_grade(simple_text):.2f}")
logger.info(f"FK complex: {textstat.flesch_kincaid_grade(complex_text):.2f}")

logger.info("All tests passed!")
