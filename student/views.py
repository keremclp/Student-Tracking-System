from django.shortcuts import get_object_or_404, render
from account.models import User
from student.models import StudentProfile
# Create your views here.


def student_view(request):
    return render(request, 'student/student_dasboard.html')


def student_profile(request,user_slug):
    profile = get_object_or_404(StudentProfile, slug=user_slug)
    context = dict(
        profile=profile,
    )
    return render(request, 'student/student_profile/profile_overview.html', context)