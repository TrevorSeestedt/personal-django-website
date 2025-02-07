from django.shortcuts import render
from .models import Projects

# Create your views here.
def home_view(request):
    return render(request, 'personal_website/home.html')

def projects_view(request):
    projects = Projects.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'personal_website/projects.html', context)


#delete this 
from django.contrib.auth.models import User
from django.http import HttpResponse
def create_admin_user(request):
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(
            "TrevorSeestedt1",        # username
            "seestedttrevor@gmail.com", # email
            "Trevor2002!!"   # password
        )
        return HttpResponse("Superuser created successfully.")
    return HttpResponse("Superuser already exists.")