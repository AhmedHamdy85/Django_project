from django.shortcuts import render
from .models import Project

# Create your views here.


def home(request):
    context = {
        "titele": "home",
        "description": 25,
        "Salary": 2000
    }
    return render(request, 'homepage/home.html', context)


def project_detail(request, project_id):
    # project=Project.objects.get(id=project_id)
    return render(request, 'homepage/project_detail.html', {'project_id': project_id})
