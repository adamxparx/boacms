from django import forms
from .models import Appointment, BarangayClearance, CertificateOfIndigency, CommunityTaxCertificate, SoloParentCertificate


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['appointment_date', 'appointment_time', 'purpose']
        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date'}),
            'appointment_time': forms.TimeInput(attrs={'type': 'time'}),
        }

class BarangayClearanceForm(forms.ModelForm):
    class Meta:
        model = BarangayClearance
        fields = ['civil_status', 'citizenship']

class CertificateOfIndigencyForm(forms.ModelForm):
    class Meta:
        model = CertificateOfIndigency
        fields = ['present_address', 'contact_number']

class CommunityTaxCertificateForm(forms.ModelForm):
    class Meta: 
        model = CommunityTaxCertificate
        fields = ['address', 'sex', 'civil_status', 'citizenship', 'occupation_or_business']

class SoloParentCertificateForm(forms.ModelForm):
    class Meta:
        model = SoloParentCertificate
        fields = ['present_address', 'contact_number']
