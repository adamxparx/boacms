from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AppointmentForm, BarangayClearanceForm, CertificateOfIndigencyForm, CommunityTaxCertificateForm, SoloParentCertificateForm
from .models import Appointment, CertificationType
from django.contrib import messages

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

            return redirect('confirmation', appointment_id=appointment.id)
        
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

            return redirect('confirmation', appointment_id=appointment.id)
        
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

            return redirect('confirmation', appointment_id=appointment.id)
        
    else:
        appointment_form = AppointmentForm()
        clearance_form = CommunityTaxCertificateForm()
        
        context = {
            'appointment_form': appointment_form,
            'clearance_form': clearance_form,
        }

    return render(request, 'appointments/comm_tax_certificate.html', context)

@login_required
def solo_parent_certificate(request):
    if request.method == 'POST':
        appointment_form = AppointmentForm(request.POST)
        clearance_form = SoloParentCertificateForm(request.POST)

        if appointment_form.is_valid() and clearance_form.is_valid():
            cert_type, created = CertificationType.objects.get_or_create(name="Solo Parent Certificate")

            appointment = appointment_form.save(commit=False)
            appointment.user = request.user
            appointment.certificate_type = cert_type
            appointment.save()

            clearance = clearance_form.save(commit=False)
            clearance.appointment = appointment
            clearance.save()

            return redirect('confirmation', appointment_id=appointment.id)
        
    else:
        appointment_form = AppointmentForm()
        clearance_form = SoloParentCertificateForm()
        
        context = {
            'appointment_form': appointment_form,
            'clearance_form': clearance_form,
        }

    return render(request, 'appointments/solo_parent_certificate.html', context)

@login_required
def appointments(request):
    user_appointments = Appointment.objects.filter(user=request.user).order_by('-appointment_date', '-appointment_time')

    context = {
        'appointments': user_appointments
    }

    return render(request, 'appointments/appointment.html', context)

@login_required
def confirmation(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id, user=request.user)

    cert_name = appointment.certificate_type.name
    context = {
        'appointment': appointment,
        'certificate_name': cert_name,
    }

    # Attach certificate-specific details if they exist
    if cert_name == "Barangay Clearance":
        try:
            context['barangay_clearance'] = appointment.barangayclearance
        except Exception:
            pass
    elif cert_name == "Certificate of Indigency":
        try:
            context['indigency'] = appointment.certificateofindigency
        except Exception:
            pass
    elif cert_name == "Community Tax Certificate":
        try:
            context['community_tax_certificate'] = appointment.communitytaxcertificate
        except Exception:
            pass
    elif cert_name == "Solo Parent Certificate":
        try:
            context['solo_parent_certificate'] = appointment.soloparentcertificate
        except Exception:
            pass

    return render(request, 'appointments/confirmation.html', context)


@login_required
def staff_appointments(request):
    all_appointments = Appointment.objects.all().order_by('-appointment_date', '-appointment_time')

    if request.method == "POST":
        appointment_id = request.POST.get("appointment_id")
        appointment = Appointment.objects.get(id=appointment_id)
        appointment.is_completed = not appointment.is_completed
        appointment.save()
        return redirect('staff_appointments')

    context = {
        'appointments': all_appointments,
    }

    return render(request, 'appointments/staff_appointment.html', context)

@login_required
def cancel_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id, user=request.user)
    
    if request.method == 'POST':
        # If form is submitted with confirmation
        appointment.delete()
        messages.success(request, 'Appointment has been cancelled successfully.')
        return redirect('appointments')
    
    # If GET request, show confirmation page
    context = {
        'appointment': appointment,
    }
    return render(request, 'appointments/confirm_cancel.html', context)