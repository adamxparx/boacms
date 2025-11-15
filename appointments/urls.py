from django.urls import path
from . import views
from .views import RequirementsView

urlpatterns = [
    path('appointments/', views.appointments, name='appointments'),
    path('staff_appointments/', views.staff_appointments, name='staff_appointments'),
    path('certification/', views.create_appointment, name='certification'),
    path('confirmation/<int:appointment_id>/', views.confirmation, name='confirmation'),
    path('cancel/<int:appointment_id>/', views.cancel_appointment, name='cancel_appointment'),
    path('requirements/', RequirementsView.as_view(), name='requirements'),
]