from django import forms
from main.models import Division, Project

class DivisionForm(forms.ModelForm):

    class Meta:
        model = Division
        fields = ('division', 'description',)

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('division', 'project', 'closed',)
