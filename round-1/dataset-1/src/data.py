#!/usr/bin/env python3
"""Transform standardized readability datasets to exp_sel_data_out.json schema."""

from loguru import logger
from pathlib import Path
import json
import sys

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

@logger.catch(reraise=True)
def main():
    """
    Load standardized datasets and transform to exp_sel_data_out.json schema.
    
    Schema requires:
    - datasets: array of objects with "dataset" and "examples" fields
    - examples: array of objects with "input" (string) and "output" (string) fields
    - Optional: metadata_* fields per example
    """
    
    # Load dataset summary
    summary_path = Path("temp/datasets/dataset_summary_final.json")
    if not summary_path.exists():
        logger.error(f"Dataset summary not found at {summary_path}")
        logger.info("Running create_splits.py to generate splits...")
        import subprocess
        result = subprocess.run(["python", "create_splits.py"], capture_output=True, text=True)
        if result.returncode != 0:
            logger.error(f"Failed to create splits: {result.stderr}")
            sys.exit(1)
    
    with open(summary_path, 'r') as f:
        summary = json.load(f)
    
    logger.info(f"Found {len(summary['datasets'])} datasets")
    
    # Transform datasets to exp_sel_data_out schema
    output = {
        "metadata": {
            "description": "Readability datasets for SCE evaluation",
            "total_examples": summary["total_examples"],
            "sources": list(summary["datasets"].keys())
        },
        "datasets": []
    }
    
    # Process each dataset
    base_dir = Path("temp/datasets/standardized")
    
    for dataset_name in ["clear_corpus", "onestop_english", "wikilarge"]:
        logger.info(f"Processing {dataset_name}...")
        
        # Load training split (use train for experiment selection)
        splits_dir = base_dir / dataset_name / "splits"
        train_file = splits_dir / "train.json"
        
        if not train_file.exists():
            logger.warning(f"Training split not found at {train_file}, skipping...")
            continue
        
        with open(train_file, 'r') as f:
            examples = json.load(f)
        
        logger.info(f"  Loaded {len(examples)} training examples")
        
        # Transform examples to schema format
        transformed_examples = []
        for i, example in enumerate(examples):
            # Create input (text to evaluate)
            input_text = example.get("text", "")
            if not input_text:
                continue
            
            # Create output (readability score or difficulty)
            # Prefer: readability_score > difficulty > grade_level
            output_value = None
            if example.get("readability_score") is not None:
                output_value = str(example["readability_score"])
            elif example.get("difficulty") is not None:
                output_value = str(example["difficulty"])
            elif example.get("grade_level") is not None:
                output_value = str(example["grade_level"])
            else:
                # Skip examples without readability labels
                continue
            
            # Build transformed example
            transformed = {
                "input": input_text,
                "output": output_value
            }
            
            # Add metadata fields (flat, not nested)
            if example.get("source"):
                transformed["metadata_source"] = example["source"]
            
            if example.get("text_id"):
                transformed["metadata_text_id"] = str(example["text_id"])
            
            if example.get("difficulty") is not None:
                transformed["metadata_difficulty"] = example["difficulty"]
            
            if example.get("grade_level"):
                transformed["metadata_grade_level"] = example["grade_level"]
            
            # Add metadata from original example
            if example.get("metadata"):
                metadata = example["metadata"]
                if isinstance(metadata, dict):
                    # Flatten metadata
                    for key, value in metadata.items():
                        if key in ["flesch_reading_ease", "flesch_kincaid_grade", 
                                   "automated_readability_index", "smog_readability"]:
                            transformed[f"metadata_{key}"] = str(value) if value else None
                        elif key in ["genre", "author", "title", "lexile_band"]:
                            transformed[f"metadata_{key}"] = str(value) if value else None
            
            transformed_examples.append(transformed)
        
        logger.info(f"  Transformed {len(transformed_examples)} examples")
        
        # Add to output
        output["datasets"].append({
            "dataset": dataset_name,
            "examples": transformed_examples
        })
    
    # Save output
    output_path = Path("full_data_out.json")
    with open(output_path, 'w') as f:
        json.dump(output, f, indent=2)
    
    logger.info(f"Saved {len(output['datasets'])} datasets to {output_path}")
    
    # Print summary
    total_examples = sum(len(d["examples"]) for d in output["datasets"])
    logger.info(f"Total examples: {total_examples}")
    for dataset in output["datasets"]:
        logger.info(f"  {dataset['dataset']}: {len(dataset['examples'])} examples")

if __name__ == "__main__":
    main()
