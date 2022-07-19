from django.shortcuts import render, get_object_or_404, redirect
from main.models import Division, Project
from .forms import DivisionForm, ProjectForm

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

# All Division Views
def division(request):
    divisions = Division.objects.all()
    return render(request, 'division.html', {'divisions': divisions})

def division_detail(request, pk):
    divisions = get_object_or_404(Division, pk=pk)
    projects = Project.objects.filter(division = pk)
    # need to add projects filtered for division
    return render(request, 'division_detail.html', {'divisions':divisions, 'projects':projects})

def division_new(request):
    if request.method == "POST":
        form = DivisionForm(request.POST)
        if form.is_valid():
            d = form.save(commit=False)
            d.save()
            return redirect('division_detail', pk=d.pk)
        else:
            form = DivisionForm()
    return render(request, 'division_edit.html', {'form':form})

def division_edit(request, pk):
    division = get_object_or_404(Division, pk=pk)
    if request.method == "POST":
        form = DivisionForm(request.POST, instance=division)
        if form.is_valid():
            d = form.save(commit=False)
            d.save()
            return redirect('division_detail', pk=d.pk)
    else:
        form = DivisionForm(instance=division)
    return render(request, 'division_edit.html', {'form': form})

# All Project Views
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project_detail.html', {'project':project})

def project_new(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            d = form.save(commit=False)
            d.save()
            return redirect('project_detail', pk=d.pk)
    else:
        form = ProjectForm()
    return render(request, 'project_edit.html', {'form':form})

def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            d = form.save(commit=False)
            d.save()
            return redirect('project_detail', pk=d.pk)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'project_edit.html', {'form': form})


#def documents(request):
#    return render(request, 'document_list.html', {})

def contacts(request):
    return render(request, 'contacts.html', {})