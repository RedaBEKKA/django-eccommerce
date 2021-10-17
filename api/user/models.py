from django.db import models
from django.contrib.auth.auth import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    name = models.CharField(max_length=50,default='Anonyme')
    email = models.EmailField(max_length=250,unique=True)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    phone = models.CharField(max_length=20,blank=True, null=True)
    gender = models.CharField(max_length=10,blank=True, null=True)

    session_token = models.CharField(max_length=10,default=0)
    created_at = models.DateTimeField(auto_now_add=False)
    updated_at = models.DateTimeField(auto_now=True)
    
    