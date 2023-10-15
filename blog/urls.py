from django.urls import path
from blog.views import blog_home
app_name = 'blog'

urlpatterns = [
    path('blog-home/', blog_home , name='blog_home'),

]
