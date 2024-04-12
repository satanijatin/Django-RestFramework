from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import *
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authtoken.models import Token

# Create your views here.

def index(request):
    return render(request,"index.html")


class RegisterUser(APIView):
     def post(self,request):
        user = UserSeralizer(data=request.data)
        if not user.is_valid():
                return Response({'status':'202','errors':user.errors,'message':"something went wrong"})
        user.save()
        udata = User.objects.get(username=request.data['username'])
        refresh = RefreshToken.for_user(udata)
        
        return Response({"data":user.data, 'refresh': str(refresh),
        'access': str(refresh.access_token),"message":"User inserted"})
        
class ProductAPI(APIView):
    def get(self,request):
        prodata = Product.objects.all()
        seralizer = ProductSerializer(prodata,many=True)
        return Response({'apidata':seralizer.data})

    def post(self,request):
            prodata =  ProductSerializer(data=request.data)
            if not prodata.is_valid():
                return Response({'status':'202','errors':prodata.errors,'message':"something went wrong"})
            prodata.save()
            return Response({"data":prodata.data,"message":"Product inserted"})

    def put(self,request):
        try:
            pdata = Product.objects.get(id=request.data['id'])
            psdata =  ProductSerializer(pdata,request.data)

            if not psdata.is_valid():
                return Response({'status':'202','errors':psdata.errors,'message':"something went wrong"})  
            
            psdata.save()
            return Response({"data":psdata.data,"message":"Product Updated"})
        except Exception as e:
            return Response({"message":"Id not found"})

    def delete(self,request):
        try:
              pdata = Product.objects.get(id=request.data['id'])
              pdata.delete()
              return Response({"message":"Product Delete"})
        except Exception as e:
            return Response({"message":"Id not found"})
        
        
class CategoryAPI(APIView):
    def get(self,request):
            catdata = Category.objects.all()
            seralizer = CategorySerializer(catdata,many=True)
            return Response({'apidata':seralizer.data})

    def post(self,request):
            catdata =  CategorySerializer(data=request.data)
            if not catdata.is_valid():
                return Response({'status':'202','errors':catdata.errors,'message':"something went wrong"})
            catdata.save()
            return Response({"data":catdata.data,"message":"Category inserted"})

    def put(self,request):
        try:
            pdata = Category.objects.get(id=request.data['id'])
            psdata =  CategorySerializer(pdata,request.data)

            if not psdata.is_valid():
                return Response({'status':'202','errors':psdata.errors,'message':"something went wrong"})  
            
            psdata.save()
            return Response({"data":psdata.data,"message":"Category Updated"})
        except Exception as e:
            return Response({"message":"Id not found"})

    def delete(self,request):
        try:
              pdata = Category.objects.get(id=request.data['id'])
              pdata.delete()
              return Response({"message":"Category Delete"})
        except Exception as e:
            return Response({"message":"Id not found"})
        
        
class CartAPI(APIView):
    def get(self,request):
        try:
            catdata = Cart.objects.filter(user=request.data['id'])
            seralizer = CartSerializer(catdata,many=True)
            return Response({'apidata':seralizer.data})
        except Exception as e:
            return Response({"message":"Userid not found"})

    def post(self,request):
            catdata =  CartSerializer(data=request.data)
            if not catdata.is_valid():
                return Response({'status':'202','errors':catdata.errors,'message':"something went wrong"})
            
            
            catdata.save()
            return Response({"data":catdata.data,"message":"Cart inserted"})

    def put(self,request):
        try:
            pdata = Cart.objects.get(id=request.data['id'])
            psdata =  CartSerializer(pdata,request.data)

            if not psdata.is_valid():
                return Response({'status':'202','errors':psdata.errors,'message':"something went wrong"})  
            
            psdata.save()   
            return Response({"data":psdata.data,"message":"Cart Updated"})
        except Exception as e:
            return Response({"message":"Id not found"})

    def delete(self,request):
        try:
              pdata = Cart.objects.get(id=request.data['id'])
              pdata.delete()
              return Response({"message":"Cart Delete"})
        except Exception as e:
            return Response({"message":"Id not found"})
