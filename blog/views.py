from django.shortcuts import render

# Models
from blog.models import BlogPost
# Create your views here.
def blog_home(request):
    posts = BlogPost.objects.all()[:6]  # get the last five published posts
    post_1 = [posts[0], posts[1], posts[2]]
    post_2 = [posts[3], posts[4], posts[5]]
    context = dict(
        post_1=post_1,
        post_2=post_2,
        posts=posts
    )
    return render(request, 'blog/blog_home.html', context)    
