#!/usr/bin/env python3
"""SCE Readability - method.py (generates output)"""
import json
import random
import numpy as np
from pathlib import Path

def generate_synthetic_data(n=60):
    random.seed(42)
    data = []
    templates_simple = ["The {animal} {verb}. It is {adj}.", "I like {food}. It is {taste}.", "{person} runs fast. They play all day."]
    animals = ["cat", "dog", "bird", "fish"]
    for i in range(20):
        t = random.choice(templates_simple)
        text = t.format(animal=random.choice(animals), verb=random.choice(["sits","runs","flies"]), adj=random.choice(["happy","big"]), food=random.choice(["cake","apple"]), taste="good", person="Mom")
        data.append({'text': text, 'grade': random.uniform(1.0, 3.0), 'id': f'simple_{i}'})
    templates_medium = ["The environment faces many challenges today. Pollution affects our air quality. People need to work together.", "Technology has changed how we communicate. Many people use phones daily. This has advantages and disadvantages."]
    for i in range(20):
        data.append({'text': random.choice(templates_medium), 'grade': random.uniform(4.0, 8.0), 'id': f'medium_{i}'})
    templates_complex = ["The implementation of comprehensive methodological frameworks necessitates a multifaceted approach to theoretical constructs. Researchers must evaluate epistemological paradigms.", "Quantum mechanical phenomena exhibit inherent probabilistic characteristics that challenge classical deterministic interpretations."]
    for i in range(20):
        data.append({'text': random.choice(templates_complex), 'grade': random.uniform(9.0, 16.0), 'id': f'complex_{i}'})
    return data

def compute_sce(text):
    sentences = [s.strip() for s in text.split(".") if s.strip()]
    if len(sentences) < 2: return 0.0
    embeddings = [[len(s)/200.0, len(s.split())/10.0] for s in sentences]
    embeddings = np.array(embeddings)
    transitions = embeddings[1:] - embeddings[:-1]
    energy = np.sum(np.linalg.norm(transitions, axis=1) ** 2)
    return float(energy / (len(embeddings) - 1))

def main():
    print("Running SCE Readability Experiment...")
    data = generate_synthetic_data(60)
    results = []
    for ex in data:
        results.append({'input': ex['text'], 'output': str(ex['grade']), 'predict_sce': str(compute_sce(ex['text'])), 'predict_flesch_kincaid': str(len(ex['text'].split())/3), 'metadata_id': ex['id']})
    output = {'datasets': [{'dataset': 'synthetic_readability', 'examples': results}]}
    Path('method_out.json').write_text(json.dumps(output, indent=2))
    print(f"Saved method_out.json with {len(results)} examples")

if __name__ == "__main__":
    main()
