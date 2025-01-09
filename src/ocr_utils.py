# src/ocr_utils.py
from paddleocr import PaddleOCR
import re
import os
import logging

# Set logging level to ERROR to minimize unnecessary output
os.environ['GLOG_minloglevel'] = '2'
logging.getLogger().setLevel(logging.ERROR)

def extract_text_from_image(image_path):
    """
    Extract text from an image using PaddleOCR and structure the data into fields.
    :param image_path: Path to the image file
    :return: Extracted text in a structured format
    """
    try:
        # Initialize PaddleOCR
        ocr = PaddleOCR(use_angle_cls=True, lang="ch")
        result = ocr.ocr(image_path, cls=True)

        # Combine OCR result into a single text block
        text = "\n".join([line[1][0] for line in result[0]])

        # Extract key fields using regex
        structured_data = {
            "医院": re.search(r"医院\s*[:：]\s*(.*)", text, re.M),
            "患者姓名": re.search(r"姓名\s*[:：]\s*(.*)", text, re.M),
            "性别": re.search(r"性别\s*[:：]\s*(.*)", text, re.M),
            "年龄": re.search(r"年龄\s*[:：]\s*(.*)", text, re.M),
            "主诉": re.search(r"主诉\s*[:：]\s*(.*)", text, re.M),
            "现病史": re.search(r"现病史\s*[:：]\s*(.*)", text, re.M),
            "诊断": re.search(r"论断\s*[:：]\s*(.*)", text, re.M),
        }

        # Clean and return structured data
        structured_data = {k: (v.group(1).strip() if v else "N/A") for k, v in structured_data.items()}
        return structured_data

    except Exception as e:
        return {"Error": str(e)}
