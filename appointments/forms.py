from django import forms
from .models import Appointment, BarangayClearance

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