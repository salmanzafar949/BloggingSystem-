from django.urls import path
from . import views

app_name="blog"

urlpatterns = [

    path('', views.PostListView.as_view(), name="index"),
    path('post/<int:pk>/detail/', views.PostDetailView.as_view(), name="detail"),
    path('about', views.about, name="about"),
]