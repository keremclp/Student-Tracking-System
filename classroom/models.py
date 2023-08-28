from django.db import models
from autoslug import AutoSlugField


# Create your models here.


class Classroom(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(unique=True)
    grade_level = models.CharField(max_length=10)
    capacity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.grade_level} - {self.name}"

    def save(self, *args, **kwargs):
        # Populate the slug field from user's username
        if not self.slug:
            self.slug = f"{self.grade_level} - {self.name}"
        super().save(*args, **kwargs)

class Timetable(models.Model):
    DAY_CHOICES = [
        (1, 'Monday'),
        (2, 'Tuesday'),
        (3, 'Wednesday'),
        (4, 'Thurday'),
        (5, 'Friday'),
    ]
    teacher = models.ForeignKey('teacher.TeacherProfile', on_delete=models.CASCADE)
    classroom = models.ForeignKey('classroom.Classroom', on_delete=models.CASCADE)
    day_of_week = models.IntegerField(choices=DAY_CHOICES)  # Add all days
    start_time = models.TimeField()
    end_time = models.TimeField()
    subject = models.CharField(max_length=100)

# Migrate yapılmadı buradan devam et ama öncesinde teacher oluştur!