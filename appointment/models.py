from django.db import models
from django.utils import timezone
from student.models import StudentProfile, TeacherProfile


class Appointment(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    teacher = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE)
    date_time = models.DateTimeField(default=timezone.now)
    description = models.TextField()

    def __str__(self):
        return f"Appointment for {self.student.user.username} with {self.teacher.user.username} at {self.date_time}"
