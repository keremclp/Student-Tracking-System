from django.urls import path
from blog.views import blog_home,create_blog_post_view
app_name = 'blog'

urlpatterns = [
    path('blog-home/', blog_home , name='blog_home'),
    path('create-blog/', create_blog_post_view , name='create_blog'),

]
