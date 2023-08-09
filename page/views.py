from django.shortcuts import render


def student_view(request):
    return render(request,'page/student-dashboard/student_dasboard.html')