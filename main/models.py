from django.db import models

# Create your models here.
class Division(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    director = models.CharField(max_length=300, null=True)
    deputy = models.CharField(max_length=300, null=True)
    support = models.CharField(max_length=300, null=True)

    def _str_(self):
        return self.division

class Project(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    description = models.TextField(null=True)
    projectleader = models.CharField(max_length=300, null=True)
    inactive = models.BooleanField()
    
    def _str_(self):
        return self.project

    
