from django.shortcuts import render,HttpResponse
from .models import *
from django.http import JsonResponse
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request,"index.html")

def display(request):
    user_data = User.objects.all()
    return JsonResponse({"data":list(user_data.values())})

def adduser(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        email = request.POST['email']
        phone = request.POST['phone']
        print(uname)
        User.objects.create(uname=uname,email=email,phone=phone)
    
    return HttpResponse("Data inserted...")

def delete(request):
    id = request.GET['uid']
    user_data = User.objects.get(id=id)
    user_data.delete()
    return HttpResponse("User deleted")

def edit(request):
    id = request.GET['uid']
    user_data = User.objects.filter(id=id)
   
    return JsonResponse({"udata":list(user_data.values())})


def update(request):
    user_data = User.objects.get(id=request.POST['id'])

    user_data.uname = request.POST['uname']
    user_data.email = request.POST['email']
    user_data.phone = request.POST['phone']
    user_data.save()
    return HttpResponse("User updated")

def search(request):
    data = request.GET['data']
    user_data = User.objects.filter(
        Q(uname__startswith=data) |
        Q(email__startswith=data) |
        Q(phone__startswith=data)  )
    return JsonResponse({"data":list(user_data.values())})