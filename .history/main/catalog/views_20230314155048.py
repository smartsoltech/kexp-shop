from django.shortcuts import render
from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def index(request):
    return HttpResponse(render(request, 'catalog/index.html'))
def about(request):
    return HttpResponse(render(request, 'catalog/about.html'))
def contacts(request):
    return HttpResponse(render(request, 'catalog/contacts.html'))
    