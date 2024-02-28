from django.http import JsonResponse
from django.db.models import Q
from django.shortcuts import redirect, render
from django.contrib import messages

from attendance.forms import TeacherCreateAttendance
from student.models import StudentProfile
# Create your views here.


def search_students(request):
    if request.method == "GET":
        query = request.GET.get('q', '')
        students = StudentProfile.objects.filter(
            Q(user__first_name__icontains=query) | Q(user__last_name__icontains=query))
        data = [{'id': student.pk, 'text': student.user.get_full_name()}
                for student in students]
        return JsonResponse({'results': data})
    return JsonResponse({}, status=400)

# TODO: Validation of filtering students from StudentProfile model!
# TODO: Keep in mind that the students should be filtered by the teacher's classroom
def create_attendance_record(request):
    form = TeacherCreateAttendance()
    if request.user.role != 'teacher':
        messages.info(request, 'You are not authorized to access this page')
        return redirect('student:student_dashboard')
    if request.method == "POST":
        print(request.POST)
        form = TeacherCreateAttendance(request.POST)
        if form.is_valid():
            # Get selected students and save the attendance record for each student on the StudentProfile mdoel at attendance_record field
            students = form.cleaned_data['students']
            date = form.cleaned_data['date']
            status = form.cleaned_data['status']
            for student in students:
                student.attendance_records.create(date=date, status=status)
            messages.success(request, 'Attendance record created successfully')
            return redirect('attendance:create_attendance_record')
        else:
            messages.error(request, 'Please correct the errors below')
            return redirect('teacher:teacher_dashboard')
    context = dict(
        title='Create Attendance Record',
        form=form,
    )
    return render(request, 'attendance/create_attendance_record.html', context)

