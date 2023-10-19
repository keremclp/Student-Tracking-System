from django.forms import forms

def min_lenght_7(value):
    if len(value) < 7 :
        raise forms.ValidationError('Title must be greater than 3 characters')