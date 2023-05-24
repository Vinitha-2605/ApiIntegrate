import requests
from config.config import get_config

class UserRepo:

 def get_repo(self, user_name, repo_name=None):
  headers = {'Accept': 'application/vnd.github.v3+json'}

  if repo_name is None:
   url = f"https://api.github.com/users/{user_name}"
  else:
   url = f"https://api.github.com/repos/{user_name}/{repo_name}"

  data =requests.get(url, headers=headers, auth=(user_name, get_config()))
  info = data.json()
  return info
