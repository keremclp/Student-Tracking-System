from django.urls import path
from attendance.views import create_attendance_record
app_name = 'attendance'

urlpatterns = [
    path('create-attendance-record/', create_attendance_record, name='create_attendance_record'),
   
]
