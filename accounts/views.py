# accounts/views.py
from django.shortcuts import render, get_object_or_404, redirect
#from django.contrib.auth.decorators import user_passes_test
#from django.views.generic import CreateView
from .models import UserProfile
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
    supervise = Task.objects.filter(supervisor = profile.employees)
    staff = Task.objects.filter(staff = profile.employees)

    author = Document.objects.filter(employee_authors = profile.employees)
    
    context = {'profile': profile,
               'project': project,
               'subproject': subproject,
               'supervise': supervise,
               'staff': staff,
               'author': author}
    
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

