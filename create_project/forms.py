from django import forms
from django.forms import ModelForm
from homepage.models import Project, User
from taggit.models import Tag

from django import forms

class ProjectForm(forms.Form):
    titele = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    images = forms.FileField()
    category = forms.IntegerField()
    totalTarget = forms.IntegerField()
    endTime = forms.DateTimeField()
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'})
    )

    def clean_title(self):
        title = self.cleaned_data.get('title', '')
        if len(title) < 10:
            raise forms.ValidationError('Title must be at least 10 characters long')
        return title

