import httpx
import asyncio

async def get_repo_summary (owner: str, repo: str) -> None:
    """
    Fetches the summary of a GitHub repository, including its description, star count, fork count, primary language, open issues count, and default branch.
    
    Args:
        owner (str): The owner of the repository.
        repo (str): The name of the repository.
    
    Returns:
        None: Prints the repository summary to the console.
    """

    url = f"https://api.github.com/repos/{owner}/{repo}"

    header = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "abhidxt299"
    }

    try:
        async with httpx.AsyncClient(headers = header) as client:
            response = await client.get(url)
            required_params = {
                "description": response.json().get("description", {}),
                "stargazers_count": response.json().get("stargazers_count", {}),
                "forks_count": response.json().get("forks_count", {}),
                "language": response.json().get("language", {}),
                "open_issues_count": response.json().get("open_issues_count", {}),
                "default_branch": response.json().get("default_branch", {})
            }
            print(required_params)

    except httpx.HTTPError as e:
        print(f"Error fetching repo summary: {e}")

if __name__ == "__main__":
    owner = "tiangolo"
    repo = "fastapi"
    asyncio.run(get_repo_summary(owner, repo))
