
from django.db import models
from accounts.models import User
from datasets.models import Dataset

class Competition(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
	host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hosted_competitions')
	prize = models.DecimalField(max_digits=12, decimal_places=2, default=0)
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()
	rules = models.TextField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

class Submission(models.Model):
	competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
	participant = models.ForeignKey(User, on_delete=models.CASCADE)
	file = models.FileField(upload_to='submissions/')
	score = models.FloatField(null=True, blank=True)
	submitted_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.participant.username} - {self.competition.title}"
