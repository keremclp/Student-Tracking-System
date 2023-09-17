from django.urls import reverse
from autoslug import AutoSlugField
from django.db import models

# Models
from account.models import User


# Create your models here.

class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    classroom = models.ManyToManyField('student.StudentClassroom')
    slug = AutoSlugField(unique=True)
    birth_date = models.DateField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    experience = models.IntegerField(null=True, blank=True)
    salary = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} (ID: {self.pk})"
    def save(self, *args, **kwargs):
        # Populate the slug field from user's username
        if not self.slug:
            self.slug = self.user.username
        super().save(*args, **kwargs)

    def get_absolute_url_overview(self):
        return reverse(
            'teacher:teacher_profile_overview',
            kwargs={'user_slug': self.slug}
        )
    
    def get_absolute_url_edit_teacher(self):
        return reverse('teacher:teacher_profile_edit', kwargs={'user_slug': self.slug})
    

