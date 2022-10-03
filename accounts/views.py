# accounts/views.py
from django.shortcuts import render, get_object_or_404, redirect
#from django.views.generic import CreateView
from .models import UserProfile
#from django.contrib.auth import get_user_model
from .forms import UserProfileForm

def profile(request, pk):
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
    return render(request, 'profile/profile.html', {'form': form})