#!/usr/bin/env python3
"""
Convert PDF pages to PNG images for visual review.
"""
import os
import sys

try:
    import pymupdf
except ImportError:
    import fitz as pymupdf

def pdf_to_png(pdf_path, output_dir, dpi=150):
    """
    Convert each page of a PDF to a PNG image.
    
    Args:
        pdf_path: Path to the PDF file
        output_dir: Directory to save PNG images
        dpi: Resolution in DPI (default: 150)
    """
    os.makedirs(output_dir, exist_ok=True)
    
    # Open the PDF
    doc = pymupdf.open(pdf_path)
    print(f"PDF has {len(doc)} pages")
    
    # Calculate zoom factor from DPI
    zoom = dpi / 72  # 72 DPI is the base PDF resolution
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        
        # Render page to image
        mat = pymupdf.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=mat)
        
        # Save as PNG
        output_path = os.path.join(output_dir, f"page_{page_num + 1:02d}.png")
        pix.save(output_path)
        print(f"Saved {output_path}")
    
    doc.close()
    print(f"\nConverted {len(doc)} pages to PNG at {dpi} DPI")

if __name__ == "__main__":
    pdf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "paper.pdf")
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "page_images")
    
    if not os.path.exists(pdf_path):
        print(f"Error: PDF not found at {pdf_path}")
        sys.exit(1)
    
    pdf_to_png(pdf_path, output_dir, dpi=150)
    print("\nDone!")
