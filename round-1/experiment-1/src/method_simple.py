#!/usr/bin/env python3
"""
Simplified SCE Readability - Uses TF-IDF embeddings for faster testing.
"""

from loguru import logger
from pathlib import Path
import json
import sys
import os
import re
import time
import numpy as np
from typing import Dict, List, Optional, Tuple
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Configure logging
logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")


class SimpleEmbedder:
    """Simple TF-IDF based embedder for testing SCE concept."""
    
    def __init__(self, max_features=1000):
        self.vectorizer = TfidfVectorizer(max_features=max_features, stop_words='english')
        self.fitted = False
        
    def fit(self, sentences: List[str]):
        """Fit the vectorizer on sentences."""
        self.vectorizer.fit(sentences)
        self.fitted = True
        
    def encode(self, sentences: List[str]) -> np.ndarray:
        """Encode sentences to embeddings."""
        if not self.fitted:
            self.fit(sentences)
        
        embeddings = self.vectorizer.transform(sentences).toarray()
        return embeddings


class BaselineReadabilityMetrics:
    """Implementation of traditional readability metrics."""
    
    @staticmethod
    def flesch_kincaid_grade(text: str) -> float:
        sentences = len(re.split(r'[.!?]+', text.strip()))
        words = len(re.findall(r'\b\w+\b', text))
        syllables = sum(BaselineReadabilityMetrics._syllables(w) for w in re.findall(r'\b\w+\b', text))
        
        if sentences == 0 or words == 0:
            return 0.0
        
        asl = words / sentences
        asw = syllables / words
        return round(0.39 * asl + 11.8 * asw - 15.59, 2)
    
    @staticmethod
    def _syllables(word: str) -> int:
        word = word.lower()
        count = 0
        vowels = 'aeiouy'
        prev_vowel = False
        
        for char in word:
            is_vowel = char in vowels
            if is_vowel and not prev_vowel:
                count += 1
            prev_vowel = is_vowel
        
        if word.endswith('e'):
            count -= 1
        return max(count, 1)


class SemanticControlEnergy:
    """SCE implementation with simple embeddings."""
    
    def __init__(self, embedder_type='tfidf'):
        self.embedder_type = embedder_type
        if embedder_type == 'tfidf':
            self.embedder = SimpleEmbedder()
        
    def _sentence_tokenize(self, text: str) -> List[str]:
        sentences = re.split(r'(?<=[.!?])\s+', text.strip())
        return [s for s in sentences if s.strip()]
    
    def compute_sce(self, text: str) -> Tuple[float, int]:
        """Compute SCE for a text."""
        sentences = self._sentence_tokenize(text)
        
        if len(sentences) < 2:
            return 0.0, len(sentences)
        
        # Get embeddings
        embeddings = self.embedder.encode(sentences)
        
        # Compute transitions
        transitions = embeddings[1:] - embeddings[:-1]
        
        # SCE = sum of squared norms
        energy = np.sum(np.linalg.norm(transitions, axis=1) ** 2)
        normalized = energy / (len(embeddings) - 1)
        
        return float(normalized), len(sentences)


def main():
    """Run experiment with synthetic data."""
    logger.info("Starting SCE Readability Experiment (Simplified)")
    
    # Load data
    data_path = Path('data/full_dataset.json')
    with open(data_path, 'r') as f:
        data = json.load(f)
    
    logger.info(f"Loaded {len(data)} examples")
    
    # Initialize
    baseline = BaselineReadabilityMetrics()
    sce_calc = SemanticControlEnergy('tfidf')
    
    results = []
    
    for i, example in enumerate(data):
        text = example['text']
        true_grade = example['grade']
        
        # Baseline metrics
        fk = baseline.flesch_kincaid_grade(text)
        
        # SCE
        sce_score, num_sents = sce_calc.compute_sce(text)
        
        result = {
            'input': text[:200],
            'output': str(true_grade),
            'metadata_text_id': example.get('id', str(i)),
            'metadata_source': example.get('source', ''),
            'metadata_num_sentences': num_sents,
            'predict_sce': str(sce_score),
            'predict_flesch_kincaid': str(fk),
            'true_grade': float(true_grade)
        }
        results.append(result)
        
        logger.info(f"Example {i+1}: SCE={sce_score:.4f}, FK={fk:.2f}, True={true_grade:.2f}")
    
    # Compute correlations
    true_grades = np.array([r['true_grade'] for r in results])
    sce_scores = np.array([float(r['predict_sce']) for r in results])
    fk_scores = np.array([float(r['predict_flesch_kincaid']) for r in results])
    
    from scipy import stats
    
    sce_r, _ = stats.pearsonr(sce_scores, true_grades)
    fk_r, _ = stats.pearsonr(fk_scores, true_grades)
    
    logger.info("=" * 50)
    logger.info("CORRELATIONS WITH TRUE GRADE:")
    logger.info(f"  SCE Pearson r: {sce_r:.4f}")
    logger.info(f"  Flesch-Kincaid Pearson r: {fk_r:.4f}")
    logger.info("=" * 50)
    
    # Save results
    output = {
        'metadata': {
            'method_name': 'Semantic Control Energy (Simplified)',
            'correlations': {
                'SCE': {'pearson_r': float(sce_r)},
                'Flesch-Kincaid': {'pearson_r': float(fk_r)}
            }
        },
        'datasets': [{'dataset': 'synthetic', 'examples': results}]
    }
    
    output_path = Path('results/method_out.json')
    output_path.parent.mkdir(exist_ok=True)
    with open(output_path, 'w') as f:
        json.dump(output, f, indent=2)
    
    logger.info(f"Results saved to {output_path}")
    

if __name__ == "__main__":
    main()
