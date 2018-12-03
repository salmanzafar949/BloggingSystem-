from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView


def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})


class PostListView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"
    ordering = ['-created_at']


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'


def about(request):
    return render(request, 'blog/about.html')
