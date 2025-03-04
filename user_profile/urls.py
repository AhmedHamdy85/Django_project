from django.urls import path
from .views import delete_profile, delete_project, update_profile, user_profile
from homepage.views import project_detail

urlpatterns = [
    path('<int:user_id>/', user_profile, name='user_profile'),
    path('profile/<int:user_id>/update/', update_profile, name='update_profile'),  
    path('profile/<int:user_id>/delete/', delete_profile, name='delete_profile'),
    path('project_detail/<int:project_id>/', project_detail, name='project_detail'),
    path('delete_project/<int:project_id>/', delete_project, name='delete_project'),

]
