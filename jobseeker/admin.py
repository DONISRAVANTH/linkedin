from django.contrib import admin

# Register your models here.

from .models import JobSeeker,JobApplication

admin.site.register(JobSeeker)

admin.site.register(JobApplication)