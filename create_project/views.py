from django.shortcuts import redirect, render
from create_project.forms import ProjectForm
from homepage.models import Category, FileFieldForm, Project, ProjectFile, User
from taggit.models import Tag


# Create your views here.


def create_project(request):
    print("create_project view called")  
    tags = Tag.objects.all()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        files = request.FILES.getlist('images')
        if form.is_valid():
            project = Project.objects.create(
                titele=form.cleaned_data['titele'],
                description=form.cleaned_data['description'],
                Category=Category.objects.get(id=form.cleaned_data['category']),
                totalTarget=form.cleaned_data['totalTarget'],
                endTime=form.cleaned_data['endTime'],
                user = User.objects.get(id=1)
            )

            tags = form.cleaned_data['tags']
            for tag in tags:
                project.tags.add(tag)

            for file in files:
                ProjectFile.objects.create(project=project, file=file)

            print("Project created successfully")
            return redirect('home')  
    
    else:
        form = ProjectForm()

    return render(request, 'create_project/project_form.html', {'form': form, 'tags': tags , 'categories': Category.objects.all()})

