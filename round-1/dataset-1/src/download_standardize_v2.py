#!/usr/bin/env python3
"""Download and standardize readability datasets using huggingface_hub."""

from loguru import logger
from pathlib import Path
import json
import sys
import os
import pandas as pd

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

@logger.catch(reraise=True)
def main():
    # Create output directories
    raw_dir = Path("temp/datasets/raw")
    standardized_dir = Path("temp/datasets/standardized")
    raw_dir.mkdir(parents=True, exist_ok=True)
    standardized_dir.mkdir(parents=True, exist_ok=True)
    
    from huggingface_hub import hf_hub_download, list_repo_files
    
    # Download CLEAR corpus (CommonLit) - parquet files
    logger.info("Downloading CLEAR corpus (parquet)...")
    try:
        repo_id = "casey-martin/CommonLit-Ease-of-Readability"
        
        # Download train, test, val parquet files
        all_data = []
        for split in ["train", "test", "val"]:
            try:
                file_path = hf_hub_download(
                    repo_id=repo_id,
                    filename=f"data/clear_{split}.parquet",
                    repo_type="dataset",
                    cache_dir=str(raw_dir / "hf_cache")
                )
                
                df = pd.read_parquet(file_path)
                logger.info(f"CLEAR {split} shape: {df.shape}, columns: {df.columns.tolist()}")
                
                # Standardize
                standardized = standardize_clear_corpus(df, split)
                all_data.extend(standardized)
                
            except Exception as e:
                logger.warning(f"Could not download clear_{split}.parquet: {e}")
        
        if all_data:
            output_path = standardized_dir / "clear_corpus.json"
            output_path.write_text(json.dumps(all_data, indent=2))
            logger.info(f"Saved {len(all_data)} CLEAR examples to {output_path}")
                
    except Exception as e:
        logger.error(f"Failed to process CLEAR corpus: {e}")
    
    # Download OneStopEnglish - jsonl files
    logger.info("Downloading OneStopEnglish (jsonl)...")
    try:
        repo_id = "SetFit/onestop_english"
        
        all_data = []
        for split in ["train", "test"]:
            try:
                file_path = hf_hub_download(
                    repo_id=repo_id,
                    filename=f"{split}.jsonl",
                    repo_type="dataset",
                    cache_dir=str(raw_dir / "hf_cache")
                )
                
                # Read jsonl
                df = pd.read_json(file_path, lines=True)
                logger.info(f"OneStopEnglish {split} shape: {df.shape}")
                
                # Standardize
                standardized = standardize_onestop_english(df, split)
                all_data.extend(standardized)
                
            except Exception as e:
                logger.warning(f"Could not download {split}.jsonl: {e}")
        
        if all_data:
            output_path = standardized_dir / "onestop_english.json"
            output_path.write_text(json.dumps(all_data, indent=2))
            logger.info(f"Saved {len(all_data)} OneStopEnglish examples to {output_path}")
                
    except Exception as e:
        logger.error(f"Failed to process OneStopEnglish: {e}")
    
    # Try to download WikiLarge
    logger.info("Downloading WikiLarge...")
    try:
        repo_id = "bogdancazan/wikilarge-text-simplification"
        
        all_data = []
        for split in ["train", "valid", "test"]:
            try:
                file_path = hf_hub_download(
                    repo_id=repo_id,
                    filename=f"wiki.full.aner.ori.{split}.95.tsv",
                    repo_type="dataset",
                    cache_dir=str(raw_dir / "hf_cache")
                )
                
                df = pd.read_csv(file_path, sep='\t', header=None, names=["Normal", "Simple"])
                logger.info(f"WikiLarge {split} shape: {df.shape}")
                
                # Standardize
                standardized = standardize_wikilarge(df, split)
                all_data.extend(standardized)
                
            except Exception as e:
                logger.warning(f"Could not download wiki.full.aner.ori.{split}.95.tsv for WikiLarge: {e}")
        
        if all_data:
            output_path = standardized_dir / "wikilarge.json"
            output_path.write_text(json.dumps(all_data, indent=2))
            logger.info(f"Saved {len(all_data)} WikiLarge examples to {output_path}")
                
    except Exception as e:
        logger.error(f"Failed to process WikiLarge: {e}")
    
    # Create dataset summary
    create_summary(standardized_dir)

