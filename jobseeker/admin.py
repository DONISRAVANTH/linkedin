from django.contrib import admin

# Register your models here.

from .models import JobSeeker,JobApplication,Notification

admin.site.register(JobSeeker)

admin.site.register(JobApplication)

admin.site.register(Notification)