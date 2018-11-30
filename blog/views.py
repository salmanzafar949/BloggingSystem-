from django.shortcuts import render
from .models import Post


def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})


def about(request):
    return render(request, 'blog/about.html')
