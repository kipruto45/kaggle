from django import forms
from .models import Competition, Submission

class CompetitionForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = ['title', 'description', 'dataset', 'prize', 'start_date', 'end_date', 'rules']

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['file']
