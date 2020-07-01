from PIL import Image
from io import BytesIO
from django.test import TestCase
from django.core.files.uploadedfile import InMemoryUploadedFile
from users.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

class TestsForms(TestCase):
  def setUp(self):
    self.form = None

  def test_user_register_form_valid(self):
    self.form = UserRegisterForm(data={
      'username': 'myusername',
      'email': 'my@email.com',
      'password1': 'dummypass1234',
      'password2': 'dummypass1234',
    })
    self.assertTrue(self.form.is_valid())
    self.assertEqual(len(self.form.errors), 0)

  def test_user_register_form_blank(self):
    self.form = UserRegisterForm(data={})
    self.assertFalse(self.form.is_valid())
    self.assertEqual(len(self.form.errors), 4)

  def test_user_update_form_valid(self):
    self.form = UserUpdateForm(data={
      'username': 'myusername123',
      'email': 'notmy@email.com',
    })
    self.assertTrue(self.form.is_valid())
    self.assertEqual(len(self.form.errors), 0)

  def test_user_update_form_blank(self):
    self.form = UserUpdateForm(data={})
    self.assertFalse(self.form.is_valid())
    self.assertEqual(len(self.form.errors), 2)

  def create_image(self):
    im_io = BytesIO()
    im = Image.new(mode='RGB', size=(300,300)).save(im_io, 'JPEG')
    return InMemoryUploadedFile(im_io, None, 'test_form.jpg',
      'image/jpeg', len(im_io.getvalue()), None).open()

  # BUG: test_profile_update_form_blank() would be a valid test
  # becasue data["image"] is only invalid when the file is not an image
  def test_profile_update_form_valid(self):
    image = self.create_image()
    self.form = ProfileUpdateForm({'image': image})
    self.assertTrue(self.form.is_valid())
    self.assertEqual(len(self.form.errors), 0)
