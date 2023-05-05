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

    AFFILIATION = (
        ("NPT","Nez Perce Tribe"),
        ("IDFG","Idaho Department of Fish and Game"),
        ("WDFW", "Washington Department of Fish and Wildlife"),
        ("ODFW", "Oregon Department of Fish and Wildlife"),
        ("USFWS", "U.S. Fish and Wildlife Service"),
        ("USFS", "U.S. Forest Service"),
        ("USACE", 'U.S. Army Core of Engineers'),
        ("NOAA", "National Oceanic Atmospheric Administration"),
        ("BPA", "Bonneville Power Administration"),
        ("NPCC", "Northwest Power and Conservation Council"),
        ("Other", "Other")
    )

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, help_text = "User name", related_name='user_profiles', verbose_name="User Name")
    #location = models.CharField(max_length = 50, null = True, blank = True, help_text="City, State")
    affiliation = models.CharField("Affiliation", choices=AFFILIATION, max_length = 50, default = 'NPT')
    work_phone = PhoneField("Work Phone", null=True, blank=True)
    mobile_phone = PhoneField("Mobile Phone", null=True, blank=True)
    email_updates = models.BooleanField("Email Updates (check for yes)", default=False)
    city = models.CharField("City", null = True, blank = True, max_length=50)
    state = models.CharField("State", null = True, blank = True, max_length=50)
    bio = RichTextField(null = True, verbose_name="Biography")   
    profile_picture = models.ImageField("Profile Picture", upload_to='images/profile/', default='images/profile/P7160105_fix.JPG') 

    class Meta:
        ordering = ['user__first_name', 'user__last_name']

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.profile_picture.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_picture.path)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
