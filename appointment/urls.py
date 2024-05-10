from django.urls import path
from appointment.views import create_appointment

app_name = 'appointment'

urlpatterns = [
    path('create-appointment/', create_appointment, name='create-appointment')
]
