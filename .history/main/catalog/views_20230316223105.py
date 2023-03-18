from django.shortcuts import render
from django.http import HttpResponse
import datetime
import os
from .models import *

def get_product():
    
    return render(request, 'template/catalog.base.html', {})

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def index(request):
    product_name = Product.objects.all()
    return render(request, 'catalog/index.html', {'product_name': product_name})
def about(request):
    return HttpResponse(render(request, 'catalog/about.html'))
def contacts(request):
    return HttpResponse(render(request, 'catalog/contacts.html'))
    