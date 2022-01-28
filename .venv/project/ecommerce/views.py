from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')
    #return HttpResponse("Hello, SOEN 341 Group!")

def login(request):
    return render(request, 'login.html')