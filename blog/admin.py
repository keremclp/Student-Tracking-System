from django.contrib import admin
from blog.models import Category, BlogPost, Tag,UserPostFav
# Register your models here.

admin.site.register(Category)
admin.site.register(BlogPost)
admin.site.register(Tag)
admin.site.register(UserPostFav)