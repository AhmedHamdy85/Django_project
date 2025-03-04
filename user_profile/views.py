from django.shortcuts import render, redirect, get_object_or_404
from homepage.models import Donation, User,Project
# Create your views here.

def user_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    projects = Project.objects.filter(user=user)
    donations = Donation.objects.filter(user=user)  
    return render(request, 'user_profile/profile.html', {'user': user, 'projects': projects,'donations': donations})

def update_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == "POST":
        user.firist_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.phone = request.POST.get('phone')
        user.birthday = request.POST.get('birthday') or None
        user.facebook = request.POST.get('facebook') or None
        user.contury = request.POST.get('country') or None
        
        if 'image' in request.FILES:
            user.image = request.FILES['image']

        user.save()
        return redirect('user_profile', user_id=user.id)

    return render(request, 'user_profile/update_profile.html', {'user': user})


def delete_profile(request, user_id): 
    user = get_object_or_404(User, id=user_id)

    if request.method == "POST":
        user.delete()
        return redirect('home')  

    return redirect('user_profile', user_id=user_id)  

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'user_profile/project_detail.html', {'project': project})

def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == "POST":
        project.delete()
        return redirect('home')