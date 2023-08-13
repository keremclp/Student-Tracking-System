from django.shortcuts import get_object_or_404, render
from student.models import StudentProfile
# Create your views here.


def student_view(request):
    return render(request, 'student/student_dasboard.html')


def student_profile_overview(request,user_slug):
    profile = get_object_or_404(StudentProfile, slug=user_slug)
    context = dict(
        profile=profile,
    )
    return render(request, 'student/student_profile/profile_overview.html', context)

def student_profile_settings(request):
    return render(request, 'student/student_profile/profile_settings.html')
