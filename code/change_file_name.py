"""
use this to change the file name
"""
import os
from pathlib import Path
folder_path = 'D:\\D\\latex_workspace\\sudoku\\code'
files = os.listdir()
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith('.java'):
            rename = file
            new_extension = '.txt'
            pre, ext = os.path.splitext(rename)
            os.rename(rename, pre + new_extension)
            # os.remove(file)
            