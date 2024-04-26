from django.db import models
from employee_profiles.models import Profile


class Project (models.Model):
    name = models.CharField(max_length=64)
    PROJECT_CHOICES = (
        ('1', 'Support'),
        ('2', 'Implementation'),
    )
    project_type = models.CharField(max_length=64, choices=PROJECT_CHOICES)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    completed = models.BooleanField()
    project_description = models.TextField()
    EXECUTION_TYPE_CHOICE = (
        ('1', 'Onsite'),
        ('2', 'Offsite'),
    )
    execution_type = models.CharField(
        max_length=1,
        choices=EXECUTION_TYPE_CHOICE,
        null=False,
        blank=False,
        default=None
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}"
