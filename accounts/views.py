# accounts/views.py
from django.shortcuts import render, get_object_or_404, redirect
#from django.contrib.auth.decorators import user_passes_test
#from django.views.generic import CreateView
from .models import UserProfile
#from django.contrib.auth import get_user_model
from .forms import UserProfileForm

# def self_check(user):
#     return user


def profile(request, pk):
    profile = get_object_or_404(UserProfile, pk=pk)
    return render(request, 'profile/profile.html', {'profile': profile})

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

