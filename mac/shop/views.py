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
    return HttpResponse("tracker")

def search(request):
    return HttpResponse("search")

def prodView(request):
    return HttpResponse("prd view")

def checkout(request):
    return HttpResponse("checkout")

def register(request):
    return HttpResponse("reg")

def login(request):
    return HttpResponse("login")

def cart(request):
    return HttpResponse("cart")

def wishlist(request):
    return HttpResponse("wishlist")