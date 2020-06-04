from django.urls import path
from . import views # import views from current directory

urlpatterns = [
    path("", views.index, name="index"),
    path("suskills", views.suskills, name="suskills"), # the index function I created in views.py
    path("<str:name>", views.greet, name="greet")
]
