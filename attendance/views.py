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
            form.save()
            return redirect('teacher:teacher_dashboard')
    context = dict(
        title='Create Attendance Record',
        form=form,
    )
    return render(request, 'attendance/create_attendance_record.html', context)

