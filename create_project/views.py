from django.shortcuts import render
from create_project.forms import ProjectForm
from homepage.models import Project
from taggit.models import Tag


# Create your views here.


def create_project(request):
    print("create_project view called") 
    if request.method == 'POST':
        tags = Tag.objects.all()
        form = ProjectForm(request.POST, request.FILES)
        file = request.FILES.getlist('image')
        if form.is_valid():
            print("create_project view called with POST method and form is valid")
            form.save()
    else:
        form = ProjectForm()
        tags = Tag.objects.all()
    return render(request, 'create_project/project_form.html', {'form': form, 'tags': tags})
