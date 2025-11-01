from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

class CustomUser(AbstractUser):
    username = None
    first_name = None
    last_name = None
    email = models.EmailField(unique=True)

    ROLE_CHOICES = (
        ('resident', 'Resident'),
        ('staff', 'Barangay Staff'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='resident')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Resident(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50)

    date_of_birth = models.DateField()
    address = models.CharField(max_length=255)

    PHONE_REGEX = RegexValidator(
        regex=r'^\d{10,15}$',
        message="Email must be between 10 and 15 digits."
    )
    phone_number = models.CharField(max_length=15, validators=[PHONE_REGEX])

    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    sex = models.CharField(max_length=10, choices=SEX_CHOICES)

    CIVIL_STATUS_CHOICES = [
        ('single', 'Single'),
        ('married', 'Married'),
        ('widowed', 'Widowed'),
        ('separated', 'Separated'),
    ]
    civil_status = models.CharField(max_length=20, choices=CIVIL_STATUS_CHOICES)

    citizenship = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"
    
class BarangayStaff(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    barangay_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.email} - {self.barangay_name}"
