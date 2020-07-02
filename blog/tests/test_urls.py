from django.test import TestCase
from django.urls import reverse, resolve
from blog.views import index, about, terms
from blog.views import (
  PostListView,
  PostDetailView,
  PostCreateView,
  PostUpdateView,
  PostDeleteView
)

class TestUrls(TestCase):
  def setUp(self):
    self.url = None

  def test_index_url(self):
    self.url = reverse('blog-home')
    self.assertEqual(
      resolve(self.url).func.__name__,
      PostListView.as_view().__name__
    )

  def test_about_url(self):
    self.url = reverse('blog-about')
    self.assertEqual(resolve(self.url).func, about)

  def test_terms_url(self):
    self.url = reverse('blog-terms')
    self.assertEqual(resolve(self.url).func, terms)

  def test_post_url(self):
    self.url = reverse('blog-terms')
    self.assertEqual(resolve(self.url).func, terms)

  # path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
  # path('post/new/', PostCreateView.as_view(), name='post-create'),
  # path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
  # path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
  # path('about/', views.about, name='blog-about'),
  # path('terms/', views.terms, name='blog-terms')
