import requests
from config.config import get_config

class UserRepo:

 def get_github_user(self, user_name, logging):
   try:
    headers = {'Accept': 'application/vnd.github.v3+json'}
    url = f"https://api.github.com/users/{user_name}"
    logging.info("Retrieve the information from the url")
    data =requests.get(url, headers=headers)
    if data.status_code == 200:
     github_user_details = data.json()
     return github_user_details
    else:
     return "Unable to retrieve the data. Check the username is present or not"
   except Exception as ex:
    logging.error(ex)

 def get_github_gitlab_repo(self, user_name, logging, repo_name, project_id):
   try:
    headers = {'Accept': 'application/vnd.github.v3+json'}
    github_url = f"https://api.github.com/repos/{user_name}/{repo_name}"
    gitlab_url = f"https://gitlab.com/api/v4/projects/{project_id}"

    logging.info("Retrieve the information from the url") 
    github_repo_data =requests.get(github_url, headers=headers, auth=(user_name, get_config()['auth_token']))
    gitlab_repo_data =requests.get(gitlab_url, headers=headers)
    if github_repo_data.status_code == 200 and gitlab_repo_data.status_code == 200:
     return github_repo_data.json() , gitlab_repo_data.json()
    else:
     error_message = {"error":"Unable to retrieve the data. Check the reponame or projectid is present or not"}
     return error_message
   except Exception as ex:
    logging.error(ex)

