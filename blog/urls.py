from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)

urlpatterns = [
  path('terms/', views.terms, name='blog-terms'),
  path('about/', views.about, name='blog-about'),
  path('', PostListView.as_view(), name='blog-home'),
  path('post/new/', PostCreateView.as_view(), name='post-create'),
  path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
  path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
  path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
  path('user/<str:username>/', UserPostListView.as_view(), name='user-posts')
]
