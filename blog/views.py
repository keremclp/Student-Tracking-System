from django.shortcuts import render

# Models
from blog.models import BlogPost
# Create your views here.
def blog_home(request):
    posts = BlogPost.objects.all().order_by('-created_at')[:6]  # get the latest six published posts
    post_1 = posts[:3]
    post_2 = posts[3:6]
    context = dict(
        post_1=post_1,
        post_2=post_2,
        posts=posts
    )
    return render(request, 'blog/blog_home.html', context)    
