from django import forms
from main.models import Division, Project

class DivisionForm(forms.ModelForm):
    class Meta:
        model = Division
        fields = ('name', 'description', 'director', 'deputy', 'support', 'phone_number', 'division_image1')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'director': forms.TextInput(attrs={'class': 'form-control'}),
            'deputy': forms.TextInput(attrs={'class': 'form-control'}),
            'support': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('division', 'name', 'description', 'projectleader', 'created', 'inactive', 'project_image1')

        widgets = {
            'division': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'projectleader': forms.TextInput(attrs={'class': 'form-control'}),
            'created': forms.DateInput(attrs={'class': 'form-control'}),
           # 'inactive': forms.RadioSelect(attrs={'class': 'form-control', 'type':'checkbox'}),
        }