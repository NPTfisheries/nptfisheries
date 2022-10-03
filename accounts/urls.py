# accounts/urls.py
from django.urls import path
from . import views
#from .views import ProfileView

urlpatterns = [
   path('profile/<int:pk>/', views.profile, name='profile'),
   # path("signup/", SignUpView.as_view(), name="signup"),
    #path("edit_profile/", UserEditView.as_view(), name="edit_profile"),
   # path("edit_profile/", ProfileEditView, name = "edit_profile"),
    #path("password/", auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
   # path("password/", PasswordsChangeView.as_view(template_name='registration/change-password.html')),
   # path('password_success/', password_success, name="password_success"),
]