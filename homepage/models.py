from django.db import models
from taggit.managers import TaggableManager
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


class Project (models.Model):
    titele = models.CharField(max_length=100)
    description = models.TextField()
    image = models.FileField(upload_to='static/images/', null=True, blank=True)
    Category = models.ForeignKey('Category', on_delete=models.CASCADE)
    totalTarget = models.IntegerField()
    startTime = models.DateTimeField(auto_now_add=True)
    endTime = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    tags = TaggableManager()

    def __str__(self):
        return self.titele
    
    def total_donations(self):
        return self.donations.aggregate(models.Sum('amount'))['amount__sum'] or 0


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
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text