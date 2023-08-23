from django.shortcuts import get_object_or_404, redirect, render
from student.forms import StudentProfileModelForm
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
    user = request.user
    profile = get_object_or_404(StudentProfile, slug=user_slug)
    initial_data = dict(
        first_name = user.first_name,
        last_name = user.last_name,
    )
    form = StudentProfileModelForm(instance= profile, initial=initial_data)
    if request.method == "POST":
        form = StudentProfileModelForm(
            request.POST or None, 
            request.FILES or None, 
            instance= profile
        )
        if form.is_valid():
            f = form.save(commit=False)
            print(form.cleaned_data)
            profile.user.first_name = form.cleaned_data.get('first_name')
            profile.user.last_name = form.cleaned_data.get('last_name')
            profile.user.profile_image = form.cleaned_data.get('profile_image')
            profile.save()
            f.save()
            return redirect('student:student_profile_overview', user_slug=user_slug)
    

    context = dict(
        form = form,
        title = "Edit Profile",
        profile=profile,
    )
    return render(request, 'student/student_profile/profile_settings.html',context)
