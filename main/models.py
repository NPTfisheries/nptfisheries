from django.db import models
from accounts.models import CustomUser
from phone_field import PhoneField
from PIL import Image

# Create your models here.
class Staff(models.Model):

    POSITION_CLASS = (
        ("Technician I","Technician I"),
        ("Technician II","Technician II" ),
        ("Technician III","Technician III"),
        ("Professional I","Professional I" ),
        ("Professional II","Professional II"),
        ("Professional III","Professional III"),
        ("Professional IV","Professional IV"),
        ("Professional V","Project Leader V"),
        ("Manager I","Manager I"),
        ("Manager II","Manager II"),
        ("Manager III","Manager III"),
        ("Manager IV","Manager IV"),
        ("Manager V","Manager V")
    )

    name = models.ForeignKey(CustomUser, on_delete=models.CASCADE, help_text = "Employee name", related_name = 'employees')
    position_class = models.CharField(choices=POSITION_CLASS, max_length=100, help_text = "Position class")
    title = models.CharField(max_length = 50, help_text="Position title")
    work_phone = PhoneField(null=True, blank=True, help_text='Work phone number')
    cell_phone = PhoneField(null=True, blank=True, help_text='Cell phone number')
    active = models.BooleanField(default=False, help_text="Is the employee actively employed?")
    bio = models.TextField(null = True, help_text = "Staff biography")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.staff_image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.staff_image.path)

    class Meta:
        verbose_name = 'Staff'
        verbose_name_plural = 'Staff'

    def __str__(self):
        return self.name.first_name + " " + self.name.last_name

class Office(models.Model):
    name = models.CharField(max_length=100, help_text = "Office name")
    phone_number = PhoneField(help_text='Phone number')
    fax_number = PhoneField(null=True, blank=True, help_text= 'Fax number')
    address = models.CharField(max_length=100, help_text = 'Street address')
    city = models.CharField(max_length=50, help_text = 'City')
    state = models.CharField(max_length=50, help_text = 'State')
    zipcode = models.CharField(max_length=5, help_text = 'Zip Code')
    office_manager = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name = 'office')
    administrative_assistant = models.ForeignKey(Staff, null = True, blank = True, on_delete=models.CASCADE, related_name = 'office_assistant')
    office_image = models.ImageField(null=True, blank=True, upload_to='images/office/')

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
    director = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='director')
    deputy_director = models.ForeignKey(Staff, null = True, blank = True, on_delete=models.CASCADE, related_name="deputy")
    administrative_assistant = models.ForeignKey(Staff, null=True, blank=True, on_delete=models.CASCADE, related_name='support')
    office = models.ForeignKey(Office, on_delete=models.CASCADE, related_name='office')
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
    name = models.CharField(max_length=300, help_text = "Project name")
    description = models.TextField(help_text = "Project description")
    project_leader = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name="project_lead")
    staff = models.ManyToManyField(Staff, blank = True)
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

    
