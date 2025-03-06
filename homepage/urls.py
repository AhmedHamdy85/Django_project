from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('project_detail/<int:project_id>/', views.project_detail, name='project_detail'),
    path('add_comment/<int:project_id>/', views.add_comment, name='add_comment'),
    path('add_donation/<int:project_id>/', views.add_donation, name='add_donation'),
    path('add_rating/<int:project_id>/', views.add_rating, name='add_rating'),  
    ]
