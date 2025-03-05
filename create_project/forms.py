from django import forms
from django.forms import ModelForm
from homepage.models import Project, User

class ProjectForm(forms.Form):
    titele = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    image = forms.FileField()
    totalTarget = forms.IntegerField()
    endTime = forms.DateField()
    tags = forms.CharField(max_length=100)
    
    def __str__(self):
        return self.titele
