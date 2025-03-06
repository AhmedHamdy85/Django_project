from django.utils import timezone  
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Project, Comment, User, Donation, Category,SelectedProject
from django.db.models import Q
from taggit.models import Tag
# Create your views here.


def home(request):
    query = request.GET.get('q', '')
    category_filter = request.GET.get('category', '')

    projects = Project.objects.prefetch_related('tags')

    if query:
        projects = projects.filter(titele__icontains=query)
    if category_filter:
        projects = projects.filter(Category__id=category_filter)

    categories = Category.objects.all()
    projects = projects.order_by('-id')    # project 1 
    tags = Tag.objects.filter(project__in=projects).distinct()
    
    projects= projects.order_by('-id') # project 2
    latest_projects = projects[:3]
    selected_projects = SelectedProject.objects.select_related('project').all()
    print(selected_projects)


    return render(request, 'homepage/home.html', {
        'projects': projects,
        'query': query,
        'categories': categories,
        'selected_category': category_filter,
        'tags': tags,
        'latest_projects': latest_projects,
        'selected_projects': selected_projects,
    })


def project_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    comments = Comment.objects.filter(project=project).order_by('-id')
    donathions = Donation.objects.filter(project=project).order_by('-id')
    total_donations = project.total_donations() or 0
    status = "Not Achieved yet"
    needed_money = project.totalTarget - total_donations
    average_rating = project.average_rating()

    if project.endTime < timezone.now():
        status = "Expired"
    elif total_donations >= project.totalTarget:
        status = "Goal Achieved"
    else:
        status = "Not Achieved yet"
    
    delete_allowed = total_donations < (project.totalTarget * 0.25)


    return render(request, 'homepage/project_detail.html', {
        'project': project,
        'comments': comments,
        'donathions': donathions,
        'total_donations': total_donations,
        'status': status,
        'needed_money': needed_money,
        'delete_allowed': delete_allowed,
        'average_rating': round(average_rating, 1),
    })

def add_rating(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if request.method == 'POST':
        rating = request.POST.get('rating')

        if rating and rating.isdigit():
            rating = int(rating)
            if 1 <= rating <= 5:
                project.ratings.append(rating)  
                project.save(update_fields=['ratings']) 

    return redirect('project_detail', project_id=project_id)

def add_comment(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if request.method == 'POST':
        text = request.POST.get("comment", "").strip()
        if text:
            Comment.objects.create(
                user_id=request.user.id, project=project, text=text)

    return redirect(reverse('project_detail', args=[project_id]))


def add_donation(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if request.method == 'POST':
        amount = request.POST.get("amount", "").strip()
        if amount.isdigit():
            Donation.objects.create(
                user_id=request.user.id, project=project, amount=int(amount))

    return redirect(reverse('project_detail', args=[project_id]))
