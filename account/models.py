from django.db import models
from django.contrib.auth.models import AbstractUser
from autoslug import AutoSlugField

class User(AbstractUser):
    roles = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('parent', 'Parent'),
    ]

    role = models.CharField(choices=roles,max_length=200)
    profile_image = models.ImageField(upload_to='profile_image')
    

