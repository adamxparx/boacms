from django.urls import path
from . import views

urlpatterns = [
    path('appointments/', views.appointments, name='appointments'),
    path('staff_appointments/', views.staff_appointments, name='staff_appointments'),
    path('barangay_clearance/', views.barangay_clearance, name='barangay_clearance'),
    path('certificate_of_indigency/', views.certificate_of_indigency, name='indigency_certificate'),
    path('community_tax_certificate/', views.comm_tax_certificate, name='comm_tax_cert'),
    path('solo_parent_certificate/', views.solo_parent_certificate, name='solo_parent_cert'),
] 