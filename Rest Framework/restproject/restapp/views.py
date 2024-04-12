from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student
from .serializer import *
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authtoken.models import Token


# Create your views here.

class GetAccessTokenView(APIView):
    permission_classes = [IsAuthenticated]  

    def post(self, request, *args, **kwargs):
        user = request.user
        token, created = Token.objects.get_or_create(user=user)
        return Response({'access_token': token.key})

class RregisterUser(APIView):
     def post(self,request):
        user = UserSeralizer(data=request.data)
        if not user.is_valid():
                return Response({'status':'202','errors':user.errors,'message':"something went wrong"})
        user.save()
        udata = User.objects.get(username=request.data['username'])
        refresh = RefreshToken.for_user(udata)
        
        return Response({"data":user.data, 'refresh': str(refresh),
        'access': str(refresh.access_token),"message":"Student inserted"})



class StudentAPI(APIView):
    
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        studentdata = Student.objects.all()
        seralizer = StudentSerealizer(studentdata,many=True)
        return Response({'apidata':seralizer.data})

    def post(self,request):
            sdata =  StudentSerealizer(data=request.data)
            if not sdata.is_valid():
                return Response({'status':'202','errors':sdata.errors,'message':"something went wrong"})
            sdata.save()
            return Response({"data":sdata.data,"message":"Student inserted"})

    def put(self,request):
        try:
            sdata = Student.objects.get(id=request.data['id'])
            sdata =  StudentSerealizer(sdata,request.data)

            if not sdata.is_valid():
                return Response({'status':'202','errors':sdata.errors,'message':"something went wrong"})  
            
            sdata.save()
            return Response({"data":sdata.data,"message":"Student Updated"})
        except Exception as e:
            return Response({"message":"Id not found"})

    def delete(self,request):
        try:
              sdata = Student.objects.get(id=request.data['id'])
              sdata.delete()
              return Response({"message":"Student Delete"})
        except Exception as e:
            return Response({"message":"Id not found"})


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
        
        
class AuthorAPI(APIView):
    def get(self,request):
            authdata = Author.objects.all()
            seralizer = AuthorSerializer(authdata,many=True)
            return Response({'apidata':seralizer.data})

    def post(self,request):
            authdata =  AuthorSerializer(data=request.data)
            if not authdata.is_valid():
                return Response({'status':'202','errors':authdata.errors,'message':"something went wrong"})
            authdata.save()
            return Response({"data":authdata.data,"message":"Author inserted"})

    def put(self,request):
        try:
            pdata = Author.objects.get(id=request.data['id'])
            psdata =  AuthorSerializer(pdata,request.data)

            if not psdata.is_valid():
                return Response({'status':'202','errors':psdata.errors,'message':"something went wrong"})  
            
            psdata.save()
            return Response({"data":psdata.data,"message":"Author Updated"})
        except Exception as e:
            return Response({"message":"Id not found"})

    def delete(self,request):
        try:
              pdata = Author.objects.get(id=request.data['id'])
              pdata.delete()
              return Response({"message":"Author Delete"})
        except Exception as e:
            return Response({"message":"Id not found"})
        
        
        
class PublisherAPI(APIView):
    def get(self,request):
            authdata = Publisher.objects.all()
            seralizer = PublisherSerializer(authdata,many=True)
            return Response({'apidata':seralizer.data})

    def post(self,request):
            authdata =  PublisherSerializer(data=request.data)
            if not authdata.is_valid():
                return Response({'status':'202','errors':authdata.errors,'message':"something went wrong"})
            authdata.save()
            return Response({"data":authdata.data,"message":"Publisher inserted"})

    def put(self,request):
        try:
            pdata = Publisher.objects.get(id=request.data['id'])
            psdata =  PublisherSerializer(pdata,request.data)

            if not psdata.is_valid():
                return Response({'status':'202','errors':psdata.errors,'message':"something went wrong"})  
            
            psdata.save()
            return Response({"data":psdata.data,"message":"Publisher Updated"})
        except Exception as e:
            return Response({"message":"Id not found"})

    def delete(self,request):
        try:
              pdata = Publisher.objects.get(id=request.data['id'])
              pdata.delete()
              return Response({"message":"Publisher Delete"})
        except Exception as e:
            return Response({"message":"Id not found"})
        
        
class BookAPI(APIView):
    def get(self,request):
            authdata = Book.objects.all()
            seralizer = BookSerializer(authdata,many=True)
            return Response({'apidata':seralizer.data})

    def post(self,request):
            authdata =  BookSerializer(data=request.data)
            if not authdata.is_valid():
                return Response({'status':'202','errors':authdata.errors,'message':"something went wrong"})
            authdata.save()
            return Response({"data":authdata.data,"message":"Book inserted"})

    def put(self,request):
        try:
            pdata = Book.objects.get(id=request.data['id'])
            psdata =  BookSerializer(pdata,request.data)

            if not psdata.is_valid():
                return Response({'status':'202','errors':psdata.errors,'message':"something went wrong"})  
            
            psdata.save()
            return Response({"data":psdata.data,"message":"Book Updated"})
        except Exception as e:
            return Response({"message":"Id not found"})

    def delete(self,request):
        try:
              pdata = Book.objects.get(id=request.data['id'])
              pdata.delete()
              return Response({"message":"Book Delete"})
        except Exception as e:
            return Response({"message":"Id not found"})
        
        
