from django.shortcuts import render
from django.http import HttpResponse
from .models import Advertisements

def index(request):
    advertisemenets=Advertisements.objects.all()
    context = {'advertisements': advertisemenets}
    return render(request, 'index.html', context)

def top_sellers(request):
    return render(request, 'top-sellers.html')

def advertisement_post(request):
    return render(request, 'advertisement-post.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def profile(request):
    return render(request, 'profile.html')
