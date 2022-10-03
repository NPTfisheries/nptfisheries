from django.contrib import admin
from .models import Employee, Office, Division, Project

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'position_class', 'title')

@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number', 'address', 'city', 'state', 'office_manager')

@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'director', 'deputy_director', 'administrative_assistant')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'project_leader', 'division', 'office')
