from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AppointmentForm
from .models import Appointment
from django.contrib import messages
from django.db import transaction

@login_required
def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    appointment = form.save(commit=False)
                    appointment.resident = request.user
                    appointment.save()
                    # messages.success(request, "Appointment booked successfully!")
                    return redirect('confirmation', appointment_id = appointment.id)
            except Exception as e:
                form.add_error(None, "There was an issue processing your booking. Please try again.")
    else:
        form = AppointmentForm()

    context = {
        'form': form
    }

    return render(request, 'appointments/certification.html', context)

@login_required
def appointments(request):
    user_appointments = Appointment.objects.filter(resident=request.user).order_by('-preferred_date', '-preferred_time')

    context = {
        'appointments': user_appointments
    }

    return render(request, 'appointments/appointment.html', context)

@login_required
def confirmation(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id, resident=request.user)

    cert_name = appointment.get_certificate_type_display()

    context = {
        'appointment': appointment,
        'certificate_name': cert_name,
    }

    return render(request, 'appointments/confirmation.html', context)


@login_required
def staff_appointments(request):
    if request.user.role != 'staff':
        messages.error(request, "You are not authorized to view this page.")
        return redirect('appointments')
    
    all_appointments = Appointment.objects.all().order_by('-preferred_date', '-preferred_time')

    if request.method == "POST":
        appointment_id = request.POST.get("appointment_id")
        appointment = get_object_or_404(Appointment, id=appointment_id)

        # Toggle between pending and approved
        if appointment.status == 'pending':
            appointment.status = 'approved'
        elif appointment.status == 'approved':
            appointment.status = 'pending'

        appointment.save()
        return redirect('staff_appointments')

    context = {'appointments': all_appointments}
    return render(request, 'appointments/staff_appointment.html', context)

@login_required
def cancel_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id, resident=request.user)

    if request.method == 'POST':
        appointment.status = 'cancelled'
        appointment.save()
        # messages.success(request, 'Appointment has been cancelled successfully.')
        return redirect('appointments')

    context = {'appointment': appointment}
    return render(request, 'appointments/confirm_cancel.html', context)