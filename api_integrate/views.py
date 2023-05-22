from django.shortcuts import render
from .services import git_service

def get_repo(request, user_name, repo_name=None):
    service = git_service.UserRepo()
    data = service.get_repo(user_name, repo_name)
    git_url = data.get('clone_url')
    return render(request, "api_integrate/view.html", {
        "gitdetails": data,
        "git": git_url,
        "repository": repo_name})
