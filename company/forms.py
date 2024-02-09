from django import forms
from .models import JobPosting, Company

class JobPostingForm(forms.ModelForm):
    class Meta:
        model = JobPosting
        fields = ['company', 'title', 'job_description', 'requirements']

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'description', 'location']
