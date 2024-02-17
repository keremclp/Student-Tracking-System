from django.contrib import admin
from student.models import StudentProfile,StudentClassroom,StudentGrade,AttendanceRecord
# Register your models here.

admin.site.register(StudentProfile)


@admin.register(StudentClassroom)
class StudentClassroomAdmin(admin.ModelAdmin):
    # list display
    list_display = (
        'pk',
        'slug'
    )

admin.site.register(StudentGrade)
admin.site.register(AttendanceRecord)


