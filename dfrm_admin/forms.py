from django import forms
from dfrm_admin.models import Employee, Facility, Division, Project

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('name', 'position_class', 'title', 'start_date', 'end_date', 'active')

class FacilityForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = ('name', 'phone_number', 'fax_number', 'street_address', 'mailing_address', 'city', 'state', 'zipcode', 'manager', 'administrative_assistant', 'facility_image')
        #fields = '__all__'

        widgets = {
            'name': forms.Select(attrs={'class': 'form-control'}),
        }

class DivisionForm(forms.ModelForm):
    class Meta:
        model = Division
        fields = ('name', 'description', 'director', 'deputy_director', 'administrative_assistant', 'facility', 'division_image1')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'director': forms.Select(attrs={'class': 'form-control'}),
            'deputy_director': forms.Select(attrs={'class': 'form-control'}),
            'administrative_assistant': forms.Select(attrs={'class': 'form-control'}),
            'facility': forms.Select(attrs={'class': 'form-control'}),
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'description', 'project_leader', 'created', 'active', 'project_image1')

        project_leader = forms.ModelMultipleChoiceField(queryset=Employee.objects.all(), help_text="Remove highlighted rows to null field.")

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'created': forms.DateInput(attrs={'class': 'form-control'}),
            'active': forms.RadioSelect(attrs={'class': 'form-control', 'type':'checkbox'}),
        }