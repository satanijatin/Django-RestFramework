from django.contrib import admin
from .models import *
# Register your models here.

class studentadmin(admin.ModelAdmin):
    list_display = ['name','email','department','student_id']

class subjectmarksadmin(admin.ModelAdmin):
    list_display = ['student','subject','marks']

admin.site.register(Department)
admin.site.register(StudentId)
admin.site.register(Student,studentadmin)
admin.site.register(Subject)
admin.site.register(SubjectMarks,subjectmarksadmin)