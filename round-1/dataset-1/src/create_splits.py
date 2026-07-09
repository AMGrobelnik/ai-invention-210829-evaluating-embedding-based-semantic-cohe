#!/usr/bin/env python3
"""Create train/validation/test splits and generate dataset variants."""

from loguru import logger
from pathlib import Path
import json
import sys
import pandas as pd
from sklearn.model_selection import train_test_split

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

@logger.catch(reraise=True)
def main():
    # Load standardized datasets
    standardized_dir = Path("temp/datasets/standardized")
    
    # Process each dataset
    for dataset_file in standardized_dir.glob("*.json"):
        if dataset_file.stem == "dataset_summary":
            continue
        
        logger.info(f"Processing {dataset_file.name}...")
        
        with open(dataset_file, 'r') as f:
            data = json.load(f)
        
        logger.info(f"  Loaded {len(data)} examples")
        
        # Create train/val/test splits (70/15/15)
        # Stratify by difficulty if available
        difficulties = [d.get("difficulty") for d in data]
        
        if all(d is not None for d in difficulties):
            # Stratified split
            train_data, temp_data = train_test_split(
                data, test_size=0.3, random_state=42, stratify=difficulties
            )
            val_data, test_data = train_test_split(
                temp_data, test_size=0.5, random_state=42,
                stratify=[d.get("difficulty") for d in temp_data]
            )
        else:
            # Random split
            train_data, temp_data = train_test_split(
                data, test_size=0.3, random_state=42
            )
            val_data, test_data = train_test_split(
                temp_data, test_size=0.5, random_state=42
            )
        
        logger.info(f"  Train: {len(train_data)}, Val: {len(val_data)}, Test: {len(test_data)}")
        
        # Save splits
        dataset_name = dataset_file.stem
        splits_dir = standardized_dir / dataset_name / "splits"
        splits_dir.mkdir(parents=True, exist_ok=True)
        
        for split_name, split_data in [("train", train_data), ("val", val_data), ("test", test_data)]:
            split_path = splits_dir / f"{split_name}.json"
            with open(split_path, 'w') as f:
                json.dump(split_data, f, indent=2)
            logger.info(f"  Saved {split_name} split to {split_path}")
        
        # Create mini dataset (10 random examples)
        mini_data = train_data[:10] if len(train_data) >= 10 else train_data
        mini_path = standardized_dir / dataset_name / f"{dataset_name}_mini.json"
        mini_path.parent.mkdir(parents=True, exist_ok=True)
        with open(mini_path, 'w') as f:
            json.dump(mini_data, f, indent=2)
        logger.info(f"  Saved mini dataset to {mini_path}")
        
        # Create preview dataset (3 examples with truncated text)
        preview_data = []
        for item in train_data[:3]:
            preview_item = item.copy()
            if len(preview_item["text"]) > 200:
                preview_item["text"] = preview_item["text"][:200] + "..."
            preview_data.append(preview_item)
        
        preview_path = standardized_dir / dataset_name / f"{dataset_name}_preview.json"
        with open(preview_path, 'w') as f:
            json.dump(preview_data, f, indent=2)
        logger.info(f"  Saved preview dataset to {preview_path}")
    
    # Create combined dataset summary
    create_final_summary(standardized_dir)
    logger.info("Done!")

def create_final_summary(standardized_dir):
    """Create final summary of all datasets."""
    logger.info("Creating final dataset summary...")
    
    # Get absolute path
    std_dir = Path(standardized_dir).resolve()
    summary = {
        "datasets": {},
        "total_examples": 0,
        "dataset_paths": {}
    }
    
    for dataset_dir in std_dir.iterdir():
        if not dataset_dir.is_dir() or dataset_dir.name == "hf_cache":
            continue
        
        dataset_name = dataset_dir.name
        
        # Count total examples
        splits_dir = dataset_dir / "splits"
        total = 0
        if splits_dir.exists():
            for split_file in splits_dir.glob("*.json"):
                with open(split_file, 'r') as f:
                    split_data = json.load(f)
                    total += len(split_data)
        
        # Get relative paths
        try:
            splits_rel = str(splits_dir.relative_to(std_dir.parent.parent))
            mini_rel = str((dataset_dir / f"{dataset_name}_mini.json").relative_to(std_dir.parent.parent))
            preview_rel = str((dataset_dir / f"{dataset_name}_preview.json").relative_to(std_dir.parent.parent))
        except:
            splits_rel = str(splits_dir)
            mini_rel = str(dataset_dir / f"{dataset_name}_mini.json")
            preview_rel = str(dataset_dir / f"{dataset_name}_preview.json")
        
        summary["datasets"][dataset_name] = {
            "total_examples": total,
            "splits_dir": splits_rel,
            "mini_path": mini_rel,
            "preview_path": preview_rel
        }
        summary["total_examples"] += total
    
    summary_path = std_dir.parent / "dataset_summary_final.json"
    with open(summary_path, 'w') as f:
        json.dump(summary, f, indent=2)
    
    logger.info(f"Saved final summary to {summary_path}")
    logger.info(f"Total examples across all datasets: {summary['total_examples']}")

if __name__ == "__main__":
    main()
