import datetime
from django.http import HttpResponse
from django.shortcuts import render

from tryhello.models import Student

# Create your views here.
def helloworld(request,name):
    s1 = Student(name=name,age=10,dob=datetime.date.today())
    s1.save() # until and unless we save it it will not reflected in db.
    return HttpResponse("Hello " + name)