from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post

# Create your test here.
class TestModels(TestCase):
  def setUp(self):
    self.user = User.objects.create(
      username='myusername',
      email='my@email.com',
      password='dummypass1234'
    )
    self.post = Post.objects.create(
      content='My content',
      title='NotMyTitle',
      author=self.user
    )
    self.post.save()

  def test_post_is_assigned(self):
    self.assertEqual(str(self.post.title), 'NotMyTitle')
    self.assertEqual(str(self.user.post_set.first()), 'NotMyTitle')

  def test_post_is_altered(self):
    self.post.title='My Title'
    self.post.save()
    self.assertEqual(str(self.post.title), 'My Title')
    self.assertEqual(str(self.user.post_set.first()), 'My Title')
