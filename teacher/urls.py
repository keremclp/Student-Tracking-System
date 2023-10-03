from django.urls import path

from teacher.views import (
    teacher_dashboard,
    teacher_profile_overview,
    teacher_profile_edit,
    teacher_create_timetable,
    activate_student,
    teacher_create_classroom,
    add_student_classroom,
    edit_student_classroom
)


app_name = 'teacher'

urlpatterns = [
    path('teacher-dashboard/', teacher_dashboard, name='teacher_dashboard'),
    path('teacher-profile/<slug:user_slug>/',
         teacher_profile_overview, name='teacher_profile_overview'),
    path('teacher-profile/<slug:user_slug>/edit/',
         teacher_profile_edit, name='teacher_profile_edit'),
    path('teacher-create-timetable/', teacher_create_timetable,
         name='teacher_create_timetable'),
    path('teacher_dashboard/activate_student/<int:student_id>/',
         activate_student, name='activate_student'),
    path('teacher-create-classroom/', teacher_create_classroom,
         name='teacher_create_classroom'),
    path('teacher-create-student-classroom/',
         add_student_classroom, name='add_student_classroom'),
     path('edit-student-classroom/<slug:classroom_slug>/', edit_student_classroom, name='edit_student_classroom'),
     
]
