from django.shortcuts import get_object_or_404, redirect, render
from student.forms import StudentProfileModelForm

# Models
from student.models import StudentProfile
from classroom.models import Classroom, Timetable

from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='account:login_view')
def student_dashboard(request, ):
    # Ders programında aynı gün farklı hocaların dersi olacak, ona göre ayarlama yapılması gerekiyor
    user = request.user
    user_slug = StudentProfile.objects.get(user=user).slug
    profile = get_object_or_404(StudentProfile, slug=user_slug)
    student_classroom = profile.classroom
    print(student_classroom)
    try:
        classroom_instance = None
        if student_classroom is not None:
            classroom_instance = student_classroom.classroom # It has to be Classroom istance, when remove classroom in here you got Studentclassroom instace
        print(classroom_instance)
        timetables = Timetable.objects.filter(classroom=classroom_instance)
    except Timetable.DoesNotExist:
        timetables = None

    context = dict(
        timetables = timetables
    )
    return render(request, 'student/student_dasboard.html', context)


@login_required(login_url='account:login_view')
def student_profile_overview(request, user_slug):
    profile = get_object_or_404(StudentProfile, slug=user_slug)
    context = dict(
        profile=profile,
    )
    return render(request, 'student/student_profile/profile_overview.html', context)


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
    return render(request, 'student/student_profile/profile_settings.html', context)


# Check the profile_iamge attribute error!!
