from django.urls import path, include
from student.views import student_profile_overview,student_view


app_name = 'student'

urlpatterns = [
    path('student-profile/<slug:user_slug>/', student_profile_overview , name='student_profile_overview'),
    path('student-view/', student_view , name='student_view'),
]
