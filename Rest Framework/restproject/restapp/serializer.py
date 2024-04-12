from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


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