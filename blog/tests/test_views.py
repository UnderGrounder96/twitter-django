from django.urls import reverse, resolve
from django.test import TestCase, Client
from blog.views import PostListView


class TestViews(TestCase):
  def setUp(self):
    self.response = None
    self.client = Client()
    self.home_url = reverse('blog-home')
    self.about_url = reverse('blog-about')
    self.terms_url = reverse('blog-terms')

  def test_index_GET(self):
    self.assertEqual(
      resolve(self.home_url).func.__name__,
      PostListView.as_view().__name__
    )
    # self.response = self.client.get(self.home_url)
    # self.assertEqual(self.response.status_code, 200)
    # self.assertTemplateUsed(self.response, 'blog/index.htm')

  def test_about_GET(self):
    self.response = self.client.get(self.about_url)
    self.assertEqual(self.response.status_code, 200)
    self.assertTemplateUsed(self.response, 'blog/about.htm')

  def test_terms_GET(self):
    self.response = self.client.get(self.terms_url)
    self.assertEqual(self.response.status_code, 200)
    self.assertTemplateUsed(self.response, 'blog/terms.htm')
