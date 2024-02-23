from django.shortcuts import redirect, render
from django.contrib import messages

from attendance.forms import TeacherCreateAttendance
# Create your views here.


def create_attendance_record(request):
    form = TeacherCreateAttendance()
    if request.user.role != 'teacher':
        messages.info(request, 'You are not authorized to access this page')
        return redirect('student:student_dashboard')
    if request.method == "POST":
        form = TeacherCreateAttendance(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher:student_dashboard')
    context = dict(
        title='Create Attendance Record',
        form=form,
    )
    return render(request, 'attendance/create_attendance_record.html', context)
