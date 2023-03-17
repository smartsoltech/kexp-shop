from django.shortcuts import render
from django.http import HttpResponse
import datetime
import os
from .models import *
import requests

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def index(request):
    product_name = Product.objects.all()
    return render(request, 'catalog/index.html', {'product_name': product_name})
def about(request):
    return render(request, 'catalog/about.html')
def contacts(request):
    return render(request, 'catalog/contacts.html')
    