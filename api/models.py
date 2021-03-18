from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Users(models.Model):
    first_name=models.CharField(max_length=50,blank=False,default="amit")
    last_name=models.CharField(max_length=50,blank=True ,default="nagar")
    email=models.EmailField(unique=True,max_length=254,blank=False,default="email")
    address1=models.CharField(max_length=200,blank=False,default="Address")
    address2=models.CharField(max_length=200,blank=True,default="Address2")


    def __str__(self):
        return self.first_name


