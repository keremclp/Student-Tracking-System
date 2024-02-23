from django.urls import path
from attendance.views import create_attendance_record, search_students
app_name = 'attendance'

urlpatterns = [
    path('create-attendance-record/', create_attendance_record, name='create_attendance_record'),
    path('search-students/', search_students, name='search_students'),
]
