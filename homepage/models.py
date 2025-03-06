from django import forms
from django.db import models
from taggit.managers import TaggableManager
from django.core.exceptions import ValidationError
# Create your models here.


class User (models.Model):
    firist_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    image = models.FileField(upload_to='static/images/')
    birthday = models.DateField(null=True, blank=True)
    facebook = models.URLField(max_length=100, null=True, blank=True)
    contury = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.firist_name



class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = [single_file_clean(data, initial)]
        return result


class FileFieldForm(forms.Form):
    file_field = MultipleFileField()


class Project (models.Model):
    titele = models.CharField(max_length=100)
    description = models.TextField()
    Category = models.ForeignKey('Category', on_delete=models.CASCADE)
    totalTarget = models.IntegerField()
    startTime = models.DateTimeField(auto_now_add=True)
    endTime = models.DateTimeField()
    ratings = models.JSONField(default=list) 

    def average_rating(self):
        if self.ratings:
            return sum(self.ratings) / len(self.ratings)
        return 0 
   
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    tags = TaggableManager()

    def __str__(self):
        return self.titele
    
    def total_donations(self):
        return self.donations.aggregate(models.Sum('amount'))['amount__sum'] or 0


class ProjectFile(models.Model):
    project = models.ForeignKey(Project, related_name='files', on_delete=models.CASCADE)
    file = models.FileField(upload_to='project_files/')

class Donation (models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, related_name='donations', on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
     return f"{self.user.firist_name} donated {self.amount}" 


class Category (models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Comment (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.TextField()
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text



class SelectedProject(models.Model):

    project = models.OneToOneField('Project', on_delete=models.CASCADE, unique=True)

    def clean(self):
        if SelectedProject.objects.count() >= 5 and not self.pk:
            raise ValidationError("You can only select up to 5 projects.")

    def save(self, *args, **kwargs):
        self.clean()  
        super().save(*args, **kwargs)

    def __str__(self):
        return self.project.titele


class Report(models.Model):
    REPORT_CHOICES = [
        ('spam', 'Spam'),
        ('offensive', 'Offensive Content'),
        ('other', 'Other'),
    ]
     
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    project = models.ForeignKey('Project', on_delete=models.CASCADE, null=True, blank=True)
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True, blank=True)
    reason = models.CharField(max_length=50, choices=REPORT_CHOICES)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.project:
            return f"Report on Project: {self.project.titele} by {self.user.firist_name}"
        elif self.comment:
            return f"Report on Comment by {self.user.firist_name}"
        return "Report"
