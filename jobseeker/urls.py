from django.urls import path
from .import views

urlpatterns = [
    path('jobseekerdashboard/',views.jobseeker_dashboard,name='jobseeker-dashboard'),
    path('readposts/<int:pk>',views.read_post,name='readposts'),
    path('job-seeker-form/', views.job_seeker_form, name='job_seeker_form'),
    path('job_applications/<int:post_id>/', views.job_applications, name='job_application_form'),
    path('job-seeker-profile/', views.job_seeker_profile, name='job_seeker_profile'),
    path('update_job_seeker_form/', views.update_job_seeker_form, name='update_jobseeker'),
    path('apply_job/<int:post_pk>/', views.apply_job, name='apply_job'),
    
]