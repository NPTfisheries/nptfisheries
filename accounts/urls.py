# accounts/urls.py
from django.urls import path
from .views import SignUpView, UserEditView, PasswordsChangeView
#from django.contrib.auth import views as auth_views
from .views import password_success

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("edit_profile/", UserEditView.as_view(), name="edit_profile"),
    #path("password/", auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
    path("password/", PasswordsChangeView.as_view(template_name='registration/change-password.html')),
    path('password_success/', password_success, name="password_success"),
]