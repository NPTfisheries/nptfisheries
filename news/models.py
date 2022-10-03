from django.db import models
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
from PIL import Image
from dfrm_admin.models import Employee

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=255)
	header_image = models.ImageField(null=True, blank=True, upload_to='images/blog/')
	uploaded_by = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="news_upload")
	primary_author = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="author")
	secondary_authors = models.ManyToManyField(Employee, related_name="other_authors") #default="This is default"
	#body = models.TextField()
	body = RichTextField(blank=True, null=True)
	snippet = RichTextField(max_length=255)#, default="Click link above to read blog post...")
	post_date = models.DateField(auto_now_add=True)

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		img = Image.open(self.header_image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.header_image.path)

	def __str__(self):
		return self.title + ' | ' + self.primary_author

	def get_absolute_url(self):
		return reverse('news_list')
		#return reverse('news_detail', args=(str(self.id)))
