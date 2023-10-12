from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login,logout
from account.forms import LoginForm, SignUpForm
from student.models import StudentProfile
from teacher.models import TeacherProfile
def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None and user.role == 'student':
                profile, profile_created = StudentProfile.objects.get_or_create(user=user)
                profile.save()
                login(request, user)
                messages.success(request,f'{username} successfully logged in.')
                return redirect('student:student_dashboard')

            elif user is not None and user.role == 'teacher': 
                login(request, user)
                messages.success(request,f'{username} successfully logged in.')
                return redirect('teacher:teacher_dashboard')
            elif user is not None and user.role == 'parent':
                login(request, user)
                return redirect('employee')
            else:
                messages.warning(request,"Please check your email or password")
                return redirect('account:error_view')
        else:
            messages.error(request, "Validation Error")
    return render(request, 'account/login.html', {'form': form})



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
    username = request.user.username
    # kullanıcıya logout olduğunu message olarak belirtmek 
    logout(request)
    messages.success(request,f'{username} successfully log out.')
    return redirect('account:login_view')

def error_view(request):
    return render(request,'account/error.html')