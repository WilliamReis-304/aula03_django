from django.shortcuts import render
from django.http import HttpResponse


def principal(request):
    return render(request,"gerenciador/paginas/index.html")

def home(request):
    return render(request,'gerenciador/paginas/home.html')