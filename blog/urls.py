from django.urls import path
from blog.views import blog_home,create_blog_post_view, post_edit_view, all_posts_view,post_detail_view, fav_update_view, tag_view, category_view
app_name = 'blog'

urlpatterns = [
    path('blog-home/', blog_home , name='blog_home'),
    path('create-blog/', create_blog_post_view , name='create_blog'),
    path('post/<slug:post_slug>/edit/', post_edit_view, name='post_edit_view'),
    # Category and Tag view
    path('category/<slug:category_slug>/', category_view, name='category_view'),
    path('tag/<slug:tag_slug>/', tag_view, name='tag_view'),

    # Read
    path('read/<slug:user_slug>/', all_posts_view, name='all_posts_view'),
    path('read/<slug:user_slug>/<slug:post_slug>/', post_detail_view, name='post_detail_view'),
    
    # Fav update using axios
    path('fav-update/', fav_update_view, name='fav_update_view'),
]
