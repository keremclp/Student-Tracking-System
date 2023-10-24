import json
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

# Models
from blog.models import BlogPost, Tag

# Forms
from blog.forms import BlogPostModelForm

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='account:login_view')
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

def create_blog_post_view(request):
    title = "Yeni Blog Post :"
    form = BlogPostModelForm()
    context = dict(
        title=title,
        form=form
    )

    if request.method == 'POST':
        form = BlogPostModelForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            print("Valid oldu...")
            f = form.save(commit=False)
            print(form.cleaned_data)
            f.user = request.user
            f.save()
            tags = json.loads(form.cleaned_data.get('tag'))
            for item in tags:
                tag_item, created = Tag.objects.get_or_create(title=item.get('value'))
                tag_item.title = tag_item.title.lower() 
                f.tag.isActive = True
                tag_item.save()
                f.tag.add(tag_item)
            messages.success(request, "Blog kaydedildi")
            return redirect('blog:blog_home')

    return render(request, 'blog/create_blog.html', context)

@login_required(login_url='user_profile:login_view')
def post_edit_view(request, post_slug):
    post = get_object_or_404(BlogPost, slug=post_slug)

    if not post.user == request.user:
        messages.warning(request, "You can n ot edit this blog")
        return redirect('home_view')

    title = post.title
    form = BlogPostModelForm(instance=post)

    if request.method == 'POST':
        form = BlogPostModelForm(request.POST or None,
                                 request.FILES or None, instance=post)
        if form.is_valid():
            print("Valid oldu...")
            f = form.save(commit=False)
            f.save()
            tags = json.loads(form.cleaned_data.get('tag'))
            for item in tags:
                tag_item, created = Tag.objects.get_or_create(
                    title=item.get('value').lower())
                f.tag.isActive = True
                tag_item.save()
                f.tag.add(tag_item)
            messages.success(request, "Blog düzenlendi")
            return redirect('home_view')

    context = dict(
        title=title,
        form=form
    )
    return render(request, 'blog/create_blog.html', context)