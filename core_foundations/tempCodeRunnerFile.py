response = httpx.get("https://api.github.com/users/torvalds")
print(response.status_code)
print(response.json())