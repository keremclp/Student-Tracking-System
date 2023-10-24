from django.urls import path
from blog.views import blog_home,create_blog_post_view, post_edit_view
app_name = 'blog'

urlpatterns = [
    path('blog-home/', blog_home , name='blog_home'),
    path('create-blog/', create_blog_post_view , name='create_blog'),
    path('post/<slug:post_slug>/edit/', post_edit_view, name='post_edit_view'),
]
