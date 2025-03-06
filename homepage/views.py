from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Project, Comment, Report, User, Donation, Category, SelectedProject
from django.db.models import Q, Count
from taggit.models import Tag
from django.contrib import messages
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
    projects = projects.order_by('-id')
    tags = Tag.objects.filter(project__in=projects).distinct()

    latest_projects = projects[:3]
    selected_projects = SelectedProject.objects.select_related('project').all()
    # print(selected_projects)

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
    project = get_object_or_404(Project, id=project_id)
    comments = Comment.objects.filter(project=project, parent=None).order_by('-id')
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


    # Fetch similar projects based on tags
    similar_projects = Project.objects.filter(
        tags__in=project.tags.all()  # Match any tags from the current project
    ).exclude(id=project.id).distinct().annotate(
        common_tags=Count('tags')
        # Order by the most common tags and limit to 4
    ).order_by('-common_tags', '-id')[:4]

    return render(request, 'homepage/project_detail.html', {
        'project': project,
        'comments': comments,
        'donathions': donathions,
        'total_donations': total_donations,
        'status': status,
        'needed_money': needed_money,
        'delete_allowed': delete_allowed,
        'average_rating': round(average_rating, 1),
        'similar_projects': similar_projects
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


def report_project(request,project_id):
    user = User.objects.get(id=request.user.id) 
    project= get_object_or_404(Project, id=project_id)

    if request.method == 'POST':
        reason = request.POST.get("reason", "")
        description = request.POST.get('description', '')

        Report.objects.create(user=user, project=project, reason=reason, description=description)
        messages.success(request, "Project reported successfully.")
        
    return redirect('project_detail', project_id=project_id)


def report_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    user = User.objects.get(id=request.user.id) 

    if request.method == 'POST':
        reason = request.POST.get('reason')
        description = request.POST.get('description', '')

        Report.objects.create(user=user, comment=comment, reason=reason, description=description)
        messages.success(request, "Comment reported successfully.")

    return redirect('project_detail', project_id=comment.project.id)


def add_reply(request, comment_id):

    if request.method == 'POST':
        user = User.objects.get(id=request.user.id) 
        parent_comment = get_object_or_404(Comment, id=comment_id)
        text = request.POST.get('reply', '').strip()
        if text:
            Comment.objects.create(
                user=user,
                project=parent_comment.project,
                text=text, 
                parent=parent_comment)

    return redirect('project_detail', project_id=parent_comment.project.id)
    
 

