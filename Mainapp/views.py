from multiprocessing import context
import django
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from .models import Customer, Restaurant, Menu, Food
from django.db import IntegrityError

# Create your views here.
from .models import *

def home(request):
    restaurants = Restaurant.objects.all()
    return render( request, 'Mainapp/index.html', {'restaurants': restaurants})

def aboutus(request):
    return render(request, 'Mainapp/aboutus.html')

def food(request):
    return render(request, 'Mainapp/food.html')



def restro(request):
    restaurants = Restaurant.objects.all()
    return render( request, 'Mainapp/restaurant.html', {'restaurants': restaurants})



def login(request):

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('Mainapp/index.html')
        
    else:
        messages.success(request, 'Account creation failed!')
   
    return render(request, 'Mainapp/login.html') 



from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'Mainapp/register.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
            logout(request)
            return redirect('login')


   



def signin(request):
    return render(request, 'Mainapp/signin.html')

    
      
def signout(request):
    logout(request)


def dilivery(request):
    return render(request, 'Mainapp/dilivery.html')   

# def detail(request):
#     return render(request, 'Mainapp/detail.html')  

def detail(request, pk):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["res"] = Restaurant.objects.get(pk = pk)
         
    return render(request, "Mainapp/detail.html", context)






def order(request):
    return render(request, 'Mainapp/orderpage.html') 

def contact(request):
    return render(request, 'Mainapp/contact.html') 



