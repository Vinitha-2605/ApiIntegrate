from django.shortcuts import render
from .services import git_service
from django.http import HttpResponse
from log import log

def get_repo(request, user_name, repo_name=None):
   logger = log.initialize_log()
   service = git_service.UserRepo()
   data = service.get_repo(user_name,  logger, repo_name)
   git_url = data.get('clone_url')
   if git_url is None:
    logger.error( "No Git is present")
    return HttpResponse("No data is present")
   else:
    logger.info(f"Git url- {git_url}")
    return render(request, "api_integrate/view.html", {
        "gitdetails": data,
        "git": git_url,
        "repository": repo_name})
       
