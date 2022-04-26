from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'blog/login.html')


def dashboard(request):
    return render(request, 'blog/login.html')


def signup(request):
    return render(request, 'blog/login.html')


def search(request):
    return render(request, 'blog/login.html')


def vedio(request):
    return render(request, 'blog/login.html')
