import httpx
import asyncio
from typing import List, Tuple

async def fetch_status(client: httpx.AsyncClient, owner: str, repo: str) -> None:
    url = f"https://api.github.com/repos/{owner}/{repo}"
    try:
        response = await client.get(url)
        print(f"{owner}/{repo} → {response.status_code} → {response.reason_phrase}")
    except httpx.HTTPError as e:
        print(f"{owner}/{repo} → Error fetching repository information: {e}")

async def check_repo_statuses(test_cases: List[Tuple[str, str]]) -> None:
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