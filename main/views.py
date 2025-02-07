from django.shortcuts import render
from .models import Product
# Create your views here.

def product_list(request):
    products = Product.objects.filter()[:16]
    return render(request, "main/index.html",
                  {"products": products})

def product_detail(request, slug):
    pass


