from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLES = [
        ('jobseeker', 'Job Seeker'),
        ('company_hr', 'Company HR'),
    ]
    role = models.CharField(max_length=20, choices=ROLES)
    fullname = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.username