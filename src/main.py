# src/main.py
import os
import pandas as pd
from datetime import datetime
from src.ocr_utils import extract_text_from_image
from src.file_utils import list_png_files

def main():
    input_dir = "pics"
    output_dir = "output"

    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Get all PNG files in the input directory
    png_files = list_png_files(input_dir)

    # Process each PNG file
    results = []
    for file in png_files:
        print(f"Processing {file}...")
        text = extract_text_from_image(file)
        results.append({"file": os.path.basename(file), "content": text})

    # Generate output CSV file name with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(output_dir, f"output_{timestamp}.csv")

    # Save results to CSV
    pd.DataFrame(results).to_csv(output_file, index=False, encoding="utf-8")
    print(f"Processing complete. Results saved to {output_file}")

if __name__ == "__main__":
    main()
