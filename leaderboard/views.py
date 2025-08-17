
from django.shortcuts import render, get_object_or_404
from .models import LeaderboardEntry
from competitions.models import Competition

def leaderboard_view(request, competition_id):
	competition = get_object_or_404(Competition, pk=competition_id)
	entries = LeaderboardEntry.objects.filter(competition=competition).order_by('rank')
	return render(request, 'leaderboard/leaderboard.html', {'competition': competition, 'entries': entries})
