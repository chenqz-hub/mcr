<!-- README.md -->
# OCR Project for Medical Case Images

## Project Overview
This project processes medical case images stored in the `pics` directory using OCR (Optical Character Recognition) to extract text content and saves the results into a CSV file in the `output` directory.

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- Ensure Tesseract is installed on your system. You can install it from: https://github.com/tesseract-ocr/tesseract

### Installation
1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
2. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Place your PNG image files in the `pics` directory.
2. Run the script:
   ```bash
   python src/main.py
   ```
3. The extracted text will be saved in a timestamped CSV file in the `output` directory.

## Notes
- Ensure the pics directory contains valid PNG images.
- Tesseract must be configured for Chinese OCR (lang="chi_sim").
- Logs are minimized for a cleaner terminal output.
