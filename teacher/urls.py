from django.urls import path, include

from teacher.views import teacher_view


app_name = 'teacher'

urlpatterns = [
    path('teacher-dashboard/', teacher_view , name='teacher_view'),
]
