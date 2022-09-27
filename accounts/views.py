# accounts/views.py
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from .forms import CustomUserCreationForm, CustomUserChangeForm, PasswordChangingFrom
from main.models import Staff
from main.forms import StaffForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

# class UserEditView(UpdateView):
#     form_class = CustomUserChangeForm
#     success_url = reverse_lazy("home")
#     template_name = "registration/edit_profile.html"

#     def get_object(self):
#         return self.request.user

def load_profile(user):
  try:
    return user.staff
  except:  # this is not great, but trying to keep it simple
    staff = Staff.objects.create(name=user)
    return staff


def ProfileEditView(request):
    if request.method == 'POST':
        user_form = CustomUserChangeForm(request.POST, instance=request.user)
        profile_form = StaffForm(request.POST, instance=load_profile(request.user))

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile updated successfully.')
            return reverse_lazy("home")

    else:
        user_form = CustomUserChangeForm(instance=request.user)
        profile_form = StaffForm(instance=load_profile(request.user))

    return render(request, 'registration/edit_profile.html', {'user_form': user_form, 'profile_form': profile_form} )    


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingFrom
    #form_class = PasswordChangeForm
    #success_url = reverse_lazy("home")
    success_url = reverse_lazy("password_success")

def password_success(request):
    return render(request, 'registration/password_success.html', {})