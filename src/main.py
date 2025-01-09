# src/main.py
import os
import sys

# Dynamically add project root directory to module search path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.ocr_utils import extract_text_from_image
from src.file_utils import list_png_files

import pandas as pd
from datetime import datetime
from tqdm import tqdm

def main():
    input_dir = "pics"
    output_dir = "output"

    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        # Get all PNG files in the input directory
        png_files = list_png_files(input_dir)
        if not png_files:
            print("No PNG files found in the input directory.")
            return
    except Exception as e:
        print(f"Error listing files: {e}")
        return

    # Process each PNG file
    results = []
    for file in tqdm(png_files, desc="Processing images"):
        try:
            text = extract_text_from_image(file)
            results.append({"file": os.path.basename(file), "content": text})
        except Exception as e:
            print(f"Error processing file {file}: {e}")

    # Generate output CSV file name with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(output_dir, f"output_{timestamp}.csv")

    # Save results to CSV
    pd.DataFrame(results).to_csv(output_file, index=False, encoding="utf-8")
    print(f"Processing complete. Results saved to {output_file}")

if __name__ == "__main__":
    main()
