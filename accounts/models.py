
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	email = models.EmailField(unique=True, null=True, blank=True)
	phone = models.CharField(max_length=15, unique=True, null=True, blank=True)
	is_phone_verified = models.BooleanField(default=False)
	is_email_verified = models.BooleanField(default=False)
	county = models.CharField(max_length=50, blank=True)
	institution = models.CharField(max_length=100, blank=True)
	# Add more Kenya-specific fields as needed

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email', 'phone']

class OTP(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	code = models.CharField(max_length=6)
	created_at = models.DateTimeField(auto_now_add=True)
	is_used = models.BooleanField(default=False)

	def __str__(self):
		return f"OTP for {self.user.username} - {self.code}"
