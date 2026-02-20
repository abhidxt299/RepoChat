from typing import List

def group_by_directory(file_path: List[str]) -> dict[str, List[str]]:
    """
    Group a list of file paths by their directory.

    Args:
        file (List[str]): A list of file paths.

    Returns:
        dict[str, List[str]]: A dictionary where the keys are directory paths and the values are lists of file names in those directories.
    """
    grouped_files = {}

    for f in file_path:
        dir_path_parts = f.split('/')

        if len(dir_path_parts) > 1:
            key = dir_path_parts[0]
        else:
            key = "/"
        
        if key not in grouped_files:
            grouped_files[key] = []
        
        grouped_files[key].append(f)
        
    return grouped_files

file_paths = [
    "src/main.py",
    "src/utils.py",
    "src/models/user.py",
    "tests/test_main.py",
    "README.md",
    "requirements.txt",
]
result = group_by_directory(file_paths)
print(result)