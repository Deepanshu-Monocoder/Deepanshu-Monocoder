import requests
from pathlib import Path

USERNAME = "Deepanshu-Monocoder"

query = """
query($login:String!){
  user(login:$login){
    contributionsCollection{
      contributionCalendar{
        weeks{
          contributionDays{
            contributionCount
          }
        }
      }
    }
  }
}
"""

response = requests.post(
    "https://api.github.com/graphql",
    headers={
        "Authorization": "Bearer YOUR_GITHUB_TOKEN"
    },
    json={
        "query": query,
        "variables": {
            "login": USERNAME
        }
    },
)

Path("data/contributions.json").write_text(response.text)

print("Contribution data saved!")