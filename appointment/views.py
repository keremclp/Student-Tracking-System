from django.shortcuts import render

# Create your views here.
def create_appointment(request):
    return render(request, 'appointment/create_appointment.html')