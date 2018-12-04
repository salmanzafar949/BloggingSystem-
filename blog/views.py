from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Post
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})


class PostListView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"
    ordering = ['-created_at']
    paginate_by = '10'

class UserPostListView(ListView):
    model = Post
    template_name = "blog/user_posts.html"
    context_object_name = "posts"
    # paginate_by = '1'


    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(user=user).order_by('-created_at')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True

        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html')
