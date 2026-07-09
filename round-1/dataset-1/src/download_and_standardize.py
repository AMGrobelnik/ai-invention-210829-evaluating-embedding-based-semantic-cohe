#!/usr/bin/env python3
"""Download and standardize readability datasets for SCE evaluation."""

from loguru import logger
from pathlib import Path
import json
import sys
import pandas as pd
from datasets import load_dataset
from sklearn.model_selection import train_test_split

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

@logger.catch(reraise=True)
def main():
    # Create output directory
    output_dir = Path("temp/datasets/standardized")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Load and standardize CLEAR corpus (CommonLit)
    logger.info("Processing CLEAR corpus (CommonLit)...")
    try:
        ds = load_dataset("casey-martin/CommonLit-Ease-of-Readability")
        
        # Combine all splits
        all_data = []
        for split in ds.keys():
            for row in ds[split]:
                # Extract excerpt text and metadata
                text = row.get("Excerpt", "")
                if not text:
                    continue
                
                # Create standardized entry
                entry = {
                    "text": text,
                    "readability_score": None,  # Need to compute or use Lexile
                    "grade_level": None,
                    "difficulty": None,
                    "source": "CLEAR",
                    "text_id": str(row.get("ID", f"clear_{len(all_data)}")),
                    "metadata": {
                        "genre": row.get("Categ", ""),
                        "author": row.get("Author", ""),
                        "title": row.get("Title", ""),
                        "lexile_band": row.get("Lexile Band", ""),
                        "pub_year": row.get("Pub Year", ""),
                        "original_split": split
                    }
                }
                all_data.append(entry)
        
        # Save CLEAR dataset
        clear_path = output_dir / "clear_corpus.json"
        clear_path.write_text(json.dumps(all_data, indent=2))
        logger.info(f"Saved {len(all_data)} CLEAR examples to {clear_path}")
        
    except Exception as e:
        logger.error(f"Failed to process CLEAR corpus: {e}")
    
    # Load and standardize OneStopEnglish
    logger.info("Processing OneStopEnglish corpus...")
    try:
        # Try iastate version first
        ds = load_dataset("iastate/onestop_english")
        
        all_data = []
        for split in ds.keys():
            for row in ds[split]:
                text = row.get("text", "")
                label = row.get("label", 0)
                
                # Map labels: 0=elementary, 1=intermediate, 2=advanced
                difficulty_map = {0: 1, 1: 3, 2: 5}  # 1-5 scale
                
                entry = {
                    "text": text,
                    "readability_score": None,
                    "grade_level": None,
                    "difficulty": difficulty_map.get(label, 3),
                    "source": "OneStopEnglish",
                    "text_id": str(len(all_data)),
                    "metadata": {
                        "label_text": ["Elementary", "Intermediate", "Advanced"][label] if label < 3 else "Unknown",
                        "original_split": split
                    }
                }
                all_data.append(entry)
        
        # Save OneStopEnglish dataset
        ose_path = output_dir / "onestop_english.json"
        ose_path.write_text(json.dumps(all_data, indent=2))
        logger.info(f"Saved {len(all_data)} OneStopEnglish examples to {ose_path}")
        
    except Exception as e:
        logger.error(f"Failed to process OneStopEnglish: {e}")
    
    # Load and standardize WikiLarge
    logger.info("Processing WikiLarge...")
    try:
        ds = load_dataset("bogdancazan/wikilarge-text-simplification")
        
        all_data = []
        for split in ds.keys():
            for row in ds[split]:
                normal_text = row.get("Normal", "")
                simple_text = row.get("Simple", "")
                
                if not normal_text:
                    continue
                
                # Add normal (complex) text
                entry = {
                    "text": normal_text,
                    "readability_score": None,
                    "grade_level": None,
                    "difficulty": 4,  # Complex
                    "source": "WikiLarge",
                    "text_id": f"wiki_normal_{len(all_data)}",
                    "metadata": {
                        "simplified_text": simple_text,
                        "original_split": split
                    }
                }
                all_data.append(entry)
                
                # Add simple text
                if simple_text:
                    entry_simple = {
                        "text": simple_text,
                        "readability_score": None,
                        "grade_level": None,
                        "difficulty": 2,  # Simple
                        "source": "WikiLarge",
                        "text_id": f"wiki_simple_{len(all_data)}",
                        "metadata": {
                            "original_text": normal_text,
                            "original_split": split
                        }
                    }
                    all_data.append(entry_simple)
        
        # Save WikiLarge dataset
        wiki_path = output_dir / "wikilarge.json"
        wiki_path.write_text(json.dumps(all_data, indent=2))
        logger.info(f"Saved {len(all_data)} WikiLarge examples to {wiki_path}")
        
    except Exception as e:
        logger.error(f"Failed to process WikiLarge: {e}")
    
    # Try to load agentlans/readability (has grade level)
    logger.info("Processing agentlans/readability...")
    try:
        ds = load_dataset("agentlans/readability", split="validation")
        
        all_data = []
        for row in ds:
            text = row.get("text", "")
            grade = row.get("grade", None)
            
            if not text or grade is None:
                continue
            
            entry = {
                "text": text,
                "readability_score": float(grade) if grade else None,
                "grade_level": str(int(grade)) if grade and grade < 13 else None,
                "difficulty": min(5, max(1, int(grade / 4))) if grade else None,  # Normalize to 1-5
                "source": "agentlans_readability",
                "text_id": str(len(all_data)),
                "metadata": {
                    "source_dataset": row.get("source", ""),
                    "original_grade": grade
                }
            }
            all_data.append(entry)
        
        # Save agentlans dataset
        agent_path = output_dir / "agentlans_readability.json"
        agent_path.write_text(json.dumps(all_data, indent=2))
        logger.info(f"Saved {len(all_data)} agentlans examples to {agent_path}")
        
    except Exception as e:
        logger.error(f"Failed to process agentlans/readability: {e}")
    
    # Create summary
    logger.info("Creating dataset summary...")
    summary = {
        "datasets": {},
        "total_examples": 0
    }
    
    for json_file in output_dir.glob("*.json"):
        with open(json_file) as f:
            data = json.load(f)
            summary["datasets"][json_file.stem] = {
                "path": str(json_file),
                "num_examples": len(data),
                "sample_keys": list(data[0].keys()) if data else []
            }
            summary["total_examples"] += len(data)
    
    summary_path = output_dir / "dataset_summary.json"
    summary_path.write_text(json.dumps(summary, indent=2))
    logger.info(f"Saved dataset summary to {summary_path}")
    logger.info(f"Total examples across all datasets: {summary['total_examples']}")

if __name__ == "__main__":
    main()
