#!/usr/bin/env python3
"""Ultra-simple SCE implementation for testing concept."""
import json
import re
import numpy as np
import time

def simple_embedding(sentence, vocab_size=1000):
    """Create a simple bag-of-words embedding."""
    # Create a simple hash-based embedding
    words = re.findall(r'\b\w+\b', sentence.lower())
    embedding = np.zeros(vocab_size)
    
    for word in words:
        # Simple hash to get index
        idx = hash(word) % vocab_size
        embedding[idx] += 1.0
    
    # Normalize
    norm = np.linalg.norm(embedding)
    if norm > 0:
        embedding = embedding / norm
    
    return embedding

def sentence_tokenize(text):
    """Simple sentence tokenization."""
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    return [s for s in sentences if s.strip()]

def compute_sce(text):
    """Compute Semantic Control Energy for text."""
    sentences = sentence_tokenize(text)
    
    if len(sentences) < 2:
        return 0.0, len(sentences)
    
    # Get embeddings
    embeddings = np.array([simple_embedding(s) for s in sentences])
    
    # Compute transitions: u(t) = x(t+1) - x(t)
    transitions = embeddings[1:] - embeddings[:-1]
    
    # Energy = sum of squared norms
    energy = np.sum(np.linalg.norm(transitions, axis=1) ** 2)
    
    # Normalize
    normalized = energy / (len(embeddings) - 1)
    
    return float(normalized), len(sentences)

def flesch_kincaid_grade(text):
    """Simple Flesch-Kincaid implementation."""
    sentences = len([s for s in re.split(r'[.!?]+', text) if s.strip()])
    words = len(re.findall(r'\b\w+\b', text))
    
    # Simple syllable count
    syllables = 0
    for word in re.findall(r'\b\w+\b', text.lower()):
        # Count vowel groups
        count = 0
        vowels = 'aeiouy'
        prev_vowel = False
        for c in word:
            is_vowel = c in vowels
            if is_vowel and not prev_vowel:
                count += 1
            prev_vowel = is_vowel
        # Adjust for silent e
        if word.endswith('e'):
            count -= 1
        syllables += max(count, 1)
    
    if sentences == 0 or words == 0:
        return 0.0
    
    asl = words / sentences
    asw = syllables / words
    return round(0.39 * asl + 11.8 * asw - 15.59, 2)

def main():
    print("="*60)
    print("SCE Readability Experiment (Ultra-Simple Version)")
    print("="*60)
    
    # Load data
    with open('data/full_dataset.json', 'r') as f:
        data = json.load(f)
    
    print(f"Loaded {len(data)} examples")
    
    results = []
    
    start_time = time.time()
    
    for i, example in enumerate(data):
        text = example['text']
        true_grade = example['grade']
        
        # Compute metrics
        sce_score, num_sents = compute_sce(text)
        fk_score = flesch_kincaid_grade(text)
        
        results.append({
            'id': example['id'],
            'text': text[:100],
            'sce': sce_score,
            'fk': fk_score,
            'grade': true_grade,
            'n_sents': num_sents
        })
        
        print(f"  {i+1}. SCE={sce_score:.4f}, FK={fk_score:.2f}, Grade={true_grade:.2f}")
    
    total_time = time.time() - start_time
    print(f"\nProcessed {len(data)} examples in {total_time:.2f}s")
    print(f"Average time per example: {total_time/len(data)*1000:.1f}ms")
    
    # Compute correlations (using simple numpy correlation)
    true_grades = np.array([r['grade'] for r in results])
    sce_scores = np.array([r['sce'] for r in results])
    fk_scores = np.array([r['fk'] for r in results])
    
    # Pearson correlation
    sce_r = np.corrcoef(sce_scores, true_grades)[0, 1]
    fk_r = np.corrcoef(fk_scores, true_grades)[0, 1]
    
    print("\n" + "="*60)
    print("CORRELATIONS WITH TRUE GRADE:")
    print(f"  SCE Pearson r: {sce_r:.4f}")
    print(f"  Flesch-Kincaid Pearson r: {fk_r:.4f}")
    print("="*60)
    
    # Save results in required format
    output = {
        'datasets': [{
            'dataset': 'synthetic_readability',
            'examples': [{
                'input': r['text'],
                'output': str(r['grade']),
                'predict_sce': str(r['sce']),
                'predict_flesch_kincaid': str(r['fk']),
                'metadata_id': r['id']
            } for r in results]
        }]
    }
    
    with open('results/method_out.json', 'w') as f:
        json.dump(output, f, indent=2)
    
    print("\nResults saved to results/method_out.json")
    
    # Also save summary
    summary = {
        'total_examples': len(results),
        'correlations': {
            'SCE': {'pearson_r': float(sce_r)},
            'Flesch-Kincaid': {'pearson_r': float(fk_r)}
        },
        'avg_time_per_example_ms': float(total_time/len(data)*1000)
    }
    
    with open('results/summary.json', 'w') as f:
        json.dump(summary, f, indent=2)
    
    print("Summary saved to results/summary.json")

if __name__ == "__main__":
    main()
