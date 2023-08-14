from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
from account.models import User
from django.utils import timezone

# Create your models here.


class Interest(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = AutoSlugField(populate_from='name', unique=True)

    def __str__(self):
        return self.name


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = AutoSlugField(unique=True, populate_from='user__username')
    student_id = models.CharField(max_length=10, unique=True, default="")
    birth_date = models.DateField(
        default=timezone.datetime(2000, 1, 1).strftime('%Y-%m-%d'))
    bio = models.TextField(blank=True, default="")
    phone_number = models.CharField(max_length=20, blank=True, default="")
    address = models.TextField(blank=True, default="")
    interests = models.ManyToManyField('Interest', blank=True, default="")

    def save(self, *args, **kwargs):
        # Populate the slug field from user's username
        if not self.slug:
            self.slug = self.user.username
        super().save(*args, **kwargs)

    def get_absolute_url_overview(self):
        return reverse(
            'student:student_profile_overview',
            kwargs={'slug': self.slug}
        )

    def get_absolute_url_edit(self):
        return reverse('student:student_profile_edit', kwargs={'user_slug': self.slug})


# Birth date field düzeltilecek
