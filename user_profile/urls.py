from django.urls import path
from .views import update_profile, user_profile

urlpatterns = [
    path('<int:user_id>/', user_profile, name='user_profile'),
    path('profile/<int:user_id>/update/', update_profile, name='update_profile'),  

]
