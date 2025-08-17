
from django.db import models
from accounts.models import User

class MpesaTransaction(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	phone = models.CharField(max_length=15)
	amount = models.DecimalField(max_digits=12, decimal_places=2)
	transaction_id = models.CharField(max_length=100, unique=True)
	status = models.CharField(max_length=20)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.user.username} - {self.amount} - {self.status}"
