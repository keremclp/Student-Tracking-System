from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
from account.models import User
from django.utils import timezone

# Create your models here.





class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = AutoSlugField(unique=True, populate_from='user__username')
    birth_date = models.DateField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

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
