from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control bg-transparent"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control bg-transparent"
            }
        )
    )


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control bg-transparent"
            }
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control bg-transparent"
            }
        )
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control bg-transparent"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control bg-transparent"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control bg-transparent"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control bg-transparent"
            }
        )
    )

    role = forms.ChoiceField(
        choices=User.roles,
        widget=forms.RadioSelect(
            attrs={

                "class": ""
            }
        ),
    )
    profile_image = forms.ImageField(
        required=False,  
        widget=forms.ClearableFileInput(
            attrs={
                "class": "form-control-file"
            }
        )
    )

    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email', 'password1',
                  'password2', 'role', 'profile_image')
