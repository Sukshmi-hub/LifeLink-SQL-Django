from django.db import models

# Create your models here.

from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    ROLE_CHOICES = [
        ('Patient', 'Patient'),
        ('Donor', 'Donor'),
        ('Hospital', 'Hospital'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return self.name


class Request(models.Model):
    patient_name = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=10)
    organ_needed = models.CharField(max_length=50)
    hospital_name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default="Pending")

    def __str__(self):
        return self.patient_name


class RedAlert(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message[:20]
