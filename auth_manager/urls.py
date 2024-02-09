from django.urls import path
from .import views

urlpatterns = [
    path('',views.home_page,name='home_page'),
    path('login', views.login_user, name='login-page'),
    path('compnayregister/',views.company_registration, name='company_registration'),
    path('jobseekerregister/', views.job_seeker_registration, name='jobseeker_registration'),
    path('logout/',views.logout_user,name='logout-user')
]
