from django.contrib import admin

# Register your models here.

from .models import Customer, Restaurant, Menu, Food

admin.site.register(Customer)
admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(Food)