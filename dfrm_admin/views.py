from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from django.core.serializers import serialize
from django.views.generic.edit import CreateView, UpdateView
from djgeojson.views import GeoJSONLayerView
from accounts.models import UserProfile
from dfrm_admin.models import Department, Employee, Facility, Division, Project, Subproject, Task
#from accounts.models import CustomUser
from news.models import Post
#from accounts.models import UserProfile
from .forms import DepartmentForm, EmployeeForm, FacilityForm, DivisionForm, ProjectForm, SubprojectFormSet, TaskFormSet

# Create your views here.

def home(request):
    department = Department.objects.all().order_by('name')
    post = Post.objects.filter(header_image__isnull = False).order_by("-pk")[0:3]
    return render(request, 'home.html', {"department":department, "post":post})

# Department Views

def department(request):
    department = Department.objects.all().order_by('name')
    return render(request, 'dfrm_admin/department.html', {'department': department})

def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk)
    division = Division.objects.filter(department = pk)
    project = Project.objects.filter(subprojects__division__department = pk).distinct()
    # need to add projects filtered for division
    return render(request, 'dfrm_admin/department_detail.html', {'department':department, 'division':division, 'project':project})

@permission_required('dfrm_admin.add_department', raise_exception=True)
def department_new(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST, request.FILES)
        if form.is_valid():
            d = form.save(commit=False)
            d.save()
            return redirect('home')
    else:
        form = DepartmentForm()
    return render(request, 'dfrm_admin/department_edit.html', {'form':form})

@permission_required('dfrm_admin.change_department', raise_exception=True)
def department_edit(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == "POST":
        form = DepartmentForm(request.POST, request.FILES, instance=department)
        if form.is_valid():
            d = form.save(commit=False)
            d.save()
            return redirect('home')
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'dfrm_admin/department_edit.html', {'form': form})

# All Division Views
def division(request):
    divisions = Division.objects.all().order_by('name')
    return render(request, 'dfrm_admin/division.html', {'divisions': divisions})

def division_detail(request, pk):
    divisions = get_object_or_404(Division, pk=pk)
    subproject = Subproject.objects.filter(division = pk)
    return render(request, 'dfrm_admin/division_detail.html', {'divisions':divisions, 'subproject':subproject})

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

def project(request):
    projects = Project.objects.all().order_by('name')
    return render(request, 'dfrm_admin/project.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    subproject = Subproject.objects.filter(project=pk)
    task = Task.objects.filter(subproject__project=pk)
    return render(request, 'dfrm_admin/project_detail.html', {'project':project, 'subproject':subproject, 'task':task})

@permission_required('dfrm_admin.add_project', raise_exception=True)
def project_new(request):
    if request.method == 'POST':
        f = ProjectForm(request.POST, request.FILES)
        #fs = SubprojectFormSet(request.POST)

        #print(f.is_valid())
        #print(fs.is_valid())

        if f.is_valid():
            new_proj = f.save(commit=False)
            new_proj.save()
            f.save_m2m()
            #new_subs = fs.save(commit=False)
            #new_subs.project = new_proj.pk
            #new_subs.save()
            return redirect('project_edit', pk=new_proj.pk)
    else:
        f = ProjectForm()
       # fs = SubprojectFormSet()
    return render(request, 'dfrm_admin/project_new.html',
    {'f':f}
    )

@permission_required('dfrm_admin.change_project', raise_exception=True)
def project_edit(request, pk=False):
    if pk:
        project=Project.objects.get(pk=pk)
    else:
        project=Project()
    if request.method == 'POST':
        f = ProjectForm(request.POST, request.FILES, instance=project)
        fs = SubprojectFormSet(request.POST,instance=project)

        if fs.is_valid() and f.is_valid():
            #pass
            new_proj = f.save(commit=False)
            new_proj.save()
            f.save_m2m()
            fs.save()
            return redirect('project_detail', pk=new_proj.pk)
        
        else:
            if f.errors:
                print('Project form errors:')
                print(f.errors)
            else:
                print('Project form valid.')
            
            if fs.errors:
                print('Subproject form errors:')
                print(fs.errors)
            else:
                print('Subproject form valid.')

    else:
        f = ProjectForm(instance=project)
        fs = SubprojectFormSet(instance=project)
    
    return render(request, 'dfrm_admin/project_edit.html',
    {'fs':fs, 'f':f, 'project':project}
    )

# Task

@permission_required('dfrm_admin.change_project', raise_exception=True)
def task_edit(request, pk):
    subproject=Subproject.objects.get(pk=pk)
    
    if request.method == 'POST':
        formset = TaskFormSet(request.POST, request.FILES, instance=subproject)

        if formset.is_valid():
            fs = formset.save(commit=False)
            formset.save()
            formset.save_m2m()
            return redirect('project_detail', pk=subproject.project.id)
    else:
        formset = TaskFormSet(instance=subproject)
    
    return render(request, 'dfrm_admin/task_edit.html',
    {'formset':formset, 'subproject':subproject}
    )


# Office Views

def facility(request):
    facility = Facility.objects.all().order_by("name")
    return render(request, 'dfrm_admin/facility.html', {'facility':facility})

def facility_detail(request, pk):
    facility = get_object_or_404(Facility, pk=pk)
    return render(request, 'dfrm_admin/facility_detail.html', {'facility':facility})

@permission_required('dfrm_admin.add_facility', raise_exception=True)
def facility_new(request):
    if request.method == "POST":
        form = FacilityForm(request.POST, request.FILES)
        if form.is_valid():
            o = form.save(commit=False)
            o.save()
            return redirect('facility')
    else:
        form = FacilityForm()
    return render(request, 'dfrm_admin/facility_edit.html', {'form':form})

@permission_required('dfrm_admin.change_facility', raise_exception=True)
def facility_edit(request, pk):
    facility = get_object_or_404(Facility, pk=pk)
    if request.method == "POST":
        form = FacilityForm(request.POST, request.FILES, instance=facility)
        if form.is_valid():
            d = form.save(commit=False)
            d.save()
            return redirect('facility')
    else:
        form = FacilityForm(instance=facility)
    return render(request, 'dfrm_admin/facility_edit.html', {'form': form})

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

# API Data
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import EmployeeSerializer, FacilitySerializer, DepartmentSerializer, DivisionSerializer, ProjectSerializer, SubprojectSerializer, TaskSerializer
from locations.models import Location, Point, Linestring, Polygon
from locations.serializers import PointSerializer, LinestringSerializer, PolygonSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Employee.objects.all()
    # specify serializer to be used
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAdminUser]

class FacilityViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Facility.objects.all()
    # specify serializer to be used
    serializer_class = FacilitySerializer
    permission_classes = [permissions.IsAdminUser]

class DepartmentViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Department.objects.all()
    # specify serializer to be used
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.IsAdminUser]

class DivisionViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Division.objects.all()
    # specify serializer to be used
    serializer_class = DivisionSerializer
    permission_classes = [permissions.IsAdminUser]

class ProjectViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Project.objects.all()
    # specify serializer to be used
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAdminUser]

    @action(detail=True)
    def subprojects(self, request, pk=None):
        project = self.get_object() # retrieve an object by pk provided
        s = Subproject.objects.filter(project=project).distinct()
        s_json = SubprojectSerializer(s, many=True)
        return Response(s_json.data)

    @action(detail=True)
    def tasks(self, request, pk=None):
        project = self.get_object() # retrieve an object by pk provided
        t = Task.objects.filter(subproject__project=project).distinct()
        t_json = TaskSerializer(t, many=True)
        return Response(t_json.data)

    @action(detail=True)
    def points(self, request, pk=None):
        project = self.get_object() # retrieve an object by pk provided
        t = Task.objects.filter(subproject__project=project).distinct()
        l = t.values_list('location', flat = True)
        #print(l)
        p = Point.objects.filter(name__in = l)
        #print(p)
        p_json = PointSerializer(p, many=True)
        return Response(p_json.data)

    @action(detail=True)
    def linestrings(self, request, pk=None):
        project = self.get_object() # retrieve an object by pk provided
        t = Task.objects.filter(subproject__project=project).distinct()
        l = t.values_list('location', flat = True)
        #print(l)
        p = Linestring.objects.filter(name__in = l)
        #print(p)
        p_json = LinestringSerializer(p, many=True)
        return Response(p_json.data)

    @action(detail=True)
    def polygons(self, request, pk=None):
        project = self.get_object() # retrieve an object by pk provided
        t = Task.objects.filter(subproject__project=project).distinct()
        l = t.values_list('location', flat = True)
        #print(l)
        p = Polygon.objects.filter(name__in = l)
        #print(p)
        p_json = PolygonSerializer(p, many=True)
        return Response(p_json.data)
    

class SubprojectViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Subproject.objects.all()
    # specify serializer to be used
    serializer_class = SubprojectSerializer
    permission_classes = [permissions.IsAdminUser]
    
class TaskViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Task.objects.all()
    # specify serializer to be used
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAdminUser]