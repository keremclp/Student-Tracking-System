from django import forms
from .models import StudentProfile
from datetime import datetime

class DateInput(forms.DateInput):
    input_type = 'date'
    format = '%d.%m.%Y'  # Format used in the form input


class StudentProfileModelForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    profile_image = forms.ImageField(required=False)
    birth_date = forms.DateField(widget=DateInput(format='%d.%m.%Y'), required=False)
    
    class Meta:
        model = StudentProfile
        fields = [
            'profile_image',
            'first_name',
            'birth_date',
            'bio',
            'phone_number',
            'address',
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Pre-fill the birth date field if the instance has a birth date
        if self.instance and self.instance.birth_date:
            self.fields['birth_date'].initial = self.instance.birth_date


# TODO:birth_date tarafında ne zaman edit yapmak istesek birth_day girilmesi gerekiyor, düzeltilmesi lazım

    