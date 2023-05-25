from django.urls import path
from . import views

urlpatterns = [
    path('git/<str:user_name>/', views.get_repo),
    path('git/<str:user_name>/<str:repo_name>/<project_id>', views.compare_repo)
]