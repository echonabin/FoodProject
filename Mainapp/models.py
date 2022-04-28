from asyncio import SendfileNotAvailableError
from django.db import models
from django.contrib.auth.models import User


# Create your models here.




class Customer(models.Model):
    name = models.CharField(max_length = 20, null=True)
    phone = models.CharField(max_length=100, null = True)
    email = models.EmailField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    mobile = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100, null=True)
    

def __str__(self):
    return self.name

# restaurant model 

class Restaurant(models.Model):
    name = models.CharField(max_length=1000,null=True,blank=True)
    owner = models.CharField(max_length=1000, null=True, blank=True)
    phone = models.CharField(max_length=20,null=True, blank=True)
    addres = models.CharField(max_length=10000, null=True, blank=True)
    area = models.CharField(max_length=1000, null=True, blank=True)
    des = models.TextField(max_length=10000, null=True, blank=True)
    opentime = models.TimeField(null=True, blank=True)
    closestime = models.TimeField(null=True, blank=True)
    restImage =  models.ImageField(upload_to ='uploads/')

   
    def __str__(self):
        return self.name



class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    menu = models.CharField(max_length=3000)
    spacial = models.CharField(max_length=3000, null=True, blank=True)
    offer = models.CharField(max_length=3000, null=True, blank=True)

    def __str__(self):
        return self.menu

class Food(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=3000)
    food_prize = models.PositiveIntegerField()
    veg = models.BooleanField(null=True, blank=True)
    nonveg = models.BooleanField(null=True, blank=True)
    egg = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.food_name