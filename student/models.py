# from django.db import models
# from account.models import User

# # Create your models here.
# class StudentProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     profile_image = models.ImageField(upload_to='profile_image',blank=True)
#     address = models.CharField(max_length=200,blank=True)
#     phone = models.CharField(max_length=200,blank=True)
#     date_of_birth = models.DateField(blank=True,null=True)
#     def __str__(self):
#         return self.user.username
#     class Meta:
#         verbose_name_plural = 'Student Profile'
