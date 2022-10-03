# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

#from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, UserProfile

class CustomUserAdmin(UserAdmin):
    #add_form = CustomUserCreationForm
    #form = CustomUserChangeForm
    model = CustomUser
    list_display = ("id","first_name", "last_name", "username", "email", )
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email',)
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        })
    )

admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'employer', 'work_phone', 'email_updates')