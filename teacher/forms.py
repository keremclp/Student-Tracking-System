from django import forms
from teacher.models import TeacherProfile
from classroom.models import Timetable

class DateInput(forms.DateInput):
    input_type = 'date'
    format = '%d.%m.%Y'  # Format used in the form input


class TeacherProfileModelForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    profile_image = forms.ImageField(required=False)
    birth_date = forms.DateField(widget=DateInput(format='%d.%m.%Y'), required=False)
    
    class Meta:
        model = TeacherProfile
        fields = [
            'profile_image',
            'first_name',
            'birth_date',
            'bio',
            'phone_number',
            'address',
            'experience',
            'salary',
        ]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Pre-fill the birth date field if the instance has a birth date
        if self.instance and self.instance.birth_date:
            self.fields['birth_date'].initial = self.instance.birth_date


# TODO:birth_date tarafında ne zaman edit yapmak istesek birth_day girilmesi gerekiyor, düzeltilmesi lazım

class TeacherTimetableModelForm(forms.ModelForm):
    class Meta:
        model = Timetable
        fields = [
            'classroom',
            'day_of_week',
            'start_time',
            'end_time',
            'subject',
        ]
        widgets = {
            'classroom': forms.Select(attrs={'class': 'form-control w-100'}),
            'day_of_week': forms.Select(attrs={'class': 'form-control w-100'}),
            'start_time': forms.TimeInput(attrs={'class': 'form-control w-100'}),
            'end_time': forms.TimeInput(attrs={'class': 'form-control w-100'}),
            'subject': forms.TextInput(attrs={'class': 'form-control w-100'}),
        }
        
        
    