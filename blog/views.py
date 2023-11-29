from django.shortcuts import render
import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

# Models
from blog.models import BlogPost, Tag, UserPostFav
from account.models import User
from teacher.models import TeacherProfile
from student.models import StudentProfile

# Forms
from blog.forms import BlogPostModelForm

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='account:login_view')
def blog_home(request):
    posts = BlogPost.objects.all().filter(is_active=True).order_by('-created_at')[:6]  # get the latest six published posts
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
                tag_item.save() # TODO: Taglar database e kayıt yapıyor ama belirli bir post oluşturmak istedğinde o posta kaydetmiyor
                f.tag.add(tag_item)
            messages.success(request, "Blog kaydedildi")
            return redirect('blog:blog_home')

    return render(request, 'blog/create_blog.html', context)

@login_required(login_url='user_profile:login_view')
def post_edit_view(request, post_slug):
    post = get_object_or_404(BlogPost, slug=post_slug)

    if not post.user == request.user:
        messages.warning(request, "You can n ot edit this blog")
        return redirect('blog:blog_home')

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
            return redirect('blog:blog_home')

    context = dict(
        title=title,
        form=form
    )
    return render(request, 'blog/create_blog.html', context)

def all_posts_view(request, user_slug):
    user = get_object_or_404(User, userslug=user_slug)
    posts = BlogPost.objects.filter(user=user, is_active=True)
    print("-"*30)
    print(posts)
    context = dict(
        posts=posts,
        user = user
    )
    return render(request, 'blog/all_posts.html', context)

def post_detail_view(request,user_slug,post_slug):
    post = get_object_or_404(BlogPost, slug=post_slug, is_active=True)
    post.view_count += 1
    post.save()
    print(post.view_count)  
    # check the user
    user = get_object_or_404(User, userslug= user_slug)
    if user.role == 'teacher':
        profile = get_object_or_404(TeacherProfile, user=user)
    else:
        profile = get_object_or_404(StudentProfile, user=user)
    post = get_object_or_404(BlogPost, slug=post_slug)

    context = dict(
        post=post,
        user=user,
        profile = profile
    )
    
    print(request)
    return render(request, 'blog/post_detail.html', context)


@login_required(login_url='account:login_view')
def fav_update_view(request):
    if request.method == 'POST':
        post = get_object_or_404(BlogPost, slug=request.POST.get('slug'))
        if (post):
            post_fav, created = UserPostFav.objects.get_or_create(
                user=request.user,
                post=post,
            )
            if not created:
                post_fav.is_deleted = not post_fav.is_deleted
                post_fav.save()

    return JsonResponse({'status': 200})
