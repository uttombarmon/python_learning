import httpx
import os
from dotenv import load_dotenv
import asyncio

# requests:  requests.get(url)
# httpx:     httpx.get(url)   ← same

# response = httpx.get("https://api.github.com/users/torvalds")
# print(response.status_code)
# print(response.json())

# requests uses: requests.Session()
# httpx uses:    httpx.Client()

with httpx.Client(
    base_url="https://api.github.com",
    headers={"Authorization": f"Bearer {os.getenv('API_KEY')}"},
    timeout=5
) as client:
    user  = client.get("/users/torvalds").json()
    repos = client.get("/users/torvalds/repos").json()

async def fetch_user(username):
    async with httpx.AsyncClient(
        base_url="https://api.github.com",
        timeout=5
    ) as client:
        response = await client.get(f"/users/{username}")
        response.raise_for_status()
        return response.json()

# run it
user = asyncio.run(fetch_user("torvalds"))
print(user["name"])

async def fetch_user(client, username):
    response = await client.get(f"/users/{username}")
    response.raise_for_status()
    return response.json()

async def fetch_all():
    usernames = ["torvalds", "gvanrossum", "yann-lecun", "karpathy", "sama"]

    async with httpx.AsyncClient(base_url="https://api.github.com", timeout=5) as client:
        tasks = [fetch_user(client, u) for u in usernames]
        users = await asyncio.gather(*tasks)   # all 5 fire simultaneously

    for user in users:
        print(user["name"], "—", user["public_repos"], "repos")

asyncio.run(fetch_all())

async def safe_fetch(client):
    username = "torvalds"
    try:
        response = await client.get(f"/users/{username}")
        response.raise_for_status()
        return response.json()

    except httpx.HTTPStatusError as e:
        print(f"HTTP {e.response.status_code} for {username}")

    except httpx.TimeoutException:
        print(f"Timeout fetching {username}")

    except httpx.RequestError as e:
        print(f"Connection error: {e}")

    return None
asyncio.run(safe_fetch())