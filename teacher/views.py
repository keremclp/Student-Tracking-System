from django.shortcuts import render, get_object_or_404
from teacher.models import TeacherProfile
# Create your views here.

def teacher_dashboard(request):
    return render(request,'teacher/teacher_dashboard.html')

def teacher_profile_overview(request, user_slug):
    profile = get_object_or_404(TeacherProfile, slug=user_slug)

    context = dict(
        profile=profile,
        slug = user_slug,
    )
    return render(request,'teacher/teacher_profile/teacher_profile_overview.html', context)