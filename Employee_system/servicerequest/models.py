from django.db import models
from employee_profiles.models import Profile


class ServiceRequest(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    SERVICE_CHOICE = (
        ("1", "Hardware"),
        ("2", "Software"),
    )
    servicetype = models.CharField(max_length=64, choices=SERVICE_CHOICE)
    manufacturer = models.TextField()
    title = models.TextField()
    description = models.TextField()
    asset = models.IntegerField()
    STATUS = (
        ("1", "Registered"),
        ("2", "Assigned"),
        ("3", "Resolved"),
        ("4", "Completed"),
        ("5", "Replaced"),       
    )
    status = models.CharField(max_length=64, choices=STATUS, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now=True, null=True)

