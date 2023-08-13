from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login,logout
from account.forms import LoginForm, SignUpForm
from student.models import StudentProfile
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
                user_slug = StudentProfile.objects.get(user=user).slug
                return redirect('student:student_profile_overview',user_slug=user_slug)
            elif user is not None and user.role == 'teacher':
                login(request, user)
                return redirect('teacher:teacher_view')
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
                   
            msg = 'user created'
            return redirect('account:login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'account/register.html', {'form': form, 'msg': msg})


