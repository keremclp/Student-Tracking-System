from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login,logout
from account.forms import LoginForm, SignUpForm
from student.models import StudentProfile
from teacher.models import TeacherProfile
def login_view(request):
    
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.role == 'student':
                login(request, user)
                return redirect('student:student_dashboard')
            elif user is not None and user.role == 'teacher':
                login(request, user)
                return redirect('teacher:teacher_dashboard')
            elif user is not None and user.role == 'parent':
                login(request, user)
                return redirect('employee')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'account/login.html', {'form': form, 'msg': msg})



def register_view(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            if user is not None and user.role == 'student':
                profile, profile_created = StudentProfile.objects.get_or_create(user=user)
                profile.save()
                return redirect('account:login_view')
            if user is not None and user.role =='teacher':
                profile, profile_created = TeacherProfile.objects.get_or_create(user=user)
                profile.save()
                return redirect('account:login_view')
    else:
        form = SignUpForm()
    return render(request,'account/register.html', {'form': form})

def logout_view(request):
    # kullanıcıya logout olduğunu message olarak belirtmek 
    logout(request)
    return redirect('account:login_view')
