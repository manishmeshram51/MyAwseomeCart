from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
import math

def index(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
    nSlides = n//4 + math.ceil((n/4)-(n//4))
    allProds = []
    # catprods = Product.objects.values('category', 'id')
    # cats = {item['category'] for item in catprods}
    # for cat in cats:
    #     prod = Product.objects.filter(category=cat)
    #     n = len(prod)
    #     nSlides = n // 4 + ceil((n / 4) - (n // 4))
    #     allProds.append([prod, range(1, nSlides), nSlides])


    allProds = [[products, range(1, nSlides), nSlides],
                [products, range(1, nSlides), nSlides]]
    params = {'allProds':allProds}
    return render(request, 'shop/index.html', params)

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