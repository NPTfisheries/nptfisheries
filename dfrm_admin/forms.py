from django import forms
from dfrm_admin.models import Employee, Office, Division, Project

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('name', 'position_class', 'title', 'active')

class OfficeForm(forms.ModelForm):
    class Meta:
        model = Office
        fields = ('name', 'phone_number', 'fax_number', 'address', 'city', 'state', 'zipcode', 'office_manager', 'administrative_assistant', 'office_image')

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
        fields = ('division', 'office', 'name', 'description', 'project_leader', 'staff', 'created', 'active', 'project_image1')

        staff = forms.ModelMultipleChoiceField(queryset=Employee.objects.all(), help_text="Remove highlighted rows to null field.")

        widgets = {
            'division': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'project_leader': forms.Select(attrs={'class': 'form-control'}),
            'created': forms.DateInput(attrs={'class': 'form-control'}),
            'active': forms.RadioSelect(attrs={'class': 'form-control', 'type':'checkbox'}),
        }