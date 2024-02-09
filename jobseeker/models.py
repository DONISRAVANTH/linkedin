from django.db import models
from auth_manager.models import CustomUser
from company.models import JobPosting

class JobSeeker(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255,null=True,blank=True)
    email = models.EmailField(max_length=254,null=True,blank=True)
    bio = models.TextField()
    skills = models.TextField()
    experience = models.TextField()
    education = models.TextField()
    resume = models.FileField(upload_to='resume/', blank=True, null=True)
    Phone = models.CharField(max_length=10,null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    website = models.URLField(null=True,blank=True)
    github = models.URLField(null=True,blank=True)
    twitter = models.URLField(null=True,blank=True)
    instagram = models.URLField(null=True,blank=True)
    profile = models.ImageField(upload_to='profile/', blank=True, null=True) 
    
    
    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('hired', 'Hired'),
        # Add more status choices as needed
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='applied')
    
    def __str__(self):
        return self.user.username  # Or any other field that uniquely identifies the user

class JobApplication(models.Model):
    job = models.ForeignKey(JobPosting, on_delete=models.CASCADE)
    applicant = models.ForeignKey(JobSeeker, on_delete=models.CASCADE)
    date_applied = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.applicant.user.username} - {self.job.title}"


