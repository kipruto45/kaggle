
from django.db import models
from accounts.models import User

class Dataset(models.Model):
	PRIVACY_CHOICES = [
		('public', 'Public'),
		('private', 'Private'),
		('competition', 'Competition Only'),
	]
	title = models.CharField(max_length=200)
	description = models.TextField()
	file = models.FileField(upload_to='datasets/')
	uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
	source = models.CharField(max_length=200, blank=True)
	license = models.CharField(max_length=100, blank=True)
	tags = models.CharField(max_length=200, blank=True)
	privacy = models.CharField(max_length=20, choices=PRIVACY_CHOICES, default='public')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title
