#from tkinter import CASCADE
#from unicodedata import name
from django.db import models
from accounts.models import UserProfile
from locations.models import Location
from phone_field import PhoneField
from ckeditor.fields import RichTextField
from PIL import Image

class PositionClass(models.Model):
    position_class = models.CharField(max_length = 50)
    grade = models.SmallIntegerField()

    def __str__(self):
        return self.position_class

class Facility(models.Model):
    manager = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name = 'fac_manager', verbose_name="Facility Manager")
    administrative_assistant = models.ForeignKey('Employee', null = True, blank = True, on_delete=models.CASCADE, related_name = 'fac_assist', verbose_name="Administrative Assistant")
    name = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name = "Facility Name")
    phone_number = PhoneField("Phone Number")
    fax_number = PhoneField("Fax Number", null=True, blank=True)
    street_address = models.CharField("Street Address", max_length=100)
    mailing_address = models.CharField("Mailing Address", null = True, blank = True, max_length=100)
    city = models.CharField("City", max_length=50)
    state = models.CharField("State", max_length=50)
    zipcode = models.CharField("Zip Code", max_length=5)
    facility_image = models.ImageField("Facility Image", upload_to='images/facility/')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.facility_image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.facility_image.path)

    def __str__(self):
        return self.name.name

    class Meta:
        verbose_name = 'Facility'
        verbose_name_plural = 'Facilities'
        ordering = ['name__name']

class Employee(models.Model):

    name = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name = 'employees', verbose_name="Name")
    position_class = models.ForeignKey(PositionClass, on_delete=models.CASCADE, verbose_name="Position Class")
    title = models.CharField("Position Title", max_length = 50)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE, related_name = 'fac_employees', verbose_name = 'Duty Station', default = 1)
    start_date = models.DateTimeField("Start Date")
    end_date = models.DateTimeField("End Date", null = True, blank =True)
    active = models.BooleanField("Employeed (check for yes)", default=True)

    class Meta:
        ordering = ['name__user__first_name', 'name__user__last_name']

    def __str__(self):
        return self.name.user.first_name + ' ' + self.name.user.last_name

class Department(models.Model):
    manager = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name = 'dept_manager', verbose_name = "Department Manager")
    deputy_manager = models.ForeignKey(Employee, null = True, blank = True, on_delete=models.CASCADE, related_name = 'dept_deputy', verbose_name = "Deputy Manager")
    administrative_assistant = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.CASCADE, related_name = 'dept_assist', verbose_name = "Administrative Assistant")
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE, verbose_name = "Department Office")
    name = models.CharField("Department Name", max_length=300)
    description = RichTextField("Department Desecription")
    department_image1 = models.ImageField("Department Image", upload_to='images/department/')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.department_image1.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.department_image1.path)

    def __str__(self):
        return self.name

class Division(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name="Division Department")
    director = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name = 'div_director', verbose_name="Division Director")
    deputy_director = models.ForeignKey(Employee, null = True, blank = True, on_delete=models.CASCADE, related_name = 'div_deputy', verbose_name="Deputy Division Director")
    administrative_assistant = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.CASCADE, related_name = 'div_assist', verbose_name = "Administrative Assistant")
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE, verbose_name="Division Office")
    name = models.CharField("Division Name", max_length=300)
    description = RichTextField("Division Desecription")
    division_image1 = models.ImageField("Division Image", upload_to='images/division/')

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
    project_leader = models.ManyToManyField(Employee, verbose_name="Project Leader")
    name = models.CharField("Project Name", max_length=300)
    description = RichTextField("Project Description")
    created = models.DateTimeField("Project Created")
    active = models.BooleanField("Active Project (check for yes)")
    project_image1 = models.ImageField("Project Image", upload_to='images/project/')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.project_image1.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.project_image1.path)
    
    def __str__(self):
        return self.name

class Subproject(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE, verbose_name='Subproject Division', related_name = "sub_div")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="subprojects", verbose_name="Parent Project")
    supervisor = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name = 'Subproject Supervisor', related_name = "sub_sup")
    name = models.CharField("Subproject Name", max_length=300)
    description = RichTextField("Subproject Description", null=True, blank=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    subproject = models.ForeignKey(Subproject, on_delete=models.CASCADE, related_name = 'tasks', verbose_name="Subproject")
    supervisor = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name = 'Task Supervisor', related_name = "task_sup")
    staff = models.ManyToManyField(Employee, blank = True, verbose_name = 'Task Staff', related_name = "staff")
    location = models.ManyToManyField(Location, blank = True, verbose_name = 'Task Location', related_name = 'locations')
    name = models.CharField("Task Name", max_length=300)
    description = RichTextField("Task Description")

    def __str__(self):
        return self.name
