from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from accounts.models import UserProfile
from dfrm_admin.models import Employee, Office, Division, Project
#from accounts.models import CustomUser
from news.models import Post
#from accounts.models import UserProfile
from .forms import EmployeeForm, OfficeForm, DivisionForm, ProjectForm

# Create your views here.

def home(request):

    post = Post.objects.filter(header_image__isnull = False).order_by("-pk")[0:3]
    return render(request, 'home.html', {"post":post})

# All Division Views
def division(request):
    divisions = Division.objects.all().order_by('name')
    return render(request, 'dfrm_admin/division.html', {'divisions': divisions})

def division_detail(request, pk):
    divisions = get_object_or_404(Division, pk=pk)
    projects = Project.objects.filter(division = pk)
    # need to add projects filtered for division
    return render(request, 'dfrm_admin/division_detail.html', {'divisions':divisions, 'projects':projects})

@permission_required('dfrm_admin.add_division', raise_exception=True)
def division_new(request):
    if request.method == "POST":
        form = DivisionForm(request.POST, request.FILES)
        if form.is_valid():
            d = form.save(commit=False)
            d.save()
            return redirect('division_detail', pk=d.pk)
    else:
        form = DivisionForm()
    return render(request, 'dfrm_admin/division_edit.html', {'form':form})

@permission_required('dfrm_admin.change_division', raise_exception=True)
def division_edit(request, pk):
    division = get_object_or_404(Division, pk=pk)
    if request.method == "POST":
        form = DivisionForm(request.POST, request.FILES, instance=division)
        if form.is_valid():
            d = form.save(commit=False)
            d.save()
            return redirect('division_detail', pk=d.pk)
    else:
        form = DivisionForm(instance=division)
    return render(request, 'dfrm_admin/division_edit.html', {'form': form})

# All Project Views
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'dfrm_admin/project_detail.html', {'project':project})

@permission_required('dfrm_admin.add_project', raise_exception=True)
def project_new(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            d = form.save(commit=False)
            d.save()
            return redirect('project_detail', pk=d.pk)
    else:
        form = ProjectForm()
    return render(request, 'dfrm_admin/project_edit.html', {'form':form})

@permission_required('dfrm_admin.change_project', raise_exception=True)
def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            d = form.save(commit=False)
            d.save()
            return redirect('project_detail', pk=d.pk)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'dfrm_admin/project_edit.html', {'form': form})

# Office Views

def office(request):
    office = Office.objects.all().order_by("name")
    return render(request, 'dfrm_admin/office.html', {'office':office})

def office_detail(request, pk):
    office = get_object_or_404(Office, pk=pk)
    projects = Project.objects.filter(office = pk)
    return render(request, 'dfrm_admin/office_detail.html', {'office':office, 'projects':projects})

@permission_required('dfrm_admin.add_office', raise_exception=True)
def office_new(request):
    if request.method == "POST":
        form = OfficeForm(request.POST, request.FILES)
        if form.is_valid():
            o = form.save(commit=False)
            o.save()
            return redirect('office')
    else:
        form = OfficeForm()
    return render(request, 'dfrm_admin/office_edit.html', {'form':form})

@permission_required('dfrm_admin.change_office', raise_exception=True)
def office_edit(request, pk):
    office = get_object_or_404(Office, pk=pk)
    if request.method == "POST":
        form = OfficeForm(request.POST, request.FILES, instance=office)
        if form.is_valid():
            d = form.save(commit=False)
            d.save()
            return redirect('office')
    else:
        form = OfficeForm(instance=office)
    return render(request, 'dfrm_admin/office_edit.html', {'form': form})

# Employee Views

def employee(request):
    employees = Employee.objects.all().order_by("-position_class","name__user__first_name")
    return render(request, 'dfrm_admin/employees.html', {'employees':employees})

@permission_required('dfrm_admin.add_employee', raise_exception=True)
def employee_new(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            return redirect('employee')
    else:
        form = EmployeeForm()
    return render(request, 'dfrm_admin/employee_edit.html', {'form':form})

@permission_required('dfrm_admin.change_employee', raise_exception=True)
def employee_edit(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            d = form.save(commit=False)
            d.save()
            return redirect('employee')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'dfrm_admin/employee_edit.html', {'form': form})