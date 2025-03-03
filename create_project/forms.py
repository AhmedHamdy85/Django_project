from django import forms
from django.forms import ModelForm
from homepage.models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'endTime': forms.DateInput(attrs={'type': 'date'}),
        }

        