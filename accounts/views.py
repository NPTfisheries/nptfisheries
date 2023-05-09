# accounts/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
#from django.contrib.auth.decorators import user_passes_test
#from django.views.generic import CreateView
from accounts.models import UserProfile
from dfrm_admin.models import Project, Subproject, Task
from documents.models import Document
#from django.contrib.auth import get_user_model
from .forms import UserProfileForm

# def self_check(user):
#     return user


def profile(request, pk):
    profile = get_object_or_404(UserProfile, pk=pk)
    
    project = Project.objects.filter(project_leader = profile.employees)
    subproject = Subproject.objects.filter(supervisor = profile.employees)
    task = Task.objects.filter(supervisor = profile.employees)
    staff = Task.objects.filter(staff = profile.employees)

    project_names = set()
    for obj in project:
        project_names.add(obj.name)
    for obj in subproject:
        project_names.add(obj.project.name)
    for obj in task:
        project_names.add(obj.subproject.project.name)
    for obj in staff:
        project_names.add(obj.subproject.project.name)

    # projects = {}
    # for obj in project:
    #     projects[obj.project.id] = {'id': obj.id, 'name': obj.name}
    # for obj in subproject:
    #     projects[obj.project.id] = {'id': obj.project.id, 'name': obj.project.name}
    # for obj in task:
    #     projects[obj.project.id] = {'id': obj.project.id, 'name': obj.subproject.project.name}
    # for obj in staff:
    #     projects[obj.project.id] = {'id': obj.project.id, 'name': obj.subproject.project.name}


    author = Document.objects.filter(employee_authors = profile.employees)
    
    context = {'profile': profile,
               'project_names':project_names,
               'project': project,
               'subproject': subproject,
               'task': task,
               'staff': staff,
               'author': author,
               'MEDIA_URL': settings.MEDIA_URL}
    
    return render(request, 'profile/profile.html', context)

#@user_passes_test(self_check, raise_exception=True)
def profile_edit(request, pk):
    profile = get_object_or_404(UserProfile, pk=pk)

    if request.method == "POST":
        user = request.user
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            p = form.save(commit=False)
            p.save()
            return redirect('profile', pk=p.pk)
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'profile/profile_edit.html', {'form': form})

