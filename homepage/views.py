from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Comment,User

# Create your views here.


def home(request):
    projects = Project.objects.all()
    return render(request, 'homepage/home.html', {'projects': projects})


def project_detail(request, project_id):
    project=Project.objects.get(id=project_id)
    comments = Comment.objects.filter(project=project).order_by('-id')  # Latest comments first

    return render(request, 'homepage/project_detail.html', {'project': project, 'comments': comments})

def add_comment(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if request.method == 'POST':
        text = request.POST.get("comment", "").strip()
        if text:  
            Comment.objects.create(user_id=request.user.id, project=project, text=text)
            

    comments = Comment.objects.filter(project=project).order_by('-id')  # Latest comments first


    return render(request, 'homepage/project_detail.html', {'project': project, 'comments': comments})