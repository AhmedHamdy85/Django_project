from django.shortcuts import render
from create_project.forms import ProjectForm
from homepage.models import Project


# Create your views here.


def create_project(request):
    print("create_project view called") 
    if request.method == 'POST':
        print("create_project view called with POST method")
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            print("create_project view called with POST method and form is valid")
            form.save()
    else:
        form = ProjectForm()
    return render(request, 'create_project/project_form.html', {'form': form})
