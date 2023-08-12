from django.urls import path, include
from student.views import student_profile


app_name = 'student'

urlpatterns = [
    path('student-profile/', student_profile , name='student_profile'),
]
