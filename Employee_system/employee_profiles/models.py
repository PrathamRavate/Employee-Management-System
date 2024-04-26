
from django.db import models
from django.contrib.auth.models import User
import uuid


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=False)
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=64)
    contact = models.CharField(max_length=64)
    joining_date = models.DateField()
    salary = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    DEPARTMENT_CHOICES = (
        ('Engineering', 'Engineering'),
        ('SAP', 'SAP'),
        ('FullStack Developer', 'FullStack Developer'),
        ('SAP_FICO', 'SAP_FICO'),
        ('Sales', 'Sales'),
    )
    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES)
    POSITION_CHOICES = (
        ('Trainee', 'Trainee'),
        ('Associate', 'Associate'),
        ('Consultant', 'Consultant'),
        ('Senior Associate', 'Senior Associate'),
        ('Manager', 'Manager'),
    )
    position = models.CharField(max_length=20, choices=POSITION_CHOICES)
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name


class Leave(models.Model):
    leave_code = models.UUIDField(default=uuid.uuid4, blank=True, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,
                                blank=True, null=True)
    LEAVE_CHOICES = (
        ('Sick Leave', 'Sick Leave'),
        ('Paid Leave', 'Piad Leave'),
        ('Others', 'Others')
    )
    leave_type = models.CharField(max_length=20, choices=LEAVE_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    STATUS_CHOICES = (
        ('1', 'Approved'),
        ('2', 'Rejected'),
        ('3', 'Registered'),
        ('4', 'Cancelled'),
        )
    status = models.CharField(max_length=20,
                              choices=STATUS_CHOICES, blank=False)
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.id}"
