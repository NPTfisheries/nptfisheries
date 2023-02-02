from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from datetime import datetime, date
from ckeditor.fields import RichTextField
from PIL import Image
from dfrm_admin.models import Employee

# Create your models here.

class Post(models.Model):
	author = models.ForeignKey(Employee, on_delete=models.CASCADE)
	title = models.CharField(max_length=255)
	header_image = models.ImageField(upload_to='images/blog/')
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
		return self.title

	def get_absolute_url(self):
		return reverse('news_list')
		#return reverse('news_detail', args=(str(self.id)))

class Comment(models.Model):
	CommentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
	author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
	content = models.TextField()
	comment_date = models.DateTimeField(auto_now_add = True)
	parent = models.ForeignKey('self', null=True, blank =True, on_delete=models.CASCADE, related_name='replies')

	class Meta:
		ordering=['-comment_date']

	def __str__(self):
		return str(self.author) + ' comment ' + str(self.content)

	@property
	def children(self):
		return Comment.objects.filter(parent=self).reverse()

	@property
	def is_parent(self):
		if self.parent is None:
			return True
		return False
