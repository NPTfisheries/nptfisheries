# doc_lib/models.py
from django.db import models
from dfrm_admin.models import Employee
from django.conf import settings
from django.urls import reverse
from datetime import datetime, date

class Document(models.Model):

	DOCUMENT_TYPE = (
		("Annual Report","Annual Report"),
		("Journal Article","Journal Article"),
		("Technical Memo","Technical Memo"),
		("Presentation Slides","Presentation Slides"),
		("Other","Other")
	)

	title = models.CharField(max_length=255)
	employee_authors = models.ManyToManyField(Employee) #default="This is default"
	publish_date = models.DateField()
	document_type = models.CharField(choices = DOCUMENT_TYPE, max_length=30)
	keywords = models.CharField(max_length = 60)
	citation = models.TextField()
	file = models.FileField(upload_to='documents/')
	uploaded_by = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name ="documents_upload")
	upload_date = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('document_list')