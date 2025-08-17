
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Dataset
from .forms import DatasetForm

@login_required
def upload_dataset(request):
	if request.method == 'POST':
		form = DatasetForm(request.POST, request.FILES)
		if form.is_valid():
			dataset = form.save(commit=False)
			dataset.uploaded_by = request.user
			dataset.save()
			return redirect('datasets:list')
	else:
		form = DatasetForm()
	return render(request, 'datasets/upload.html', {'form': form})

def list_datasets(request):
	datasets = Dataset.objects.filter(privacy='public')
	return render(request, 'datasets/list.html', {'datasets': datasets})
