from django.db import models
from django.conf import settings

# Create your models here.
class CertificationType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
class Appointment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    certificate_type = models.ForeignKey(CertificationType, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    purpose = models.CharField(max_length=200, help_text="e.g. Employment, Business Permit, Government Benefits")
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.get_full_name()}'s appointment for {self.certificate_type.name} on {self.appointment_date}"
    
class BarangayClearance(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    civil_status = models.CharField(
        max_length=50,
        choices = [
            ('single', 'Single'),
            ('married', 'Married'),
            ('widowed', 'Widowed'),
            ('divorced', 'Divorced'),
        ],
    )
    citizenship = models.CharField(max_length=50)
    has_derogatory_record = models.BooleanField(default=False)

    def __str__(self):
        return f"Clearance for {self.appointment.user.get_full_name()}"
    
class CertificateOfIndigency(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    present_address = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)

    def __str__(self):
        return f"Certificate of Indigency for {self.full_name}"
    
class CommunityTaxCertificate(models.Model):
    SEX_CHOICES = (('Male', 'Male'), ('Female', 'Female'))
    CIVIL_STATUS_CHOICES = (('Single', 'Single'), ('Married', 'Married'), ('Widowed', 'Widowed'), ('Separated', 'Separated'))

    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE, primary_key=True)
    address = models.CharField(max_length=255)
    sex = models.CharField(max_length=10, choices=SEX_CHOICES)
    civil_status = models.CharField(max_length=20, choices=CIVIL_STATUS_CHOICES)
    citizenship = models.CharField(max_length=50)
    occupation_or_business = models.CharField(max_length=255)

    def __str__(self):
        return f"Community Tax Certificate for {self.full_name}"