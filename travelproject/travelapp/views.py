from django.shortcuts import render
from django.http import HttpResponse
from .models import Place,Team
# Create your views here.


def demo(request):
    obj=Place.objects.all()
    obj1=Team.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})

def about(request):
    return render(request,"about.html")

# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     return render(request,"result.html",{'result':res})

def contact(request):
    return HttpResponse("Hello, I am contact")

