from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.db.models import Sum



class UserSeralizer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password']
    
    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class User1Seralizer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username']

    
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields= '__all__'

class ProductSerializer(serializers.ModelSerializer):
   
    class Meta:
        model=Product
        fields=['pname']   
  
    def to_representation(self, instance):
       self.fields['category'] =  CategorySerializer(read_only=True)
       return super(ProductSerializer, self).to_representation(instance)

class CartSerializer(serializers.ModelSerializer):
    class Meta:
            model=Cart
            fields='__all__' 
            
    def to_representation(self, instance):
            resp = super().to_representation(instance)
            resp['user'] = User1Seralizer(instance.user).data
            resp['product'] = ProductSerializer(instance.product).data
            return resp
    
    def create(self, validated_data):
                              
                    
        product_id = validated_data['product'].pk
        qty = validated_data['qty']
        user_id = validated_data['user'].pk
                 
        select_cart1 = Cart.objects.filter(user=user_id,product=product_id).first()
        if select_cart1 is not None:
             select_cart1.qty = qty
             select_cart1.save()
        else:
                        
             select_cart= Cart.objects.create(qty=qty,
                                                user_id=user_id,
                                                product_id=product_id)
                        
        return select_cart              
                    
    def validate(self, attrs):
            product_id = attrs['product'].pk
            qty = attrs['qty']
            # user_id = attrs['user'].pk
            # user=User.objects.get(id=user_id)
            
            # if user is not None:
                
            total_qty_added = Cart.objects.filter(product=product_id).aggregate(Sum('qty'))
            if total_qty_added['qty__sum'] is not None:
                   
                    qty1 = int(total_qty_added['qty__sum']) + qty
                    
            else:
                    qty1 = qty
               
            select_p = Product.objects.get(id=product_id)
            if select_p.qty >= qty1:
                    return attrs
            else:
                    raise serializers.ValidationError("quntity not added")
            # else:
            #     raise serializers.ValidationError("user not exist")
                    
        
     
                        
               
                
           
       
    
   