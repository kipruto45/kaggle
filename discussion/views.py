
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import DiscussionThread, DiscussionPost
from competitions.models import Competition

def thread_list(request, competition_id):
	competition = get_object_or_404(Competition, pk=competition_id)
	threads = DiscussionThread.objects.filter(competition=competition)
	return render(request, 'discussion/thread_list.html', {'competition': competition, 'threads': threads})

@login_required
def create_thread(request, competition_id):
	competition = get_object_or_404(Competition, pk=competition_id)
	if request.method == 'POST':
		title = request.POST.get('title')
		if title:
			thread = DiscussionThread.objects.create(
				competition=competition,
				title=title,
				created_by=request.user
			)
			return redirect('discussion:thread_detail', thread_id=thread.id)
	return render(request, 'discussion/create_thread.html', {'competition': competition})

def thread_detail(request, thread_id):
	thread = get_object_or_404(DiscussionThread, pk=thread_id)
	posts = thread.posts.all()
	if request.method == 'POST' and request.user.is_authenticated:
		content = request.POST.get('content')
		if content:
			DiscussionPost.objects.create(thread=thread, author=request.user, content=content)
			return redirect('discussion:thread_detail', thread_id=thread.id)
	return render(request, 'discussion/thread_detail.html', {'thread': thread, 'posts': posts})
