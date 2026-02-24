import httpx
import asyncio
from typing import List

async def send_ingest_payload (repo_url: str, files_indexed: int, tags: List[str]) -> None:
    """
    Sends a POST request to the ingest endpoint with the provided repository information.
    
    Args:
        repo_url (str): The URL of the repository being indexed.
        files_indexed (int): The number of files indexed in the repository.
        tags (List[str]): A list of tags associated with the repository.
    
    Returns:
        None: Prints the response from the server to the console.
    """

    url = "https://httpbin.org/post"
    payload = {
        "repo_url": repo_url,
        "files_indexed": files_indexed,
        "tags": tags
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json = payload)
        data = response.json()
        json_payload = data["json"]
        return {
            "repo_url": json_payload["repo_url"],
            "files_indexed": json_payload["files_indexed"],
            "tags": json_payload["tags"]
        }

async def main () -> None:
    print(await send_ingest_payload("https://github.com/abhidxt299/RoManOV", 150, ["python", "async"]))

if __name__ == "__main__":
    asyncio.run(main())