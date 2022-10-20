from django import forms
from django.forms import inlineformset_factory
from dfrm_admin.models import Department, Employee, Facility, Division, Project, Subproject, Task

class DateInput(forms.DateInput):
    input_type = 'date'

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

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ('name', 'description', 'manager', 'deputy_manager', 'administrative_assistant', 'facility', 'department_image1')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'manager': forms.Select(attrs={'class': 'form-control'}),
            'deputy_manager': forms.Select(attrs={'class': 'form-control'}),
            'administrative_assistant': forms.Select(attrs={'class': 'form-control'}),
            'facility': forms.Select(attrs={'class': 'form-control'}),
        }

class DivisionForm(forms.ModelForm):
    class Meta:
        model = Division
        fields = ('department','name', 'description', 'director', 'deputy_director', 'administrative_assistant', 'facility', 'division_image1')

        widgets = {
            'department': forms.Select(attrs={'class': 'form-control'}),
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
            'created': DateInput(attrs={'class': 'form-control'}),
            #'active': forms.RadioSelect(attrs={'class': 'form-control'}),
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
    can_delete=False,
    #fields = ('name', 'description', 'division', 'supervisor'),
    fields = '__all__',
    form = SubprojectForm)

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

TaskFormSet = inlineformset_factory(
    Subproject,
    Task,
    extra=1,
    fields='__all__',
    form = TaskForm)
