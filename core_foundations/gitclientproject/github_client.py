"""
GitHub API client
Covers: .env secrets, httpx, error handling, JSON parsing
"""

import os
import asyncio
from dotenv import load_dotenv
import httpx

load_dotenv()


# ── Custom exceptions ──────────────────────────────────────────────────────────

class GitHubError(Exception):
    """Base error for all client failures."""
    pass

class NotFoundError(GitHubError):
    pass

class AuthError(GitHubError):
    pass

class RateLimitError(GitHubError):
    pass


# ── Client ─────────────────────────────────────────────────────────────────────

class GitHubClient:
    """
    Async GitHub API client.

    Usage:
        async with GitHubClient() as gh:
            user = await gh.get_user("torvalds")
    """

    BASE_URL = "https://api.github.com"

    def __init__(self, token: str | None = None):
        self.token = token or os.getenv("GITHUB_TOKEN")
        if not self.token:
            raise AuthError("GITHUB_TOKEN missing — add it to your .env file")

        self._client: httpx.AsyncClient | None = None

    # ── Context manager ────────────────────────────────────────────────────────

    async def __aenter__(self):
        self._client = httpx.AsyncClient(
            base_url=self.BASE_URL,
            headers={
                "Authorization": f"Bearer {self.token}",
                "Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28",
            },
            timeout=10,
        )
        return self

    async def __aexit__(self, *args):
        if self._client:
            await self._client.aclose()

    # ── Internal helpers ───────────────────────────────────────────────────────

    async def _get(self, path: str, params: dict | None = None) -> dict | list:
        """Make a GET request and return parsed JSON. Raises on errors."""
        try:
            response = await self._client.get(path, params=params)
            return self._handle_response(response)

        except httpx.TimeoutException:
            raise GitHubError(f"Request timed out: {path}")

        except httpx.RequestError as e:
            raise GitHubError(f"Connection error: {e}")

    def _handle_response(self, response: httpx.Response) -> dict | list:
        """Map HTTP status codes to typed exceptions, return JSON on success."""
        if response.status_code == 200:
            return response.json()

        # Try to extract GitHub's error message from the body
        try:
            message = response.json().get("message", "Unknown error")
        except Exception:
            message = response.text

        if response.status_code == 401:
            raise AuthError(f"Bad token — {message}")
        if response.status_code == 403:
            raise RateLimitError(f"Rate limited or forbidden — {message}")
        if response.status_code == 404:
            raise NotFoundError(f"Not found — {message}")

        # Catch-all for other 4xx/5xx
        raise GitHubError(f"HTTP {response.status_code}: {message}")

    # ── Public methods ─────────────────────────────────────────────────────────

    async def get_user(self, username: str) -> dict:
        """Fetch a GitHub user's profile."""
        data = await self._get(f"/users/{username}")
        # Return only the fields we care about (clean JSON parsing)
        return {
            "username":   data.get("login"),
            "name":       data.get("name"),
            "bio":        data.get("bio"),
            "followers":  data.get("followers", 0),
            "repos":      data.get("public_repos", 0),
            "url":        data.get("html_url"),
        }

    async def get_repos(self, username: str, limit: int = 5) -> list[dict]:
        """Fetch a user's most recently updated repos."""
        data = await self._get(
            f"/users/{username}/repos",
            params={"sort": "updated", "per_page": limit},
        )
        return [
            {
                "name":        repo.get("name"),
                "description": repo.get("description", "—"),
                "stars":       repo.get("stargazers_count", 0),
                "language":    repo.get("language", "—"),
                "url":         repo.get("html_url"),
            }
            for repo in data
        ]

    async def search_repos(self, query: str, limit: int = 5) -> list[dict]:
        """Search GitHub repositories."""
        data = await self._get(
            "/search/repositories",
            params={"q": query, "sort": "stars", "per_page": limit},
        )
        return [
            {
                "name":    repo.get("full_name"),
                "stars":   repo.get("stargazers_count", 0),
                "language": repo.get("language", "—"),
                "url":     repo.get("html_url"),
            }
            for repo in data.get("items", [])
        ]

    async def get_multiple_users(self, usernames: list[str]) -> list[dict]:
        """Fetch several users in parallel using asyncio.gather."""
        tasks = [self.get_user(u) for u in usernames]
        results = await asyncio.gather(*tasks, return_exceptions=True)

        output = []
        for username, result in zip(usernames, results):
            if isinstance(result, Exception):
                print(f"  ⚠ Failed to fetch '{username}': {result}")
            else:
                output.append(result)
        return output