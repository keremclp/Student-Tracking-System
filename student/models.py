from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from autoslug import AutoSlugField

# Models
from account.models import User
from classroom.models import Classroom
from teacher.models import TeacherProfile

from datetime import date

# Create your models here.
class AttendanceRecord(models.Model):
    STATUS_CHOICES = [
        ('P', 'Present'),
        ('A', 'Absent'),
    ]

    date = models.DateField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    notes = models.TextField(blank=True, null=True)

    # str function
    def __str__(self):
        return f"{self.date} - {self.status}"
    
class StudentClassroom(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)
    responsible_teacher = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE, null=True, blank=True)
    students = models.ManyToManyField('student.StudentProfile', related_name='classrooms')
    def __str__(self):
        return f"{self.classroom.grade_level} - {self.classroom.name}"
    

class StudentProfile(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = AutoSlugField(unique=True)
    birth_date = models.DateField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    attendance_records = models.ManyToManyField(AttendanceRecord,null=True, blank=True)


    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} (ID: {self.pk})"
    def save(self, *args, **kwargs):
        # Populate the slug field from user's username
        if not self.slug:
            self.slug = self.user.username
        super().save(*args, **kwargs)

    def get_absolute_url_overview(self):
        return reverse(
            'student:student_profile_overview',
            kwargs={'user_slug': self.slug}
        )
    
    def age(self):
        if self.birth_date:
            today = date.today()
            age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
            return age
        return None
    def get_absolute_url_edit(self):
        return reverse('student:student_profile_edit', kwargs={'user_slug': self.slug})
    

class StudentGrade(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    grade = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    exam_name = models.CharField(max_length=100)
    date = models.DateField()
    def __str__(self):
        return f"{self.student.user.first_name} {self.student.user.last_name} - {self.exam_name}"






    
    # def get_absolute_url(self):
    #     return reverse('student:student_classroom_detail', kwargs={'pk': self.pk})
    



