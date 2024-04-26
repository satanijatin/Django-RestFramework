from django.shortcuts import render,redirect
from .models import *
from django.core.paginator import Paginator
from django.db.models import Sum
from django.db.models import Q
from io import BytesIO
from django.core.mail import send_mail
from django.template.loader import get_template


# Create your views here.
def index(request):
#     if request.method=="POST":
#             name = request.POST['name']
#             email = request.POST['email']
#             department = request.POST['department']

                
#             q_objects = Q()
    
#             if name!="":
#                     q_objects &= Q(name__icontains=name)
#             if email!="":
#                     q_objects &= Q(email__icontains=email)
#             if department!="":
#                     q_objects &= Q(department__dept_name__icontains=department)
              
            
            
#             datas = Student.objects.filter(q_objects) 
            
#             paginator = Paginator(datas, 2)  

#             page_number = request.GET.get("page",1)
#             page_obj = paginator.get_page(page_number)
#             context =  {
#                         'queryset':page_obj
                
#                     }
           
#             return render(request, 'index.html', context)    
#     else:
        queryset = Student.objects.all()

        paginator = Paginator(queryset, 10)  

        page_number = request.GET.get("page",1)
        page_obj = paginator.get_page(page_number)


        return render(request,'index.html',{"queryset":page_obj})

def marks(request,id):       
    ranks =  Student.objects.annotate(marks = Sum('subjectmarks__marks')).order_by('-marks')
    i = 1;
    current_rank = 0;
    for rank in ranks:
       
        if rank.student_id.student_id==id:
            
            current_rank = i;
            
        i = i+1;

    
    queryset = SubjectMarks.objects.filter(student__student_id__student_id = id)
    total =  queryset.aggregate(total = Sum('marks'))
    

    return render(request,'card.html',{'queryset':queryset, 'total':total,'rank':current_rank,'id':id})


from django.template.loader import render_to_string

from django.core.mail import EmailMessage

def sendstudentmarksemail(request,id):
        
        ranks =  Student.objects.annotate(marks = Sum('subjectmarks__marks')).order_by('-marks')
        i = 1
        current_ranks = 0
        for rank in ranks:
       
                if rank.student_id.student_id==id:
                     current_ranks = i;
            
                i = i+1;
        queryset = SubjectMarks.objects.filter(student__student_id__student_id = id)
        total =  queryset.aggregate(total = Sum('marks'))
        students=Student.objects.get(student_id__student_id = id)
        
                   
        html_content = render_to_string('cards.html', {'queryset': queryset, 'total': total,'rank':current_ranks})

    
        email = EmailMessage(
        subject= f'Hi {students.name} Your Progerss Report',
        body=html_content,
        from_email='jatinsatani111@gmail.com',
        to=[students.email],
        )
        email.content_subtype = 'html' 

        email.send()
                   
      
        return  redirect('/') 
