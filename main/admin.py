from django.contrib import admin
from .models import Office, Employee, Division, Project

# Register your models here.
admin.site.register(Office)
admin.site.register(Employee)
admin.site.register(Division)
admin.site.register(Project)
