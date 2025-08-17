
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Competition, Submission
from .forms import CompetitionForm, SubmissionForm
from leaderboard.models import LeaderboardEntry

def list_competitions(request):
	competitions = Competition.objects.all()
	return render(request, 'competitions/list.html', {'competitions': competitions})

@login_required
def create_competition(request):
	if request.method == 'POST':
		form = CompetitionForm(request.POST)
		if form.is_valid():
			comp = form.save(commit=False)
			comp.host = request.user
			comp.save()
			return redirect('competitions:list')
	else:
		form = CompetitionForm()
	return render(request, 'competitions/create.html', {'form': form})

def competition_detail(request, pk):
	competition = get_object_or_404(Competition, pk=pk)
	leaderboard = LeaderboardEntry.objects.filter(competition=competition).order_by('rank')
	return render(request, 'competitions/detail.html', {'competition': competition, 'leaderboard': leaderboard})

@login_required
def submit_solution(request, pk):
	competition = get_object_or_404(Competition, pk=pk)
	if request.method == 'POST':
		form = SubmissionForm(request.POST, request.FILES)
		if form.is_valid():
			submission = form.save(commit=False)
			submission.competition = competition
			submission.participant = request.user
			submission.save()
			# Placeholder: scoring logic should be added here
			return redirect('competitions:detail', pk=competition.pk)
	else:
		form = SubmissionForm()
	return render(request, 'competitions/submit.html', {'form': form, 'competition': competition})
