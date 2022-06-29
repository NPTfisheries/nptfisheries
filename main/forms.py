from django import forms
from main.models import Division, Project

class DivisionForm(forms.ModelForm):

    class Meta:
        model = Division
        fields = ('name', 'description', 'director', 'deputy', 'support',)

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('division', 'name', 'description', 'projectleader', 'inactive',)