def standardize_clear_corpus(df, split):
    """Standardize CLEAR corpus to common schema."""
    standardized = []
    
    for _, row in df.iterrows():
        # Extract text - the column might be named differently
        text_col = None
        for col in ["Excerpt", "text", "content", "passage"]:
            if col in df.columns:
                text_col = col
                break
        
        if not text_col or not row[text_col]:
            continue
        
        # Extract readability scores
        # BT_easiness is the main CLEAR score (higher = easier)
        # Convert to difficulty (lower = easier)
        bt_easiness = row.get("BT_easiness", None)
        difficulty = None
        if bt_easiness and not pd.isna(bt_easiness):
            # Convert easiness to difficulty (1-5 scale, 1=easy, 5=hard)
            # BT_easiness is typically negative to positive
            difficulty = max(1, min(5, 3 - (bt_easiness / 2)))
        
        # Get Flesch-Kincaid Grade Level
        fk_grade = row.get("Flesch-Kincaid-Grade-Level", None)
        grade_level = None
        if fk_grade and not pd.isna(fk_grade):
            grade_level = str(int(fk_grade)) if fk_grade < 13 else None
        
        entry = {
            "text": str(row[text_col]),
            "readability_score": float(bt_easiness) if bt_easiness and not pd.isna(bt_easiness) else None,
            "grade_level": grade_level,
            "difficulty": int(difficulty) if difficulty else None,
            "source": "CLEAR",
            "text_id": str(row.get("ID", len(standardized))),
            "metadata": {
                "genre": str(row.get("Categ", "")),
                "author": str(row.get("Author", "")),
                "title": str(row.get("Title", "")),
                "lexile_band": str(row.get("Lexile Band", "")),
                "pub_year": str(row.get("Pub Year", "")),
                "original_split": split,
                "flesch_reading_ease": float(row.get("Flesch-Reading-Ease", None)) if not pd.isna(row.get("Flesch-Reading-Ease", None)) else None,
                "flesch_kincaid_grade": float(fk_grade) if fk_grade and not pd.isna(fk_grade) else None,
                "automated_readability_index": float(row.get("Automated Readability Index", None)) if not pd.isna(row.get("Automated Readability Index", None)) else None,
                "smog_readability": float(row.get("SMOG Readability", None)) if not pd.isna(row.get("SMOG Readability", None)) else None
            }
        }
        standardized.append(entry)
    
    return standardized

def standardize_onestop_english(df, split):
    """Standardize OneStopEnglish to common schema."""
    standardized = []
    
    # Map labels
    difficulty_map = {0: 1, 1: 3, 2: 5}  # Elementary=1, Intermediate=3, Advanced=5
    label_text_map = {0: "Elementary", 1: "Intermediate", 2: "Advanced"}
    
    for _, row in df.iterrows():
        text_col = "text" if "text" in df.columns else df.columns[0]
        label_col = "label" if "label" in df.columns else df.columns[-1]
        
        text = str(row[text_col])
        label = int(row[label_col]) if label_col in df.columns else 0
        
        entry = {
            "text": text,
            "readability_score": None,
            "grade_level": None,
            "difficulty": difficulty_map.get(label, 3),
            "source": "OneStopEnglish",
            "text_id": f"ose_{split}_{len(standardized)}",
            "metadata": {
                "label_text": label_text_map.get(label, "Unknown"),
                "original_split": split
            }
        }
        standardized.append(entry)
    
    return standardized

def standardize_wikilarge(df, split):
    """Standardize WikiLarge to common schema."""
    standardized = []
    
    for _, row in df.iterrows():
        normal_text = str(row.get("Normal", ""))
        simple_text = str(row.get("Simple", ""))
        
        if not normal_text:
            continue
        
        # Add normal (complex) text
        entry = {
            "text": normal_text,
            "readability_score": None,
            "grade_level": None,
            "difficulty": 4,  # Complex
            "source": "WikiLarge",
            "text_id": f"wiki_normal_{split}_{len(standardized)}",
            "metadata": {
                "simplified_text": simple_text,
                "original_split": split
            }
        }
        standardized.append(entry)
        
        # Add simple text
        if simple_text:
            entry_simple = {
                "text": simple_text,
                "readability_score": None,
                "grade_level": None,
                "difficulty": 2,  # Simple
                "source": "WikiLarge",
                "text_id": f"wiki_simple_{split}_{len(standardized)}",
                "metadata": {
                    "original_text": normal_text,
                    "original_split": split
                }
            }
            standardized.append(entry_simple)
    
    return standardized

def create_summary(standardized_dir):
    """Create summary of all standardized datasets."""
    logger.info("Creating dataset summary...")
    
    # Get absolute path
    std_dir = Path(standardized_dir).resolve()
    summary = {
        "datasets": {},
        "total_examples": 0
    }
    
    for json_file in std_dir.glob("*.json"):
        try:
            with open(json_file, 'r') as f:
                data = json.load(f)
                summary["datasets"][json_file.stem] = {
                    "path": str(json_file.relative_to(Path.cwd())),
                    "num_examples": len(data),
                    "sample_keys": list(data[0].keys()) if data else []
                }
                summary["total_examples"] += len(data)
        except Exception as e:
            logger.error(f"Error reading {json_file}: {e}")
    
    summary_path = std_dir / "dataset_summary.json"
    with open(summary_path, 'w') as f:
        json.dump(summary, f, indent=2)
    logger.info(f"Saved dataset summary to {summary_path}")
    logger.info(f"Total examples across all datasets: {summary['total_examples']}")

if __name__ == "__main__":
    main()
