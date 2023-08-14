from django.shortcuts import get_object_or_404, render
from student.models import StudentProfile

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='account:login_view')
def student_dashboard(request):
    user = request.user
    slug = StudentProfile.objects.get(user=user).slug
    context = dict(
        slug=slug,
    )
    return render(request, 'student/student_dasboard.html',context)

@login_required(login_url='account:login_view')
def student_profile_overview(request,user_slug):
    profile = get_object_or_404(StudentProfile, slug=user_slug)
    context = dict(
        profile=profile,
    )
    return render(request, 'student/student_profile/profile_overview.html', context)

def student_profile_edit(request,user_slug):
    profile = get_object_or_404(StudentProfile, slug=user_slug)
    context = dict(
        profile=profile,
    )
    return render(request, 'student/student_profile/profile_settings.html',context)
