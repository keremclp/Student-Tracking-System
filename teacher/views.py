from django.shortcuts import render

# Create your views here.

def teacher_view(request):
    return render(request,'teacher/teacher_dashboard.html')