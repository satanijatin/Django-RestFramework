from faker import Faker
fake = Faker()
from .models import *
import random
from django.db.models import *


def setmarks():

    students = Student.objects.all()
    for std in students:
        subjects = Subject.objects.all()
        for sub in subjects:
            SubjectMarks.objects.create(
                student = std,
                subject = sub,
                marks = random.randint(0,100)
            )


def setdata(n = 10):

    for i in range(n):
        dept_data = Department.objects.all()
        r_index = random.randint(0,len(dept_data)-1)
        dept = dept_data[r_index]
        name = fake.name()
        email = fake.email()

        student_id = f"STD_{random.randint(100,999)}"
        student_id_obj =  StudentId.objects.create(student_id = student_id)

        Student.objects.create(
            name = name,
            email = email,
            department = dept,
            student_id = student_id_obj 
        )
        
        
def generate_report_card():
    current_rank = -1
    ranks = Student.objects.annotate(
        marks=Sum('marks')).order_by('-marks')
    i = 1
 
    for rank in ranks:
        ReportCard.objects.create(
            student=rank,
            student_rank=i
        )
        i = i + 1