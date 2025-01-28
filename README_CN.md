# MCR 项目

## 项目介绍

MCR 项目旨在从医学文档的 PNG 图像中提取文本，并将结果保存到 CSV 文件中。该项目使用 PaddleOCR 进行光学字符识别 (OCR)，并通过正则表达式提取关键字段，如医院名称、患者姓名、年龄、诊断等。项目设计用于批量处理 `pics` 目录中的图像，并将结构化数据输出到 `output` 目录中的带有时间戳的 CSV 文件中。

## 目录

```
MCR/
├── output/                # 输出 CSV 文件目录
│   └── output_20240308_153000.csv  # 输出文件示例
├── pics/                  # 输入 PNG 图像目录
│   ├── image1.png
│   ├── image2.png
│   └── ...
├── src/                   # 源代码目录
│   ├── __pycache__/       # Python 缓存目录
│   ├── file_utils.py      # 文件工具函数
│   ├── main.py            # 主脚本
│   └── ocr_utils.py       # OCR 工具函数
├── .gitignore             # Git 忽略文件
├── LICENSE                # 项目许可证文件
├── README.md              # 项目 README 文件
└── requirements.txt       # Python 依赖列表
```

## 学习目标

通过本项目，你将学习到以下内容：

1. **批量图像处理：** 处理 `pics` 输入目录中的所有 PNG 文件。
2. **使用 PaddleOCR 进行 OCR：** 利用 PaddleOCR 准确识别和提取图像中的文本。
3. **结构化数据提取：** 使用正则表达式从提取的文本中提取关键字段，如医院名称、患者姓名、年龄、诊断等。
4. **CSV 输出：** 将结构化数据保存到 CSV 文件中，方便分析并与数据库集成。
5. **基本错误处理：** 实现文件处理和 OCR 操作的错误处理，并在命令行中记录错误。
6. **动态路径处理：** 使用动态路径管理 Python 脚本导入。
7. **进度指示器：** 使用 `tqdm` 显示图像处理的实时进度条。
8. **最小化日志：** 默认情况下日志被最小化，以保持终端输出的简洁。

## 环境要求

在开始之前，请确保满足以下要求：

- **Python 3.6+：** 本工具需要 Python 3.6 或更高版本。
- **PaddlePaddle：** 使用以下命令安装 CPU 版本的 PaddlePaddle：
    ```bash
    pip install paddlepaddle
    ```
  或使用以下命令安装 GPU 版本的 PaddlePaddle：
    ```bash
    pip install paddlepaddle-gpu
    ```
- **PaddleOCR：** 使用以下命令安装 PaddleOCR：
    ```bash
    pip install paddleocr
    ```
- **Tesseract-OCR：** 需要 Tesseract-OCR 进行图像预处理，请从 [https://github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract) 安装。
- **pandas：** 使用以下命令安装 pandas 用于数据处理：
    ```bash
    pip install pandas
    ```
- **tqdm：** 使用以下命令安装 tqdm 用于显示进度条：
    ```bash
    pip install tqdm
    ```

## 安装步骤

1. **克隆仓库：**

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

    （注意：将 `<repository-url>` 替换为您的仓库的实际 URL，将 `<repository-directory>` 替换为您的仓库目录的实际名称）。
2. **安装所需包：**

    ```bash
    pip install -r requirements.txt
    ```

## 使用方法

1. **放置 PNG 图像：**

    将您要处理的 PNG 图像文件放入项目根目录下的 `pics` 目录中。
2. **运行脚本：**

    从根目录执行主脚本：
    ```bash
    python src/main.py
    ```
3. **查找输出：**

    结果将保存在 `output` 目录中带有时间戳的 CSV 文件中。

## 代码说明

### `src/main.py`

- 这是应用程序的主要入口点。
- 它动态调整 Python 路径，以便可以相对导入其他模块。
- 它定义 `pics` 目录为输入目录，`output` 目录为 CSV 结果的输出目录。
- 该脚本遍历 `pics` 目录中的所有 PNG 文件。
- 它使用 `extract_text_from_image` 函数获取每个图像的文本内容。
- 结果被收集，转换为 pandas DataFrame，并保存为 `output` 目录中的 CSV 文件，并使用时间戳生成唯一的输出文件名。

### `src/ocr_utils.py`

- 此文件包含使用 PaddleOCR 进行光学字符识别 (OCR) 的工具函数。
- `extract_text_from_image` 函数执行以下操作：
    - 初始化 PaddleOCR 并支持中文。
    - 对提供的图像路径执行文本识别。
    - 将 OCR 结果连接成一个字符串。
    - 使用正则表达式提取特定字段，例如医院名称、患者姓名和诊断。
    - 返回结构化和提取的字段的字典。

### `src/file_utils.py`

- 此文件提供文件管理实用程序。
- `list_png_files` 函数执行以下操作：
    - 接收目录路径作为输入。
    - 列出指定目录中的所有文件。
    - 过滤列表，仅返回 PNG 文件。

## 关键提取数据字段

该脚本从医学文档图像中提取以下字段：

- **医院 (Hospital Name)：** 医院的名称。
- **患者姓名 (Patient Name)：** 患者的姓名。
- **性别 (Gender)：** 患者的性别。
- **年龄 (Age)：** 患者的年龄。
- **主诉 (Chief Complaint)：** 患者就诊的主要原因。
- **现病史 (Present Illness)：** 患者当前病情的病史。
- **既往史 (Past History)：** 患者的既往病史。
- **体格检查 (Physical Examination)：** 体格检查的结果。
- **过敏史 (Allergy History)：** 患者可能存在的任何过敏症。
- **个人史 (Personal History)：** 患者相关的个人详细信息。
- **生命体征 (Vital Signs)：** 患者的生命体征。
- **处理 (Treatment)：** 提供给患者的治疗方案。
- **辅助检查 (Auxiliary Examination)：** 执行的任何其他检查。
- **诊断 (Diagnosis)：** 医生做出的诊断。
- **处方 (Prescription)：** 提供给患者的处方。
- **就诊科室 (Department)：** 患者就诊的科室。
- **就诊医生 (Doctor)：** 接诊患者的医生姓名。
- **就诊日期 (Visit Date)：** 患者就诊的日期和时间。
- **复诊流水号 (Revisit ID)：** 复诊流水号。
- **更新日期 (Update Date)：** 文档更新的日期和时间。

## 使用提示

- 确保 PNG 图像质量足够好，以获得最佳 OCR 效果。
- 如有必要，调整 `ocr_utils.py` 中的正则表达式以匹配您的输入文档的特定结构。
- 当前的正则表达式是为医疗报告硬编码的，可能需要根据您的用例进行调整。
- Tesseract-OCR 用于图像预处理，因此请确保它已正确安装在您的系统上。

## 已知问题

- PaddleOCR 的准确性可能受到低质量图像的影响。预处理图像可能会提高结果。
- 提供的正则表达式是为典型的医疗报告量身定制的，可能无法准确匹配所有文档格式。可能需要进行自定义。

## 许可证

[License](LICENSE)