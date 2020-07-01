from django.urls import reverse
from django.test import TestCase, Client

class TestViews(TestCase):
  def setUp(self):
    self.response = None
    self.client = Client()
    self.home_url = reverse('blog-home')
    self.about_url = reverse('blog-about')
    self.terms_url = reverse('blog-terms')

  def test_index_GET(self):
    self.response = self.client.get(self.home_url)
    self.assertEqual(self.response.status_code, 200)
    self.assertTemplateUsed(self.response, 'blog/index.htm')

  def test_about_GET(self):
    self.response = self.client.get(self.about_url)
    self.assertEqual(self.response.status_code, 200)
    self.assertTemplateUsed(self.response, 'blog/about.htm')

  def test_terms_GET(self):
    self.response = self.client.get(self.terms_url)
    self.assertEqual(self.response.status_code, 200)
    self.assertTemplateUsed(self.response, 'blog/terms.htm')
