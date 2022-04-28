from unicodedata import name
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .views import detail



urlpatterns = [

    path('home', views.home, name='home'),
    path('aboutus', views.aboutus, name="aboutus"),
    path('food', views.food, name="food"),
    path('restro', views.restro, name="restro"),
    # path('detail', views.detail, name="detail"),
    path('detail/<int:pk>/', views.detail, name="detail"),
    path('login/', auth_views.LoginView.as_view(template_name='Mainapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='Mainapp/index.html'), name='logout'),
    path('register', views.register, name="register"),
    path('dilivery', views.dilivery, name="dilivery"),
    path('order', views.order, name="order"),
    path('contact', views.contact, name="contact"),
   
]