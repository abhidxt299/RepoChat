from typing import List

files = ["main.py", "styles.py", "notes.py", "script.py", "image.png", "config.yaml", "README.md", "data.csv", "archive.zip", "presentation.pptx"]
chunks = ["short", "this is a longer chunk that exceeds one hundred characters in total length so it should be trimmed down nicely"]
paths = ["src/main.py", "src/utils.py", "src/models/user.py", "tests/test_main.py", "README.md", "requirements.txt"]

def ends_with_py (file: List[str]) -> dict[str, List[str]]:
    """
    Part A
    # Rewrite this:
    result = []
    for f in file:
        if f.endswith(".py"):
        result.append(f.upper())

    # As one line:
    result = [...]
    """
    
    result = [f.upper() for f in file if f.endswith(".py")]
    return result

def chunking (chunks: List[str]) -> dict[str, List[str]]:
    """
    Part B
    # Rewrite this:
    result = []
    for chunk in chunks:
        if len(chunk) > 100:
            result.append(chunk[:100])
    
    # As one line:
    result = [...]
    """

    result = [chunk[:100] for chunk in chunks if len(chunk) > 100]
    return result

def find_file_name (paths: List[str]) -> str:
    """
    Part C
    # Rewrite this:
    result = []
    for path in paths:
        parts = path.split("/")
        result.append(parts[-1])

    # As one line — extract just the filename from each path:
    result = [...]
    """

    result = [path.split("/")[-1] for path in paths]
    return result

ends_with_py_result = ends_with_py(files)
print(ends_with_py_result)

chunking_result = chunking(chunks)
print(chunking_result)

file_names_result = find_file_name(paths)
print(file_names_result)