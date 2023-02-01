from types import CoroutineType
from django.contrib.auth.models import AbstractUser
from django.db import models
from phone_field import PhoneField
from ckeditor.fields import RichTextField
from PIL import Image

class CustomUser(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.first_name + " " + self.last_name

class UserProfile(models.Model):

    # EMPLOYER = (
    #     ("NPT","Nez Perce Tribe"),
    #     ("IDFG","Idaho Department of Fish and Game"),
    #     ("WDFW", "Washington Department of Fish and Wildlife"),
    #     ("ODFW", "Oregon Department of Fish and Wildlife"),
    #     ("USFWS", "U.S. Fish and Wildlife Service"),
    #     ("USFS", "U.S. Forest Service"),
    #     ("USACE", 'U.S. Army Core of Engineers'),
    #     ("NOAA", "National Oceanic Atmospheric Administration"),
    #     ("BPA", "Bonneville Power Administration"),
    #     ("Other", "Other")
    # )

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, help_text = "User name", related_name='user_profiles')
    #location = models.CharField(max_length = 50, null = True, blank = True, help_text="City, State")
    organization = models.CharField(max_length = 50)
    work_phone = PhoneField(null=True, blank=True)
    mobile_phone = PhoneField(null=True, blank=True)
    email_updates = models.BooleanField(default=False)
    city = models.CharField("City", null = True, blank = True, max_length=50)
    state = models.CharField("State", null = True, blank = True, max_length=50)
    bio = RichTextField(null = True)   
    profile_picture = models.ImageField(upload_to='images/profile/', default='images/profile/P7160105_fix.JPG') 

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.profile_picture.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_picture.path)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
