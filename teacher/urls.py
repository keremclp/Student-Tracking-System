from django.urls import path, include

from teacher.views import teacher_dashboard,teacher_profile_overview


app_name = 'teacher'

urlpatterns = [
    path('teacher-dashboard/', teacher_dashboard , name='teacher_dashboard'),
    path('teacher-profile-overview/', teacher_profile_overview , name='teacher_profile_overview'),
]
