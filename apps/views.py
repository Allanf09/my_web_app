from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Post, Body, Profile
from .forms import PostForm, BodyForm


def home(request):
    return render(request, 'apps/home.html')

def posts(request):
    posts = Post.objects.order_by("posted_at")
    context = {'posts': posts}
    return render(request, 'apps/posts.html', context)

def post(request, post_id):
    post = Post.objects.get(id=post_id)
    
    bodies = post.body_set.order_by("posted_at")
    context = {'post': post, 'bodies': bodies}
    return render(request, 'apps/post.html', context)


def new_post(request):
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(data=request.POST)
        
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect('apps:posts')

    context = {'form': form}
    return render(request, 'apps/new_post.html', context)

def add_body(request, post_id):
    post = Post.objects.get(id=post_id)
    if post.owner != request.user:
        raise Http404


    if request.method != 'POST':
        form = BodyForm()
    else:
        form = BodyForm(data=request.POST)

        if form.is_valid():
            add_body = form.save(commit=False)
            add_body.post = post
            add_body.save()
            return redirect('apps:post', post_id=post_id)
    
    context = {'form': form, 'post': post}
    return render(request, 'apps/add_body.html', context)

def edit_body(request, body_id):
    body = Body.objects.get(id=body_id)
    post = body.post
    if post.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = BodyForm(instance=body)
    else:
        form = BodyForm(instance=body, data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('apps:post', post_id=post.id)
    
    context = {'form': form, 'topic': post, 'body': body}
    return render(request, 'apps/edit_body.html', context)

def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if post.owner != request.user:
        raise Http404

    if request.method == 'POST':
        post.delete()
        return redirect('apps:posts')
    
    context = {'post': post}
    return render(request, 'apps/delete_post.html', context)


