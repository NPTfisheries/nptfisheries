# accounts/views.py
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from .forms import CustomUserCreationForm, CustomUserChangeForm, PasswordChangingFrom

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class UserEditView(UpdateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy("home")
    template_name = "registration/edit_profile.html"

    def get_object(self):
        return self.request.user

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingFrom
    #form_class = PasswordChangeForm
    #success_url = reverse_lazy("home")
    success_url = reverse_lazy("password_success")

def password_success(request):
    return render(request, 'registration/password_success.html', {})