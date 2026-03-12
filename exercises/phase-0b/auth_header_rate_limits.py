import os
import httpx
import asyncio
from dotenv import load_dotenv

load_dotenv()

async def check_rate_limit(token: str | None = None) -> dict:
    """
    Check the GitHub API rate limit for both authenticated and unauthenticated requests.
    
    Args:
        token (str | None): The GitHub personal access token for authentication. If None, the request will be unauthenticated.
    
    Returns:
        dict: A dictionary containing the rate limit information, including the total limit, remaining requests, and whether the request was authenticated. 
    """

    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "abhidxt299"
    }

    if token:
        headers["Authorization"] = f"Bearer {token}"
    
    async with httpx.AsyncClient (headers = headers) as client:
        response = await client.get("https://api.github.com/rate_limit")
        data = response.json()
        core = data["resources"]["core"]
        return {
            "limit": core["limit"],
            "remaining": core["remaining"],
            "authenticated": token is not None
        }

async def main() -> None:
    print("Checking the rate limit without authentication: ")
    print(await check_rate_limit(token = None))
    print("\nChecking the rate limit with authentication: ")
    print(await check_rate_limit(token = os.getenv("GITHUB_TOKEN")))

if __name__ == "__main__":
    asyncio.run(main())