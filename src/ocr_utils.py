# src/ocr_utils.py
import pytesseract
from PIL import Image

def extract_text_from_image(image_path):
    """
    Extract text from an image using Tesseract OCR.
    :param image_path: Path to the image file
    :return: Extracted text
    """
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image, lang="chi_sim")
        return text.strip()
    except Exception as e:
        return f"Error: {e}"
