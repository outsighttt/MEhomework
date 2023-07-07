from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Дз по 4 занятию')
