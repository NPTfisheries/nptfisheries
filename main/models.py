from __future__ import division
from ctypes import addressof
from types import CoroutineType
from django.db import models
from accounts.models import CustomUser
from phone_field import PhoneField
from PIL import Image

# Create your models here.
class Office(models.Model):
    office = models.CharField(max_length=100)
    phone_number = PhoneField(null=True, blank=True, help_text='Contact phone number')
    fax_number = PhoneField(null=True, blank=True, help_text='Contact phone number')
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)

    def __str__(self):
        return self.office

class Employee(models.Model):

    POSITION_CLASS = (
        ("Technician I","Technician I"),
        ("Technician II","Technician II" ),
        ("Technician III","Technician III"),
        ("Biologist I","Biologist I" ),
        ("Biologist II","Biologist II"),
        ("Project Leader III","Project Leader III"),
        ("Project Leader V","Project Leader V"),
        ("Manager I","Manager I"),
        ("Manager II","Manager II"),
        ("Manager III","Manager III"),
        ("Manager IV","Manager IV"),
        ("Manager V","Manager V")
    )

    employee = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    position_class = models.CharField(choices=POSITION_CLASS, max_length=100)
    title = models.CharField(max_length = 30)
    phone_number = PhoneField(null=True, blank=True, help_text='Contact phone number')
    is_employed = models.BooleanField(default=False)

    def __str__(self):
        return self.employee


class Division(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    director = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name="employee")
    deputy = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name="employee")
    support = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name="employee")
    phone_number = PhoneField(null=True, blank=True, help_text='Contact phone number')
    division_image1 = models.ImageField(null=True, blank=True, upload_to='images/division/')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.division_image1.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.division_image1.path)

    def __str__(self):
        return self.name

class Project(models.Model):
    division = models.ForeignKey(Division, on_delete=models.PROTECT)
    name = models.CharField(max_length=300)
    description = models.TextField(null=True)
    projectleader = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name="employee")
    created = models.DateTimeField(null=True)
    inactive = models.BooleanField()
    project_image1 = models.ImageField(null=True, blank=True, upload_to='images/project/')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.project_image1.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.project_image1.path)
    
    def __str__(self):
        return self.name

    
