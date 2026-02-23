import os
from typing import List

VALID_EXTENSIONS = {".ipynb", ".py", ".java", ".cpp", ".js", ".html", ".css", ".md", ".txt", ".json", ".xml", ".yml", ".yaml", ".sh", ".go", ".rb", ".erb"}

def filter_code_files(file: List[str]) -> List[str]:
    """
    Filter a list of file paths to include only those with valid code extensions.

    Args:
        file (List[str]): A list of file paths.

    Returns:
        List[str]: A list of file paths that have valid code extensions.
    """
    
    return [f for f in file if os.path.splitext(f)[1] in VALID_EXTENSIONS]

my_files = ["main.py", "styles.css", "notes.txt", "script.js", "image.png", "config.yaml", "README.md", "data.csv", "archive.zip", "presentation.pptx"]
test_files = []
filtered = filter_code_files(my_files)
filtered_empty = filter_code_files(test_files)
print(filtered)
print(filtered_empty)