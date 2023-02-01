from django import forms
from django.forms import inlineformset_factory
from dfrm_admin.models import Department, Employee, Facility, Division, Project, Subproject, Task

class DateInput(forms.DateInput):
    input_type = 'date'

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('name', 'position_class', 'title', 'start_date', 'end_date', 'active')

        widgets = {
            'name': forms.Select(attrs={'class': 'form-select'}),
            'position_class': forms.Select(attrs={'class': 'form-select'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': DateInput(attrs={'class': 'form-control'}),
            'end_date': DateInput(attrs={'class': 'form-control'}),
            'active': forms.CheckboxInput(attrs={'class': 'form-check form'}),
        }

class FacilityForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = ('name', 'phone_number', 'fax_number', 'street_address', 'mailing_address', 'city', 'state', 'zipcode', 'manager', 'administrative_assistant', 'facility_image')
        #fields = '__all__'

        widgets = {
            'name': forms.Select(attrs={'class': 'form-select'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'street_address': forms.TextInput(attrs={'class': 'form-control'}),
            'mailing_address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'zipcode': forms.TextInput(attrs={'class': 'form-control'}),
            'manager': forms.TextInput(attrs={'class': 'form-control'}),
            'administrative_assistant': forms.TextInput(attrs={'class': 'form-control'}),
            'facility_image': forms.FileInput(attrs={'class': 'form-control'}),
        }

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ('name', 'description', 'manager', 'deputy_manager', 'administrative_assistant', 'facility', 'department_image1')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'manager': forms.Select(attrs={'class': 'form-select'}),
            'deputy_manager': forms.Select(attrs={'class': 'form-select'}),
            'administrative_assistant': forms.Select(attrs={'class': 'form-select'}),
            'facility': forms.Select(attrs={'class': 'form-select'}),
            'department_image1': forms.FileInput(attrs={'class': 'form-control'}),
        }

class DivisionForm(forms.ModelForm):
    class Meta:
        model = Division
        fields = ('department','name', 'description', 'director', 'deputy_director', 'administrative_assistant', 'facility', 'division_image1')

        widgets = {
            'department': forms.Select(attrs={'class': 'form-select'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'director': forms.Select(attrs={'class': 'form-select'}),
            'deputy_director': forms.Select(attrs={'class': 'form-select'}),
            'administrative_assistant': forms.Select(attrs={'class': 'form-select'}),
            'facility': forms.Select(attrs={'class': 'form-select'}),
            'division_image1': forms.FileInput(attrs={'class': 'form-control'}),
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'description', 'project_leader', 'created', 'active', 'project_image1')

        project_leader = forms.ModelMultipleChoiceField(
            queryset=Employee.objects.all(),
            help_text="Remove highlighted rows to null field.")

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'project_leader': forms.SelectMultiple(attrs={'class':'form-select', 'size':10}),
            'created': DateInput(attrs={'class': 'form-control'}),
            'active': forms.CheckboxInput(attrs={'class': 'form-check form'}),
            'project_image1': forms.FileInput(attrs={'class': 'form-control'}),
        }

class SubprojectForm(forms.ModelForm):
    class Meta:
        model = Subproject
        #fields = ('name', 'description', 'division', 'supervisor')
        fields = '__all__'

        # widgets = {
        #     'division':forms.Select(attrs={'class': 'form-control'}),
        #     'name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'description': forms.Textarea(attrs={'class': 'form-control'}),
        #     'supervisor':forms.Select(attrs={'class': 'form-control'}),
        # }

SubprojectFormSet = inlineformset_factory(
    Project,
    Subproject,
    extra=2,
    can_delete=True,
    #fields = ('name', 'description', 'division', 'supervisor'),
    fields = '__all__',
    form = SubprojectForm)

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

        # staff = forms.ModelMultipleChoiceField(
        #     queryset=Employee.objects.all(),
        #     widget=forms.SelectMultiple)

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows':10, 'cols':100}),
            'supervisor': forms.Select(attrs={'class': 'form-select'}),
            'location': forms.SelectMultiple(attrs={'class': 'form-select', 'size':10}),
            'staff': forms.SelectMultiple(attrs={'class': 'form-select', 'size':'10'}),
        }


TaskFormSet = inlineformset_factory(
    Subproject,
    Task,
    extra= 3,
    can_delete=True,
    fields='__all__',
    form = TaskForm)
