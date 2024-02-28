from django.contrib import admin
from student.models import StudentProfile, StudentClassroom, StudentGrade, AttendanceRecord
# Register your models here.


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    # list display
    list_display = (
        'pk',
        'user',
        'classroom',
    )


@admin.register(StudentClassroom)
class StudentClassroomAdmin(admin.ModelAdmin):
    # list display
    list_display = (
        'pk',
        'slug',
        'responsible_teacher',
    )


admin.site.register(StudentGrade)
admin.site.register(AttendanceRecord)
