from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

phone_regex = RegexValidator(
    regex=r'^\d{10,15}$',
    message="Email must be between 10 and 15 digits."
)

ROLE_CHOICES = (
    ('resident', 'Resident'),
    ('barangay_staff', 'Barangay Staff'),
)

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(
        validators=[phone_regex],
        unique=True,
        blank=True,
        null=True,
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='resident')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []