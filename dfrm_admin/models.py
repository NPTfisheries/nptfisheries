from tkinter import CASCADE
from unicodedata import name
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

class Employee(models.Model):

    # POSITION_CLASS = (
    #     (9,"Administrative Specialist I"),
    #     (11,"Administrative Specialist II"),
    #     (13,"Administrative Specialist III"),
    #     (15,"Executive Assistant I"),
    #     (9,"Technician I"),
    #     (11,"Technician II" ),
    #     (13,"Technician III"),
    #     (15,"Technician IV"),
    #     (17,"Professional I" ),
    #     (19,"Professional II"),
    #     (20,"Professional III"),
    #     (21,"Professional IV"),
    #     (22,"Professional V"),
    #     (23,"Manager I"),
    #     (24,"Manager II"),
    #     (26,"Manager III"),
    #     (28,"Manager IV"),
    #     (30,"Manager V")
    # )

    name = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name = 'employees')
    position_class = models.ForeignKey(PositionClass, on_delete=models.CASCADE)
    title = models.CharField("Position title", max_length = 50)
    start_date = models.DateTimeField("Start date")
    end_date = models.DateTimeField("End date", null = True, blank =True)
    active = models.BooleanField("Active", default=False)

    def __str__(self):
        return self.name.user.first_name + ' ' + self.name.user.last_name

class Facility(models.Model):
    manager = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name = 'fac_manager')
    administrative_assistant = models.ForeignKey(Employee, null = True, blank = True, on_delete=models.CASCADE, related_name = 'fac_assist')
    name = models.ForeignKey(Location, on_delete=models.CASCADE)
    #name = models.CharField("Facility name", max_length=100)
    phone_number = PhoneField("Phone number")
    fax_number = PhoneField("Fax number", null=True, blank=True)
    street_address = models.CharField("Street address", max_length=100)
    mailing_address = models.CharField("Mailing address", null = True, blank = True, max_length=100)
    city = models.CharField("City", max_length=50)
    state = models.CharField("State", max_length=50)
    zipcode = models.CharField("Zip Code", max_length=5)
    facility_image = models.ImageField("Facility image", blank=True, upload_to='images/facility/')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.office_image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.office_image.path)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Facility'
        verbose_name_plural = 'Facilities'


class Department(models.Model):
    manager = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name = 'dept_manager')
    deputy_manager = models.ForeignKey(Employee, null = True, blank = True, on_delete=models.CASCADE, related_name = 'dept_deputy')
    administrative_assistant = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.CASCADE, related_name = 'dept_assist')
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    name = models.CharField("Department name", max_length=300)
    description = RichTextField("Department desecription")
    department_image1 = models.ImageField("Department Image", null=True, blank=True, upload_to='images/department/')

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
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    director = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name = 'div_director')
    deputy_director = models.ForeignKey(Employee, null = True, blank = True, on_delete=models.CASCADE, related_name = 'div_deputy')
    administrative_assistant = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.CASCADE, related_name = 'div_assist')
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    name = models.CharField("Division name", max_length=300)
    description = RichTextField("Division desecription")
    division_image1 = models.ImageField("Division Image", null=True, blank=True, upload_to='images/division/')

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
    project_leader = models.ManyToManyField(Employee)
    name = models.CharField("Project name", max_length=300)
    description = RichTextField("Project description")
    created = models.DateTimeField("Created")
    active = models.BooleanField("Active")
    project_image1 = models.ImageField("Project image", null=True, blank=True, upload_to='images/project/')

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
    division = models.ForeignKey(Division, on_delete=models.CASCADE, related_name = "sub_div")
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    supervisor = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name = "sub_sup")
    name = models.CharField("Subproject name", max_length=300)
    description = RichTextField("Subproject description")

class Task(models.Model):
    subproject = models.ForeignKey(Subproject, on_delete=models.CASCADE)
    supervisor = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name = "task_sup")
    staff = models.ManyToManyField(Employee, blank = True, related_name = "staff")
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    name = models.CharField("Task name", max_length=300)
    description = RichTextField("Task description")
