from django.shortcuts import render
from .models import Project

# Create your views here.


def home(request):
    return render(request, 'homepage/home.html')

def project_detail(request, project_id):
    # project=Project.objects.get(id=project_id)
    return render(request, 'homepage/project_detail.html', {'project_id':project_id})

