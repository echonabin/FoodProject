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

# Create your views here.
from .models import *

def home(request):
    return render(request, 'Mainapp/index.html')

def aboutus(request):
    return render(request, 'Mainapp/aboutus.html')

def food(request):
    return render(request, 'Mainapp/food.html')

def restaurant(request):
    return render(request, 'Mainapp/restaurant.html')

def login(request):
    context = {}
    return render(request, 'Mainapp/login.html',context) 



from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'Mainapp/register.html', {'form': form})



# def register(request):
#     if request.method == 'POST':
#         fname = request.POST['fname']
#         lname = request.POST['lname']
#         email = request.POST['email']
#         mobile = request.POST['mobile']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']

#         user = User.object.create_user(fname=fname,l_name=lname,email=email,password=password1)
#         user.save()
#         print('user created')
#         return redirect('Mainapp/login.html')
#     else:    



#            return render(request, 'Mainapp/register.html')

   



def signin(request):
    return render(request, 'Mainapp/signin.html')

    
      
def signout(request):
    logout(request)


def dilivery(request):
    return render(request, 'Mainapp/dilivery.html')   



