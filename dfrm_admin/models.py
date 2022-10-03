from django.db import models
from accounts.models import UserProfile
from phone_field import PhoneField
from PIL import Image

class Employee(models.Model):

    POSITION_CLASS = (
        (9,"Administrative Specialist I"),
        (11,"Administrative Specialist II"),
        (13,"Administrative Specialist III"),
        (15,"Executive Assistant I"),
        (9,"Technician I"),
        (11,"Technician II" ),
        (13,"Technician III"),
        (15,"Technician IV"),
        (17,"Professional I" ),
        (19,"Professional II"),
        (20,"Professional III"),
        (21,"Professional IV"),
        (22,"Project Leader V"),
        (23,"Manager I"),
        (24,"Manager II"),
        (26,"Manager III"),
        (28,"Manager IV"),
        (30,"Manager V")
    )

    name = models.OneToOneField(UserProfile, on_delete=models.CASCADE, help_text = "Employee name", related_name = 'employees')
    position_class = models.SmallIntegerField(choices=POSITION_CLASS, help_text = "Position class")
    title = models.CharField(max_length = 50, help_text="Position title")
    active = models.BooleanField(default=False, help_text="Is the employee actively employed?")

    def __str__(self):
        return self.name.user.first_name + ' ' + self.name.user.last_name

class Office(models.Model):
    name = models.CharField(max_length=100, help_text = "Office name")
    phone_number = PhoneField(help_text='Phone number')
    fax_number = PhoneField(null=True, blank=True, help_text= 'Fax number')
    address = models.CharField(max_length=100, help_text = 'Street address')
    city = models.CharField(max_length=50, help_text = 'City')
    state = models.CharField(max_length=50, help_text = 'State')
    zipcode = models.CharField(max_length=5, help_text = 'Zip Code')
    office_manager = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name = 'offices')
    administrative_assistant = models.ForeignKey(Employee, null = True, blank = True, on_delete=models.CASCADE, related_name = 'office_assistants')
    office_image = models.ImageField(blank=True, upload_to='images/office/')

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
        verbose_name = 'Office'
        verbose_name_plural = 'Offices'


class Division(models.Model):
    name = models.CharField(max_length=300, help_text = "Division name")
    description = models.TextField(help_text = "Division description")
    director = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='division_directors')
    deputy_director = models.ForeignKey(Employee, null = True, blank = True, on_delete=models.CASCADE, related_name="division_deputies")
    administrative_assistant = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.CASCADE, related_name='division_support')
    office = models.ForeignKey(Office, on_delete=models.CASCADE, related_name='division_offices')
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
    office = models.ForeignKey(Office, on_delete=models.CASCADE, default = "1")
    name = models.CharField(max_length=300, help_text = "Project name")
    description = models.TextField(help_text = "Project description")
    project_leader = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="project_leads")
    staff = models.ManyToManyField(Employee, blank = True)
    created = models.DateTimeField(help_text = "When was the project created?")
    active = models.BooleanField(help_text = "Is the project currently active?")
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
    
