from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import JobseekerRegistrationForm, CompanyRegistrationForm
from django.contrib import messages
from .models import CustomUser
from company.models import Company
from django.core.mail import send_mail


def home_page(request):
    return render(request, 'home.html')

# job_seeker Registration


def job_seeker_registration(request):
    if request.method == 'POST':
        form = JobseekerRegistrationForm(request.POST)

        if form.is_valid():
            fullname = form.cleaned_data['fullname']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            # Create a new CustomUser instance using create_user
            job_seeker = CustomUser.objects.create_user(
                username=username,
                email=email,
                password=password,
                fullname=fullname,
                role='jobseeker',  # Use 'jobseeker' as per the choices in your models.py
            )

            # Send Email Data
            subject = 'Welcome to LinkedIn!'
            from_email = 'donisravanth@gmail.com'
            recipient_list = [email]
            message = f"""
    Dear {username},

    Congratulations! You have successfully registered for LinkedIn, the world's largest professional network. 🎉

    Your new LinkedIn account is now ready for you to start connecting with professionals, exploring job opportunities, and building your online presence.

    Here are a few things you can do to get started:

    1. Complete your profile: Add your work experience, education, skills, and a professional profile picture to make your profile stand out.

    2. Explore job opportunities: Visit the LinkedIn Jobs section to search for job openings that match your skills and interests.

    Welcome aboard, and we wish you success in your professional journey!

    Best regards,
    The LinkedIn Team
    """
            send_mail(subject=subject, message=message,
                      from_email=from_email, recipient_list=recipient_list)

            messages.success(request, 'Job Seeker Registration Successful')
            return redirect('login-page')

    else:
        form = JobseekerRegistrationForm()

    return render(request, 'jobseeker_registration.html', {'form': form})

# Company & HR Registration


def company_registration(request):
    if request.method == 'POST':
        form = CompanyRegistrationForm(request.POST)

        if form.is_valid():
            company_name = form.cleaned_data['company_name']
            full_name = form.cleaned_data['fullname']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            # Assuming you have a create_user method in your CustomUser manager
            user_instance = CustomUser.objects.create_user(
                username=username,
                email=email,
                password=password,
                fullname=full_name,
                role='company_hr'
            )

            company_instance = Company.objects.create(
                company_hr=user_instance,
                name=company_name
                # Add other fields from your form as needed (e.g., description, location)
            )

            # Send Email Data
            subject = 'Welcome to LinkedIn!'
            from_email = 'donisravanth@gmail.com'
            recipient_list = [email]
            message = f"""
    Subject: {subject}

    Dear {username},

    Welcome to {company_name}'s HR Portal! 🎉

    We are thrilled to have you onboard as part of our HR team. With the HR Portal, you'll have access to a range of tools and resources to streamline your HR processes and support our employees.

    Here's what you can do with the HR Portal:

    - Job Posting and Recruitment: Post job openings, manage applications, and track the recruitment process all in one place.

    Please log in to the HR Portal using your credentials to explore these features and get started.

    Once again, welcome to the team! We look forward to working together to support our employees and achieve our company's goals.

    Best regards,
    The LinkedIn Team
    """
            send_mail(subject=subject, message=message,
                      from_email=from_email, recipient_list=recipient_list)

            messages.success(request, 'Company/HR Registration Successful')
            return redirect('login-page')

    else:
        form = CompanyRegistrationForm()

    return render(request, 'company_registration.html', {'form': form})

# Common Login Page


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'Login Successful')

                if user.role.lower() == 'jobseeker':
                    return redirect('jobseeker-dashboard')
                elif user.role.lower() == 'company_hr':
                    return redirect('hr-dashboard')
                else:
                    return redirect('home-page')
            else:
                messages.error(
                    request, 'Invalid username or password. Please try again.')

    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


# Logout
def logout_user(request):
    logout(request)
    messages.success(request, 'Logout Successful')
    return redirect('home_page')
