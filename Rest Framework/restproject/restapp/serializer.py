from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

from datetime import date, timedelta

from django.utils import timezone
import datetime





class PersonSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = ['id', 'name', 'birthdate', 'age']

    def get_age(self, obj):
        from datetime import datetime
        birthdate = datetime.strptime(obj.birthdate, '%Y-%m-%d')
        today = datetime.today()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return f"Your age is {age}"


class AgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Age
        fields= '__all__'
        
    # def create(self, validated_data):
        
    #     dates=validated_data['age']
    #     year=dates.split('/')
    #     yys=year[2]
        
    #     mms=year[1]
    #     dds=year[0]
    #     ages = datetime.date(int(yys), int(mms), int(dds))
    #     today = datetime.date.today()
    #     age = (today - ages) // datetime.timedelta(days=365.2425)
    #     user = Age.objects.create(age=dates,agecalc=f"Your Age is {age}")
    #     user.save()
    #     return user
    
    def create(self, validated_data):
            
        dates=validated_data['age']
        year=dates.split('/')
        yys=year[2]
        
        mms=year[1]
        dds=year[0]
        ages = datetime.date(int(yys), int(mms), int(dds))
        
        today = datetime.date.today()
        age = today - ages
        years = age.days // 365
        months = (age.days % 365) // 30
        days = (age.days % 365) % 30
        # today = datetime.date.today()
        # age = (today - ages) // datetime.timedelta(days=365.2425)
        print(f"Age: {years} years, {months} months, {days} days")

        user = Age.objects.create(age=dates,agecalc=f"Your Age is {years} years, {months} months, {days} days")
        user.save()
        return user
    
    
    #   def create(self, validated_data):
            
    #     date=validated_data['age']
   
    #     year=date.split('/')
     
    #     age = 2024 - int(year[2])
    #     user = Age.objects.create(age=date,agecalc=f"Your Age is {age}")
    #     user.save()
    #     return user
    
    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
        
       
    #     selected_fields = {
    #         'age': instance.age,
           
           
    #     }
    #     data.update(selected_fields)

    #     return data
        

class UserSeralizer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password']
    
    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

class StudentSerealizer(serializers.ModelSerializer):
    
    class Meta:
        model=Student
        fields='__all__'
        # fields = ['name','email']
        # exclude = ['age']
    
    def validate(self, data):

        if data['age']<18:
           raise serializers.ValidationError("Age must be more than 18")
        
        return data

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields= '__all__'

class ProductSerializer(serializers.ModelSerializer):
    # category = CategorySerializer()
    class Meta:
        model=Product
        fields='__all__'
        # depth=1
    
    # category = CategorySerializer()
    def to_representation(self, instance):
       self.fields['category'] =  CategorySerializer(read_only=True)
       return super(ProductSerializer, self).to_representation(instance)
    
class UserSeralizer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password']
    
    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    
    
    
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields= '__all__'
        
        
class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields= '__all__'
        
    def to_representation(self, instance):
        self.fields['author'] =  AuthorSerializer(read_only=True)
        return super(PublisherSerializer, self).to_representation(instance)
        
        
class BookSerializer(serializers.ModelSerializer):
   
    class Meta:
        model=Book
        fields='__all__'
           
  
    def to_representation(self, instance):
       self.fields['author'] =  AuthorSerializer(read_only=True)
       self.fields['publisher'] =  PublisherSerializer(read_only=True)
       return super(BookSerializer, self).to_representation(instance)
   
   
   
   
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        # fields= '__all__'
        exclude=['id']
        
class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        # fields= '__all__'
        # fields=['statename']
        exclude=['id']
        
    def to_representation(self, instance):
       self.fields['country'] =  CountrySerializer(read_only=True)
       return super(StateSerializer, self).to_representation(instance)
   
   
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields= '__all__'
        
    def to_representation(self, instance):
       self.fields['state'] =  StateSerializer(read_only=True)
       return super(CitySerializer, self).to_representation(instance)
   
   
class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields= '__all__'
        
    def to_representation(self, instance):
       self.fields['country'] =  CountrySerializer(read_only=True)
       self.fields['state'] =  StateSerializer(read_only=True)
       self.fields['city'] =  CitySerializer(read_only=True)
       return super(AreaSerializer, self).to_representation(instance)