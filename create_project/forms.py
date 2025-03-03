from django import forms
from django.forms import ModelForm
from homepage.models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Project Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Project Description'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'Category': forms.Select(attrs={'class': 'form-control'}),
            'totalTarget': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Total Target'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
            'endTime': forms.DateInput(attrs={'type': 'date'}),
        }
