from django.contrib import admin
from student.models import StudentProfile,StudentClassroom,StudentGrade,AttendanceRecord
# Register your models here.

admin.site.register(StudentProfile)
admin.site.register(StudentClassroom)
admin.site.register(StudentGrade)
admin.site.register(AttendanceRecord)


