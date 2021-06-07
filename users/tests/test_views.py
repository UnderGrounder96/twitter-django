import os
# import boto3
from PIL import Image
from io import BytesIO
from django.urls import reverse
from django.test import TestCase, Client
from django.core.files.uploadedfile import InMemoryUploadedFile

class TestViews(TestCase):
  def setUp(self):
    self.response = None
    self.client = Client()
    self.profile_url = reverse('profile')
    self.register_url = reverse('register')

  def test_register_GET(self):
    self.response = self.client.get(self.register_url)
    self.assertEqual(self.response.status_code, 200)
    self.assertTemplateUsed(self.response, 'users/register.htm')

  def test_register_POST_blank(self):
    self.response = self.client.post(self.register_url)
    self.assertEqual(self.response.status_code, 200)
    self.assertTemplateUsed(self.response, 'users/register.htm')

  def test_register_POST_valid(self):
    self.response = self.client.post(
      self.register_url,
      {
        'username': 'myusername',
        'email': 'my@email.com',
        'password1': 'dummypass1234',
        'password2': 'dummypass1234'
      }
    )
    self.assertEqual(self.response.status_code, 302)
    self.assertRedirects(self.response, '/login/')

  def test_register_POST_and_login(self):
    self.test_register_POST_valid()
    self.assertTrue(
      self.client.login(
        username='myusername',
        password='dummypass1234'
      )
    )

  def test_profile_GET_not_logged_in(self):
    self.response = self.client.get(self.profile_url)
    self.assertEqual(self.response.status_code, 302)
    self.assertRedirects(self.response, '/login/?next=/profile/')

  def test_profile_GET_logged_in(self):
    self.test_register_POST_and_login()
    self.response = self.client.get(self.profile_url)
    self.assertEqual(self.response.status_code, 200)
    self.assertTemplateUsed(self.response, 'users/profile.htm')

  def create_image(self):
    im_io = BytesIO()
    im = Image.new(mode='RGB', size=(300,300)).save(im_io, 'JPEG')
    return InMemoryUploadedFile(im_io, None, 'test_view.jpg',
      'image/jpeg', len(im_io.getvalue()), None).open()

  def test_profile_POST_alter(self):
    image = self.create_image()
    self.test_profile_GET_logged_in()
    self.response = self.client.post(
      self.profile_url,
      {
        'username': 'myusernamex',
        'email': 'Notmy@email.com',
        'image': image
      }
    )
    self.assertEqual(self.response.status_code, 302)
    self.assertRedirects(self.response, '/profile/')
    self.response = self.client.get(self.profile_url)
    self.assertEqual(self.response.status_code, 200)
    self.assertTemplateUsed(self.response, 'users/profile.htm')
    # s3 = boto3.resource('s3')
    # s3.Object(
    #   os.getenv('AWS_STORAGE_BUCKET_NAME'),
    #   'profile_pics/'+image.name
    # ).delete()
