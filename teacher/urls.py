from django.urls import path, include

from teacher.views import teacher_dashboard


app_name = 'teacher'

urlpatterns = [
    path('teacher-dashboard/', teacher_dashboard , name='teacher_dashboard'),

]
