from django.db import models
from phone_field import PhoneField

# Create your models here.
class Division(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    director = models.CharField(max_length=300, null=True)
    deputy = models.CharField(max_length=300, null=True, blank=True)
    support = models.CharField(max_length=300, null=True, blank=True)
    phone_number = PhoneField(null=True, blank=True, help_text='Contact phone number')

    def __str__(self):
        return self.name

class Project(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    description = models.TextField(null=True)
    projectleader = models.CharField(max_length=300, null=True)
    created = models.DateTimeField(null=True)
    inactive = models.BooleanField()
    
    def __str__(self):
        return self.name

    
