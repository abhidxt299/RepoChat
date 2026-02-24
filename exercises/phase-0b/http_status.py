import httpx
import asyncio
from typing import List, Tuple

async def fetch_status(client: httpx.AsyncClient, owner: str, repo: str) -> None:
    """
    Fetches the HTTP status code for a given GitHub repository and prints a message based on the status code.

    Args:
        client (httpx.AsyncClient): The HTTP client to use for making requests.
        owner (str): The owner of the repository.
        repo (str): The name of the repository.

    Returns:
        None: Prints the status of the repository to the console.
    """
    
    url = f"https://api.github.com/repos/{owner}/{repo}"
    status_codes = {
        200: "Accessible",
        404: "Not Found",
        403: "Forbidden",
        429: "Too Many Requests",
        500: "Internal Server Error",
        502: "Bad Gateway"
    }
    
    try:
        response = await client.get(url)
        status_message = status_codes.get(response.status_code, "Unknown Status Code")
        print(f"{owner}/{repo} → {response.status_code} → {status_message}")

    except httpx.HTTPError as e:
        print(f"{owner}/{repo} → Error fetching repository information: {e}")

async def check_repo_statuses(test_cases: List[Tuple[str, str]]) -> None:
    """
    Checks the HTTP status codes for a list of GitHub repositories and prints the results.
    
    Args:
        test_cases (List[Tuple[str, str]]): A list of tuples containing the owner and repository name.
    
    Returns:
        None: Prints the status of each repository to the console.
    """

    header = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "abhidxt299"
    }

    async with httpx.AsyncClient(headers = header) as client:
        tasks = [fetch_status(client, owner, repo) for owner, repo in test_cases]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    test_cases = [
        ("tiangolo", "fastapi"),          # public, exists
        ("torvalds", "private-repo-xyz"), # doesn't exist
        ("django", "django"),             # public, exists
        ("octocat", "Hello-World"),       # public, exists
        ("nonexistent-user", "repo"),     # user doesn't exist
        ("python", "cpython"),            # public, exists
        ("octocat", "nonexistent-repo")   # user exists, repo doesn't exist
    ]
    asyncio.run(check_repo_statuses(test_cases))