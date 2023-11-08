from django.urls import path
from blog.views import blog_home,create_blog_post_view, post_edit_view, all_posts_view,post_detail_view, fav_update_view
app_name = 'blog'

urlpatterns = [
    path('blog-home/', blog_home , name='blog_home'),
    path('create-blog/', create_blog_post_view , name='create_blog'),
    path('post/<slug:post_slug>/edit/', post_edit_view, name='post_edit_view'),
    path('read/<slug:user_slug>', all_posts_view, name='all_posts_view'),
    path('read/<slug:user_slug>/<slug:post_slug>', post_detail_view, name='post_detail_view'),
    path('fav-update/', fav_update_view, name='fav_update_view'),
]
