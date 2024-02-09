from django.shortcuts import render, redirect
from company.models import JobPosting
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import JobSeekerForm, JobApplicationForm
from .models import JobSeeker, JobApplication
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse


# Create your views here.

@login_required
def jobseeker_dashboard(request):
    posts = JobPosting.objects.all().order_by('-posted_on')
    jobseeker = JobSeeker.objects.get(user=request.user)
    return render(request, 'jobseeker-dashboard.html', {'posts': posts , 'jobseeker': jobseeker})


@login_required
def read_post(request, pk):
    post = JobPosting.objects.get(pk=pk)
    post.views += 1
    post.save()
    jobseeker = JobSeeker.objects.get(user=request.user)
    applied = JobApplication.objects.filter(
        applicant=jobseeker, job=post).exists()
    return render(request, 'readpost.html', {'post': post, 'applied': applied})


@login_required
def job_seeker_form(request):
    if request.method == 'POST':
        form = JobSeekerForm(request.POST, request.FILES)
        if form.is_valid():
            jobseeker = form.save(commit=False)
            jobseeker.user = request.user
            jobseeker.save()
            return redirect('job_seeker_profile')
    else:
        form = JobSeekerForm()

    return render(request, 'job_seeker_form.html', {'form': form})


@login_required
def update_job_seeker_form(request):
    jobseeker = JobSeeker.objects.get(user=request.user)

    if request.method == 'POST':
        form = JobSeekerForm(request.POST, request.FILES, instance=jobseeker)
        if form.is_valid():
            form.save()
            return redirect('job_seeker_profile')
    else:
        form = JobSeekerForm(instance=jobseeker)

    return render(request, 'update_job_seeker_form.html', {'form': form})

# -----------


@login_required
def job_applications(request, post_id):
    user = request.user
    post = JobPosting.objects.get(pk=post_id)
    job_applications = JobApplication.objects.filter(job=post)
    return render(request, 'job_applications.html', {'user': user, 'post': post, 'job_applications': job_applications})


@login_required
def job_seeker_profile(request):
    try:
        job_seeker = JobSeeker.objects.get(user=request.user)
    except JobSeeker.DoesNotExist:
        job_seeker = None

    if request.method == 'POST':
        form = JobSeekerForm(request.POST, instance=job_seeker)
        if form.is_valid():
            job_seeker = form.save(commit=False)
            job_seeker.user = request.user
            job_seeker.save()
            return redirect('job_seeker_profile')
    else:
        form = JobSeekerForm(instance=job_seeker)

    return render(request, 'job_seeker_profile.html', {'form': form, 'job_seeker': job_seeker})


@api_view(['POST'])
@login_required
def apply_job(request, post_pk):
    try:
        job_posting = get_object_or_404(JobPosting, pk=post_pk)

        if not request.user.is_authenticated:
            return Response({'status': 'error', 'message': 'Authentication required'}, status=401)

        job_seeker = JobSeeker.objects.get(user=request.user)

        existing_application = JobApplication.objects.filter(
            job=job_posting, applicant=job_seeker).exists()

        if existing_application:
            return Response({'status': 'error', 'message': 'You have already applied for this job'}, status=400)

        job_application = JobApplication.objects.create(
            job=job_posting, applicant=job_seeker)
        return Response({'status': 'success'})

    except Exception as e:

        return Response({'status': 'error', 'message': str(e)}, status=500)
