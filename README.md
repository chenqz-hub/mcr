<!-- README.md -->
# Image Text Extraction Tool for Medical Documents

## Project Overview

This project extracts text from PNG images of medical documents (like medical records or prescriptions) using PaddleOCR and saves the results into a CSV file. It's designed to process a batch of images in the `pics` directory, extracting key information, and outputting structured data into a timestamped CSV file in the `output` directory.

## Features

-   **Batch Image Processing:** Processes all PNG files located within the `pics` input directory.
-   **OCR using PaddleOCR:** Utilizes PaddleOCR to accurately recognize and extract text from the images.
-   **Structured Data Extraction:** Employs regular expressions to extract key fields such as hospital name, patient name, age, diagnosis, etc., from the extracted text.
-   **CSV Output:** Saves the structured data into a CSV file, facilitating easy analysis and integration with databases.
-   **Basic Error Handling:** Implements error handling for file processing and OCR operations, logging errors in the command line.
-   **Dynamic Path Handling:** Dynamically manages Python script imports using dynamic paths.
-   **Progress Indicator:** Includes a progress bar using `tqdm` to display the real-time processing status of images.
- **Minimal logging:** Logs are minimized to maintain a cleaner terminal output.

## Prerequisites

Before you begin, ensure that you have met the following requirements:

-   **Python 3.6+:** This tool requires Python 3.6 or a later version.
-   **PaddlePaddle:** Install PaddlePaddle for CPU using:
    ```bash
    pip install paddlepaddle
    ```
    Or PaddlePaddle with GPU using:
       ```bash
    pip install paddlepaddle-gpu
    ```
-   **PaddleOCR:** Install PaddleOCR using:
    ```bash
    pip install paddleocr
    ```
-   **Tesseract-OCR:** Tesseract-OCR is needed to pre-process the images, install from: [https://github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract).
-   **pandas:** Install pandas for data manipulation:
    ```bash
    pip install pandas
    ```
-   **tqdm:** Install tqdm for the progress bar:
    ```bash
    pip install tqdm
    ```

## Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

    (Note: Replace `<repository-url>` with the actual URL of your repository and `<repository-directory>` with the actual name of your repository directory).
2.  **Install required packages:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Place your PNG images:**

    Put the PNG image files you want to process inside the `pics` directory in the project root.
2.  **Run the script:**

    Execute the main script from the root directory:
    ```bash
    python src/main.py
    ```
3.  **Locate the output:**

    The results will be saved in a timestamped CSV file within the `output` directory.

## Project Structure
MCR/ # Project root directory
├── output/ # Directory for output CSV files
│ └── output_20240308_153000.csv # Example output file
├── pics/ # Directory for input PNG images
│ ├── image1.png
│ ├── image2.png
│ └── ...
├── src/ # Source code directory
│ ├── pycache/ # Python cache directory
│ ├── file_utils.py # File utility functions
│ ├── main.py # Main script
│ └── ocr_utils.py # OCR utility functions
├── .gitignore # Git ignore file
├── LICENSE # Project license file
├── README.md # This README file
└── requirements.txt # List of Python dependencies

## Code Explanation

### `src/main.py`

-   This is the main entry point of the application.
-   It dynamically adjusts the Python path, enabling relative imports of the other modules.
-   It defines the `pics` directory as the input and the `output` directory for CSV results.
-   The script iterates through all PNG files in the `pics` directory.
-   It utilizes the `extract_text_from_image` function to get the text content for each image.
-   The results are collected, converted into a pandas DataFrame, and saved as a CSV file in the `output` directory, with a unique filename generated using a timestamp.

### `src/ocr_utils.py`

-   This file contains utility functions for Optical Character Recognition (OCR), using PaddleOCR.
-   The `extract_text_from_image` function performs the following:
    -   Initializes PaddleOCR with Chinese language support.
    -   Performs text recognition on the provided image path.
    -   Concatenates the OCR results into a single string.
    -   Uses regular expressions to extract specific fields, such as the hospital name, patient name, and diagnosis.
    -   Returns a dictionary of the structured and extracted fields.

### `src/file_utils.py`

-   This file provides file management utilities.
-   The `list_png_files` function does the following:
    -   Receives a directory path as an input.
    -   Lists all the files located in the specified directory.
    -   Filters the list, returning only the PNG files.

## Key Extracted Data Fields

The script extracts the following fields from the medical document images:

-   **医院 (Hospital Name):** The name of the hospital.
-   **患者姓名 (Patient Name):** The name of the patient.
-   **性别 (Gender):** The gender of the patient.
-   **年龄 (Age):** The age of the patient.
-   **主诉 (Chief Complaint):** The main reason for the patient's visit.
-   **现病史 (Present Illness):** The history of the patient's current condition.
-   **既往史 (Past History):** The patient's past medical history.
-  **体格检查 (Physical Examination):** The findings of the physical examination.
-   **过敏史 (Allergy History):** Any allergies the patient may have.
-   **个人史 (Personal History):** Relevant personal details of the patient.
-   **生命体征 (Vital Signs):** The patient's vital signs.
-   **处理 (Treatment):** The treatment provided to the patient.
-   **辅助检查 (Auxiliary Examination):** Any additional examinations performed.
-   **诊断 (Diagnosis):** The diagnosis made by the doctor.
-   **处方 (Prescription):** The prescription provided to the patient.
-    **就诊科室 (Department):** The department the patient visited.
-   **就诊医生 (Doctor):** The name of the doctor who saw the patient.
-   **就诊日期 (Visit Date):** The date and time the patient visited.
-  **复诊流水号 (Revisit ID):** The revisit ID number
-   **更新日期 (Update Date):** The date and time the document was updated.

## Usage Tips

-   Ensure the PNG images are of sufficient quality to achieve the best results.
-   Adjust the regular expressions within `ocr_utils.py` to align with the specific structure of your input documents if necessary.
- The current regular expressions are hard-coded for medical reports and might need adjustments depending on your use case.
-   Tesseract-OCR is used for image pre-processing so make sure it is correctly installed on your system

## Known Issues

-  PaddleOCR's accuracy might be affected by poor-quality images. Pre-processing the images may enhance the results.
-  The regular expressions provided are tailored for a typical medical report and might not accurately match all document formats. Customization may be required.

## License

[License](LICENSE)