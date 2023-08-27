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

