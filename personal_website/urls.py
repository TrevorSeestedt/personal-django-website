from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home_view, name='home'), 
    path('projects/', views.projects_view, name='projects'),

    #delete this
    path('create-superuser/', views.create_admin_user),
]