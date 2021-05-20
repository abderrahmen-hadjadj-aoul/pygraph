from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('workspace/', views.workspace_index, name="workspace_index"),
    path('workspace/create', views.workspace_create, name="workspace_create"),
]
