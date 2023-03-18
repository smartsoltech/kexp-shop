from django.shortcuts import render
import datetime
import os
from .models import *
import requests
from django.views.generic import DetailView


class ProductDetailView(DetailView):
    model = Product
    template_name = './catalog/productdetail.html'
    context_object_name = 'product'
 
class SupplierInfo(DetailView):
    model = Supplier
    template_name = './catalog/productdetail.html'
    context_object_name = 'supplier'    
    
    
def index(request):
    product_name = Product.objects.all()
    return render(request, 'catalog/index.html', {'product_name': product_name})
def about(request):
    return render(request, 'catalog/about.html')
def contacts(request):
    return render(request, 'catalog/contacts.html')
    