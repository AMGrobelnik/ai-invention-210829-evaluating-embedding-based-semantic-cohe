#!/usr/bin/env python3
"""
Final SCE Readability Experiment - Complete Implementation.
"""
import json
import re
import numpy as np
import time
import gc
from pathlib import Path
from loguru import logger

# Configure logging
logger.remove()
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")
logger.add(lambda msg: print(msg), level="INFO")

class ReadabilityExperiment:
    """Complete experiment for SCE readability."""
    
    def __init__(self, data_path='data/full_dataset.json', use_sbert=True):
        self.data_path = Path(data_path)
        self.use_sbert = use_sbert
        self.model = None
        
    def sentence_tokenize(self, text):
        """Simple sentence tokenization."""
        sentences = re.split(r'(?<=[.!?])\s+', text.strip())
        return [s for s in sentences if s.strip()]
    
    def load_sbert_model(self):
        """Load sentence transformer model."""
        if not self.use_sbert:
            return None
        from sentence_transformers import SentenceTransformer
        logger.info("Loading SBERT model...")
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        logger.info("Model loaded!")
        return self.model
    
    def get_embeddings(self, sentences):
        """Get embeddings for sentences."""
        if self.model is not None:
            return self.model.encode(sentences, show_progress_bar=False)
        else:
            # Use sentence length and word complexity features
            embeddings = []
            for sent in sentences:
                # Features: sentence length, avg word length, unique words ratio
                words = re.findall(r'\b\w+\b', sent.lower())
                if not words:
                    emb = np.zeros(10)
                else:
                    feat1 = len(sent) / 200.0  # Normalized sentence length
                    feat2 = np.mean([len(w) for w in words]) / 10.0  # Avg word length
                    feat3 = len(set(words)) / len(words)  # Unique word ratio
                    feat4 = len([w for w in words if len(w) > 6]) / len(words)  # Complex word ratio
                    
                    # Create embedding from features + some n-grams
                    emb = np.array([
                        feat1, feat2, feat3, feat4,
                        len(sent) / 1000.0,
                        len(words) / 100.0,
                        np.std([len(w) for w in words]) if words else 0,
                        1.0 if '?' in sent else 0.0,
                        1.0 if ';' in sent else 0.0,
                        1.0 if any(w[0].isupper() for w in words) else 0.0
                    ])
                embeddings.append(emb)
            return np.array(embeddings)
    
    def compute_sce(self, text):
        """Compute Semantic Control Energy."""
        sentences = self.sentence_tokenize(text)
        
        if len(sentences) < 2:
            return 0.0, len(sentences)
        
        embeddings = self.get_embeddings(sentences)
        
        # Transitions
        transitions = embeddings[1:] - embeddings[:-1]
        
        # Energy
        energy = np.sum(np.linalg.norm(transitions, axis=1) ** 2)
        normalized = energy / (len(embeddings) - 1)
        
        return float(normalized), len(sentences)
    
    def flesch_kincaid(self, text):
        """Flesch-Kincaid Grade Level."""
        sentences = len([s for s in re.split(r'[.!?]+', text) if s.strip()])
        words = len(re.findall(r'\b\w+\b', text))
        
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
        return round(0.39 * asl + 11.8 * asw - 15.59, 2)
    
    def smog_grade(self, text):
        """SMOG Grade Level."""
        sentences = len([s for s in re.split(r'[.!?]+', text) if s.strip()])
        words = re.findall(r'\b\w+\b', text.lower())
        
        # Count complex words (3+ syllables)
        complex_words = 0
        for word in words:
            count = 0
            vowels = 'aeiouy'
            prev = False
            for c in word:
                if c in vowels and not prev:
                    count += 1
                prev = c in vowels
            if word.endswith('e'):
                count -= 1
            if count >= 3:
                complex_words += 1
        
        if sentences < 30:
            factor = 30 / max(sentences, 1)
            adjusted_complex = complex_words * factor
        else:
            adjusted_complex = complex_words
        
        if sentences == 0:
            return 0.0
        
        grade = 1.0430 * np.sqrt(adjusted_complex + 3) + 3.1291
        return round(grade, 2)
    
    def coleman_liau(self, text):
        """Coleman-Liau Index."""
        sentences = len([s for s in re.split(r'[.!?]+', text) if s.strip()])
        words = len(re.findall(r'\b\w+\b', text))
        characters = len(re.sub(r'\s+', '', text))
        
        if sentences == 0 or words == 0:
            return 0.0
        
        if words < 100:
            sentences = sentences * (100 / words)
        
        asl = (words / sentences) * 100
        asw = (characters / words) * 100
        
        grade = 0.0588 * asw - 0.296 * asl - 15.8
        return round(grade, 2)

    
    def run(self, max_samples=None):
        """Run the experiment."""
        logger.info("="*60)
        logger.info("Starting SCE Readability Experiment")
        logger.info("="*60)
        
        # Load data
        if not self.data_path.exists():
            logger.error(f"Data not found: {self.data_path}")
            return None
        
        with open(self.data_path, 'r') as f:
            data = json.load(f)
        
        if max_samples:
            data = data[:max_samples]
        
        logger.info(f"Loaded {len(data)} examples")
        
        # Load model if using SBERT
        if self.use_sbert:
            self.load_sbert_model()
        
        results = []
        grades = []  # Store grades separately
        start = time.time()
        
        for i, example in enumerate(data):
            text = example['text']
            grade = example['grade']
            grades.append(grade)  # Store for correlation
            
            sce, n_sents = self.compute_sce(text)
            fk = self.flesch_kincaid(text)
            smog = self.smog_grade(text)
            cli = self.coleman_liau(text)
            
            results.append({
                'input': text[:500],
                'output': str(grade),
                'predict_sce': str(sce),
                'predict_flesch_kincaid': str(fk),
                'predict_smog': str(smog),
                'predict_coleman_liau': str(cli),
                'metadata_id': example.get('id', str(i)),
                'metadata_num_sentences': n_sents,
            })
            
            if (i+1) % 10 == 0:
                logger.info(f"Processed {i+1}/{len(data)}")
        
        elapsed = time.time() - start
        logger.info(f"Done! {len(data)} examples in {elapsed:.1f}s")
        
        # Correlations
        true_g = np.array(grades)
        sce_s = np.array([float(r['predict_sce']) for r in results])
        fk_s = np.array([float(r['predict_flesch_kincaid']) for r in results])
        smog_s = np.array([float(r['predict_smog']) for r in results])
        cli_s = np.array([float(r['predict_coleman_liau']) for r in results])
        
        from scipy import stats
        sce_r = stats.pearsonr(sce_s, true_g)[0]
        fk_r = stats.pearsonr(fk_s, true_g)[0]
        smog_r = stats.pearsonr(smog_s, true_g)[0]
        cli_r = stats.pearsonr(cli_s, true_g)[0]
        
        logger.info("="*60)
        logger.info("CORRELATIONS WITH TRUE GRADE:")
        logger.info(f"  SCE Pearson r: {sce_r:.4f}")
        logger.info(f"  Flesch-Kincaid Pearson r: {fk_r:.4f}")
        logger.info(f"  SMOG Pearson r: {smog_r:.4f}")
        logger.info(f"  Coleman-Liau Pearson r: {cli_r:.4f}")
        logger.info("="*60)
        
        # Output
        output = {
            'metadata': {
                'method': 'SCE with SBERT' if self.use_sbert else 'SCE simple',
                'correlations': {
                    'SCE': float(sce_r),
                    'FleschKincaid': float(fk_r)
                }
            },
            'datasets': [{'dataset': 'readability', 'examples': results}]
        }
        
        out_path = Path('results/method_out.json')
        out_path.parent.mkdir(exist_ok=True)
        with open(out_path, 'w') as f:
            json.dump(output, f, indent=2)
        
        logger.info(f"Saved to {out_path}")
        return output

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', default='data/full_dataset.json')
    parser.add_argument('--max-samples', type=int, default=50)
    parser.add_argument('--no-sbert', action='store_true')
    args = parser.parse_args()
    
    exp = ReadabilityExperiment(args.data, use_sbert=not args.no_sbert)
    exp.run(max_samples=args.max_samples)
