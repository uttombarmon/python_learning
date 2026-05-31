import requests
import os
from dotenv import load_dotenv

headers = {
    "Authorization": f"Bearer {os.getenv('API_KEY')}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

response = requests.get("https://api.github.com/users/torvalds")

print(response.status_code)   # 200
print(response.json())        # full dict

params = {
    "q": "python api client",
    "sort": "stars",
    "per_page": 5
}

response = requests.get("https://api.github.com/search/repositories", params=params)
results = response.json()

for repo in results["items"]:
    print(repo["full_name"], "⭐", repo["stargazers_count"])

payload = {
    "title": "Fix login bug",
    "body": "Users can't log in after password reset",
    "labels": ["bug", "urgent"]
}

response = requests.post(
    "https://api.github.com/repos/myuser/myrepo/issues",
    headers=headers,
    json=payload       # automatically sets Content-Type and calls json.dumps()
)

new_issue = response.json()
print(new_issue.get("number"))   # issue number created

import requests
from requests.exceptions import HTTPError, ConnectionError, Timeout

def fetch_user(username):
    try:
        response = requests.get(
            f"https://api.github.com/users/{username}",
            timeout=5     # always set this — never wait forever
        )
        response.raise_for_status()   # raises HTTPError for 4xx/5xx
        return response.json()

    except HTTPError as e:
        status = e.response.status_code
        if status == 404:
            print(f"User '{username}' not found")
        elif status == 401:
            print("Bad API key — check your .env")
        elif status == 429:
            print("Rate limited — slow down requests")
        else:
            print(f"HTTP error: {status}")

    except ConnectionError:
        print("No internet or DNS failed")

    except Timeout:
        print("Request took too long")

    return None
session = requests.Session()
session.headers.update({
    "Authorization": f"Bearer {os.getenv('API_KEY')}",
    "Accept": "application/json"
})

# Headers are sent automatically on every call
user     = session.get("https://api.example.com/user").json()
projects = session.get("https://api.example.com/projects").json()
session.post("https://api.example.com/log", json={"event": "login"})

session.close()   # or use as a context manager (see below)