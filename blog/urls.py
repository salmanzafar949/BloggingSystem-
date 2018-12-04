from django.urls import path
from . import views

app_name="blog"

urlpatterns = [

    path('', views.PostListView.as_view(), name="index"),
    path('post/<int:pk>/detail/', views.PostDetailView.as_view(), name="detail"),
    path('post/new/create/', views.PostCreateView.as_view(), name="create"),
    path('user/<str:username>/posts/', views.UserPostListView.as_view(), name="user-post"),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name="update"),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name="delete"),
    path('about', views.about, name="about"),
]