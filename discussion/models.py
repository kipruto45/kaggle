
from django.db import models
from accounts.models import User
from competitions.models import Competition

class DiscussionThread(models.Model):
	competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	created_by = models.ForeignKey(User, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

class DiscussionPost(models.Model):
	thread = models.ForeignKey(DiscussionThread, on_delete=models.CASCADE, related_name='posts')
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.author.username}: {self.content[:30]}"
