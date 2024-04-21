from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from django.db.models import Sum
from django.db.models import Q
# Create your views here.
def index(request):
    if request.method=="POST":
            name = request.POST['name']
            email = request.POST['email']
            department = request.POST['department']

                
            q_objects = Q()
    
            if name!="":
                    q_objects &= Q(name__icontains=name)
            if email!="":
                    q_objects &= Q(email__icontains=email)
            if department!="":
                    q_objects &= Q(department__dept_name__icontains=department)
              
            
            
            datas = Student.objects.filter(q_objects) 
            
            paginator = Paginator(datas, 2)  

            page_number = request.GET.get("page",1)
            page_obj = paginator.get_page(page_number)
            context =  {
                        'queryset':page_obj
                
                    }
           
            return render(request, 'index.html', context)    
    else:
        queryset = Student.objects.all()

        paginator = Paginator(queryset, 2)  

        page_number = request.GET.get("page",1)
        page_obj = paginator.get_page(page_number)


        return render(request,'index.html',{"queryset":page_obj})

def marks(request,id):       
        queryset = SubjectMarks.objects.filter(student__student_id__student_id = id)
        total =  queryset.aggregate(total = Sum('marks'))
        return render(request,'card.html',{'queryset':queryset, 'total':total})