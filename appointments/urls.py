from django.urls import path
from . import views

urlpatterns = [
    path('barangay_clearance/', views.barangay_clearance, name='barangay_clearance'),
    path('certificate_of_indigency/', views.certificate_of_indigency, name='indigency_certificate'),
    path('community_tax_certificate/', views.comm_tax_certificate, name='comm_tax_cert'),
    path('solo_parent_certificate/', views.solo_parent_certificate, name='solo_parent_cert'),
] 