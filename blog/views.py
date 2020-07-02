from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post

context = {}

def index(request):
  context['title'] = 'Home'
  context['posts'] = Post.objects.all()
  return render(request, 'blog/index.htm', context)

def about(request):
  context['title'] = 'About'
  return render(request, 'blog/about.htm', context)

def terms(request):
  context['title'] = 'Terms of use'
  return render(request, 'blog/terms.htm', context)

class PostListView(ListView):
  model = Post
  template_name = 'blog/index.htm'
  context_object_name = 'posts'
  ordering = ['-date_posted']

class PostDetailView(DetailView):
  model = Post
  template_name = 'blog/post_detail.htm'

class PostCreateView(LoginRequiredMixin, CreateView):
  model = Post
  fields = ['title', 'content']
  template_name = 'blog/post_form.htm'

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  model = Post
  fields = ['title', 'content']
  template_name = 'blog/post_form.htm'

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

  def test_func(self):
    post = self.get_object()
    if self.request.user == post.author:
      return True
    return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  model = Post
  success_url = '/'
  template_name = 'blog/post_delete.htm'

  def test_func(self):
    post = self.get_object()
    if self.request.user == post.author:
      return True
    return False
