from django.shortcuts import render

# sample tasks
tasks = ["foo", "bar", "baz"]

# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks # a key and a value - same word but different 'things'
    })

def add(request):
    return render(request, "tasks/add.html")
