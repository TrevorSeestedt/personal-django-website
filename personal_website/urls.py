from django.urls import path
from . import views 

from .views import create_admin_user

urlpatterns = [
    path('', views.home_view, name='home'), 
    path('projects/', views.projects_view, name='projects'),

    path('create-superuser/', create_admin_user),
]