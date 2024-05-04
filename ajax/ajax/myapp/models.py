from django.db import models

# Create your models here.
class User(models.Model):
    uname = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)