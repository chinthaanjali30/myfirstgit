from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HTTPResponse('<h1>This is app1 first view</h1>'),


