from django import forms
from django.urls import reverse_lazy
from student.models import AttendanceRecord, StudentProfile


class TeacherCreateAttendance(forms.ModelForm):
    students = forms.ModelMultipleChoiceField(
        queryset=StudentProfile.objects.none(),
        widget=forms.SelectMultiple(
            attrs={'class': 'form-control w-100', 'data-ajax--url': reverse_lazy('attendance:search_students')})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['students'].queryset = StudentProfile.objects.all()

    class Meta:
        model = AttendanceRecord
        fields = [
            'date',
            'status',
            'students',
        ]
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control w-100'}),
            'date': forms.DateInput(attrs={'class': 'form-control w-100', 'type': 'date'}),
        }
