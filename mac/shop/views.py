from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def index(request):
    prd = Product.objects.all()
    print(prd)
    context = {'prd': prd}
    return render(request,'shop/index.html',context)

def about(request):
    return render(request,'shop/about.html')


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