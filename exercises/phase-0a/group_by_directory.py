import os
from typing import List

def group_by_directory(file: List[str]) -> dict[str, List[str]]:
    """
    Group a list of file paths by their directory.

    Args:
        file (List[str]): A list of file paths.

    Returns:
        dict[str, List[str]]: A dictionary where the keys are directory paths and the values are lists of file names in those directories.
    """
    for f in file:
        dir_path = os.path.dirname(f)
        file_name = os.path.basename(f)
        if dir_path not in grouped_files:
            grouped_files[dir_path] = []
        grouped_files[dir_path].append(file_name)
