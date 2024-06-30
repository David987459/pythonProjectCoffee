from django.http import HttpResponse
from django.shortcuts import render

from orders.models import Product


# Create your views here.


def home(request):
    return render(request, 'home.html', {'title': 'Welcome to CaffeShop'})


def products(request):
    return render(request, 'products.html', {'products': Product.objects.all()})


def o_nas(request):
    return render(request, 'o_nas.html')
