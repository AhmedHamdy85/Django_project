from django.shortcuts import render, redirect, get_object_or_404
from homepage.models import User
# Create your views here.

def user_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'user_profile/profile.html', {'user': user})

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
