#!/usr/bin/env python3
"""Minimal SCE test script."""
import json
import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy import stats

def sentence_tokenize(text):
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    return [s for s in sentences if s.strip()]

def compute_sce(text):
    sentences = sentence_tokenize(text)
    if len(sentences) < 2:
        return 0.0, 0
    
    # Simple TF-IDF embeddings
    vectorizer = TfidfVectorizer(stop_words='english', max_features=500)
    embeddings = vectorizer.fit_transform(sentences).toarray()
    
    # Compute transitions
    transitions = embeddings[1:] - embeddings[:-1]
    
    # SCE = sum of squared norms
    energy = np.sum(np.linalg.norm(transitions, axis=1) ** 2)
    normalized = energy / (len(embeddings) - 1)
    
    return float(normalized), len(sentences)

def flesch_kincaid(text):
    sentences = len([s for s in re.split(r'[.!?]+', text) if s.strip()])
    words = len(re.findall(r'\b\w+\b', text))
    
    # Count syllables (simplified)
    syllables = 0
    for word in re.findall(r'\b\w+\b', text.lower()):
        count = 0
        vowels = 'aeiouy'
        prev = False
        for c in word:
            if c in vowels and not prev:
                count += 1
            prev = c in vowels
        if word.endswith('e'):
            count -= 1
        syllables += max(count, 1)
    
    if sentences == 0 or words == 0:
        return 0.0
    
    asl = words / sentences
    asw = syllables / words
    return 0.39 * asl + 11.8 * asw - 15.59

# Load data
with open('data/full_dataset.json', 'r') as f:
    data = json.load(f)

print(f"Processing {len(data)} examples...")

results = []
for i, ex in enumerate(data):
    text = ex['text']
    grade = ex['grade']
    
    sce, n_sents = compute_sce(text)
    fk = flesch_kincaid(text)
    
    results.append({
        'id': ex['id'],
        'sce': sce,
        'fk': fk,
        'grade': grade,
        'n_sents': n_sents
    })
    
    print(f"  {i+1}. SCE={sce:.4f}, FK={fk:.2f}, Grade={grade:.2f}, Sents={n_sents}")

# Correlations
true_grades = [r['grade'] for r in results]
sce_scores = [r['sce'] for r in results]
fk_scores = [r['fk'] for r in results]

sce_r, _ = stats.pearsonr(sce_scores, true_grades)
fk_r, _ = stats.pearsonr(fk_scores, true_grades)

print("\n" + "="*50)
print("RESULTS:")
print(f"  SCE Pearson r: {sce_r:.4f}")
print(f"  FK Pearson r:  {fk_r:.4f}")
print("="*50)

# Save
output = {
    'datasets': [{
        'dataset': 'synthetic',
        'examples': [{
            'input': r['id'],
            'output': str(r['grade']),
            'predict_sce': str(r['sce']),
            'predict_flesch_kincaid': str(r['fk'])
        } for r in results]
    }]
}

with open('results/method_out.json', 'w') as f:
    json.dump(output, f, indent=2)

print("\nSaved to results/method_out.json")