class CountryAPI(APIView):
    def get(self,request):
            authdata = Country.objects.all()
            seralizer = CountrySerializer(authdata,many=True)
            return Response({'apidata':seralizer.data})

    def post(self,request):
            authdata =  CountrySerializer(data=request.data)
            if not authdata.is_valid():
                return Response({'status':'202','errors':authdata.errors,'message':"something went wrong"})
            authdata.save()
            return Response({"data":authdata.data,"message":"Country inserted"})

    def put(self,request):
        try:
            pdata = Country.objects.get(id=request.data['id'])
            psdata =  CountrySerializer(pdata,request.data)

            if not psdata.is_valid():
                return Response({'status':'202','errors':psdata.errors,'message':"something went wrong"})  
            
            psdata.save()
            return Response({"data":psdata.data,"message":"Country Updated"})
        except Exception as e:
            return Response({"message":"Id not found"})

    def delete(self,request):
        try:
              pdata = Country.objects.get(id=request.data['id'])
              pdata.delete()
              return Response({"message":"Country Delete"})
        except Exception as e:
            return Response({"message":"Id not found"})     
        
        
class StateAPI(APIView):
    def get(self,request):
            authdata = State.objects.all()
            seralizer = StateSerializer(authdata,many=True)
            return Response({'apidata':seralizer.data})

    def post(self,request):
            authdata =  StateSerializer(data=request.data)
            if not authdata.is_valid():
                return Response({'status':'202','errors':authdata.errors,'message':"something went wrong"})
            authdata.save()
            return Response({"data":authdata.data,"message":"State inserted"})

    def put(self,request):
        try:
            pdata = State.objects.get(id=request.data['id'])
            psdata =  StateSerializer(pdata,request.data)

            if not psdata.is_valid():
                return Response({'status':'202','errors':psdata.errors,'message':"something went wrong"})  
            
            psdata.save()
            return Response({"data":psdata.data,"message":"State Updated"})
        except Exception as e:
            return Response({"message":"Id not found"})

    def delete(self,request):
        try:
              pdata = State.objects.get(id=request.data['id'])
              pdata.delete()
              return Response({"message":"State Delete"})
        except Exception as e:
            return Response({"message":"Id not found"})
        
class CityAPI(APIView):
    def get(self,request):
            authdata = City.objects.all()
            seralizer = CitySerializer(authdata,many=True)
            return Response({'apidata':seralizer.data})

    def post(self,request):
            authdata =  CitySerializer(data=request.data)
            if not authdata.is_valid():
                return Response({'status':'202','errors':authdata.errors,'message':"something went wrong"})
            authdata.save()
            return Response({"data":authdata.data,"message":"City inserted"})

    def put(self,request):
        try:
            pdata = City.objects.get(id=request.data['id'])
            psdata =  CitySerializer(pdata,request.data)

            if not psdata.is_valid():
                return Response({'status':'202','errors':psdata.errors,'message':"something went wrong"})  
            
            psdata.save()
            return Response({"data":psdata.data,"message":"City Updated"})
        except Exception as e:
            return Response({"message":"Id not found"})

    def delete(self,request):
        try:
              pdata = City.objects.get(id=request.data['id'])
              pdata.delete()
              return Response({"message":"City Delete"})
        except Exception as e:
            return Response({"message":"Id not found"})
        
        
        
class StateAPI(APIView):
    def get(self,request):
            authdata = State.objects.all()
            seralizer = StateSerializer(authdata,many=True)
            return Response({'apidata':seralizer.data})

    def post(self,request):
            authdata =  StateSerializer(data=request.data)
            if not authdata.is_valid():
                return Response({'status':'202','errors':authdata.errors,'message':"something went wrong"})
            authdata.save()
            return Response({"data":authdata.data,"message":"State inserted"})

    def put(self,request):
        try:
            pdata = State.objects.get(id=request.data['id'])
            psdata =  StateSerializer(pdata,request.data)

            if not psdata.is_valid():
                return Response({'status':'202','errors':psdata.errors,'message':"something went wrong"})  
            
            psdata.save()
            return Response({"data":psdata.data,"message":"State Updated"})
        except Exception as e:
            return Response({"message":"Id not found"})

    def delete(self,request):
        try:
              pdata = State.objects.get(id=request.data['id'])
              pdata.delete()
              return Response({"message":"State Delete"})
        except Exception as e:
            return Response({"message":"Id not found"})
        
class AreaAPI(APIView):
    def get(self,request):
            authdata = Area.objects.all()
            seralizer = AreaSerializer(authdata,many=True)
            return Response({'apidata':seralizer.data})

    def post(self,request):
            authdata =  AreaSerializer(data=request.data)
            if not authdata.is_valid():
                return Response({'status':'202','errors':authdata.errors,'message':"something went wrong"})
            authdata.save()
            return Response({"data":authdata.data,"message":"Area inserted"})

    def put(self,request):
        try:
            pdata = Area.objects.get(id=request.data['id'])
            psdata =  AreaSerializer(pdata,request.data)

            if not psdata.is_valid():
                return Response({'status':'202','errors':psdata.errors,'message':"something went wrong"})  
            
            psdata.save()
            return Response({"data":psdata.data,"message":"Area Updated"})
        except Exception as e:
            return Response({"message":"Id not found"})

    def delete(self,request):
        try:
              pdata = Area.objects.get(id=request.data['id'])
              pdata.delete()
              return Response({"message":"Area Delete"})
        except Exception as e:
            return Response({"message":"Id not found"})