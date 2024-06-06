from django.shortcuts import render
from django.http import HttpResponse


def principal(request):
    return request("gerenciador\indext.html")