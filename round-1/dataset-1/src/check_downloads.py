#!/usr/bin/env python3
"""Standardize readability datasets that were downloaded via HF scripts."""

from loguru import logger
from pathlib import Path
import json
import sys

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

@logger.catch(reraise=True)
def main():
    # Check what files are available
    datasets_dir = Path("temp/datasets")
    datasets_dir.mkdir(parents=True, exist_ok=True)
    
    # List all files
    all_files = list(datasets_dir.glob("**/*"))
    logger.info(f"Found {len(all_files)} files in temp/datasets")
    
    for f in all_files:
        logger.info(f"  {f}")
    
    # Try to read the preview files to understand structure
    preview_files = list(datasets_dir.glob("preview_*.json"))
    
    if not preview_files:
        logger.warning("No preview files found. Trying to download datasets directly...")
        download_datasets_directly()
    else:
        logger.info(f"Found {len(preview_files)} preview files")
        standardize_from_previews(preview_files)

def download_datasets_directly():
    """Download datasets directly using HuggingFace API."""
    import requests
    
    logger.info("Downloading datasets directly from HuggingFace...")
    
    # Dataset URLs (parquet files from HF datasets server)
    datasets_to_download = {
        "clear_corpus": "https://huggingface.co/datasets/casey-martin/CommonLit-Ease-of-Readability/raw/main/clear_corpus.csv",
        "onestop_english": "https://huggingface.co/datasets/SetFit/onestop_english/raw/main/dev.csv",
    }
    
    output_dir = Path("temp/datasets/raw")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    for name, url in datasets_to_download.items():
        try:
            logger.info(f"Downloading {name} from {url}")
            response = requests.get(url, timeout=60)
            response.raise_for_status()
            
            output_path = output_dir / f"{name}.csv"
            output_path.write_bytes(response.content)
            logger.info(f"Saved to {output_path}")
            
        except Exception as e:
            logger.error(f"Failed to download {name}: {e}")

def standardize_from_previews(preview_files):
    """Try to standardize datasets from preview files."""
    logger.info("Standardizing from preview files...")
    
    # This is a placeholder - we need actual data
    # Let's try a different approach: use the HF datasets library via subprocess
    pass

if __name__ == "__main__":
    main()
