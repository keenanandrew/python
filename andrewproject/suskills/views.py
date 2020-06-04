from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# this function represents a view; it returns "Hello, folks" as an http response
def index(request):
    return render(request, "suskills/index.html")
    # renders an html page, which can be edited with variables etc

def suskills(request):
    return HttpResponse("Hello, Andrew")

def greet(request, name):
    # the {} contents are the 'context' - all of the info/variables being provided to the template
    return render(request, "suskills/greet.html", {
        "name": name.capitalize()    
    })
