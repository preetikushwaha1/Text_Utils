from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello(request):
    return render(request,'Home.html',{"name":"preeti"})

def addition(request):

    val1 = request.POST["num1"]
    val2 = request.POST["num2"]
    res = int(val1)+ int(val2)
    return render(request, "Result.html",{'result':res})

