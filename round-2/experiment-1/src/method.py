#!/usr/bin/env python3
"""
SCD Readability Experiment (TF-IDF version)
"""
import re
import json
import time
import numpy as np
from pathlib import Path
from loguru import logger
from typing import Dict, List, Optional
from scipy.stats import pearsonr
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_distances
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

try:
    import textstat
    textstat.set_lang('en')
    HAS_TEXTSTAT = True
except:
    HAS_TEXTSTAT = False
    logger.warning("textstat not available")


class SCDReadabilityExperiment:
    def __init__(self, data_path: str):
        self.data_path = Path(data_path)
        self.results = {
            "metadata": {"experiment": "SCD Readability", "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")},
            "evaluation": {}, "timing": {}, "plots": []
        }
    
    def tokenize_sentences(self, text: str) -> List[str]:
        sentences = re.split(r'(?<=[.!?])\s+', text.strip())
        return [s for s in sentences if s.strip()]
    
    def compute_scd(self, text: str) -> float:
        sentences = self.tokenize_sentences(text)
        if len(sentences) < 2:
            return np.nan
        try:
            tfidf = TfidfVectorizer(max_features=500)
            vectors = tfidf.fit_transform(sentences).toarray()
            cos_dists = []
            for i in range(len(vectors) - 1):
                dist = cosine_distances([vectors[i]], [vectors[i+1]])[0][0]
                cos_dists.append(dist)
            return float(np.mean(cos_dists))
        except:
            return np.nan
    
    def compute_readability(self, text: str) -> Dict[str, float]:
        scores = {}
        if HAS_TEXTSTAT:
            try:
                scores["flesch_kincaid"] = textstat.flesch_kincaid_grade(text)
            except:
                scores["flesch_kincaid"] = np.nan
        else:
            scores["flesch_kincaid"] = self._manual_fk(text)
        return scores
    
    def _manual_fk(self, text: str) -> float:
        words = text.split()
        sentences = self.tokenize_sentences(text)
        if len(sentences) == 0 or len(words) == 0:
            return np.nan
        syllable_count = sum(max(1, len(re.findall(r"[aeiouy]+", w.lower()))) for w in words)
        asl = len(words) / len(sentences)
        asw = syllable_count / len(words)
        return 0.39 * asl + 11.8 * asw - 15.59
    
    def load_data(self):
        logger.info(f"Loading {self.data_path}")
        with open(self.data_path, "r") as f:
            return json.load(f)
    
    def process_dataset(self, dataset, max_examples=None):
        examples = dataset["examples"]
        if max_examples:
            examples = examples[:max_examples]
        logger.info(f"Processing {len(examples)} examples from {dataset['dataset']}")
        results = []
        for i, ex in enumerate(examples):
            if i % 50 == 0:
                logger.info(f"  Processed {i}/{len(examples)}")
            text = ex["input"]
            target = ex["output"]
            r = {"input": text, "output": target, "dataset": dataset["dataset"]}
            r["predict_scd"] = self.compute_scd(text)
            r.update(self.compute_readability(text))
            # Copy metadata fields
            for k, v in ex.items():
                if k.startswith("metadata_"):
                    r[k] = v
            results.append(r)
        return results
    
    def evaluate_clear(self, results):
        logger.info("Evaluating CLEAR corpus")
        valid = []
        for r in results:
            try:
                t = float(r["output"])
                if not np.isnan(t):
                    valid.append(r)
            except: pass
        logger.info(f"Valid examples: {len(valid)}")
        metrics = ["scd", "flesch_kincaid"]
        correlations = {}
        for metric in metrics:
            values, targets = [], []
            for r in valid:
                v = r.get(metric)
                if v is not None and not np.isnan(float(v)):
                    values.append(float(v))
                    targets.append(float(r["output"]))
            if len(values) >= 10:
                try:
                    r_val, p_val = pearsonr(values, targets)
                    correlations[metric] = {"pearson_r": float(r_val), "p_value": float(p_val), "n": len(values)}
                    logger.info(f"  {metric}: r={r_val:.4f}, p={p_val:.4f}")
                except Exception as e:
                    logger.warning(f"Correlation failed for {metric}: {e}")
        return correlations
    

    def evaluate_onestop(self, results):
        """Evaluate OneStopEnglish classification."""
        from sklearn.tree import DecisionTreeClassifier
        from sklearn.model_selection import cross_val_score
        
        logger.info("Evaluating OneStopEnglish")
        valid = [r for r in results if r.get('output') in ['1', '2', '3']]
        logger.info(f"Valid examples: {len(valid)}")
        
        if len(valid) < 30:
            return {}
        
        # Prepare features
        X = []
        y = []
        for r in valid:
            features = [r.get('scd', np.nan), r.get('flesch_kincaid', np.nan)]
            if not any(np.isnan(f) for f in features):
                X.append(features)
                y.append(int(r['target']))
        
        if len(X) < 30:
            return {}
        
        X = np.array(X)
        y = np.array(y)
        
        clf = DecisionTreeClassifier(max_depth=5, random_state=42)
        scores = cross_val_score(clf, X, y, cv=5, scoring='accuracy')
        
        return {'accuracy_mean': float(np.mean(scores)), 'accuracy_std': float(np.std(scores))}
    
    def evaluate_wikilarge(self, results):
        """Evaluate WikiLarge ranking."""
        logger.info("Evaluating WikiLarge")
        # Group by pair ID using metadata_text_id
        # Format: wiki_simple_train_XXX or wiki_normal_train_XXX
        pairs = {}
        for r in results:
            text_id = r.get('metadata_text_id', '')
            if not text_id:
                continue
            
            # Extract numeric ID
            parts = text_id.split('_')
            if len(parts) >= 4:
                numeric_id = parts[-1]  # Last part is the numeric ID
                
                if numeric_id not in pairs:
                    pairs[numeric_id] = {}
                
                if 'simple' in text_id:
                    pairs[numeric_id]['simple'] = r
                elif 'normal' in text_id:
                    pairs[numeric_id]['normal'] = r
        
        logger.info(f"Found {len(pairs)} pairs")
        
        # Compute ranking accuracy
        correct = 0
        total = 0
        for numeric_id, pair in pairs.items():
            if 'simple' in pair and 'normal' in pair:
                s_scd = pair['simple'].get('scd', np.nan)
                n_scd = pair['normal'].get('scd', np.nan)
                if not np.isnan(s_scd) and not np.isnan(n_scd):
                    total += 1
                    if s_scd < n_scd:  # Lower SCD = simpler
                        correct += 1
        
        if total > 0:
            accuracy = correct / total
            logger.info(f"  Ranking accuracy: {accuracy:.4f} ({correct}/{total})")
            return {'ranking_accuracy': accuracy, 'correct': correct, 'total': total}
        return {}


    def generate_plots(self, clear_results, output_dir='plots'):
        """Generate scatter plots for CLEAR corpus."""
        import os
        os.makedirs(output_dir, exist_ok=True)
        
        logger.info("Generating visualizations")
        valid = [r for r in clear_results if not np.isnan(float(r.get('output', np.nan)))]
        
        if len(valid) < 10:
            return []
        
        plot_files = []
        metrics = ['scd', 'flesch_kincaid']
        
        for metric in metrics:
            values, targets = [], []
            for r in valid:
                v = r.get(metric)
                if v is not None and not np.isnan(float(v)):
                    values.append(float(v))
                    targets.append(float(r['target']))
            
            if len(values) < 10:
                continue
            
            plt.figure(figsize=(8, 6))
            plt.scatter(values, targets, alpha=0.5)
            plt.xlabel(metric)
            plt.ylabel('Human readability judgment')
            
            r_val, p_val = pearsonr(values, targets)
            plt.title(f'{metric} vs Human (r={r_val:.3f})')
            
            plot_file = os.path.join(output_dir, f'{metric}_vs_human.png')
            plt.savefig(plot_file, dpi=150, bbox_inches='tight')
            plt.close()
            plot_files.append(plot_file)
            logger.info(f"  Saved: {plot_file}")
        
        return plot_files


    def run(self, max_examples=None):
        logger.info("Starting experiment")
        data = self.load_data()
        all_results = {}
        
        # Process all datasets
        for dataset in data["datasets"]:
            results = self.process_dataset(dataset, max_examples)
            all_results[dataset["dataset"]] = results
        
        # Run evaluations (stores in self.results)
        if "clear_corpus" in all_results:
            self.results["evaluation"]["clear_corpus"] = self.evaluate_clear(all_results["clear_corpus"])
        if "onestop_english" in all_results:
            self.results["evaluation"]["onestop_english"] = self.evaluate_onestop(all_results["onestop_english"])
        if "wikilarge" in all_results:
            self.results["evaluation"]["wikilarge"] = self.evaluate_wikilarge(all_results["wikilarge"])
        
        # Generate plots
        if "clear_corpus" in all_results:
            self.results["plots"] = self.generate_plots(all_results["clear_corpus"])
        
        # Save results in exp_gen_sol_out schema format
        output_file = "method_out.json"
        output_data = {
            "datasets": []
        }
        
        # Convert all_results to schema format
        for dataset_name, results in all_results.items():
            dataset_examples = []
            for r in results:
                example = {
                    "input": r.get("input", ""),
                    "output": str(r.get("output", ""))
                }
                # Add prediction fields
                if "predict_scd" in r:
                    example["predict_scd"] = str(r["predict_scd"])
                if "flesch_kincaid" in r:
                    example["predict_flesch_kincaid"] = str(r["flesch_kincaid"])
                # Add metadata fields
                for k, v in r.items():
                    if k.startswith("metadata_"):
                        example[k] = v
                dataset_examples.append(example)
            
            output_data["datasets"].append({
                "dataset": dataset_name,
                "examples": dataset_examples
            })
        
        with open(output_file, "w") as f:
            json.dump(output_data, f, indent=2)
        
        logger.info(f"Saved results to {output_file}")
        return output_data



@logger.catch(reraise=True)
def main():
    data_path = sys.argv[1] if len(sys.argv) > 1 else "../iter_1/gen_art/gen_art_dataset_1/mini_data_out.json"
    max_examples = int(sys.argv[2]) if len(sys.argv) > 2 else None
    experiment = SCDReadabilityExperiment(data_path)
    experiment.run(max_examples)


if __name__ == "__main__":
    main()
