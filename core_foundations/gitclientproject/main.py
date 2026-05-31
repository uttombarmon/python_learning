
import asyncio
from github_client import GitHubClient, NotFoundError, RateLimitError, GitHubError


def print_user(user: dict):
    print(f"\n  {user['name']} (@{user['username']})")
    print(f"  {user['bio']}")
    print(f"  {user['followers']} followers · {user['repos']} public repos")
    print(f"  {user['url']}")


def print_repos(repos: list[dict]):
    for repo in repos:
        stars = f"⭐ {repo['stars']}"
        lang  = repo['language']
        print(f"  {repo['name']:<35} {stars:<12} {lang}")


async def main():
    async with GitHubClient() as gh:

        # ── 1. Fetch a single user ─────────────────────────────────────────
        print("\n── Fetch user ────────────────────────────────")
        user = await gh.get_user("torvalds")
        print_user(user)

        # ── 2. Fetch their repos ───────────────────────────────────────────
        print("\n── Recent repos ──────────────────────────────")
        repos = await gh.get_repos("torvalds", limit=5)
        print_repos(repos)

        # ── 3. Search repos ────────────────────────────────────────────────
        print("\n── Search: 'python api client' ───────────────")
        results = await gh.search_repos("python api client", limit=5)
        print_repos(results)

        # ── 4. Fetch multiple users in parallel ────────────────────────────
        print("\n── Parallel fetch (asyncio.gather) ───────────")
        users = await gh.get_multiple_users([
            "gvanrossum", "karpathy", "sama", "nonexistent-user-xyz"
        ])
        for u in users:
            name = u.get('name')
            print(f"  {name} {u.get('followers', 0)} followers")

        # ── 5. Error handling demo ─────────────────────────────────────────
        print("\n── Error handling ────────────────────────────")
        try:
            await gh.get_user("this-user-definitely-does-not-exist-xyz")
        except NotFoundError as e:
            print(f"  NotFoundError caught: {e}")
        except RateLimitError as e:
            print(f"  RateLimitError caught: {e}")
        except GitHubError as e:
            print(f"  GitHubError caught: {e}")


if __name__ == "__main__":
    asyncio.run(main())