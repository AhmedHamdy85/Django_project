from django.contrib import admin

from .models import User, Project, Category, Donation

# Register your models here.


admin.site.register(User)
admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Donation)


