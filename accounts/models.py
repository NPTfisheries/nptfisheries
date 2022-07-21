from django.contrib.auth.models import AbstractUser
from django.db import models
from phone_field import PhoneField

class CustomUser(AbstractUser):
    pass
    # add additional fields in here
    title = models.CharField(max_length = 30)
    phone_number = PhoneField(null=True, blank=True, help_text='Contact phone number')
    employee = models.BooleanField(default=False)

    def __str__(self):
        return self.username