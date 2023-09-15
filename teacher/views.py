from django.shortcuts import redirect, render, get_object_or_404
from teacher.models import TeacherProfile
from teacher.forms import TeacherProfileModelForm
# Create your views here.

def teacher_dashboard(request):
    return render(request,'teacher/teacher_dashboard.html')

def teacher_profile_overview(request, user_slug):
    teacher_profile = get_object_or_404(TeacherProfile, slug=user_slug)
    context = dict(
        profile=teacher_profile,
    )
    return render(request,'teacher/teacher_profile/teacher_profile_overview.html', context)

def teacher_profile_edit(request, user_slug):
    user = request.user
    profile = get_object_or_404(TeacherProfile, slug=user_slug)
    initial_data = dict(
        first_name=user.first_name,
        last_name=user.last_name,
    )
    form = TeacherProfileModelForm(instance=profile, initial=initial_data)
    if request.method == "POST":
        form = TeacherProfileModelForm(
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