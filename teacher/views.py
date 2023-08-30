from django.shortcuts import render

# Create your views here.

def teacher_dashboard(request):
    return render(request,'teacher/teacher_dashboard.html')

def teacher_profile_overview(request):
    profile = 
    return render(request,'teacher/teacher_profile/teacher_profile_overview.html')