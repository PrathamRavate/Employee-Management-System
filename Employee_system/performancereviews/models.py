from django.db import models
from employee_profiles.models import Profile


class Review(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date = models.DateField()
    comments = models.CharField(max_length=64)
    ratings = models.CharField(max_length=64)
