from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request,'shop/index.html')

def about(request):
    return HttpResponse("About us")

def contact(request):
    return HttpResponse("contact us")

def tracker(request):
    return HttpResponse("About us")

def search(request):
    return HttpResponse("About us")

def prodView(request):
    return HttpResponse("About us")

def checkout(request):
    return HttpResponse("About us")