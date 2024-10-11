from django import forms
from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=20)

class Broker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    admin = models.BooleanField(default=False)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    PIN = models.IntegerField()

class UserInfo(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)