import asyncio
import time
from typing import List

async def fake_fetch(url: str) -> str:
    """
    Simulates fetching data from a URL by sleeping for 1 second.
    Args:
        url (str): The URL to fetch data from.
    Returns:
        str: A message indicating that data has been fetched from the URL.
    """

    await asyncio.sleep(1)
    return f"Fetched data from {url} \n"

async def fetch_all_sequentials(urls: List[str]) -> List[str]:
    """
    Fetch data from a list of URLs sequentially.
    Args:
        urls (List[str]): A list of URLs to fetch data from.
    Returns:
        List[str]: A list of results from fetching each URL.
    """
    
    results = []
    for url in urls:
        result = await fake_fetch(url)
        results.append(result)
    return results

async def fetch_all_concurrents(urls: List[str]) -> list[str]:
    """
    Fetch data from a list of URLs concurrently.
    Args:
        urls (List[str]): A list of URLs to fetch data from.
    Returns:
        List[str]: A list of results from fetching each URL.
    """
    
    results = await asyncio.gather(*(fake_fetch(url) for url in urls))
    return results

urls = ["https://api.github.com/repos/octocat/Hello-World", "https://api.github.com/repos/octocat/Spoon-Knife", "https://api.github.com/repos/octocat/linguist", "https://api.github.com/repos/octocat/atom", "https://api.github.com/repos/octocat/visual-studio-code"]
start_time = time.time()
results = asyncio.run(fetch_all_sequentials(urls))
print(f"Time taken to fetch all URLs sequentially: {time.time() - start_time:.2f} seconds")
print(results)

start_time = time.time()
results = asyncio.run(fetch_all_concurrents(urls))
print(f"Time taken to fetch all URLs concurrently: {time.time() - start_time:.2f} seconds")
print(results)