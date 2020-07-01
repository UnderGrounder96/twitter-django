from django.shortcuts import render
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
