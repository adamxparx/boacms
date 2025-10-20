from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AppointmentForm, BarangayClearanceForm, CertificateOfIndigencyForm, CommunityTaxCertificateForm
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

            return redirect('appointments')
        
    else:
        appointment_form = AppointmentForm()
        clearance_form = BarangayClearanceForm()
        
        context = {
            'appointment_form': appointment_form,
            'clearance_form': clearance_form,
        }

    return render(request, 'appointments/barangay_clearance.html', context)

@login_required
def certificate_of_indigency(request):
    if request.method == 'POST':
        appointment_form = AppointmentForm(request.POST)
        clearance_form = CertificateOfIndigencyForm(request.POST)

        if appointment_form.is_valid() and clearance_form.is_valid():
            cert_type, created = CertificationType.objects.get_or_create(name="Certificate of Indigency")

            appointment = appointment_form.save(commit=False)
            appointment.user = request.user
            appointment.certificate_type = cert_type
            appointment.save()

            clearance = clearance_form.save(commit=False)
            clearance.appointment = appointment
            clearance.save()

            return redirect('appointments')
        
    else:
        appointment_form = AppointmentForm()
        clearance_form = CertificateOfIndigencyForm()
        
        context = {
            'appointment_form': appointment_form,
            'clearance_form': clearance_form,
        }

    return render(request, 'appointments/certificate_of_indigency.html', context)

@login_required
def comm_tax_certificate(request):
    if request.method == 'POST':
        appointment_form = AppointmentForm(request.POST)
        clearance_form = CommunityTaxCertificateForm(request.POST)

        if appointment_form.is_valid() and clearance_form.is_valid():
            cert_type, created = CertificationType.objects.get_or_create(name="Community Tax Certificate")

            appointment = appointment_form.save(commit=False)
            appointment.user = request.user
            appointment.certificate_type = cert_type
            appointment.save()

            clearance = clearance_form.save(commit=False)
            clearance.appointment = appointment
            clearance.save()

            return redirect('appointments')
        
    else:
        appointment_form = AppointmentForm()
        clearance_form = CommunityTaxCertificateForm()
        
        context = {
            'appointment_form': appointment_form,
            'clearance_form': clearance_form,
        }

    return render(request, 'appointments/comm_tax_certificate.html', context)

def solo_parent_certificate(request):
    return render(request, 'appointments/solo_parent_certificate.html')

@login_required
def appointments(request):
    user_appointments = Appointment.objects.filter(user=request.user).order_by('-appointment_date', '-appointment_time')

    context = {
        'appointments': user_appointments
    }

    return render(request, 'appointments/appointment.html', context)

@login_required
def staff_appointments(request):
    all_appointments = Appointment.objects.all().order_by('-appointment_date', '-appointment_time')

    context = {
        'appointments': all_appointments
    }

    return render(request, 'appointments/staff_appointment.html', context)