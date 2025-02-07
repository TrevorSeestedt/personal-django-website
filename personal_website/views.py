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