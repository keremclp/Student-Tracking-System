from django.urls import path, include
from student.views import student_profile_overview,student_dashboard,student_profile_edit


app_name = 'student'

urlpatterns = [
    path('student-profile/<slug:user_slug>/', student_profile_overview , name='student_profile_overview'),
    path('student-dashboard/', student_dashboard , name='student_dashboard'),
    path('profile-edit/<slug:user_slug>', student_profile_edit , name='student_profile_edit'),
]
