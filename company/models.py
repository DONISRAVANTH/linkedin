from django.db import models
from auth_manager.models import CustomUser

class Company(models.Model):
    company_hr = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name='hr_of_company')
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name    

class JobPosting(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    job_description = models.TextField()
    requirements = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default = 0)


    def __str__(self):
        return self.title
