from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import JobPostingForm
from .models import JobPosting,Company
from .forms import CompanyForm
from django.shortcuts import render, redirect, get_object_or_404
from jobseeker.forms import JobSeekerForm
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from jobseeker.models import JobApplication
from .serializers import JobApplicationSerializer
from jobseeker.serializers import JobSeekerSerializer
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.http import JsonResponse
from jobseeker.models import JobSeeker
from django.http import HttpResponse
from django.utils.html import strip_tags


@login_required
def hr_dashboard(request):
    posts = JobPosting.objects.all().order_by('-posted_on')
    return render (request,'hr-dashboard.html', {'posts':posts})

def jobpost(request):
    return render(request,'base1.html')


@login_required
def create_job_posting(request):
    if request.method == 'POST':
        form = JobPostingForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_job_posting = JobPosting(
                company=data['company'],
                title=data['title'],
                job_description=data['job_description'],
                requirements=data['requirements']
            )
            new_job_posting.save()
            messages.success(request, 'Job Posting Created Successfully')
            return redirect('hr-dashboard')
    else:
        form = JobPostingForm()

    return render(request, 'create_post.html', {'form': form})

def read_post_page(request,pk):
    post = JobPosting.objects.get(pk=pk)
    post.views +=1
    post.save()
    return render(request, 'read_post.html',{'post' : post})


@login_required
def my_posts(request):
    hr_user = request.user
    # Assuming company is the related_name in the JobPosting model
    posts = JobPosting.objects.filter(company__company_hr=hr_user).order_by('-posted_on')
    return render(request, 'my_posts.html', {'posts': posts})



@login_required
def company_list(request):
    companies = Company.objects.filter(company_hr=request.user)
    return render(request, 'company_list.html', {'companies': companies})

@login_required
def update_company(request, company_id):
    company = get_object_or_404(Company, id=company_id, company_hr=request.user)

    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfully')
            return redirect('company-list')
    else:
        form = CompanyForm(instance=company)
    return render(request, 'update_company.html', {'form': form, 'company': company})

# update and delete 

def update_job_posting(request, pk):

    job_posting = get_object_or_404(JobPosting, pk=pk)


    if request.user != job_posting.company.company_hr:
       
        return redirect('hr-dashboard')  

    if request.method == 'POST':
      
        form = JobPostingForm(request.POST, instance=job_posting)
        if form.is_valid():
            form.save()
            messages.success(request, ' Post Updated Successfully')
            return redirect('read-page', pk=pk) 
    else:
  
        form = JobPostingForm(instance=job_posting)

    return render(request, 'update_post.html', {'form': form, 'job_posting': job_posting})

def delete_job_posting(request, pk):
 
    job_posting = get_object_or_404(JobPosting, pk=pk)

  
    if request.user != job_posting.company.company_hr:
        messages.success(request, ' Post Deleted Successfully')
        return redirect('hr-dashboard')  

    if request.method == 'POST':

        job_posting.delete()
        return redirect('hr-dashboard') 

    return render(request, 'delete_post.html', {'job_posting': job_posting})



@api_view(['GET'])
def applied_jobseekers(request, job_posting_id):
    job_posting = get_object_or_404(JobPosting, id=job_posting_id)
    applied_applications = job_posting.jobapplication_set.all()

    jobseeker_details = []
    for application in applied_applications:
        jobseeker = application.applicant
        jobseeker_serializer = JobSeekerSerializer(jobseeker)  # Serialize jobseeker details
        application_serializer = JobApplicationSerializer(application)  # Serialize job application details
        jobseeker_details.append({'jobseeker': jobseeker_serializer.data, 'application': application_serializer.data})
    
    return render(request,'applied_jobseekers.html', {'job_posting': job_posting.id, 'applied_jobseekers': jobseeker_details})
    # return Response({'job_posting': job_posting.id, 'applied_jobseekers': jobseeker_details})
    

def hire_jobseeker(request):
    if request.method == 'POST':
        application_id = request.POST.get('application_id')
        job_application = get_object_or_404(JobApplication, id=application_id)

        # Update status to "hired"
        job_application.status = 'hired'
        job_application.save()
        
        # Send email notification to the hired jobseeker
        subject = 'Congratulations! You have been hired'
        html_message = render_to_string('hire_email_template.html',{'job_seeker': job_application.applicant})
        message = strip_tags(html_message)
        from_email = 'donisravanth@gmail.com'  # Update with your email
        recipient_list = [job_application.applicant.user.email]
        send_mail(subject=subject,html_message=html_message, message=message,
                        from_email=from_email, recipient_list=recipient_list)

        # return HttpResponse('Job seeker hired successfully and email sent.')
        messages.success(request, 'Job seeker hired successfully and email sent Successfully')
        return redirect('my-posts') 
    else:
         return HttpResponse('Invalid request method.')