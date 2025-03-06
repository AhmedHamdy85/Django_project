from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('project_detail/<int:project_id>/', views.project_detail, name='project_detail'),
    path('add_comment/<int:project_id>/', views.add_comment, name='add_comment'),
    path('add_donation/<int:project_id>/', views.add_donation, name='add_donation'),
    path('add_rating/<int:project_id>/', views.add_rating, name='add_rating'), 
    path('report/project/<int:project_id>/', views.report_project, name='report_project'),
    path('report/comment/<int:comment_id>/', views.report_comment, name='report_comment'),
    path('comment/reply/<int:comment_id>/', views.add_reply, name='add_reply'), 
    ]
