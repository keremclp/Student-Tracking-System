from django.db import models
from autoslug import AutoSlugField
from account.models import User

# Create your models here.


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200)   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



# Migrationlar yapılacak
# Student profile kısmını daha güzel yap 
# User ı çek ve first name ve last name ile profile slug ının ayarla
# Profile oluştur.