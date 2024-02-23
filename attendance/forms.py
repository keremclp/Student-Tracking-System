from django import forms
from student.models import AttendanceRecord

class TeacherCreateAttendance(forms.ModelForm):
    class Meta:
        model = AttendanceRecord
        fields = [
            'date',
            'status',
        ]
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control w-100'}),
            'date': forms.DateInput(attrs={'class': 'form-control w-100'}),
        }
