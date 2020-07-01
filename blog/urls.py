from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='blog-home'),
  path('about/', views.about, name='blog-about'),
  path('terms/', views.terms, name='blog-terms')
]
