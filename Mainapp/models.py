from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length = 20, null=True)
    phone = models.CharField(max_length=100, null = True)
    email = models.CharField(max_length=100, null=True)
    data_created = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.name