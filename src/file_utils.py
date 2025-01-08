# src/file_utils.py
import os

def list_png_files(directory):
    """
    List all PNG files in a directory.
    :param directory: Path to the directory
    :return: List of PNG file paths
    """
    return [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith(".png")]
