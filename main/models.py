from django.db import models
from phone_field import PhoneField
from PIL import Image


# Create your models here.
class Division(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    director = models.CharField(max_length=300, null=True)
    deputy = models.CharField(max_length=300, null=True, blank=True)
    support = models.CharField(max_length=300, null=True, blank=True)
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
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    description = models.TextField(null=True)
    projectleader = models.CharField(max_length=300, null=True)
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

    
