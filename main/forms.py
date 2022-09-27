from django import forms
from main.models import Staff, Office, Division, Project

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ('name', 'position_class', 'title', 'work_phone', 'cell_phone', 'active', 'bio')

        widgets = {
            'active': forms.RadioSelect(attrs={'class': 'form-control', 'type':'checkbox'}),
        }

class OfficeForm(forms.ModelForm):
    class Meta:
        model = Office
        fields = ('name', 'phone_number', 'fax_number', 'address', 'city', 'state', 'zipcode', 'office_manager', 'administrative_assistant')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class DivisionForm(forms.ModelForm):
    class Meta:
        model = Division
        fields = ('name', 'description', 'director', 'deputy_director', 'administrative_assistant', 'office', 'division_image1')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'director': forms.Select(attrs={'class': 'form-control'}),
            'deputy_director': forms.Select(attrs={'class': 'form-control'}),
            'administrative_assistant': forms.Select(attrs={'class': 'form-control'}),
            'office': forms.Select(attrs={'class': 'form-control'}),
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('division', 'name', 'description', 'project_leader', 'created', 'active', 'project_image1')

        widgets = {
            'division': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'project_leader': forms.Select(attrs={'class': 'form-control'}),
            'staff': forms.Select(attrs={'class': 'form-control'}),
            'created': forms.DateInput(attrs={'class': 'form-control'}),
            'active': forms.RadioSelect(attrs={'class': 'form-control', 'type':'checkbox'}),
        }