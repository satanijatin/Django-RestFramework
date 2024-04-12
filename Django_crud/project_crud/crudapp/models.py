from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager


# Create your models here.

class Student(models.Model):
    uname=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    lang=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    img=models.ImageField(upload_to='images')


class User(AbstractUser):
   
    department = models.CharField(max_length=100,default='False')
    phoneno = models.CharField(max_length=100,default='')
    
    # USERNAME_FIELD='username'
    objects=UserManager()
    
    
class Author(models.Model):
    authorname = models.CharField(max_length=50)

    
class Publisher(models.Model):
    
    publishername = models.CharField(max_length=50)

    
class Book(models.Model):
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    publisher=models.ForeignKey(Publisher,on_delete=models.CASCADE)
    Bookname = models.CharField(max_length=200)
    price = models.IntegerField()
    