from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
import math

def index(request):
    products = Product.objects.all()
    
    n = len(products)

    nSlides = n//4 + math.ceil((n/4)-(n//4))
    print(n, nSlides)
    params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    return render(request,'shop/index.html',params)

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