from django.db import models

# Create your models here.
class Division(models.Model):
    division = models.CharField(max_length=300)
    description = models.TextField()

    def _str_(self):
        return self.division

class Project(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    project = models.CharField(max_length=300)
    closed = models.BooleanField()
    
    def _str_(self):
        return self.project

    
