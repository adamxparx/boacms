from django.shortcuts import render
from django.contrib.auth.decorators import login_required   

@login_required
def barangay_clearance(request):
    return render(request, 'appointments/barangay_clearance.html')

def certificate_of_indigency(request):
    return render(request, 'appointments/certificate_of_indigency.html')

def comm_tax_certificate(request):
    return render(request, 'appointments/comm_tax_certificate.html')

def solo_parent_certificate(request):
    return render(request, 'appointments/solo_parent_certificate.html')