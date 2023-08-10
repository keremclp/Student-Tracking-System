from django.urls import path, include

from student.views import student_view


app_name = 'student'

urlpatterns = [
    path('student-dashboard/', student_view , name='student_view'),

]
