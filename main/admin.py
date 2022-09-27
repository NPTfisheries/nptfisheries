from django.contrib import admin
from .models import Staff, Office, Division, Project

# Register your models here.
admin.site.register(Staff)
admin.site.register(Office)
admin.site.register(Division)
admin.site.register(Project)
