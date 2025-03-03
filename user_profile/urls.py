from django.urls import path
from .views import delete_profile, update_profile, user_profile
from homepage.views import project_detail

urlpatterns = [
    path('<int:user_id>/', user_profile, name='user_profile'),
    path('profile/<int:user_id>/update/', update_profile, name='update_profile'),  
    path('profile/<int:user_id>/delete/', delete_profile, name='delete_profile'),
    path('project_detail/<int:project_id>/', project_detail, name='project_detail'),


]
