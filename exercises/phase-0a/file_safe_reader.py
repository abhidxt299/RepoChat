def read_file_safe (file_path: str) -> str | None:
    """
    Read the contents of a file safely, handling potential exceptions.

    Args:
        file_path (str): The path to the file to be read.

    Returns:
        str | None: The contents of the file if successful, otherwise None.
    """
    try:
        with open(file_path, 'r', encoding = 'utf-8') as f:
            print(f"Successfully read file: {file_path}")
            return f.read()
    
    except FileNotFoundError:
        return "File not found."
    
    except PermissionError:
        return "Permission denied."

    except UnicodeDecodeError:
        return "File is not a text file or contains invalid characters."

# Example usage:
file_content_python = read_file_safe("app/main.py")
print(file_content_python)

file_content_readme = read_file_safe("README.md")
print(file_content_readme)