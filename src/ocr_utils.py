# src/ocr_utils.py
from paddleocr import PaddleOCR
import re
import os
import logging

# Set logging level to ERROR to minimize unnecessary output
os.environ['GLOG_minloglevel'] = '3'
logging.getLogger().setLevel(logging.ERROR)

def extract_text_from_image(image_path):
    """
    Extract text from an image using PaddleOCR and structure the data into fields.
    :param image_path: Path to the image file
    :return: Extracted text in a structured format
    """
    try:
        # Initialize PaddleOCR with show_log=False to disable verbose output
        ocr = PaddleOCR(use_angle_cls=True, lang="ch", show_log=False)
        result = ocr.ocr(image_path, cls=True)

        # Combine OCR result into a single text block
        text = "\n".join([line[1][0] for line in result[0]])

        # Extract key fields using regex
        structured_data = {
            "医院": re.search(r"(上海交通大学医学院附属第\S+人民医院)", text, re.M),
            "患者姓名": re.search(r"姓名\s*[:：]\s*([\u4e00-\u9fa5]+)", text, re.M),
            "性别": re.search(r"性别\s*[:：]\s*([男女])", text, re.M),
            "年龄": re.search(r"年龄\s*[:：]\s*(\d+)", text, re.M),
            "主诉": re.search(r"主诉\s*[:：]\s*(.+)", text, re.M),
            "现病史": re.search(r"现病史\s*[:：]\s*(.+)", text, re.M),
            "既往史": re.search(r"既往史\s*[:：]\s*(.+)", text, re.M),
            "体格检查": re.search(r"体格检查\s*[:：]\s*(.+)", text, re.M),
            "过敏史": re.search(r"过敏史\s*[:：]\s*(.+)", text, re.M),
            "个人史": re.search(r"个人史\s*[:：]\s*(.+)", text, re.M),
            "生命体征": re.search(r"生命体征\s*[:：]\s*(.+)", text, re.M),
            "处理": re.search(r"处理\s*[:：]\s*(.+)", text, re.M),
            "辅助检查": re.search(r"辅助检查\s*[:：]\s*(.+)", text, re.M),
            "诊断": re.search(r"诊断\s*[:：]\s*(.+)", text, re.M),
            "处方": re.search(r"处方\s*[:：]\s*(.+)", text, re.M),
             "就诊科室": re.search(r"就诊科室\s*[:：]\s*(.+)", text, re.M),
            "就诊医生": re.search(r"就诊医生\s*[:：]\s*(.+)", text, re.M),
            "就诊日期": re.search(r"就诊日期\s*[:：]\s*(\d{4}-\d{2}-\d{2}\s*\d{2}:\d{2}:\d{2})", text, re.M),
             "复诊流水号": re.search(r"复诊流水号\s*[:：]\s*([a-zA-Z0-9]+)", text, re.M),
            "更新日期": re.search(r"更新日期\s*[:：]\s*(\d{4}-\d{2}-\d{2}\s*\d{2}:\d{2}:\d{2})", text, re.M),
            
        }
        # Clean and return structured data
        structured_data = {k: (v.group(1).strip() if v else "N/A") for k, v in structured_data.items()}

        return structured_data

    except Exception as e:
        return {"Error": str(e)}