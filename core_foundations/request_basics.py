import os;
from dotenv import load_dotenv
import requests;
import json;

load_dotenv()

api_url = os.getenv("API_URL")
if not api_url:
  print("Api Url not get")
  raise ValueError("API_URL is missing — check your .env file")

response = requests.get("https://api.github.com/users/torvalds")
if response.status_code != 200:
  print("Api not working!")
else:
  info = response.json()
  # print(info)


raw = '''
{
  "status": "success",
  "data": {
    "user": {
      "id": 42,
      "email": "uttom@example.com"
    },
    "subscription": {
      "plan": "pro",
      "expires": "2025-12-31"
    }
  },
  "errors": []
}
'''

result = json.loads(raw)

# Drilling into nested keys
email = result["data"]["user"]["email"]
plan  = result["data"]["subscription"]["plan"]

raw = '''
{
  "status": "success",
  "data": {
    "user": {
      "id": 42,
      "email": "uttom@example.com"
    },
    "subscription": {
      "plan": "pro",
      "expires": "2025-12-31"
    }
  },
  "errors": []
}
'''

result = json.loads(raw)

# Drilling into nested keys
email = result["data"]["user"]["email"]
plan  = result["data"]["subscription"]["plan"]
# Risky — crashes if key doesn't exist
# name = result["data"]["user"]["name"]   # KeyError!

# Safe — returns None (or your default) if missing
name    = result["data"]["user"].get("name")
country = result["data"]["user"].get("country", "Unknown")

payload = {
    "model": "gpt-4",
    "messages": [
        {"role": "user", "content": "Hello!"}
    ],
    "temperature": 0.7
}
send_data = json.dumps(payload, indent=2)
print(send_data)

print(payload["messages"])
print(payload["messages"][0]["role"])
print(payload["messages"][0].get("name"))