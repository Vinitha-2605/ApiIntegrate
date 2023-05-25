from django.shortcuts import render
from .services import git_service
from log import log

def get_repo(request, user_name):
   logger = log.initialize_log()
   service = git_service.UserRepo()
   github_repo = service.get_github_user(user_name,  logger)
   return render(request, "api_integrate/view.html", {
        "githubrepo": github_repo,
      })

def compare_repo(request,  user_name, repo_name, project_id):
  logger = log.initialize_log()
  service = git_service.UserRepo()
  github_repo = service.get_github_gitlab_repo(user_name,  logger, repo_name, project_id)
  if 'error' in github_repo and github_repo['error'] is not None:
      message = f"{github_repo['error']}"  
      return render(request, "api_integrate/view.html", {
        "errormessage": message,
      })
  elif github_repo[0]['name'] != github_repo[1]['name']:
     message = f"Github {repo_name} and Gitlab {project_id} repository is not same"
     return render(request, "api_integrate/view.html", {
        "errormessage": message,
      })
  else: 
   github_url = github_repo[0]['clone_url']
   gitlab_url = github_repo[1]['http_url_to_repo']
   github_star = github_repo[0]['stargazers_count']
   gitlab_star = github_repo[1]['star_count']
   if github_star > gitlab_star:
      message = f"Github repository {repo_name} have higher rating with {github_star} *"
   else:
      message = f"Gitlab repository {project_id} have high rating with {gitlab_star} *"
   logger.info(f"Github star- {github_star}")
   logger.info(f"Gitlab star- {gitlab_star}")
  return render(request, "api_integrate/view.html", {
        "git": github_url,
        "gitlab": gitlab_url,
        "messages": message,
        "repository": repo_name})