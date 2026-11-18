from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog-single/', views.blog_single, name='blog-single'),
    path('blog/', views.blog, name='blog'),
    path('cases/', views.cases, name='cases'),
    path('contact/', views.contact, name='contact'),
    path('main/', views.main, name='main'),
    path('services/', views.services, name='services'),
]