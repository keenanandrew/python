from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# this function represents a view; it returns "Hello, folks" as an http response
def index(request):
    return HttpResponse("Hello there, folks!")

def andrew(request):
    return HttpResponse("Hello, Andrew")
