# doc_lib/models.py
from django.db import models
from django.conf import settings
from django.urls import reverse
from datetime import datetime, date

class Document(models.Model):
	title = models.CharField(max_length=255)
	primary_author = models.CharField(max_length=30)
	secondary_authors = models.CharField(max_length=255, null = True) #default="This is default"
	publish_date = models.DateField()
	document_type = models.CharField(max_length=30)
	keywords = models.CharField(max_length = 60)
	file = models.FileField(upload_to='documents/')
	uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	upload_date = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.title + ' | ' + self.primary_author

	def get_absolute_url(self):
		return reverse('document_list')