from django import forms
from .models import JobSeeker, JobApplication


class JobSeekerForm(forms.ModelForm):
    class Meta:
        model = JobSeeker
        fields = '__all__'
       # # fields = ['name','email','bio', 'skills', 'experience', 'education','resume']

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['job', 'applicant', 'status']
