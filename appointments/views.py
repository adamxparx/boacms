from django.shortcuts import render

def certification(request):
    return render(request, 'appointments/certification.html')