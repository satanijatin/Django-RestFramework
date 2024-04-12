from typing import Any
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Category(models.Model):
    categoryname=models.CharField(max_length=100)
    
    # def __str__(self):
    #         return self.categoryname
    
class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    pname = models.CharField(max_length=500)
    image = models.ImageField(upload_to='my_image',default="img")
    price = models.IntegerField()
    qty = models.IntegerField()
    
    # def __str__(self):
    #         return self.id
    
    # def __str__(self):
    #         return (self.category,self.pname,self.image,self.price,self.qty)
        
    # def __init__(self,category,pname,image,price,qty) :
    #        self.category=category
    #        self.pname=pname
    #        self.image=image
    #        self.price=price
    #        self.qty=qty
    
     
    
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    qty = models.IntegerField()
    
 
  
    
    
   
