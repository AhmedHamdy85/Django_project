from django.contrib import admin

from .models import User, Project, Category, Donation, Comment, SelectedProject

# Register your models here.


admin.site.register(User)
admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Donation)
admin.site.register(Comment)
admin.site.register(SelectedProject)


