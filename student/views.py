from django.shortcuts import render
from account.models import User
# Create your views here.


def student_view(request):
    return render(request, 'student/student_dasboard.html')


def student_profile(request):

    

    return render(request, 'student/student_profile.html')