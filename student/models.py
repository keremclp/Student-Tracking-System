from django.db import models
from autoslug import AutoSlugField
from account.models import User

# Create your models here.


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = AutoSlugField(unique=True, populate_from='user__username') 
    
    def save(self, *args, **kwargs):
        # Populate the slug field from user's username
        if not self.slug:
            self.slug = self.user.username
        super().save(*args, **kwargs)



# Migrationlar yapılacak
# Student profile kısmını daha güzel yap 
# User ı çek ve first name ve last name ile profile slug ının ayarla
# Profile oluştur.