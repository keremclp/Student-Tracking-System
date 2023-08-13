from django.urls import path, include
from student.views import student_profile,student_view


app_name = 'student'

urlpatterns = [
    path('student-profile/<slug:user_slug>/', student_profile , name='student_profile'),
    path('student-view/', student_view , name='student_view'),
]
