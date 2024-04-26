from django.db import models
from employee_profiles.models import Profile


class Attendance(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,
                                blank=True, null=True)
    date = models.DateField()
    time_in = models.TimeField()
    time_out = models.TimeField()
    STATUS_CHOICE = (
        ('1', 'Present'),
        ('2', 'Absent'),
        ('3', 'Late')
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICE)
