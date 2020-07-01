from django.test import TestCase
from django.urls import reverse, resolve
from blog.views import index, about, terms

class TestUrls(TestCase):
  def setUp(self):
    self.url = None

  def test_index_url(self):
    self.url = reverse('blog-home')
    self.assertEqual(resolve(self.url).func, index)

  def test_about_url(self):
    self.url = reverse('blog-about')
    self.assertEqual(resolve(self.url).func, about)

  def test_terms_url(self):
    self.url = reverse('blog-terms')
    self.assertEqual(resolve(self.url).func, terms)
