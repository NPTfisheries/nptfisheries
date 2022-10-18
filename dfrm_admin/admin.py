from django.contrib import admin
from .models import PositionClass, Employee, Facility, Department, Division, Project, Subproject, Task

# Register your models here.
@admin.register(PositionClass)
class PositionClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'position_class', 'grade')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'position_class', 'title')

@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number', 'city', 'state', 'manager')

@admin.register(Department)
class DepartmentClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'manager')

@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'director', 'deputy_director', 'administrative_assistant')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Subproject)
class SubprojectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'supervisor')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'supervisor')