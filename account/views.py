from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login,logout
from account.forms import LoginForm, SignUpForm

# Create your views here.

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
                return redirect('account:student')
            elif user is not None and user.role == 'teacher':
                login(request, user)
                return redirect('customer')
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
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            msg = 'user created'
            return redirect('account:login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'account/register.html', {'form': form, 'msg': msg})


def student_view(request):
    return render(request,'account/student_dasboard.html')