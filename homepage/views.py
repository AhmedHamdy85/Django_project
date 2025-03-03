from django.shortcuts import render
from .models import Project

# Create your views here.


def home(request):
    projects = Project.objects.all()
    return render(request, 'homepage/home.html', {'projects': projects})


def project_detail(request, project_id):
    project=Project.objects.get(id=project_id)
    return render(request, 'homepage/project_detail.html', {'project': project})
