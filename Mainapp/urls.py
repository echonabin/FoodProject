from unicodedata import name
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

urlpatterns = [

    path('home', views.home, name='home'),
    path('aboutus', views.aboutus, name="aboutus"),
    path('food', views.food, name="food"),
    path('restaurant', views.restaurant, name="restaurant"),
     path('login/', auth_views.LoginView.as_view(template_name='Mainapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='Mainapp/index.html'), name='logout'),
    path('register', views.register, name="register"),
    path('dilivery', views.dilivery, name="dilivery"),

   
    


   
]