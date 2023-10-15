from django.contrib import admin
from blog.models import Category, BlogPost
# Register your models here.

admin.site.register(Category)
admin.site.register(BlogPost)