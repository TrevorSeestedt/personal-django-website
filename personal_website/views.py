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


# delete this after deployed  
from django.contrib.auth.models import User 
from django.http import HttpResponse
def create_admin(request): 
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser("steele2002", "admin@example.com", "8iA3y6@<otOr")
        return HttpResponse("Superuser created successfully.")
    return HttpResponse("Superuser already exists.")
