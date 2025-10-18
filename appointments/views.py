from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AppointmentForm, BarangayClearanceForm
from .models import Appointment, CertificationType

@login_required
def barangay_clearance(request):
    if request.method == 'POST':
        appointment_form = AppointmentForm(request.POST)
        clearance_form = BarangayClearanceForm(request.POST)

        if appointment_form.is_valid() and clearance_form.is_valid():
            cert_type, created = CertificationType.objects.get_or_create(name="Barangay Clearance")

            appointment = appointment_form.save(commit=False)
            appointment.user = request.user
            appointment.certificate_type = cert_type
            appointment.save()

            clearance = clearance_form.save(commit=False)
            clearance.appointment = appointment
            clearance.save()

            return redirect('indigency_certificate')
        
    else:
        appointment_form = AppointmentForm()
        clearance_form = BarangayClearanceForm()
        
        context = {
            'appointment_form': appointment_form,
            'clearance_form': clearance_form,
        }

    return render(request, 'appointments/barangay_clearance.html', context)

def certificate_of_indigency(request):
    return render(request, 'appointments/certificate_of_indigency.html')

def comm_tax_certificate(request):
    return render(request, 'appointments/comm_tax_certificate.html')

def solo_parent_certificate(request):
    return render(request, 'appointments/solo_parent_certificate.html')