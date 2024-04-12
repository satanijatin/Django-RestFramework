from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20)
    email =  models.CharField(max_length=20)
    age = models.IntegerField()
    


class Category(models.Model):
    catname = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.catname

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    pname = models.CharField(max_length=20)
    price = models.IntegerField()
    qty = models.IntegerField()
    

class Author(models.Model):
    authorname = models.CharField(max_length=50)

    
class Publisher(models.Model):
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    publishername = models.CharField(max_length=50)

    
class Book(models.Model):
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    publisher=models.ForeignKey(Publisher,on_delete=models.CASCADE)
    Bookname = models.CharField(max_length=200)
    price = models.IntegerField()
    
    
    
class Country(models.Model):
    countryname = models.CharField(max_length=250)
    
class State(models.Model):
    country=models.ForeignKey(Country,on_delete=models.CASCADE)
    statename = models.CharField(max_length=50)

    
class City(models.Model):
    state=models.ForeignKey(State,on_delete=models.CASCADE)
    cityname = models.CharField(max_length=200)
    country=models.ForeignKey(Country,on_delete=models.CASCADE,default=1)
    
class Area(models.Model):
      areaname = models.CharField(max_length=200)
      city=models.ForeignKey(City,on_delete=models.CASCADE)
      state=models.ForeignKey(State,on_delete=models.CASCADE)
      country=models.ForeignKey(Country,on_delete=models.CASCADE)
      
