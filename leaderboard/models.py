
from django.db import models
from competitions.models import Competition, Submission

class LeaderboardEntry(models.Model):
	competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
	submission = models.OneToOneField(Submission, on_delete=models.CASCADE)
	score = models.FloatField()
	rank = models.PositiveIntegerField()
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		unique_together = ('competition', 'submission')
		ordering = ['rank']

	def __str__(self):
		return f"{self.competition.title} - {self.submission.participant.username} - Rank {self.rank}"
