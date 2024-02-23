from itertools import groupby
from operator import attrgetter
from django.shortcuts import get_object_or_404, redirect, render
from student.forms import StudentProfileModelForm

# Models
from student.models import StudentProfile
from classroom.models import Classroom, Timetable
from assignment.models import Quiz, SolvedQuiz, AssignmentFile, UploadedSolution

from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='account:login_view')
def student_dashboard(request):
    user = request.user
    user_slug = StudentProfile.objects.get(user=user).slug
    profile = get_object_or_404(StudentProfile, slug=user_slug)
    student_classroom = profile.classroom

    try:
        classroom_instance = None
        if student_classroom is not None:
            classroom_instance = student_classroom.classroom
        timetables = Timetable.objects.filter(classroom=classroom_instance)
    except Timetable.DoesNotExist:
        timetables = []

    # Convert QuerySet to a list and then group timetables by day of the week
    timetables_list = list(timetables)
    timetables_list.sort(key=attrgetter('day_of_week')
                         )  # Sort by day_of_week field
    grouped_timetables = {}
    for day, day_timetables in groupby(timetables_list, key=lambda t: t.day_of_week):
        # Convert integer day to day name
        day_name = dict(Timetable.DAY_CHOICES)[day]
        grouped_timetables[day_name] = list(day_timetables)

    total_assignment = AssignmentFile.objects.all().count()
    total_quiz = Quiz.objects.all().count()
    solved_quiz_number = SolvedQuiz.objects.filter(student=profile).count()
    uploaded_solution = UploadedSolution.objects.filter(
        student=profile).count()
    context = dict(
        grouped_timetables=grouped_timetables,
        profile=profile,
        total_quiz=total_quiz,
        solved_quiz_number=solved_quiz_number,
        total_assignment=total_assignment,
        uploaded_solution=uploaded_solution
    )
    return render(request, 'student/student_dasboard.html', context)


@login_required(login_url='account:login_view')
def student_profile_overview(request, user_slug):
    profile = get_object_or_404(StudentProfile, slug=user_slug)
    context = dict(
        profile=profile,
    )
    return render(request, 'student/student_profile/student_profile_overview.html', context)


def student_profile_edit(request, user_slug):
    user = request.user
    profile = get_object_or_404(StudentProfile, slug=user_slug)
    initial_data = dict(
        first_name=user.first_name,
        last_name=user.last_name,
    )
    form = StudentProfileModelForm(instance=profile, initial=initial_data)
    if request.method == "POST":
        form = StudentProfileModelForm(
            request.POST or None,
            request.FILES or None,
            instance=profile
        )
        if form.is_valid():
            f = form.save(commit=False)
            print(form.cleaned_data)
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            new_profile_image = form.cleaned_data.get('profile_image')
            if new_profile_image:
                user.profile_image = new_profile_image
                user.save()

            user.save()
            profile.save()
            f.save()
            return redirect('student:student_profile_overview', user_slug=user_slug)

    context = dict(
        form=form,
        title="Edit Profile",
        profile=profile,
    )
    return render(request, 'student/student_profile/student_profile_settings.html', context)

# ATTENDANCE RECORD 

def create_attendance_record(request):
    return render(request, 'student/attendance/create_attendance_record.html', {})