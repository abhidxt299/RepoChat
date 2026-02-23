class FileChunk:

    def __init__ (self, path: str, content: str, chunk_index: int):
        self.path = path
        self.content = content
        self.chunk_index = chunk_index
    
    def preview (self) -> str:
        """
        Return a preview of the file chunk, including the file path and the first few characters of the content.

        Returns:
            str: A string containing the file path and a preview of the content.
        """

        result = f"File: {self.path}\nPreview: {self.content[:self.chunk_index]}"
        result += "..." if len(result) > self.chunk_index else ""
        return result
    
    def word_count (self) -> int:
        """
        Count the number of words in the file chunk content.

        Returns:
            int: The number of words in the content.
        """

        result = len(self.content.split())
        return result
    
    def __repr__ (self) -> str:
        """
        prints as FileChunk(path='src/main.py', index=0, words=42)
        """

        return f"FileChunk(path='{self.path}', index={self.chunk_index}, words={self.word_count()})"

# Example usage:
chunk = FileChunk(
    path="src/main.py",
    content="def authenticate(user, password):\n    if not user:\n        raise ValueError('User required')\n    return check_db(user, password)",
    chunk_index=0
)

print(chunk.preview())
print(chunk.word_count())
print(chunk)