from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=10)
    password=models.CharField(max_length=100)
    isAdmin=models.BooleanField(default=False)
    isAuthenticated=models.BooleanField(default=False)
    createdttm=models.DateTimeField(auto_now_add=True)
    updatedttm=models.DateTimeField(auto_now=True)
